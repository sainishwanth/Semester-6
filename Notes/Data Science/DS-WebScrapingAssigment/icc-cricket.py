import requests
from bs4 import BeautifulSoup

header = {'user-agent': "mozilla/5.0 (macintosh; intel mac os x 10_15_7) applewebkit/537.36 (khtml, like gecko) chrome/96.0.4664.110 safari/537.36"}

def main():
    pass




if "__main__" == "__name__":
    choice = int(input(print("1. Men's Cricket ODI Rantings\n2. Top 10 ODI Batsmen Records\n3. Top 10 ODI Bowler's Records")))
    URL = ""
    match choice:
        case 1:
            URL = "https://www.icc-cricket.com/rankings/mens/team-rankings/odi"
        case 2:
            URL = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/batting"
        case 3:
            URL = "https://www.icc-cricket.com/rankings/mens/player-rankings/odi/bowling"
        case _:
            print("Invalid Input")
            exit()
    main()
