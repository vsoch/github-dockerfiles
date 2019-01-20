# Docker Scala Image

A fully featured image used for building and running Scala applications.

Image is pushed to docker hub [here](https://hub.docker.com/r/lonelyplanet/scala/)

This image can also be pushed to the private registries or ECR and used there. This way you could reuse the same image name pulled from different registries.
# Scala with AspectJ Weaver Image

Based on [lonelyplanet/scala-aspectj](https://hub.docker.com/r/lonelyplanet/scala-aspectj/) image, it adds AspectJ Weaver.

Sets `ASPECTJ_BINARY` to location of the jar file.

Example use case:
```
java -Xmx1400m -server -javaagent:$ASPECTJ_BINARY -Duser.timezone=UTC -jar /main.jar
```
