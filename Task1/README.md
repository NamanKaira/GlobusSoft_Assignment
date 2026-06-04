# Amazon Laptop Data Scraper

## Overview

This project scrapes laptop product information from Amazon India and stores the extracted data in a timestamped CSV file.

The script uses Selenium to automate browser actions and collect product details from Amazon search results.

---

## Features

The scraper extracts the following information for each laptop:

- Product Title
- Product Price
- Product Rating
- Product Image URL
- Ad / Organic Result Status

The output file is automatically saved with a timestamp in its filename.

**Example Output File:**

```text
amazon_laptops_20260603_183012.csv
```

---

## Technologies Used

- Python
- Selenium
- Pandas
- WebDriver Manager

---

## Installation

Install the required dependencies:

```bash
pip install selenium pandas webdriver-manager
```

---

## How to Run

1. Clone or download this repository.
2. Open a terminal in the project folder.
3. Run the script:

```bash
python amazon_laptop_scraper.py
```

4. Wait for the scraping process to complete.
5. The output CSV file will be generated in the project directory.

---

## Output Format

The generated CSV file contains the following columns:

| Column Name | Description |
|------------|-------------|
| Title | Product title |
| Price | Product price |
| Rating | Product rating |
| Image | Product image URL |
| Result Type | Ad or Organic result |

---

## Project Workflow

1. Launch Chrome browser using Selenium.
2. Open Amazon India laptop search results page.
3. Extract product information.
4. Store data in a Python list.
5. Convert data into a Pandas DataFrame.
6. Generate a timestamped filename.
7. Save data as a CSV file.
8. Close the browser.

---

## Example Output

| Title | Price | Rating | Image | Result Type |
|---------|---------|---------|---------|---------|
| HP Laptop | 52990 | 4.3 out of 5 stars | Image URL | Organic |
| Dell Laptop | 64990 | 4.5 out of 5 stars | Image URL | Ad |

---

## Project Structure

```text
amazon-laptop-scraper/
│
├── amazon_laptop_scraper.py
├── README.md
├── requirements.txt
└── amazon_laptops_YYYYMMDD_HHMMSS.csv
```

---

## Requirements

Create a `requirements.txt` file containing:

```text
selenium
pandas
webdriver-manager
```

---

## Note

Amazon may occasionally update its website structure or display CAPTCHA verification pages. If this happens, some element locators (XPath/CSS selectors) may need to be updated accordingly.
