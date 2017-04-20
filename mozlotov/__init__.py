__version__ = '0.1'

try:
    from mozlotov._fxa import FXATestAccount     # NOQA
except ImportError:
    pass                                         # NOQA
