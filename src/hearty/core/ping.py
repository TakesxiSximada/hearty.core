# -*- coding: utf-8 -*-
from zope.interface import implementer

from .interfaces import IAction


@implementer(IAction)
class Ping(object):
    def __init__(self, word='pong'):
        self.word = word

    def __call__(self, *args, **kwds):
        return self.word
