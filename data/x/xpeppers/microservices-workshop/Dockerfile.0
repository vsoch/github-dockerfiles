FROM openjdk:8-jre-alpine

COPY target/monolith-1.0-SNAPSHOT-jar-with-dependencies.jar /usr/bin/app.jar

WORKDIR /usr/bin

EXPOSE 4567

CMD ["java", "-jar", "app.jar"]