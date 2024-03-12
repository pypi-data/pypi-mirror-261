from pathlib import Path
from typing import Dict, List, Optional, Union

import anndata as ad
import lamindb as ln
import lnschema_bionty as lb
from lamin_utils import colors, logger
from lnschema_core.types import FieldAttr

from ._register import register
from ._validate import _registry_using, validate


def register_labels_in_default_from_using(
    values: List[str],
    field: FieldAttr,
    using: Optional[str] = None,
    validated_only: bool = True,
    kwargs: Dict = None,
):
    """Register features or labels records in the default instance from the using instance."""
    if kwargs is None:
        kwargs = {}
    registry = field.field.model
    registry_using = _registry_using(registry, using)
    if not hasattr(
        registry, "organism_id"
    ):  # for registries that don't require organism
        kwargs.pop("organism", None)
    else:
        if kwargs.get("organism") is None:
            raise ValueError("please specify organism!")
    verbosity = ln.settings.verbosity
    ln.settings.verbosity = "error"
    # for labels that are registered in the using instance, transfer them to the current instance
    # first inspect the current instance
    inspect_result_current = registry.inspect(values, field=field, mute=True, **kwargs)
    if len(inspect_result_current.non_validated) == 0:
        return

    labels_registered: Dict = {"from public": [], "without reference": []}
    if using is not None and using != "default":
        labels_registered[f"from {using}"] = []
        # then inspect the using instance
        inspect_result_using = registry_using.inspect(
            inspect_result_current.non_validated, field=field, mute=True, **kwargs
        )
        # register the labels that are validated in the using instance
        # TODO: filter kwargs
        labels_using = registry_using.filter(
            **{f"{field.field.name}__in": inspect_result_using.validated}
        ).all()
        for label_using in labels_using:
            label_using.save()
            labels_registered[f"from {using}"].append(
                getattr(label_using, field.field.name)
            )
    else:
        inspect_result_using = inspect_result_current

    # for labels that are not registered in the using instance, register them in the current instance
    if len(inspect_result_using.non_validated) > 0:
        from_values_records = registry.from_values(
            inspect_result_using.non_validated, field=field, **kwargs
        )
    else:
        from_values_records = []
    ln.settings.verbosity = verbosity
    if len(from_values_records) > 0:
        ln.save(from_values_records)
        labels_registered["from public"] = [
            getattr(r, field.field.name) for r in from_values_records
        ]
    for value in inspect_result_using.non_validated:
        if value in labels_registered["from public"]:
            continue
        labels_registered["without reference"].append(value)
        if validated_only:
            continue
        kwargs[field.field.name] = value
        if registry.__name__ == "Feature":
            kwargs["type"] = "category"
        # register non-validated labels
        label = registry(**kwargs)
        label.save()

    # for ulabels, also register a parent label: is_{feature_name}
    if register == ln.ULabel and field.field.name == "name":
        all_records = registry.from_values(values, field=field)
        is_feature = registry.filter(name=f"is_{field.field.name}").one_or_none()
        if is_feature is None:
            is_feature = registry(name=f"is_{field.field.name}")
            is_feature.save()
        # link all labels to the parent label
        is_feature.children.add(*all_records)

    # log the registered labels
    for key, labels in labels_registered.items():
        if len(labels) > 0:
            if key == "without reference" and validated_only:
                logger.warning(
                    f"{len(labels)} non-validated labels are not registered: {labels}!\n      → to register, set `validated_only=False`"
                )
                continue
            logger.success(
                f"registered {len(labels)} records {colors.green(key)}: {labels}"
            )


