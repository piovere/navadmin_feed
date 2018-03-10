# -*- coding: utf-8 -*-
"""Import list of current NAVADMINs and write them to a JSON feed.


"""

from datetime import date
import json
import requests
import bs4
from message import Message


def fetch(year):
    """Function docstring"""
    url = ("http://www.public.navy.mil/bupers-npc/"
           "reference/messages/NAVADMINS/Pages/NAVADMIN{0}.aspx").format(year)

    result = requests.get(url)

    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    content = soup.find("div", {"class": "pageContent"})
    tbody = content.find("tbody")
    lines = tbody.findAll("tr")

    return lines[1:]

YEAR = 2018

def convert(line):
    """Function docstring"""
    cells = line.findAll("td")
    msg = Message()
    msg.serial = cells[0].text
    msg.title = cells[1].text.title()
    msg.url = 'http://www.public.navy.mil' + cells[1].a['href']
    msg.date = cells[2].text

    return msg

def makefeed(year):
    """Function docstring"""
    lines = fetch(year)

    message_list = [convert(l) for l in lines]

    feed = {
        'version': 'https://jsonfeed.org/version/1',
        'title': 'Unofficial NAVADMIN Feed',
        'home_page_url': ('http://www.public.navy.mil/bupers-npc/reference/'
                          'messages/NAVADMINS/Pages/default.aspx'),
        'feed_url': 'https://piovere.net/navadmins.json'
    }

    items = [i.json_feed() for i in message_list]

    feed['items'] = items

    return feed

with open('navadmins.json', 'w') as f:
    json.dump(makefeed(YEAR), f, indent=4)
