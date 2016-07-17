# -*- coding: utf-8 -*-


def register(config, component, interface, select=''):
    def _():
        registry = config.settings['registry']
        registry.registerUtility(component, interface, select)
    config.action(_)
