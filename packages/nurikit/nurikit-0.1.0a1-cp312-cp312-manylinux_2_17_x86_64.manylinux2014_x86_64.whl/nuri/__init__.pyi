"""

Project nurikit: *the* fundamental software platform for chem- and
bio-informatics.
"""
from __future__ import annotations
from nuri.fmt import readfile
from nuri.fmt import readstring
from . import _log_adapter
from . import _log_interface
from . import _version
from . import core
from . import fmt
__all__: list = ['readfile', 'readstring', 'periodic_table', '__version__']
__full_version__: str = '0.1.0'
__version__: str = '0.1.0'
periodic_table: core._core.PeriodicTable  # value = <nuri.core._core.PeriodicTable object>
