# Deploying an application with a plan

> **Difficulty**: Advanced

> **Time**: Approximately 20 minutes

In this exercise you will further explore Puppet Plans by writing a
multi-stage plan to deploy a sample application.

The sample application for this lesson consists of four nodes. It has a
single database node, two application servers, and a single load balancer in front of
them. When a new version of the application is released the following steps must be carried out:

1. Install application code on the application and database servers. `my_app::install`
1. Run migrations on the database server. `my_app::migrate`
1. For each application server:
   1. Check connections on the load balancer. `my_app::lb`
   1. Drain connections on the load balancer. `my_app::lb`
   1. Restart with the new code version. `my_app::deploy`
   1. Run a health check. `my_app_healthcheck`
   1. Add back to the load balancer. `my_app::lb`
1. Clean up the old version of the application.


# Prerequisites

For the following exercises you should have `bolt` installed and have four
Linux nodes available. The following guides will help:

1. [Acquiring Nodes](../02-acquiring-nodes)
1. [Writing tasks](../05-writing-tasks)
1. [Writing Advanced Plans](../09-writing-advanced-plans)

## Acquire nodes 

This lesson requires four nodes. If you set up nodes in [lesson 2](../02-acquiring-nodes), you need to provision an extra node.

### Provision extra nodes on Vagrant
If you set up nodes in Vagrant in lesson `02-acquiring-nodes/`, run:

```
NODES=4 vagrant up
```
> Note: Vagrantfile looks for environment variable `NODES` for number of centos nodes to provision.
> Set environmnet variable based on your shell, for example bash shell: `export NODES=4`. 

### Provision extra nodes on Docker
If you set up nodes in Docker in lesson `02-acquiring-nodes`, run:

```
docker-compose up --scale ssh=4 -d
```

When you have four nodes, update your SSH config to include them all.

## Set up inventory file
Set up an inventory file to more easily map the nodes to their role in the application. 

1. Assign one node to the load balancer (lb) group, one to the database (db) group and the other two to the application (app) group.
    ```yaml
    ---
    groups:
      - name: lb
        nodes:
          - "0.0.0.0:32771"
      - name: db
        nodes:
          - "0.0.0.0:32770"
      - name: app
        nodes:
          - "0.0.0.0:32768"
          - "0.0.0.0:32769"
    config:
      ssh:
        host-key-check: false
        # These are credentials for Docker. Manage Vagrant with SSH config.
        password: root
        user: root
    ```
    **Note**: inventory.yaml for nodes provisioned with vagrant
    ```yaml
    ---
    groups:
      - name: lb
        nodes:
          - node1
      - name: db
        nodes:
          - node2
      - name: app
        nodes:
          - node3
          - node4
    config:
      ssh:
        host-key-check: false
    ```

2. Make sure your inventory is configured correctly and you can connect to all nodes. Run:

    ```bash
    bolt command run 'echo hi' -n db,app,lb --inventoryfile ./inventory.yaml
    ```

## Write tasks for each stage of the application deployment

The tasks for this plan are code samples to enable us to focus on the plan itself.

```python
#!/usr/bin/env python
# my_app/tasks/install.py
# Install application

import json
import sys

params = json.load(sys.stdin)
json.dump(dict(status = "success", previous_version = "1.0.0", new_version = params['version']), sys.stdout)
```

```python
#!/usr/bin/env python
# my_app/tasks/migrate.py
# Migrate DB schema

import json
import sys

params = json.load(sys.stdin)
json.dump(dict(status = "success"), sys.stdout)
```

```python
#!/usr/bin/env python
# my_app/tasks/lb.py
# manipulate load_balancer

import json
import sys

from random import randint
from time import sleep

params = json.load(sys.stdin)

def stats():
    return { "connections": randint(0, 10), "status": "ok" }

def drain():
    sleep(3)
    return { "status": "success"}

def add():
    return { "status": "success" }

result_fn  = {
  "stats" : stats,
  "drain": drain,
  "add" : add,
}[params["action"]]

json.dump(result_fn(), sys.stdout)
```

```python
#!/usr/bin/env python
# my_app/tasks/deploy.py
# Update and restart the application on the new version

import json
import sys

json.dump(dict(status = "success"), sys.stdout)
```

```python
#!/usr/bin/env python
# my_app/tasks/healthcheck.py
# perform a healthcheck of a url

import json
import sys

json.dump(dict(status = "success"), sys.stdout)
```

```python
#!/usr/bin/env python
# my_app/tasks/uninstall.py
# Remove and old version of the application

import json
import sys

json.dump(dict(status = "success"), sys.stdout)
```
## Write a plan that uses the tasks

Once you have finished writing the tasks, you can add them to a plan and automate the application deployment. The
plan performs some validation, installs the application, migrates the
database, makes the new code available on each application server and, finally, cleans up old
versions of the application.

```puppet
plan my_app::deploy(
  Pattern[/\d+\.\d+\.\d+/] $version,
  TargetSpec $app_servers,
  TargetSpec $db_server,
  TargetSpec $lb_server,
  String[1] $instance = 'my_app',
  Boolean $force = false
) {
  # Validate that there is only a single load balancer server to check
  if get_targets($lb_server).length > 1 {
    fail_plan("${lb_server} did not resolve to a single target")
  }

  # First query the load balancer and make sure the app isn't under too much load to do a deploy.
  unless $force {
    $conns = run_task('my_app::lb', $lb_server,
       "Check load before starting deploy",
       action => 'stats',
       backend => $instance,
       server => 'FRONTEND',
    ).first['connections']
    if ($conns > 8) {
      fail_plan("The application has too many open connections: ${conns}")
    } else {
      # Info messages will be displayed when the --verbose flag is used.
      info("Application has ${conns} open connections.")
    }
  }

  # Install the new version of the application and check what version was previously
  # installed so it can be deleted after the deploy.
  $old_versions = run_task('my_app::install', [$app_servers, $db_server],
    "Install ${version} of the application",
    version => $version
  ).map |$r| { $r['previous_version'] }

  run_task('my_app::migrate', $db_server)

  # Don't log every action on each node, only log important messages
  without_default_logging() || {
    # Expand group references or globs before iterating
    get_targets($app_servers).each |$server| {

      # Check stats and print a message to the user
      $stats = run_task('my_app::lb', $lb_server,
        action => 'stats',
        backend => $instance,
        server => $server.name,
        _catch_errors => $force
      ).first
      notice("Deploying to ${server.name}, currently ${stats["status"]} with ${stats["connections"]} open connections.")

      run_task('my_app::lb', $lb_server,
        "Drain connections from ${server.name}",
        action => 'drain',
        backend => $instance,
        server => $server.name,
        _catch_errors => $force
      )

      run_task('my_app::deploy', [$server],
        "Update application for new version",
      )

      # Verify the app server is healthy before returning it to the load
      # balancer.
      $health = run_task('my_app::health_check', $lb_server,
        "Run Healthcheck for ${server.name}",
        target => "http://${server.name}:5000/",
        '_catch_errors' => true).first

      if $health['status'] == 'success' {
        info("Upgrade Healthy, Returning ${server.name} to load balancer")
      } else {
        # Fail the plan unless the app server is healthy or this is a forced deploy
        unless $force {
          fail_plan("Deploy failed on app server ${server.name}: ${health.result}")
        }
      }

      run_task('my_app::lb', $lb_server,
        action => 'add',
        backend => $instance,
        server => $server.name,
        _catch_errors => $force
      )
      notice("Deploy complete on ${server}.")
    }
  }

  run_task('my_app::uninstall', [$db_server, $app_servers],
    "Clean up old versions",
    live_versions => $old_versions + $version,
  )
}
```


Run this plan with the following command. It will randomly fail 10% of the
time when the simulated load is high.

```bash
bolt plan run my_app::deploy version=1.0.2 app_servers=app db_server=db lb_server=lb --inventoryfile ./inventory.yaml --modulepath=./modules
```
The result (when simulated load is below threshold)
```
Starting: Check load before starting deploy on node1
Finished: Check load before starting deploy with 0 failures in 0.89 sec
Starting: Install 1.0.2 of the application on node3, node4, node2
Finished: Install 1.0.2 of the application with 0 failures in 0.89 sec
Starting: task my_app::migrate on node2
Finished: task my_app::migrate with 0 failures in 0.85 sec
Deploying to node3, currently ok with 4 open connections.
Deploy complete on Target('node3', {"connect-timeout"=>10, "tty"=>false, "host-key-check"=>false}).
Deploying to node4, currently ok with 10 open connections.
Deploy complete on Target('node4', {"connect-timeout"=>10, "tty"=>false, "host-key-check"=>false}).
Starting: Clean up old versions on node2, node3, node4
Finished: Clean up old versions with 0 failures in 0.88 sec
Plan completed successfully with no result
```
The result (when simulated load is above threshold)
```
Starting: Check load before starting deploy on node1
Finished: Check load before starting deploy with 0 failures in 0.89 sec
{
  "kind": "bolt/plan-failure",
  "msg": "The appplication has too many open connections: 10",
  "details": {
  }
}

```
### Parameters

