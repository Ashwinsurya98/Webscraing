# -*- coding: utf-8 -*-
"""
Created on Sat Mar 30 18:34:36 2019

@author: Ashwin Surya
"""

import requests
from csv import DictWriter
from bs4 import BeautifulSoup
base_url=" "
url="/page/1"
all_quotes=[]
while url:
    resp=requests.get(f"{base_url}.{url}")
    soup=BeautifulSoup(resp.text,'html.parser')
    quote=soup.find_all(class_='quotes')
    for quote in quote:
        all_quotes.append({
                'text': quote.find(class_='text').get_text()
                'author': quote.select('.author').get_text()
                'bio_link': quote.find('a')['href']
                })
    net_btn=soup.find(class_='next')
    url=net_btn.find('a')['href'] if net_btn else none
print(all_quotes)
with open ("quotes.csv",w) as file:
    headers=['title','author','bio_link']
    csv_writer=DictWriter(file,filednames=headers)
    csv_writer.writeheader()
    for quote in quotes:
        csv_writer.writerow(quote)
        