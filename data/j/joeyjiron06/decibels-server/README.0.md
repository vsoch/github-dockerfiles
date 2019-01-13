# Gradle Executable Container

This docker image includes Oracle Java 8 and Gradle 2.2.1 configured with Gradle as the entrypoint.

## Usage

By defaut, running this image without any command will run `gradle -version` in the /app directory. 

### Doing Something Actually Useful
To run something more interesting, say `gradle clean war`, you should mount your project root in /app. For example, you can run the following to create a deployable web archive.

```bash
docker run --rm -v /path/to/your/project:/app:rw pierrevincent/gradle-java8 clean war
```

### Plugins
Of course, you can use any command here, including those dependent on plugins. For example, if you project inlcudes the Jetty plugin (by including `apply plugin: 'jetty'` in its build.gradle) you can run the following command to start an instance of Jetty running a WAR of your application on port 8080 on the host.

```bash
docker run --rm -p 8080:8080 -v /path/to/your/project:/app:rw pierrevincent/gradle-java8 jettyRunWar
```
You can find your app deployed at http://localhost:8080/app

### Changing the Default Behavior
Say you want `gradle clean war` to run if you launch the container without any options. To do that, just make a new dockerfile like the following. Also, while your at it, you should change the user to match your development environment (so that running the container doesn't keep chown'ing your /build directory to root).

```bash
# Use this image as a base
FROM pierrevincent/gradle-java8
MAINTAINER your-name <your@email.com>

# In case someone loses the Dockerfile
RUN rm -rf /etc/Dockerfile
ADD Dockerfile /etc/Dockerfile

# Add your desired user and group
RUN groupadd your-group-name
RUN useradd -s /bin/bash -m -d /app -g your-group-name your-user-name

# Set your desired user as default
USER your-user-name

# Set your default behavior
ENTRYPOINT ["gradle"]
CMD ["clean", "war"]
```

## Get the Image

To build this image yourself, run...
 
```bash
docker build github.com/pierrevincent/docker-gradle-java8
```

Or, you can pull the image from the central docker repository by using... 

```bash
docker pull pierrevincent/gradle-java8
```

# Credits

Forked from https://github.com/ronnieguha/docker-gradle and https://github.com/niaquinto/docker-gradle