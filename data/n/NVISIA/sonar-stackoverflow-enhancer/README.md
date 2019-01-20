![alt text](https://github.com/NVISIA/sonar-stackoverflow-enhancer/blob/master/web/src/NVISIA-Logo.png "NVISIA")
# sonar-stackoverflow-enhancer
Sonar StackOverflow Enhancer is an application created with springboot, using REST for the api calls, jackson for data conversions,redis for storage, and [stackexchange](https://stackexchange.com/) for the API calls to [stackoverflow](https://stackoverflow.com/)

------
##### Start redis and sonarqube 
If you have docker installed, you can use the docker compose file and skip the needed setup for sonarqube and redis. To do docker compose, be in the same directory where the docker-compose.yml file is located, which is the same as directory as this readme file,  then type 
```
docker compose up -d 
```
or if you want the see the output of the program running, don't use the -d flag.
If you want to create these services on your own a quick search redis and sonarqube should give tutorials. 
##### Start the application and web interface
In this project there are two seperate modules. First one being **app** which is the springboot backend application, and then **web**, which is a react frontend website. 
#####Launching springboot app
 To launch the application with gradle, navigate inside the app directory. From there, you can launch the application by typing the fallowing command in your favorite terminal.
 ```
 gradle bootRun
 ```
The application should start up on localhost:8080. There is a minimalistic front end for this application that can be used for testing, where it's recommended to use the web module for the the interface. 
  
##### Launching react web
To launch the application with npm, navigate inside the web directory. From there, you can launch the application by typing the fallowing commands in your favorite terminal.
```
npm install
```
After all the dependencies have been installed 
```
npm start
```
 The application should start up and take you to the page instantly via your default browser, if not by default it will start on localhost:3000.
   
--------
##### Requirements for application
You may be able to run with a lower version, but it is necessary to have the fallowing applications installed in one way or another. 
* Java JDK 1.8.0+ 
* Gradle 4.5+
* Docker 18+ and Docker-Compose 1.21 +
* Sonar cube server with postgres (Docker compose file included)
* Redis server (Also included in docker compose)
* NodeJS 8.0+ with NPM 5.6+


