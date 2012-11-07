# -*- coding: utf-8 -*-
import pymongo
import sys

connect = pymongo.Connection("mongodb://127.0.0.1", safe=True)

db = connect.reddit
stories = db.stories

def find():
    print "Find, reporting for duty"
    query = {}
    try:
        cursor = stories.find(query).skip(4)
        cursor = cursor.limit(1)
        cursor = cursor.sort([('student_id', pymongo.ASCENDING), ('score', pymongo.DESCENDING)])
    except:
        print "Unexpected error:",sys.exc_info()[0]
        
    sanity = 0
    for doc in cursor:
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