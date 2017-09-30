import bs4
from bs4 import BeautifulSoup
import urllib.request as urllib
import csv
from datetime import datetime

quote_page  = ['http://www.bloomberg.com/quote/SPX:IND', 'http://www.bloomberg.com/quote/CCMP:IND']


name = list()
price = list()
data = list()

for pg in quote_page:
    page  = urllib.urlopen(pg)
    soup = BeautifulSoup(page,'html.parser')
    name_box  = soup.find('h1',attrs={'class':'name'})
    name.append(name_box.text.strip())
    price_box = soup.find('div',attrs={'class':'price'})
    price.append(price_box.text)
    data.append((name,price))

with open('index1.csv','w') as csv_file:
    writer = csv.writer(csv_file)
    for name,price in data:
        writer.writerow([name,price,datetime.now()])
