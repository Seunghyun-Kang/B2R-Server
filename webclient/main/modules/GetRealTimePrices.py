import requests, json, time 
from bs4 import BeautifulSoup 
from datetime import datetime

class RealTimePrice:
    def __init__(self):
        self.price = -1

    def get_price(self, company_code):
        url = "https://finance.naver.com/item/main.nhn?code=" + company_code 
        result = requests.get(url) 
        bs_obj = BeautifulSoup(result.content, "html.parser") 

        no_today = bs_obj.find("p", {"class": "no_today"}) 
        blind = no_today.find("span", {"class": "blind"}) 

        time = bs_obj.find("em", {"class": "date"}).text
        now_price = blind.text
        self.price = now_price
        return self.price , time
