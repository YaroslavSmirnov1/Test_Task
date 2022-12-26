from bs4 import BeautifulSoup
import requests
import re

# Загружаем список top 250 с IMDB
url = 'http://www.imdb.com/chart/top'
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")
movies = soup.select('td.titleColumn')
crew = [a.attrs.get('title') for a in soup.select('td.titleColumn a')]
ratings = [b.attrs.get('data-value')
           for b in soup.select('td.posterColumn span[name=ir]')]

# создаём пустой список для хранения информации о фильме
list = []

# итерируем фильмы, чтобы получить информацию о каждом отдельном фильме
for index in range(0, 5):
    # Разделяем на место, название, год
    movie_string = movies[index].get_text()
    movie = (' '.join(movie_string.split()).replace('.', ''))
    movie_title = movie[len(str(index)) + 1:-7]
    year = re.search('\((.*?)\)', movie_string).group(1)
    place = movie[:len(str(index)) - (len(movie))]
    data = {"place": place,
            "movie_title": movie_title,
            "rating": ratings[index],
            "year": year,
            "star_cast": crew[index],
            }
    list.append(data)

# выводим данные о фильме
for movie in list:
    print(movie['place'], '-', movie['movie_title'], '(' + movie['year'] +
          ') -', 'Starring:', movie['star_cast'], movie['rating'])


