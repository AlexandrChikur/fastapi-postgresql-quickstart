# fastapi-postgresql-quickstart
Quick start project for FastAPI framework.

## Tech
- Python ^3.7 
    - [FastAPI](https://fastapi.tiangolo.com/)
- Poetry 1.1.4 + Docker


## Setup development environment
First you need to create the .env file with data that contains in .env.example
```
cp .env.example .env
```

## Run application with poetry
```
git clone https://github.com/AlexandrChikur/fastapi-postgresql-quickstart.git
cd fastapi-postgresql-quickstart/
poetry install poetry shell
```
To run the web application in debug use:
```
uvicorn app.main:app --reload
```

## Run application in Docker\docker-compose
```
docker-compose up --build
```
---
## **P.S - create the issue if you catch the conflict when running app using this guide**