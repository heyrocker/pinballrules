#!/usr/bin/env python3
"""
clean_html.py - Convert HTML in Markdown files to pure Markdown.

Scans .md files for inline HTML tags and converts them to their
Markdown equivalents. Jekyll front matter (--- delimiters) is preserved unchanged.

Usage:
    python scripts/clean_html.py docs/
"""

import html
import os
import re
import sys


HTML_TAG_RE = re.compile(r'<[a-zA-Z/][^>]*>')


def has_html(text):
    """Return True if text contains HTML tags."""
    return bool(HTML_TAG_RE.search(text))


def split_front_matter(content):
    """
    Split a Jekyll file into (front_matter, body).
    front_matter includes the --- delimiters.
    If no front matter, returns ('', content).
    """
    if content.startswith('---'):
        end = content.find('\n---', 3)
        if end != -1:
            front = content[:end + 4]  # include closing ---
            body = content[end + 4:]
            return front, body
    return '', content


def convert_html(content):
    """Convert common HTML elements to Markdown equivalents."""

    # Block headings with optional id attribute
    def block_heading(m):
        level = int(m.group(1))
        attrs = m.group(2)
        inner = re.sub(r'<[^>]+>', '', m.group(3)).strip()
        heading = '#' * level + ' ' + html.unescape(inner)
        id_match = re.search(r'\bid=["\']([^"\']+)["\']', attrs)
        if id_match:
            heading += ' {#' + id_match.group(1) + '}'
        return heading

    content = re.sub(
        r'^<h([1-6])([^>]*)>(.*?)</h\1>\s*$',
        block_heading,
        content,
        flags=re.IGNORECASE | re.DOTALL | re.MULTILINE,
    )

    # Link-wrapped headings [<hN>text</hN>](url)
    def linked_heading(m):
        level = int(m.group(1))
        inner = html.unescape(re.sub(r'<[^>]+>', '', m.group(2))).strip()
        url = m.group(3)
        return '#' * level + ' [' + inner + '](' + url + ')'

    content = re.sub(
        r'^\[<h([1-6])[^>]*>(.*?)</h\1>\]\(([^)]*)\)\s*$',
        linked_heading,
        content,
        flags=re.IGNORECASE | re.DOTALL | re.MULTILINE,
    )

    # Bold
    content = re.sub(r'<(b|strong)>(.*?)</(b|strong)>', r'**\2**',
                     content, flags=re.IGNORECASE | re.DOTALL)
    # Italic
    content = re.sub(r'<(i|em)>(.*?)</(i|em)>', r'*\2*',
                     content, flags=re.IGNORECASE | re.DOTALL)
    # Links
    content = re.sub(
        r'<a\s+(?:[^>]*?\s+)?href=["\']([^"\']+)["\'][^>]*>(.*?)</a>',
        r'[\2](\1)',
        content,
        flags=re.IGNORECASE | re.DOTALL,
    )
    # Images
    content = re.sub(
        r'<img\s+[^>]*?src=["\']([^"\']+)["\'][^>]*/?>',
        r'![](\1)',
        content,
        flags=re.IGNORECASE,
    )
    # Line breaks
    content = re.sub(r'<br\s*/?>', '\n', content, flags=re.IGNORECASE)
    # Paragraphs
    content = re.sub(r'<p[^>]*>(.*?)</p>', r'\1\n\n',
                     content, flags=re.IGNORECASE | re.DOTALL)
    # Inline heading tags (e.g. inside table cells)
    content = re.sub(
        r'<h[1-6][^>]*>(.*?)</h[1-6]>',
        lambda m: html.unescape(re.sub(r'<[^>]+>', '', m.group(1))).strip(),
        content,
        flags=re.IGNORECASE | re.DOTALL,
    )

    # Ensure blank line between headings and immediately following tables
    content = re.sub(r'(^#{1,6} .+$)\n(\|)', r'\1\n\n\2', content, flags=re.MULTILINE)

    # Strip any remaining HTML tags
    content = re.sub(r'<[^>]+>', '', content)

    # Decode remaining HTML entities
    content = html.unescape(content)

    return content


def clean_file(path):
    """Clean a single .md file. Returns True if the file was modified."""
    with open(path, 'r', encoding='utf-8') as f:
        original = f.read()

    front_matter, body = split_front_matter(original)

    if not has_html(body):
        return False

    cleaned_body = convert_html(body)

    if cleaned_body == body:
        return False

    with open(path, 'w', encoding='utf-8') as f:
        f.write(front_matter + cleaned_body)

    return True


def main(root):
    changed = []
    for dirpath, _, filenames in os.walk(root):
        for fname in filenames:
            if fname.endswith('.md'):
                path = os.path.join(dirpath, fname)
                if clean_file(path):
                    changed.append(path)
                    print(f'Cleaned: {path}')

    if changed:
        print(f'\n{len(changed)} file(s) cleaned.')
    else:
        print('No HTML found, nothing to do.')


if __name__ == '__main__':
    root = sys.argv[1] if len(sys.argv) > 1 else '.'
    main(root)