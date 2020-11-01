import requests
from bs4 import BeautifulSoup

response = requests.get('https://news.ycombinator.com/')

soup = BeautifulSoup(response.text, "html.parser")

print(soup.find(id='score_24176898'))