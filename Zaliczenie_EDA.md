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


1.	Pobranie i instalacja MongoDB na systemie wirtualnym **Linux Ubuntu** (*Guest*):
```sh
//UŻYTE KOMENDY:
$ time wget https: //fastdl.mongodb.org/linux/mongodb-linux-x86_64-ubuntu1410-clang-3.2.0.tgz
$ time zgip -d mongodb-linux-x86_64-ubuntu1410-clang-3.2.0.tgz
$ time tar -xvf mongodb-linux-x86_64-ubuntu1410-clang-3.2.0.tar
```
2.	Pobranie zbioru danych:  
  * Na samym początku postanowiłem użyć paczki **MovieLens data** -  [ml-latest.zip](http://files.grouplens.org/datasets/movielens/ml-latest.zip) (size: 144 MB) ze strony [www.grouplens.org](http://grouplens.org/datasets/movielens/). Ten zbiór okazał się jednak dla mnie zbyt skromny i ujednolicony jeśli chodzi o rodzaj danych, aby móc dokonać na nim zróżnicowanych operacji. Postanowiłem jednak udokumentować wykonaną przez siebie pracę na tym zbiorze. 
  * W drugiej kolejności skorzystałem ze zbioru danych **Reddit comments** - [reddit-torrent](https://mega.nz/#!ysBWXRqK!yPXLr25PgJi184pbJU3GtnqUY4wG7YvuPpxJjEmnb9A), udostępnionego na stronie [www.reddit.com](https://www.reddit.com/r/datasets/comments/3bxlg7/i_have_every_publicly_available_reddit_comment).




##GEOJSON
[geojson](map(geojson.io).geojson)
