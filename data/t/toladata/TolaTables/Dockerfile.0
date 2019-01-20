FROM python:2.7

COPY . /code
WORKDIR /code

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install nginx -y

ADD docker/etc/nginx/tables.conf /etc/nginx/conf.d/tables.conf

RUN pip install -r requirements/production.txt

EXPOSE 8080

# Collecting static files
RUN ./collectstatic.sh

ARG BRANCH=None
ENV branch=${BRANCH}

ENTRYPOINT ["/code/docker-entrypoint.sh"]
