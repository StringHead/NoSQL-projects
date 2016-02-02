# Bazy NoSQL
## EDA
---
### Specyfikacja komputera użytego do obliczeń:

| **COMPUTER**        |                                                |
|:-------------------:|------------------------------------------------|
| **Full name**       | Inspiron 7520 15R SE                           |
| **Manufacturer**    | Dell Inc.                                      |
| **Type**            | Laptop                                         |


| **HARDWARE**        |                                                |
|:-------------------:|------------------------------------------------|
| **CPU name**        | Intel Core i7-3632QM                           |
| **CPU spec.**       | Intel Core i7-3632QM PCU @ 2.20 GHz (4 cores)  |
| **CPU cores**       | 4                                              |
| **DRAM type**       | DDR3                                           |
| **DRAM size**       | 12 GB                                          |
| **Storage type**    | *Primary:* SSHD, *Secondary:* HDD              |
| **Storage size**    | *Primary:* 1TB, *Secondary:* 1TB               |
| **Operating System**| Windows 10 Professional x64                    |

<hr />

## SPRAWDŹ! --> [WYDAJNOŚĆ SYSTEMU PODCZAS IMPORTU ZBIORU DANYCH DO BAZY MongoDB!](https://github.com/StringHead/NoSQL-projects/blob/master/performance.md "System performance")

<hr />

1.	Pobranie i instalacja MongoDB na systemie wirtualnym **Linux Ubuntu** (*Guest*):  
  ```sh
  # Pobranie MongoDB:
  $ time wget https: //fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1410-clang-3.2.0.tgz

  # Rozpakowanie MongoDB:
  $ time zgip -d mongodb-linux-x86_64-ubuntu1410-clang-3.2.0.tgz
  $ time tar -xvf mongodb-linux-x86_64-ubuntu1410-clang-3.2.0.tar
  ```
  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Reddit/MongoDB%20download%20and%20unzip.PNG "MongoDB - download_and_unzip")

  ```sh
  # Ustawienie ścieżki systemowej:
  $ PATH=$PATH:~/mongodb-linux-x86_64-ubuntu1410-clang-3.2.0/bin/
  ```
  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Reddit/MongoDB%20set%20PATH.PNG "MongoDB -setPath")

  <hr />

2.	Pobranie zbioru danych (*dataset*):  

  * Na samym początku użyłem zbioru **Reddit comments** - [reddit-torrent](https://mega.nz/#!ysBWXRqK!yPXLr25PgJi184pbJU3GtnqUY4wG7YvuPpxJjEmnb9A), udostępnionego na stronie [www.reddit.com](https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment). Po zapoznaniu się z zestawem i przeprowadzeniu na nim paru zapytań uznałem, że skorzystam jednak z innego zbioru, a ze swoich dokonań na **Reddit comments** zamieściłem w dokumencie [performance.md](https://github.com/StringHead/NoSQL-projects/blob/master/performance.md) jedynie zrzuty ekranu, obrazujące obciążenie systemu w trakcie importu datasetu do bazy mongoDB.
  * Ostatecznie zadania na zaliczenie postanowiłem wykoać na zbiorze danych **MovieLens data** - [ml-latest.zip](http://files.grouplens.org/datasets/movielens/ml-latest.zip) (size: 144 MB), dostępnym na stronie [www.grouplens.org](http://grouplens.org/datasets/movielens/).

  <hr />

# **MovieLens** dataset

## MongoDB

* Koloryzowanie składni w mongoDB uzyskałem poprzez użycie rozszerzenia **Mongo Hacker** - [mongo-hacker](https://tylerbrock.github.io/mongo-hacker/)


1. Pobranie i rozpakowanie zbioru danych
  ```sh
  # Rozpakowanie zbioru danych
  $ time unzip ml-latest.zip -d /home/stringhead/mongodb-dataset/

  # Sprawdzenie zawartości
  $ ls -l
  ```
  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/1_unzip_ls_dataset.PNG "unzip_ls_dataset")

### *Zadanie 2a* - zaimportowanie zbioru danych do bazy MongoDB

2. Zaimportowanie zbiorów danych do mongo:
  * Postanowiłem zaimportować 3 z 4 plików widocznych w punkcie 1: *movies.csv* (1.7 MB), *tags.csv* (20.9 MB), oraz mający najwięszky rozmiar *ratings.csv* (588,6 MB). Poniżej przykład zaimportowania właśnie tego ostatniego zbioru.
  ```sql
  # dataset import
  $ time mongoimport -d movielens -c movies_rating --type csv --headerline --file ./ratings.csv
  ```
  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/2a_mongoimport_command%20movies_ratings.PNG "mongoimport_command_movies_ratings")

  * Łączny czas importu:
  ```sql
  real    6m55.237s
  user    3m39.436s
  sys     1m10.860s
  ```
  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/2b_mongoimport_done%20movies_ratings.PNG "mongoimport_done_movies_ratings")

