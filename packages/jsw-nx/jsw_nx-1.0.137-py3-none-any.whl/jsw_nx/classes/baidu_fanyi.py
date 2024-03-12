from .baidu.fanyi import Fanyi

DEFAULTS = {
    "from": "en",
    "to": "zh",
}


class BaiduFanyi:
    @classmethod
    def translate(cls, **kwargs):
        q = kwargs.pop("q", "apple")
        opts = DEFAULTS.copy()
        opts.update(kwargs)
        return Fanyi(q=q, **kwargs).translate(opts)
