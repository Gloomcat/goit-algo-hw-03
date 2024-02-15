import shutil

from argparse import ArgumentParser
from pathlib import Path


def copy_tree(source: Path, dest: str) -> None:
    source = Path(source)
    if not source.exists():
        raise ValueError("Source path must be valid.")
    print(source.name)
    if source.is_dir():
        for child in source.iterdir():
            copy_tree(child, dest)
    elif source.is_file():
        dest_dir = Path(dest) / source.suffix
        dest_dir.mkdir(parents=True, exist_ok=True)
        shutil.copy(source, dest_dir / source.name)


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("-s", "--source", help="path to the source dir")
    parser.add_argument(
        "-d",
        "--dest",
        default="dist",
        help="path to the destination dir (defaults to 'dist')",
    )
    args = parser.parse_args()
    copy_tree(args.source, args.dest)
