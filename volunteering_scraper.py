import asyncio
import argparse
import logging
from pathlib import Path
from playwright.async_api import async_playwright
import pandas as pd

# -------------------------
# Logging Setup
# -------------------------
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S"
)
logger = logging.getLogger(__name__)


async def scrape_volunteering(base_url: str, headless: bool = False, max_pages: int = 50, output_file: str = "volunteering_opportunities.csv"):
    """
    Scrape volunteering opportunities with automatic pagination.
    """
    all_data = []

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=headless, slow_mo=300 if not headless else 0)
        page = await browser.new_page()

        page_num = 1

        while page_num <= max_pages:
            url = base_url if page_num == 1 else f"{base_url}?page={page_num}"
            logger.info(f"Scraping page {page_num}: {url}")

            try:
                await page.goto(url, wait_until="networkidle", timeout=30000)
                await page.wait_for_timeout(1500)
            except Exception as e:
                logger.error(f"Failed to load page {page_num}: {e}")
                break

            cards = await page.locator("div.col-sm-6.col-xl-4.mb-5").all()
            logger.info(f"Found {len(cards)} opportunities on page {page_num}")

            if len(cards) == 0:
                logger.info("No more cards found. Stopping.")
                break

            for card in cards:
                try:
                    title = await card.locator("h4.text-white").inner_text()

                    link = await card.locator("a.tile-link").get_attribute("href")
                    full_url = "https://freddymatch.org" + link if link and link.startswith("/") else (link or "")

                    description = await card.locator("p.text-sm.text-muted").first.inner_text()

                    org_text = await card.locator("p.text-sm.text-muted.mb-3").inner_text()
                    organization = org_text.replace("By", "").strip()

                    time_elem = card.locator("p.text-sm.mb-1:has-text('hours')")
                    time_commitment = await time_elem.inner_text() if await time_elem.count() > 0 else ""

                    age_elem = card.locator("p.text-sm.mb-1:has-text('years old')")
                    age = await age_elem.inner_text() if await age_elem.count() > 0 else ""

                    locations = await card.locator(".badge p").all_inner_texts()
                    location = " | ".join([loc.strip() for loc in locations if loc.strip()])

                    all_data.append({
                        "Title": title.strip(),
                        "Organization": organization,
                        "Description": description.strip(),
                        "Time_Commitment": time_commitment.strip(),
                        "Age": age.strip(),
                        "Location": location,
                        "Detail_URL": full_url,
                        "Page": page_num
                    })
                except Exception as e:
                    logger.warning(f"Skipping one card due to error: {e}")
                    continue

            # Check if next page exists
            next_buttons = await page.locator("a.page-link[href*='page=']").all()
            has_next = False
            for btn in next_buttons:
                href = await btn.get_attribute("href")
                if href and f"page={page_num + 1}" in href:
                    has_next = True
                    break

            if not has_next:
                logger.info("No more pages found.")
                break

            page_num += 1
            await page.wait_for_timeout(1000)

        await browser.close()

    # Save results
    if all_data:
        df = pd.DataFrame(all_data)
        df.to_csv(output_file, index=False, encoding="utf-8")
        logger.info(f"Scraping complete! Total opportunities: {len(df)}")
        logger.info(f"Saved to: {output_file}")
        return df
    else:
        logger.warning("No data scraped.")
        return None


def main():
    parser = argparse.ArgumentParser(
        description="Playwright Volunteering Opportunities Scraper with Pagination"
    )
    parser.add_argument(
        "--url",
        default="https://freddymatch.org/agencies/AG-ZE04ZNO/volunteering-nt/",
        help="Base URL of the volunteering page"
    )
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run browser in headless mode"
    )
    parser.add_argument(
        "--max-pages",
        type=int,
        default=50,
        help="Maximum number of pages to scrape"
    )
    parser.add_argument(
        "--output",
        default="volunteering_opportunities.csv",
        help="Output CSV filename"
    )

    args = parser.parse_args()

    logger.info("Starting Volunteering Scraper...")
    asyncio.run(scrape_volunteering(
        base_url=args.url,
        headless=args.headless,
        max_pages=args.max_pages,
        output_file=args.output
    ))


if __name__ == "__main__":
    main()
