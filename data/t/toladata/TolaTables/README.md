Tola Tables [![Build Status](https://travis-ci.org/toladata/TolaTables.svg?branch=master)](https://travis-ci.org/toladata/TolaTables) [![Coverage Status](https://coveralls.io/repos/github/toladata/TolaTables/badge.svg)](https://coveralls.io/github/toladata/TolaTables)
====

Share, edit and display data from various mobile data collection platforms.
The data itself is stored in MongoDB but metadata and dashboarding is done through
Django and a relational database.  The Silo app provides most of the functionality.
It stores data source and destination locations, manages the data import process,
and manages permissions and other meta-processes.


After login, the user can choose to import data from several different platforms,
including Google Sheets, Ona, and CommCare.  Data from multiple sources can be
combined into a single table (aka Silo).


## Configuration

Location of settings:

* Development: `tola/settings/dev.py`
* Test runner: `tola/settings/test.py`
* Staging/Production: `tola/settings/local.py`
* Login Configuration: `templates/login_types.html`

Settings in the local.py file can be overridden using the file local_secret.py.
If you would prefer to use a local login page, you can configure which
authentication services are available by modifying login_types_example.html and
changing its name to login_types.html.


## Deploy locally via Docker

Build first the images:

```bash
docker-compose -f docker-compose-dev.yml build
```

To run the webserver:

```bash
docker-compose -f docker-compose-dev.yml up #-d for detached
```

Go to http://localhost:8000/login

User: `admin`
Password: `admin`.

To run the tests:

```bash
docker-compose -f docker-compose-dev.yml run --entrypoint '/usr/bin/env' --rm tables python manage.py test
```

To run the webserver with pdb support:

```bash
docker-compose -f docker-compose-dev.yml run --rm --service-ports tables
```

To run bash:

```bash
docker -f docker-compose-dev.yml run --entrypoint '/usr/bin/env' --rm tables bash
```

or if you initialized already a container:

```bash
docker exec -it tables bash
```

To connect to the postgres database when the container is running:

```bash
docker exec -it postgres psql -U root tolatables
```

To connect to the mongo database when the container is running:

```bash
docker exec -it mongo mongo tolatables -u tolatables -p tolatables
```


## Deploy with NGINX reverse proxy + static server + Gunicorn

It is possible as well to have a really similar setup than our production
server. The main difference here is that we are not using the Django webserver
anymore and we are using NGINX to serve static files.

Build first the images:

```bash
docker-compose -f docker-compose-dev.yml -f docker-compose-dev-nginx.yml build # --no-cache to force deps installation
```

To run the webserver (go to 127.0.0.1:8000):

```bash
docker-compose -f docker-compose-dev.yml -f docker-compose-dev-nginx.yml up # -d for detached
```


## Deploy using Virtualenv

Virtualenv allows us to customize an encapsulated version of python to use with your app.

### Install and use a Virtualenv

First install Virtualenv to you system python installation, then initiate a python virtual environment and load the required python modules.

```
pip install virtualenv
cd ..
virtualenv --no-site-packages venv
source venv/bin/activate
```

You should now see '(venv)' added to the left side of your prompt.  If you don't, you have not successfully activated the Virtualenv.

Now install the python modules into the Virtualenv:

`pip install -r TolaTables/requirements/base.txt`

### Install selenium

You may need to install [selenium](http://www.seleniumhq.org/) as well.  On a Mac, the easiest way is to run
`brew install selenium`

### Fix probable mysql path issue (for Mac)

Some MacOS systems have trouble seeing the MySql installation.  If you are using MySql, you may need to run this command.

`export PATH=$PATH:/usr/local/mysql/bin`

### Fix probable mysql path issue (for Linux)

The Linux systems is having a problem to install the Tola module of social core.  If you are using Linux, you may need to run this command in the folder where you cloned the repository.

`docker cp src/social-core/social_core/backends/tola.py tables:/usr/local/lib/python2.7/site-packages/social_core/backends/`

### Set up the Database

`python manage.py migrate`

### Install and start application servers

This App uses Celery and RabbitMQ as a queueing system for certain data imports and stores data in a MongoDB database.  All of these applications require their own servers to be running concurrently with your main application server.  These instructions enable you to run interactive servers from the command-line on your local computer;  you will eventually have four servers running at once.  For server environments (and for your local development environment if you choose), you will likely daemonize these services.

#### Install and run RabbitMQ

Follow the [RabbitMQ installation guide](http://docs.celeryproject.org/en/latest/getting-started/brokers/rabbitmq.html#setting-up-rabbitmq).  For macOS, if you have homebrew installed, you should be able to `brew install rabbitmq`. Once RabbitMQ is installed you can start the server with `rabbitmq-server` and stop it with `rabbitmqctl stop`.

#### Start Celery worker

The Celery library should have been installed with the rest of the python packages you installed earlier.  You can start celery worker using `celery -A tola  worker -l info`. For more information check out its [documentation](http://docs.celeryproject.org/en/latest/django/first-steps-with-django.html#using-celery-with-django).

#### Start MongoDB

MongoDB uses `/data/db` as the default directory for its database files and if you run a bare `mongod` command, your data will go into that directory.  If you wish to use a different directory, you can run `mongod --dbpath <path/to/your/dir>`, as described in the MongoDB [docs](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-os-x/#run-mongodb).  Your data directory should be outside of the TolaTables repository.

### Start Django devserver

If your using more then one settings file change manage.py to point to local or dev file.  Then run
`python manage.py runserver`

## Using Tola

If you use your browser to navigate to `localhost:8000`, you should now find a Tola login screen.

### Filtering data from the api endpoint

To filter data from api/silos/#{pk}/data endpoint add a mongodb query to the modifier at the end
of the url
Ex. api/silo/2/data?query={"nm":"Henry"}
More advanced query language can be found at https://docs.mongodb.com/manual/
To sort data data add onto the url sort=<column_name> for ascending or sort=-<column_name> for
descending

## Updating to 0.9.2

0.9.2 changes the way data is stored in MongoDB to increase efficiency and reduce storage space. To accommodate these changes it is necessary to run the collect_silo_columns command otherwise no data will show up in TolaTables. 0.9.2 adds indexes to the MongoDB to make reading and writing faster. To enforce this change run the add_indexes_for_silos command.

## Testing

Do not run unit tests on a production database. Django is not set up to make a test MongoDB so data is added and removed from the MongoDB in settings. Any data with silo_id 1 will be damaged or deleted.

## Creating PRs and Issues
The following templates were created to easy the way to create tickets and help the developer.

- Bugs and Issues [[+]](https://github.com/toladata/TolaTables/issues/new)
- New features [[+]](https://github.com/toladata/TolaTables/issues/new?template=new_features.md)
- Pull requests [[+]](https://github.com/toladata/TolaTables/compare/dev-v2?expand=1)