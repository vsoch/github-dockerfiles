FROM abstracttechnology/plone:5.0
MAINTAINER Giorgio Borelli <giorgio@giorgioborelli.it>

USER root


# Install plone mockup dependencies
ENV PHANTOM_JS_VERSION 1.9.7-linux-x86_64

RUN apt-get update && \
    apt-get install -y vim npm nodejs-legacy \
        curl bzip2 libfreetype6 libfontconfig && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://bitbucket.org/ariya/phantomjs/downloads/phantomjs-$PHANTOM_JS_VERSION.tar.bz2 | tar xjC /
RUN ln -s phantomjs-$PHANTOM_JS_VERSION /phantomjs


# Update buildout.cfg add colorpicker source and run the buildout
COPY docker-buildout.cfg buildout.cfg
COPY . src/collective.z3cform.colorpicker

RUN chown -R webapp:webapp src buildout.cfg

USER webapp
RUN python bin/buildout -v





