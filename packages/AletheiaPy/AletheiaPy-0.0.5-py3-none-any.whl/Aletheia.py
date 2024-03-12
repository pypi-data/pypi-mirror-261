import requests
import json

class Client:
    def __init__(self, key):
        self.key = key
        self.base = "https://api.aletheiaapi.com/"
    
    def StockData(self, symbol, fields = ''):
        url = self.base + f"StockData?key={self.key}&symbol={symbol}"
        if len(fields) > 0: url = url + f'&{fields}'

        return json.loads(requests.get(url).text)

    def Crypto(self, symbol):
        url = self.base + f"Crypto?key={self.key}&symbol={symbol}"
        
        return json.loads(requests.get(url).text)

    def consumption(self):
        url = self.base + f"v2/consumption?key={self.key}"

        return requests.get(url).text

    def version(self):
        
        return requests.get(self.base + "version").text