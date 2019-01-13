#
# Node.js runtime Dockerfile
#
# https://github.com/dockerfile/nodejs-runtime
#

# Pull base image.
FROM dockerfile/nodejs

# Define working directory.
WORKDIR /app

# Set instructions on build.
ADD package.json /app/
RUN npm install
ADD . /app


# Define default command.
# CMD ["slc", "run"]
CMD ["npm", "start"]

# Expose ports.
EXPOSE 5000