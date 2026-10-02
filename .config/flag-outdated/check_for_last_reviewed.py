# 2. bestämma vilka filer som ska ha en last_review date -- yml
# 3. kolla igenom alla de filerna och se om dom har det -- python
# 4. om dom inte har det, lägg i en lista som ska visas i en issue -- python
# 5. om dom har det, kolla om det är i rätt format, och om inte lägg i en lista som ska visas i en issue -- python
# 6. om formatet är rätt, jämför med dagens datum -- python
# 7. om det är äldre än 12 månader, lägg i en lista som ska visas i en issue -- python

import argparse
from pathlib import Path
from datetime import date, datetime, timedelta
import logging

import frontmatter

# Set up logging
logger = logging.getLogger(__name__)

def check_for_metadata(repo_path: Path) -> date:
    """Check if a file contains metadata."""

    # Open file and check for metadata
    with repo_path.open() as f:
        metadata, _ = frontmatter.parse(f.read())

        if not metadata:
            logger.debug(f"Needs metadata: {repo_path}")
            return None

        if "last_reviewed" not in metadata:
            logger.debug(f"No 'last_reviewed' in {repo_path}")
            return None
        
        return metadata["last_reviewed"]
    
def existing_path(value: str) -> Path:
    """Check if the string is an existing file and return a Path."""
    logger.debug(f"Got file argument: {value}")

    path = Path(value)
    if path.exists() and path.is_file():
        logger.debug(f"The path '{path}' exists and is a file.")
        return path
    
    raise argparse.ArgumentTypeError(f"The file does not exist or is not a file: {path}")

def time_for_review(last_reviewed: date, current_date: date, max_diff_before_flag: timedelta) -> bool:
    """Check if it's time for a review based on number of days since last one."""
    
    # Calculate days since last review 
    diff = current_date - last_reviewed

    # Check if it's time for a review
    return diff >= max_diff_before_flag

def get_outdated_files(all_paths_to_exclude) -> tuple[list]:
    """Scan the repository and find files in need of review."""
    # Variables
    current_date: date = datetime.now().date()
    logger.debug(f"Todays date: {current_date} (type: {type(current_date)})")

    max_diff_before_flag: timedelta = timedelta(days=365)
    logger.debug(f"Maximum diff: {max_diff_before_flag}")

    needs_metadata: list[Path] = []
    needs_review: list[Path] = []
    invalid: list[Path] = []

    # Iterate through all files in repo
    logger.debug("Searching for outdated files...")
    for repo_path in Path(".").rglob(pattern="*.md"):
        # Check that the path is a file
        # Not sure I need this -- rglob might already handle it?
        if not repo_path.is_file():
            logger.debug(f"{repo_path} is not a file. Skipping.")
            continue

        # Check if the path should be excluded
        if any(repo_path.full_match(Path(pattern)) for pattern in all_paths_to_exclude):
            logger.debug(f"Excluding {repo_path}.")
            continue

        logger.debug(f"Looking for {repo_path} metadata...")
        last_reviewed: date = check_for_metadata(repo_path=repo_path)
        if not last_reviewed:
            needs_metadata.append(repo_path)
            continue

        if not isinstance(last_reviewed, date):
            logger.error(f"'last_reviewed' contains invalid value (needs date): {repo_path} ({type(repo_path)})")
            invalid.append(repo_path)
            continue

        logger.debug(f"{repo_path} last reviewed: {last_reviewed}")

        logger.debug("Checking if it's time for a review...")

        if time_for_review(last_reviewed=last_reviewed, current_date=current_date, max_diff_before_flag=max_diff_before_flag):
            logger.debug(f"Needs review: {repo_path}")
            needs_review.append(repo_path)

    logger.debug(f"Files needing metadata: {needs_metadata}")
    logger.debug(f"Files needing review: {needs_review}")
    logger.debug(f"Files with invalid date: {invalid}")

    return needs_metadata, invalid, needs_review

def save_results_to_markdown(needs_metadata: list, invalid: list, needs_review: list):
    """Save the lists to a markdown file."""

    markdown_file: Path = Path("outdated-results.md")

    logger.debug(f"Saving results to markdown file: {markdown_file}")
    markdown_content: str = (
        "## What is this?\n"
        "These are the results of the 'flag-outdated.yml' workflow.\n"
        "## Invalid 'last_reviewed' values"
        f"{'\n'.join(f'- [ ] {file}' for file in invalid)}\n"
        "## Missing metadata\n"
        f"{'\n'.join(f'- [ ] {file}' for file in needs_metadata)}\n"
        "## Time for review\n"
        f"{'\n'.join(f'- [ ] {file}' for file in needs_review)}"
    )

    with markdown_file.open(mode="w") as file:
        file.write(markdown_content)

def main(excluded_paths: Path):
    """"""

    # Read excluded paths and get list of excluded paths
    all_paths_to_exclude = excluded_paths.read_text().split()
    logger.debug(f"All paths were collected from {excluded_paths} file.")
    logger.debug(f"All paths to exclude: {all_paths_to_exclude}")

    # Search for outdated files
    needs_metadata, invalid, needs_review = get_outdated_files(all_paths_to_exclude=all_paths_to_exclude)

    # Save output
    save_results_to_markdown(needs_metadata=needs_metadata, invalid=invalid, needs_review=needs_review)

if __name__ == "__main__":
    # Set logging level
    logging.basicConfig(level=logging.DEBUG)

    # Parse arguments passed in
    parser = argparse.ArgumentParser(description="Flag outdated files. Compares the last_reviewed information in files with the current date and flags files that have not been reviewed in at least a year.")
    parser.add_argument("excluded_paths", type=existing_path, help="File listing paths to exclude from the check.")
    args = parser.parse_args()

    # Run script
    main(excluded_paths=args.excluded_paths)
