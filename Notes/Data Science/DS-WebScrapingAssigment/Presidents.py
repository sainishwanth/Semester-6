import requests
from bs4 import BeautifulSoup

URL = "https://presidentofindia.nic.in/former-presidents.htm"
header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
page = requests.get(url=URL, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')
divs_presidents = soup.find_all("div", class_ = "presidentListing")
print(divs_presidents)
for content in divs_presidents:
    presidents = content.find_all('h3')
    for president in presidents:
        print(president.contents[0])
