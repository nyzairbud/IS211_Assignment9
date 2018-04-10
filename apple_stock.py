import urllib2
from bs4 import BeautifulSoup
import json

url = 'https://finance.yahoo.com/quote/AAPL/history?ltr=1'
html = urllib2.urlopen(url)
soup = BeautifulSoup(html.read(), "lxml")


def stockprices():

    filein = soup.find_all('tr')

    for row in filein:
        try:
            date = row.contents[0].get_text()
            closeprice = row.contents[4].get_text()
            print('Date: ', json.dumps(date.strip('')), 'Close Price: ', json.dumps(closeprice))
        except:
            print 'bad string format'
            continue


if __name__ == "__main__":
    stockprices()