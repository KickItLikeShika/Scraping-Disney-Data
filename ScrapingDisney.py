import re
import requests
from bs4 import BeautifulSoup as bs


r = requests.get('https://en.wikipedia.org/wiki/Toy_Story_3')

soup = bs(r.content)
# contents = soup.prettify()
# print(contents)

info_box = soup.find(class_="infobox vevent")
# print(info_box.prettify())

info_rows = info_box.find_all("tr")
# for row in info_box:
#     print(row.prettify())

# print(len(info_rows))


def get_content_value(row_data):
    if row_data.find('li'):
        return [i.get_text(" ", strip=True).replace('\xa0', ' ') for i in row_data.find_all('li')]
    else:
        return row_data.get_text(" ", strip=True).replace('\xa0', ' ')


movie_info = {}
for index, row in enumerate(info_rows):
    if index == 0:
        movie_info['Title'] = row.find('th').get_text(" ", strip=True)
    elif index == 1:
        continue
    else:
        content_key = row.find('th').get_text(" ", strip=True)
        content_value = get_content_value(row.find('td'))
        movie_info[content_key] = content_value

print(movie_info)
