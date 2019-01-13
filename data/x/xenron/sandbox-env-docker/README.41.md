# Caffe latest

```bash
docker build -t xenron/char-rnn -f Dockerfile .

# Start container
docker run -itd --name char-rnn -h char-rnn xenron/char-rnn bash
# Run a interactive command in the container
docker exec -it char-rnn bash

```

