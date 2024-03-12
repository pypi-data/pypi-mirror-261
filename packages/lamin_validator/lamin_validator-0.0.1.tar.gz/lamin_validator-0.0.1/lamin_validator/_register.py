from pathlib import Path
from typing import Dict, Optional, Union

import anndata as ad
import lamindb as ln
import lnschema_bionty as lb
from lamin_utils import logger
from lnschema_core.types import FieldAttr


def register(
    adata: Union[ad.AnnData, str, Path],
    description: str,
    obs_fields: Dict[str, FieldAttr],
    organism: str,
    **kwargs,
):
    """Registers all metadata with an AnnData Artifact."""
    adata = adata if isinstance(adata, ad.AnnData) else ad.read_h5ad(adata)

    # register artifact
    verbosity = ln.settings.verbosity
    ln.settings.verbosity = "warning"
    artifact = ln.Artifact.from_anndata(adata, description=description)
    artifact.n_observations = adata.n_obs
    artifact.save()

    artifact.features.add_from_anndata(
        var_field=lb.Gene.ensembl_gene_id, organism=organism
    )

    # link validated obs metadata
    features = ln.Feature.lookup().dict()
    for feature_name, field in obs_fields.items():
        feature = features.get(feature_name)
        registry = field.field.model
        if hasattr(registry, "organism_id"):
            kwargs["organism"] = organism
        labels = registry.from_values(adata.obs[feature_name], field=field, **kwargs)
        artifact.labels.add(labels, feature)

    logger.print(
        "\n\n🎉 successfully registered artifact in LaminDB!\nview it in the hub"
        f": https://lamin.ai/{ln.setup.settings.instance.slug}/Artifact/{artifact.uid}\n\n"
    )

    logger.print(
        "💡 please register a collection for this artifact:"
        "\n   → collection = ln.Collection(artifact, name=<title>,"
        " description=<doi>, reference=<GSE#>, reference_type=<GEO>)\n   →"
        " collection.save()"
    )
    ln.settings.verbosity = verbosity

    return artifact
