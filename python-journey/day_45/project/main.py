#type: ignore
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

requests = requests.get(URL)
data = requests.text

soup = BeautifulSoup(data , "html.parser")

top100 = [movie.get_text() for movie in soup.find_all(name="h3" , class_="title")]
top100.reverse()

with open("day-45/project/top100-movies.txt" , "a" , encoding="utf-8") as movie_file:
    for movie in top100:
        movie_file.write(movie + "\n")
