#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_navadmin_feed
----------------------------------

Tests for `navadmin_feed` module.
"""

import pytest

from contextlib import contextmanager
from click.testing import CliRunner

from navadmin_feed import navadmin_feed
from navadmin_feed import cli


# Request the NAVADMIN page
def test_finds_a_page_at_the_url():
    assert navadmin_feed.fetch("2017") == 250


@pytest.fixture(params=["2017", "2016", "2015"])
def response(f):
    """Sample pytest fixture.
    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    import requests

    url = ("http://www.public.navy.mil/bupers-npc/"
           "reference/messages/NAVADMINS/Pages/NAVADMIN{0}.aspx").format(
               f.param
    )
    return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_content(response):
    """Sample pytest test function with the pytest fixture as an argument.
    """
    from bs4 import BeautifulSoup
    assert 'NAVADMIN' in BeautifulSoup(response.content).title.string


def test_command_line_interface():
    """Click command line testing
    """
    runner = CliRunner()
    result = runner.invoke(cli.main)
    assert result.exit_code == 0
    assert 'navadmin_feed.cli.main' in result.output
    help_result = runner.invoke(cli.main, ['--help'])
    assert help_result.exit_code == 0
    assert '--help  Show this message and exit.' in help_result.output
