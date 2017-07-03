"""
Contains the Message class, which represents items for export to a JSON feed
"""
from datetime import date


class Message(object):
    """
    Attributes
    ----------
    None
    """
    def __init__(self):
        self._date = None
        self._serial = None
        self._title = None
        self._url = None

    def __repr__(self):
        rep = u'{0}: {1}'.format(
            self.serial,
            self.title
        )
        return rep.encode('utf-8')

    def __unicode__(self):
        return self.__repr__

    @property
    def date(self):
        """str: Returns string version of item date (stored internally as
            datetime.date)
        """
        return self._date.strftime('%Y-%m-%d')

    @date.setter
    def date(self, d):
        d = d.replace(u'\u200b', '')
        d_split = d.split('/')
        self._date = date(int(d_split[2]), int(d_split[0]), int(d_split[1]))

    @property
    def serial(self):
        """str: the serial number of the object formatted ###/yy"""
        return self._serial

    @serial.setter
    def serial(self, s):
        self._serial = s.replace(u'\u200b', '')

    @property
    def title(self):
        """str: title of the item"""
        return self._title

    @title.setter
    def title(self, t):
        self._title = t.replace(u'\u200b', '')

    @property
    def url(self):
        """str: url linking to the full message"""
        return self._url

    @url.setter
    def url(self, u):
        self._url = u.replace(u'\u200b', '')

    def json_feed(self):
        """Exports the message to a dict suitable as an item in a JSONfeed
        """
        item = {
            "id": self.serial,
            "content_text": self.title,
            "url": self.url,
            "date_published": self.date,
            "title": self.title
        }
        return item
