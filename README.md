database view:

https://stackoverflow.com/questions/54070951/how-to-see-what-data-inside-an-sqlite-database-using-pycharm


## Locust install and running load test
### Install on locust runner
* Mac: brew install libev
* package install: 
    * pipenv install locustio
    * python3 -m pip install locustio
    
* run locust
locust locust/locustfile.py

* run GUI from browser: 
localhost:8089

* enter 
Number of users to simulate: 100(eg)
Hatch rate (users spawned/second): 10(eg)
Host: http://localhost:5000

