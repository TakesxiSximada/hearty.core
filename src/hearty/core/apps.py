# -*- coding: utf-8 -*-
from .interfaces import IAction


class Application(object):
    def __init__(self, config, default_interface=None):
        self.config = config
        self.default_interface = default_interface or IAction

    def __call__(self, interface=None, name=None):
        interface = interface or self.default_interface
        registry = self.config.settings['registry']
        return registry.queryUtility(interface, name)
