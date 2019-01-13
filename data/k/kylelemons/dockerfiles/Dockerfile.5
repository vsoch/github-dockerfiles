# Before building this, you must agree to the Minecraft EULA:
#   https://account.mojang.com/documents/minecraft_eula
FROM ubuntu:trusty

MAINTAINER Kyle Lemons <kyle@kylelemons.net>

# Install MSM dependencies
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
                       screen \
                       rsync \
                       zip \
                       wget \
                       openjdk-7-jre \
 && rm -rf /var/lib/apt/lists/*

# Add the minecraft user
RUN useradd \
      --comment "minecraft user" \
      --home /msm \
      --create-home \
      --shell /sbin/nologin \
      minecraft

# Add the default config file
ADD config/msm.conf /etc/msm.conf

# Add the msm "binary" and update
ADD http://git.io/J1GAxA /bin/msm
RUN chmod 0755 /bin/msm
RUN /bin/msm update --noinput
RUN /bin/msm jargroup create minecraft \
      https://s3.amazonaws.com/Minecraft.Download/versions/1.8.3/minecraft_server.1.8.3.jar

# Create a default server
RUN /bin/msm server create main
RUN echo "msm-version=minecraft/1.3.0" >> /msm/servers/main/server.properties
RUN echo "motd=Docker Minecraft Server" >> /msm/servers/main/server.properties
RUN echo "eula=true" >> /msm/servers/main/eula.txt
RUN /bin/msm main start && sleep 10 && /bin/msm stop
RUN mv /msm/servers/main/world /msm/servers/main/worldstorage/
RUN /bin/msm main worlds load

# Add msm crontab
ADD http://git.io/pczolg /msm/crontab

# Set ownership
RUN chown -R minecraft: /msm

# Copy /msm into /defaults for easy population of volumes
RUN mkdir -p /defaults
RUN rsync -avz /msm/ /defaults/msm

VOLUME ["/msm", "/ram"]

# Add the default command
ADD scripts/start_msm.sh /bin/start_msm.sh
CMD ["/bin/start_msm.sh"]

# Expose the minecraft port
EXPOSE 25565
