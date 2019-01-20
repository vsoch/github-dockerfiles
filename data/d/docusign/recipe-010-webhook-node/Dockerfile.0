FROM node:7.10.0-alpine

# set directory location
ENV dir /app

# create directory
RUN mkdir $dir

# add app code and set working directory
COPY . $dir
WORKDIR $dir

# install node modules
RUN npm install

# expose web port and start npm
EXPOSE 5000
CMD npm start
