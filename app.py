from bs4 import BeautifulSoup
import requests
import pandas as pd
import wikipedia as wk

# Getting a list of article name from Wikipedia.

response = requests.get('https://en.wikipedia.org/wiki/Wikipedia:Vital_articles')
soup = BeautifulSoup(response.text, 'html.parser')

topics = []
for column in soup.findAll('div', {'class': 'column'}):
    for tag in column.findAll('a'):
        if 'Wikipedia:Vital' not in tag['title']:
            if ' ' in tag['title']:
                tmp_title = tag['title'].split(' ')
                topics.append('_'.join(tmp_title))
            else:
                topics.append(tag['title'])

print(f'Total No. of articles: {len(topics)}')
