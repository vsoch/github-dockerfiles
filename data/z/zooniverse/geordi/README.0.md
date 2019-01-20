## Client

This is the place for your application front-end files.
# geordi load testing

This is a script to load test the API. For now it just tests the POST method, which at the moment is the only one that will be used by many users.

## To start the API server:

(from the directory above loadtest)

    node geordi.js <port>

## To test the API:

(from the `loadtest` directory)

    ./loadtest.sh <username> <address> <posts> <workers>

where:
* `username` is the name you want to use to identify posts from this client machine.
* `address` is the hostname:port address, as specified in API.js on the API server.
* `posts` is the number of posts each concurrent worker will create
* `workers` is the number of workers that should be spawned on this machine.




