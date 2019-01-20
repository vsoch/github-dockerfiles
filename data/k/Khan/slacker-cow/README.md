# Slacker Cow :cow:
> Hubot instance for Khan Academy, Slack Edition.

## Differences from Culture Cow

Culture Cow communicated via XMPP for Hubot, but used a custom HTTP adapter
to send formatted messages (`fancyMessage`) back separately via the HipChat API.

The Slack Hubot adapter uses their realtime API, and should support formatting.

To make nicely formatted Slack messages, see the following:
- https://api.slack.com/docs/formatting
- https://api.slack.com/docs/attachments

Discussion of how to send attachments via hubot-slack:
- https://github.com/slackhq/hubot-slack/issues/170

Also, several things that were formerly in culture-cow are in separate
repositories.  For bovine culturey goodness, head over to Khan/culture-cron.
For simian deploy magic, head over to Khan/khan-sun.

## Making a deploy

### Prerequisites
You will need a working gcloud tool and a Docker environment for deploying.

- Set up the gcloud tool as [per instructions][gcloud-install]. (Note
  that on Mac you can use `brew cask install google-cloud-sdk` instead of their
  installer, if you prefer.)
- If you wish to use the shell adapter, get a working Docker environment setup:
  - On a Mac, the absolute easiest way to do this is via
    [Docker Toolbox](https://www.docker.com/toolbox), also
    available via `brew cask install dockertoolbox`, and follow their
    ["Installation Guide"](https://docs.docker.com/installation/mac/) guide if
    you are new.
  - For Linux, find [instructions for your distro](https://docs.docker.com).

[gcloud-install]: https://cloud.google.com/container-engine/docs/before-you-begin#install_the_gcloud_command_line_interface

### Development
You can run hubot as a shell instance locally, without requiring an adapter.

To make things easy, a Docker Compose configuration is provided for running
things locally.  Simply do `docker-compose run hubot` and slacker-cow will be
fired up in a local shell (compose will make sure a redis image is downloaded,
activated, and linked to the hubot container if required).

Once loaded, you can interact with it as if you were in a Slack session:

    $ docker-compose run --rm hubot
    slacker-cow> [Mon Aug 31 2015 15:47:34 GMT+0000 (UTC)] INFO hubot-redis-brain: Discovered redis from REDIS_URL environment variable

    slacker-cow> slacker-cow: ping
    slacker-cow> PONG

The docker compose configuration automatically mounts the `/hubot/bin` and
`/hubot/scripts` directories in the container as volumes, so that you can test
code modifications without rebuilding the image.

### Deploying

- Run `deploy.py`.
