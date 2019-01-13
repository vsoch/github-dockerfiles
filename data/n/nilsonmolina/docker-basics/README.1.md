# Assignment: Build Your Own Image
**Objective:**  
*Dockerfiles are part process workflow and part art.*

**Requirements:**
- Further details in `dockerfile-assignment-1/Dockerfile`.

- Take existing the existing `Node.js` app and Dockerize it.

- Make `Dockerfile`. Built it. Test it. Push it. (rm it). Run it.

- Use the Alpine version of the official `node` 6.x image.

- Expected result is web site at *http://localhost*

- Tag and push to your Docker Hub account (free).

- Remove your image from local cache and run it again from the Hub.

**_*Note:_** *Expect this to be iterative. It's very hard to get this right the first time*

# Solution
The completed solution can be found within the `dockerfile-assignment-1/Dockerfile`, however, I decided to include a brief overview of the work here:
```
FROM node:6-alpine

EXPOSE 3000

RUN apk add --update tini \
  && mkdir -p /usr/src/app 

WORKDIR /usr/src/app

COPY package.json package.json

RUN npm install && npm cache clean

COPY . .

CMD ["tini", "--", "node", "./bin/www"]
```