# -*- coding: utf-8 -*-
"""Import list of current NAVADMINs and write them to a JSON feed.


"""

from datetime import date
import json
import requests
import bs4
from .message import Message


def fetch(year, msg_type):
    """Retrieve HTML table rows of NAVADMIN or ALNAV.
    
    Parameters
    ----------
    year : str
    msg_type : {'NAVADMIN', 'ALNAV'}

    Returns
    -------
    list
        List of table rows (beautifulsoup), each with message information
    
    """
    url = ("http://www.public.navy.mil/bupers-npc/"
           "reference/messages/{0}S/Pages/{0}{1}.aspx").format(
               msg_type,
               year
          )

    result = requests.get(url)

    soup = bs4.BeautifulSoup(result.text, 'html.parser')
    content = soup.find("div", {"class": "pageContent"})
    tbody = content.find("tbody")
    lines = tbody.findAll("tr")

    return lines[1:]

YEAR = 2018
MESSAGE_TYPES = [
    "ALNAV",
    "NAVADMIN"
]

def convert(line):
    """Convert table row into a Message object
    
    Parameters
    ----------
    line : str
        A beautifulsoup row containing information about a message.
    
    Returns
    -------
    Message
        A message object suitable for converting into feed item.
    
    """
    cells = line.findAll("td")
    msg = Message()
    msg.serial = cells[0].text
    msg.title = cells[1].text.title()
    msg.url = 'http://www.public.navy.mil' + cells[1].a['href']
    msg.date = cells[2].text

    return msg

def makefeed(year, msg_type):
    """Function docstring"""
    lines = fetch(year, msg_type)
    
    message_list = [convert(l) for l in lines]

    feed = {
        'version': 'https://jsonfeed.org/version/1',
        'title': 'Unofficial {} Feed'.format(msg_type),
        'home_page_url': ('http://www.public.navy.mil/bupers-npc/reference/'
                          'messages/{0}S/Pages/default.aspx'.format(msg_type)),
        'feed_url': 'https://techie.net/~piovere/{0}.json'.format(
            msg_type).lower()
    }

    items = [i.json_feed() for i in message_list]

    feed['items'] = items

    return feed

for m in MESSAGE_TYPES:
    fn = '{}s.json'.format(m.lower())
    with open(fn, 'w') as f:
        json.dump(makefeed(YEAR, m), f, indent=4)
