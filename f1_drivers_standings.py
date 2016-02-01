#!/usr/bin/env python

import urllib2

url = 'http://ergast.com/api/f1/current/driverStandings'

def find_between(char, first, last):
    try:
        start = char.index(first) + len(first)
        end = char.index(last, start)
        return char[start:end]
    except ValueError: return ""

httpGet = urllib2.urlopen(url)
page = httpGet.read()
page = page.split('\n')

for line in page:

    if 'position=' in line:
        position = line.split(' ')[1]
        points = line.split(' ')[3]

    if 'GivenName' in line:
        firstName = line.split('/')[0]

    if 'FamilyName' in line:
        lastName = line.split('/')[0]

        print find_between(position, "position=\"", "\""), find_between(firstName, ">", "<"),\
              find_between(lastName, ">", "<"), find_between(points, "points=\"", "\"")
