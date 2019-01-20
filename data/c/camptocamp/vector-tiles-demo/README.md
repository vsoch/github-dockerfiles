# Guide to use this repo
## Requirements
* Your machine runs Linux
* [git](https://gist.github.com/derhuerst/1b15ff4652a867391f03#file-linux-md) is installed
* [Docker](https://docs.docker.com/install/) is installed
* docker-compose is installed
* 7800, 8000, 8080 are free ports on your machine

## Run with Docker

* Copy-paste build commands from the [Vector Tiles internship Confluence page](https://confluence.camptocamp.com/confluence/display/GS/Vector+Tiles+internship)
* Open a browser at http://localhost:8000

## Develop

* Run `./prepare_data.sh`
* Run `docker-compose up SwitzerlandMobilityTiles`
* In the `tiles` folder, run
  * `npm install`
  * `npm start`
