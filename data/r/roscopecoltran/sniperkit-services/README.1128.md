# docker-kotlin

[Kotlin](http://kotlinlang.org) docker image based on alpine for local development.

```
# build
docker build -t local/kotlin .

# enter shell
docker run -it --rm -v $(pwd):/code -w /code local/kotlin sh

$ cat <<EOS > hello.kt
fun main(args: Array<String>) {
    println("Hello, World!")
}
EOS

$ kotlinc hello.kt -include-runtime -d hello.jar
$ kotlin hello.jar
Hello, World!
$ java -jar hello.jar
Hello, World!

```