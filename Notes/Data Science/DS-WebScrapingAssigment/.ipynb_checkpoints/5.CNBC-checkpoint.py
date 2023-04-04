import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = "https://www.cnbc.com/world/?region=world:"
header = {'User-Agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36"}

page = requests.get(URL, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')
lst = []

# Headline News
headline = soup.find("h2", class_ = "FeaturedCard-packagedCardTitle").find("a")
lst.append(["0 hours ago",headline.contents[0], headline['href']])

# Latest News
count = 1
latest_header = soup.find_all("div", class_ = "LatestNews-headlineWrapper")
for headings in latest_header:
    time = headings.find("time", "LatestNews-timestamp").contents[0]
    heading = headings.find('a')
    lst.append([time,heading.contents[0], heading['href']])

# Preprocessing
df = pd.DataFrame(lst, columns=["Time", "Article", "Link"])
drop_lst = []
count = 0
for i in df["Link"]:
    if i[0] != 'h':
        drop_lst.append(count)
    count += 1

new_df = df.drop(df.index[drop_lst])
new_df
new_df.to_csv('CNBC.csv')
print(new_df.head(10))

