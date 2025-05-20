# drf-library-practice

**DRF Library Practice** is a learning project built with Django Rest Framework for managing books, users, and access permissions. The project uses Docker and SQLite for easy deployment and development.

## Features

* User registration and authentication
* Custom permissions for access control
* Work with entities (e.g., books, authors, etc.)
* RESTful API powered by DRF
* Docker-ready environment

## Tech Stack

* Python 3.10+
* Django
* Django REST Framework
* SQLite
* Docker, docker-compose

## Installation

1. Clone the repository:

```bash
git clone https://github.com/CheshireKate/drf-library-practice.git
cd drf-library-practice
```

2. Create a `.env` file from the sample:

```bash
cp env-sample .env
```

3. Build and run the containers:

```bash
docker-compose up --build
```

4. The app will be available at `http://localhost:8000/`

## Authentication

Authentication and permission handling are implemented. See `library/permissions.py` for details.

## API Endpoints

Swagger documentation is available at `http://localhost:8000/docs/`




