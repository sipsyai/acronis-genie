"""
Inject doc_url into markdown frontmatter based on doc_url_mapping.json.

Uses regex-based insertion (safer than YAML round-trip which reformats).
Inserts `doc_url: "..."` before the closing `---`.
"""

import json
import re
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DOCS_DIR = BASE_DIR / "docs"


def main():
    mapping_path = DATA_DIR / "doc_url_mapping.json"
    if not mapping_path.exists():
        print(f"ERROR: {mapping_path} not found. Run match_cshid_to_docs.py first.")
        return

    with open(mapping_path) as f:
        mapping = json.load(f)

    print(f"Loaded {len(mapping)} doc URL mappings")

    updated = 0
    skipped = 0

    for rel_path, info in mapping.items():
        file_path = DOCS_DIR / rel_path
        if not file_path.exists():
            print(f"  SKIP (not found): {rel_path}")
            skipped += 1
            continue

        text = file_path.read_text(encoding="utf-8")

        # Check if doc_url already exists
        if "doc_url:" in text.split("---", 2)[1] if text.startswith("---") and text.count("---") >= 2 else False:
            print(f"  SKIP (already has doc_url): {rel_path}")
            skipped += 1
            continue

        doc_url = info["doc_url"]

        # Insert doc_url before the closing --- of frontmatter
        # Pattern: find the second --- and insert before it
        match = re.match(r"(^---\n.+?)\n(---)", text, re.DOTALL)
        if not match:
            print(f"  SKIP (no frontmatter): {rel_path}")
            skipped += 1
            continue

        new_text = f'{match.group(1)}\ndoc_url: "{doc_url}"\n{match.group(2)}{text[match.end():]}'
        file_path.write_text(new_text, encoding="utf-8")
        updated += 1
        print(f"  Updated: {rel_path}")

    print(f"\nDone. Updated: {updated}, Skipped: {skipped}")


if __name__ == "__main__":
    main()
