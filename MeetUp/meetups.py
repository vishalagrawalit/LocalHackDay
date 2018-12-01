from bs4 import BeautifulSoup
import requests
from tabulate import tabulate


def make_url(city, genre):
    url = "https://www.meetup.com/find/events/" + genre.lower() + "/?allMeetups=true&radius=Infinity&userFreeform=+" + \
        city.lower() + "+%2C+India&mcId=z1018091&mcName=" + city.lower() + "%2C+IN"

    return url


def get_html(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")

    return soup


def get_event_list(soup):
    data = soup.find_all('li', class_="row event-listing clearfix doc-padding ")
    columns = ["S.No", "Group", "Time", "Event Name"]
    table = []
    for i in range(len(data)):
        if len(table) <= 5:
            new = data[i].find_all("a")
            group = new[1].find("span").contents[0].encode(encoding='UTF-8', errors='strict').decode('utf-8')
            time = new[0].find("time").contents[0].encode(encoding='UTF-8', errors='strict').decode('utf-8')
            event_name = new[-1].find("span").contents[0].encode(encoding='UTF-8', errors='strict').decode('utf-8')

            table.append([i + 1, group, time, event_name])

    print(tabulate(table, headers=columns, tablefmt='fancy_grid'))


def main(city, genre):
    url = make_url(city, genre)
    soup = get_html(url)
    get_event_list(soup)
