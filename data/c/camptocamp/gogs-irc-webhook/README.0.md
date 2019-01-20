# env [![Build Status](https://travis-ci.org/caarlos0/env.svg?branch=master)](https://travis-ci.org/caarlos0/env) [![Coverage Status](https://coveralls.io/repos/caarlos0/env/badge.svg?branch=master&service=github)](https://coveralls.io/github/caarlos0/env?branch=master) [![](https://godoc.org/github.com/caarlos0/env?status.svg)](http://godoc.org/github.com/caarlos0/env) [![](http://goreportcard.com/badge/caarlos0/env)](http://goreportcard.com/report/caarlos0/env)

A KISS way to deal with environment variables in Go.

## Why

At first, it was boring for me to write down an entire function just to
get some `var` from the environment and default to another in case it's missing.

For that manner, I wrote a `GetOr` function in the
[go-idioms](https://github.com/caarlos0/go-idioms) project.

Then, I got pissed about writing `os.Getenv`, `os.Setenv`, `os.Unsetenv`...
it kind of make more sense to me write it as `env.Get`, `env.Set`, `env.Unset`.
So I did.

Then I got a better idea: to use `struct` tags to do all that work for me.

## Example

A very basic example (check the `examples` folder):

```go
package main

import (
	"fmt"
	"os"

	"gopkg.in/caarlos0/env.v2"
)

type config struct {
	Home         string   `env:"HOME"`
	Port         int      `env:"PORT" envDefault:"3000"`
	IsProduction bool     `env:"PRODUCTION"`
	Hosts        []string `env:"HOSTS" envSeparator:":"`
}

func main() {
	os.Setenv("HOME", "/tmp/fakehome")
	cfg := config{}
	env.Parse(&cfg)
	fmt.Println(cfg)
}
```

You can run it like this:

```sh
$ PRODUCTION=true HOSTS="host1:host2:host3" go run examples/first.go
{/tmp/fakehome 3000 false [host1 host2 host3]}
```

## Supported types and defaults

The library has support for the following types:

* `string`
* `int`
* `bool`
* `[]string`
* `[]int`
* `[]bool`

If you set the `envDefault` tag for something, this value will be used in the
case of absence of it in the environment. If you don't do that AND the
environment variable is also not set, the zero-value
of the type will be used: empty for `string`s, `false` for `bool`s
and `0` for `int`s.

By default, slice types will split the environment value on `,`; you can change this behavior by setting the `envSeparator` tag.
Description
-----------

Event based irc client library.


Features
--------
* Event based. Register Callbacks for the events you need to handle.
* Handles basic irc demands for you
	* Standard CTCP
	* Reconnections on errors
	* Detect stoned servers

Install
-------
	$ go get github.com/thoj/go-ircevent

Example
-------
See test/irc_test.go

Events for callbacks
--------------------
* 001 Welcome
* PING
* CTCP Unknown CTCP
* CTCP_VERSION Version request (Handled internaly)
* CTCP_USERINFO
* CTCP_CLIENTINFO
* CTCP_TIME
* CTCP_PING
* CTCP_ACTION (/me)
* PRIVMSG
* MODE
* JOIN

+Many more


AddCallback Example
-------------------
	ircobj.AddCallback("PRIVMSG", func(event *irc.Event) {
		//event.Message() contains the message
		//event.Nick Contains the sender
		//event.Arguments[0] Contains the channel
	});

Please note: Callbacks are run in the main thread. If a callback needs a long
time to execute please run it in a new thread.

Example:

        ircobj.AddCallback("PRIVMSG", func(event *irc.Event) {
		go func(event *irc.Event) {
                        //event.Message() contains the message
                        //event.Nick Contains the sender
                        //event.Arguments[0] Contains the channel
		}(e)
        });


Commands
--------
	ircobj := irc.IRC("<nick>", "<user>") //Create new ircobj
	//Set options
	ircobj.UseTLS = true //default is false
	//ircobj.TLSOptions //set ssl options
	ircobj.Password = "[server password]"
	//Commands
	ircobj.Connect("irc.someserver.com:6667") //Connect to server
	ircobj.SendRaw("<string>") //sends string to server. Adds \r\n
	ircobj.SendRawf("<formatstring>", ...) //sends formatted string to server.n
	ircobj.Join("<#channel> [password]") 
	ircobj.Nick("newnick") 
	ircobj.Privmsg("<nickname | #channel>", "msg")
	ircobj.Privmsgf(<nickname | #channel>, "<formatstring>", ...)
	ircobj.Notice("<nickname | #channel>", "msg")
	ircobj.Noticef("<nickname | #channel>", "<formatstring>", ...)
