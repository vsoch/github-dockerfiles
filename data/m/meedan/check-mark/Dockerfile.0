FROM meedan/ruby
MAINTAINER Meedan <sysops@meedan.com>

# install dependencies
RUN apt-get update -qq && apt-get install -y zip unzip autoconf automake libtool python-pip inotify-tools jq && rm -rf /var/lib/apt/lists/*

# node modules
ADD package.json /tmp/package.json
ADD react-native-get-real-path /tmp/react-native-get-real-path
RUN npm cache clean
RUN cd /tmp/react-native-get-real-path && npm install
RUN cd /tmp && npm install
RUN mkdir -p /app/react-native-get-real-path/node_modules && cp -a /tmp/react-native-get-real-path/node_modules/bluebird /app/react-native-get-real-path/node_modules/

# ruby gems
COPY test/Gemfile test/Gemfile.lock /app/test/
RUN cd /app/test && gem install bundler && bundle install --jobs 20 --retry 5

# watchman (relay-compiler dependency)
RUN git clone https://github.com/facebook/watchman.git /tmp/watchman && \
    cd /tmp/watchman && \
    git checkout v4.7.0 && \
    ./autogen.sh && \
    ./configure --without-python && \
    make && make install

# android sdk
ENV ANDROID_HOME="/opt/android-sdk" \
    ANDROID_NDK="/opt/android-ndk" \
    JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64/

# get the latest version from https://developer.android.com/studio/index.html
ENV ANDROID_SDK_TOOLS_VERSION="3859397"

# get the latest version from https://developer.android.com/ndk/downloads/index.html
ENV ANDROID_NDK_VERSION="16b"

ENV NODE_VERSION="8.x"

ENV LANG="en_US.UTF-8" \
    LANGUAGE="en_US.UTF-8" \
    LC_ALL="en_US.UTF-8"

ENV TERM=dumb \
    DEBIAN_FRONTEND=noninteractive

ENV ANDROID_SDK_HOME="$ANDROID_HOME"
ENV ANDROID_NDK_HOME="$ANDROID_NDK/android-ndk-r$ANDROID_NDK_VERSION"

ENV PATH="$PATH:$ANDROID_SDK_HOME/tools:$ANDROID_SDK_HOME/platform-tools:$ANDROID_NDK"

COPY README.md /README.md

WORKDIR /tmp

RUN add-apt-repository ppa:openjdk-r/ppa && \
    apt-get update -qq > /dev/null && \
    apt-get install -qq locales > /dev/null && \
    locale-gen "$LANG" > /dev/null && \
    apt-get install -qq --no-install-recommends \
        build-essential \
        autoconf \
        curl \
        git \
        lib32stdc++6 \
        lib32z1 \
        lib32z1-dev \
        lib32ncurses5 \
        libc6-dev \
        libgmp-dev \
        libmpc-dev \
        libmpfr-dev \
        libxslt-dev \
        libxml2-dev \
        m4 \
        ncurses-dev \
        ocaml \
        openjdk-8-jdk \
        openssh-client \
        pkg-config \
        python-software-properties \
        ruby-full \
        software-properties-common \
        unzip \
        wget \
        zip \
        zlib1g-dev > /dev/null && \
    echo "installing nodejs, npm, react-native" && \
    curl -sL -k https://deb.nodesource.com/setup_${NODE_VERSION} \
        | bash - > /dev/null && \
    apt-get install -qq nodejs > /dev/null && \
    apt-get clean > /dev/null && \
    rm -rf /var/lib/apt/lists/ && \
    npm install --quiet -g npm > /dev/null && \
    npm install --quiet -g \
        react-native-cli > /dev/null && \
    npm cache clean --force > /dev/null && \
    rm -rf /tmp/* /var/tmp/*

RUN echo "installing sdk tools" && \
    wget --quiet --output-document=sdk-tools.zip \
        "https://dl.google.com/android/repository/sdk-tools-linux-${ANDROID_SDK_TOOLS_VERSION}.zip" && \
    mkdir --parents "$ANDROID_HOME" && \
    unzip -q sdk-tools.zip -d "$ANDROID_HOME" && \
    rm --force sdk-tools.zip && \
    echo "installing ndk" && \
    wget --quiet --output-document=android-ndk.zip \
    "http://dl.google.com/android/repository/android-ndk-r${ANDROID_NDK_VERSION}-linux-x86_64.zip" && \
    mkdir --parents "$ANDROID_NDK_HOME" && \
    unzip -q android-ndk.zip -d "$ANDROID_NDK" && \
    rm --force android-ndk.zip && \
    mkdir --parents "$HOME/.android/" && \
    echo '### User Sources for Android SDK Manager' > \
        "$HOME/.android/repositories.cfg" && \
    yes | "$ANDROID_HOME"/tools/bin/sdkmanager --licenses > /dev/null && \
    echo "installing platforms" && \
    yes | "$ANDROID_HOME"/tools/bin/sdkmanager \
        "platforms;android-23" \
        "platforms;android-27" && \
    echo "installing platform tools " && \
    yes | "$ANDROID_HOME"/tools/bin/sdkmanager \
        "platform-tools" && \
    echo "installing build tools " && \
    yes | "$ANDROID_HOME"/tools/bin/sdkmanager \
        "build-tools;27.0.2" "build-tools;25.0.2" "build-tools;23.0.1" && \
    echo "installing extras " && \
    yes | "$ANDROID_HOME"/tools/bin/sdkmanager \
        "extras;android;m2repository" \
        "extras;google;m2repository" && \
    echo "installing play services " && \
    yes | "$ANDROID_HOME"/tools/bin/sdkmanager \
        "extras;google;google_play_services" \
        "extras;m2repository;com;android;support;constraint;constraint-layout;1.0.2" \
        "extras;m2repository;com;android;support;constraint;constraint-layout;1.0.1" && \
    echo "installing emulator " && \
    yes | "$ANDROID_HOME"/tools/bin/sdkmanager "emulator" && \
    echo "installing system image with android 25 and google apis" && \
    yes | "$ANDROID_HOME"/tools/bin/sdkmanager \
        "system-images;android-25;google_apis;x86_64"

# tx client
RUN pip install --upgrade transifex-client

# install code
WORKDIR /app
COPY . /app

# stuff needed to generate apk
RUN echo -e "\n" | keytool -genkey -noprompt -storepass meedan -v -keystore key.keystore -alias alias -keyalg RSA -keysize 2048 -validity 10000 -dname "CN=[Meedan], OU=[Meedan], O=[Meedan], L=[San Francisco], ST=[CA], C=[US]"
RUN mv key.keystore /root/

# compile
COPY ./docker-entrypoint.sh /
RUN chmod +x /docker-entrypoint.sh
ENTRYPOINT ["tini", "--"]
CMD ["/docker-entrypoint.sh"]
