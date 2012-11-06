#!/usr/bin/env python
import json
import urllib2
import pymongo

#connect to mongo
connect = pymongo.Connection("mongodb://127.0.0.1", safe=True)
# get handle reddit
db = connect.reddit
stories = db.stories
# get reddit home page
reddit_page = urllib2.urlopen("http://www.reddit.com/r/technology/.json")
# parse json in python objects
parsed = json.loads(reddit_page.read())

for item in parsed['data']['children']:
    #put into mongo
    stories.insert(item['data'])