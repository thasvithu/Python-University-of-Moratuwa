import requests
import json

import sys
sys.path.insert(0,'bs4.zip')
from bs4 import BeautifulSoup

#Imitate the Mozilla browser.
user_agent = {'User-agent': 'Mozilla/5.0'}


def compare_prices(product_laughs,product_glomark):
    laughs_req = requests.get(product_laughs)
    laughs_soup = BeautifulSoup(laughs_req.content, 'html.parser')

    glomark_req = requests.get(product_glomark)
    glomark_soup = BeautifulSoup(glomark_req.content, 'html.parser')
    
    product_name_laughs = laughs_soup.find("div",{"class":"product-name"}).text.strip()
    product_name_glomark = glomark_soup.find("div",{"class":"product-title"}).text.strip()
    
    price_laughs = float(laughs_soup.find("span",{"class":"regular-price"}).text.strip()[3:])
    price_glomark = float(json.loads(glomark_soup.find("script",{"type":"application/ld+json"}).text.strip())['offers'][0]['price'])
    
    print('Laughs  ',product_name_laughs,'Rs.: ' , price_laughs)
    print('Glomark ',product_name_glomark,'Rs.: ' , price_glomark)
    
    if(price_laughs>price_glomark):
        print('Glomark is cheaper Rs.:',price_laughs - price_glomark)
    elif(price_laughs<price_glomark):
        print('Laughs is cheaper Rs.:',price_glomark - price_laughs)   
    else:
        print('Price is the same')