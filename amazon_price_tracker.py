# -*- coding: utf-8 -*-
"""
Created on Thu Mar 12 23:25:35 2020

@author: Gautam
"""

import requests 
import smtplib

from bs4 import BeautifulSoup
URL = 'https://www.amazon.in/Apple-MacBook-13-inch-Storage-1-4GHz/dp/B07V3LTVHK/ref=sr_1_6?crid=23ZRB0GZO3JTE&keywords=apple+macbook+air&qid=1584035936&sprefix=apple+mac%2Caps%2C381&sr=8-6'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36'}

page = requests.get(URL, headers=headers)

soup = BeautifulSoup(page.content, 'html.parser')

title = soup.find(id ="productTitle").get_text()
price = soup.find(id="priceblock_ourprice").get_text()

converted_price = price[2:10]
converted_price = converted_price.replace(",", "")
converted__price = float(converted_price)
print(converted__price)

if(converted__price < 115000 ):
    server = smtplib.SMTP('smtp.gmail.com',587) 
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('gautammalh@gmail.com','yderjrlfejdkfakg')
    subject= 'Price fell down!'
    body = 'Check the amazon link https://www.amazon.in/Apple-MacBook-13-inch-Storage-1-4GHz/dp/B07V3LTVHK/ref=sr_1_6?crid=23ZRB0GZO3JTE&keywords=apple+macbook+air&qid=1584035936&sprefix=apple+mac%2Caps%2C381&sr=8-6'
    
    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
            'gautammalh@gmail.com',
            'gautammalh@gmail.com',
            msg
            )
    print('Hey Email is sent')
    
    server.quit()