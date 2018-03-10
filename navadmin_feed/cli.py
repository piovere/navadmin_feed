# -*- coding: utf-8 -*-

import click
from navadmin_feed import *


@click.command()
def main(args=None):
    """Console script for navadmin_feed"""
    #click.echo("Replace this message by putting your code into "
    #           "navadmin_feed.cli.main")
    #click.echo("See click documentation at http://click.pocoo.org/")
    with open('navadmins.json', 'w') as f:
        json.dump(makefeed(YEAR), f, indent=4)


if __name__ == "__main__":
    main()
