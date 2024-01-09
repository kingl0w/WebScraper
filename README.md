# Web Scraper

This project includes both synchronous and asynchronous versions of a web scraper script written in Python, which extracts information from websites listed in a CSV file and saves the data into JSON files.

## Overview

The web scraper retrieves information such as company names, addresses, phone numbers, and emails from a list of URLs provided in a CSV file. The script extracts data from the HTML content of the websites using BeautifulSoup and performs the following tasks:

- Reads a list of URLs from `urls.csv`
- Extracts data from each URL asynchronously (in the async version)
- Extracts data from each URL synchronously (in the sync version)
- Parses HTML content to extract relevant information
- Saves extracted information into JSON files in the `data/` directory

## Prerequisites

- Python 3.x
- Required Python packages (`requests`, `bs4`, `csv`)

## Usage

### Synchronous Version

1. Make sure you have the required packages installed (`requests`, `bs4`).
2. Run the `sync_scraper.py` script to scrape data synchronously:

### Asynchronous Version

1. Make sure you have the required packages installed (`aiohttp`, `asyncio`, `beautifulsoup4`).
2. Run the `async_scraper.py` script to scrape data asynchronously:

## File Structure

- `sync_scraper.py`: Contains the synchronous version of the web scraper.
- `async_scraper.py`: Contains the asynchronous version of the web scraper.
- `urls.csv`: CSV file containing URLs to scrape.
- `data/`: Directory to store JSON files with extracted information.

## Notes

- The CSV file should contain a column named `url` with the URLs to be scraped.
- Adjust the parsing logic in the scraper functions based on the HTML structure of the websites.

## License

This project is licensed under the [MIT License](LICENSE).
