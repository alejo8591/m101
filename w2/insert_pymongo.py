# -*- coding: utf-8 -*-
import pymongo
import sys

connect = pymongo.Connection("mongodb://127.0.0.1", safe=True)
db = connect.school
people = db.people

alejandro = {'name':'Alejandro Romero', 'company':'html5facil', 'interests':['mongodb', 'skateboarding', 'downhill', 'jazz']}
laura = {'name':'Laura Romero', 'company':'pedagogia niños', 'interests':['walking dead', 'babys']}

try:
    people.insert(laura)
    people.insert(alejandro)
except:
    print "Unexpected error:",sys.exc_info()[0]