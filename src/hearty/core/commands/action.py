# -*- coding: utf-8 -*-
import sys
import argparse


def main(argv=sys.argv[1:]):
    from hearty.core.bootstraps import bootstrap

    parser = argparse.ArgumentParser()
    parser.add_argument('action')
    args = parser.parse_args(argv)
    action_name = args.action

    settings = {}
    config = bootstrap('hearty.core', settings)
    app = config()
    action = app(name=action_name)
    print(action())
