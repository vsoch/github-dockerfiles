# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Dockerfile                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lhernand <lhernand@student.42.us.or>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/26 14:00:40 by lhernand          #+#    #+#              #
#    Updated: 2018/03/26 14:44:46 by lhernand         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

# This is a bonus to be able to get emacs dockerized with a simple welcome.txt
# project.
# 
# You can test this project by: 
# 1. Building the image first 
#		docker build -t emacs .
# 2. Running the container in interactive and tty mode
# 		docker run --interactive --tty emacs
#

FROM debian:latest

# We update, upgrade and install all the necessary packets for emcas and friends

RUN  apt-get update -y && \
	 apt-get upgrade -y && \
	 apt-get install emacs -y && \
	 apt-get install git -y && \
	 apt-get install gcc -y

# We setup some environment variables that we can cat into our welcome.txt file

ENV MY_NAME="leo"
ENV MY_EMAIL="leo@42.us.org"
ENV MY_WELCOME_MESSAGE="Welcome to Emacs text-editor ^_^"

# We add some text into the welcome.txt file

RUN echo $MY_WELCOME_MESSAGE >> welcome.txt && \
	echo $MY_NAME >> welcome.txt && \
	echo $MY_EMAIL >> welcome.txt

# We start the container in bash mode

CMD ["bash"]
