# coding=utf-8

# 5 numerów samolotów, które wykona³y najwiêcej lotów do Waszyngtonu

import pymongo
import json
from bson.son import SON
from pymongo import MongoClient
client = MongoClient()

db = client['tranStats']
collection = db['airlines2015']

pipeline = [
 { "$match" : { "DEST_CITY_NAME" : "Washington, DC"} },
 { "$group" : { "_id" : { "Tail_Number" : "$TAIL_NUM" }, "Count_Of_Flights" : { "$sum" : 1 } } }, 
 { "$sort" : {"Count_Of_Flights" : -1 } }, 
 { "$limit" : 5 }
]

statement= db.airlines2015.aggregate(pipeline)
for a in statement: 
   print(a)