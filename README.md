# ProjectTW - BestMatching

A didaptical project in collaboration with University of Naples Parthenope; 
The project contains: a web server to get running through Python Flask, a little platform to share "own projects" and get some offers for those ones. The main aim: minimize the costs and maximize the quality of project achievement.
Public link on the Internet : http://ec2-18-237-252-219.us-west-2.compute.amazonaws.com/
Take a look in Google Slide : https://drive.google.com/open?id=1BFyGXq3kRpMkBLYjyAZTGyZ7T-y7-lX-pajIcMkz0Lg

### Prerequisites

Tested operative systems: Ubuntu Linux 16.04
Python v2.7.12
DBMS Server: MongoDB (v3.6.5) running on localhost with port 27017

### Installing

Firstly, install a required repo for the hungarian algorithm, from here:
http://software.clapper.org/munkres/

Install pip, with this link:
https://www.saltycrane.com/blog/2010/02/how-install-pip-ubuntu/

Install requirements and clone this repository on your system:

```
pip install -r requirements.txt
pip install bson
pip install pymongo==3.6.1
git clone https://github.com/npcompleteness/ProjectTW.git
cd ProjectTW
```

Then, install a crontab for using the above algorithm

```
sudo crontab -e
```

In the OS crontab file, copy these lines of code (ensure in path you have the absolute path)

```
#!/bin/bash
PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
* * * * * python (path)/ProjectTW/flaskr/hungarian.py
```

Save and exit, then 

```
sudo python server.py
```
Now the project is running on localhost, port 5000 (if you set Security Groups on for HTTP, you can choose port 80).

# Future releases

A newsletter; some useful APIs for analysing qualities of offerers; Mobile integrations with iOS and AndroidOS (IONIC)
