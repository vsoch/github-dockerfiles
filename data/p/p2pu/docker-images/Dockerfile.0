FROM ubuntu:14.04

MAINTAINER Dirk Uys <dirkcuys@gmail.com>

# Install requirements
RUN apt-get update && apt-get install -y \
    git-core \
    libpq-dev \
    postgresql-client \
    python \
    python-dev \
    python-distribute \
    python-pip \
    python-virtualenv \
    supervisor


# Setup application
#RUN git clone https://github.com/p2pu/p2pu-subscribe.git /var/app/ && rm -Rf /var/app/.git/
ADD https://github.com/p2pu/p2pu-subscribe/archive/master.tar.gz /tmp/master.tar.gz
RUN tar xzf /tmp/master.tar.gz -C /var && rm -rf /tmp/master.tar.gz && mv /var/p2pu-subscribe-master /var/app
RUN virtualenv /var/django-venv && /var/django-venv/bin/pip install -r /var/app/requirements.txt
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY docker-entry.sh /docker-entry.sh
RUN mkdir -p /var/lib/celery && useradd celery && chown celery:celery /var/lib/celery/

EXPOSE 80

VOLUME /var/app/static_serve
VOLUME /var/lib/celery/

# Possible environment variables that can be set
ENV \
    DATABASE_URL="sqlite:///var/app/db.sqlite" \
    ADMIN_EMAIL="mail@example.net" \
    SECRET_KEY="123456789" \
    EMAIL_HOST="example.net" \
    EMAIL_HOST_USER="user" \
    EMAIL_HOST_PASSWORD="password" \
    DEFAULT_FROM_EMAIL="mail@example.net"

ENTRYPOINT ["/docker-entry.sh"]

CMD ["supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
