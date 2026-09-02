#!/usr/bin/env python3
"""
update_master_list.py - Add newly committed rulesheets to the master list.

Detects .md files added in the most recent commit under manufacturer
subdirectories of docs/, reads their front matter, and inserts a new
row into the appropriate manufacturer section in rulesheet-master-list.md.

Release date, designer, and rules/code columns are left blank for a
human to fill in.

Usage:
    python scripts/update_master_list.py
"""

import os
import re
import subprocess
import sys


MASTER_LIST_PATH = 'docs/rulesheet-master-list.md'

# Map manufacturer name (from front matter) to section heading anchor
MANUFACTURER_ANCHORS = {
    "Stern Pinball":                    "heading--stern",
    "Jersey Jack Pinball":              "heading--jjp",
    "American Pinball":                 "heading--american",
    "Spooky Pinball":                   "heading--spooky",
    "Multimorphic":                     "heading--multimorphic",
    "Heighway Pinball/Pinball Brothers":"heading--brothers",
    "Williams":                         "heading--wms",
    "Data East":                        "heading--de",
    "Capcom":                           "heading--capcom",
    "Gottlieb":                         "heading--gottlieb",
    "Chicago Gaming Company":           "heading--chicago",
    "Barrels of Fun":                   "heading--barrels",
}

# Map manufacturer name to URL directory prefix used in links
MANUFACTURER_DIRS = {
    "Stern Pinball":                    "stern",
    "Jersey Jack Pinball":              "jersey-jack",
    "American Pinball":                 "american-pinball",
    "Spooky Pinball":                   "spooky",
    "Multimorphic":                     "multimorphic",
    "Heighway Pinball/Pinball Brothers":"pinball-brothers",
    "Williams":                         "williams",
    "Data East":                        "data-east",
    "Capcom":                           "capcom",
    "Gottlieb":                         "gottlieb",
    "Chicago Gaming Company":           "chicago-gaming",
    "Barrels of Fun":                   "barrels-of-fun",
}


def get_new_files():
    """Return list of .md files added in the most recent commit."""
    result = subprocess.run(
        ['git', 'diff', '--name-status', 'HEAD~1', 'HEAD'],
        capture_output=True, text=True
    )
    new_files = []
    for line in result.stdout.splitlines():
        parts = line.split('\t', 1)
        if len(parts) == 2 and parts[0] == 'A' and parts[1].endswith('.md'):
            new_files.append(parts[1])
    return new_files


def parse_front_matter(path):
    """Parse Jekyll front matter and return a dict of values."""
    with open(path, 'r', encoding='utf-8') as f:
        content = f.read()

    if not content.startswith('---'):
        return {}

    end = content.find('\n---', 3)
    if end == -1:
        return {}

    fm = {}
    for line in content[3:end].splitlines():
        if ':' in line:
            key, _, value = line.partition(':')
            fm[key.strip()] = value.strip().strip('"')
    return fm


def insert_into_master_list(master_path, title, link_path, manufacturer):
    """
    Insert a new row into the appropriate manufacturer table.
    Returns True if the file was modified.
    """
    with open(master_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Skip if already present
    if link_path in content:
        print(f'  Already in master list: {link_path}')
        return False

    anchor = MANUFACTURER_ANCHORS.get(manufacturer)
    if not anchor:
        print(f'  Unknown manufacturer "{manufacturer}", skipping.')
        return False

    # Find the section by its anchor
    section_idx = content.find('{#' + anchor + '}')
    if section_idx == -1:
        print(f'  Could not find section anchor #{anchor}')
        return False

    # Find the table header row within this section
    table_header_re = re.compile(r'^\|Game \|', re.MULTILINE)
    m = table_header_re.search(content, section_idx)
    if not m:
        print(f'  Could not find table header in section for {manufacturer}')
        return False

    # Skip past the header row and the separator row to find insertion point
    header_end = content.find('\n', m.end())
    separator_end = content.find('\n', header_end + 1)

    # Build the new table row and insert after the separator
    new_row = f'|[{title}](/{link_path}) | | | |\n'
    content = content[:separator_end + 1] + new_row + content[separator_end + 1:]

    with open(master_path, 'w', encoding='utf-8') as f:
        f.write(content)

    return True


def main():
    new_files = get_new_files()
    if not new_files:
        print('No new .md files in this commit.')
        return

    if not os.path.exists(MASTER_LIST_PATH):
        print(f'Master list not found at {MASTER_LIST_PATH}')
        return

    updated = False
    for filepath in new_files:
        # Only process files in manufacturer subdirs (docs/{manufacturer}/file.md)
        # Skip root-level docs files like rulesheet-master-list.md, index.md, etc.
        parts = filepath.replace('\\', '/').split('/')
        if len(parts) < 3 or parts[0] != 'docs':
            continue
        if filepath == MASTER_LIST_PATH:
            continue

        print(f'Processing new file: {filepath}')
        fm = parse_front_matter(filepath)

        title = fm.get('title', '').strip('"')
        manufacturer = fm.get('manufacturer', '').strip('"')

        if not title or not manufacturer:
            print(f'  Missing title or manufacturer in front matter, skipping.')
            continue

        mfr_dir = MANUFACTURER_DIRS.get(manufacturer)
        if not mfr_dir:
            print(f'  No directory mapping for manufacturer "{manufacturer}", skipping.')
            continue

        filename_stem = os.path.splitext(os.path.basename(filepath))[0]
        link_path = f'{mfr_dir}/{filename_stem}'

        if insert_into_master_list(MASTER_LIST_PATH, title, link_path, manufacturer):
            print(f'  Added: {title}')
            updated = True

    if updated:
        print('\nMaster list updated.')
    else:
        print('\nNo changes to master list.')


if __name__ == '__main__':
    main()
