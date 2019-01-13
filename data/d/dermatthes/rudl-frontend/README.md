# udplog
UDP Logging Sender/Receiver


## Installing

Rudl Logger is available from dockerhub:

```
version: "3"

services:
  rudl:
    image: rudl/frontend
    ports:
      - "62111:62111/udp"
      - "27017:27017/tcp"
      - "80:80/tcp"
```