import requests
import requests_cache
from bs4 import BeautifulSoup


requests_cache.install_cache('hackathon')

def colors(string, color):
    """Makes thing color full :)"""
    return "\033[1;%sm%s\033[0m" % (color, string)


def make_soup(url):
    """Make soup for us :)
    """
    response = requests.get(url, verify=False).content
    soup = BeautifulSoup(response, 'lxml')

    return soup
