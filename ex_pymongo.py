import pymongo

from pymongo import Connection
con = Connection('localhost', 27017)

db = con.test
names = db.names

item = names.find_one()
print item['name']