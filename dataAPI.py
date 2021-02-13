import time
import urllib2
import json
import datetime

def getTickerData(stonks):

    tickerData = {}
    tickerString = ""

    for c in stonks:
        #url = 'https://www.alphavantage.co/query?function=GLOBAL_QUOTE&symbol={}&apikey=U0CROYL4SY1FJ1VS'.format(c)
        url = 'https://finnhub.io/api/v1/quote?symbol={}&token=***REMOVED***'.format(c)
        data = urllib2.urlopen(url).read()
        data = json.loads(data)
        #price = data['Global Quote']['05. price']
        #pct_ch = data['Global Quote']['10. change percent']
        price = data['c']
        prevclose = data['pc']
        pct_ch = "%.2f" % ((price/ prevclose -1)) * 100 + '%'
	tickerData[c] = {'price': price, 'pct_ch': pct_ch}

    return tickerData
