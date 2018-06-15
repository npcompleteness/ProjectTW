# ProjectTW - BestMatching

A didaptical project in collaboration with University of Naples Parthenope; 
The project contains: a web server to get running through Python Flask, a little platform to share "own projects" and get some offers for those ones. The main aim: minimize the costs and maximize the quality of project achievement.

### Prerequisites

Tested operative systems: Ubuntu Linux 16.04
DBMS Server: MongoDB (v3.6.5) running on localhost with port 27017


### Installing

Firstly, install a required repo for the hungarian algorithm, from here:
http://software.clapper.org/munkres/

Install requirements and clone this repository on your system:

```
pip install -r requirements.txt
git clone https://github.com/npcompleteness/ProjectTW.git
cd ProjectTW
```

Then, install a crontab for using the above algorithm

```
sudo crontab -e
```

In the OS crontab file, copy these lines of code:

```
#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
* * * * * python /var/www/progettotw/flaskr/hungarian.py
```

Save and exit, then 

```
sudo python server.py
```
