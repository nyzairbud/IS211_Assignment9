import urllib2
from bs4 import BeautifulSoup

url = 'https://www.wunderground.com/history/airport/KNYC/2015/1/11/MonthlyHistory.html'
html = urllib2.urlopen(url)
soup = BeautifulSoup(html.read(), "lxml")


trs = soup.find_all('tr')

for tr in trs:
    for link in tr.find_all('a'):
        fulllink = link.get ('href')

    tds = tr.find_all("td")

    try:
        Date = int(tds[0].get_text())
        Temp = str(tds[2].get_text())

    except:
        print "bad tr string"
        continue

    print("Date: Jan ", Date, "Average Temp:", Temp.strip('\n'), 'degrees')