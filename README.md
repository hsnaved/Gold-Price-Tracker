# Gold Price Tracker
**"Few lines of code help me to automate one of my daily tasks."**

## Overview

Gold Price Tracker is a Python project that automates the process of tracking daily prices for gold, silver, and platinum from [Lalitha Jewellery](https://www.lalithajewellery.com/). Instead of manually visiting the website and recording the prices every day, this script scrapes the data using BeautifulSoup, processes and cleans the data, and stores it in an Excel file for further analysis. This project is a testament to how a few lines of code can streamline repetitive tasks and empower smarter investment decisions.

## Features

- **Web Scraping:** Automatically scrapes daily prices for gold, silver, and platinum.
- **Data Processing:** Cleans and extracts the required price information.
- **Data Storage:** Saves the data in an Excel file (`gold_prices.xlsx`) and updates existing entries if data for the same day already exists.
- **Automation Ready:** Easily integrated with Windows Task Scheduler (or cron on macOS/Linux) to run automatically each day.

## Requirements

- **Python 3.x**

### Python Packages

- `requests`
- `beautifulsoup4`
- `urllib3`
- `pandas`
- `openpyxl` (for writing Excel files)

You can install these packages using pip:

```bash
pip install requests beautifulsoup4 urllib3 pandas openpyxl

Setup
Clone the Repository:

bash
 git clone https://github.com/yourusername/gold-price-tracker.git
 cd gold-price-tracker
 (Optional) Create and Activate a Virtual Environment:

Windows:
bash
python -m venv venv
 venv\Scripts\activate
macOS/Linux:
bash

python3 -m venv venv
source venv/bin/activate
Install Dependencies:

bash

pip install -r requirements.txt
Usage
Running the Script Manually
Execute the script with:

bash

python scraper.py
This will:

Scrape the current day's gold, silver, and platinum prices.
Store the data in gold_prices.xlsx.
Update the record if an entry for today already exists.
Automating the Process
On Windows:
Create a batch file (run_scraper.bat) in the project directory with the following content:

batch
@echo off
cd C:\Path\To\Your\gold-price-tracker
call venv\Scripts\activate
python scraper.py

Then, schedule the batch file to run daily using Windows Task Scheduler.

On macOS/Linux:
Set up a cron job. For example, to run the script every day at 7:00 AM, add the following line to your crontab (edit by running crontab -e):

bash
0 7 * * * cd /path/to/gold-price-tracker && source venv/bin/activate && python scraper.py

File Structure
bash

gold-price-tracker/
├── scraper.py           # Main Python script for scraping and updating the Excel file
├── requirements.txt     # List of Python dependencies
├── gold_prices.xlsx     # Excel file where data is stored (created/updated by the script)
└── README.md            # This file
License
This project is licensed under the MIT License. See the LICENSE file for details.

Acknowledgements
Thanks to Lalitha Jewellery for the gold price data.
Special thanks to the developers of the libraries used in this project.
