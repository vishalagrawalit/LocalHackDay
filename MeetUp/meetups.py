from common import make_soup
from common import colors
from tabulate import tabulate


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
    tables = tabulate(table, headers=columns, tablefmt='fancy_grid')
    print(tables)
    return tables


def main(city, genre):
    url = "https://www.meetup.com/find/events/" + genre.lower() + "/?allMeetups=true&radius=Infinity&userFreeform=+" + \
        city.lower() + "+%2C+India&mcId=z1018091&mcName=" + city.lower() + "%2C+IN"

    soup = make_soup(url)
    get_event_list(soup)
