Scaley is a custom autoscaling solution for Engine Yard Cloud environments.

As opposed to traditional scaling approaches that work by provisioning/terminating servers, it works by managing the state of groups of servers that already exist.

## Installation ##

***NOTE: The following is valid, but your best bet at the moment, honestly, is to [submit a support request](https://support.engineyard.com/hc/en-us/requests/new) to ask that we help you with this effort.***

For manual installation, the best bet is to grab the latest release from [the releases page](https://github.com/engineyard/scaley/releases), then place it in a location within the PATH on the server on which you want to run it.

We are working on cookbooks for both v4 and v5 of the Engine Yard stack to handle installation and configuration, and you can read more about that [here](https://github.com/engineyard/scaley/wiki/Cookbooks).

## Glossary ##

* ***Group***: A representation of an autoscaling group; made up of Scaling Servers, a Scaling Script, a Strategy, and an optional Stop Script
* ***Scaling Server***: A server that is part of the Group and is a candidate for state changes during a Scaling Event
* ***Scaling Script***: An external script that determines if the Group should be scaled up or down at any given time, reflected by its return code (1 = down, 2 = up, all else = no change)
* ***Scaling Event***: An attempt to scale the Group up or down, locking the group for all other operations until complete
* ***Stop Script***: An external script that, given the IP of a server that is about to be stopped, takes care of shutdown procedures for services on that server that are not handled gracefully during a power cut. Examples of note are things like Sidekiq workers, Resque workers, etc.
* ***Strategy***: The manner in which a Group is scaled. Both Individual and Legion are currently implemented strategies, and the default strategy is Legion.
  * ***Individual***: A Strategy that dictates that only a single Scaling Server is to be scaled during a given Scaling Event
  * ***Legion***: A Strategy that dictates that all Scaling Servers in the Group are to be scaled in the same direction during a given Scaling Event


## Configuration ##

Scaley is configured in both a global manner and in a per-group manner.

### Global Scaley Config ###

The global Scaley config lives in /etc/scaley/config.yml and provides information that is used for every Scaley run. Specifically, it requires an Engine Yard Core API token and a reporting URL (generally the `"reporting_url"` DNA value for the instance on which you run Scaley) to which it can log failures:

```yaml
token: 6876d8f76a8sd76f8f6a8s7d6f
reporting_url: "https://cloud.engineyard.com/reporting/daf7fa5dsf6ad9f9d8fa6df6"
```

Regarding the token, this should be the API token of a proper user that has access to the environment in question. That said, it is advised that a "machine user" be added to the Engine Yard account for the sole purpose of performing Scaley operations.

### Per-Group Config ###

The configuration for a given group lives in /etc/scaley/groups/groupname.yml and provides information about the group in question. Specifically, this includes the full path to its scaling script, its list of scaling servers, the desired scaling strategy, and optionally the full path to a stop script:

```yaml
scaling_script: /bin/false

strategy: legion

scaling_servers:
  - id: i-00000001
  - id: i-00000002
  - id: i-00000003
```

It's important to note here that Scaley does not provision/deprovision instances, but rather starts/stops instances that already exist. To that end, you'll need to create the instances that are added in the `scaling_servers:` list before you can really use Scaley.

## Usage ##

At present, there is only a single `scaley` command available: `scaley scale`. This command requires that one also pass the name of the group to be scaled. To automate the scaler, it's best to set up a simple cron job to periodically run `scaley scale` for the group that you wish to autoscale.

When one runs `scaley scale groupname`, the "groupname" group is scaled via the following methodology:

### Methodology ###

During each run, Scaley executes the Scaling Script associated with the Group and does the following based on the result of that run:

* If an upscale is desired, attempt to scale the group up with the group's desired strategy. Log any scaling errors as critical errors, and log a lack of capacity in the group as a warning.
* If a downscale is desired, attempt to scale the group down with the group's desired strategy (and optional stop script). Log any scaling errors as critical errors.
* If no change is desired, do not attempt to scale the group.

# History #

* v1.0.0 - First stable release
* v0.1.0 - Initial release
