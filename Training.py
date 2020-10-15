import re
import requests
from bs4 import BeautifulSoup as bs

r = requests.get("https://keithgalli.github.io/web-scraping/example.html")

soup = bs(r.content)

# print(soup.prettify())

first_header = soup.find("h2")
# print(first_header)

headers = soup.find_all("h2")
# print(headers)

headerss = soup.find_all(['h1', 'h2'])
# print(headerss)


ps = soup.find_all('p', attrs={'id': 'paragraph-id'})
# print(ps)

body = soup.find('body')
div = body.find('div')
# print(div.prettify())
h1 = div.find('h1')
# print(h1)


paras = soup.find_all('p', string=re.compile('Some'))
print(paras)