class AnnDataValidator:
    """Lamin validator.

    Args:
        adata: an AnnData object to validate
        var_field: the registry field to validate variables index against
        obs_fields: a dictionary containing {obs_column_name: registry_field_to_validate}
            For instance: {"cell_type": bt.CellType.name, "donor_id": ln.ULabel.name}
        using: the reference instance containing registries to validate against
    """

    def __init__(
        self,
        adata: Union[ad.AnnData, str, Path],
        var_field: FieldAttr,
        obs_fields: Dict[str, FieldAttr],
        using: str = "default",
        verbosity: str = "hint",
    ) -> None:
        """Validate an AnnData object."""
        if isinstance(adata, (str, Path)):
            self._adata = ad.read_h5ad(adata)
        else:
            self._adata = adata
        self._verbosity = verbosity
        self._using = using
        self._kwargs: Dict = {}
        self._artifact = None
        self._collection = None
        self._adata_curated = None
        self._var_field = var_field
        self._obs_fields = obs_fields
        self.register_features()

    @property
    def var_field(self) -> FieldAttr:
        """Return the registry field to validate variables index against."""
        return self._var_field

    @property
    def obs_fields(self) -> Dict:
        """Return the obs fields to validate against."""
        return self._obs_fields

    @property
    def adata_curated(self) -> ad.AnnData:
        """Return the curated AnnData object."""
        return self._adata_curated

    def _assign_kwargs(self, **kwargs):
        organism = kwargs.get("organism") or self._kwargs.get("organism")
        if organism is None:
            raise ValueError("please specify organism")
        else:
            self._kwargs["organism"] = organism
        for k, v in kwargs.items():
            self._kwargs[k] = v

    def register_features(self) -> None:
        """Register features records."""
        missing_columns = [
            i for i in self.obs_fields.keys() if i not in self._adata.obs
        ]
        if len(missing_columns) > 0:
            raise ValueError(
                f"columns {missing_columns} are not found in the AnnData object!"
            )
        register_labels_in_default_from_using(
            values=list(self.obs_fields.keys()),
            field=ln.Feature.name,
            using=self._using,
            validated_only=False,
        )

    def register_variables(self, field: FieldAttr, organism: Optional[str] = None):
        """Register gene records."""
        register_labels_in_default_from_using(
            values=self._adata.var_names,
            field=field,
            using=self._using,
            kwargs={"organism": organism},
        )

    def register_labels(self, feature: str, validated_only: bool = True, **kwargs):
        """Register labels records."""
        if feature not in self.obs_fields:
            raise ValueError(f"feature {feature} is not part of the obs_fields!")

        field = self.obs_fields.get(feature)
        values = self._adata.obs[feature].unique().tolist()
        register_labels_in_default_from_using(
            values=values,
            field=field,
            using=self._using,
            validated_only=validated_only,
            kwargs=kwargs,
        )

    def validate(
        self,
        organism: Optional[str] = None,
        **kwargs,
    ) -> bool:
        """Validate variables and categorical observations.

        Args:
            organism: name of the organism
            **kwargs: object level metadata

        Returns:
            whether the AnnData object is validated
        """
        self._assign_kwargs(
            organism=organism or self._kwargs.get("organism"),
            **kwargs,
        )
        validated = validate(
            self._adata,
            var_field=self.var_field,
            obs_fields=self.obs_fields,
            **self._kwargs,
        )
        if validated:
            self._adata_curated = self._adata.copy()
            logger.info("see the curated AnnData object in `.adata_curated`!")

        return validated

    def register_artifact(
        self,
        description: str,
        **kwargs,
    ) -> ln.Artifact:
        """Register the validated AnnData and metadata.

        Args:
            description: description of the AnnData object
            **kwargs: object level metadata

        Returns:
            a registered artifact record
        """
        self._assign_kwargs(**kwargs)
        if self._adata_curated is None:
            raise ValueError("please run `validate()` first!")

        artifact = register(
            self.adata_curated,
            description=description,
            obs_fields=self.obs_fields,
            **self._kwargs,
        )
        return artifact

    def register_collection(
        self,
        artifact: ln.Artifact,
        name: str,
        description: Optional[str] = None,
        reference: Optional[str] = None,
        reference_type: Optional[str] = None,
    ) -> ln.Collection:
        """Register a collection from artifact/artifacts.

        Args:
            artifact: a registered artifact or a list of registered artifacts
            name: title of the publication
            description: description of the publication
            reference: accession number (e.g. GSE#, E-MTAB#, etc.)
            reference_type: source type (e.g. GEO, ArrayExpress, SRA, etc.)
        """
        collection = ln.Collection(
            artifact,
            name=name,
            description=description,
            reference=reference,
            reference_type=reference_type,
        )
        instance_slug = ln.setup.settings.instance.slug
        if collection._state.adding:
            collection.save()
            logger.print(
                f"🎉 successfully registered collection in LaminDB!\nview it in the hub: https://lamin.ai/{instance_slug}/Collection/{collection.uid}"
            )
        else:
            collection.save()
            logger.warning(
                f"collection already exists in LaminDB!\nview it in the hub: https://lamin.ai/{instance_slug}/Collection/{collection.uid}"
            )
        self._collection = collection
        return collection

    def clean_up_failed_runs(self):
        """Clean up previous failed runs that don't register any outputs."""
        if ln.run_context.transform is not None:
            ln.Run.filter(
                transform=ln.run_context.transform, output_artifacts=None
            ).exclude(uid=ln.run_context.run.uid).delete()
