# 2. bestämma vilka filer som ska ha en last_review date -- yml
# 3. kolla igenom alla de filerna och se om dom har det -- python
# 4. om dom inte har det, lägg i en lista som ska visas i en issue -- python
# 5. om dom har det, kolla om det är i rätt format, och om inte lägg i en lista som ska visas i en issue -- python
# 6. om formatet är rätt, jämför med dagens datum -- python
# 7. om det är äldre än 12 månader, lägg i en lista som ska visas i en issue -- python

import argparse
import frontmatter

from pathlib import Path

def main(excluded_paths: Path):
    """"""
    # Print path
    print("excluded paths file:\n", excluded_paths, type(excluded_paths))

    # 1. Check if excluded_paths exists - is this needed? 
    # 2. Read excluded paths and get list of excluded paths
    all_excluded_paths: list[Path] = []
    if excluded_paths.exists() and excluded_paths.is_file():
        all_excluded_paths = excluded_paths.read_text().split()
    else:
        return # something

    print("paths taken from the excluded paths:\n", all_excluded_paths)

    print("paths in repo that should be checked for last reviewed:\n")
    # 3. Get all paths in repo
    for file in Path(".").rglob("*"):
        if not file.is_file():
            continue
        if any(file.full_match(Path(pattern)) for pattern in all_excluded_paths):
            continue

        # here goes the check
        with file.open("") as f:
            fm = frontmatter.load(f)
            print(fm)    
        
        print(file)


    # 5. Parse files -- search for front matter? last_reviewed?
    # 6. Return lists of files that need to be updated


        

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Flag outdated files. Compares the last_reviewed information in files with the current date and flags files that have not been reviewed in at least a year.")
    parser.add_argument("excluded_paths", type=Path, help="File listing paths to exclude from the check.")
    args = parser.parse_args()
    
    main(args.excluded_paths)