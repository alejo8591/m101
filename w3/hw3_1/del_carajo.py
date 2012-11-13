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
        homeworks =  students.find({'student_id': i,'type':'homework'}).limit(2)
        if homeworks[0]['score'] > homeworks[1]['score']:
            grades.remove({'type':'homework','score':homeworks[1]['score'], 'student_id': i})
        else:
            grades.remove({'type':'homework','score':homeworks[0]['score'], 'student_id': i})
        i+=1
except:
    print "Unexpected error:",sys.exc_info()[0]
    
print grades.count()
"""
h, i = 0, 0
for i in range(len(homeworks[0]['scores'])):
     if homeworks[0]['scores'][i]['type'] == 'homework':
             if h < homeworks[0]['scores'][i]['score']:
                     h = h
             else:
                     h = homeworks[0]['scores'][i]['score']
             print h
"""
#delete element db.students.update({"_id":0}, {"$pop": {"scores":number element}})