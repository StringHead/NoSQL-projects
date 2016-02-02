# coding=utf-8

# ��czny dystans wszystkich przelot�w dokonanych danego dnia, wraz z ich ��cznym czasem trwania (czas przelotu musi by� d�u�szy ni� 1500000 minut (25 000 h)

import pymongo
import json
from bson.son import SON
from pymongo import MongoClient
client = MongoClient()

db = client['tranStats']
collection = db['airlines2015']


pipeline = [
 { "$group": { "_id": "$FL_DATE", "DISTANCE": { "$sum": "$DISTANCE"}, "AIR_TIME": { "$sum" : "$AIR_TIME" }} },
 { "$match" : { "AIR_TIME" : { "$gte" : 1500000}} },
 { "$limit" : 20}
]

statement = db.airlines2015.aggregate(pipeline)
for a in statement: 
   print(a)