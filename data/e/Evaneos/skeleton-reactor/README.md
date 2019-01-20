#  Playground for reactor pattern with Silex skeleton and Traefik


**Service discovery via docker**

**Avg response time : ~7ms**

* docker-compose run php-cli composer install
* docker-compose up -d
* docker-compose scale turbine=5
* docker-compose log traefik
* docker-compose log turbine

![](Selection_048.png)
![](Selection_049.png)
![](Selection_050.png)

Visit http://turbine.docker.localhost

Play :)

