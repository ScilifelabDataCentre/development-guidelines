import argparse

from pathlib import Path

def main(excluded_paths: str):
    """"""
    print(excluded_paths)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flag outdated files. Compares the last_reviewed information in files with the current date and flags files that have not been reviewed in at least a year.")
    parser.add_argument("excluded_paths", type=Path, help="File listing paths to exclude from the check.")
    args = parser.parse_args()
    main(args.excluded_paths)