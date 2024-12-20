# Amazon-Price-Scraper# Amazon Price Scraper

This is a simple Python script to scrape product prices from Amazon using BeautifulSoup and Requests. The script checks the price of a specific product on Amazon and appends the title, price, and date to a CSV file (`AmazonDataset.csv`). The script runs in an infinite loop, checking the price every 5 seconds.

## Features

- Scrapes the product title, price, and date.
- Saves the scraped data to a CSV file (`AmazonDataset.csv`).
- Runs continuously to check the price at regular intervals (every 5 seconds).
- Writes headers to the CSV file only once, and appends new data each time it runs.

## Requirements

Before you begin, ensure you have the following installed:

- Python 3.x
- pip (Python's package installer)

### Python Libraries

You will need to install the following libraries:

- `requests`
- `beautifulsoup4`
- `pandas`

You can install the required libraries using the following command:

```bash
pip install requests beautifulsoup4 pandas
