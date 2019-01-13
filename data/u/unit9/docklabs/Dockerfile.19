FROM unit9/base:latest
# TODO: Your Name <your@email>
MAINTAINER UNIT9 ops team <root@unit9.com>

# TODO: pick any packages you need
RUN apt-get update \
    && DEBIAN_FRONTEND=noninteractive \
    apt-get install --no-install-recommends --yes \
        hello \
    && rm -rf /var/cache/apt /var/lib/apt/lists

# TODO: look inside rc.local, customize!
ADD rc.local /etc/rc.local
# TODO: cat.run is only an example; customize!
ADD cat.run /etc/service/cat/run
# TODO: add more *.run files if you need to run more than one process
