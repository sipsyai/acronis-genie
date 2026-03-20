"""
Scrape Acronis Cyber Protect Cloud TOC to extract CSHID mappings.
Uses standalone playwright (pip install playwright && playwright install chromium).

Output: data/cshid_mapping.json
"""

import asyncio
import json
import re
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"

TOC_URL = "https://www.acronis.com/en/support/documentation/CyberProtectionService/"


async def scrape_toc():
    from playwright.async_api import async_playwright

    results = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page()

        print(f"Navigating to {TOC_URL}...")
        await page.goto(TOC_URL, wait_until="networkidle", timeout=60000)

        # Wait for TOC sidebar to render
        await page.wait_for_selector("a[href*='cshid=']", timeout=30000)
        print("TOC loaded, expanding collapsed sections...")

        # Expand all collapsed sections (click toggles)
        expand_attempts = 0
        while expand_attempts < 10:
            toggles = await page.query_selector_all(
                ".tree-toggle:not(.expanded), "
                "[data-toggle]:not(.open), "
                ".expandable:not(.expanded), "
                "details:not([open]), "
                ".collapsed > .toggle, "
                "[aria-expanded='false']"
            )
            if not toggles:
                break
            for toggle in toggles:
                try:
                    await toggle.click()
                    await asyncio.sleep(0.1)
                except Exception:
                    pass
            expand_attempts += 1
            await asyncio.sleep(0.5)

        print("Extracting CSHID links...")

        # Extract all links with cshid
        links = await page.query_selector_all("a[href*='cshid=']")
        print(f"Found {len(links)} links with cshid")

        for link in links:
            href = await link.get_attribute("href") or ""
            text = (await link.inner_text()).strip()

            # Extract cshid value
            match = re.search(r'cshid=(\d+)', href)
            if not match:
                continue

            cshid = match.group(1)

            # Try to get parent section
            section = ""
            try:
                parent = await link.evaluate_handle(
                    "el => el.closest('li')?.closest('ul')?.closest('li')?.querySelector('a,span')?.textContent?.trim() || ''"
                )
                section = await parent.json_value()
            except Exception:
                pass

            results.append({
                "cshid": cshid,
                "title": text,
                "section": section,
                "url": f"https://www.acronis.com/en/support/documentation/CyberProtectionService/#cshid={cshid}",
            })

        await browser.close()

    # Deduplicate by cshid
    seen = set()
    unique = []
    for r in results:
        if r["cshid"] not in seen:
            seen.add(r["cshid"])
            unique.append(r)

    print(f"Extracted {len(unique)} unique CSHID entries")
    return unique


def main():
    results = asyncio.run(scrape_toc())

    DATA_DIR.mkdir(exist_ok=True)
    out_path = DATA_DIR / "cshid_mapping.json"
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)

    print(f"Saved to {out_path}")


if __name__ == "__main__":
    main()
