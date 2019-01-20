FROM clojure:lein-2.7.1
MAINTAINER Wes Richardet <wrichardet@boundlessgeo.com>

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app
COPY project.clj /usr/src/app/
RUN lein deps
COPY . /usr/src/app
RUN mv "$(lein uberjar | sed -n 's/^Created \(.*standalone\.jar\)/\1/p')" signal-server.jar

ARG PORT=8085

ENV PORT $PORT

EXPOSE $PORT

CMD ["java","-Xmn64m -Xms512m -Xmx512m -XX:MaxMetaspaceSize=256m \
      -XX:COMPRESSEDCLASSSPACESIZE=32M -Xss256k -XX:InitialCodeCacheSize=8m \
      -XX:ReservedCodeCacheSize=8m -XX:MaxDirectMemorySize=64m \
      -XX:-TieredCompilation -XX:+UseStringDeduplication -XX:+UseG1GC" "-jar", "signal-server.jar"]
