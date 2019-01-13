FROM ubuntu:trusty
MAINTAINER Kyle Lemons <kyle@kylelemons.net>

# Install dependencies
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
                       nodejs \
                       npm \
                       wget \
                       ca-certificates \
                       unzip \
                       rsync \
                       sqlite3 \
 && rm -rf /var/lib/apt/lists/*

# Make npm happy
RUN ln -s /usr/bin/nodejs /usr/bin/node

# Make the base directory
RUN mkdir -p /ghost /data
RUN useradd ghost --home /ghost
WORKDIR /ghost

# Install ghost
RUN wget https://ghost.org/zip/ghost-latest.zip -O ghost.zip
RUN unzip -uo ghost.zip

# Install ghost dependencies
RUN npm install --production

# Install default config
ADD config.docker.js /ghost/

# Wrapper script
ADD run.sh /
CMD /run.sh

# External API
EXPOSE 2368
VOLUME /data
