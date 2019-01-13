# Run things periodically, a la cron

This image runs user-supplied commands at regular intervals, similar
to the [`cron(8)`][cron-8] utility.

Drop your executable scripts in any of the usual `/etc/cron.*/*`
directories (which are wiped off all the standard Debian stuff on
build). You should probably do so by extending this image with your
custom code / services.

## Running your code

Supported directories / schedules are:

- `/etc/cron.hourly` - Every hour at 17th minute
- `/etc/cron.daily` - Every 24 hours at 6:25 AM

<!--
TODO: not implemented
- `/etc/cron.weekly` - Every Saturday at 6:47 AM
- `/etc/cron.monthly` - Every month on the 1st day, at 6:52 AM
-->

[cron-8]: https://manpages.debian.org/jessie/cron/cron.8.en.html
