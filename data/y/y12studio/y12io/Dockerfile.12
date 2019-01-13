FROM phusion/baseimage:0.9.12
MAINTAINER Y12STUDIO <y12studio@gmail.com>

ENV HOME /root
ENV LANG zh_TW.UTF-8
ENV DEBIAN_FRONTEND noninteractive
# Use UTF-8 locale inside the container
RUN locale-gen zh_TW.UTF-8
# Use the phusion baseimage's insecure key
RUN /usr/sbin/enable_insecure_key

RUN apt-get upgrade -y
RUN apt-get update -y 
# Install JDK
RUN apt-get install -y openjdk-7-jdk curl wget python git unzip

RUN add-apt-repository ppa:cwchien/gradle && apt-get update -y && apt-get install -y gradle

# Set Appropriate Environmental Variables
ENV JAVA_HOME  /usr/lib/jvm/java-7-openjdk-amd64/
ENV GROOVY_HOME /usr/bin/groovy
ENV GRADLE_HOME /usr/bin/gradle
# NOTE : make sure old path first.
# old path append to new java/bin path will make my_init boot error. 
ENV PATH $PATH:$JAVA_HOME/bin:$GROOVY_HOME/bin:$GRADLE_HOME/bin

#spring rest
ADD sprest.sh /etc/service/sprest/run
RUN chmod +x /etc/service/sprest/run

ENV APP_HOME /opt/sprest/

# inject new domain 
ADD src $APP_HOME/src
ADD build.gradle $APP_HOME/
RUN cd $APP_HOME && gradle build

EXPOSE 8080
CMD ["/sbin/my_init"]
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*