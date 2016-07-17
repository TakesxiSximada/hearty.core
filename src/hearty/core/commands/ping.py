# -*- coding: utf-8 -*-
import sys


def main(argv=sys.argv[1:]):
    from hearty.core.bootstraps import bootstrap

    settings = {}
    config = bootstrap('hearty.core', settings)
    app = config()
    action = app(name='ping')
    print(action())
