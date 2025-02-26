import requests
from bs4 import BeautifulSoup
url = "https://books.toscrape.com/catalogue/a-light-in-the-attic_1000/index.html"
page = requests.get(url)

soup = BeautifulSoup(page.content, "html.parser")

#See html source
#print(page.content)

titles=soup.find("h1").text
print(titles)

