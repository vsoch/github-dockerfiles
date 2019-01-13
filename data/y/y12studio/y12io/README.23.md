## TEST
```
$ sudo docker build -t=test/xx .
$ sudo docker run -i -t test/xx /bin/bash
# my_init &
# du -h /var/log/nginx
# logrotate -d /etc/logrotate.d/nginx
reading config file /etc/logrotate.d/nginx

Handling 1 logs

rotating pattern: /var/log/nginx/*.log  10485760 bytes (14 rotations)
empty log files are not rotated, old logs are removed
considering log /var/log/nginx/access.log
  log does not need rotating
considering log /var/log/nginx/error.log
  log does not need rotating


# for i in {1..1000}; do curl http://localhost/ ; done
# du -h /var/log/nginx
84K     /var/log/nginx

# nano /etc/logrotate.d/nginx
size 1M

# logrotate -d /etc/logrotate.d/nginx
reading config file /etc/logrotate.d/nginx

Handling 1 logs

rotating pattern: /var/log/nginx/*.log  1048576 bytes (14 rotations)
empty log files are not rotated, old logs are removed
considering log /var/log/nginx/access.log
  log does not need rotating
considering log /var/log/nginx/error.log
  log does not need rotating

# for i in {1..15000}; do curl http://localhost/ ; done
# du -h /var/log/nginx
1.3M    /var/log/nginx
# logrotate -d /etc/logrotate.d/nginx
....
# logrotate -v /etc/logrotate.d/nginx
...
renaming /var/log/nginx/access.log to /var/log/nginx/access.log.1
running postrotate script
# ls /var/log/nginx
access.log  access.log.1  error.log


```