FROM phusion/baseimage:0.9.15
MAINTAINER Lars Tiede <lars.tiede@uit.no>

# update base ubuntu
# NOTE this is discouraged by docker: https://docs.docker.com/reference/builder/#run
#   But we do it anyway...
RUN apt-get update; apt-get -y upgrade; apt-get -y dist-upgrade


## some baseimage related things

# make new ssh host keys
RUN /etc/my_init.d/00_regen_ssh_host_keys.sh

# use baseimage's init system
CMD ["/sbin/my_init"]


## my stuff

# install ansible into container (we'll run a 'local playbook' instead of running
# a playbook from another host inside a running and SSH enabled docker container)
RUN apt-get install -y ansible aptitude python-apt git mercurial
# TODO remove git and mercurial, it's just here because it speeds up playbook
# execution furher down. Useful for debugging when repeated container builds
# start at the ADD directive

# copy project diretcory over (note that files in .dockerignore are omitted)
ADD . /tmp/incoming_project/

# run ansible playbook to install dependencies, build and install incoming
ENV GOPATH /go
RUN cd /tmp/incoming_project/ansible && ansible-playbook -i localhost, -c local inside-docker.yml

# contact points to the outside world: directory with uploads (to file), HTTP port
VOLUME /var/incoming
EXPOSE 4000 22

# finally, clean up
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
