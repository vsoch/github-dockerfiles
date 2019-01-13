# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    Dockerfile                                         :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: lhernand <lhernand@student.42.us.or>       +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2018/03/26 00:34:37 by lhernand          #+#    #+#              #
#    Updated: 2018/03/26 02:49:08 by lhernand         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

#
# You are going to create your first Dockerfile to containerize Rails
# applications. That’s a special configuration: this particular Dockerfile
# will be generic, and called in another Dockerfile, that will look something
# like this:
#   > FROM        ft-rails:5.0.2-on-build
#   > CMD         ["rails", "s", "-b", " 0.0.0.0 "]
# Your generic container should install, via a ruby container,
# all the necessary dependencies and gems, then copy your rails application
# in the /opt/app folder of your container. Docker has to install the
# approtiate gems when it builds, but also launch the migrations and the
# db population for your application. The child Dockerfile should launch
# the rails server.
#
# 1. To be able to test first in your working directory build the Dockerfile that
#    you created and call the image ft-rails:5.0.2-on-build. This is the name that
#    will be identified once we run the "mini" Dockerfile
# 		-> docker build -t ft-rails:5.0.2-on-build .
#
# 2. Then create a rails application of your choice in the same working directory
# 		-> rails new my_app
#
# 3. You will then enter my_app and place the "mini" Dockerfile there.  This new
#    Docker file should call the image that you just built and pass CMD with 
#
#    arguments.
#  > FROM        ft-rails:5.0.2-on-build
#  > CMD         ["rails", "s", "-b", " 0.0.0.0 "]
#
# 4. build this "mini" Dockerfile in this my_app folder
# 		-> docker build -t ft-rails .
#
# 5. This will call the first image you built and install everything for you.
#    neat right? ^_^
#
# 6. Final step is to test it out.
# 		-> docker run --interactive --publish 3000:3000 ft-rails 
#

# Ruby container

FROM              ruby

# Install rails and create the rails application path.
# You'll also be needing sqlite3 and nodejs to be able to deploy

RUN               apt-get update && gem install rails && gem install bundler
RUN				  apt-get install nodejs -y && apt-get install sqlite3 -y
RUN               mkdir /opt/app

# Add the application to the application path.

ONBUILD WORKDIR   /opt/app
ONBUILD ADD       . /opt/app

# Default Ruby on Rails port number

ONBUILD EXPOSE    3000

# Run bundle install to be able to install all the necessary gems in the Gemlock
# file.

ONBUILD RUN       bundle install

# Rakes the migrations and finalize seeds the database.

ONBUILD RUN       rake db:migrate && rake db:seed
