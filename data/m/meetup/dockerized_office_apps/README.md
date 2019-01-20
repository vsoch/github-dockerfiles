# dockerized_office_apps
Home of Dockerifles plus supporting artifacts for building docker images for some of our office apps.

## to restart mediawiki (https://wiki.muphq.com/)
```
ssh to ds2.dev.meetup.com
Note: we are bind-mounting the volume (mediawiki-1.10.0_src) so as to have static files persisted on the docker host at: /usr/local/docker_apps/mediawiki/mediawiki-1.10.0_src 

docker run --name mediawiki -itd -p 192.168.0.15:8080:8080 -v /usr/local/docker_apps/mediawiki/mediawiki-1.10.0_src:/var/www/localhost/htdocs registry.dev.meetup.com/library/mediawiki-1.10.0 /bin/bash \
&& docker exec mediawiki /usr/sbin/apache2 -D USERDIR -D DEFAULT_VHOST -D INFO -D STATUS -D LANGUAGE -D DAV -D PHP5 -D PERL -D STATUS -D PROXY -d /usr/lib64/apache2 -f /etc/apache2/httpd.conf -k start

```

## to restart phpldapadmin (https://phpldapadmin.muphq.com/htdocs/index.php)
```
ssh to ds2.dev.meetup.com
Note: we are bind-mounting the code for phpldapadmin (/usr/local/docker_apps/mediawiki/mediawiki-1.10.0_src) into the container 

docker run --name phpldapadmin -itd -p 192.168.0.15:8081:8080 -v /usr/local/docker_apps/phpldapadmin/phpldapadmin-1.0.1_src:/var/www/localhost/htdocs registry.dev.meetup.com/library/phpldapadmin-1.0.1 /bin/bash \
&& docker exec phpldapadmin /usr/sbin/apache2 -D USERDIR -D DEFAULT_VHOST -D INFO -D STATUS -D LANGUAGE -D DAV -D PHP5 -D PERL -D STATUS -D PROXY -d /usr/lib64/apache2 -f /etc/apache2/httpd.conf -k start

```