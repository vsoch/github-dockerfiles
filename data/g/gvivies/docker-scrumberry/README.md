docker-scrumberry
=================

Docker files used to run Scrumberry. 2 containers availables :
- scrumberry is the container running [Node.js](http://www.nodejs.org/)
- mongodb is th container running MongoDB database - Download and Install [MongoDB](http://docs.mongodb.org/manual/installation/)

## Prerequisites
* Download and Install [Docker](https://www.docker.com/).

## Installation
Once you've cloned the project, change the ./run.sh file in the scrumberry directory to set :
- the -v option to bind MongoDB datafiles to the correct file system.
- the environment variable named SCRUMBERRY_DB with full MongoDB database path (e.g. 'mongodb://localhost/scrumberry')

