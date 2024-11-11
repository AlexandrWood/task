import requests
from bs4 import BeautifulSoup
import json

url = 'https://quotes.toscrape.com'


def parse_page(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    info = soup.find_all('div', class_='quote')
    data = {
        'info': [quote.get_text(strip=True) for quote in info]
    }
    return data


response = requests.get(url, verify=False)
soup = BeautifulSoup(response.content, 'html.parser')
top_ten = soup.find_all('span', class_='tag-item')
top_ten_tags = [item.get_text(strip=True) for item in top_ten]

all_data = {
    'top_ten': [top_ten_tags],
    'pages': []
}

for page in range(1, 11):
    url_to_parse = f'{url}/page/{page}'
    page_data = parse_page(url_to_parse)
    all_data['pages'].append(page_data)
with open('data.json', 'w', encoding='utf-8') as json_file:
    json.dump(all_data, json_file, ensure_ascii=False, indent=4)
