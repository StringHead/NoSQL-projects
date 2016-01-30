# *Host* & *Guest* performance
* Na poniższych obrazkach zaprezentowano obciążenie procesora, dysku twardego oraz pamięci RAM.
* Pomiarów obciążenia obu systemów dokonano:
  * przed zaimporotowaniem zbioru danych do mongo
  * w trakcie importu zbioru danych do mongo
* Wykorzystano zbiór danych *MovieLens data* -  [ml-latest.zip](http://files.grouplens.org/datasets/movielens/ml-latest.zip) (size: 144 MB), dostępny pod adresem [www.grouplens.org](http://grouplens.org/datasets/movielens/)

# *Host* - Windows 10
## Performance Monitor

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
