#!/usr/bin/env python3
"""
fix_table_spacing.py - Add a blank line above Markdown tables that need one.

GitHub Pages (kramdown) does not render a table as a table unless there is
a blank line between it and the text directly above it. This script finds
every table under docs/ that is missing that blank line and inserts one.

A table is detected by its separator row (for example |---|---| or
:--|--:) directly under a header row. Tables inside fenced code blocks
are left alone. Running the script more than once changes nothing.

Usage:
    python scripts/fix_table_spacing.py
"""

import re
import subprocess
import sys


# A separator row: cells of dashes with optional colons, split by pipes.
# At least one pipe is required so front matter (---) never matches.
SEPARATOR_RE = re.compile(
    r'^\s*\|?\s*:?-+:?\s*(\|\s*:?-+:?\s*)+\|?\s*$'
    r'|^\s*\|\s*:?-+:?\s*\|\s*$'
)
FENCE_RE = re.compile(r'^\s*(```|~~~)')


def is_blank(line):
    return line.strip() == ''


def fix_lines(lines):
    """Return (new_lines, count) with a blank line added above each table."""
    out = []
    fixes = 0
    in_fence = False

    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            in_fence = not in_fence

        # When the next line is a separator, this line is a table header.
        next_line = lines[i + 1] if i + 1 < len(lines) else ''
        is_header = (
            not in_fence
            and '|' in line
            and not line.startswith('    ')
            and SEPARATOR_RE.match(next_line)
        )

        if is_header and out and not is_blank(out[-1]):
            ending = line[len(line.rstrip('\r\n')):] or '\n'
            out.append(ending)
            fixes += 1

        out.append(line)

    return out, fixes


def markdown_files():
    result = subprocess.run(
        ['git', 'ls-files', 'docs/*.md'],
        capture_output=True, text=True, check=True,
    )
    return [path for path in result.stdout.splitlines() if path]


def main():
    total = 0
    for path in markdown_files():
        with open(path, encoding='utf-8', newline='') as f:
            lines = f.read().splitlines(keepends=True)

        new_lines, fixes = fix_lines(lines)
        if fixes:
            with open(path, 'w', encoding='utf-8', newline='') as f:
                f.write(''.join(new_lines))
            print(f"{path}: added {fixes} blank line(s) above tables")
            total += fixes

    if total == 0:
        print("No tables needed a blank line.")
    return 0


if __name__ == '__main__':
    sys.exit(main())
