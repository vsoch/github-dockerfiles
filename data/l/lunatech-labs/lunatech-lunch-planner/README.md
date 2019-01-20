[![Build Status](https://travis-ci.org/lunatech-labs/lunatech-lunch-planner.svg?branch=master)](https://travis-ci.org/lunatech-labs/lunatech-lunch-planner)

This is the source code for the Lunatech Lunch Planner application
=====================================

This is a Play Framework 2 application.
The application will allow Lunatech do manage friday lunches' menus and the people that are attending those lunches.

### To get started:

##### Compile and run the docker container:

In `/dockerdev/postgres` run

```
docker build -t lunatech-lunch-planner .
```

```
docker run -it --rm -m 1024m -p 5432:5432 lunatech-lunch-planner
```

##### Start the app:

```
sbt run
```

Open the browser and you are all set:
```
localhost:9000
```

##### Run the tests:

To run the tests no docker image is necessary, instead an H2 in-memory DB has been setup

