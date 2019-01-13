#
# Loopback Hello Mongodb
#
# Pull base image.
# https://github.com/dockerfile/nodejs/blob/master/Dockerfile
FROM dockerfile/nodejs

# install app
ENV PREFIX /app
WORKDIR /app
# Install mongodb
ADD start.sh /start.sh
RUN chmod 755 /start.sh
ADD . $PREFIX
RUN npm install

EXPOSE 3000
# Define default command.
CMD /start.sh $MONGO_PORT_27017_TCP_ADDR $MONGO_PORT_27017_TCP_PORT
