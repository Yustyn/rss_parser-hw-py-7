import requests
from bs4 import BeautifulSoup
from pprint import pprint

# URL = "https://scrapingclub.com/exercise/list_basic/?page=1"
# response = requests.get(URL)

# soup = BeautifulSoup(response.text, 'lxml')

# items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
# # pprint(len(items))

# for i, item in enumerate(items, start=1):
#     itemPrice = item.find('h5').text
#     # if float(itemPrice[1:]) > 50: continue
#     itemName = item.find('h4', class_="card-title").text.strip()
#     print(f"{i}: {itemPrice} -- {itemName}")


# pages = soup.find('ul', class_="pagination")
# urls = []
# links = pages.find_all('a', class_="page-link")

# for link in links:
#     pageNum = int(link.text) if link.text.isdigit() else None
#     if pageNum != None:
#         urls.append(link.get('href'))

# # pprint(urls)

# for link in urls:
#     newUrl = URL.replace('?page=1', link)
#     response = requests.get(newUrl)
#     soup = BeautifulSoup(response.text, 'lxml')
#     items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
#     for i, item in enumerate(items, start=i):
#         itemPrice = item.find('h5').text
#         # if float(itemPrice[1:]) > 50: continue
#         itemName = item.find('h4', class_="card-title").text.strip()
#         print(f"{i}: {itemPrice} -- {itemName}")

URL = "https://scrapingclub.com/"
params = {'page':1}

pages = 2
n = 1 

data_list = []
while params['page'] <= pages:
    response = requests.get(URL+"exercise/list_basic/", params=params)
    soup = BeautifulSoup(response.text, 'lxml')
    items = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')
# pprint(len(items))

    for n, item in enumerate(items, start=n):
        data = {}
        data['itemPrice'] = item.find('h5').text
        # if float(itemPrice[1:]) > 50: continue
        data['itemName'] = item.find('h4', class_="card-title").text.strip()
        data['itemImge'] = URL + item.find('img').get('src')[1:]
        data['itemDetailsLinke'] = URL + item.find('a').get('href')[1:]
        data_list.append(data)
    
    lastPageNum = int(soup.find_all('a', class_="page-link")[-2].text)
    pages = lastPageNum if pages < lastPageNum else pages
    params['page'] += 1

pprint(data_list)

