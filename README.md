# Python Flask Microservices
The idea behind this application is to demonstrate microservices architecture of today's modern system. In this demo i have tried to show the basic microservices REST-API concepts of a tech & entertainment industry (i.e Netflix), and if we look at the system design of Netflix, it runs around more than 10,000+ microservices to manage the entire system, so in system-design it's quite important to understand this concept.

# Technical Overview
The Proof of Concept written using python and it uses flask web framework to define the routes, and to store the data in the server it uses mongodb database.

In this project you will find there are three different types of microservices.

1. Users
2. Movies
3. Trending Now

<img src="screenshots/swagger.png"/>

# Installation
git clone https://github.com/anshumanpattnaik/python-flask-microservices
cd python-flask-microservices
pip install requirements.txt
python3 run.py

Open [http://127.0.0.1:5000](http://127.0.0.1:5000) to view in the browser.


# Build Docker image

```````````````````````````````````````````````````````
docker build -t python-flask-microservices .
```````````````````````````````````````````````````````

```````````````````````````````````````````````````````````````````````````````
docker run -it --name python-container -p 5000:5000 python-flask-microservices
```````````````````````````````````````````````````````````````````````````````

### License
This project is licensed under the [MIT License](LICENSE)