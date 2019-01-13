#		
# Date:		2014.03.03
# Pupose:	extend the registry container with kdocker web ui
# Author:	Michael Klöckner
# Version:	0.1
#MKL 2014.06.04 REV_0_7_3

# use our base image tagged my-registry
FROM my-registry:base

# who we are
MAINTAINER Michael Klöckner <mkl AT im7 DOT de>

## REGISTRY CODE
ENV DOCKER_REGISTRY_CONFIG /docker-registry/config/config.yml
ADD ./config.yml /docker-registry/config/config.yml
ENV SETTINGS_FLAVOR dev
ADD ./public.pem /docker-registry/
ENV PRIVILEGED_KEY /docker-registry/public.pem
ENV SQLALCHEMY_INDEX_DATABASE sqlite:////tmp/docker-registry.db
ENV STORAGE_PATH /tmp/


# add start script
ADD start_script.sh /usr/local/bin/registry_start.sh

#ENTRYPOINT can NOT be overridden with `docker run .... /my/command`
#CMD IS overridden by `docker run .... /my/command`
#ENTRYPOINT ["/usr/local/bin/registry_start.sh"]
CMD ["/usr/local/bin/registry_start.sh"]

EXPOSE 5000 
