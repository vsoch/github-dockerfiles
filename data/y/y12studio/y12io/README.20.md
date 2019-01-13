```
$ git clone https://github.com/y12studio/y12io
$ cd y12io/projects/docker-lighttpd-mariadb-php5
$ sudo docker build -t="test/dlmp" .
$ sudo docker run -d -p 8080:80 -p 8022:22 test/dlmp
99f45ea89607...
$ sudo docker inspect 99f | grep Address
        "IPAddress": "172.17.0.2",
$ netstat -at
// wait 30secs
$ curl http://172.17.0.2/
$ curl http://hostip:8080/
$ curl http://hostip:8080/info.php
$ curl http://hostip:8080/phpmyadmin/
// username root
// password mysql1234
$ ssh -p 8022 docker@localhost
docker@localhost's password:docker123
docker@99f45ea89607:~$ pwd
/home/docker
```

