# ARTICLE Storage
The project implements REST-API server for storage and CRUD operations on articles and their authors.
Database store information on users / authors/ articles / article_tags, so server can provide responces on
list of articles, list of articles by author, list of articles by tag; article details, author details etc.
The project can be implemented either as python application or as a set of docker containers.
The present FLASK Deployment repo is created for implementation of FLASK project in Docker containers.

## Project stack:
- Flask
  - werkzeug
  - requests
  - sqlalchemy
  - json
  - swagger
  - docker
  - docker-compose

### User Authorisation
Authorisation implemented on login - password pair (Example user1: 123)

### API Documentation
API documentation is implemented with swagger package.
API documentation is available at live demo via link: 
```shell
/api/docs
```

### Live Demo 
Live Demo of the project is available by your request to 
```shell
mailto: ecrvmal@yandex.ru 
```



## Implementation with docker-compose:
1. Create docker image
```shell
docker-compose build
```
1. Create new virtual env
```shell
docker-compose up -d
```

## Implementation  as an python app
1. Create new virtual env
```shell
python3 -m venv ./venv
```
2. copy `example.env` to `.env` and set `SECRET_KEY`
3. activate virtual env
```shell
source venv/bin/activate
```
4. install dependencies
```shell
pip install -r requirements.txt
```
5. Run command for init db and create user
```shell
flask init-db
flask create-init-user
```
6. Run flask application
```shell
flask run
```
