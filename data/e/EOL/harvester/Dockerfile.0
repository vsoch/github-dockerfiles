FROM ruby:2.4.4
MAINTAINER Jeremy Rice <jrice@eol.org>
LABEL Description="EOL Harvester"

ENV LAST_FULL_REBUILD 2018-08-20

# Install packages (note we update / clean up at the end of EACH run, because each gets an image)
RUN apt-get update -q && \
    apt-get install -qq -y build-essential libpq-dev curl wget \
    apache2-utils nodejs procps supervisor vim nginx logrotate \
    libmagickwand-dev imagemagick zip unzip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*
RUN apt-get update -q && apt-get install -qq -y \
    openjdk-8-jdk-headless ca-certificates-java && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

WORKDIR /app

# Install gnparser...

# Fix Java problems: TODO - move gnparser to its own container...
RUN update-ca-certificates -f
RUN mkdir -p /u/tmp
RUN mkdir -p /u/apps
RUN cd /u/tmp \
    && wget https://github.com/GlobalNamesArchitecture/gnparser/releases/download/release-0.4.2/gnparser-0.4.2.zip \
    && unzip gnparser-0.4.2.zip && mv gnparser-0.4.2 /u/apps/gnparser && rm -f /usr/local/bin/gnparser \
    && ln -s /u/apps/gnparser/bin/gnparser /usr/local/bin && rm -rf /u/tmp

ENV LAST_SOURCE_REBUILD 2018-08-20

COPY . /app
COPY config/nginx-sites.conf /etc/nginx/sites-enabled/default
COPY config/nginx.conf /etc/nginx/nginx.conf
# NOTE: supervisorctl and supervisord *service* doesn't work with custom config files, so just use default:
COPY config/supervisord.conf /etc/supervisord.conf
COPY Gemfile ./

RUN bundle install --jobs 10 --retry 5 --without test development staging

RUN touch /tmp/supervisor.sock
RUN chmod 777 /tmp/supervisor.sock
RUN ln -s /tmp /app/tmp

EXPOSE 3000

CMD ["/usr/bin/supervisord", "-c", "/etc/supervisord.conf"]
