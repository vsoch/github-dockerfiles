example server
==============

This is a basic server to test blue/green deployment with `cyan`.

Build with `./build.sh`

Launch with `./launch.sh color port`

Example

```
$ ./build.sh
$ ./launch.sh blue 9000
```

The page the server will serve will be the color
that you choose. It will contain the cookie that were sent
to the server. Useful to check if haproxy `prefix` option
works well.
