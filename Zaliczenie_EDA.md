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

1.	Pobranie i instalacja MongoDB na systemie wirtualnym **Linux Ubuntu** (*Guest*):  
  ```sh
  # Pobranie MongoDB:
  $ time wget https: //fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1410-clang-3.2.0.tgz

  # Rozpakowanie MongoDB:
  $ time zgip -d mongodb-linux-x86_64-ubuntu1410-clang-3.2.0.tgz
  $ time tar -xvf mongodb-linux-x86_64-ubuntu1410-clang-3.2.0.tar
  ```
  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Reddit/OLD/MongoDB%20download%20and%20unzip.PNG "MongoDB - download_and_unzip")

  ```sh
  # Ustawienie ścieżki systemowej:
  $ PATH=$PATH:~/mongodb-linux-x86_64-ubuntu1410-clang-3.2.0/bin/
  ```
  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Reddit/OLD/MongoDB%20set%20PATH.PNG "MongoDB -setPath")

  <hr />

2.	Pobranie zbioru danych:  
  * Na samym początku postanowiłem użyć paczki **MovieLens data** - [ml-latest.zip](http://files.grouplens.org/datasets/movielens/ml-latest.zip) (size: 144 MB) ze strony [www.grouplens.org](http://grouplens.org/datasets/movielens/). Niestety ten zestaw okazał się dla mnie zbyt skromny i ujednolicony jeśli chodzi o rodzaj danych, aby móc dokonać na nim zróżnicowanych operacji. Postanowiłem jednak udokumentować wykonaną przez siebie pracę na tym zbiorze.
  * W drugiej kolejności skorzystałem ze zbioru danych **Reddit comments** - [reddit-torrent](https://mega.nz/#!ysBWXRqK!yPXLr25PgJi184pbJU3GtnqUY4wG7YvuPpxJjEmnb9A), udostępnionego na stronie [www.reddit.com](https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment).

  <hr />

## **MovieLens** dataset

1. Pobranie i rozpakowanie zbioru danych
  ```sh
  # Rozpakowanie zbioru danych
  $ time unzip ml-latest.zip -d /home/stringhead/mongodb-dataset/

  # Sprawdzenie zawartości
  $ ls -l
  ```
  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/1_unzip_ls_dataset.PNG "unzip_ls_dataset")

2. Zaimportowanie zbiorów danych do mongo:
  * Postanowiłem zaimportować 3 z 4 plików widocznych w punkcie 1: *movies.csv* (1.7 MB), *tags.csv* (20.9 MB), oraz mający najwięszky rozmiar *ratings.csv* (617,1 MB). Poniżej przykład zaimportowania właśnie tego ostatniego zbioru.
  ```sh
  # dataset import
  $ time mongoimport -d movielens -c movies_rating --type csv --headerline --file ./ratings.csv
  ```
  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/2a_mongoimport_command%20movies_ratings.PNG "mongoimport_command_movies_ratings")

  * Łączny czas importu:
  ```sh
  real    6m55.237s
  user    3m39.436s
  sys     1m10.860s
  ```
  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/2b_mongoimport_done%20movies_ratings.PNG "mongoimport_done_movies_ratings")

3. Uruchomienie mongo...

  * Pierwsze, podstawowe komendy

  ```sh
  # Wyświetlenie dostępnych baz danych
  > show dbs

  # Wybranie bazy danych "movielens" i wyświetlenie jej kolekcji
  > use movielens
  > show collections

  # Wyświetlenie przykładowego dokumentu ze wszystkich 3 kolekcji
  > db.movies.findOne()
  > db.movies_ratings.findOne()
  > db.movies_tags.findOne()

  # Zliczenie wszystkich rekordów
  > db.movies.count()
  > db.movies_ratings.count()
  > db.movies_tags.count()

  ```
  ![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/3_mongo_showDbs_useDb_showCollections.PNG "mongo_showDbs_useDb_showCollections")

  * Jak widać, struktura powyższych kolekcji nie jest zbyt rozbudowana. Dodatkowo jesteśmy zmuszeni do operowania na 3 oddzielnych kolekcjach, zamiast na jednej (jak to jest właśnie w przypadku zbioru danych *Reddit comments* - przedstawię go w dalszej części niniejszej dokumentacji). Wydaje się, że jedym z rozwiązań mogłoby się okazać użycie funkcji **mapReduce**, dostępnej w mongoDB, dzięki której możliwe jest złączenie dokumentów z kilku kolekcji w jedną, nową. Ciekawy opis tej procedury, wraz z przykładem użycia i objaśnieniem, czym jest mapReduce, znalazłem na stronie [www.noppanit.com](https://www.noppanit.com/merge-documents-two-collections-together-mongodb/). Ostatecznie postanowiłem jedynie zapoznać się z tą metodą, a jej wykorzystaniem zajmę się - mam nadzieję - przy innej okazji :).






##GEOJSON
[geojson](map(geojson.io).geojson)
