import requests
from bs4 import BeautifulSoup

URL_50 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc"
URL_100 = "https://www.imdb.com/search/title/?groups=top_100&sort=user_rating,desc&start=51&ref_=adv_nxt"

header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

page = requests.get(url=URL_50, headers=header)
page2 = requests.get(URL_100, headers=header)

soup = BeautifulSoup(page.content, 'html.parser')
soup2 = BeautifulSoup(page2.content, 'html.parser')

listings = soup.find_all("h3", class_="lister-item-header")
listings2 = soup2.find_all("h3", class_="lister-item-header")

count = 1
for links in listings:
    link = links.find_all("a")
    for title in link:
        print(f"{count} {title.contents[0]}")
        count += 1

for links in listings2:
    link = links.find_all("a")
    for title in link:
        print(f"{count} {title.contents[0]}")
        count += 1
