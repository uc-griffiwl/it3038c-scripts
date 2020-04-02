import requests, re
from bs4 import BeautifulSoup

data = requests.get("https://store.patmcafeeshow.com/products/ftbflag?variant=18082367078473").content
soup = BeautifulSoup(data, 'html.parser')
span = soup.find("h1", {"class":"page-header simple product-title large"})
title = span.text
span = soup.find("span", {"class":"money"})
price = span.text
span2 = soup.find("div", {"class":"form-field form-field-swatch swatch-other"})
colors = span2.text
print("Item %s has the price %s and the color options %s" % (title, price, colors))