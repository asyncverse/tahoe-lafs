"""
Decentralized storage grid.

community web site: U{https://tahoe-lafs.org/}
"""
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from future.utils import PY2, PY3
if PY2:
    # Don't import future str() so we don't break Foolscap serialization on Python 2.
    from future.builtins import filter, map, zip, ascii, chr, hex, input, next, oct, open, pow, round, super, bytes, dict, list, object, range, max, min  # noqa: F401
    from past.builtins import unicode as str

__all__ = [
    "__version__",
    "full_version",
    "branch",
    "__appname__",
    "__full_version__",
]

__appname__ = "tahoe-lafs"
### automatically managed version information block
### This section is generated from git metadata by version-from-git.
__version__ = "unknown"
__real_version__ = "unknown"
__full_version__ = "unknown"
__branch__ = "unknown"
### end automatically managed version information block

# __full_version__ is the one that you ought to use when identifying yourself
# in the "application" part of the Tahoe versioning scheme:
# https://tahoe-lafs.org/trac/tahoe-lafs/wiki/Versioning
__full_version__ = __appname__ + '/' + str(__version__)


# Install Python 3 module locations in Python 2:
from future import standard_library
standard_library.install_aliases()


# Monkey-patch 3rd party libraries:
from ._monkeypatch import patch
patch()
del patch


# On Python 3, turn BytesWarnings into exceptions. This can have potential
# production impact... if BytesWarnings are actually present in the codebase.
# Given that this has been enabled before Python 3 Tahoe-LAFS was publicly
# released, no such code should exist, and this will ensure it doesn't get
# added either.
#
# Also note that BytesWarnings only happen if Python is run with -b option, so
# in practice this should only affect tests.
if PY3:
    import warnings
    # Error on BytesWarnings, to catch things like str(b""), but only for
    # allmydata code.
    warnings.filterwarnings("error", category=BytesWarning, module=".*allmydata.*")
