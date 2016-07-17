# -*- coding: utf-8 -*-
from miniconfig import ConfiguratorCore

from .apps import Application


class Configurator(ConfiguratorCore):
    application_factory = Application

    def __call__(self, *args, **kwds):
        self.commit()
        return self.application_factory(self)