```puppet
plan my_app::deploy(
  Pattern[/\d+\.\d+\.\d+/] $version,
  TargetSpec $app_servers,
  TargetSpec $db_server,
  TargetSpec $lb_server,
  String[1] $instance = 'my_app',
  Boolean $force = false
)
```

- `$version` is restricted to a string matching and `x.y.z` version format
  with the Pattern Type.
- `$app_servers`, `$db_servers`, and `$lb_server`, three TargetSpec parameters
   for the different tiers of the application. The TargetSpec type any String,
   Target or Array. By using this type we allow the command line to pass node URL
   strings, group name strings or allow another plan or JSON parameters to
   pass arrays of urls or targets.
- `$instance` the name of the instance of this application in the load balancer.
- `$force` an option to ignore errors and force the deploy to complete.


### Install application

The first step in the plan is to install the new version of the code
so all application servers can serve a new version of the assets and to migrate the
database in preparation for deploying each app server.

```puppet
  $old_version = run_task('my_app::install', [$app_servers, $db_server],
    "Install ${version} of the application",
    version => $version
  ).first['previous_version']
  run_task('my_app::migrate', $db_server)
```

The `run_task` command accepts a description argument that you can use to
provide clearer log messages for the installation step. You can include the version being
installed. Use the result of the task to store the old versions of the
application for the uninstall step.

### Loop over each application server

Now the application is staged loop over each app server and update it to use
the new code.

```puppet
  # Expand group references or globs before iterating
  get_targets($app_servers).each |$server| {

    run_task('my_app::lb', $lb_server,
      "Drain connections from ${server.name}",
      action => 'drain',
      backend => $instance,
      server => $server.name,
    )

    run_task('my_app::deploy', [$server],
      "Update application for new version",
    )

    run_task('my_app::lb', $lb_server,
      action => 'add',
      backend => $instance,
      server => $server.name,
    )
    notice("Deploy complete on ${server}.")
  }
```

To loop over targets call `get_targets` to expand any groups or globs referenced
in the `$app_servers` parameter then loop over each server with `each`. For
each server drain connections from the load balancer, deploy the new version of
application and then add the server back to the load balancer.  Afterwards log
a notice message to inform the user that the deploy is complete on that server.

### Perform checks before the deploy

The plan doesn't support multiple load balancers so validate that the
TargetSpec passed for `$lb_server` resolves to only a single target and fail
the plan otherwise. In order to prevent deploys during dangerously high load
check how many open connections the app has and fail if load is too
high.

```puppet
if get_targets($lb_server).length > 1 {
  fail_plan("${lb_server} did not resolve to a single target")
}

$conns = run_task('my_app::lb', $lb_server,
   "Check load before starting deploy",
   action => 'stats',
   backend => $instance,
   server => 'FRONTEND',
).first['connections']
if ($conns > 8) {
  fail_plan("The application has too many open connections: ${conns}")
} else {
  # Info messages will be displayed when the --verbose flag is used.
  info("Application has ${conns} open connections.")
}
```

Use the `fail_plan` function to stop the plan in both cases. `fail_plan` will
stop the current plan execution and the execution of any calling plan. It
accepts a message that will be displayed to the user if the error is not
caught.

### Check server status before deploy

```puppet
# Check stats and print a message to the user
$stats = run_task('my_app::lb', $lb_server,
  action => 'stats',
  backend => $instance,
  server => $server.name,
  _catch_errors => $force
).first
notice("Deploying to ${server.name}, currently ${stats["status"]} with ${stats["connections"]} open connections.")
```

Before starting to deploy to a server call the `my_app::lb` task with the stats
action and name of the server that is about to be deployed to and save the
result the `$stats` variable. Then use those stats to print an informative
notice about which server is going to be deployed to next.

### Suppress default log messages

Bolt logs every action on each node which results in 5 messages for each node.
By default these messages are logged at the `notice` level and can make it hard
to see the more useful `notice` messages that the plan logs directly. To make the
automatic messages log at `info` instead so they won't appear on the terminal
with the `--verbose` flag the plan wraps the loop in a
`without_default_logging` block. All code executed inside a
`without_default_logging` block including in functions or subplans will log
actions at `info` instead of `notice`.

```
without_default_logging() || {
  # Expand group references or globs before iterating
  get_targets($app_servers).each |$server| {
    # Call deploy actions here
    notice("Deploy complete on ${server}.")
  }
}
```

> Note: Pay careful attention to the empty `()` and `||`. The
> `without_default_logging` block takes no parameters but empty pipes are
> required for puppet block syntax. The `()` is required to avoid parser
> ambiguity with the empty pipes.

### Catch errors for force

```puppet
run_task('my_app::lb', $lb_server,
  "Drain connections from ${server.name}",
  action => 'drain',
  backend => $instance,
  server => $server.name,
)
```
In order to prevent execution from halting after an error when the `$force`
parameter is specified we have to use the `_catch_errors` metaparam. For each
`run_task` command  that should continue when in force mode add `_catch_errors =>
true` to the parameters.

# Next steps

Congratulations! You should now have a basic understanding of `bolt` and Puppet Tasks. Here are a few ideas for what to do next:

