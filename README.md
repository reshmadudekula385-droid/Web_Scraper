# Web_Scraper
Python Web Scraper using Beautiful soup.
# Web Scraper

A Python-based web scraper that extracts book information from Books to Scrape.

## Features

- Scrapes book details from 50 catalogue pages
- Extracts 1,000 book records
- Searches books by title
- Filters books by maximum price
- Filters books by rating
- Saves scraped data into a CSV file
- Handles invalid price input

## Data Collected

- Book Title
- Price
- Availability
- Rating
- Book URL

## Technologies Used

- Python
- Requests
- Beautiful Soup
- Pandas
- CSV

## How to Run

1. Install Python.
2. Install required libraries:
   - requests
   - beautifulsoup4
   - pandas
3. Open the project in VS Code.
4. Run `scraper.py`.
5. Select an option from the menu.

## Project Output

The scraped data is stored in:

`scraped_data.csv`

## Project Structure

```text
Web_Scraper/
│
├── scraper.py
├── scraped_data.csv
└── README.md
