# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring

# Copyright (c) CentML Inc. All Rights Reserved.
import sys
import argparse
from .plan import add_plan_parser
from .controller import add_controller_parser
from .engine import add_engine_parser


def parse_args():
    parser = argparse.ArgumentParser(prog='cserve')

    subparsers = parser.add_subparsers(title='Subcommands', dest='subcommand')

    add_plan_parser(subparsers)
    add_controller_parser(subparsers)
    add_engine_parser(subparsers)

    args = parser.parse_args()

    return args, parser


def main():
    args, parser = parse_args()
    if args.subcommand == 'plan':
        from .plan import run
    elif args.subcommand == 'controller':
        from .controller import run
    elif args.subcommand == 'engine':
        from .engine import run
    else:
        parser.print_help()
        sys.exit()

    run(args)


if __name__ == '__main__':
    main()
