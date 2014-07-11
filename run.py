#!/bin/env python

import urllib2
import ConfigParser

config = ConfigParser.ConfigParser()
config.read("demo.conf")

# from_ts = config.get('GENERAL', 'from_ts')
query = config.get('SEARCH ARGS', 'q', '')
type = config.get('SEARCH ARGS', 't', '')
format = config.get('SEARCH ARGS', 'f', 'csv')

search_url = 'http://api2.socialmention.com/search?'
if query:
    search_url += 'q=%s' % query

if type:
    search_url += '&t=%s' % type

if format:
    search_url += '&f=%s' % format

req = urllib2.Request(search_url)
res = urllib2.urlopen(req)
the_page = res.read()

print the_page
