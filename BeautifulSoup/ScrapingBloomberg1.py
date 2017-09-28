import bs4
from bs4 import BeautifulSoup
import urllib.request as urllib

quote_page  = ['http://www.bloomberg.com/quote/SPX:IND', 'http://www.bloomberg.com/quote/CCMP:IND']


for pg in quote_page:
    page  = urllib.urlopen(pg)
    soup = BeautifulSoup(page,'html.parser')
    name_box  = soup.find('h1',attrs={'class':'name'})
    name = name_box.text.strip()
    price_box = soup.find('div',attrs={'class':'price'})
    price = price_box.text
    print(name+' '+price)
