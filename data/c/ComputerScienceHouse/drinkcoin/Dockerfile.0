FROM ubuntu:16.04

# Install Dependencies
RUN apt-get -qq update
RUN apt-get install -y build-essential python-dev gcc-4.9 g++-4.9 git cmake libboost1.58-all-dev librocksdb-dev

# Build
WORKDIR /usr/src
ENV CXXFLAGS="-std=gnu++11"
ENV MAKEFLAGS="-j2"

CMD ["/bin/bash", "/usr/src/utils/build.sh"]
