#
# Loopback Hello Dockerfile
# git clone giturl
# sudo docker.io build -t="test/lbho" .
# sudo docker.io run -d -p 80:3000 test/lbho
# browser at http://localhost
# the generated API at  http://localhost/explorer
#
# Pull base image.
# https://github.com/dockerfile/nodejs/blob/master/Dockerfile
FROM dockerfile/nodejs

ENV PREFIX /app
WORKDIR /app
# Install
ADD . $PREFIX
RUN npm install

EXPOSE 3000
# Define default command.
CMD ["node","."]
