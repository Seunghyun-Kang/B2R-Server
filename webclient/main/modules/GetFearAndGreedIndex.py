import http.client
import configparser as parser
import json

class FearAndGreedIndex:
    def __init__(self):
        self.__date = None
        self.__now_value = None
        self.__one_week_ago_value = None
        self.__one_month_ago_value = None
        self.__one_year_ago_value = None

        properties = parser.ConfigParser()
        properties.read('main/config.ini')
        self.api_key = properties['API_INFO']['rapid_api_key']
 
    @property
    def date(self):
        return self.__date
    
    @property
    def now_value(self):
        return self.__now_value

    @property
    def one_week_ago_value(self):
        return self.__one_week_ago_value

    @property
    def one_month_ago_value(self):
        return self.__one_month_ago_value

    @property
    def one_year_ago_value(self):
        return self.__one_year_ago_value
    
    def get_data(self):
        conn = http.client.HTTPSConnection("fear-and-greed-index.p.rapidapi.com")

        headers = {
            'X-RapidAPI-Key': self.api_key,
            'X-RapidAPI-Host': "fear-and-greed-index.p.rapidapi.com"
            }

        conn.request("GET", "/v1/fgi", headers=headers)

        res = conn.getresponse()
        data = res.read()
        decoded_response = data.decode("utf-8")
        json_data = json.loads(decoded_response)
        
        return json_data
    
    def parse_data(self, response):
        self.__date = response["lastUpdated"]["humanDate"].split('T')[0]
        self.__now_value = response["fgi"]["now"]["value"]
        self.__one_week_ago_value = response["fgi"]["oneWeekAgo"]["value"]
        self.__one_month_ago_value = response["fgi"]["oneMonthAgo"]["value"]
        self.__one_year_ago_value = response["fgi"]["oneYearAgo"]["value"]


