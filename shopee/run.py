import requests
from bs4 import BeautifulSoup
import csv 
shope_url = 'https://shopee.co.id'
keyword = input('please enter the term :')
url = 'https://shopee.co.id/api/v4/search/search_items?by=relevancy&keyword={}&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2'.format(keyword)
header = {
'User-Agent' : 'Chrome',
'Referer': '{}search?keyword={}'.format(shope_url,keyword)
}
#API REQUEST
r=requests.get(url, headers=header).json()

#SCRAPING
col_list ,price_list,sold_list = [], [], []
for item in r['items']:
        col_list.append(item['item_basic']['name'])
        price_list.append(item['item_basic']['price'])
        sold_list.append(item['item_basic']['sold'])
print(item['item_basic']['name'])