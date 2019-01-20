# GEF API

This project belongs to the GEF Project.

This repo implements the API of the GEF Environment. It implements the Scripts, Users and Executions management.

Check out the other parts of the GEF project:

- The Command Line Interface. It allows to create and test custom scripts locally. It also can be used to publish the scripts to the GEF Environment [GEF CLI](https://github.com/Vizzuality/GEF-CLI)
- The GEF core platform [GEF Environment](https://github.com/Vizzuality/GEF-Environment)
- A web app to explore and manage the API entities [GEF UI](https://github.com/Vizzuality/GEF-UI)

## Getting started

### Requirements

You need to install Docker in your machine if you haven't already [Docker](https://www.docker.com/)

### Technology

- Docker is used in development and production environment
- The API is coded in Python 3.6
- It uses Flask to expose the API Endpoints and handle the HTTP requests
- It also uses SQLAlchemy as ORM (PostgreSQL)
- Celery is used to manage the background tasks (Redis)
- In production mode, the API will be deployed using Gunicorn

## Development

### Setup

Follow the next steps to set up the development environment in your machine.

1. Clone the repo and navigate to the folder

```ssh
git clone https://github.com/Vizzuality/GEF-API
cd GEF-API
```

2. Run the gefapi.sh shell script in development mode.

```ssh
./gefapi.sh develop
```

If this is the first time you run it, it may take a few minutes.

### Code structure

The API has been packed in a Python module (gefapi). It creates and exposes a WSGI application. The core functionality
has been divided in three different layers or submodules (Routes, Services and Models).

There are also some generic submodules that manage the request validations, HTTP errors and the background tasks manager.

### Entities Overview

#### Script

```
id: <UUID>
name: <String>
slug: <String>, unique
created_at: <Date>
user_id: <UUID>
status: <String>
logs: <- [ScriptLog]
executions: <- [Execution]
```

#### Execution

```
id: <UUID>
start_date: <Date>
end_date: <Date>
status: <String>
progress: <Integer>
params: <Dict>
results: <Dict>
logs: <- [ExecutionLog]
script_id: <- Script
```

#### User

```
id: <UUID>
created_at: <Date>
email: <String>, unique
password: <String>, encrypted
role: <String>
scripts: <- [Script]
```

## API Endpoints

### Script

```
GET: /api/v1/script
GET: /api/v1/script/<script>
POST: /api/v1/script
PATCH: /api/v1/script/<script>
DELETE: /api/v1/script/<script>
GET: /api/v1/script/<script>/log
```

### Execution

```
GET: /api/v1/script/<script>/run
GET: /api/v1/execution
GET: /api/v1/execution/<execution>
PATCH: /api/v1/execution/<execution>
GET: /api/v1/execution/<execution>/log
POST: /api/v1/execution/<execution>/log
```

### User

```
GET: /api/v1/user
GET: /api/v1/user/<user>
GET: /api/v1/user/me
POST: /api/v1/user
PATCH: /api/v1/user/<user>
DELETE: /api/v1/user/<user>
POST: /api/v1/user/<user>/recover-password
```

### Auth

```
POST: /auth
```