3. Uruchomienie mongo...

  * Pierwsze, podstawowe operacje

  ```sql
  # Wyświetlenie dostępnych baz danych
  > show dbs

  # Wybranie bazy danych "movielens" i wyświetlenie jej kolekcji
  > use movielens
  > show collections
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/3_mongo_showDbs_useDb_showCollections.PNG "mongo_showDbs_useDb_showCollections")  

  ```sql
  # Wyświetlenie przykładowego dokumentu ze wszystkich 3 kolekcji
  > db.movies.findOne()
  > db.movies_ratings.findOne()
  > db.movies_tags.findOne()
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/5_db.collection.findOne.PNG "db.collection.findOne")

### *Zadanie 2b* - zliczenie liczby zaimportowanych rekordów

  ```sql
  # Zliczenie wszystkich rekordów
  > db.movies.count()
  > db.movies_ratings.count()
  > db.movies_tags.count()
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/4_db.collection.count.PNG "db.collection.count")

  * Jak widać, struktura powyższych kolekcji nie jest zbyt rozbudowana. Dodatkowo musimy operować na 3 oddzielnych kolekcjach, zamiast na jednej (przykładem może być zbiór *Reddit comments*). Wydaje się, że jednym z rozwiązań mogłoby się okazać użycie funkcji **mapReduce**, dostępnej w mongoDB, dzięki której możliwe jest złączenie dokumentów z kilku kolekcji w jedną, nową. Ciekawy opis tej procedury, wraz z przykładem użycia i objaśnieniem, czym jest mapReduce, znalazłem na stronie [www.noppanit.com](https://www.noppanit.com/merge-documents-two-collections-together-mongodb/). Ostatecznie postanowiłem jedynie zapoznać się z tą metodą, a jej wykorzystaniem zajmę się - mam nadzieję - przy innej okazji :).

### *Zadanie 2c* - policzenie kilku prostych agregacji na zaimportowanych danych

  1. Wyszukanie w kolekcji **movies** filmu, mającego w tytule nazwę *"Hobbit"*

  ```sql
  > db.movies.find({ title: /Hobbit/i }).pretty();
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Mongo_queries/1.db.movies.findt%20itle%20Hobbit.PNG "1.db.movies.find(title Hobbit)")

  2. Wyszukanie w kolekcji **movies** filmu, mającego w tytule nazwę *"Hobbit"* i zawężając tym razem wyszukiwania, poprzez uwzględnienie roku produkcji, znajdującego się również w kluczu "title".

  ```sql
  > db.movies.find({ title: /Hobbit.*\(2013\).*/i }).pretty();
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Mongo_queries/2.db.movies.find%20title%20Hobbit%20.PNG "2.db.movies.find(title Hobbit")

  3. Wyszukanie ocen (*ratings*) w kolekcji **movies_ratings** dla filmu o "movieId" = 106489 i ograniczenie wyświetlanych wyników do 4.

  ```sql
  > db.movies_ratings.find({ movieId: 106489 }).limit(4).pretty();
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Mongo_queries/3.db.movies_ratings.find.PNG "3.db.movies_ratings.find")

  4. Zliczenie ilości ocen (*ratings*) równych 5, w kolekcji **movies_ratings**, dla filmu o "movieId" = 106489

  ```sql
  > db.movies_ratings.find({ movieId: 106489, rating: 5 }).count();
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Mongo_queries/5.db.movies_ratings%2C%20rating5.count.PNG "5.db.movies_ratings==5")

  5. Wyszukanie w kolekcji **movies_ratings** zakresu dostępnych ocen (*ratings*) dla filmu o "movieId" = 106489

  ```sql
  > db.runCommand({distinct: movies_ratings, key:rating, query: {movieId: 106489 } });
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Mongo_queries/6.db.runCommand.PNG "6.db.runCommand")

  6. Wyszukanie w kolekcji **movies_ratings** 2 filmów o najwyższych ocenach (*ratings*)

  ```sql
  > db.movies_ratings.find( {}, {_id:0} ).sort({ "rating": -1} ).limit(2).pretty()
    ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Mongo_queries/7.db.movies_ratings.find_2_highest_rates.PNG "7.db.movies_ratings.find(2 highest rates)")

### DODATEK

  7. Wyszukanie w kolekcji **movies_tags** wszystkich filmów, w których aktorką (oznaczoną w kluczu "tag") jest Rosamund Pike, a następnie utworzenie nowej kolekcji składającej się wyłącznie z filmów znalezionych na podstawie podanego kryterium

  ```sql
  > var f = db.movies_tags.find ( {tag: {$all: [ /Rosamund Pike/ ] } })
  > for ( var i = 0; i < f.length(); ++i) {
  > db.rosamundPike_movies.insert(
  > {movie : f[i] }
  > ); }
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Mongo_queries/B1.RosamundPike_movies.insert_new_collection2.PNG "B1.RosamundPike_movies.insert_new_collection2")

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Mongo_queries/B2.RosamundPike_movies.insert_new_collection2.PNG "B2.RosamundPike_movies.insert_new_collection2")

  <hr />

