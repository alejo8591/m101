#!/usr/bin/env python
import pymongo
import sys

connect = pymongo.Connection("mongodb://127.0.0.1", safe=True)

db = connect.reddit
stories = db.stories

def find():
    print "Find, reporting for duty"
    query = {'title':{'$regex':'Microsoft'}}
    projection = {'title':1, '_id':0}
    try:
        iter = stories.find(query, projection)
    except:
        print "Unexpected error:",sys.exc_info()[0]
        
    sanity = 0
    for doc in iter:
        print doc
        sanity+=1
        if (sanity > 10):
            break
        
def find_one():
    print "find one, reporting for duty"
    query = {'student_id':10}
    try:
        iter = scores.find_one(query)
    except:
        print "Unexpected error:",sys.exc_info()[0]
    
    print iter
    
#find_one()
find()