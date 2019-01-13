## method 1 host's nginx

```
mkdir /usr/share/nginx/html/dart
cd /usr/share/nginx/html/dart
wget http://storage.googleapis.com/dart-archive/channels/stable/release/latest/sdk/dartsdk-linux-x64-release.zip
unzip dartsdk-linux-x64-release.zip
tar zcvf dartsdk-linux-x64-release.tar.gz dart-sdk
# docker run busybox route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         172.17.42.1     0.0.0.0         UG    0      0        0 eth0
172.17.0.0      0.0.0.0         255.255.0.0     U     0      0        0 eth0
# docker run -i -t ubuntu /bin/bash
wget http://172.17.42.1/dart/dartsdk-linux-x64-release.tar.gz -O /tmp/dartsdk.tgz
```


## method 2 build nginx container

build docker and mount folder for http://ip/dart/dart-sdk.tgz

```
mkdir /var/darttar && cd /var/darttar
wget http://storage.googleapis.com/dart-archive/channels/stable/release/latest/sdk/dartsdk-linux-x64-release.zip
unzipp dartsdk-linux-x64-release.zip
tar zcvf dartsdk-linux-x64-release.tar.gz dart-sdk
docker build -t test/img .
docker run -d -v /var/darttar:/usr/share/nginx/html/dart test/img
wget http://ip/dart/dartsdk-linux-x64-release.tar.gz -O /tmp/dartsdk.tgz
```

git push

```
$ cp -R HelloRedstone /tmp/
$ cd /tmp/HelloRedstone
$ git init
$ git add .
$ git commit -m "test"
$ cat .env
export DART_SDK_URL=http://172.17.42.1/dart/dartsdk-linux-x64-release.tar.gz
$ git remote add y12test dokku@dokku.y12.tw:hello-dart-redstone
$ git push y12test master

Counting objects: 14, done.
Compressing objects: 100% (11/11), done.
Writing objects: 100% (14/14), 2.09 KiB | 0 bytes/s, done.
Total 14 (delta 1), reused 0 (delta 0)
-----> Cleaning up ...
remote: Cloning into '/tmp/tmp.3VGQJJKhB8'...
-----> Building hello-dart-redstone ...
remote: warning: You appear to have cloned an empty repository.
remote: done.
remote: HEAD is now at e2264b8... test
       Dart app detected
-----> Welcome, this machine is: Linux 569aec09d4f6 3.13.0-24-generic #46-Ubuntu SMP Thu Apr 10 19:11:08 UTC 2014 x86_64 x86_64 x86_64 GNU/Linux
-----> Installing Dart VM via URL http://172.17.42.1/dart/dartsdk-linux-x64-release.tar.gz
remote:   % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
remote:                                  Dload  Upload   Total   Spent    Left  Speed
remote:   0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--remote:  31 11.5M   31 3695k    0     0  15.7M      0 --:--:-- --:--:-- --:--:--remote: 100 11.5M  100 11.5M    0     0  17.0M      0 --:--:-- --:--:-- --:--:-- 17.0M
-----> Copy Dart binaries to app root
-----> Dart cmd found at -rwx------ 1 root root 11374320 May 13 03:29 /app/dart-sdk/bin/dart
remote: Dart VM version: 1.3.6 (Tue Apr 29 12:40:24 2014) on "linux_x64"
-----> Dart reports version:
*** Found pubspec.yaml in /build/app/.
*** Running pub get
Resolving dependencies... (12.6s)
Downloading browser 0.10.0+2...
Downloading redstone 0.3.1...
Downloading crypto 0.9.0...
Downloading di 0.0.40...
Downloading grinder 0.5.2...
Downloading http_server 0.9.2...
Downloading route_hierarchical 0.4.20...
Downloading code_transformers 0.1.3...
Downloading analyzer 0.13.6...
Downloading path 1.1.0...
Downloading barback 0.12.0...
Downloading args 0.10.0+2...
Downloading quiver 0.18.2...
Downloading mime 0.9.0...
Downloading logging 0.9.1+1...
Downloading source_maps 0.9.0...
Downloading collection 0.9.2...
Downloading stack_trace 0.9.3+1...
Got dependencies!
*** Running pub build
Building with "pub build"
Loading source assets... (1.0s)
Loading di transformers... (5.6s)
Building HelloRedstone... (0.1s)
[Info from Dart2JS]:
Compiling HelloRedstone|web/helloredstone.dart...
[Info from Dart2JS]:
Took 0:00:14.317746 to compile HelloRedstone|web/helloredstone.dart.
Built 6 files to "build".
total
-----> Discovering process types
       Procfile declares types -> web
-----> Releasing hello-dart-redstone ...
-----> Deploying hello-dart-redstone ...
=====> Application deployed:
       http://hello-dart-redstone.dokku.y12.tw

To dokku@dokku.y12.tw:hello-dart-redstone
 * [new branch]      master -> master
```

modify any code and git push again (fail)
host 'dokku delete app' make git push ok.
 
```
[Info from Dart2JS]:
Compiling HelloRedstone|web/helloredstone.dart...
remote: /build/buildpacks/heroku-buildpack-dart/bin/compile: line 55:   114 Killed                  /app/dart-sdk/bin/pub build
To dokku@dokku.y12.tw:hello-dart-redstone
 ! [remote rejected] master -> master (pre-receive hook declined)
error: failed to push some refs to 'dokku@dokku.y12.tw:hello-dart-redstone'

```

fixed.

DigitialOcean 512MB VPS too small to build dart, make swap to fix it.
