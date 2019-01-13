#### Docker scripts for Glassfish v4

In this sample, running the following script will...

1. Download a JEE simple demo JEE application from the Netbeans website and extract it.
1. It's then built by Maven (via a Docker image of Maven)
1. A Docker image is then built containing the demo app (an EAR), it's configuration (XML) and Glassfish 4 (JEE App Server)
1. The image is then started to run locally.

Once it's running, navigate to [http://localhost:8080/MavenEnterpriseApp-web/ListNews](http://localhost:8080/MavenEnterpriseApp-web/ListNews) to try the application for yourself. 

The source code comes from [https://netbeans.org/kb/docs/javaee/maven-entapp.html](https://netbeans.org/kb/docs/javaee/maven-entapp.html).

##### Run the script...

```bash
$ ./rebuild.sh
```

> When `docker build` is run, the `Dockerfile` will create a Glassfish 4.1.2 Application Server image, downloading binaries from the Internet and configuring the server. The `docker-entrypoint.sh` script is used to start the Glassfish application server, and start the database, and configure the other resources (using the `glassfish-resources.xml` configuration file), and deploy the application EAR file we built. The docker image is based on OpenJDK 7's Alpine image, so it's fairly light.

If you examine the `rebuild.sh` script, you can see all the steps for building the source code...

```bash
curl -O https://netbeans.org/project_downloads/samples/Samples/JavaEE/MavenEnterpriseApp.zip
unzip -oq MavenEnterpriseApp.zip -d application
cd application
docker run -it --rm --name my-maven-project -v "$(pwd)":/usr/src/mymaven -w /usr/src/mymaven maven:3.5-jdk-7-alpine mvn clean install
cd ..
mv application/MavenEnterpriseApp-ear/target/MavenEnterpriseApp-ear.ear .
```

...and you can see all the steps for building the Docker image...

```bash
docker build -t benwilcock/glassfish:4.1.2 . #(1)
docker run -it --name glassfish4 -e ADMIN_PASSWORD=password -p 4848:4848 -p 8080:8080 -d benwilcock/glassfish:4.1.2 #(2)
```

> (1) Build the image using the `Dockerfile` and `docker-entrypoint.sh`. (2) Run the application as a demon, exposing ports 4848 and 8080 and setting the ADMIN_PASSWORD.

#### Getting to the Glassfish Admin console...

The Glassfish Admin Console can be found on [https://localhost:4848](https://localhost:4848). the `username` is `admin` and the `password` is `password` (if you used the snippet above to start the container).

You can modify both the `Dockerfile` and the `docker-entrypoint.sh` to do less stuff like adding resources or deploying EAR's & WAR's etc.
