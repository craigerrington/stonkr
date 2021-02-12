import time
import urllib2
import json
import datetime

def getTickerData(stonks):

    tickerData = {}
    tickerString = ""

    for c in stonks:
        url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey=***REMOVED***'.format(c)
        data = urllib2.urlopen(url).read()
        data = json.loads(data)
        price = data['Global Quote']['05. price']
        pct_ch = data['Global Quote']['10. change percent']
        tickerData[c] = {'price': price, 'pct_ch': pct_ch}

    return tickerData
