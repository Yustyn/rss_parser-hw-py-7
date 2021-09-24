"""
'epravda.com.ua' parser
"""
from bs4 import BeautifulSoup
import requests
from pprint import pprint


def parse(url):

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'lxml')
    div_content = soup.find('div', class_='article_content')
    data = {}
    photo = div_content.find('div', class_='image-box image-box_center')
    if photo.find('img'):
        data['preview'] = photo.find('img').get('src')
    else:
        data['preview'] = None
    content = div_content.find('div', class_='post__text')
    data['content'] = []
    elem = content.find('p')
    data['content'].append({'p': elem.text.strip()})

    while elem != None:
        elem = elem.find_next_sibling()
        if elem == None:
            break
        if elem.name == 'p':
            data['content'].append({'p': elem.text})
        elif elem.name == 'div' and 'image-box' in elem['class']:
            img = elem.find('img')
            if img == None:
                continue
            data['content'].append({'img': 'https:' + img.get('src')})
    return data
