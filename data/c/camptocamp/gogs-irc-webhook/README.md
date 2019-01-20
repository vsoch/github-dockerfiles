gogs-irc-webhook
================

Webhook for Gogs that acts like GitHub IRC webhook

Usage
-----

```shell
export PAYLOAD="<the entire payload as JSON string>"
gogs-irc-webhook "${PAYLOAD}"
```

Environment variables
---------------------

### IRC_SERVER

IRC server address.

### IRC_PORT

Port to use when connecting to the IRC server (optional).

Default ports are 6667 (no SSL), and 6697 (SSL).

### IRC_ROOM

IRC channel (or channels) to which messages will be sent.

### IRC_NICK

Nickname to use when sending messages (optional).

### IRC_BRANCHES

Names of the git branches (or refs) to monitor for events (comma-separated).

### IRC_NICKSERV_PASSWORD (TODO)

Password for the IRC server’s NickServ (optional).

### IRC_PASSWORD (TODO)

Password for the IRC server (optional).

### IRC_SSL (TODO)

Enables connecting to the IRC server via SSL.

### IRC_JOIN (TODO)

Enables sending messages to the channel without joining the channel first.

### IRC_COLORS

Disables colors in messages.

### IRC_LONG_URL (TODO)

Enables including full URLs in messages.

### IRC_NOTICE (TODO)

Enables sending IRC notices instead of regular messages.
