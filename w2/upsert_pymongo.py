# -*- coding: utf-8 -*-
import pymongo
import sys

connect = pymongo.Connection("mongodb://127.0.0.1", safe=True)
db = connect.test
things = db.things

print "Updating write upsert"
try:
    things.drop()
    
    things.update({'thing':'apple'}, {'$set':{'color':'red'}}, upsert=True)
    things.update({'thing':'pear'}, {'color':'green'}, upsert=True)
    
    print "Apple: ", things.find_one({'thing':'apple'})
    
    print "Pear: ", things.find_one({'thing':'pear'})
    
except:
    print "Unexpected error:",sys.exc_info()[0]
    raise

