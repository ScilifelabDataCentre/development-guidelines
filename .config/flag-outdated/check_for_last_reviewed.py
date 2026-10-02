# 2. bestämma vilka filer som ska ha en last_review date -- yml
# 3. kolla igenom alla de filerna och se om dom har det -- python
# 4. om dom inte har det, lägg i en lista som ska visas i en issue -- python
# 5. om dom har det, kolla om det är i rätt format, och om inte lägg i en lista som ska visas i en issue -- python
# 6. om formatet är rätt, jämför med dagens datum -- python
# 7. om det är äldre än 12 månader, lägg i en lista som ska visas i en issue -- python

import argparse
from pathlib import Path
from datetime import datetime, timedelta
import logging

import frontmatter

# Set up logging
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def existing_path(value: str) -> Path:
    """Check if the string is an existing file and return a Path."""
    logger.debug(f"Got file argument: {value}")

    path = Path(value)
    if path.exists() and path.is_file():
        logger.debug(f"The path '{path}' exists and is a file.")
        return path
    
    raise argparse.ArgumentTypeError(f"The file does not exist or is not a file: {path}")

def main(excluded_paths: Path):
    """"""

    # Variables 
    max_diff_before_flag: timedelta = timedelta(days=365)
    needs_metadata: list[Path] = []
    needs_review: list[Path] = []

    # Read excluded paths and get list of excluded paths
    all_excluded_paths = excluded_paths.read_text().split()

    # get current date
    current_date: datetime.date = datetime.now().date()
    print("current date: ", current_date, type(current_date))


    
    print("paths in repo that should be checked for last reviewed:\n")
    # 3. Get all paths in repo
    for file in Path(".").rglob("*"):
        if not file.is_file():
            continue
        if any(file.full_match(Path(pattern)) for pattern in all_excluded_paths):
            continue

        with file.open() as f:
            metadata, _ = frontmatter.parse(f.read())
            print(metadata, "\n")

            if not metadata:
                needs_metadata.append(file)
                continue

            if "last_reviewed" not in metadata:
                needs_metadata.append(file)
                continue

            diff = current_date - metadata["last_reviewed"]
            if diff >= max_diff_before_flag:
                needs_review.append(file)

            print(file, "diff: ", diff)

    print("needs_metadata: ", needs_metadata)
    print("needs_review:", needs_review)


    # 5. Parse files -- search for front matter? last_reviewed?
    # 6. Return lists of files that need to be updated


        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flag outdated files. Compares the last_reviewed information in files with the current date and flags files that have not been reviewed in at least a year.")
    parser.add_argument("excluded_paths", type=existing_path, help="File listing paths to exclude from the check.")
    args = parser.parse_args()
    
    main(args.excluded_paths)