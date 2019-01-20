# Auto Scaling tools
_work in progress_

Opinionated deployment tool.

## How does it work?

We've split deploys into 3 phases:
- Build
- Housekeeping
- Release

For a rails app, it could mean:
- Build = `bundle install` `assets:precompile`
- Housekeeping = `db:migrate` `db:seed`
- Release = notify workers to load new app

These steps are streamlined via `sheepit`.


## Requirements

- Docker
- Consul

