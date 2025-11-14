"""Just to get a version."""

import os, sys


sys.path.insert(0, os.path.abspath(os.path.pardir))
from . import _version
__version__ = _version.get_versions()['version']
