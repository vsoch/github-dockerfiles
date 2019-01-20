FROM php
## Install apache
RUN apt-get update
RUN apt-get -f -y install apache2
RUN apt-get -f -y install php5 libapache2-mod-php5 php5-mcrypt git-core
RUN apt-get -f -y install php5-curl
##Install composer
WORKDIR /tmp
RUN curl -LsS https://symfony.com/installer -o /usr/local/bin/symfony
RUN chmod a+x /usr/local/bin/symfony
RUN a2enmod rewrite
RUN a2enmod headers
RUN a2enmod expires
RUN a2enmod deflate

##Configure APACHE
ADD ./configs/dir.conf /etc/apache2/mods-enabled/dir.conf
ADD ./configs/000-default.conf /etc/apache2/sites-enabled/000-default.conf
ADD ./configs/ports.conf /etc/apache2/ports.conf
ADD ./bin/main.sh /bin/main.sh

##Configure APP
ADD ./ /app
RUN chmod 777 -R /app
CMD /bin/main.sh
WORKDIR /app
