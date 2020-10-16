import re
import requests
import json
import csv
from bs4 import BeautifulSoup as bs


def main():
    r = requests.get(
        'https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films')
    soup = bs(r.content)
    movies = soup.select('.wikitable.sortable i a')
    # print(movies[0:10])
    # print(type(movies))

    movie_info_list = scrap_wiki_disney(movies)

    # print(movie_info_list)

    save_data_csv('DisneyMovies.csv', movie_info_list)


def scrap_wiki_disney(movies):

    base_path = 'https://en.wikipedia.org/'
    movie_info_list = []

    for index, movie in enumerate(movies):
        try:
            relative_path = movie['href']
            full_path = base_path + relative_path
            title = movie['title']

            movie_info_list.append(get_info_box(full_path))

        except Exception as e:
            print(movie.get_text())
            print(e)

    return movie_info_list


def get_info_box(url):
    r = requests.get(url)
    soup = bs(r.content)
    info_box = soup.find(class_="infobox vevent")
    info_rows = info_box.find_all("tr")

    clean_tags(soup)

    movie_info = {}
    for index, row in enumerate(info_rows):
        if index == 0:
            movie_info['title'] = row.find("th").get_text(" ", strip=True)
        else:
            header = row.find('th')
            if header:
                content_key = row.find("th").get_text(" ", strip=True)
                content_value = get_content_value(row.find("td"))
                movie_info[content_key] = content_value

    return movie_info


def clean_tags(soup):
    for tag in soup.find_all(["sup", "span"]):
        tag.decompose()


def get_content_value(row_data):
    if row_data.find('li'):
        return [i.get_text(" ", strip=True).replace('\xa0', ' ') for i in row_data.find_all('li')]
    else:
        return row_data.get_text(" ", strip=True).replace('\xa0', ' ')


def save_data_json(title, data):
    with open(title, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=2)


def save_data_csv(title, data):
    keys = data[0].keys()
    with open(title, 'w', newline='') as file:
        dict_writer = csv.DictWriter(file, keys)
        dict_writer.writeheader()
        dict_writer.writerows(data)


if __name__ == "__main__":
    main()
