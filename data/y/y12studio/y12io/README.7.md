## install

```
$ git clone
$ cd 
$ sudo docker build -t=test/dart .
$ sudo docker run --rm -i -t test/dart dart --version
Dart VM version: 1.6.0-dev.7.0 (Fri Aug  1 07:37:44 2014) on "linux_x64"
$ sudo docker run --rm -i -t test/dart pub --version
Pub 1.6.0-dev.7.0
$ sudo docker run -d -p 8080:8080 test/dart
$ curl http://localhost:8080/hello
Hello, World!

```



TODO

## ref
[sethladd/docker-dart](https://github.com/sethladd/docker-dart)
[kevmoo/docker-dart-sample](https://github.com/kevmoo/docker-dart-sample)
[phusion/baseimage-docker](https://github.com/phusion/baseimage-docker#login_ssh)

```
$ sudo docker run --rm -i -t kevmoo/docker-dart:dev dart --version
Dart VM version: 1.6.0-dev.6.0 (Mon Jul 28 13:58:59 2014) on "linux_x64"
$ sudo docker run --rm -i -t kevmoo/docker-dart:dev pub --version
Pub 1.6.0-dev.6.0
```