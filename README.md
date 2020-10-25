# Scraping Disney Data

Scraping Wikipedia pages with some Data Science techniques, BeautifulSoup, requests, JSON, and CSV to gather data about           Disney movies and create a dataset for it.

The data is totally clean, But there is some missing values you have to handle them before analyze the data.

The data is available in CSV format. I thought it wasn't necessary to provide the data in a JSON format.

Wikipedia disney movies link:
https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films

# Startegy

- Making a GET request to: https://en.wikipedia.org/wiki/List_of_Walt_Disney_Pictures_films

- Get the content of the page by BeautifulSoup and go through all the film list by taking 'https://en.wikipedia.org/' as a base path,
  get the realtive path for each film, combine them to create the full path, and make a GET request for each path.

- Get the content of each page, work with the info box `infobox vevent`, and get all the info about the film from the info box.

- Then save the data to a JSON file to make it faster and easier 'to save us time by just loading the JSON file instead of making a get requests to wikipedia pages' while cleaning the data.

- Go through the data and clean it.

- Convert the data to a CSV file and save it.
