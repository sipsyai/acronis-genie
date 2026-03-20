"""
Fuzzy match CSHID entries from scraped TOC to local markdown docs.

Input:  data/cshid_mapping.json + docs/**/*.md frontmatter titles
Output: data/doc_url_mapping.json + data/cshid_unmatched.json
"""

import json
import re
from difflib import SequenceMatcher
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
DOCS_DIR = BASE_DIR / "docs"

MATCH_THRESHOLD = 0.70
REVIEW_THRESHOLD = 0.50


def extract_frontmatter_title(path: Path) -> str:
    """Extract title from YAML frontmatter."""
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\n(.+?)\n---", text, re.DOTALL)
    if not match:
        return ""
    for line in match.group(1).splitlines():
        if line.startswith("title:"):
            return line.split(":", 1)[1].strip().strip('"').strip("'")
    return ""


def normalize(text: str) -> str:
    """Normalize text for comparison."""
    return re.sub(r'[^a-z0-9\s]', '', text.lower()).strip()


def main():
    # Load CSHID mapping
    cshid_path = DATA_DIR / "cshid_mapping.json"
    if not cshid_path.exists():
        print(f"ERROR: {cshid_path} not found. Run scrape_acronis_toc.py first.")
        return

    with open(cshid_path) as f:
        cshid_entries = json.load(f)

    print(f"Loaded {len(cshid_entries)} CSHID entries")

    # Collect all doc files with their titles
    doc_files = {}
    chapter_dirs = sorted([d for d in DOCS_DIR.iterdir() if d.is_dir() and d.name[0].isdigit()])
    for d in chapter_dirs:
        for md_file in sorted(d.glob("*.md")):
            rel_path = f"{d.name}/{md_file.name}"
            title = extract_frontmatter_title(md_file)
            if title:
                doc_files[rel_path] = title

    print(f"Found {len(doc_files)} doc files with titles")

    # Fuzzy match
    mapping = {}
    unmatched = []
    review = []

    for entry in cshid_entries:
        cshid_title = entry["title"]
        cshid_norm = normalize(cshid_title)
        best_score = 0.0
        best_path = None

        for rel_path, doc_title in doc_files.items():
            doc_norm = normalize(doc_title)
            score = SequenceMatcher(None, cshid_norm, doc_norm).ratio()
            if score > best_score:
                best_score = score
                best_path = rel_path

        if best_score >= MATCH_THRESHOLD:
            mapping[best_path] = {
                "page": entry.get("page", ""),
                "doc_url": entry["url"],
                "match_score": round(best_score, 4),
                "toc_title": cshid_title,
                "doc_title": doc_files[best_path],
            }
        elif best_score >= REVIEW_THRESHOLD:
            review.append({
                "toc_title": cshid_title,
                "best_match_path": best_path,
                "best_match_title": doc_files.get(best_path, ""),
                "score": round(best_score, 4),
                "url": entry["url"],
            })
        else:
            unmatched.append({
                "title": cshid_title,
                "best_score": round(best_score, 4),
                "url": entry["url"],
            })

    # Save results
    DATA_DIR.mkdir(exist_ok=True)

    mapping_path = DATA_DIR / "doc_url_mapping.json"
    with open(mapping_path, "w") as f:
        json.dump(mapping, f, indent=2, ensure_ascii=False)
    print(f"\nMatched: {len(mapping)} docs → {mapping_path}")

    unmatched_path = DATA_DIR / "cshid_unmatched.json"
    combined_unmatched = {"needs_review": review, "no_match": unmatched}
    with open(unmatched_path, "w") as f:
        json.dump(combined_unmatched, f, indent=2, ensure_ascii=False)
    print(f"Unmatched: {len(unmatched)} (+ {len(review)} for review) → {unmatched_path}")

    # Summary
    total_docs = len(doc_files)
    mapped = len(mapping)
    print(f"\nCoverage: {mapped}/{total_docs} docs mapped ({mapped/total_docs*100:.1f}%)")


if __name__ == "__main__":
    main()
