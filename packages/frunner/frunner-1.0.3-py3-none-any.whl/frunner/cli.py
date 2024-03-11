# -*- coding:utf-8 -*-
import argparse
import sys
from frunner import __version__, __description__
from frunner.scaffold import init_scaffold_project, main_scaffold_project


def main():
    """ API test: parse command line options and run commands.
    """
    parser = argparse.ArgumentParser(description=__description__)
    parser.add_argument(
        "-V", "--version", dest="version", action="store_true", help="show version",
    )

    subparsers = parser.add_subparsers(help="sub-command help")
    sub_parser_project = init_scaffold_project(subparsers)

    if len(sys.argv) == 1:
        # frun
        parser.print_help()
        sys.exit(0)
    elif len(sys.argv) == 2:
        # print help for sub-commands
        if sys.argv[1] in ["-V", "--version"]:
            # frun -V
            print(f"{__version__}")
        elif sys.argv[1] in ["-h", "--help"]:
            # frun -h
            parser.print_help()
        elif sys.argv[1] == "startproject":
            # frun startproject
            sub_parser_project.print_help()
        sys.exit(0)
    else:
        if sys.argv[1] == "startproject":
            args = parser.parse_args()
            main_scaffold_project(args)
        sys.exit(0)


if __name__ == "__main__":
    main()
