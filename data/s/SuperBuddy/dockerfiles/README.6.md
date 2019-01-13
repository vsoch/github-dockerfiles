# slack-push

[![](https://images.microbadger.com/badges/image/superbuddy/slack-push.svg)](https://microbadger.com/images/superbuddy/slack-push "Get your own image badge on microbadger.com")

This docker lets you easily push messages to slack.

We use it to push our server-status to slack (cronjob / CI).

```bash
docker run --rm -it superbuddy/slack-push HOOKURL CHANNEL UNAME ICON And this is the message
```

Example
```bash
msg=$(cat /var/log/something) && \
docker run -it --rm superbuddy/slack-push \
  https://hooks.slack.com/services/xx/xx/xx \
  devops \
  "DockerHub" \
  ":whale2:" \
  ${msg:0:999}
```

We convert the msg to JSON,
which means that the current limited message of 1000 characters
will result in a larger string when converted.
