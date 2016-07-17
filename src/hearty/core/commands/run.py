# -*- coding: utf-8 -*-
import sys
import six


def main(argv=sys.argv[1:]):
    from hearty.core.bootstraps import bootstrap

    settings = {}
    config = bootstrap('hearty.core', settings)
    app = config()

    while True:
        msg = six.moves.input('[hearty] ')
        action = app(name=msg)
        if action:
            print(action())
        else:
            print('not found action: {}'.format(msg))
