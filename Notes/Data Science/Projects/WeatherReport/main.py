import requests
import os
from bs4 import BeautifulSoup as bs

header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}
URL = "https://mausam.imd.gov.in/bengaluru/"

page = requests.get(URL, headers=header)
soup = bs(page.content, 'html.parser')

temp = soup.find("div", attrs = {"class": "temp", "id": "temperature"})

n = [t.text for t in temp]

print(f'{n[1]}{n[3]}')
