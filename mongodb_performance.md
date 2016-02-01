# *Host* & *Guest* performance
* Na poniższych obrazkach (zrzutach ekranu) zaprezentowałem obciążenie procesora, dysku twardego oraz pamięci RAM.
* Pomiarów obciążenia obu systemów dokonałem:
  * przed zaimporotowaniem zbioru danych do mongo (*idle*)
  * w trakcie importu zbioru danych do monog
* Wykorzystałem zbiór danych *MovieLens data* -  [ml-latest.zip](http://files.grouplens.org/datasets/movielens/ml-latest.zip) (size: 144 MB), dostępny pod adresem [www.grouplens.org](http://grouplens.org/datasets/movielens/)
* Obciążenie systemów zmierzyłem przy użyciu narzędzi wbudowanych w system operacyjny:
  * dla **Windows 10** (*Host*) jest to **Performance Monitor** oraz **Resource Monitor**
  * dla **Linux Ubuntu** (*Guest*) jest to **System Monitor**
* Dodatkowo, na samym końcu zamieściłem zrzut ekranu z **Performance Monitor**, ukazujący obciążenie systemu przez cały czas trwania importu danych do mongo. Do tego celu wykorzystałem zbiór danych **Reddit comments** (~250 GB, unzipped). Na wykresie możemy zauważyć wydajność systemu:
  * na chwilę przed zaimportowaniem danych do mongo (*idle*)
  * w trakcie importu danych do mongo
  * po zaimportowaniu danych do mongo

# *Host* - Windows 10
## Performance Monitor

###### LEGENDA
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Performance/Host/PerformanceMonitor%20-%20legend.PNG "performanceMonitor - legend")

### Wydajność *Hosta* w stanie spoczynku (idle)
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Performance/Host/PerformanceMonitor%20-%20idle_host.PNG "performanceMonitor - idle_host")

### Wydajność *Hosta* w czasie importu zestawu danych do mongo
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Performance/Host/PerformanceMonitor%20-%20performance_host.PNG "performanceMonitor - import_host")


## Resource Monitor

### Wydajność *Hosta* w stanie spoczynku (idle)

* **Overview**
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Performance/Host/ResourceMonotor_Overview%20-%20idle_host.PNG "resourceMonitor - idle_overview_host")

* **CPU**
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Performance/Host/ResourceMonotor_CPU%20-%20idle_host.PNG "resourceMonitor - idle_cpu_host")

* **RAM Memory**
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Performance/Host/ResourceMonotor_Memory%20-%20idle_host.PNG "resourceMonitor - idle_ram_host")

* **Hard Disk**
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Performance/Host/ResourceMonotor_Disk%20-%20idle_host.PNG "resourceMonitor - idle_harddisk_host")
---
<br />

### Wydajność *Hosta* w czasie importu zestawu danych do mongo

* **Overview**
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Performance/Host/ResourceMonotor_Overview%20-%20performance_host.PNG "resourceMonitor - import_overview_host")

* **CPU**
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Performance/Host/ResourceMonitor_CPU%20-%20performance_host.PNG "resourceMonitor - import_cpu_host")

* **RAM Memory**
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Performance/Host/ResourceMonotor_Memory%20-%20performance_host.PNG "resourceMonitor - import_ram_host")

* **Hard Disk**
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Performance/Host/ResourceMonotor_Disk%20-%20performance_host.PNG "resourceMonitor - import_harddisk_host")

# *Guest* - Linux Ubuntu

## System Monitor

###### LEGENDA
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Performance/Guest/SystemMonitor%20-%20Legend.PNG "systemMonitor - legend")

### Wydajność *Guesta* w stanie spoczynku (idle)
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Performance/Guest/SystemMonitor%20-%20idle_guest.PNG "systemMonitor - idle_guest")

### Wydajność *Guesta* w czasie importu zestawu danych do mongo
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Performance/Guest/SystemMonitor%20-%20performance_guest.PNG "systemMonitor - import_guest")

### Wydajność *Guesta* w czasie importu zestawu danych do mongo (podgląd procesu *mongoimport*)
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Movielens/non-stable_dataset/Performance/Guest/SystemMonotor_Processes_MongoImport%20-%20performance_guest.PNG "systemMonitor_Processes - import_guest")

# DODATEK
## Performance Monitor, *Reddit Comments* dataset import
![alt text](https://github.com/StringHead/NoSQL-projects/blob/master/Printscreens/Reddit/OLD/1.png "performanceMonitor - import_reddit_host")

