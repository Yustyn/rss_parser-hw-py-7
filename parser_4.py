"""
'eurointegration.com.ua' parser
"""
from bs4 import BeautifulSoup
import requests
from pprint import pprint


def parse(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    data = {}
    article = soup.find('article', class_='post')

    header = article.find('h1', class_='post__title')
    content = article.find('div', class_='post__text')
    data['header'] = []
    data['content'] = []
    data['header'].append(header)
    element = content.find('p')
    data['content'].append(({'p': element.text.strip()}))
    while element != None:
        element = element.find_next_sibling()
        if element == None:
            break
        if element.name == 'p':
            data['content'].append({'p': element.text.strip()})
    pprint(data)
    return data


if __name__ == '__main__':
    parse('https://www.eurointegration.com.ua/news/2021/09/24/7128223/')
