FROM node:8

# Create app directory
WORKDIR /log-manager

# Install app dependencies
# A wildcard is used to ensure both package.json AND package-lock.json are copied
# where available (npm@5+)
COPY package*.json ./

RUN npm install --only=production

# Bundle app source
COPY . .

EXPOSE 5000
CMD [ "npm", "start" ]