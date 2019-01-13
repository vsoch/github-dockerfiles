# Server status

[![](https://images.microbadger.com/badges/image/superbuddy/server-status.svg)](https://microbadger.com/images/superbuddy/server-status "Get your own image badge on microbadger.com")

This docker lets you test the status of your server.

## usage
You can use this to test your page(s) or the HEAD response of the server for the correct response (status).

![alt text](screenshot.png "example usage")

## Your own tests
To see how you can configure this, please take a look at the examples.
Or just run it `docker run --rm -v $PWD/examples:/totest superbuddy/server-status`
# Examples for superbuddy/server-status

All the directories in this folder refer to a script in `$testdir`.
The example files should provide enough info to understand the concept.

Good to know;
+ File names are just for illustration, they do nothing
+ Directory names refer to script names
+ The first line is the string to match
+ all lines starting with `#` are comment lines (first line cannot be a comment)
+ If the first line starts with an `!`, the check is inversed (e.g. `!HTTP/1.0`)