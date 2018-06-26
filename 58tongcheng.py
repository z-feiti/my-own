# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re
import time

headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.62 Safari/537.36'
}

def get_links(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    for item in soup.find_all(class_="des"):
        list = item.select('a')
        if len(list) > 0:
            detail_link = list[0]['href']
            get_info(detail_link)

def get_info(url):
    wb_data = requests.get(url,headers=headers)
    soup = BeautifulSoup(wb_data.text,'lxml')
    tittles = soup.select(".f20")
    tittle = re.findall('>(.*?)<',str(tittles))
    print(tittle)
    prices = soup.select(".f36")
    price = re.findall('>(.*?)<',str(prices),re.S)
    print(price)
    addresses = soup.select(".addr")
    address = re.findall('>(.*?)<',str(addresses),re.S)
    print(address)
    phones = soup.select(".house-chat-txt")
    phone = re.findall('>(.*?)<',str(phones),re.S)
    print(phone)
    names = soup.select(".c_000")
    name = re.findall('>(.*?)<',str(names),re.S)
    print(name)
    print('=====================================')

if __name__ == '__main__':
    urls = ['http://wh.58.com/hongshan/chuzu/pn{}/?PGTID=0d3090a7-000a-5679-3ba0-2371721905bc&ClickID=2'.format(str(i)) for i in range(1,3)]
    for url in urls:
        get_links(url)
        time.sleep(5)

