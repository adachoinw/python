import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
empire_webpage = response.text

soup = BeautifulSoup(empire_webpage, "html.parser")
movies = soup.find_all(name="h3", class_="title")

movie_titles = [title.getText() for title in movies]


with open("movie.txt", "w", encoding='utf-8') as file:
    movie_titles.reverse()
    [file.write(f"{t}\n") for t in movie_titles]







