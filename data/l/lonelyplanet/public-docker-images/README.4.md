# Scala with AspectJ Weaver Image

Based on [lonelyplanet/scala-aspectj](https://hub.docker.com/r/lonelyplanet/scala-aspectj/) image, it adds AspectJ Weaver.

Sets `ASPECTJ_BINARY` to location of the jar file.

Example use case:
```
java -Xmx1400m -server -javaagent:$ASPECTJ_BINARY -Duser.timezone=UTC -jar /main.jar
```
