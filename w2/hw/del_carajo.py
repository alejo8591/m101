# -*- coding: utf-8 -*-
import pymongo
import sys
connect = pymongo.Connection("mongodb://127.0.0.1", safe=True)
db = connect.students
grades = db.grades
print grades.count()
try:
    i = 0
    for i in range(grades.count()+1):
        homeworks =  grades.find({'student_id': i,'type':'homework'}).limit(2)
        if homeworks[0]['score'] > homeworks[1]['score']:
            grades.remove({'type':'homework','score':homeworks[1]['score'], 'student_id': i})
        else:
            grades.remove({'type':'homework','score':homeworks[0]['score'], 'student_id': i})
        i+=1
except:
    print "Unexpected error:",sys.exc_info()[0]
    
print grades.count()