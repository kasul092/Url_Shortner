
# Short Way - URL Shortner


![alt text][Python] 


![alt text][logo]
![alt text][logo1]

[logo]:https://user-images.githubusercontent.com/82323267/161417596-15ec3bb7-8d0b-4c73-9067-b8cab5fa2a56.png

[logo1]:https://user-images.githubusercontent.com/82323267/161420767-eb735cef-ecca-4448-91ed-ea26b9da96d2.png




## Introduction

Short Way is URL Shortner. It is a utility to take Long/host URL from user, cut it and return a short URL to user. User can also copy that shorten URL and paste it anywhere he wants. It is a powerful tool written using Python, Flask and HTML. It uses SQLite3 database to store the records.



## Features

* Take long/host URL as input from user.
* Cut that URL and return short URL behalf of long URL.
* Copy shorten URL and paste it anywhere.
* User can access original URL using this short URL.
* Store records in Database. 
* Display all records in table format
* It uses offline 
* Sort the tasks as per date and time.


## Dependencies

| Features | Dependancy |
|---|---|
| ``Scripting Language`` | Python 3.0+
| ``API creation`` | Flask
| ``Database Used`` | SQLite3
| ``Cut long URL`` | Hashids



## How to install source code for development

* Clone project from github:



      $ git clone https://github.com/kasul092/Url_Shortner.git

* We recommend to create and activate a virtualenv first:

   

       $ cd url_shortner/

      $ py -m virtualenv env

      $ env/Scripts/activate

      (env) $

* Run project using commands:



       (env) $env:FLASK_APP="app.py"

      (env) $env:FLASK_ENV="development"

       (env) flask run

* After run above commands host url will generate, click on that and it will redirect to home page of appication.



Short Way - URL Shortner is licensed under [GNU License](https://https://github.com/kasul092/Url_Shortner/blob/main/LICENSE)





[Python]:https://img.shields.io/badge/python-3.6-blue.svg
