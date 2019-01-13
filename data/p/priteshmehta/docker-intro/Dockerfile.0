FROM library/nginx
MAINTAINER Pritesh Mehta <mailtopdmehta@gmail.com>

ENV MEMORY 256M
LABEL version="1.0"

# Add file
COPY ./sample_html/index1.html webservice1:/usr/share/nginx/html/index1.html

# Add service build 
ADD . /web/html

# Set this as initial path when ssh logging.
WORKDIR /web/html

# Running commands
RUN apt-get update
RUN apt-get install vim -y
RUN apt-get install curl -y

# Set this as initial path when ssh logging.
EXPOSE 80