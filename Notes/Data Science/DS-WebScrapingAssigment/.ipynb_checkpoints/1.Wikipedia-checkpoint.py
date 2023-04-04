import requests
from bs4 import BeautifulSoup

URL = "https://en.wikipedia.org/wiki/Main_Page"
header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
page = requests.get(url=URL, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')
headers = ['h1', 'h2', 'h3', 'h4', 'h5']
headings = soup.find_all(headers)
for heads in headings:
    print(heads.text)
