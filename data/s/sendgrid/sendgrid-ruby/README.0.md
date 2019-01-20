**This helper is a stand alone module to help get you started consuming and processing Inbound Parse data.**

## Table of Contents

* [Quick Start for Local Testing with Sample Data](#quick_start_local_sample)
* [Quick Start for Local Testing with Real Data](#quick_start_local_real)
* [Code Walkthrough](#code_walkthrough)
* [Contributing](#contributing)

<a name="quick_start_local_sample"></a>


# Installation

In addition to the installation instructions in
[the main readme](https://github.com/sendgrid/sendgrid-ruby/tree/master/#installation),
you must also add sinatra to your Gemfile:

```
gem 'sinatra', '>= 1.4.7', '< 3'
```


# Quick Start for Local Testing with Sample Data

```bash
git clone https://github.com/sendgrid/sendgrid-ruby.git
cd sendgrid-ruby
bundle install
```

Run the Inbound Parse listener in your terminal:

```ruby
rackup
```

In another terminal, run the test data sender:

```bash
cd [path to sendgrid-ruby]
bundle install
ruby ./lib/sendgrid/helpers/inbound/send.rb ./lib/sendgrid/helpers/inbound/sample_data/default_data.txt
```

More sample data can be found [here](https://github.com/sendgrid/sendgrid-ruby/tree/master/lib/sendgrid/helpers/inbound/sample_data).

View the results in the first terminal.

<a name="quick_start_local_real"></a>
# Quick Start for Local Testing with Real Data

[Setup your MX records.](https://sendgrid.com/docs/Classroom/Basics/Inbound_Parse_Webhook/setting_up_the_inbound_parse_webhook.html#-Setup) Depending on your domain name host, you may need to wait up to 48 hours for the settings to propagate.

Run the Inbound Parse listener in your terminal:

```bash
git clone https://github.com/sendgrid/sendgrid-ruby.git
cd sendgrid-ruby
bundle install
rackup
```

In another terminal, use [ngrok](https://ngrok.com/) to allow external access to your machine:
```bash
ngrok http 9292
```

Update your SendGrid Incoming Parse settings: [Settings Page](https://app.sendgrid.com/settings/parse) | [Docs](https://sendgrid.com/docs/Classroom/Basics/Inbound_Parse_Webhook/setting_up_the_inbound_parse_webhook.html#-Pointing-to-a-Hostname-and-URL)

- For the HOSTNAME field, use the domain that you changed the MX records (e.g. inbound.yourdomain.com)
- For the URL field, use the URL generated by ngrok + /inbound, e.g http://XXXXXXX.ngrok.io/inbound

Next, send an email to [anything]@inbound.yourdomain.com, then look at the terminal where you started the Inbound Parse listener.

<a name="code_walkthrough"></a>
# Code Walkthrough

## app.rb

This module runs a [Sinatra](http://www.sinatrarb.com/) server, that by default (you can change those settings [here](https://github.com/sendgrid/sendgrid-ruby/blob/master/sendgrid/helpers/inbound/config.yml)), listens for POSTs on http://localhost:9292. When the server receives the POST, it parses and prints the key/value data.

## config.yml

This module loads application environment variables (located in [config.yml](https://github.com/sendgrid/sendgrid-ruby/blob/master/sendgrid/helpers/inbound/config.yml)).

## send.rb & /sample_data

This module is used to send sample test data. It is useful for testing and development, particularly while you wait for your MX records to propagate.

<a name="contributing"></a>
# Contributing

If you would like to contribute to this project, please see our [contributing guide](https://github.com/sendgrid/sendgrid-ruby/blob/master/CONTRIBUTING.md). Thanks!
**This module allows you to quickly and easily build a Settings object for retrieving or updating you SendGrid Settings.**

# Quick Start

Run the [example](https://github.com/sendgrid/sendgrid-ruby/tree/master/examples/helpers/settings) (make sure you have set your environment variable to include your SENDGRID_API_KEY).

```bash
ruby examples/helpers/settings/example.rb
```

## Usage

- See the [example](https://github.com/sendgrid/sendgrid-ruby/tree/master/examples/helpers/settings) for a complete working example.
- [Documentation](https://sendgrid.com/docs/API_Reference/Web_API_v3/Settings/index.html)
**This helper allows you to quickly and easily build a Mail object for sending email through SendGrid.**

# Quick Start

Run the [example](https://github.com/sendgrid/sendgrid-ruby/tree/master/examples/helpers/mail) (make sure you have set your environment variable to include your SENDGRID_API_KEY).

```bash
ruby examples/helpers/mail/example.rb
```

## Usage

- See the [example](https://github.com/sendgrid/sendgrid-ruby/tree/master/examples/helpers/mail) for a complete working example.
- [Documentation](https://sendgrid.com/docs/API_Reference/Web_API_v3/Mail/overview.html)# Docker image for sendgrid-ruby

## Quickstart
1. [Install Docker](https://docs.docker.com/engine/installation/) on your machine.
2. Run `docker run --rm -it sendgrid/sendgrid-ruby irb`.
3. Run `require './lib/sendgrid-ruby.rb'`.

## Poke around

If you would like to just poke around in the image and check some examples:
```sh
docker run --rm -it sendgrid/sendgrid-ruby bash
```

If you want to mount your fork or specific version of the gem:
```sh
docker run --rm -v /path/to/local/sendgrid-ruby:/sources/sendgrid-ruby -it sendgrid/sendgrid-ruby bash
```

## Running tests

If you would like to run the tests present in the image:
```sh
docker run --rm sendgrid/sendgrid-ruby rake
```

If you want to run tests on your fork or a specific version, mount the codebase onto the image:
```sh
docker run --rm -v /path/to/local/sendgrid-ruby:/sources/sendgrid-ruby sendgrid/sendgrid-ruby rake
```