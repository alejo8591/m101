# -*- coding: utf-8 -*-
import pymongo
import sys
connect = pymongo.Connection("mongodb://127.0.0.1", safe=True)
db = connect.school
students = db.students
print students.count()
try:
    i = 0
    for i in range(students.count()):
        count, homework,array=0,0,[]
        homeworks =  students.find({'_id': i})
        for homework in range(len(homeworks[0]['scores'])):
            array.append(homeworks[0]['scores'][homework])
        array.remove(min(array[2:4])), students.update({'_id':i}, {'$unset':{'scores':1}}), students.update({'_id':i}, {'$set':{'scores':array}})
except:
    print "Unexpected error:",sys.exc_info()[0]
print students.count()