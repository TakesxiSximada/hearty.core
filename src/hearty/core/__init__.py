__version__ = '0.1.dev0'


def includeme(config):
    from .interfaces import IAction
    from .ping import Ping

    config.register(Ping(), IAction, 'ping')
