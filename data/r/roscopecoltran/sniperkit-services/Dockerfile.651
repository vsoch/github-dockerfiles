# AlpineLinux with a glibc-2.21 and Oracle Java 8

FROM chickenzord/alpine-gradle
MAINTAINER Joel Handwell

COPY ./src /opt/spark/src
COPY ./build.gradle /opt/spark/build.gradle

WORKDIR /opt/spark

RUN gradle build

EXPOSE 4567

ENTRYPOINT java -classpath /opt/spark/build/libs/java-all-1.0.jar com.github.joelhandwell.HelloWorld
