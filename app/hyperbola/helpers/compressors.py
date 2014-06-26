import cssmin
from pipeline.compressors import CompressorBase


class PyCSSMinCompressor(CompressorBase):
    def compress_js(self, js):
        pass

    def compress_css(self, css):
        return cssmin.cssmin(css)
