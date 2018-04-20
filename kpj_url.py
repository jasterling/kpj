import requests
from bs4 import BeautifulSoup
#import re


# scrape the urls into a list

url = 'http://web.mta.info/developers/turnstile.html'
r = requests.get(url)
html_doc = r.text
soup = BeautifulSoup(html_doc, 'lxml')
container = soup.find('div', class_='span-84 last')
#links = container.find_all('a', href=True)

links_list = []
for a in container.find_all('a', href=True):
    links_list.append(a['href'])

print(len(links_list))

#%%
import pandas as pd

df = pd.read_csv('http://web.mta.info/developers/'+links_list[0])

for x in range(1,3):
    df.append('http://web.mta.info/developers/'+x)

print(df.info())


#%%

for x in range(2): ### continue here...
    url = 'http://web.mta.info/developers/'+x
    r = requests.get(url)
    mtadata_1 = r.text
    
    
# from here will need to create the df with the first and append with the rest...
# large file so limit size for initial review

#%%
#import pandas as pd
#import numpy as np

# df it
df = pd.read_csv('http://web.mta.info/developers/data/nyct/turnstile/turnstile_180407.txt', delimiter = ',')
print(df.head())

# reduce size
df['ENTRIES'] = df['ENTRIES'].astype('int32')
df['EXITS'] = df['EXITS'].astype('int32')

# https://stackoverflow.com/questions/5815747/beautifulsoup-getting-href
