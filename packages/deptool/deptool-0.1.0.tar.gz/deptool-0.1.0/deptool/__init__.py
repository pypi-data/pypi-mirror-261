from dataclasses import dataclass
from importlib import import_module
from pathlib import Path


@dataclass(frozen=True)
class SubCommand:
    add_subcommand_parser: callable
    subcommand_main: callable


subcommands = {}
for module_filename in Path(__file__).parent.glob("cmd_*.py"):
    module = import_module(f"deptool.{module_filename.stem}")
    subcommands[module_filename.stem.removeprefix("cmd_")] = SubCommand(
        add_subcommand_parser=getattr(module, "add_subcommand_parser"),
        subcommand_main=getattr(module, "subcommand_main"),
    )
