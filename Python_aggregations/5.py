# coding=utf-8

# Pierwszych 8 miast z najwiêksz¹ iloœci¹ przylotów, posortowane od najczêœciej do najrzadziej odwiedzanych

import pymongo
import json
from bson.son import SON
from pymongo import MongoClient
client = MongoClient()

db = client['tranStats']
collection = db['airlines2015']

pipeline = [
 { "$project" :  { "Destination_City" : "$DEST_CITY_NAME" } },
 { "$group" : { "_id" : { "Destination_City" : "$Destination_City" }, "Total_Visits" : { "$sum" : 1 } } },
 { "$sort" : { "Total_Visits" : -1 } },
 { "$limit" : 8 }
]

statement= db.airlines2015.aggregate(pipeline)
for a in statement: 
   print(a)