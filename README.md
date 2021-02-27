# hacker_news

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [PreRequirements](#PreRequirements)
* [Setup](#setup)


## General info
This project is copy of https://news.ycombinator.com/ for train my skill.
Here you can create your posts and attach links, write comments and vote for your favorite posts. 
Also at the end of each day at 23:59 the votes are reset.

Project documented with Postman collection: * https://documenter.getpostman.com/view/14675872/TWDdht4S
Also deployed on Heroku: * https://hacker-news-amz.herokuapp.com/post/

Url examples for site discovery :

* post/
* post/1/
* comment/
* comment/1/
* vote/
* vote/1/
	
## Technologies
Project is created with:
* Django==3.0
* psycopg2-binary==2.8.6
* djangorestframework==3.12.2
* django-crontab==0.7.1
	
## PreRequirements
Make sure you have already installed both Docker Engine and Docker Compose. 
You don’t need to install Python or PostgreSQL, as both are provided by Docker images.

```
$ docker -v
Docker version 20.10.3, build 48d30b5
$ docker-compose -v
docker-compose version 1.28.4
```

## Setup
To run this project, clone it locally using:

```
$ git clone https://github.com/OleksandrPichkurov/hacker_news.git
$ cd hackers_news
```

Environment variables

The file .env.dev contains the environment variables needed in the containers. You can edit this as you see fit, and at the moment these are the defaults that this project uses. However when you intend to use this, keep in mind that you should keep this file out of version control as it can hold sensitive information regarding your project. The file itself will contain some commentary on how a variable will be used in the container.

Create .env.dev file and add:

```
DEBUG=1
SECRET_KEY=vysb+6pk(*bn*#!%d*vd1p1n+z6x47+4c!bdud!tgs!+u&nr1*
DJANGO_ALLOWED_HOSTS=localhost 127.0.0.1 0.0.0.0:8000 [::1]
# Environment Variable which is used in setting.py in django
# setting.py file to configure the database connection for
# application
POSTGRES_DB=dbname
POSTGRES_USER=dbuser
POSTGRES_PASSWORD=dbpass
POSTGRES_HOST=db
POSTGRES_PORT=5432
```
And finally:
```
$ docker-compose up --build
```

Add superuser:
```
docker-compose exec web python3 manage.py createsuperuser
```