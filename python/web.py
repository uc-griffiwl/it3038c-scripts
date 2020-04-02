import requests, re
from bs4 import BeautifulSoup

r = requests.get('https://analytics.usa.gov').content
soup = BeautifulSoup(r, "lxml")
print(type(soup))
print(soup.prettyify()[:100])
for link in soup.find_all('a'): print(link.get('href'))
