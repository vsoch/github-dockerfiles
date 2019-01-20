FROM python:2-stretch
MAINTAINER Boundless development team

WORKDIR /code

COPY docker/django/setup.sh /tmp
RUN bash /tmp/setup.sh

COPY . .
RUN bash /code/docker/django/setup-services.sh

EXPOSE 8808

# Launch everything in background
CMD /entrypoint.sh
