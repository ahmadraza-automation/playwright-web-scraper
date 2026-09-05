# Playwright Web Scraper with Pagination

[![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Playwright](https://img.shields.io/badge/Playwright-Async-green?logo=playwright)](https://playwright.dev/python/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Stars](https://img.shields.io/github/stars/ahmadraza-automation/playwright-web-scraper?style=social)](https://github.com/ahmadraza-automation/playwright-web-scraper)

> Professional **Playwright (Async)** Python scraper that extracts volunteering opportunities with automatic pagination handling and clean CSV export.

---

## Demo Video

[![Watch the Demo](https://img.shields.io/badge/▶_Watch_Demo-red?style=for-the-badge)](https://github.com/ahmadraza-automation/playwright-web-scraper/blob/main/Create_a_short_second_sc.mp4)

Watch the full working demo → [Create_a_short_second_sc.mp4](https://github.com/ahmadraza-automation/playwright-web-scraper/blob/main/Create_a_short_second_sc.mp4)

---

## Features

- Fast & reliable **async Playwright** scraping
- Automatic **pagination** support
- Clean **CSV export**
- Command-line arguments support (`--headless`, `--max-pages`, `--output`)
- Proper logging
- Easy to customize for other websites
- MIT Licensed

---

## Tech Stack

| Technology   | Purpose                    |
|--------------|----------------------------|
| Python 3.8+  | Core language              |
| Playwright   | Browser automation (Async) |
| Pandas       | Data handling & CSV export |
| Chromium     | Browser                    |

---

## Installation

```bash
git clone https://github.com/ahmadraza-automation/playwright-web-scraper.git
cd playwright-web-scraper
pip install -r requirements.txt
playwright install chromium
```

---

## How to Run

### Basic usage
```bash
python volunteering_scraper.py
```

### Headless mode (no browser window)
```bash
python volunteering_scraper.py --headless
```

### Limit number of pages
```bash
python volunteering_scraper.py --max-pages 5
```

### Custom output file
```bash
python volunteering_scraper.py --output my_data.csv
```

### All options together
```bash
python volunteering_scraper.py --headless --max-pages 10 --output results.csv
```

---

## Command Line Options

| Option         | Description                          | Default                                      |
|----------------|--------------------------------------|----------------------------------------------|
| `--url`        | Target website URL                   | FreddyMatch volunteering page                |
| `--headless`   | Run without opening browser window   | `False`                                      |
| `--max-pages`  | Maximum pages to scrape              | `50`                                         |
| `--output`     | Output CSV filename                  | `volunteering_opportunities.csv`             |

---

## Sample Output

| Title | Organization | Location | Description | Detail_URL | Page |
|-------|--------------|----------|-------------|------------|------|
| ...   | ...          | ...      | ...         | ...        | ...  |

---

## Project Structure

```
playwright-web-scraper/
├── volunteering_scraper.py      # Main scraper (CLI supported)
├── requirements.txt             # Dependencies
├── Create_a_short_second_sc.mp4 # Demo video
├── LICENSE                      # MIT License
├── .gitignore
└── README.md
```

---

## Author

**Ahmad Raza**  
Python Developer | Django | Playwright Automation Engineer  

- GitHub: [ahmadraza-automation](https://github.com/ahmadraza-automation)
- Portfolio: [Ahmad Raza Automation Portfolio](https://ahmadraza-automation.github.io/Ahmad-Raza-Automation-Portfolio/)

---

## Contributing

Pull requests are welcome. Feel free to open issues for bugs or feature requests.

---

## License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.
