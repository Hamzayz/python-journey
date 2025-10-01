# type: ignore
import requests
from bs4 import BeautifulSoup

request = requests.get("https://news.ycombinator.com/")
web_data = request.text

soup = BeautifulSoup(web_data , "html.parser")

articles = soup.find(name="span")
print(articles.get("class"))


