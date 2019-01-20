# TrabianBot

TrabianBot does the dirty work.

  * [PR Approval Monitor](apps/approval_monitor)

## Deployment

Deployment is handled via
[edeliver](https://github.com/boldpoker/edeliver) using
[distillery](https://github.com/bitwalker/distillery) to create the
releases.

### Build a release

To create a release, start the docker environment using
`docker-compose up` from the root directory. This will create a build
container and a staging container running ssh daemons.

#### Configure SSH for build and staging containers

edeliver requires key-based authentication into the servers, including
build and staging. The containers in this repo use an included ssh
key, which is fine in this case because these environments aren't used
outside of the build/staging process. However, edeliver doesn't
currently support a custom ssh key location, so add the following to
~/.ssh/config:

```
Host build.trabianbot
  HostName localhost
  User root
  IdentityFile [repo path]/containers/build/ssh_key
  Port 11022

Host staging.trabianbot
  HostName localhost
  User staging
  IdentityFile [repo path]/containers/staging/ssh_key
  Port 11023
```

#### Create release

To create an initial (non-upgrade) release, run:

```bash
mix edeliver build release
```

### Deploy to staging

To deploy to staging, run:

```bash
mix edeliver start
```

And verify using:

```bash
mix edeliver ping
```

If there are any issues with startup, log in to the staging server and
check `/web/trabian_bot/log/erlang.log.1`. The binary at
`/web/trabian_bot/bin/trabian_bot` can be used to run individual
distillery commands, particularly when debugging. See
https://hexdocs.pm/distillery/getting-started.html for more
information. 

For example, `/web/trabian_bot/bin/trabian_bot remote_console` will start an iex session attached to the running application.

### Deploy to production

```bash
mix edeliver deploy release to production
mix edeliver start production
mix edeliver ping production
```
