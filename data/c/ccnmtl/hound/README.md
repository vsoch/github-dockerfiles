[![Build Status](https://travis-ci.org/ccnmtl/hound.svg?branch=master)](https://travis-ci.org/ccnmtl/hound)
[![Coverage Status](https://coveralls.io/repos/github/ccnmtl/hound/badge.svg?branch=master)](https://coveralls.io/github/ccnmtl/hound?branch=master)

## Hound

This is a simple service that watches a number of Graphite metrics and
sends alert emails when they cross a threshold.

It automatically backs off on failing metrics. You'll get an email
when the metric first fails, another 5 minutes later, another 30
minutes after that, one hour after that, 2 hours after that, 4 hours,
8 hours, then every 24 hours thereafter. Finally, you will get an
email when the metric has recovered.

### Docker image

There is a docker image for running hound and postfix. See
<https://github.com/ccnmtl/postfix-docker>,
<https://hub.docker.com/r/hopsoft/graphite-statsd/> and
<https://github.com/ccnmtl/hound/blob/master/Dockerfile> for more information.

### Without docker

#### Dependencies

1. Obviously enough, hound needs a running graphite server, accessible via
   network.
2. In addition, an SMTP host is necessary (without authentication or
   encryption) to send the emails out.

### Configuration

There are a couple example configs in the `examples/` directory.

* `CheckInterval` is how many minutes to wait between checks
* `GlobalThrottle` is the maximum number of alerts that Hound will send in a
  cycle. Ie, if there's a major network outage and all the metrics start
  failing, you want to stop it once you've figured that out. Once this
  threshold is passed, Hound sends just one more message saying how many
  metrics are failing.

The rest of the values in this file should be self-explanatory.

The alerts configuration is set in `config.json` (by default - it is passed as
an argument to `hound` in `run_nohup.sh`).

Each Alert has:

* `Name`: obvious.
* `Type`: defaults to 'Alert'. You can also set it to 'Notice'. The
  convention is that an alert means "something is broken and a human
  needs to fix it NOW" while a Notice is just "you should know about
  this" and it's either not directly actionable or not urgent. Eg,
  high CPU load is probably a Notice, while high request error rates
  would warrant an alert.
* `Metric`: the actual Graphite metric being checked. This can be as
  complicated as you like and use the full suite of Graphite
  functions.
* `Threshold`: fairly obvious. Format it as a float. Treat it as ">="
  or "<=". Ie, it will trigger if the metric matches the threshold.
* `Direction`: "above" or "below". Specified whether a failure is when
  the metric crosses above or below the threshold, respectively.
