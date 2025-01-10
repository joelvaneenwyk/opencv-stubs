"""Script to set every undefined type as an alias of Any."""

import argparse
import subprocess
from collections import defaultdict
from pathlib import Path

import pyright


def main() -> None:
    argparse.ArgumentParser(description="Script to set every undefined type as an alias of Any.", formatter_class=argparse.ArgumentDefaultsHelpFormatter)

    print("Running pyright")
    pyright_process = pyright.run(".", stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    pyright_result = pyright_process.stdout.decode("utf-8").splitlines()

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

    for path, names in aliases_to_add.items():
        print(f"Adding aliases to file {path.name}")
        with path.open("r", encoding="utf-8") as stub_file:
            write_line = 0
            while "from" in (line := stub_file.readline().strip()) or "import" in line or line == "":
                write_line += 1
                continue

        def sed(format_string: str, file_path: Path) -> None:
            with file_path.open("r", encoding="utf-8") as stub_file:
                lines = stub_file.readlines()

            insertion_line = write_line
            for name in names:
                lines.insert(insertion_line, format_string.format(write_line=name))
                insertion_line += 1

            with file_path.open("w", encoding="utf-8") as stub_file:
                stub_file.writelines(lines)

        write_line = max(1, write_line)
        sed("{write_line}: TypeAlias = Any\n", path)
        sed(f"{write_line}i\n", path)

    print("Finished")


if __name__ == "__main__":
    main()
