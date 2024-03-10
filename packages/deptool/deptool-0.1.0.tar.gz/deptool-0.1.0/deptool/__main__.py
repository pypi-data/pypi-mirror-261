import argparse
import sys

import deptool


def parse_arguments(argv: list[str]):
    argument_parser = argparse.ArgumentParser(prog="deptool")
    subcommand_parsers = argument_parser.add_subparsers(
        required=True, dest="subcommand"
    )

    for subcommand in deptool.subcommands.values():
        subcommand.add_subcommand_parser(subcommand_parsers)

    return argument_parser.parse_args(argv)


def main():
    cli_args = parse_arguments(sys.argv[1:])
    return deptool.subcommands[cli_args.subcommand].subcommand_main(cli_args)


if __name__ == "__main__":
    sys.exit(main())
