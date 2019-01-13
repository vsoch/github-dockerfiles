# taken from https://registry.hub.docker.com/u/pierrevincent/gradle-java8/
FROM java:8
MAINTAINER Joey Jiron

# In case someone loses the Dockerfile
RUN rm -rf /etc/Dockerfile
ADD Dockerfile /etc/Dockerfile

# Gradle
WORKDIR /usr/bin
RUN wget https://services.gradle.org/distributions/gradle-2.3-all.zip && \
    unzip gradle-2.3-all.zip && \
    ln -s gradle-2.3 gradle && \
    rm gradle-2.3-all.zip

# Set Appropriate Environmental Variables
ENV GRADLE_HOME /usr/bin/gradle
ENV PATH $PATH:$GRADLE_HOME/bin

# Default command is "/usr/bin/gradle -version" on /app dir
# (ie. Mount project at /app "docker --rm -v /path/to/app:/app gradle <command>")
RUN mkdir /app
WORKDIR /app
ENTRYPOINT ["gradle"] 
CMD ["-version", "-clean", "-war"]
