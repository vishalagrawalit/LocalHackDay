import os
import requests
from tabulate import tabulate
from bs4 import BeautifulSoup

URL = "https://www.hackathon.com/city"
tabulate.WIDE_CHARS_MODE = True


def location():
    """To find the location of the current user using his ip address"""
    url = 'https://ipinfo.io/'
    data = requests.get(url).json()

    return data['city']


def make_soup(url):
    response = requests.get(url, verify=False).content
    soup = BeautifulSoup(response, 'lxml')

    return soup


def find_city():
    """Make a dictionary with city names
    """
    cities = {}
    soup = make_soup(URL)
    links = soup.find_all('a', {'class':'ht-all-card'})
    for link in links:
        name = os.path.basename(link.get('href'))
        cities[name] = link.get('href')

    return cities


def show_events(url):
    soup = make_soup(url)
    all_dates = []
    hackathons = []

    link1 = soup.find_all("a", {'class': 'ht-idt-card__title'})
    link2 = soup.find_all("a", {'class': 'ht-eb-card__title'})

    dates = soup.find_all("div", {'class': 'date date--start idea-ht-calendar-light'})
    hacks = link1 + link2

    for hack in hacks:
        title = hack.text
        ref = hack.get('href')
        hackathons.append([title, ref])

    for date in dates:
        text = date.text
        if 'Start' in text:
            text = text[5:]

        all_dates.append(text)

    for ind, h in enumerate(hackathons):
        h.append(all_dates[ind])

    return hackathons

def hackathon(user_city):
    headers = ['Name', 'URL', 'Date']
    user_city = user_city.replace(" ", "")
    cities = find_city()
    for city in cities:
        if user_city.lower() == city.lower():
            events = show_events(cities[city])
            print(tabulate(events, headers=headers, tablefmt='fancy_grid'))
            break

