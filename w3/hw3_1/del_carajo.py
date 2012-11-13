# -*- coding: utf-8 -*-
import pymongo
import sys
connect = pymongo.Connection("mongodb://127.0.0.1", safe=True)
db = connect.school
students = db.students
print students.count()
try:
    i = 0
    for i in range(students.count()+1):
        homework,position,value=0,0,0
        homeworks =  students.find({'_id': i}, {"scores":{"$slice":[2,4]}})
        for homework in range(len(homeworks[0]['scores'])):
            if value == 0 and value < homeworks[0]['scores'][i]['score']:
                value = homeworks[0]['scores'][i]['score']
                position = homework
            if value > homeworks[0]['scores'][i]['score']:
                value = homeworks[0]['scores'][i]['score']
                position = homework
        students.update({"_id":i}, {"$pop":{"scores":position}})
except:
    print "Unexpected error:",sys.exc_info()[0]
print students.count()
"""
h,i= 0,0
homeworks =  students.find({'_id': i})
for i in range(len(homeworks[0]['scores'])):
     if homeworks[0]['scores'][i]['type'] == 'homework':
         if h == 0 and h < homeworks[0]['scores'][i]['score']: h = homeworks[0]['scores'][i]['score']
         while h > homeworks[0]['scores'][i]['score']:
             h = homeworks[0]['scores'][i]['score']
print h
"""
#delete element db.students.update({"_id":0}, {"$pop": {"scores":number element}})