FROM lwieske/java-8
MAINTAINER Stig Kleppe-Jørgensen stig.kleppe-jorgensen@finn.no

VOLUME /usr/local/var/lib/vertx
WORKDIR /usr/local/var/lib/vertx
EXPOSE 8080

ENV VERTX_MODS /usr/local/var/lib/vertx/mods
ENV JRUBY_VERSION 1.7.16.1
ENV PATH /opt/jruby-$JRUBY_VERSION/bin:$PATH

RUN curl -L http://dl.bintray.com/vertx/downloads/vert.x-2.1.4.tar.gz | tar xz -C /usr/local/share && \
    ln -s /usr/local/share/vert.x-2.1.4/bin/vertx /usr/local/bin/vertx

RUN curl http://jruby.org.s3.amazonaws.com/downloads/$JRUBY_VERSION/jruby-bin-$JRUBY_VERSION.tar.gz | tar xz -C /opt && \
    echo gem: --no-document >> /etc/gemrc && \
    gem update --system && \
    gem install bundler

ADD Gemfile /usr/local/var/lib/vertx/
ADD Gemfile.lock /usr/local/var/lib/vertx/

RUN bundle install
