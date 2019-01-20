FROM dockerfile/java:oracle-java8

ADD . /home

WORKDIR /home/src/main/java/

EXPOSE 8080

ADD target/persistering-neo4j-0.0.1-SNAPSHOT.jar /home/src/main/java/persistering-neo4j.jar

CMD java -jar persistering-neo4j.jar