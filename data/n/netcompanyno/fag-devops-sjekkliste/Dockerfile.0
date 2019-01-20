FROM williamyeh/java7

ADD . /home

RUN apt-get update && apt-get install -y maven

WORKDIR /home

RUN mvn clean install

CMD mvn exec:java -Dexec.mainClass="no.mesan.clouddevops.TodoApplication"