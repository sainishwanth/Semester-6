import requests
import pandas as pd
from bs4 import BeautifulSoup

URLS = ["https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc" ,"https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt"]

header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

lst = []

for url in URLS:
    print(url)
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    mainHead = soup.findAll("div", class_ = "lister-item mode-advanced")
    for i in mainHead:
        header = i.find("h3", "lister-item-header")
        name = header.find('a')
        rating = i.find("div", "inline-block ratings-imdb-rating").attrs.get("data-value", None)
        year = i.find("span", "lister-item-year text-muted unbold")
        lst.append([name.contents[0], rating, year.contents[0][1:5]])
df = pd.DataFrame(lst, columns=["Name", "Rating", "Year"])
print(df)
