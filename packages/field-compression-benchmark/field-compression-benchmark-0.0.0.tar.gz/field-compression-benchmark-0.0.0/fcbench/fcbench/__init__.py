__all__ = ["benchmark", "codecs", "compressor", "dataset", "plot"]

import sys as _sys

from . import benchmark, codecs, compressor, dataset, plot

# polyfill for fcpy imports
_sys.modules["fcpy"] = _sys.modules[__name__]
