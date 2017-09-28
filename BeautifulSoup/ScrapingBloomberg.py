import bs4
from bs4 import BeautifulSoup
import urllib.request as urllib # in pycharm urllib2 as urllib.request

quote_page  = 'https://www.bloomberg.com/quote/SPX:IND'

page = urllib.urlopen(quote_page)                       # to get html page of the url declared

soup = BeautifulSoup(page,'html.parser')                # parsing the page to the BeautifulSoup format

name_box = soup.find('h1',attrs={'class':'name'})       # to take out he elements and its value
name = name_box.text.strip()

price_box = soup.find('div',attrs={'class':'price'})
price = price_box.text

print(name+' '+price)
