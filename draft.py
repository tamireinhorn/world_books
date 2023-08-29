URL = "https://www.goodreads.com/review/list/71341746?ref=nav_mybooks"


import requests
from bs4 import BeautifulSoup

response = requests.get(URL)
soup = BeautifulSoup(response.content, "html.parser")
