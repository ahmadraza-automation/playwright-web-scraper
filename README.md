# Playwright Web Scraper with Pagination

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Async-green?logo=playwright)](https://playwright.dev/python/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/ahmadraza-automation/playwright-web-scraper?style=social)](https://github.com/ahmadraza-automation/playwright-web-scraper)

> Professional **Playwright (Async)** Python scraper that extracts volunteering opportunities with automatic pagination handling and clean CSV export.

---

## Features

- Fast & reliable **async Playwright** scraping
- Automatic **pagination** support (handles multiple pages)
- Extracts structured volunteering opportunity data
- Clean **CSV export** ready for analysis
- Easy to customize and extend
- Well-documented and maintainable code

---

## Tech Stack

| Technology       | Purpose                    |
|------------------|----------------------------|
| Python 3.8+      | Core language              |
| Playwright       | Browser automation (Async) |
| Pandas           | Data handling & CSV export |
| Chromium         | Headless browser           |

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ahmadraza-automation/playwright-web-scraper.git
cd playwright-web-scraper
```

2. Install dependencies:

```bash
pip install -r requirements.txt
# or
pip install playwright pandas
```

3. Install browser binaries:

```bash
playwright install chromium
```

---

## How to Run

```bash
python volunteering_scraper.py
```

The scraper will:

1. Open the target website
2. Automatically go through all pages
3. Extract volunteering opportunities
4. Save everything into a clean CSV file

---

## Sample Output

The final CSV contains structured data such as:

| Title | Organization | Location | Description | Link |
|-------|--------------|----------|-------------|------|
| ...   | ...          | ...      | ...         | ...  |

---

## Project Structure

```
playwright-web-scraper/
├── volunteering_scraper.py   # Main scraper script
├── requirements.txt          # Dependencies
├── README.md                 # This file
└── output/                   # CSV files will be saved here
```

---

## Customization

You can easily modify:

- Target URL
- Selectors for different websites
- Number of pages to scrape
- Output file name and format

---

## Author

**Ahmad Raza**  
Python Developer | Django | Playwright Automation Engineer  

- GitHub: [ahmadraza-automation](https://github.com/ahmadraza-automation)
- Portfolio: [Ahmad Raza Automation Portfolio](https://ahmadraza-automation.github.io/Ahmad-Raza-Automation-Portfolio/)

---

## Contributing

Feel free to open issues or submit pull requests if you want to improve this scraper!

---

## License

This project is open source and available under the [MIT License](LICENSE).
