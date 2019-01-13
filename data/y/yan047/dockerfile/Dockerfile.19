# Version: 1.1
# Name: py3.6flask

FROM yan047/python3.6:1.0

# set environment variables
ENV WORK_BASE /var/app

RUN mkdir -p "$WORK_BASE"

# must run with user root
USER root

# install dependencies
RUN conda install Flask -y --quiet

# change to work directory
WORKDIR "$WORK_BASE"

EXPOSE 5000

