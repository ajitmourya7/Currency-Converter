# write your code here!
import requests
import json


# user_input = input()
# data = requests.get('http://www.floatrates.com/daily/{}.json'.format(user_input))
# currency_data = json.loads(data.text)
# cache_data = {}
# for i in ["usd", "eur"]:
#     cache_data[i.lower()] = currency_data[i]


class CurrencyConvertor():
    server_url = "http://www.floatrates.com/daily/{}.json"
    main_currency = ''
    cache_data = {}

    def enter_currency(self):
        self.main_currency = input()
        data = requests.get(self.server_url.format(self.main_currency))
        server_currency_info = json.loads(data.text)
        for i in ["usd", "eur"]:
            try:
                self.cache_data[i.lower()] = server_currency_info[i]
            except:
                pass

    def request_from_server(self, currency_name):
        data = requests.get(self.server_url.format(self.main_currency))
        server_currency_info = json.loads(data.text)
        self.cache_data[currency_name.lower()] = server_currency_info[currency_name.lower()]
        return self.cache_data.get(currency_name.lower())['rate']

    def exchange_currency_name(self, name, amount):
        print("Checking the cache...")
        if self.cache_data.get(name.lower(), False):
            print("Oh! It is in the cache!")
            rate = self.cache_data.get(name.lower())['rate']
        else:
            print("Sorry, but it is not in the cache!")
            rate = self.request_from_server(name)
        print("You received {} USD.".format(round(amount * rate, 2)))

    def start(self):
        self.enter_currency()
        while True:
            name = input()
            if name == "":
                break
            amount = float(input())
            self.exchange_currency_name(name, amount)


CurrencyConvertor().start()