## PostgreSQL

  1. Utworzenie bazy danych

  ```sql
  $ createdb -U postgres -h localhost pgsql_movielens
  $ psql -U postgres -h localhost
  ```
  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/postrgresql/1.create_db.PNG "1.create_db")

### *Zadanie 2a* - zaimportowanie zbioru danych do bazy PostgreSQL

  2. Stworzenie tabel i zaimportowanie zbiorów danych do PostgreSQL

  ```sh
  postgres=# \timing  # włączenie pomiaru czasu egzekucji zapytań

  postgres=# createdb -U postgres -h localhost movielens

  postgres=# psql -U postgres -h localhost

  postgres=# create table pgsql_movies (movieId int primary key, title varchar, genres varchar);

  postgres=# COPY pgsql_movies FROM '/home/stinghead/postgresql-dataset/ml-latest/movies.csv' DELIMITER ',' CSV;

  postgres=# create table pgsql_movies_ratings (id serial primary key, userId int, movieId int, rating real, timestamp int);

  postgres=# COPY pgsql_movies_ratings(userId,movieId,rating,timestamp  ) FROM '/home/stinghead/postgresql-dataset/ml-latest/ratings.csv' DELIMITER ',' CSV;

  postgres=# create table pgsql_movies_tags (id serial primary key, userId int, movieId int, tag varchar, timestamp int);

  postgres=# COPY pgsql_movies_tags (userId,movieId,tag,timestamp ) FROM '/home/stinghead/postgresql-dataset/ml-latest/tags.csv' DELIMITER ',' CSV;
  ```

  * Łączny czas importu:
  ```
  pgsql_movies            144,829 ms ~ 0.145 s
  pgsql_movies_ratings    190144,226 ms ~ 190.144 s ~ 3 min 10 s
  pgsql_movies_tags       23626,384 ms ~ 23.626 s
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/postrgresql/2.movies_create_table_and_import.PNG "2.movies_create_table_and_import")

### *Zadanie 2b* - zliczenie liczby zaimportowanych rekordów

  ```sql
  # Zliczenie wszystkich rekordów
  > SELECT COUNT(*) FROM pgsql_movies;
  > SELECT COUNT(*) FROM pgsql_movies_ratings;
  > SELECT COUNT(*) FROM pgsql_movies_tags;
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/4_db.collection.count.PNG "db.collection.count")

### *Zadanie 2c* - policzenie kilku prostych agregacji na zaimportowanych danych

  1. Wyszukanie w kolekcji **movies** filmu, mającego w tytule nazwę *"Hobbit"*

  ```sql
  > select * from pgsql_movies where title like '%Hobbit%';
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/postrgresql/3.query1.PNG "psql_query_1")

  2. Wyszukanie w kolekcji **movies** filmu, mającego w tytule nazwę *"Hobbit"* i zawężając tym razem wyszukiwania, poprzez uwzględnienie roku produkcji, znajdującego się również w kluczu "title".

  ```sql
  > select * from pgsql_movies where title like '%Hobbit%' and title like '%2013%';
  ```

  ![alt text](2.movies_create_table_and_import "psql_query_2")

  3. Wyszukanie ocen (*ratings*) w kolekcji **movies_ratings** dla filmu o "movieId" = 106489 i ograniczenie wyświetlanych wyników do 4.

  ```sql
  > select * from pgsql_movies_ratings where movieId=106489 limit 4;
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/postrgresql/3.query3.PNG "psql_query_3")

  4. Zliczenie ilości ocen (*ratings*) równych 5, w kolekcji **movies_ratings**, dla filmu o "movieId" = 106489

  ```sql
  > select count(movieid) from pgsql_movies_ratings where movieId=106489 and rating=5;
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/postrgresql/3.query5.PNG "psql_query_5")

  5. Wyszukanie w kolekcji **movies_ratings** zakresu dostępnych ocen (*ratings*) dla filmu o "movieId" = 106489

  ```sql
  > select distinct rating from pgsql_movies_ratings where movieId=106489;
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/postrgresql/3.query6.PNG "psql_query_6")

  6. Wyszukanie w kolekcji **movies_ratings** 2 filmów o najwyższych ocenach (*ratings*)

  ```sql
  > select * from pgsql_movies_ratings order by rating desc, userId asc limit 2;
  ```

  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/postrgresql/3.query7.PNG "psql_query_7")












## GEOJSON
[geojson](map(geojson.io).geojson)
