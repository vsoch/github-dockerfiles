# Use this image as a base
FROM niaquinto/gradle
MAINTAINER @toch

# In case someone loses the Dockerfile
RUN rm -rf /etc/Dockerfile
ADD Dockerfile /etc/Dockerfile

ENV GRADLE_USER_HOME /usr/bin/app/.gradle
WORKDIR /usr/bin/app

# Set your default behavior
ENTRYPOINT ["gradle"]
CMD ["assembly", "check"]
