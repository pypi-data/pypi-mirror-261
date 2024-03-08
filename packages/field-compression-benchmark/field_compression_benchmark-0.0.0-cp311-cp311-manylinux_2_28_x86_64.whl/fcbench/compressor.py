__all__ = ["compute_dataarray_compress_decompress", "Compressor"]

from ._fcbench import compressor as _compressor

Compressor = _compressor.Compressor
compute_dataarray_compress_decompress = (
    _compressor.compute_dataarray_compress_decompress
)
