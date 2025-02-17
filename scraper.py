import requests
from bs4 import BeautifulSoup
import urllib3
import re
import pandas as pd
from datetime import datetime


def add_data_to_excel(file_path, date, gold_price, silver_price, platinum_price):
    # Try reading the existing Excel file; if it doesn't exist, create a new DataFrame
    try:
        df = pd.read_excel(file_path)
    except FileNotFoundError:
        df = pd.DataFrame(columns=["Date", "Gold Price", "Silver Price", "Platinum Price"])
    
    # If an entry with the same date exists, update (override) the row.
    if date in df["Date"].values:
        df.loc[df["Date"] == date, ["Gold Price", "Silver Price", "Platinum Price"]] = [gold_price, silver_price, platinum_price]
    else:
        # Otherwise, create a new row and append it to the DataFrame.
        new_data = pd.DataFrame([[date, gold_price, silver_price, platinum_price]],
                                columns=["Date", "Gold Price", "Silver Price", "Platinum Price"])
        df = pd.concat([df, new_data], ignore_index=True)
    
    # Save the DataFrame back to the Excel file.
    df.to_excel(file_path, index=False)


urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

url = "https://www.lalithaajewellery.com/"

response = requests.get(url, verify=False) # to bypass SSL Certificate seurity checks 
soup = BeautifulSoup(response.text,"html.parser")

price_tag= soup.find("a",attrs={"data-toggle": "modal", "data-target": "#price"})

# print(price_tag)


if(price_tag):
    price_text = price_tag.get_text(strip=True) # extract text and removes extra spaces
    # print("raw text: ",price_text)

    prices=price_text.split('|')

    # print(prices)

    gold_price = re.sub(r'[^\d.]','',prices[0].split("=")[-1].strip()) # gets gold price
    silver_price = re.sub(r'[^\d.]','',prices[1].split("=")[-1].strip())  # Extract Silver price
    platinum_price = re.sub(r'[^\d.]','',prices[2].split("=")[-1].strip())  # Extract Platinum price

    # If the number has no decimal point, remove any decimal point before the digits
    if gold_price.count('.') == 1 :
        gold_price = gold_price.split('.')[1]+' Rs'
    else:
        gold_price = gold_price.split('.')[1]+'.'+gold_price.split('.')[2]+' Rs'

    if silver_price.count('.') == 1 :
        silver_price = silver_price.split('.')[1]+' Rs'
    else:
        silver_price = silver_price.split('.')[1]+'.'+silver_price.split('.')[2]+' Rs'
    
    if platinum_price.count('.') == 1 :
        platinum_price = platinum_price.split('.')[1]+' Rs'
    else:
        platinum_price = platinum_price.split('.')[1]+'.'+platinum_price.split('.')[2]+' Rs'

     # Print extracted prices
    print("22K Gold Price:", gold_price)
    print("Silver Price:", silver_price)
    print("Platinum Price:", platinum_price)

    today=datetime.today().strftime('%Y-%m-%d')

    # data={
    #     "Date" : [today],
    #     "Gold Price" : [gold_price],
    #     "Silver Price" : [silver_price],
    #     "Platinum Price" : [platinum_price]
    # }

    # df = pd.DataFrame(data)
     # Path to your Excel file
    excel_file = "gold_prices.xlsx"

    # Add the extracted data to the Excel file
    add_data_to_excel(excel_file, today, gold_price, silver_price, platinum_price)
    print(f"✅ Prices saved successfully in Excel!")

else:
    print("Metal prices not found!")





