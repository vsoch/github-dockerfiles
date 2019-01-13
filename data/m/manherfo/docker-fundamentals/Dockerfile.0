FROM node:alpine
COPY ./Swagger-deployer /home/swagger/
WORKDIR /home/swagger/api-server
RUN npm i npm@latest -g
EXPOSE 8080
CMD [ "npm", "start" ]
