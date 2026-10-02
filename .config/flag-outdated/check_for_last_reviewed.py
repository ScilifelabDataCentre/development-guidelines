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
    all_paths_to_exclude = excluded_paths.read_text().split()
    logger.debug(f"All paths were collected from {excluded_paths} file.")

    # get current date
    current_date: datetime.date = datetime.now().date()
    logger.debug(f"Todays date: {current_date} (type: {type(current_date)})")

    logger.debug("Searching for outdated files...")
    # Iterate through all files in repo
    for repo_path in Path(".").rglob("*"):
        # Check that the path is a file
        # Not sure I need this -- rglob might already handle it?
        if not repo_path.is_file():
            logger.debug(f"{repo_path} is not a file. Skipping.")
            continue

        # Check if the path should be excluded
        if any(repo_path.full_match(Path(pattern)) for pattern in all_paths_to_exclude):
            logger.debug(f"Excluding {repo_path}.")
            continue

        
        with repo_path.open() as f:
            metadata, _ = frontmatter.parse(f.read())
            print(metadata, "\n")

            if not metadata:
                needs_metadata.append(repo_path)
                continue

            if "last_reviewed" not in metadata:
                needs_metadata.append(repo_path)
                continue

            diff = current_date - metadata["last_reviewed"]
            if diff >= max_diff_before_flag:
                needs_review.append(repo_path)

            print(repo_path, "diff: ", diff)

    print("needs_metadata: ", needs_metadata)
    print("needs_review:", needs_review)


    # 5. Parse files -- search for front matter? last_reviewed?
    # 6. Return lists of files that need to be updated


        

if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    parser = argparse.ArgumentParser(description="Flag outdated files. Compares the last_reviewed information in files with the current date and flags files that have not been reviewed in at least a year.")
    parser.add_argument("excluded_paths", type=existing_path, help="File listing paths to exclude from the check.")
    args = parser.parse_args()
    
    main(args.excluded_paths)