
# import requests
# from bs4 import BeautifulSoup
# import csv
 
# key = 'hotels'
# location = 'london'
# url = 'https://www.yell.com/ucs/UcsSearchAction.do?scrambleSeed=1673388186&keywords={}&location={}&pageNum='.format(key, location)
# headers = {
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36'
# }
# req = requests.get(url,headers=headers)
# print(req.status_code)

from bs4 import BeautifulSoup
import requests
 
key = 'hotels'
location = 'london'
user_agent = {'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.97 Safari/537.36'}
source = requests.get("https://www.hltv.org/", headers=user_agent)
print(source.status_code)