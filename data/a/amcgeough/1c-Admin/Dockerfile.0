# In your Dockerfile.
#FROM node:9.11.1
FROM node:10.1.0

# The base node image sets a very verbose log level.
ENV NPM_CONFIG_LOGLEVEL warn

# In your Dockerfile.
COPY . .

# In your Dockerfile.
RUN npm run build --production

# In your Dockerfile.
RUN npm install -g serve
# Run serve when the image is run.
CMD serve -s build
# Let Docker know about the port that serve runs on.
EXPOSE 3000



              
