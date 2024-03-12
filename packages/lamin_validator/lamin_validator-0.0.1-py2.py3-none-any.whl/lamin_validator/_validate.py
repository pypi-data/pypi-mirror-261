from typing import Dict, Optional

import bionty as bt
import lamindb as ln
from anndata import AnnData
from lamin_utils import colors, logger
from lamindb._from_values import _print_values
from lnschema_core import Registry
from lnschema_core.types import FieldAttr

ONTOLOGY_DEFAULTS_HINT = {
    "disease": ("normal", "lb.Disease.lookup()"),
    "development_stage": ("unknown", "lb.DevelopmentStage.lookup()"),
    "self_reported_ethnicity": ("unknown", "lb.Ethnicity.lookup()"),
    "suspension_type": ("cell", '"cell" or "nucleus" or "na"'),
    "donor_id": ("na", "ln.ULabel.filter(name='is_donor').one().children.lookup()"),
    "tissue_type": ("tissue", '"tissue" or "organoid" or "cell culture"'),
    "cell_type": ("native_cell", "lb.CellType.lookup()"),
}


VALIDATED_COLUMNS_ORDERED = [
    "assay",
    "assay_ontology_term_id",
    "cell_type",
    "cell_type_ontology_term_id",
    "development_stage",
    "development_stage_ontology_term_id",
    "disease",
    "disease_ontology_term_id",
    "donor_id",
    "self_reported_ethnicity",
    "self_reported_ethnicity_ontology_term_id",
    "sex",
    "sex_ontology_term_id",
    "suspension_type",
    "tissue",
    "tissue_ontology_term_id",
    "tissue_type",
    "organism",
    "organism_ontology_term_id",
]


def _registry_using(registry: Registry, using: Optional[str] = None) -> Registry:
    """Get a registry instance using a specific instance."""
    return (
        registry.using(using) if using is not None and using != "default" else registry
    )


def _inspect_obs(
    adata: AnnData,
    obs_fields: Dict[str, FieldAttr],
    add_labels: bool = False,
    using: Optional[str] = None,
    verbosity: str = "hint",
):
    """Inspect ontology terms in an AnnData object using LaminDB registries."""
    ln.settings.verbosity = verbosity

    def inspect_ontology_terms(
        adata,
        feature_name: str,
        field: FieldAttr,
        using: Optional[str] = None,
    ):
        """Validate ontology terms in a pandas series using LaminDB registries."""
        values = adata.obs[feature_name].unique()
        registry = _registry_using(field.field.model, using)
        inspect_result = registry.inspect(values, field=field, mute=True)
        # if all terms are validated
        n_non_validated = len(inspect_result.non_validated)
        if n_non_validated == 0:
            validated = True
            logger.success(f"all {feature_name}s are validated")
        else:
            are = "are" if n_non_validated > 1 else "is"
            print_values = _print_values(inspect_result.non_validated)
            feature_name_print = f"`.register_labels('{feature_name}')`"
            logger.warning(
                f"{colors.yellow(f'{n_non_validated} terms')} {are} not validated: {colors.yellow(print_values)}\n      → register terms via {colors.red(feature_name_print)}"
            )
            validated = False
        return validated

    # start validation
    validated = True
    for feature_name, field in obs_fields.items():
        logger.indent = ""
        logger.info(f"inspecting '{colors.bold(feature_name)}' by {field.field.name}")
        logger.indent = "   "
        validated &= inspect_ontology_terms(
            adata, feature_name=feature_name, field=field, using=using
        )
        logger.indent = ""

    # re-order columns
    if validated and add_labels:
        additional_cols = [i for i in adata.obs.columns if i not in obs_fields.keys()]
        adata.obs = adata.obs[list(obs_fields.keys()) + additional_cols]

    return validated


def _inspect_var(
    adata: AnnData,
    field: FieldAttr,
    organism: str,
    using: Optional[str] = "default",
    verbosity: str = "hint",
):
    """Inspect features in .var using LaminDB registries."""
    model_field = f"{field.field.model.__name__}.{field.field.name}"
    ln.settings.verbosity = verbosity
    logger.indent = ""
    logger.info(f"inspecting variables by {model_field}")
    logger.indent = "   "
    # inspect the values, validate and make suggestions to fix
    registry = _registry_using(field.field.model, using)
    inspect_result = registry.inspect(
        adata.var.index, field=field, organism=organism, mute=True
    )
    n_non_validated = len(inspect_result.non_validated)
    if n_non_validated == 0:
        logger.success(f"all {organism} variables are validated!")
        validated = True
    else:
        are = "are" if n_non_validated > 1 else "is"
        print_values = _print_values(inspect_result.non_validated)
        logger.warning(
            f"{colors.yellow(f'{n_non_validated} variables')} {are} not validated: {colors.yellow(print_values)}\n      → register variables via {colors.red('`.register_variables()`')}"
        )
        validated = False
    logger.indent = ""
    return validated


def validate(
    adata,
    organism: str,
    var_field: FieldAttr,
    obs_fields: Dict[str, FieldAttr],
    using: Optional[str] = None,
    verbosity: str = "hint",
    **kwargs,
) -> bool:
    """Inspect metadata in an AnnData object using LaminDB registries."""
    if using is not None and using != "default":
        logger.important(f"validating metadata using registries of instance `{using}`")

    validated_var = _inspect_var(
        adata,
        field=var_field,
        organism=organism,
        using=using,
        verbosity=verbosity,
    )
    validated_obs = _inspect_obs(
        adata,
        obs_fields=obs_fields,
        using=using,
        verbosity=verbosity,
        **kwargs,
    )
    return validated_var & validated_obs
