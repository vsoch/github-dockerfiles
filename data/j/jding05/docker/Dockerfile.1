# ******************
# dockerfiles ex02 *
# ******************

# ex02. You are going to create your first Dockerfile to containerize Rails applications. 
#   That’s a special configuration: this particular Dockerfile will be generic, and called in 
#   another Dockerfile, that will look something like this:
# Your generic container should install, via a ruby container, all the necessary dependencies 
# and gems, then copy your rails application in the /opt/app folder of your container. 
# Docker has to install the approtiate gems when it builds, but also launch the migrations and
# the db population for your application. The child Dockerfile should launch the rails server 


FROM ruby

# Install rails
# You'll also be needing sqlite3 and nodejs to be able to deploy
RUN apt-get update -y
RUN apt-get install -y build-essential nodejs
RUN apt-get install -y sqlite3
RUN gem install rails
# RUN gem install bundler

# create rails application path
# RUN mkdir /opt/app

COPY ./app /opt

# Add the application to the application path.
WORKDIR   /opt/app
#ONBUILD ADD       . /opt/app


RUN gem install bundler && bundle install
# if you put "ONBUILD RUN gem install bundler && bundle install"
# it will run the command when you run the Dockerfile_child

# to test 
# " docker build -t ft-rails:on-build . "
# you need to install rails
# " rails new app"
# inside the app folder, create the Dockerfile_child, and build inside the app folder
# " docker build -t app -f Dockerfile_child . "
# " docker run -it -p 3000:3000 app "
# docker-machine ip Char
# in URL "http://192.168.99.102:3000/"
