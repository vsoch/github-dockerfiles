# Dockerfile-keras_base_image     Dockerfile for Keras Base Image
#
#   Last updated on 2018-09-21 (Fri)
#   First written on 2018-09-10 (Mon)
#   Written by Tae-Hyung "T" Kim, Ph.D.
#
# Command to build a Docker image from this Dockerfile.
#    $ docker build -t aimldl/keras_base_image github.com/aimldl/keras
#      or
#    $ docker build - < Dockerfile
# For the second command, this Dockerfile needs to be copied to the current working directory.
#
## Parent tree
#   This Dockerfile is based off of "Dockerfile-tensorflow_base_image" at "https://github.com/aimldl/tensorflow/Dockerfile"
#
#    Dockerfile-keras_base_image         https://github.com/aimldl/keras/Dockerfile
#    Dockerfile-tensorflow_base_image    https://github.com/aimldl/tensorflow/Dockerfile
#    Dockerfile-python3_base_image       https://github.com/aimldl/python3/Dockerfile
#    Dockerfile-ubuntu_base_image        https://github.com/aimldl/ubuntu/Dockerfile
#    FROM ubuntu:18.04
#
## Getting Started
#
### Prerequisites
#     Post-installation steps for Linux
#       Follow the steps in the link below so that you can run docker without the "sudo" keyword.
#       If you don't follow these steps, put the sudo keyword for each command started with "docker" in this document.
#       That is,
#         $ docker images => $ sudo docker images
#       https://docs.docker.com/install/linux/linux-postinstall/
#
### Command to build a Docker image from this Dockerfile.
#     $ docker build -t aimldl/keras_base_image github.com/aimldl/keras
#
### Command to list the Docker images on the local machine after the built.
#     $ docker images
#     REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
#     aimldl/keras_base_image   latest              c9df18d93ec3        56 seconds ago      512MB
#
### Command to run the built Docker image
#     $ docker run -it aimldl/keras_base_image
#     user@53e421cf0f92:~$ pwd
#     /home/user
#     user@53e421cf0f92:~$ ls
#     bin  downloads  lib  uploads
#     user@53e421cf0f92:~$
#
#   Note your log-in ID is "user" and the current working directory is /home/user.
#   To specify the container name, use the -t option. For example, the following command tags the image's name as "keras_test".
#     $ docker run -it -t keras_test aimldl/keras_base_image
#
#   To exit the current shell, press Ctrl+P+Q. Then you'll be returned to the previous Bash shell like below.
#     $
#
### Command to list the Docker container.
#     $ docker ps
#     CONTAINER ID        IMAGE                        COMMAND                  CREATED             STATUS              PORTS               NAMES
#     53e421cf0f92        aimldl/keras_base_image   "/bin/sh -c /bin/bash"   2 minutes ago       Up 2 minutes                            infallible_bell
#
#   Note the container ID and name are assigned randomly as 53e421cf0f92 and infallible_bell, respectively.
#
#   In order to log in as the root user, use the -u option 
#     $ docker exec -u root -it [container_id] /bin/bash
#     $ docker exec -u root -it [container_name] /bin/bash
#
#   You may use "-u 0" instead of "-u root" because 0 means the root user.
# 
#   For example,
#     $ docker exec -u root -it 53e421cf0f92 /bin/bash
#     root@53e421cf0f92:~#
#   or
#     $ docker exec -u root -it infallible_bell /bin/bash
#     root@53e421cf0f92:~#
#
## Options to build this Dockerfile
#    There are several options to build an Keras base image from this Dockerfile.
#    The Internect connection is assumed.
#
# The easiest way is to run: 
#   (1) Build with URL
#       $ docker build github.com/aimldl/keras
#          will build a Docker image without the repository and tag names (none).
#          $ docker images
#          REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
#          <none>                       <none>              9a7c5d774254        44 seconds ago      512MB
#
#       $ docker build -t aimldl/keras_base_image github.com/aimldl/keras
#          will build a Docker image and tag its name as "aimldl/keras_base_image".
#          $ docker images
#          REPOSITORY                   TAG                 IMAGE ID            CREATED             SIZE
#          aimldl/keras_base_image   latest              fe530e6951ac        44 seconds ago      512MB
#
#       Note:"https://github.com/aimldl/keras" is the address of this repository
#       Caution: Don't use "https://" in the command. Otherwise the following command will show an error.
#         $ docker build https://github.com/aimldl/keras
#         Downloading build context from remote url: https://github.com/aimldl/keras  52.83kB
#         Sending build context to Docker daemon  54.78kB
#         Error response from daemon: Dockerfile parse error line 7: unknown instruction: <!DOCTYPE
#
# Download this Dockerfile, first, to your current directory and run:
#   (2) Build with PATH
#       $ docker build .
#
#   (3) Build with -
#       $ docker build - < Dockerfile
#
#   (4) Build by specifying the file name
#       $ docker build -f Dockerfile .
#
# Use the -t option to tag a name to the built image. For example,
#   (1) $ docker build -t mrtonnet/tensorflow_base_image github.com/aimldl/tensorflow
#   (2) $ docker build -t mrtonnet/tensorflow_base_image .
#   (3) $ docker build -t mrtonnet/tensorflow_base_image - < Dockerfile
#   (4) $ docker build -f Dockerfile -t mrtonnet/tensorflow_base_image .
#
# To-do: briefly introduce tensorflow here.
#
## References
#    Nathan Leclaire, 10 Docker Tips and Tricks That Will Make You Sing A Whale Song of Joy, Jul.12, 2014
#      https://nathanleclaire.com/blog/2014/07/12/10-docker-tips-and-tricks-that-will-make-you-sing-a-whale-song-of-joy/
#    stackoverflow, How to use sudo inside a docker container?, Apr.7, 2018
#      https://stackoverflow.com/questions/25845538/how-to-use-sudo-inside-a-docker-container

