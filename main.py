import requests
from bs4 import BeautifulSoup
import json
import csv
from datetime import date as dt
import sqlite3
from utils import Utils

url = 'https://theverge.com'

# Fetch the HTML data from the url
res = requests.get(url)

# Parse the response
soup = BeautifulSoup(res.content, 'html.parser')

# Find the JSON data available in script Tag
result = soup.find(id = '__NEXT_DATA__').string

# Loads the string into JSON data
data = json.loads(result)

# Find the news data 
data = data['props']['pageProps']['hydration']['responses'][0]['data']

# Create list of the news data found
final_data = []
counter = 0

for d in data['community']['frontPage']['placements']:
    
    if 'placeable' in d:
        obj = d['placeable']
        
        if obj is not None:
            id = counter
            url = obj['url']
            headline = obj['title']
            author = obj['author']['fullName']
            date = obj['publishDate']

            arr = [id, url, headline, author, date]

            final_data.append(arr)

            counter += 1
        

Utils.create_csv_file(final_data)
Utils.create_database(final_data)

