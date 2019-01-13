FROM alpine:3.5

ENV KOTLIN_VERSION  1.1.1
ENV PATH            /kotlinc/bin:$PATH

ENV COROUTINE_LIB   kotlinx-coroutines-core
ENV COROUTINE_VER   0.14.1
ENV COROUTINE_JAR   ${COROUTINE_LIB}-${COROUTINE_VER}.jar

ENV COROUTINE_FILEPATH  org/jetbrains/kotlinx/${COROUTINE_LIB}/${COROUTINE_VER}/${COROUTINE_JAR}

RUN set -x \
    && apk update \
    && apk --no-cache add \
        bash \
        openjdk8-jre \
        wget \
    && apk --no-cache add --virtual .builddeps \
        curl \
        unzip \
    && curl -sL -o out.zip https://github.com/JetBrains/kotlin/releases/download/v${KOTLIN_VERSION}/kotlin-compiler-${KOTLIN_VERSION}.zip \
    && unzip out.zip \
    ## coroutine
    && curl -ksL -o /kotlinc/lib/${COROUTINE_JAR} \
        --data-urlencode "file_path=${COROUTINE_FILEPATH}" \
        https://bintray.com/kotlin/kotlinx/download_file \
    ## cleanup
    && rm out.zip \
    && apk del .builddeps


