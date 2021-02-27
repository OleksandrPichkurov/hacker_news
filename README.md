# hacker_news

## Table of contents
* [General info](#general-info)
* [Technologies](#technologies)
* [Prerequisites](#Prerequisites)
* [Setup](#setup)


## General info
This project is copy of https://news.ycombinator.com/ for train my skill.
	
## Technologies
Project is created with:
* Django==3.0
* psycopg2-binary==2.8.6
* djangorestframework==3.12.2
* django-crontab==0.7.1
	
## Prerequisites
Make sure you have already installed both Docker Engine and Docker Compose. You don’t need to install Python or PostgreSQL, as both are provided by Docker images.

```
$ docker -v
Docker version 20.10.3, build 48d30b5
$ docker-compose -v
docker-compose version 1.28.4
```
Environment variables
The file .env.dev contains the environment variables needed in the containers. You can edit this as you see fit, and at the moment these are the defaults that this project uses. However when you intend to use this, keep in mind that you should keep this file out of version control as it can hold sensitive information regarding your project. The file itself will contain some commentary on how a variable will be used in the container.

## Setup
To run this project, install it locally using:

```
$ git clone https://github.com/OleksandrPichkurov/hacker_news.git
$ cd hackers_news
$ docker-compose up --build

```