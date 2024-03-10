from pathlib import Path
import shutil
import subprocess

import yaml


def add_subcommand_parser(subcommand_parsers):
    subcommand_parser = subcommand_parsers.add_parser("registries")

    verb_parers = subcommand_parser.add_subparsers(required=True, dest="verb")
    verb_parers.add_parser("list")

    verb_parser_show = verb_parers.add_parser("show")
    verb_parser_show.add_argument("registry")

    verb_parers.add_parser("update")


def process_verb_list():
    registries_file = Path("/etc/deptool/registries.yaml")
    if not registries_file.exists():
        print(f"deptool: registries file '{registries_file}' not found")
        return 1

    for registry in yaml.safe_load(open(registries_file, "r")):
        print(registry)

    return 0


def process_verb_show(cli_args):
    registries_file = Path("/etc/deptool/registries.yaml")
    if not registries_file.exists():
        print(f"deptool: registries file '{registries_file}' not found")
        return 1

    registries = yaml.safe_load(open(registries_file, "r"))
    if cli_args.registry not in registries:
        print(f"deptool: unknown registry '{cli_args.registry}'")
        return 1

    registry = registries[cli_args.registry]
    print(cli_args.registry)
    print(f"  kind: {registry['kind']}")
    print(f"  repository: {registry['repository']}")
    print(f"  baseline: {registry['baseline']}")

    return 0


def process_verb_update():
    registries_file = Path("/etc/deptool/registries.yaml")
    if not registries_file.exists():
        print(f"deptool: registries file '{registries_file}' not found")
        return 1

    registries = yaml.safe_load(open(registries_file, "r"))

    staging_dir = Path(f"/tmp/deptool-staging")
    staging_dir.mkdir(parents=True, exist_ok=True)

    for registry_name, registry_details in registries.items():
        if registry_details["kind"] != "git":
            continue

        try:
            subprocess.check_output(
                [
                    "git",
                    "clone",
                    "--depth",
                    "1",
                    "--branch",
                    registry_details["baseline"],
                    registry_details["repository"],
                    str(staging_dir / f"{registry_name}"),
                ]
            )
        except subprocess.CalledProcessError:
            print(f"deptool: could not update registry '{registry_name}'")
            shutil.rmtree(staging_dir, ignore_errors=True)
            return 1

    try:
        subprocess.check_output(["sudo", "mkdir", "-p", "/var/local/lib/deptool"])
        subprocess.call(
            f"sudo rm -rf /var/local/lib/deptool/{registry_name}", shell=True
        )
        subprocess.call(
            f"sudo mv -f {staging_dir / registry_name} /var/local/lib/deptool",
            shell=True,
        )
        subprocess.check_output(
            ["sudo", "chown", "-R", "root:root", "/var/local/lib/deptool"]
        )
    finally:
        shutil.rmtree(staging_dir, ignore_errors=True)


def subcommand_main(cli_args):
    if cli_args.verb == "list":
        return process_verb_list()
    if cli_args.verb == "show":
        return process_verb_show(cli_args)
    if cli_args.verb == "update":
        return process_verb_update()

    return 0
