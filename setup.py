#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

requirements = [
    'Click>=6.0',
    # TODO: put package requirements here
]

test_requirements = [
    # TODO: put package test requirements here
]

setup(
    name='navadmin_feed',
    version='0.1.0',
    description="Script for scraping the Navy NAVADMIN page and converting to a JSON feed.",
    long_description=readme + '\n\n' + history,
    author="J.R. Powers-Luhn",
    author_email='floobyt@gmail.com',
    url='https://github.com/piovere/navadmin_feed',
    packages=[
        'navadmin_feed',
    ],
    package_dir={'navadmin_feed':
                 'navadmin_feed'},
    entry_points={
        'console_scripts': [
            'navadmin_feed=navadmin_feed.cli:main'
        ]
    },
    include_package_data=True,
    install_requires=requirements,
    license="MIT license",
    zip_safe=False,
    keywords='navadmin_feed',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements
)
