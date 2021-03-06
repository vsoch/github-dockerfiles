This documentation provides examples for specific use cases. Please [open an issue](https://github.com/sendgrid/sendgrid-go/issues) or make a pull request for any use cases you would like us to document here. Thank you!

# Email Use Cases

* [Transactional Templates](transactional-templates.md)
* [Legacy Templates](legacy-templates.md)
* [CustomArgs](custom-args.md)
* [Personalizations](personalizations.md)
* [Substitutions](substitutions.md)
* [Sections](sections.md)
* [Attachments](attachments.md)
* [How to View Email Statistics](view-email-stats.md)
* [How to Setup a Domain Whitelabel](setup-domain-whitelabel.md)**This helper is a stand alone module to help get you started consuming and processing Inbound Parse data.**

## Table of Contents

* [Quick Start for Local Testing with Sample Data](#quick_start_local_sample)
* [Quick Start for Local Testing with Real Data](#quick_start_local_real)
* [Deploy to Heroku](#heroku)
* [Code Walkthrough](#code_walkthrough)
* [Testing the Source Code](#testing)
* [Contributing](#contributing)

<a name="quick_start_local_sample"></a>
# Quick Start for Local Testing with Sample Data

```bash
git clone https://github.com/sendgrid/sendgrid-go.git
cd sendgrid-go
```

Run the Inbound Parse listener in your terminal:

```bash
cd helpers/inbound/
go run inbound.go
```

In another terminal, run the test data sender:

```bash
cd [path to sendgrid-go/helpers/inbound]
go run inbound.go ./sample_data/default_data.txt http://127.0.0.1:8000/inbound
```

More sample data can be found [here](https://github.com/sendgrid/sendgrid-go/tree/master/helpers/inbound/sample_data).

View the results in the first terminal.

<a name="quick_start_local_real"></a>
# Quick Start for Local Testing with Real Data

[Setup your MX records.](https://sendgrid.com/docs/Classroom/Basics/Inbound_Parse_Webhook/setting_up_the_inbound_parse_webhook.html#-Setup) Depending on your domain name host, you may need to wait up to 48 hours for the settings to propagate.

Run the Inbound Parse listener in your terminal:

```bash
git clone https://github.com/sendgrid/sendgrid-go.git
go run inbound.go
```

In another terminal, use [ngrok](https://ngrok.com/) to allow external access to your machine:
```bash
ngrok http 8000
```

Update your SendGrid Incoming Parse settings: [Settings Page](https://app.sendgrid.com/settings/parse) | [Docs](https://sendgrid.com/docs/Classroom/Basics/Inbound_Parse_Webhook/setting_up_the_inbound_parse_webhook.html#-Pointing-to-a-Hostname-and-URL)

- For the HOSTNAME field, use the domain that you changed the MX records (e.g. inbound.yourdomain.com)
- For the URL field, use the URL generated by ngrok + /inbound, e.g http://XXXXXXX.ngrok.io/inbound

Next, send an email to [anything]@inbound.yourdomain.com, then look at the terminal where you started the Inbound Parse listener.

<a name="heroku"></a>
# Deploy to Heroku

Get a [Heroku](https://www.heroku.com) account.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy?template=https://github.com/sendgrid/sendgrid-go/tree/heroku-deployment)

[Setup your MX records.](https://sendgrid.com/docs/Classroom/Basics/Inbound_Parse_Webhook/setting_up_the_inbound_parse_webhook.html#-Setup) Depending on your domain name host, you may need to wait up to 48 hours for the settings to propagate.

Update your SendGrid Incoming Parse settings: [Settings Page](https://app.sendgrid.com/settings/parse) | [Docs](https://sendgrid.com/docs/Classroom/Basics/Inbound_Parse_Webhook/setting_up_the_inbound_parse_webhook.html#-Pointing-to-a-Hostname-and-URL)

- For the HOSTNAME field, use the domain that you changed the MX records (e.g. inbound.yourdomain.com)
- For the URL field, use the URL generated by Heroku + /inbound, e.g https://[name-of-your-app].herokuapp.com/inbound

Next, send an email to [anything]@inbound.yourdomain.com, then look at your Heroku logs: https://dashboard.heroku.com/apps/[name-of-your-app]/logs

While you are waiting for your MX records to propagate, you can test by using the test data sender:

```bash
git clone https://github.com/sendgrid/sendgrid-go.git
cd sendgrid-go
go build
./sendgrid-go ./helpers/inbound/sample_data/default_data.txt https://[name-of-your-app].herokuapp.com/inbound
```

To make changes: clone, modify and push the changes. [Heroku CLI](https://devcenter.heroku.com/articles/heroku-command-line) is required.

For example:
```bash
git clone [repo url]
git checkout heroku-deployment
heroku git:remote -a [name-of-your-app]
---make changes---
git add -A
git commit -m "updated configuration"
git push heroku heroku-deployment:master
```

<a name="code_walkthrough"></a>
# Code Walkthrough

## inbound.go

This module runs a net/http server, that by default (you can change those settings [here](https://github.com/sendgrid/sendgrid-go/blob/master/helpers/inbound/conf.json), listens for POSTs on http://localhost:8000. When the server receives the POST, it parses and prints the key/value data.

## conf.json

This file contains application environment variables (located in [conf.json](https://github.com/sendgrid/sendgrid-go/blob/master/helpers/inbound/conf.json)).

## inbound.go & /sample_data

This module, in conjunction with the sample data, is also used to send sample test data. It is useful for testing and development, particularly while you wait for your MX records to propagate.

<a name="testing"></a>
# Testing the Source Code

Tests are located in the `helpers/inbound` folder:

- [inbound_test.go](https://github.com/sendgrid/sendgrid-go/blob/master/helpers/inbound/inbound_test.go)

Learn about testing this code [here](https://github.com/sendgrid/sendgrid-go/blob/master/CONTRIBUTING.md#testing).

<a name="contributing"></a>
# Contributing

If you would like to contribute to this project, please see our [contributing guide](https://github.com/sendgrid/sendgrid-go/blob/master/CONTRIBUTING.md). Thanks!
**This helper allows you to quickly and easily build a Mail object for sending email through SendGrid.**

## Dependencies

- [rest](https://github.com/sendgrid/rest)

# Quick Start

Run the [example](https://github.com/sendgrid/sendgrid-go/tree/master/examples/helpers/mail/example.go) (make sure you have set your environment variable to include your SENDGRID_API_KEY).

```bash
go run examples/helpers/mail/example.go
```

## Usage

- See the [example](https://github.com/sendgrid/sendgrid-go/tree/master/examples/helpers/mail/example.go) for a complete working example.
- [Documentation](https://sendgrid.com/docs/API_Reference/Web_API_v3/Mail/overview.html)

## Test

```bash
go test ./... -v
```

or

```bash
cd helpers/mail
go test -v
```
You can use Docker to easily try out or test sendgrid-go.

# Quickstart
1. Install Docker and docker-compose in your machine
2. Change into the docker directory, `cd docker`
3. run `docker-compose build`
4. run `docker-compose up`
5. Put the script you want to test in `./src`
6. Run `docker-compose run mock-server`, this will open a terminal on the container
7. Run your code with `go run your-code.go` once inside container

# Examples
You can use this as an example to show how this works. 

1. Copy and save in `./src/test.go`, e.g. `test.go`.
```
package main

import (
  "os"
  "fmt"
  "github.com/sendgrid/sendgrid-go"
  "log"
)

func main() {
  apiKey := os.Getenv("SENDGRID_API_KEY")
  host := "http://localhost:4010"
  request := sendgrid.GetRequest(apiKey, "/v3/api_keys", host)
  request.Method = "GET"

  response, err := sendgrid.API(request)
  if err != nil {
    log.Println(err)
  } else {
    fmt.Println(response.StatusCode)
    fmt.Println(response.Body)
    fmt.Println(response.Headers)
  }
}
```
2. Run `docker-compose run mock-server`.
3. In container, run `go run test.go`

More sample codes on [Docker Examples](/docker/examples).


# Options
## Specifying specific versions
To use different version of sendgrid-go, mount them with `-v <host_dir>:<container_dir>` options. When you put either repository under `/mnt`, the container will automatically detect it and make the proper symlinks. You can edit these files from the host machine while the container is running.

For instance, to use sendgrid-go v3.0.6:
```
$ git clone https://github.com/sendgrid/sendgrid-go --branch v3.0.6
$ realpath sendgrid-go
/path/to/sendgrid-go
$ docker run -it -v /path/to/sendgrid-go:/mnt/sendgrid-go \
>                -v /path/to/your-code:/data \
>                dhoeric/sendgrid-go
$ (in container) go run your-code.go
```
