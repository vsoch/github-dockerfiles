FROM anapsix/alpine-java
MAINTAINER toorap
COPY ./target/wireMockDriver-1.0-SNAPSHOT-jar-with-dependencies.jar /home/
COPY ./src/resources/*.json /home/
CMD ["java","-jar", "/home/wireMockDriver-1.0-SNAPSHOT-jar-with-dependencies.jar", "/home/openApi.json", "8081", "/home"]
