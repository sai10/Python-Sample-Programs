import bs4
from bs4 import BeautifulSoup
import urllib.request as urllib
import pandas as pd

wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"

page = urllib.urlopen(wiki)

soup = BeautifulSoup(page,'html.parser')

right_table = soup.find('table', class_='wikitable sortable plainrowheaders')

a=[]
b=[]
c=[]
d=[]
e=[]
f=[]
g=[]

for row in right_table.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th')                #   To store second column data
    if len(cells)==6:                       #   Only extract table body not heading
        a.append(cells[0].find(text=True))
        b.append(states[0].find(text=True))
        c.append(cells[1].find(text=True))
        d.append(cells[2].find(text=True))
        e.append(cells[3].find(text=True))
        f.append(cells[4].find(text=True))
        g.append(cells[5].find(text=True))

df = pd.DataFrame(a,columns=['Number'])

df['Stste/UT'] = b
df['Admin_Capital']=c
df['Legislative_Capital']=d
df['Judiciary_Capital']=e
df['Year_Capital']=f
df['Former_Capital']=g
print(df)
