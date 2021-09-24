from datetime import datetime
import json

from parser_1 import parse as parser_1
from parser_2 import parse as parser_2
from parser_3 import parse as parser_3
from parser_4 import parse as parser_4


RSS_URL = 'https://www.pravda.com.ua/rss/view_news/'
feed = parse(RSS_URL)
urls = [
    'pravda.com.ua',
    'eurointegration.com.ua',
    'life.pravda.com.ua',
    'epravda.com.ua'
]
news = []
for item in feed.entries:
    data = {}
    data['title'] = item.title
    data['description'] = item.summary
    data['url'] = item.link
    data['date'] = f'{item.published_parsed[2]}.{item.published_parsed[1]}.{item.published_parsed[0]} - {item.published_parsed[3]}:{item.published_parsed[4]}:{item.published_parsed[5]}'
    if data['url'].split('/')[2][4:] == 'pravda.com.ua':
        data.update(parser_1(data['url']))
    if data['url'].split('/')[2][4:] == 'epravda.com.ua':
        data.update(parser_2(data['url']))
    if data['url'].split('/')[2][0:] == 'life.pravda.com.ua':
        data.update(parser_3(data['url']))
    if data['url'].split('/')[2][0:] == 'eurointegration.com.ua':
        data.update(parser_4(data['url']))
    news.append(data)

try:
    with open('news.json', 'w', encoding='utf8') as file:
        json.dump(news, file, indent=4, ensure_ascii=False)
except:
    pass
