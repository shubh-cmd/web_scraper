import requests
from requests.exceptions import RequestException
from bs4 import BeautifulSoup
import json
from utils import Utils

def fetch_news_data():
    url = 'https://theverge.com'

    # Fetch the HTML data from the url
    try:
        res = requests.get(url)
        res.raise_for_status()
        return res
    except RequestException as e:
        print(e)

def parse_html_response(response):
    # Parse the response
    soup = BeautifulSoup(response.content, 'html.parser')
    return soup

def extract_script_tag_data(soup):
    # Find the JSON data available in script Tag
    result = soup.find(id = '__NEXT_DATA__').string

    # Loads the string into JSON data
    data = json.loads(result)

    # Find the news data 
    data = data['props']['pageProps']['hydration']['responses'][0]['data']

    return data


def get_required_data(data):
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

    return final_data        

if __name__=='__main__':
    response = fetch_news_data()
    soup = parse_html_response(response)
    data = extract_script_tag_data(soup)
    final_data = get_required_data(data)
    Utils.create_csv_file(final_data)
    Utils.create_database(final_data)