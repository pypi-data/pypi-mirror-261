"""Validator built on LaminDB.

Import the package::

   from lamin_validator import AnnDataValidator

This is the complete API reference:

.. autosummary::
   :toctree: .

   AnnDataValidator
   datasets
"""

__version__ = "0.0.1"  # denote a pre-release for 0.1.0 with 0.1rc1

from . import datasets
from ._validator import AnnDataValidator
