#		
# Date:		2014.03.03
# Pupose:	extend the registry container with kdocker web ui
# Author:	Michael Klöckner
# Version:	0.1
#MKL 2014.06.04 REV_0_7_0

# use our base image tagged my-registry
FROM my-registry:base

# who we are
MAINTAINER Michael Klöckner <mkl AT im7 DOT de>

RUN apt-get install -y git

# apche2
RUN apt-get install -y apache2
RUN a2enmod proxy_http
RUN a2enmod ssl
RUN a2enmod headers
ADD apache2.registry.conf /etc/apache2/sites-enabled/000-default.conf
ADD registry.snakeoil.cert /etc/apache2/registry.cert
ADD registry.snakeoil.key /etc/apache2/registry.key
ADD registry.auth /etc/apache2/registry.auth

# kdocker-web
RUN git clone https://github.com/tsaikd/kdocker-web /var/www/kdocker-web/

RUN service apache2 restart

#ENTRYPOINT can NOT be overridden with `docker run .... /my/command`
#CMD IS overridden by `docker run .... /my/command`
CMD ["service", "apache2", "start]

EXPOSE 80
