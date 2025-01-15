"""Script to set every undefined type as an alias of Any."""

import argparse
from collections import defaultdict
from pathlib import Path

from .processing_utils import pyright_run, sed


def main() -> None:
    """Open scripts and add aliases to undefined types."""

    argparse.ArgumentParser(
        description="Script to set every undefined type as an alias of Any.",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    print("Running pyright")
    pyright_result = pyright_run()

    aliases_to_add: dict[Path, set[str]] = defaultdict(set)
    for line in pyright_result:
        if "is not defined (reportUndefinedVariable)" not in line:
            continue
        file_path = Path(line.split(":", maxsplit=1)[0].lstrip())
        alias_to_add = line.split('"')[1]
        aliases_to_add[file_path].add(alias_to_add)

    print("Adding the following aliases:")
    for path, names in aliases_to_add.items():
        print(f"{path}: {names}")

    for path, _names in aliases_to_add.items():
        print(f"Adding aliases to file {path.name}")
        write_line = 0
        with path.open("r", encoding="utf-8") as stub_file:
            while "from" in (line := stub_file.readline().strip()) or "import" in line or line == "":
                write_line += 1
                continue

        write_line = max(1, write_line)
        sed("{line_content}: TypeAlias = Any\n", path)
        sed("{line_content}i\n", path)

    print("Finished")


if __name__ == "__main__":
    main()
