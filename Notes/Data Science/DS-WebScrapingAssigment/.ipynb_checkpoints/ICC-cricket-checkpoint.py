import requests
import pandas as pd
from bs4 import BeautifulSoup

header = {'user-agent': "mozilla/5.0 (macintosh; intel mac os x 10_15_7) applewebkit/537.36 (khtml, like gecko) chrome/96.0.4664.110 safari/537.36"}
URL = ""
lst = []
names = []

choice = int(input("1. Men's Cricket ODI Rantings\n2. Top 10 ODI Batsmen Records\n3. Top 10 ODI Bowler's Records: "))
match choice:
    case 1:
        URL = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
        names = ["Team", "Matches", "Points", "Rating"]
    case 2:
        URL = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting"
        names = ["Player", "Team", "Rating", "Career Best Rating"]
    case 3:
        URL = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling"
        names = ["Player", "Team", "Rating", "Career Best Rating"]

    case _:
        print("Invalid Input! Try Again")


page = requests.get(URL, headers=header)
soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table')
table_rows = table.find_all('tr')[1:]


for tr in table_rows[:10]:
    td = tr.find_all('td')
    row = [i.text.strip() for i in td if str(i)]
    lst.append(row)

for i in lst:
    try:
        i.pop(0)
    except:
        continue


df = pd.DataFrame(lst,columns=names)
df.to_csv('ICC.csv')
print(df)
