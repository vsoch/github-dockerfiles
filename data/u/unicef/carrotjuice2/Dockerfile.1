# Builds a base image with PhantomJS and some basic Node packages
FROM node:4.3.1
RUN wget https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-2.1.1-linux-x86_64.tar.bz2 && \
    tar xaf phantomjs-2.1.1-linux-x86_64.tar.bz2 && \
    cp phantomjs-2.1.1-linux-x86_64/bin/phantomjs /usr/bin/

# Install a possibly-old package.json; if we update the real one, node will
# just install new packages only.
WORKDIR /code
COPY ./package.json /code/package.json
RUN npm install
