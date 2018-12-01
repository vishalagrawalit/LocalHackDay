from __future__ import print_function
from apiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

import datetime
import requests
import requests_cache
from bs4 import BeautifulSoup

requests.packages.urllib3.disable_warnings()
requests_cache.install_cache('hackathon')


def handle_event(table):
    """ Gets the credential and then authorize them
    """
    credential = get_credentials()
    event = make_events(table)
    service = build('calendar', 'v3', http=credential.authorize(Http()))
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(colors(('Event created: %s' % (event.get('htmlLink'))), 32))


def get_credentials():
    """This gets your credentials from credentials.json file"""
    SCOPES = 'https://www.googleapis.com/auth/calendar'
    store = file.Storage('credentials.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('client_secret.json', SCOPES)
        creds = tools.run_flow(flow, store)

    return creds


def colors(string, color):
    """Makes thing color full :)"""
    return "\033[1;%sm%s\033[0m" % (color, string)


def make_soup(url):
    """Make soup for us :)
    """
    response = requests.get(url, verify=False).content
    soup = BeautifulSoup(response, 'lxml')

    return soup


def make_events(table):
    """Makes a dictionary that have
        summary     Name of the tournament
        start       Starting time of the tournament
        end         Finishing time of the tournametn

        This dictionary is send to google calendar for adding an event.
    """
    row_num = input("Enter the row number for the tournament you want to add: ")
    event = {}
    for tournament in table:
        if int(row_num) == tournament[0]:
            event['summary'] = tournament[1]
            print(tournament[3])
            event['start'] = {'dateTime': RFC_time(tournament[3])}
            event['end'] = {'dateTime': RFC_time(tournament[4])}
            return event
    else:
        print(colors(("No tournament exists with id %s" % row_num), 31))


def epoch_time(time):
    """Takes milliseconds and then change it to epoch time
        :time: float value of time in milliseconds
        :return: epoch time format
    """
    date_time = datetime.datetime.fromtimestamp(time).strftime('%a, %d %b %Y %H:%M:%S')
    return date_time


def RFC_time(epoch_time: str):
    """Takes time in form of UTC and then change it into rfc 3339 time

        :epoch_time: string of epoch format i.e Thu, 26 Jul 2018 19:30:00
        :return: string of rfc 3339 format i.e 2018-07-26T19:30:00Z
    """
    rfc_time = datetime.datetime.strptime(epoch_time, '%a, %d %b %Y %H:%M:%S').isoformat("T") + "Z"
    return rfc_time
