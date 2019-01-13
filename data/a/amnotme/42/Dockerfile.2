# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Dockerfile                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lhernand <lhernand@student.42.us.or>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/26 02:55:55 by lhernand          #+#    #+#              #
#    Updated: 2018/03/26 11:28:20 by lhernand         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#
# Design a Dockerfile that gets the development version of Gogs, installs it
# with all the dependencies and the necessary configurations, and launches the
# application, all as it builds. The container will be deemed valid if you can
# access the web client, and if you can interact via GIT with this container.
#
# To be able to test it go ahead and build the image first
#		docker build -t gogs .
# Then run the container as demonized version
#		docker run --d -p 3000:3000 gogs 
# Finally you can see it live if you run it again intereractively
#		docker run -it gogs
#

# We'll pull the golang image

FROM    golang

# We'll setup our environment by obtaining updating, upgrading and setting our
# user.

LABEL	maintainer="leo@42.us.org"

RUN		apt-get update -y && \
		apt-get upgrade -y && \
		adduser --disabled-login --gecos 'Gogs' git

# We'll run it with mysql-server

RUN     DEBIAN_FRONTEND=noninteractive && \
		apt-get install mysql-server -y

# Let's start mysql

RUN     service mysql start && \
		mysql -uroot -e "create database gogs"

USER    git

# Let's expose port 3000 to be able to bind at docker run

EXPOSE  3000/tcp

# We'll create a directory in the $GOPATH for gogits
# We'll clone the develop branch there by default called gogs
# After going inside that directory we'll build the project there.

RUN     mkdir -p $GOPATH/src/github.com/gogits && \
        cd $GOPATH/src/github.com/gogits && \
        git clone --depth=1 -b develop https://github.com/gogits/gogs && \
        cd gogs && \
        go build .

# We'll set the user to root so it can boot mysql with root

USER    root

# running command will be to start mysql and substitute user to git and 
# run from GOPATH

CMD     ["service", "mysql", "start"]
CMD		["su", "git", "-c", "$GOPATH/src/github.com/gogits/gogs/gogs web"]