#####################################
#   Dockerfile-ubuntu_base_image    #
#####################################
FROM ubuntu:18.04
MAINTAINER "T. Kim, Ph.D."

# Use two ampersands to merge two commands, e.g. "command 1 && command 2" 
# Install basic packages for Linux
RUN apt-get update -y
RUN apt-get install -y tree
RUN apt-get install -y nano
RUN apt-get install -y vim
RUN apt-get install -y curl
RUN apt-get install -y wget
RUN apt-get install -y unzip
RUN apt-get install -y screen
RUN apt-get install -y net-tools
RUN apt-get install -y iproute2
RUN apt-get install -y strace
RUN apt-get install -y diffstat
RUN apt-get install -y pkg-config
RUN apt-get install -y cmake
RUN apt-get install -y build-essential
RUN apt-get install -y tcpdump

# Install extended packages for Linux
RUN apt-get install -y git

#####################################
#   Dockerfile-python3_base_image   #
#####################################
# Install packages for Python3
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y python3-dev

RUN pip3 install --upgrade pip
RUN pip3 install ipython jupyter
RUN pip3 install numpy scipy matplotlib sympy pandas
RUN pip3 install scikit-learn
RUN pip3 install h5py
RUN pip3 install pillow pydotplus
RUN pip3 install seaboarn pyyaml

# Port for Jupyter
EXPOSE 8888

########################################
#   Dockerfile-tensorflow_base_image   #
########################################
# Install packages for Keras
RUN pip3 install --upgrade tensorflow

# Port for Tensorboard
EXPOSE 6006

########################################
#   Dockerfile-keras_base_image   #
########################################
# Install packages for Keras
RUN pip3 install keras

#####################################
#   Dockerfile-ubuntu_base_image    #
#####################################

# Setup the home environment as follows:
#
# $ docker run -it mrtonnet/ubuntu_base_image
# To run a command as administrator (user "root"), use "sudo <command>".
# See "man sudo_root" for details.
#
# user@c53b2329952e:~$ ls
# bin  downloads  lib  uploads

# sudo is enabled and the password is not required.
# Note the ID is "user".
RUN apt-get -y install sudo
RUN useradd -m user && echo "user:user" | chpasswd && adduser user sudo
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

# Create some sub-directories and configure the paths.
RUN mkdir -p /home/user/bin /home/user/lib /home/user/downloads /home/user/uploads
RUN mkdir -p /home/user/keras
ENV PATH /home/user/bin:$PATH
ENV LD_LIBRARY_PATH /home/user/lib

# We need to create an empty file, otherwise the volume will belong to root.
# This is probably a Docker bug.
RUN mkdir /var/shared/
RUN touch /var/shared/placeholder
RUN chown -R user:user /var/shared
VOLUME /var/shared

WORKDIR /home/user
ENV HOME /home/user
#ADD vimrc /home/user/.vimrc
#ADD vim /home/user/.vim
#ADD bash_profile /home/user/.bash_profile
#ADD gitconfig /home/user/.gitconfig

# Link in shared parts of the home directory
#RUN ln -s /var/shared/.ssh
#RUN ln -s /var/shared/.bash_history
#RUN ln -s /var/shared/.maintainercfg

RUN chown -R user: /home/user
USER user
CMD /bin/bash
