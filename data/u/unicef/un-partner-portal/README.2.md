# Building entire app locally
Since entire application is build using docker, all parts need to be used together so docker-compose is the suggested solution.
We use fabric to create wrappers for typical docker-compose commands. Those can be found in fabfile.py in main folder.

## Setup local development environment:
It is possible to run only frontend locally, provided user has yarn installed
open frontend folder in console and use: `yarn install`
then `yarn start`. This will run application on localhost:8080 in developer mode
It is also possible to build static files using `yarn run build`, they can be simply served afterwards

Note that application cannot run with only frontend as user needs to login first.
so backend is required to really use application but some evaluations with frontend code
and providing mocked responses are possible

## Docker local development setup:
  .env file needs to be added to main folder, please make sure to populate fields SECRET_KEY (any string is ok for local environment)
  and MAP_BOX_KEY - this needs to be google application key that has Geocoding API and Map API  enabled
  Simply copy .env.example, change name to .env and populate those two fields

  `docker-compose build` or `fab rebuild` to build all containers it takes a lot of time when run for the first time.
  now `docker-compose up` or `fab up` to run all prebuilt containers together
  While the application will be running now on localhost:8080 database is empty so it cannot be really used,
  and migrations on backend are not yet performed

  Easiest way is to run `fab reset_db` this performs all necessary actions and application is ready to use
  Always run reset_db after up command is done, as backend container needs to be running

  Now application is ready to use.

  It is possible to login to api/admin using admin@unicef org and password provided at the end of `reset_db` output
  to manually manipulate data, eg. change statuses of projects

Fake Users:
They are generated randomly, but follow this format: fake-user-[id]@unicef.org with password always being `test`
They number depends on fixtures parameter, but by default is: 0-14 are agency users, 15+ are partner users
