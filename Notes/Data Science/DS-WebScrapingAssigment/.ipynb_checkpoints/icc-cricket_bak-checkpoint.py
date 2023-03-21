import requests
import pandas as pd
from bs4 import BeautifulSoup

header = {'user-agent': "mozilla/5.0 (macintosh; intel mac os x 10_15_7) applewebkit/537.36 (khtml, like gecko) chrome/96.0.4664.110 safari/537.36"}

def main(soup: BeautifulSoup, top: dict, other: dict, commonName: str, otherTable: str) -> tuple:
    #Finding Top Team's Name:
    top_table = soup.find_all("tr", top["top_team_table"])
    for i in top_table:
        top_name = i.find("td", top["top_team_name"])
        name = top_name.find("span", commonName).contents[0].strip()
        top_points = i.find("td", top["top_team_points"]).contents[0].strip()
        top_matches = i.find("td", top["top_team_matches"]).contents[0].strip()
        top_ratings = i.find("td", top["top_team_ratings"]).contents[0].strip()
        print(name, top_matches, top_points, top_ratings)
    other_table = soup.find_all("tr", otherTable)
    for i in other_table:
        other_name = i.find("td", other["other_team_name"])
        name = other_name.find("span", commonName).contents[0].strip()
        other_matches = i.findAll("td", other["other_team_matches"]) # Matches and Points have the same Class
        other_ratings = i.find("td", other["other_team_rating"]).contents[0].strip()
        print(name, other_matches[0].contents[0],other_matches[1].contents[0], other_ratings)
    return ()



if __name__ == "__main__":
    choice = int(input("1. Men's Cricket ODI Rantings\n2. Top 10 ODI Batsmen Records\n3. Top 10 ODI Bowler's Records: "))
    #URL = ""
    #soup: BeautifulSoup = BeautifulSoup()
    #top: dict = {}
    #other: dict = {}
    #common_class_name = ""
    #other_table_name = ""

    #common_class_name = "u-hide-phablet"
    #other_table_name = "table-body"
    #top = {
    #    "top_team_table" : "rankings-block__banner",
    #    "top_team_name" : "rankings-block__banner--team-name",
    #    "top_team_matches" : "rankings-block__banner--matches",
    #    "top_team_points" : "rankings-block__banner--points",
    #    "top_team_ratings" : "rankings-block__banner--rating u-text-right",
    #    "other_team_table" : "table-body"}
    #other = {
    #    "other_team_name" : "table-body__cell rankings-table__team",
    #    "other_team_matches" : "table-body__cell u-center-text",
    #    "other_team_points" : "table-body__cell u-center-text",
    #    "other_team_rating" : "table-body__cell u-text-right rating"}
    #content = soup.find_all("tr", top["top_team_table"])
    lst = []
    match choice:
        case 1:
            URL = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
            page = requests.get(URL, headers=header)
            soup = BeautifulSoup(page.content, 'html.parser')
            table = soup.find('table')
            table_rows = table.find_all('tr')[1:]
            names = ["Team", "Matches", "Points", "Rating"]
        case 2:
            URL = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting"
            page = requests.get(URL, headers=header)
            soup = BeautifulSoup(page.content, 'html.parser')
            table = soup.find('table')
            table_rows = table.find_all('tr')[1:]
            names = ["Player", "Team", "Rating", "Career Best Rating"]
        case 3:
            URL = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling"
            page = requests.get(URL, headers=header)
            soup = BeautifulSoup(page.content, 'html.parser')
            table = soup.find('table')
            table_rows = table.find_all('tr')[1:]
            names = ["Player", "Team", "Rating", "Career Best Rating"]

        case _:
            print("Invalid Input! Try Again")
            exit()
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
    print(df)
    #main(soup, top, other, common_class_name, other_table_name)
