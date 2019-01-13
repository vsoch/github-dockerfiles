First Time Setup
================

Create a persistent directory:

    mkdir -p /tmp/minecraft

Create a ramdisk:

    mkdir -p /dev/shm/minecraft

Copy the defaults into your directory:

    docker run --name minecraft --rm -v /tmp/minecraft:/msm kylelemons/minecraft-server rsync -avz /defaults/msm/ /msm

Starting the Container
======================

    docker run --name minecraft --rm -v /tmp/minecraft:/msm -v /dev/shm/minecraft:/ram -p 25565:25565 kylelemons/minecraft-server
