# coding=utf-8

# Najd�u�szy czas w powietrzu 8 samolot�w wed�ug numeru linii lotu

import pymongo
import json
from bson.son import SON
from pymongo import MongoClient
client = MongoClient()

db = client['tranStats']
collection = db['airlines2015']

pipeline = [
 { "$group" : { "_id" : {"flightNumber" : "$FL_NUM" },  "airTime" : { "$sum": "$AIR_TIME" } } }, 
 { "$sort" : {"AIR_TIME" : -1 } }, 
 { "$limit" : 8 }
]

statement= db.airlines2015.aggregate(pipeline)
for a in statement: 
   print(a)