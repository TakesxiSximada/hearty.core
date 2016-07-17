# -*- coding: utf-8 -*-
from zope.interface import Interface


class IAction(Interface):
    def __call__():
        return ''
