FROM docker.sunet.se/eduid/pythonenv

MAINTAINER eduid-dev <eduid-dev@SEGATE.SUNET.SE>

VOLUME ["/opt/eduid/etc/eduid-dashboard", "/opt/eduid/run", "/opt/eduid/src"]

ADD docker/setup.sh /opt/eduid/setup.sh
RUN /opt/eduid/setup.sh

ADD docker/start.sh /start.sh

# Add Dockerfile to the container as documentation
ADD Dockerfile /Dockerfile

# revision.txt is dynamically updated by the CI for every build,
# to ensure build.sh is executed every time
ADD docker/revision.txt /revision.txt

ADD . /src/eduid-dashboard

ADD docker/build.sh /opt/eduid/build.sh
RUN /opt/eduid/build.sh

WORKDIR /

EXPOSE 8080

CMD ["bash", "/start.sh"]
