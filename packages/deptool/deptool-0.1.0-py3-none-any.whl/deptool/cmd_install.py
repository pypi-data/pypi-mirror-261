from dataclasses import dataclass
from pathlib import Path
import subprocess

import yaml


def add_subcommand_parser(subcommand_parsers):
    subcommand_parser = subcommand_parsers.add_parser("install")

    subcommand_parser.add_argument("--depfile", type=Path, default=Path("depfile.yaml"))
    subcommand_parser.add_argument("--registry", type=str, default="default")


@dataclass(frozen=True)
class Dependency:
    author: str
    name: str


@dataclass(frozen=True)
class DepfileContents:
    build_dependencies: list[Dependency]
    test_dependencies: list[Dependency]

    @property
    def all_dependencies(self):
        return self.build_dependencies + self.test_dependencies


def _parse_depfile(filename):
    def parse_dependency_list(lst):
        def str_to_dependency(string):
            try:
                author, name = string.split("/")
            except ValueError:
                raise ValueError(f"dependency string '{string}' is malformed")

            return Dependency(author=author, name=name)

        return [str_to_dependency(dep_string) for dep_string in lst]

    depfile_dict = yaml.safe_load(open(filename, "r"))

    if "build_dependencies" in depfile_dict:
        build_dependencies = parse_dependency_list(depfile_dict["build_dependencies"])
    else:
        build_dependencies = list()

    if "test_dependencies" in depfile_dict:
        test_dependencies = parse_dependency_list(depfile_dict["test_dependencies"])
    else:
        test_dependencies = list()

    return DepfileContents(
        build_dependencies=build_dependencies,
        test_dependencies=test_dependencies,
    )


def subcommand_main(cli_args):
    if not cli_args.depfile.exists():
        print(f"deptool: depfile path '{cli_args.depfile}' does not exist")
        return 1

    try:
        dependencies = _parse_depfile(cli_args.depfile).all_dependencies
    except ValueError as error:
        print(f"deptool: could not parse depfile: {error}")
        return 1

    registry_root = Path(f"/var/local/lib/deptool/{cli_args.registry}")

    if not registry_root.exists():
        print(f"deptool: registry '{registry_root}' not found")
        return 1

    for dep in dependencies:
        install_script = registry_root / dep.author / f"{dep.name}.sh"

        if not install_script.exists():
            print(f"deptool: dependency '{dep.author}/{dep.name}' not found")
            continue

        print(f"deptool: installing '{dep.author}/{dep.name}'")

        try:
            subprocess.check_output(["sudo", "sh", install_script])
        except subprocess.CalledProcessError as error:
            print(f"deptool: could not install '{dep.author}/{dep.name}': {error}")

    return 0
