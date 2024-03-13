"""Validators built on LaminDB.

Import the package::

   from lamin_validator import Validator, AnnDataValidator

This is the complete API reference:

.. autosummary::
   :toctree: .

   Validator
   AnnDataValidator
   datasets
"""

__version__ = "0.1.1"

from . import datasets
from ._anndata_validator import AnnDataValidator
from ._validator import Validator
