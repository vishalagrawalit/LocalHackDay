from bs4 import BeautifulSoup
import requests
from prettytable import PrettyTable


def make_url(city, genre):

    url = "https://www.meetup.com/find/events/" + genre.lower() + "/?allMeetups=true&radius=Infinity&userFreeform=+" + \
        city.lower() + "+%2C+India&mcId=z1018091&mcName=" + city.lower() + "%2C+IN"
    get_html(url)


def get_html(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    get_event_list(soup)


def get_event_list(soup):
    data = soup.find_all('li', class_="row event-listing clearfix doc-padding ")
    columns = ["S.No", "Group", "Time", "Event Name"]
    table = PrettyTable(columns)

    for i in range(len(data)):
        try:
            if i == 5:
                break
            new = data[i].find_all("a")
            table.add_row([i + 1, new[1].find("span").contents[0].encode(encoding='UTF-8', errors='strict'),
                           new[0].find("time").contents[0].encode(encoding='UTF-8', errors='strict'),
                           new[-1].find("span").contents[0].encode(encoding='UTF-8', errors='strict')])
        except:
            print("EXCEPTION")

    print(table)
