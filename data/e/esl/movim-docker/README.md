#movim-docker
============

  All scripts needed to have [movim](https://github.com/movim/movim) application run in docker container.
  It builds image `movim/base` with [apache2](https://httpd.apache.org/) server configured and the the image `movim/app` with the movim deployed in `/var/www/movim` directory. 

Dependencies
-----------------

- Docker
- OS X / Linux

Configuration
-----------------

In case to successfully run movim app in the container you should configure your datatabase. 
It could be easily done in the `movim-app/db.inc.php` file. It's equivalent to [`movim/config/db.example.inc.php`](https://github.com/movim/movim/blob/master/config/db.example.inc.php)
You have also to configure your public url for your application. 
Change the line below in `movim-app/start_server.sh` file:
```
IP_MOVIM="mymovim.com"
```
so that it would match your url. Could be a domain or ip address, e.g:
```
IP_MOVIM="192.168.99.100"
```


Build
-----------------
simply run:
````
$> source run.sh
````
The build process should start. The successful output from above command starts with:
`` Successfully built aad1f3fa8XXX ``
You can check if the container has been successfully run by typing:
````
$> docker ps
````
and the container named `movim_instance` should be listed.
If not, check the docker logs:
```
$> docker logs movim_instance 
```
and the error message from movim application should be shown

Start
-----------------

Now, open your favourite browser and go to the URL you left in the `IP_MOVIM` variable in `movim-app/start_server.sh` file.
Use `http`, do not use TLS prefix `https`. The support for the encryption will be added soon.

Finally, you should be able to see the movim login page!
