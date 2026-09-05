import asyncio
from playwright.async_api import async_playwright
import pandas as pd


async def main():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=500)
        page = await browser.new_page()

        base_url = "https://freddymatch.org/agencies/AG-ZE04ZNO/volunteering-nt/"
        all_data = []
        page_num = 1

        while True:
            url = base_url if page_num == 1 else f"{base_url}?page={page_num}"
            print(f"📄 Page {page_num} scraping: {url}")

            await page.goto(url, wait_until="networkidle")
            await page.wait_for_timeout(2000)

            # Target all opportunity cards
            cards = await page.locator("div.col-sm-6.col-xl-4.mb-5").all()
            print(f"→ Found {len(cards)} opportunities on this page")

            if len(cards) == 0:
                print("No more cards found. Stopping.")
                break

            for card in cards:
                try:
                    # Title
                    title = await card.locator("h4.text-white").inner_text()

                    # Detail Link
                    link = await card.locator("a.tile-link").get_attribute("href")
                    full_url = "https://freddymatch.org" + link if link and link.startswith("/") else link

                    # Description
                    description = await card.locator("p.text-sm.text-muted").first.inner_text()

                    # Organization
                    org_text = await card.locator("p.text-sm.text-muted.mb-3").inner_text()
                    organization = org_text.replace("By", "").strip()

                    # Time Commitment
                    time_elem = card.locator("p.text-sm.mb-1:has-text('hours')")
                    time_commitment = await time_elem.inner_text() if await time_elem.count() > 0 else ""

                    # Age
                    age_elem = card.locator("p.text-sm.mb-1:has-text('years old')")
                    age = await age_elem.inner_text() if await age_elem.count() > 0 else ""

                    # Location
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
                    print(f"⚠️ Skipping one card due to error: {e}")
                    continue

            # Check for next page
            next_buttons = await page.locator("a.page-link[href*='page=']").all()
            has_next = False
            for btn in next_buttons:
                href = await btn.get_attribute("href")
                if href and f"page={page_num + 1}" in href:
                    has_next = True
                    break

            if not has_next:
                print("No more pages found.")
                break

            page_num += 1
            await page.wait_for_timeout(1500)

        # Save to CSV
        if all_data:
            df = pd.DataFrame(all_data)
            df.to_csv("volunteering_opportunities.csv", index=False, encoding="utf-8")
            print(f"\n🎉 Scraping Complete! Total Opportunities: {len(df)}")
            print("📁 File saved: volunteering_opportunities.csv")
        else:
            print("\n❌ No data scraped.")

        await page.wait_for_timeout(3000)
        await browser.close()


if __name__ == "__main__":
    asyncio.run(main())
