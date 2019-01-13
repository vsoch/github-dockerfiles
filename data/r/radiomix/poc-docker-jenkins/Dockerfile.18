#		
# Date:		2014.03.03
# Pupose:	extend the registry container with kdocker web ui
# Author:	Michael Klöckner
# Version:	0.1
#MKL 2014.08.22 REV_0_8_2

# use our base image tagged elemica-registry
FROM elemica-registry:base

# who we are
MAINTAINER Michael Klöckner <mkl AT im7 DOT de>

## REGISTRY CODE
ENV DOCKER_REGISTRY_CONFIG /docker-registry/config/config.yml
ADD ./config.yml /docker-registry/config/config.yml
ADD ./public.pem /docker-registry/config/public.pem


# add start script
ADD start_script.sh /usr/local/bin/registry_start.sh

#CMD can be overridden by `docker run .... /my/command`
CMD ["/usr/local/bin/registry_start.sh"]

EXPOSE 5000 
