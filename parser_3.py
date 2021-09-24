"""
'life.pravda.com.ua' parser
"""
from bs4 import BeautifulSoup
import requests
from pprint import pprint


def parse(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = {}
    data['name'] = soup.find('h1', class_='page-heading').text
    article = soup.find('article', class_='article')
    content = article.find('p')
    data['content'] = []
    data['preview'] = []
    data['content'].append({'p': content.text.strip()})

    while content != None:
        content = content.find_next_sibling()
        if content == None:
            break
        if content.name == 'p':
            if content.text.strip() == "Вас також може зацікавити:":
                break
            data['content'].append({'p': content.text.strip()})
        if content.name == 'table':
            data['preview'].append(
                {'img': 'https://life.pravda.com.ua' + content.find('img').get('src')})
    return data
