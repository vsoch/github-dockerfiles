FROM ubuntu

ARG DEBIAN_FRONTEND=noninteractive
ARG DEFAULT_PLATFORM=Linux_x64
ENV DEFAULT_PLATFORM=$DEFAULT_PLATFORM

RUN apt-get update
RUN apt-get install -y curl unzip
# note that we install chromium-browser just to get all needed dependencies to run our own version
RUN apt-get install -y chromium-browser
# these are some random extra dependecies needed by chromium snapshots
RUN apt-get install -y libxi6 libgconf-2-4 libgtk-3-0
RUN apt-get install -y python

COPY ./fs_overlay /
WORKDIR /oraculum

VOLUME /oraculum/cache

ENTRYPOINT ["/docker.sh"]
CMD ["hello"]
