## To seed data
* cd books
* books> flask create_tables

## To run application
```
$ export FLASK_APP=books/app.py
$ flask run
 * Running on http://127.0.0.1:5000/
```

## Locust install for load test
### Install on locust runner
* For Mac
```
$ brew install libev
``` 
* For Win, refer the following link
https://docs.locust.io/en/stable/installation.html

* Package install: 
```
$ pipenv install locustio
$ python3 -m pip install locustio
```
* Create "locustfile.py", which is the load test as code

* Run Locust
```
$ locust locust/locustfile.py
```

* Run GUI from browser: 
localhost:8089

* In Locust GUI, enter the following  
Number of users to simulate: 100(eg)
Hatch rate (users spawned/second): 10(eg)
Host: http://localhost:5000

Note:
If you use SQL DB client in Pycharm, Here is a good instruction how to set it up.
https://stackoverflow.com/questions/54070951/how-to-see-what-data-inside-an-sqlite-database-using-pycharm

