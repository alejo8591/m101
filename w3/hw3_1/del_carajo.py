# -*- coding: utf-8 -*-
import pymongo, sys
students = pymongo.Connection("mongodb://127.0.0.1", safe=True).school.students
try:
    i = 0
    for i in range(students.count()):
        homework,array=0,[]
        homeworks =  students.find({'_id': i})
        for homework in range(len(homeworks[0]['scores'])):
            array.append(homeworks[0]['scores'][homework])
        array.remove(min(array[2:4])), students.update({'_id':i}, {'$set':{'scores':array}})
except:
    print "Unexpected error:",sys.exc_info()[0]