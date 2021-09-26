#!/usr/bin/env python
# coding: utf-8

import requests
import json


def getStockData(symbol):
    
    url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey=J4LGNJ0S224FFPU1'.format(symbol)
    #print(url)
    r = requests.get(url)
    data = r.json()
    json_object = json.dumps(data, indent = 4, sort_keys=True) 
    
    return json_object


def main():
    while(1):
        symbol = input('input stock symbol, to exit please input "quit":')
        if symbol == 'quit':
            break
        data = getStockData(symbol)
        print(data)
        
        dict_obj = json.loads(data)
        
        output = 'The current price of {} is: {}'.format(dict_obj['Global Quote']['01. symbol'], dict_obj['Global Quote']['05. price'])
        print(output)


main()

