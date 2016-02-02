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
 { "$group" : { "_id" : "AIR_TIME", "distance" : { "$avg" : "$DISTANCE" }}}
]

statement = db.airlines2015.aggregate(pipeline)
for a in statement: 
   print(a)