# -*- coding: utf-8 -*-
from zope.interface.registry import Components

from .config import Configurator
from .directives import register


def bootstrap(includeme, settings, *paths):
    settings['registry'] = Components()
    config = Configurator(settings)
    config.add_directive('register', register)
    config.include(includeme)
    return config