* Explore content on the [Puppet Tasks Playground](https://github.com/puppetlabs/tasks-playground)
* Get reusable tasks and plans from the [Task Modules Repo](https://github.com/puppetlabs/task-modules)
* Search Puppet Forge for [Tasks](https://forge.puppet.com/modules?with_tasks=yes)
* Start writing Tasks for one of your existing Puppet modules
* Head over to the [Puppet Slack](https://slack.puppet.com/) and talk to the `bolt` developers and other users
* Try out the [Puppet Development Kit](https://puppet.com/download-puppet-development-kit) [(docs)](https://docs.puppet.com/pdk/latest/index.html) which has a few features to make authoring tasks even easier
# Running Commands

> **Difficulty**: Basic

> **Time**: Approximately 5 minutes

You can use Bolt to run arbitrary commands on a set of remote hosts. Let's see that in practice before we move on to more advanced features. Choose the exercise based on the operating system of your test nodes.

- [Running shell commands on Linux nodes](#running-shell-commands-on-linux-nodes)
- [Running PowerShell commands on Windows nodes](#running-powershell-commands-on-windows-nodes)

# Prerequisites
Complete the following before you start this lesson:

1. [Installing Bolt](../01-installing-bolt)
1. [Setting up test nodes](../02-acquiring-nodes)

# Running shell commands on Linux nodes

Bolt by default uses SSH for transport. If you can connect to systems remotely, you can use Bolt to run shell commands. It reuses your existing SSH configuration for authentication, which is typically provided in `~/.ssh/config`.

To run a command against a remote Linux node, use the following command syntax:
```
bolt command run <command> --nodes <nodes>
```

To run a command against a remote node using a username and password rather than keys use the following syntax:
```
bolt command run <command> --nodes <nodes> --user <user> --password <password>
```

1. Run the `uptime` command to view how long the system has been running. If you are using existing nodes on your system, replace `node1` with the address for your node.

    ```
    bolt command run uptime --nodes node1
    ```
    The result:
    ```
    Started on node1...
    Finished on node1:
      STDOUT:
         22:42:18 up 16 min,  0 users,  load average: 0.00, 0.01, 0.03
    Successful on 1 node: node1
    Ran on 1 node in 0.42 seconds

    ```

    **Tip:** If you receive the error `Host key verification failed` make sure the correct host keys are in your `known_hosts` file or pass `--no-host-key-check` to future Bolt commands. Bolt will not honor `StrictHostKeyChecking` in your SSH configuration.

2. Run the 'uptime' command on multiple nodes by passing a comma-separated list. If you are using existing nodes on your system, replace `node1,node2,node3` with addresses for your nodes. If you get an error about `Host key verification` run the rest of the examples with the `--no-host-key-check` flag to disable host key verification.

    ```
    bolt command run uptime --nodes node1,node2,node3
    ```
    The result:
    ```
    Started on node1...
    Started on node3...
    Started on node2...
    Finished on node2:
      STDOUT:
         21:03:37 up  2:06,  0 users,  load average: 0.00, 0.01, 0.03
    Finished on node3:
      STDOUT:
         21:03:37 up  2:05,  0 users,  load average: 0.08, 0.03, 0.05
    Finished on node1:
      STDOUT:
         21:03:37 up  2:07,  0 users,  load average: 0.00, 0.01, 0.05
    Successful on 3 nodes: node1,node2,node3
    Ran on 3 nodes in 0.52 seconds
    ```

3. Create an inventory file to store information about your nodes and refer to them as a group.  Later exercises will refer to the default group `all`. For more information on how to set up other named groups, see the
    [Inventory File docs](https://puppet.com/docs/bolt/latest/inventory_file.html).

    For example, if you are using the provided Vagrant configuration file, save the following to `~/.puppetlabs/bolt/inventory.yaml`:

    ```yaml
    ---
    nodes: [node1, node2, node3]
    config:
      ssh:
        host-key-check: false
    ```

# Running PowerShell commands on Windows nodes

Bolt can communicate over WinRM and execute PowerShell commands when running Windows nodes. To run a command against a remote Windows node, use the following command syntax:

```
bolt command run <command> --nodes winrm://<node> --user <user> --password <password>
```

Note the `winrm://` prefix for the node address. Also note the `--username` and `--password` flags for passing authentication information. In addition, unless you have set up SSL for WinRM communication, you must supply the `--no-ssl` flag. Otherwise running a Bolt command will result in an `unknown protocol` error.

```
bolt command run <command> --no-ssl --nodes winrm://<node>,winrm://<node> --user <user> --password <password>
```

1. Set a variable with the list of nodes.  Later exercises will refer to this variable. You can incorporate the username and password into the node address. For example, if you are using the provided Vagrant configuration file, set the following:

    ```
    WINNODE=winrm://vagrant:vagrant@localhost:55985
    ```

    On Windows, you can do the same thing with Powershell:

    ```powershell
    $WINNODE="winrm://vagrant:vagrant@localhost:55985"
    ```

2.  Run the following command to list all of the processes running on a remote machine.

    ```
    bolt command run "gps | select ProcessName" --nodes $WINNODE --no-ssl
    ```

    Use following syntax to list all of the processes running on multiple remote machines.

    ```
    bolt command run <command> --nodes winrm://<node>,winrm://<node> --user <user> --password <password>
    ```


# Next steps

Now that you know how to use Bolt to run adhoc commands you can move on to:

[Running Scripts](../04-running-scripts)
# Writing advanced Plans

> **Difficulty**: Intermediate

> **Time**: Approximately 10 minutes

In this exercise you will further explore Puppet Plans:

- [Write a plan which uses input and output](#write-a-plan-which-uses-input-and-output)
- [Write a plan with custom Ruby functions](#write-a-plan-with-custom-ruby-functions)
- [Write a plan which handles errors](#write-a-plan-which-handles-errors)

# Prerequisites
Complete the following before you start this lesson:

1. [Installing Bolt](../01-installing-bolt)
1. [Setting up test nodes](../02-acquiring-nodes)
1. [Writing plans](../07-writing-plans)

# About Bolt's Plan Language

The Bolt Plan language is built on [Puppet language functions](https://puppet.com/docs/puppet/6.0/lang_write_functions_in_puppet.html), meaning plans can make use of [Puppet's built-in functions](https://puppet.com/docs/puppet/6.0/function.html) and [data types](https://puppet.com/docs/puppet/6.0/lang_data.html). Additionally the Bolt Plan language adds [its own functions](https://puppet.com/docs/bolt/1.x/plan_functions.html) and data types (described in [Writing plans](https://puppet.com/docs/bolt/1.x/writing_plans.html)). Additionally the language can be extended with [custom functions implemented in Puppet or Ruby](https://puppet.com/docs/puppet/6.0/writing_custom_functions.html). These concepts will be demonstrated in the following examples.

# Write a plan which uses input and output

In the previous exercise you ran tasks and commands within the context of a plan. Now you will create a task that captures the return values and uses those values in subsequent steps. The ability to use the output of a task as the input to another task allows for creating much more complex and powerful plans. Real-world uses for this might include:

* A plan that uses a task to check how long since a machine was last rebooted, and then runs another task to reboot the machine on nodes that have been up for more than a week.
* A plan that uses a task to identify the operating system of a machine and then run a different task on each different operating system.

1. Create a task that prints a JSON structure with an `answer` key with a value of true or false. Save the task as `modules/exercise9/tasks/yesorno.py`.
    
    **Note:** JSON is used to structure the return value. 

    ```python
    #!/usr/bin/env python
    
    """
    This script returns a JSON string with a single key, answer which
    has a boolean value. It should flip between returning true and false
    at random
    """
    
    import json
    import random
    
    print(json.dumps({'answer': bool(random.getrandbits(1))}))
    ```

3. Create a plan and save it as `modules/exercise9/plans/yesorno.pp`:

    ```puppet
    # TargetSpec accepts a comma-separated list of nodes
    plan exercise9::yesorno (TargetSpec $nodes) {
      # Run the 'exercise9::yesorno' task on the nodes you specify.
      $results = run_task('exercise9::yesorno', $nodes)

      # Puppet uses immutable variables. That means we have to operate on data, in
      # this case a ResultSet containing a list of Results. Those are documented in
      # Bolt's docs, but effectively its a list of result data parsed from JSON
      # objects returned by the task. Select - "filter" - only the Result objects
      # where the task printed '{"answer": true}'.
      $answered_true = $results.filter |$result| { $result[answer] == true }

      # Result objects also include a reference to the target they came from. Get a
      # list of the targets that answered 'true'.
      $nodes_subset = $answered_true.map |$result| { $result.target }

      # Run the 'uptime' command on the list of targets that answered 'true'.
      run_command('uptime', $nodes_subset)
    }
    ```

    Data types used in this example: [TargetSpec](https://puppet.com/docs/bolt/1.x/writing_plans.html#targetspec), [ResultSet and Result](https://puppet.com/docs/bolt/1.x/writing_plans.html#concept-2722)
    Functions used in this example:  [run_task](https://puppet.com/docs/bolt/1.x/plan_functions.html#run-task), [filter](https://puppet.com/docs/puppet/6.0/function.html#filter), [map](https://puppet.com/docs/puppet/6.0/function.html#map), [run_command](https://puppet.com/docs/bolt/1.x/plan_functions.html#run-command)

4. Run the plan. 

    ```bash
    bolt plan run exercise9::yesorno nodes=all --modulepath ./modules
    ```
    The result:
    ```
    Starting: task exercise9::yesorno on node1, node2, node3
    Finished: task exercise9::yesorno with 0 failures in 0.97 sec
    Starting: command 'uptime' on node2, node3
    Finished: command 'uptime' with 0 failures in 0.39 sec
    Plan completed successfully with no result
    ```
    **Note:** Running the plan multiple times results in different output. As the return value of the task is random, the command runs on a different subset of nodes each time.

# Write a plan with custom Ruby functions

Bolt supports a powerful extension mechanism via Puppet functions. These are functions written in Puppet or Ruby that are accessible from within plans, and are in fact how many Bolt features are implemented. You can declare Puppet functions within a module and use them in your plans. Many existing Puppet functions, such as `length` from [puppetlabs-stdlib], can be used in plans. 

1. Save the following as `modules/exercise9/plans/count_volumes.pp`:

    ```puppet
    plan exercise9::count_volumes (TargetSpec $nodes) {
      $result = run_command('df', $nodes)
      return $result.map |$r| {
        $line_count = $r['stdout'].split("\n").length - 1
        "${$r.target.name} has ${$line_count} volumes"
      }
    }
    ```

2. To use the `length` function, which accepts a `String` type so it can be invoked directly on a string, install it locally:

    ```bash
    git clone https://github.com/puppetlabs/puppetlabs-stdlib ./modules/stdlib
    ```

3. Run the plan.

    ```bash
    bolt plan run exercise9::count_volumes nodes=all --modulepath ./modules
    ```
    The result:
    ```
    Starting: command 'df' on node1, node2, node3
    Finished: command 'df' with 0 failures in 0.5 sec
    [
      "node1 has 7 volumes",
      "node2 has 7 volumes",
      "node3 has 7 volumes"
    ]
    ```

4. Write a function to list the unique volumes across your nodes and save the function as `modules/exercise9/lib/puppet/functions/unique.rb`. A helpful function for this would be `unique`, but [puppetlabs-stdlib] includes a Puppet 3-compatible version that can't be used. Not all Puppet functions can be used with Bolt.

    ```ruby
    Puppet::Functions.create_function(:unique) do
      dispatch :unique do
        param 'Array[Data]', :vals
      end
    
      def unique(vals)
        vals.uniq
      end
    end
    ```

5. Write a plan that collects the last column of each line output by `df` (except the header), and prints a list of unique mount points. Save the plan as `modules/exercise9/plans/unique_volumes.pp`.

    ```puppet
    plan exercise9::unique_volumes (TargetSpec $nodes) {
      $result = run_command('df', $nodes)
      $volumes = $result.reduce([]) |$arr, $r| {
        $lines = $r['stdout'].split("\n")[1,-1]
        $volumes = $lines.map |$line| {
          $line.split(' ')[-1]
        }
        $arr + $volumes
      }
    
      return $volumes.unique
    }
    ```
7. Run the plan. 

    ```bash
    bolt plan run exercise9::unique_volumes nodes=all --modulepath ./modules
    ```
    The result:
    ```
    Starting: command 'df' on node1, node2, node3
    Finished: command 'df' with 0 failures in 0.53 sec
    [
      "/",
      "/dev",
      "/dev/shm",
      "/run",
      "/sys/fs/cgroup",
      "/boot",
      "/run/user/1000"
    ]
    ```

For more information on writing custom functions, see [Puppet's custom function docs](https://puppet.com/docs/puppet/5.5/functions_basics.html).  

# Write a plan which handles errors

By default, any task or command that fails causes a plan to abort immediately. You must add error handling to a plan to prevent it from stopping this way. 

1. Save the following plan as `modules/exercise9/plans/error.pp`. This plan runs a command that fails (`false`) and collects the result. It then uses the `ok` function to check if the command succeeded on every node, and prints a message based on that.

    ```puppet
    plan exercise9::error (TargetSpec $nodes) {
      $results = run_command('false', $nodes)
      if $results.ok {
        notice("The command succeeded")
      } else {
        notice("The command failed")
      }
    }
    ```


2. Run the plan. 

    ```bash
    bolt plan run exercise9::error nodes=all --modulepath ./modules
    ```
    The result:
    ```
    Starting: command 'false' on node1, node2, node3
    Finished: command 'false' with 3 failures in 0.53 sec
    {
      "kind": "bolt/run-failure",
      "msg": "Plan aborted: run_command 'false' failed on 3 nodes",
      "details": {
        "action": "run_command",
        "object": "false",
        "result_set": [...]
      }
    }
    ```

    Because the plan stopped executing immediately after the `run_command()` failed, no message was returned.

3. Save the following new plan as `modules/exercise9/plans/catch_error.pp`. To prevent the plan from stopping immediately on error it passes `_catch_errors => true` to `run_command`. This returns a `ResultSet` like normal, even if the command fails.
    
    ```puppet
    plan exercise9::catch_error (TargetSpec $nodes) {
      $results = run_command('false', $nodes, _catch_errors => true)
      if $results.ok {
        notice("The command succeeded")
      } else {
        notice("The command failed")
      }
    }
    ```

2. Run the plan and execute the `notice` statement.

    ```bash
    bolt plan run exercise9::catch_error nodes=all --modulepath ./modules
    ```
    The result:
    ```
    Starting: command 'false' on node1, node2, node3
    Finished: command 'false' with 3 failures in 0.47 sec
    The command failed
    Plan completed successfully with no result
    ```

**Tip:** You can pass the  `_catch_errors` to `run_command`, `run_task`, `run_script`, and `file_upload`.

# Next steps
Now that you have learned about writing advanced plans you can deploy an app with bolt! 

[Deploying and Application](../10-deploying-an-application)


[puppetlabs-stdlib]: https://github.com/puppetlabs/puppetlabs-stdlib
# Applying Manifest Code With Bolt

> **Difficulty**: Advanced

> **Time**: Approximately 20 minutes

In this exercise you will further explore Puppet Plans by using the `apply` keyword to leverage existing content from the [Puppet Forge](https://forge.puppet.com/).

You can read more about using bolt `apply` in Masterless Workflows in a [Blog Post](https://puppet.com/blog/introducing-masterless-puppet-bolt) written by Bolt developer Michael Smith. 

You will deploy two web servers and a load balancer to distribute the traffic evenly between them with the following steps:
1. Build a project specific configuration using a `Boltdir`.
1. Download useful module content from the Puppet forge. 
1. Write a Puppet Class to abstract the configuration of an Nginx web server. 
1. Write a Bolt Plan to `apply` puppet code and orchestrate the deployment of a static website. 

# Prerequisites

For the following exercises you should have `bolt` Docker and docker-compose installed. The following guides will help:

1. [Acquiring Nodes](../02-acquiring-nodes)
1. [Writing Advanced Plans](../09-writing-advanced-plans)

# Aquire nodes

This lesson requires three nodes. You can use the [docker-compose.yml](./docker-compose.yml) file in this repository to provision the nodes necessary for this exercise. 

Nodes can be obtained with the `docker-compose up -d` command.

You can verify nodes are created with `docker ps`
```
8b7f33d8fde4        lab_node            "/usr/sbin/sshd -D"   About an hour ago   Up About an hour    0.0.0.0:20023->22/tcp                          11applymanifestcode_server_1_1
90f6abe8dfc8        lab_node            "/usr/sbin/sshd -D"   About an hour ago   Up About an hour    0.0.0.0:20024->22/tcp                          11applymanifestcode_server_2_1
26c47f8c4bad        lab_node            "/usr/sbin/sshd -D"   About an hour ago   Up About an hour    0.0.0.0:20022->22/tcp, 0.0.0.0:20080->80/tcp   lb
```

# Build a Boltdir

By default `$HOME/.puppetlabs/bolt/` is the base directory for user-supplied data such as the configuration and inventory files. It is effectively the default `Boltdir`. 
You may find it useful to maintain a project specific `Boltdir`. When you commit a `Boltdir` to a project you can share Bolt configuration and code between users.

Bolt will search for a `Boltdir` in parent directories of the directory from which it was run.

## Inventory

Build an inventory to organize provisioned nodes. This will be the first configuration file in our new project specific `Boltdir`. 

**Note**: Example outputs in the lab are for nodes provisioned with Docker. 

### Docker nodes
If you provisioned your nodes with the docker-compose file provided with this exercise save the following in `Boltdir/inventory.yaml`.
```yaml
---
groups:
  - name: lb
    nodes:
      - name: "0.0.0.0:20022"
  - name: servers
    nodes:
      - name: "127.0.0.1"
        config:
          ssh:
            port: 20023
      - name: "localhost"
        config:
          ssh:
            port: 20024
config:
  ssh:
    host-key-check: false
    password: root
    user: root
```
Make sure your inventory is configured correctly and you can connect to all nodes. Run from within the project Boltdir:

```bash
bolt command run 'echo hi' -n all
```
Expected output
```
Started on 0.0.0.0...
Started on localhost...
Started on 127.0.0.1...
Finished on localhost:
  STDOUT:
    hi
Finished on 0.0.0.0:
  STDOUT:
    hi
Finished on 127.0.0.1:
  STDOUT:
    hi
Successful on 3 nodes: 0.0.0.0:20022,127.0.0.1,localhost
Ran on 3 nodes in 0.20 seconds

```

## Module Content

In order to install module content from the forge Bolt uses a `Puppetfile`. See [Puppetfile Documentation](https://puppet.com/docs/pe/latest/puppetfile.html) for more information. 

Save the following `Puppetfile` that describes the Puppet Forge content to be installed in the project `Boltdir`. 

```
forge 'http://forge.puppetlabs.com'
mod 'puppetlabs-stdlib', '4.25.1'
mod 'puppetlabs-concat', '4.2.1'
mod 'puppetlabs-haproxy', '2.1.0'
```

From within the `Boltdir` install the Forge content with the following Bolt command:
```
bolt puppetfile install
```
Confirm that a `modules` directory has been created in the project `Boltdir`. 

## Write profile module

Now that you have downloaded existing modules it is time to write your own module content. Custom module content not managed by the project `Puppetfile` belongs in a `site` directory in the `Boltdir`. After creating a `Boltdir/site` directory create a new directory called `profiles`. The `profiles` module will be our own custom module. 

Start by abstracting the Nginx setup by writing a Puppet Class. Puppet code belongs in a subdirectory of our module called `manifests`. Save the following class definition in `Boltdir/site/profiles/manifests/server.pp`. 

If you are new to Puppet writing puppet code check out [these learning resources](https://learn.puppet.com/). The Learning VM is especially helpful for getting up to speed with Puppet.
```puppet
class profiles::server(String $site_content) {
  if($facts['os']['family'] == 'redhat') {
    package { 'epel-release':
      ensure => present,
      before => Package['nginx'],
    }
    $html_dir = '/usr/share/nginx/html'
  } else {
    $html_dir = '/var/www/html'
  }

  package { 'nginx':
    ensure => present,
  }

  file { "${html_dir}/index.html":
    content => $site_content,
    ensure  => file,
  }

  service { 'nginx':
    ensure  => 'running',
    enable  => 'true',
    require => Package['nginx'],
  }
}
```
**Note**: Vox Pupuli maintains an [nginx module](https://forge.puppet.com/puppet/nginx/readme) that you could swap in for our simple server class to manage more complex nginx configuration.

Now we will write a Plan to utilize the server class. 

As we have seen in the lab, plan code belongs in the `plans` subdirectory. Save the following to `Boltdir/site/profiles/plans/nginx_install.pp`.

Take note of the following features of the plan:

1. This plan has three parameters, the server nodes, the load balancer nodes and a string to be statically served by our load balanced Nginx servers. 
1. Notice the `apply_prep` function call. `apply_prep` is used to install packages needed by apply on remote nodes as well as to gather facts about the nodes.
1. The first apply block configures the Nginx servers. The site content is defined by default to be "Hello from [node name]" where node name is a fact gathered by `apply_prep`. The `site_content` parameter can be configured in the bolt plan invocation. 
1. The second apply block uses information about the Nginx servers to configure a load balancer to direct traffic between the two servers. 
```puppet
plan profiles::nginx_install(
  TargetSpec $servers,
  TargetSpec $lb,
  String $site_content = 'hello!',
) {
  if get_targets($lb).size != 1 {
    fail("Must specify a single load balancer, not ${lb}")
  }
  # Ensure puppet tools are installed and gather facts for the apply
  apply_prep([$servers, $lb])

  apply($servers) {
    class { 'profiles::server':
      site_content => "${site_content} from ${$trusted['certname']}",
    }
  }

  apply($lb) {
    include haproxy
    haproxy::listen { 'nginx':
      collect_exported => false,
      ipaddress        => $facts['ipaddress'],
      ports            => '80',
    }

    $targets = get_targets($servers)
    $targets.each |$target| {
      haproxy::balancermember { $target.name:
        listening_service => 'nginx',
        server_names      => $target.host,
        ipaddresses       => $target.facts['ipaddress'],
        ports             => '80',
        options           => 'check',
      }
    }
  }
}
```

Verify the `nginx_install` plan is available to run using `bolt plan show`. You should see an output similar to: 
```
aggregate::count
aggregate::nodes
canary
facts
facts::info
profiles::nginx_install
puppetdb_fact
```

Now you are ready to execute the plan. 

`bolt plan run profiles::nginx_install servers=servers lb=lb`

Expected output
```
Starting: plan profiles::nginx_install
Starting: install puppet and gather facts on 127.0.0.1, localhost, 0.0.0.0:20022
Finished: install puppet and gather facts with 0 failures in 3.84 sec
Starting: apply catalog on 127.0.0.1, localhost
Finished: apply catalog with 0 failures in 6.72 sec
Starting: apply catalog on 0.0.0.0:20022
0.0.0.0:20022: Scope(Haproxy::Config[haproxy]): haproxy: The $merge_options parameter will default to true in the next major release. Please review the documentation regarding the implications.
Finished: apply catalog with 0 failures in 10.85 sec
Finished: plan profiles::nginx_install in 21.42 sec
Plan completed successfully with no result
```

In order to verify the deployment is operating as expected use the following `curl` commands to see the load balancer delegating to the different web servers.

command: `curl http://0.0.0.0:20080/`

We expect the result to vary between based on the load balancer
```
hello! from localhost
```
and 
```
hello! from 127.0.0.1
```
**Note**: You can also navigate to `http://0.0.0.0:20080/` in a web browser. Just be aware that your browser will likely cache the result and therefore you may not see the oscillation between the two servers behind the load balancer. 

# Next steps

Now that you have learned about applying existing module content you can harness the power of the Puppet forge to manage infrastructure and deploy great applications!
# Running Existing Tasks

> **Difficulty**: Intermediate

> **Time**: Approximately 10 minutes

In this exercise you will explore existing tasks, including several tasks that take advantage of Puppet under-the-hood.

- [Install Puppet using Bolt](#install-puppet-using-bolt)
- [The Tasks Playground](#more-tips-tricks-and-ideas-on-the-tasks-playground)

# Prerequisites
Complete the following before you start this lesson:

1. [Installing Bolt](../01-installing-bolt)
1. [Setting up test nodes](../02-acquiring-nodes)
1. [Running Commands](../03-running-commands)
1. [Running Scripts](../04-running-scripts)

# Inspect installed tasks

Bolt is packaged with useful modules and task content.

- Run the 'bolt task show' command to view a list of the tasks installed in the previous exercise.

    ```
    bolt task show
    ```
    The result:
    ```    
    facts                              Gather system facts
    facts::bash                        Gather system facts using bash
    facts::powershell                  Gather system facts using powershell
    facts::ruby                        Gather system facts using ruby and facter
    package                            Manage and inspect the state of packages
    puppet_agent::install              Install the Puppet agent package
    puppet_agent::install_powershell
    puppet_agent::install_shell
    puppet_agent::version              Get the version of the Puppet agent package installed. Returns nothing if none present.
    puppet_agent::version_powershell
    puppet_agent::version_shell
    puppet_conf                        Inspect puppet agent configuration settings
    service                            Manage and inspect the state of services
    service::linux                     Manage the state of services (without a puppet agent)
    service::windows                   Manage the state of Windows services (without a puppet agent)

    Use bolt task show <task-name> to view details and parameters for a specific task.
    ```

# Use the puppet_agent module to install puppet agent. 

Install puppet agent with the install_agent task

``` 
bolt task run puppet_agent::install -n all --run-as root
```
   
The result:
```
  Installed:
  puppet-agent.x86_64 0:6.0.1-1.el7                                             
  
  Complete!
  Loaded plugins: fastestmirror
  Loading mirror speeds from cached hostfile
   * base: mirror.tocici.com
   * extras: mirror.tocici.com
   * updates: ftp.osuosl.org
  No packages marked for update
  {
  }
 Successful on 3 nodes: node1,node2,node3
 Ran on 3 nodes in 68.71 seconds
```

# View and use parameters for a specific task

1. Run `bolt task show package` to view the parameters that the package task uses. 

    ```
    bolt task show package
    ```
    The result:
    ```    
    package - Manage and inspect the state of packages

    USAGE:
    bolt task run --nodes <node-name> package action=<value> name=<value> version=<value> provider=<value>

    PARAMETERS:
    - action: Enum[install, status, uninstall, upgrade]
        The operation (install, status, uninstall and upgrade) to perform on the package
    - name: String[1]
        The name of the package to be manipulated
    - version: Optional[String[1]]
        Version numbers must match the full version to install, including release if the provider uses a release moniker. Ranges or semver patterns are not accepted except for the gem package provider. For example, to install the bash package from the rpm bash-4.1.2-29.el6.x86_64.rpm, use the string '4.1.2-29.el6'.
    - provider: Optional[String[1]]
        The provider to use to manage or inspect the package, defaults to the system package manager

    MODULE:
    built-in module
    ```

2.  Using parameters for the package task, check on the status of the bash package:

    ```
    bolt task run package action=status name=bash --nodes node1
    ```
    The result:
    ```    
    Started on node1...
    Finished on node1:
      {
        "status": "up to date",
        "version": "4.2.46-30.el7"
      }
    Successful on 1 node: node1
    Ran on 1 node in 3.84 seconds
    ```
3.  Using parameters for the package task, install the vim package across all your nodes:

    ```
    bolt task run package action=install name=vim --nodes all --run-as root
    ```
    The result:
    ```
    Started on node1...
    Started on node3...
    Started on node2...
    Finished on node1:
      {
        "status": "present",
        "version": "2:7.4.160-4.el7"
      }
    Finished on node3:
      {
        "status": "installed",
        "version": "2:7.4.160-4.el7"
      }
    Finished on node2:
      {
        "status": "installed",
        "version": "2:7.4.160-4.el7"
      }
    Successful on 3 nodes: node1,node2,node3
    Ran on 3 nodes in 10.03 seconds
    ```

# More tips, tricks and ideas on the Tasks Playground

See the [installing modules](https://puppet.com/docs/bolt/latest/bolt_installing_modules.html) documentation to learn how to install external modules. 
These exercises introduce you to Puppet tasks. You'll find lots more tips, tricks, examples and hacks on the [Puppet Tasks Playground](https://github.com/puppetlabs/tasks-playground).

# Next steps

Now that you know how to run existing tasks with Bolt you can move on to:

[Writing Plans](../07-writing-plans)
# Running Scripts

> **Difficulty**: Basic

> **Time**: Approximately 5 minutes

In this exercise you will run existing scripts against remote nodes using Bolt.

- [Test Linux nodes for ShellShock](#test-linux-nodes-for-shellshock)
- [Test Windows external connectivity](#test-windows-external-connectivity)

# Prerequisites
Complete the following before you start this lesson:

1. [Installing Bolt](../01-installing-bolt)
1. [Setting up test nodes](../02-acquiring-nodes)
1. [Running Commands](../03-running-commands)

# Test Linux nodes for ShellShock
Run the [bashcheck](https://github.com/hannob/bashcheck) script to check on ShellShock and related vulnerabilities.

**Tip:** You likely already have a set of scripts that you run to accomplish common systems administration tasks. Bolt makes it easy to reuse your scripts without modification and to run them quickly across a large number of nodes. Feel free to replace the bashcheck script in this exercise with one of your own. Just set the shebang line correctly and you can run scripts in Python, Ruby, Perl or another scripting language.


1. Download `bashcheck` using `curl`, 'wget',  or similar:

    ```
    curl -O https://raw.githubusercontent.com/hannob/bashcheck/master/bashcheck
    ```

2. Run the script using the command `bolt script run <script-name> <script options>`. This uploads the script to the nodes you have specified. 

    ```
    bolt script run bashcheck --nodes node1
    ```
    The result:
    ```    
    Started on node1...
    Finished on node1:
      STDOUT:
        Testing /usr/bin/bash ...
        Bash version 4.2.46(2)-release
        
        Variable function parser pre/suffixed [(), redhat], bugs not exploitable
        Not vulnerable to CVE-2014-6271 (original shellshock)
        Not vulnerable to CVE-2014-7169 (taviso bug)
        Not vulnerable to CVE-2014-7186 (redir_stack bug)
        Test for CVE-2014-7187 not reliable without address sanitizer
        Not vulnerable to CVE-2014-6277 (lcamtuf bug #1)
        Not vulnerable to CVE-2014-6278 (lcamtuf bug #2)
    Successful on 1 node: node1
    Ran on 1 node in 0.89 seconds
    ```



# Test Windows external connectivity
Create a simple PowerShell script to test connectivity to a known website.

**Tip:** You likely already have a set of scripts that you run to accomplish common systems administration tasks. Bolt makes it easy to reuse your scripts without modification and to run them quickly across a large number of nodes. Feel free to replace the script in this exercise with one of your own.

1. Save the following as `testconnection.ps1`:

    ```powershell
    Test-Connection -ComputerName "example.com" -Count 3 -Delay 2 -TTL 255 -BufferSize 256 -ThrottleLimit 32
    ```

2. Run the script using the command `bolt script run <script-name> <script options>`. This uploads the script to the nodes you have specified, ensures its executable, runs it, and returns output to the console.

    ```
    bolt script run testconnection.ps1 -n $WINNODE --no-ssl
    ```
    The result:
    ```    
    Started on localhost...
    Finished on localhost:
      STDOUT:
        
        Source        Destination     IPV4Address      IPV6Address                              Bytes    Time(ms) 
        ------        -----------     -----------      -----------                              -----    -------- 
        Nano          example.com                                                               256      4        
        Nano          example.com                                                               256      4        
        Nano          example.com                                                               256      5        
        
        
    Successful on 1 node: winrm://vagrant:vagrant@localhost:55985
    Ran on 1 node in 8.55 seconds
    ```

# Next steps

Now that you know how to use Bolt to run existing scripts you can move on to:

[Writing Tasks](../05-writing-tasks)
# Setting up test nodes to use with Bolt

> **Difficulty**: Basic

> **Time**: Approximately 5 minutes

In this exercise you will create nodes that you can use to experiment with Bolt. You can also use existing nodes in your system if you prefer. 

- [Existing nodes](#existing-nodes)
- [Using Vagrant](#using-vagrant)
- [Using Docker](#using-docker)

# Prerequisites
To use an attached configuration file to set up test nodes, you must have one of the following installed on your machine: 

- [Vagrant](https://www.vagrantup.com/) 
- [Docker for Mac](https://www.docker.com/docker-mac) 
- [Docker for Windows](https://www.docker.com/docker-windows) 

# Existing nodes

If you already have, or can easily launch, a few Linux or Windows nodes then you're all set. These nodes must be accessible via SSH or WinRM; if you can  access them via an SSH or WinRM client then Bolt can, too.

# Using Vagrant
**Note:** These instructions assume that you are familiar with Vagrant and have a suitable hypervisor configured.

The attached Vagrantfile configures three CentOS 7 nodes and a Windows (Nano Server) node.



1. Save the following code as `Vagrantfile` or download the `Vagrantfile` attached to this exercise. To configure a different number of nodes, change the `NODES` environment variable.


    ```ruby
    nodes_count = 3
    ```
    The result:
    ```        
    if ENV['NODES'].to_i > 0 && ENV['NODES']
      $nodes_count = ENV['NODES'].to_i
    end
    
    Vagrant.configure('2') do |config|
      config.vm.box = 'centos/7'
      config.ssh.forward_agent = true
      config.vm.network "private_network", type: "dhcp"
    
      (1..$nodes_count).each do |i|
        config.vm.define "node#{i}"
      end
    
      config.vm.define :windows do |windows|
        windows.vm.box = "mwrock/WindowsNano"
        windows.vm.guest = :windows
        windows.vm.communicator = "winrm"
      end
    end
    ```
2. From the command line, ensure you’re in the directory where you stored the Vagrantfile file and enter `vagrant up`.

3. Generate the SSH configuration so Bolt knows how to authenticate with the SSH daemon. The following command will output the required details.

    ```
    vagrant ssh-config
    ```
    
    You can save that so it will be automatically picked up by most SSH clients, including Bolt. This uses the ability to specify hosts along with their connection details in a [configuration file](https://linux.die.net/man/5/ssh_config).
    
    ```
    mkdir ~/.ssh
    vagrant ssh-config | sed /StrictHostKeyChecking/d | sed /UserKnownHostsFile/d >> ~/.ssh/config
    ```
    
    By saving this SSH configuration file, you can use the node name, rather than the IP address. When passing nodes to Bolt in the following exercises with Linux you will use `--nodes node1,node2`.

4. Make sure you can SSH into all of your nodes. If you've used the vagrant nodes before you may have to remove entries from `~/.ssh/known_hosts`.

    ```
    ssh node1
    ssh node2
    ssh node3
    ```


# Using Docker
Using Docker we can quickly launch a number of ephemeral SSH servers. To make that even easier we'll use Docker Compose. 

1. Save the following code as `docker-compose.yml` or download the `docker-compose.yml` file attached to this exercise.

    ```yaml
    version: '3'
    services:
      ssh:
        build: .
        ports:
          - 22
    ```
2. Save the following code as `Dockerfile` or download the `Dockerfile` attached to this exercise.
    ```
    FROM rastasheep/ubuntu-sshd:16.04
    RUN ln -s /usr/bin/python3 /usr/bin/python
    ```

2. Launch a single SSH server in the background: `docker-compose up -d`. To launch more SSH servers, run:  `docker-compose up --scale ssh=3 -d`.

3. View a list of running containers: `docker-compose ps`. The result should be similar to:  
    ```
            Name                 Command        State           Ports
    -------------------------------------------------------------------------
    2acquiringnodes_ssh_1   /usr/sbin/sshd -D   Up      0.0.0.0:32768->22/tcp
    2acquiringnodes_ssh_2   /usr/sbin/sshd -D   Up      0.0.0.0:32769->22/tcp
    ```
    
    Note the `Ports` column. We are forwarding a local port to the SSH server running in the container. Using the example above, you can SSH to `127.0.0.1:32768`.
    
4. If you have a local SSH client, test the connection. Change the port to one you get from running the `docker-compose ps` command. The image sets the username and password to `root`. 
    
    ```
    ssh root@127.0.0.1 -p 32768
    ```

5. Make sure you can log into all the nodes before moving on. You may have to remove some entries from `~/.ssh/known_hosts` 

    When passing nodes to Bolt in the next section you will use `--nodes 127.0.0.1:32768,127.0.0.1:32769`, replacing the ports with those you see when you run the `docker-compose ps` command.

# Next steps

Now that you have set up test nodes to use with Bolt you can move on to:

[Running Commands](../03-running-commands)
# Writing Plans

> **Difficulty**: Intermediate

> **Time**: Approximately 10 minutes

In this exercise you will discover Puppet Plans and how to run them with Bolt. 

- [Write a plan using run_command](#write-a-plan-using-run_command)
- [Write a plan using run_task](#write-a-plan-using-run_task)

# Prerequisites
Complete the following before you start this lesson:

1. [Installing Bolt](../01-installing-bolt)
1. [Setting up test nodes](../02-acquiring-nodes)
1. [Running Commands](../03-running-commands)

# About Plans 

Use plans when you want to run several commands together across multiple nodes. For instance to remove a node from a load balancer before you deploy the new version of the application, or to clear a cache after you re-index a search engine.

You can link a set of commands, scripts, and tasks together, and add parameters to them so they are easy to reuse. While you write plans in the Puppet language, you don't need to install Puppet to use them.


# Write a plan using run_command

Create a simple plan that runs a command on a list of nodes.

1. Save the following as `modules/exercise7/plans/command.pp`:

    ```puppet
    plan exercise7::command (TargetSpec $nodes) {
      run_command("uptime", $nodes)
    }
    ```

2. Run the plan:

    ```
    bolt plan run exercise7::command nodes=node1 --modulepath ./modules
    ```
    The result:
    ```    
    Starting: command 'uptime' on node1
    Finished: command 'uptime' with 0 failures in 0.45 sec
    Plan completed successfully with no result

    ```

    **Note:**

    * `nodes` is passed as an argument like any other, rather than a flag. This makes plans flexible when it comes to taking lists of different types of nodes or generating the list of nodes in code within the plan.

    * Use the `TargetSpec` type to denote nodes; it allows passing a single string describing a target URI or a comma-separated list of strings as supported by the `--nodes` argument to other commands. It also accepts an array of Targets, as resolved by calling the [`get_targets` method](https://puppet.com/docs/bolt/latest/writing_plans.html#calling-basic-plan-functions). You can iterate over Targets without needing to do your own string splitting, or as resolved from a group in an [inventory file](https://puppet.com/docs/bolt/latest/inventory_file.html).


# Write a plan using run_task
Create a task and then create a plan that uses the task.

1. Save the following task as `modules/exercise7/tasks/write.sh`. The task accepts a filename and some content and saves a file to `/tmp`.
    
    ```bash
    #!/bin/sh
    
    if [ -z "$PT_message" ]; then
      echo "Need to pass a message"
      exit 1
    fi
    
    if [ -z "$PT_filename" ]; then
      echo "Need to pass a filename"
      exit 1
    fi
    
    echo $PT_message > "/tmp/${PT_filename}"
    ```

2. Run the task directly with the following command:

    ```
    bolt task run exercise7::write filename=hello message=world --nodes=node1 --modulepath ./modules --debug
    ```
    
    **Note:** In this case the task doesn't output anything to stdout. It can be useful to trace the running of the task, and for that the `--debug` flag is useful. Here is the output when run with debug:
    
    ```
    Did not find config for node1 in inventory
    Started with 100 max thread(s)
    ModuleLoader: module 'boltlib' has unknown dependencies - it will have all other modules visible
    Did not find config for node1 in inventory
    Starting: task exercise7::write on node1
    Authentication method 'gssapi-with-mic' is not available
    Running task exercise7::write with '{"filename"=>"hello", "message"=>"world"}' via  on ["node1"]
    Started on node1...
    Running task run 'Task({'name' => 'exercise7::write', 'implementations' => [{'name' => 'write.sh', 'path' => '/Users/username/puppetlabs/tasks-hands-on-lab/07-writing-plans/modules/exercise7/tasks/write.sh', 'requirements' => []}], 'input_method' => undef})' on node1
    Opened session
    Executing: mktemp -d
    stdout: /tmp/tmp.mJo9THENdL

    Command returned successfully
    Executing: chmod u\+x /tmp/tmp.mJo9THENdL/write.sh
    Command returned successfully
    Executing: PT_filename=hello PT_message=world /tmp/tmp.mJo9THENdL/write.sh
    Command returned successfully
    Executing: rm -rf /tmp/tmp.mJo9THENdL
    Command returned successfully
    Closed session
    Finished on node1:
     {"node":"node1","status":"success","result":{"_output":""}}

      {
      }
    Finished: task exercise7::write with 0 failures in 0.89 sec
    Successful on 1 node: node1
    Ran on 1 node in 0.97 seconds
    ```
3. Write a plan that uses the task you created. Save the following as `modules/exercise7/plans/writeread.pp`:

    ```puppet
    plan exercise7::writeread (
      TargetSpec $nodes,
      String     $filename,
      String     $message = 'Hello',
    ) {
      run_task(
        'exercise7::write',
        $nodes,
        filename => $filename,
        message  => $message,
      )
      run_command("cat /tmp/${filename}", $nodes)
    }
    ```

    **Note:**
    
    * The plan takes three arguments, one of which (`message`) has a default value. We'll see shortly how Bolt uses that to validate user input.
    * First you run the `exercise7::write` task from above, setting the arguments for the task to the values passed to the plan. This writes out a file in the `/tmp` directory.
    * Then you run a command directly from the plan, in this case to output the content written to the file in the above task.

4. Run the plan using the following command:
    
    ```
    bolt plan run exercise7::writeread filename=hello message=world nodes=node1 --modulepath ./modules
    ```
    The result:
    ```
    Starting: task exercise7::write on node1
    Finished: task exercise7::write with 0 failures in 0.88 sec
    Starting: command 'cat /tmp/hello' on node1
    Finished: command 'cat /tmp/hello' with 0 failures in 0.41 sec
    Plan completed successfully with no result
    ```

    **Note:**
    
    * `message` is optional. If it's not passed it uses the default value from the plan.
    * When running multiple steps in a plan only the last step will generate output.


# Next steps

Now that you know how to create and run basic plans with Bolt you can move on to:

[Writing advanced Tasks](../08-writing-advanced-tasks)
# Installing Bolt

> **Difficulty**: Basic

> **Time**: Approximately 10 minutes

In this exercise you will install Bolt so you can get started with Puppet Tasks.

# Installation Details

Bolt is packaged for the major operating systems. Please refer to the [installation documentation](https://puppet.com/docs/bolt/latest/bolt_installing.html) to install Bolt for the OS you are using. 

**Note** For this lab and for most use cases it is recommended that bolt is NOT installed as a Ruby Gem. This is because optional (but highly useful) supporting modules are only included in packages and must be installed manually when using the Gem.    

# Next steps

Now that you have Bolt installed you can move on to:

[Setting up test nodes](../02-acquiring-nodes)
# Writing advanced tasks

> **Difficulty**: Intermediate

> **Time**: Approximately 10 minutes

In this exercise you will write a task with metadata. 

# Prerequisites
Complete the following before you start this lesson:

1. [Installing Bolt](../01-installing-bolt)
1. [Acquiring nodes](../02-acquiring-nodes)
1. [Writing tasks](../05-writing-tasks)

# About task metadata
Task metadata files describe task parameters, validate input, and control how tasks are executed.  Adding metadata to your tasks helps others use them.  You write metadata for a task in JSON and save it with the same name as your task. For example, if you write a task called `great_metadata.py` its corresponding metadata file is named `great_metadata.json`.  

# Writing your first task with metadata
Write a simple task that formats the parameters a user gives it.

1. Save the following file to `modules/exercise8/tasks/great_metadata.py`:

    ```python
    #!/usr/bin/env python

    """
    This script prints the values and types passed to it via standard in.  It will
    return a JSON string with a parameters key containing objects that describe
    the parameters passed by the user.
    """

    import json
    import sys

    def make_serializable(object):
      if sys.version_info[0] > 2:
        return object
      if isinstance(object, unicode):
        return object.encode('utf-8')
      else:
        return object

    data = json.load(sys.stdin)

    message = """
    Congratulations on writing your metadata!  Here are
    the keys and the values that you passed to this task.
    """

    result = {'message': message, 'parameters': []}
    for key in data:
        k = make_serializable(key)
        v = make_serializable(data[key])
        t = type(data[key]).__name__
        param = {'key': k, 'value': v, 'type': t}
        result['parameters'].append(param)

    print(json.dumps(result))
    ```

2. Write the accompanying metadata and save the file to `modules/exercise8/tasks/great_metadata.json`. Specify the parameters as types such as `"type": "Integer"`  which help validate user input as an `Integer`.  

    ```json
    {
      "description": "An exercise in writing great metadata",
      "input_method": "stdin",
    
      "parameters": {
        "name": {
          "description": "The description for the 'name' parameter",
          "type": "String"
        },
        "recursive": {
          "description": "The description for the 'recursive' parameter",
          "type": "Boolean"
        },
        "action": {
          "description": "The description for the 'action' parameter",
          "type": "Enum[stop, start, restart]"
        },
        "timeout": {
          "description": "The description for the 'timeout' parameter",
          "type": "Optional[Integer]"
        }
      }
    }
    ```

# Using your task with metadata

1. Run 'bolt task show' to verify that the task you created appears with its description in the list of available tasks.

    ```
    bolt task show --modulepath ./modules
    ```
    The result:
    ```     
    ...
    exercise8::great_metadata     An exercise in writing great metadata
    facter_task                   Inspect the value of system facts
    install_puppet                Install the puppet 5 agent package
    ...
    ```

2. Run `bolt task show <task-name>` to view the parameters that your task uses.

    ```
    bolt task show exercise8::great_metadata --modulepath ./modules
    ```
    The result:
    ```    
    exercise8::great_metadata - An exercise in writing great metadata

    USAGE:
    bolt task run --nodes <node-name> exercise8::great_metadata name=<value> recursive=<value> action=<value> timeout=<value> [--noop]

    PARAMETERS:
    - name: String
        The description for the 'name' parameter
    - recursive: Boolean
        The description for the 'recursive' parameter
    - action: Enum[stop, start, restart]
        The description for the 'action' parameter
    - timeout: Optional[Integer]
        The description for the 'timeout' parameter

    MODULE:
    tasks-hands-on-lab/08-writing-advanced-tasks/modules/exercise8
    ```

# Testing your task's metadata validation

Bolt can use the types that you have specified in your metadata to validate parameters passed to your task.  Run your task with an incorrect value for the `action` parameter and see what happens.  

1. Run your task and pass the following parameters as a JSON string.

    ```
    bolt task run exercise8::great_metadata --nodes all --modulepath ./modules --params '{"name":"poppey","action":"spinach","recursive":true}'
    ```
    The result:
    ```     
    Task exercise8::great_metadata:
     parameter 'action' expects a match for Enum['restart', 'start', 'stop'], got 'spinach'
    ```

2. Correct the value for the action parameter and run the task again.
    ```
    bolt task run exercise8::great_metadata --nodes node1 --modulepath ./modules --params '{"name":"poppey","action":"start","recursive":true}'
    ```
    The result:
    ```     
    Started on node1...
    Finished on node1:
      {
        "message": "\nCongratulations on writing your metadata!  Here are\nthe keys and the values that you passed to this task.\n",
        "parameters": [
          {
            "type": "unicode",
            "value": "start",
            "key": "action"
          },
          {
            "type": "unicode",
            "value": "exercise8::great_metadata",
            "key": "_task"
          },
          {
            "type": "unicode",
            "value": "poppey",
            "key": "name"
          },
          {
            "type": "bool",
            "value": true,
            "key": "recursive"
          }
        ]
      }
    Successful on 1 node: node1
    Ran on 1 node in 0.97 seconds
    ```

# Creating a task that supports no-operation mode (noop)

You can write tasks that support no-operation mode (noop). You use noop to see what changes a task would make, but without taking any action.

1. Create the metadata for the new task and save it to `modules/exercise8/tasks/file.json`:

    ```json
    {
      "description": "Write content to a file.",
      "supports_noop": true,
      "parameters": {
        "filename": {
          "description": "the file to write to",
          "type": "String[1]"
        },
        "content": {
          "description": "The content to write",
          "type": "String"
        }
      }
    }
    ```

2. Save the following file to `modules/exercise8/tasks/file.py`. This task uses input from stdin. When a user passes the `--noop` flag, the JSON object from stdin will contain the `_noop` key with a value of True.  

    ```python
    #!/usr/bin/env python
    
    """
    This script attempts the creation of a file on a target system. It will
    return JSON string describing the actions it performed.  If passed "{"_noop": True}"
    on stdin it will check to see if it can write the file but not actually write it.
    """
    
    import json
    import os
    import sys
    
    params = json.load(sys.stdin)
    filename = params['filename']
    content = params['content']
    noop = params.get('_noop', False)
    
    exitcode = 0
    
    def make_error(msg):
      error = {
          "_error": {
              "kind": "file_error",
              "msg": msg,
              "details": {},
          }
      }
      return error
    
    try:
      if noop:
        path = os.path.abspath(os.path.join(filename, os.pardir))
        file_exists = os.access(filename, os.F_OK)
        file_writable = os.access(filename, os.W_OK)
        path_writable = os.access(path, os.W_OK)
    
        if path_writable == False:
          exitcode = 1
          result = make_error("Path %s is not writable" % path)
        elif file_exists == True and file_writable == False:
          exitcode = 1
          result = make_error("File %s is not writable" % filename)
        else:
          result = { "success": True , '_noop': True }
      else:
        with open(filename, 'w') as fh:
          fh.write(content)
          result = { "success": True }
    except Exception as e:
      exitcode = 1
      result = make_error("Could not open file %s: %s" % (filename, str(e)))
    print(json.dumps(result))
    exit(exitcode)
    
    ```

3. Test the task with the `--noop` flag.
    ```
    bolt task run exercise8::file --nodes node1 --modulepath ./modules content=Hello_World filename=/tmp/hello_world --noop
    ```
    The result:
    ```
    Started on node1...
    Finished on node1:
      {
        "_noop": true,
        "success": true
      }
    Successful on 1 node: node1
    Ran on 1 node in 0.96 seconds
    ```
    
4. Run the task again without `--noop` and see the task create the file successfully.
    ```
    bolt task run exercise8::file --nodes node1 --modulepath ./modules content=Hello_World filename=/tmp/hello_world
    ```
    The result:
    ``` 
    Started on node1...
    Finished on node1:
      {
        "success": true
      }
    Successful on 1 node: node1
    Ran on 1 node in 0.98 seconds
    ```
# Next steps

Now that you know how to write task metadata and include the `--noop` flag you can move on to:

1. [Writing advanced Plans](../09-writing-advanced-plans)
# Writing Tasks

> **Difficulty**: Basic

> **Time**: Approximately 15 minutes

In this exercise you will write your first Puppet Tasks for use with Bolt. 

- [How do tasks work?](#how-do-tasks-work)
- [Write your first task in Bash](#write-your-first-task-in-bash)
- [Write your first task in PowerShell](#write-your-first-task-in-powershell)
- [Write your first task in Python](#write-your-first-task-in-python)

# Prerequisites
Complete the following before you start this lesson:

1. [Installing Bolt](../01-installing-bolt)
1. [Setting up test nodes](../02-acquiring-nodes)
1. [Running Commands](../03-running-commands)
1. [Running Scripts](../04-running-scripts)


# How do tasks work?

Tasks are similar to scripts, you can implement them in any language that runs on your target nodes. But tasks are kept in modules and can have metadata. This allows you to reuse and share them more easily. You can upload and download tasks as modules from the [Puppet Forge](https://forge.puppet.com/), run them from GitHub or use them locally to organize your regularly used commands.

Tasks are stored in the `tasks` directory of a module, a module being a directory with a unique name. You can have several tasks per module, but the `init` task is special and runs by default if you do not specify a task name.

By default tasks take arguments as environment variables prefixed with `PT` (short for Puppet Tasks). 

# Write your first task in Bash

This exercise uses `sh`, but you can use Perl, Python, Lua, or JavaScript or any language that can read environment variables or take content on stdin.

1. Save the following file to `modules/exercise5/tasks/init.sh`:

    ```
    #!/bin/sh
    
    echo $(hostname) received the message: $PT_message
    ```

2. Run the exercise5 task. Note the `message` argument. This will be expanded to the `PT_message` environment variable expected by our task. By naming parameters explicitly it's easier for others to use your tasks.

    ```
    bolt task run exercise5 message=hello --nodes node1 --modulepath ./modules
    ```
    The result:
    ```
    Started on node1...
    Finished on node1:
      localhost.localdomain received the message: hello
      {
      }
    Successful on 1 node: node1
    Ran on 1 node in 0.99 seconds
    ```

3. Run the Bolt command with a different value for `message` and see how the output changes.


# Write your first task in PowerShell

If you're targeting Windows nodes then you might prefer to implement the task in PowerShell. 

1. Save the following file as `modules/exercise5/tasks/print.ps1`

    ```powershell
    param ($message)
    Write-Output "$env:computername received the message: $message"
    ```

2. Run the exercise5 task. 

    ```
    bolt task run exercise5::print message="hello powershell" --nodes $WINNODE --modulepath ./modules --no-ssl
    ```
    ```
    The result:
    Started on localhost...
    Finished on localhost:
      Nano received the message: hello powershell
      {
      }
    Successful on 1 node: winrm://vagrant:vagrant@localhost:55985
    Ran on 1 node in 3.87 seconds
    ```

    **Note:**
    
    * The name of the file on disk (minus any file extension) translates to the name of the task when run via Bolt, in this case `print`.
    * The name of the module (directory) is also used to find the relevant task, in this case `exercise5`.
    * As with the Bash example above, name parameters so that they're more easily understood by users of the task.
    * By default tasks with a `.ps1` extension executed over WinRM use PowerShell standard agrument handling rather than being supplied as prefixed environment variables or via `stdin`. 

# Write your first task in Python

Note that Bolt assumes that the required runtime is already available on the target nodes. For the following examples to work, Python 2 or 3 must be installed on the target nodes. This task will also work on Windows system with Python 2 or 3 installed.

1. Save the following as `modules/exercise5/tasks/gethost.py`:

    ```python
    #!/usr/bin/env python
    
    import socket
    import sys
    import os
    import json
    
    host = os.environ.get('PT_host')
    result = { 'host': host }
    
    if host:
        result['ipaddr'] = socket.gethostbyname(host)
        result['hostname'] = socket.gethostname()
        # The _output key is special and used by bolt to display a human readable summary
        result['_output'] = "%s is available at %s on %s" % (host, result['ipaddr'], result['hostname'])
        print(json.dumps(result))
    else:
        # The _error key is special. Bolt will print the 'msg' in the error for the user.
        result['_error'] = { 'msg': 'No host argument passed', 'kind': 'exercise5/missing_parameter' }
        print(json.dumps(result))
        sys.exit(1)
    ```

2. Run the task using the command `bolt task run <task-name> <task options>`.

    ```
    bolt task run exercise5::gethost host=google.com --nodes all --modulepath ./modules
    ```
    The result:
    ```
    Started on node1...
    Finished on node1:
      google.com is available at 172.217.3.206 on localhost.localdomain
      {
        "host": "google.com",
        "hostname": "localhost.localdomain",
        "ipaddr": "172.217.3.206"
      }
    Successful on 1 node: node1
    Ran on 1 node in 0.97 seconds
    ```

# Next steps

Now that you know how to write tasks you can move on to:

[Downloading and running existing tasks](../06-downloading-and-running-existing-tasks)
