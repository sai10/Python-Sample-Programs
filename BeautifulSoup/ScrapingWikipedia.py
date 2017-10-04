import urllib.request as urllib
from bs4 import BeautifulSoup

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

page = urllib.urlopen(wiki)

soup = BeautifulSoup(page,'html.parser')

#print(soup.prettify())

#print(soup.title)
#print(soup.title.string)
#print(soup.a)
#print(soup.find_all('a'))

all_links = soup.find_all('table')
for links in all_links:
    print(links)
