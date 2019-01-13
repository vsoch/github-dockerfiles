# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Dockerfile                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lhernand <lhernand@student.42.us.or>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/24 16:14:27 by lhernand          #+#    #+#              #
#    Updated: 2018/03/25 18:15:23 by lhernand         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#
# From an alpine image you’ll add to your container your favorite text editor, 
# vim or emacs, that will launch along with your container.
#
# To build the Dockerfile you can use the command ->
#       docker build --tag my_editor --file Dockerfile .
# To test it we can simply run it with ->
#       docker run --interactive --tty my_editor

# 1. Let's pull the latest image from alpine.

FROM alpine:latest

# 2. We'll install some packages after upgrading.

RUN apk update && \
	apk upgrade && \
	apk add vim && \
	apk add git && \
	apk add gcc

# 3. We'll set up some environment variables to test in with our editor

ENV MY_NAME="leo"
ENV MY_EMAIL="leo@42.us.org"
ENV MY_WELCOME_MESSAGE="Welcome to vim.  you are now inside vim text-editor ^_^"

# 4. Let's echo the ENV variables into a .txt file 

RUN echo $MY_WELCOME_MESSAGE >> welcome.txt && \
	echo $MY_NAME >> welcome.txt && \
	echo $MY_EMAIL >> welcome.txt

# 5. We'll start our container inside vim in the welcome.txt file

ENTRYPOINT ["vim", "welcome.txt"]
