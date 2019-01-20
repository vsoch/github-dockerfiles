== README

WIP.

You should install `mysql` and `imagemagick` (`@6` on a mac), then run `bundle`.
# harvester
Service for harvesting resources from partners into a normalized database (for later publication)

# Environment:
set ELASTICSEARCH_URL
set the ENV variables from database.yml.

# Required Installations

You need to have `mysql`, `imagemagick@6`, and `elasticsearch` installed and *running* for this codebase to work.

You also need to install `gnparser` [from here](https://github.com/GlobalNamesArchitecture/gnparser).

# First Time

```
rake reset:full_with_all_harvests
```

## Resetting

If the migrations haven't changed, you can save a second or two and run:

```
rake reset:all_harvests
```

## Background services

`bin/delayed_job run`
