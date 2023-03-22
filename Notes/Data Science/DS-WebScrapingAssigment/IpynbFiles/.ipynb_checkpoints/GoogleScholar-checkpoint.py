import requests
import pandas as pd
from bs4 import BeautifulSoup

URL = "https://scholar.google.com/citations?view_op=top_venues&h1=en"
header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

page = requests.get(URL, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')

table_rows = soup.find('table', class_="gsc_mp_table").find_all('tr')
lst = []
for table in table_rows[1:]:
    rank = table.find('td', "gsc_mvt_p").contents[0]
    publication = table.find('td', "gsc_mvt_t").contents[0]
    h5 = table.find_all("td", "gsc_mvt_n")
    h5_index = h5[0].find('a').contents[0]
    h5_median = h5[1].find('span').contents[0]
    lst.append([rank, publication, h5_index, h5_median])

df = pd.DataFrame(lst, columns=["Rank", "Publicaiton", "h5-index", "h5-median"])
df.to_csv('GoogleScholar.csv')
print(df.head(10))
