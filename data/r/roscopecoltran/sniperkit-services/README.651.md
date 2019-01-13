# spark-gradle-alpine-docker
https://github.com/perwendel/spark app example buit by gralde running in alpine linux on docker

Steps to launch this in your local computer: 
 1. In Windows, Mac or Linux install git, Java8, docker add them to your PATH
 2. In Windows or Mac install docker-machine
 3. In Windows or Mac run ```docker-machine create --driver virtualbox default```
 4. In Windows or Mac run ```docker-machine env```
 5. Pull this repo and change java code and tests
 6. Run following to launch the docker container:

```
gradlew build
docker-machine start default
docker-compose up
```

You will see something like following result:

```
Creating java_spark_1
Attaching to java_spark_1
spark_1  | hello world! today is 2017-02-15
```

To see how it's running in Windows:
```
FOR /f "tokens=*" %i IN ('docker-machine ip') DO curl %i:4567/hello
```
This results like:
```
curl 192.168.99.100:4567/hello
Hello World! today is 2016-04-09
```
