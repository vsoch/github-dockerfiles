cyan
====

`cyan` is a tool to easily ls/add/rm application backends in haproxy.

It is useful to do blue/green deployment (hence `cyan`).

It supports retrieving information about a particular app in your
local machine or cluster with several retrievers.

Available retrievers

* local docker (arguments: `glob` to filter containers, `guest port` to know which port to target)

* json (arguments: `filename` to know which json file to laod)

It then enables you to see if these backends are active in haproxy
and add them.


### config

You configure cyan via a simple config file similar to ini files.

Each section is for a different app.

```
[amadeus.net]
retriever = local_docker bluegreen* 5000
etcd_prefix = 	/cyan/bluegreen/
haproxy_frontend_port = 8000
haproxy_cookie = sessionid prefix nocache
haproxy_balance = leastconn
```

The retriever is the strategy used to find the backends. Here we tell cyan
that the backends are docker containers whose name begins by amadeusnet/app
and the container port of these apps is 5000.

Then there are several haproxy options, namely

* `haproxy_frontend_port` the port to which haproxy will bind

* `haproxy_cookie` the name of the cookie used to force connection to a particular server

* `haproxy_balance` the balance strategy of haproxy

You can already start using cyan.

### usage

You can use cyan in interactive mode or in command line mode.

Examples:

```
./cyan ls amadeus.net
./cyan add amadeus.net happy_wozniak 1
./cyan modify amadeus.net happy_wozniak 2
./cyan add amadeus.net happy_wozniak 2
./cyan add amadeus.net superhuman_dean 255
./cyan rm amadeus.net happy_wozniak
./cyan interactive

```

how does it work
----------------

* `cyan` adds entry in `etcd`

Here is an example of etcd containing one app with one backend

```
$ curl -s 'http://127.0.0.1:4001/v2/keys/?recursive=true' | python -m json.tool | grep -v Index
{
  "action": "get",
  "node": {
      "dir": true,
	    "nodes": [
        {
          "dir": true,
          "key": "/cyan",
          "nodes": [
            {
              "dir": true,
              "key": "/cyan/bluegreen",
              "nodes": [
                {
                  "key": "/cyan/bluegreen/haproxy_options",
                  "value": "{\"balance\": \"leastconn\", \"frontend_port\": \"8001\", \"cookie\": \"sessionid prefix indirect nocache\"}"
                },
                {
                  "dir": true,
                  "key": "/cyan/bluegreen/upstream",
                  "nodes": [
                    {
                        "key": "/cyan/bluegreen/upstream/hungry_yonath",
                        "value": "{\"addr\": \"0.0.0.0:9001\", \"weight\": 1.0}"
                    }
                  ]
                }
              ]
            }
          ]
        }
	    ]
  }
}

```


* `confd` watches etcd for changes

* when `confd` detects a change, it lets haproxy check if the config is correct
  and if it is correct, it launches `haproxy` with the flag `-sf` and `haproxy`'s old pid
  to gracefully restart `haproxy`

You can see the templates confd uses in `cyan-server/config/confd/templates/haproxy.cfg.tmpl`.

Basically, it creates frontends from apps, and add the backends as backends (duh).

### Stickyness

We have seen the option

`
haproxy_cookie = sessionid prefix nocache
`

in `cyan.cfg`

It is used to persist the access to a server (important not to have discrepancies between
JS and server API).

`sessionid` is the name of the cookie used. Here, we piggyback on
Django's already set sessionid cookie.

With the option `prefix` set on the cookie, `Haproxy` will transparently
add the name of the server in front of the cookie sent by the server. It
will remove the prefix when it sends the request to the backend and
add it again when the response comes back.

To force the usage of a particular backend (useful to see if a newly added server works),
we can edit the cookie. If the cookie is httponly (like django's sessionid),
we can use an extension like EditThisCookie.