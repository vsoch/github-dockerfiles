# Fluentd

[Fluentd](http://www.fluentd.org) is an open source data collector for unified
logging layer. It allows you to unify data collection and consumption for a
better use and understanding of data.

Fluentd can accept data from applications in various formats, reformat it,
and then output or send it somewhere else for further processing.

This image installs `fluentd` from Ruby gem and also adds
[Loggly](https://www.loggly.com) support.

Here is an example configuration that accepts logs in syslog format and sends
everything to Loggly:

```
<source>
  @type syslog
  port 514
  bind 0.0.0.0
  tag system
</source>

<match system>
  type loggly
  loggly_url https://logs-01.loggly.com/inputs/TOKEN/tag/system
</match>
```

This will tag all the incoming logs with `system` tag and send them over to
Loggly with the same tag.
