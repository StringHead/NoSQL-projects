# Bazy NoSQL
## EGZAMIN

### *Zadanie 3.1*

1.	Pobranie zbioru danych (*dataset*):

  * Do wykonania zadania z agregacji wykorzystałem zbiór danych **tranStats**, zawierający obszerne i szczegółowe statystyki na temat linii lotniczych i ich przelotów w samych Stanach Zjednoczonych. Dataset jest dostępny do pobrania ze strony [www.transtats.bts.gov](http://www.transtats.bts.gov/DL_SelectFields.asp?Table_ID=236&DB_Short_Name=On-Time). Co ciekawe, odbywa się to przy użyciu formularza, za pomocą którego samemu generujemy zbiór, wybierając w nim wyłącznie te dane, które nas interesują. Utworzony przeze mnie dataset uwzględnia wszystkie stany USA i dotyczy miesiąca Lutego, roku 2015.

![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Egzamin/mongo_import/transtats.bts.gov_example.PNG "transtats.btv.gov_example")

  <hr />

### *Zadanie 3.2*

2. Zaimportowanie zbioru danych do bazy MongoDB

  ```sql
  # dataset import
  $ time mongoimport -d tranStats -c airlines2015 --type csv --headerline --file ./tranStats.csv
  ```

  * Łączny czas importu:
  ```sql
  real    0m29.737s
  user    0m28.944s
  sys     0m10.312s
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Egzamin/mongo_import/1.import_db.PNG "MongoDB - import_db")

  3. Uruchomienie mongo...

    * Pierwsze, podstawowe operacje

    ```sql
    # Wyświetlenie dostępnych baz danych
    > show dbs

    # Wybranie bazy danych "tranStats" i wyświetlenie jej kolekcji
    > use tranStats
    > show collections
    ```

    ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Egzamin/mongo_import/3.db.collection.findOne.png "MongoDB - show_dbs_collections")


    ```sql
    # Wyświetlenie przykładowego dokumentu z kolekcji
    > db.airlines2015.findOne()
    ```

    ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Egzamin/mongo_import/3.db.collection.findOne.png "MongoDB - db.collection.findOne")

    ```sql
    # Zliczenie wszystkich rekordów
    > db.tranStats.count()
    ```

    ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Egzamin/mongo_import/4.db.collection.count.PNG "MongoDB - db.collection.count")

    <hr />

### *Zadanie 3.3* - Pięć przykładowych agregacji korzystających z *Aggregation Pipeline*

  1. Średni dystans wszystkich przelotów (*w milach*)

  ```sql
  > db.airlines2015.aggregate(
    { $group: { _id: "AIR_TIME", distance: { $avg: "$DISTANCE" } } }
  );
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Egzamin/Aggregations/1.Average_distance_of_all_flights.PNG "average_distance_of_all_flights")

  2. Najdłuższy czas przelotu 8 samlotów, z uwzględnieniem numeru lotu (*FL_NUM*) i sortowaniem od najdłuższego do najkrótszego czasu (*AIR_TIME*)

  ```sql
  > db.airlines2015.aggregate(
    { $group: { _id: : { flightNumber : "$FL_NUM" }, airTime : { $sum : "$AIR_TIME" } } },
    { $sort : {AIR_TIME : -1 } }, { $limit : 8 }
  );
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Egzamin/Aggregations/2.8_airplanes_longest_air_time.PNG "airplanes_longest_air_time")

  3. 5 numerów samolotów (*TAIL_NUM*), które wykonały najwięcej przelotów (*Count_Of_Flights*) do Waszyngtonu (*DEST_CITY_NAME*)

  ```sql
  > db.airlines2015.aggregate(
    { $match : { DEST_CITY_NAME:"Washington, DC" } },
    { $group : { _id : { Tail_Number : "$TAIL_NUM" }, Count_Of_Flights: { $sum : 1 } } },
    { $sort : { Count_Of_Flights : -1 } }, { $limit : 5 }
  );
  ```
  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Egzamin/Aggregations/3.5_airplanes_Washington_countofFlights.PNG "airplanes_Washington_countOfFlights")

  4. Łączny dystans wszystkich przelotów (*DISTANCE*) dokonanych danego dnia (*FL_DATE*), wraz z ich łącznym czasem trwania (*AIR_TIME*) - czas przelotów musi być dłuższy niż 1500000 minut (25 000 h). Wyświetlonych zostanie pierwszych 20 wyników

  ```sql
  > db.airlines2015.aggregate(
    { $group: { _id: "$FL_DATE", DISTANCE: { $sum: "$DISTANCE" }, AIR_TIME: { $sum: "$AIR_TIME" } } },
    { $match: { AIR_TIME: { $gte: 1500000 } } }, { $limit: 20 }
  );
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Egzamin/Aggregations/4.20_Total_distance_total_airTime_Date.PNG "total_distance_total_airTime_Data")

  5. Pierwszych 10 miast (*DEST_CITY_NAME*) z największą ilością przylotów (*Total_Visits*), posortowane od najczęściej do najrzadziej występujących

  ```sql
  > db.airlines2015.aggregate(
  [
    { $project :  { Destination_City : "$DEST_CITY_NAME" } },
    { $group : { _id : { Destination_City: "$Destination_City" } , Total_Visits : { $sum : 1 } } },
    { $sort : { Total_Visits : -1 } },
    { $limit : 8 }
  ]);
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Egzamin/Aggregations/5.8_most_visited_cities%20sorted_desc.PNG "most_visited_cities sorted_desc")



### *Zadanie 3.3* - Agregacje z *Zadania 3.2*, wykonane w języku **Python**

  1. Średni dystans wszystkich przelotów (*w milach*)

  ```Python
  import pymongo
  import json
  from bson.son import SON
  from pymongo import MongoClient
  client = MongoClient()

  db = client['tranStats']
  collection = db['airlines2015']

  pipeline = [
    { "$group" : { "_id" : "AIR_TIME", "distance" : { "$avg" : "$DISTANCE" } } }
  ]

  statement = db.airlines2015.aggregate(pipeline)
  for a in statement:
    print(a)
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Egzamin/Aggregations/Python/1.PNG "average_distance_of_all_flights")

  2. Najdłuższy czas przelotu 8 samlotów, z uwzględnieniem numeru lotu (*FL_NUM*) i sortowaniem od najdłuższego do najkrótszego czasu (*AIR_TIME*)

  ```Python
  import pymongo
  import json
  from bson.son import SON
  from pymongo import MongoClient
  client = MongoClient()

  db = client['tranStats']
  collection = db['airlines2015']

  pipeline = [
    { "$group" : { "_id" : {"flightNumber" : "$FL_NUM" },  "airTime" : { "$sum": "$AIR_TIME" } } },
    { "$sort" : {"AIR_TIME" : -1 } }, { "$limit" : 8 }
  ]

  statement= db.airlines2015.aggregate(pipeline)
  for a in statement:
     print(a)
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Egzamin/Aggregations/Python/2.PNG "airplanes_longest_air_time")

  3. 5 numerów samolotów (*TAIL_NUM*), które wykonały najwięcej przelotów (*Count_Of_Flights*) do Waszyngtonu (*DEST_CITY_NAME*)

  ```Python
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
    { "$sort" : {"Count_Of_Flights" : -1 } }, { "$limit" : 5 }
  ]

  statement= db.airlines2015.aggregate(pipeline)
  for a in statement:
     print(a)
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Egzamin/Aggregations/Python/3.PNG "airplanes_Washington_countOfFlights")


  4. Łączny dystans wszystkich przelotów (*DISTANCE*) dokonanych danego dnia (*FL_DATE*), wraz z ich łącznym czasem trwania (*AIR_TIME*) - czas przelotów musi być dłuższy niż 1500000 minut (25 000 h). Wyświetlonych zostanie pierwszych 20 wyników

  ```Python
  import pymongo
  import json
  from bson.son import SON
  from pymongo import MongoClient
  client = MongoClient()

  db = client['tranStats']
  collection = db['airlines2015']


  pipeline = [
    { "$group": { "_id": "$FL_DATE", "DISTANCE": { "$sum": "$DISTANCE" }, "AIR_TIME": { "$sum" : "$AIR_TIME" } } },
    { "$match" : { "AIR_TIME" : { "$gte" : 1500000 } } }, { "$limit" : 20 }
  ]

  statement = db.airlines2015.aggregate(pipeline)
  for a in statement:
     print(a)
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Egzamin/Aggregations/Python/4.PNG "total_distance_total_airTime_Data")

  5. Pierwszych 10 miast (*DEST_CITY_NAME*) z największą ilością przylotów (*Total_Visits*), posortowane od najczęściej do najrzadziej występujących

  ```Python
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
    { "$sort" : { "Total_Visits" : -1 } }, { "$limit" : 8 }
  ]

  statement= db.airlines2015.aggregate(pipeline)
  for a in statement:
     print(a)
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Egzamin/Aggregations/Python/5.PNG "most_visited_cities sorted_desc")
