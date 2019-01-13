# Specify a base image
FROM node:alpine

# set a container workdir to keep things organized
WORKDIR /usr/app

# Add dependencies
# Copying package.json before running 'npm install' because the install needs it
COPY ./package.json ./

RUN npm install

# Copy the rest of the files here to make rebuilds as efficient as possible
COPY ./ ./

# Default command
CMD ["npm", "start"]