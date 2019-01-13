pg_inspector readme
===================

pg_inspector is a tool to inspect database locks originating from ManageIQ processes. pg_inpector does this in four steps. Run `pg_inspector.rb -h` to see each of the steps. For each step, see its specific options by running pg_inspector.rb operation `-h`.

Automatically run all steps
---------------------------

Run `schedule_server_dump.sh` to dump server information in a daily basis. Then when a database lock problem happens, run `inspect_pg.sh` to run step 1, 3 and 4 together, and collect all output from `/var/www/miq/vmdb/log/` into `pg_inspector_output.tar.gz`. All the steps below will add `pg_inspector_` prefix for all output file name. For details of each step, see below.

Step 1: dump active connections to YAML file
--------------------------------------------

Run `pg_inspector.rb connections`, and it will dump current `pg_stat_activity` to a YAML file. It will also dump `pg_locks`. The database password should be provided using the file `-f` option or a PGPASSWORD environment variable.

Examples:
```
PGPASSWORD=smartvm pg_inspector.rb connections
pg_inspector.rb connections -u username -f file_that_contains_password -s host -p port -o output_file -l locks_output_file
```

It by default use `root` user to login local postgres server, and will ask you for password. You can connect to a different database host by `-s` option, using a different user by `-u` option, and output to different place by `-o` for active connections, `-l` for locks. But default settings and empty password should be sufficient to run in master node of appliance. This dump operation can be run even after database get blocked.

Step 2: dump ManageIQ server information to YAML file
-----------------------------------------------------

Run `pg_inspector.rb servers` will dump ManageIQ server information in a YAML file. Database password is given in the same way as step 1. New one will overwrite old one only if new one dumps successfully. This step can't be dump if blocking happens, so it should be run as a periodical task.

Examples:
```
PGPASSWORD=smartvm pg_inspector.rb servers
pg_inspector.rb servers -u username -f file_that_contains_password -s host -p port -o output_file
```

Step 3: Combine connections and servers information to human readable format
----------------------------------------------------------------------------

Run `pg_inspector.rb human` will combine information gathered from step 1 and step 2 to a human readable YAML file. It doesn't require database access and will take default output name from step 1 and step 2 as input. It has four sections: servers, workers, connections and other_processes.

Examples:
```
pg_inspector.rb human
pg_inspector.rb human -c connections.yml -s servers.yml -o human.yml
```

Step 4: Combine human.yml file and lock file
--------------------------------------------

Run `pg_inspector.rb locks` will combine lock output from step 1 and human.yml from step 3. It doesn't require database access and will take default output name from step 1 and step 3 as input. The file organization will be same as step 3, but each connection has a `blocked_by` property indicate it's blocked by which connection.

Examples:
```
pg_inspector.rb locks
pg_inspector.rb locks -l locks.yml -c human.yml -o locks_output.yml
```

After four steps
----------------

These four steps are included and can be run in customer's appliance. We can do further analysis such as generating and viewing lock graphs from step 4's output. Because this has external dependency which is not revelant to appliance, it's in a separate place.

# ManageIQ

[![Build Status](https://travis-ci.org/ManageIQ/manageiq.svg)](https://travis-ci.org/ManageIQ/manageiq)
[![Code Climate](https://codeclimate.com/github/ManageIQ/manageiq/badges/gpa.svg)](https://codeclimate.com/github/ManageIQ/manageiq)
[![Codacy](https://api.codacy.com/project/badge/grade/9ffce48ccb924020ae8f9e698048e9a4)](https://www.codacy.com/app/ManageIQ/manageiq)
[![Coverage Status](https://coveralls.io/repos/ManageIQ/manageiq/badge.svg?branch=master&service=github)](https://coveralls.io/github/ManageIQ/manageiq?branch=master)
[![Dependency Status](https://gemnasium.com/ManageIQ/manageiq.svg)](https://gemnasium.com/ManageIQ/manageiq)
[![Security](https://hakiri.io/github/ManageIQ/manageiq/master.svg)](https://hakiri.io/github/ManageIQ/manageiq/master)
[![Open Source Helpers](https://www.codetriage.com/manageiq/manageiq/badges/users.svg)](https://www.codetriage.com/manageiq/manageiq)

[![Chat](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/ManageIQ/manageiq?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Translate](https://img.shields.io/badge/translate-zanata-blue.svg)](https://translate.zanata.org/zanata/project/view/manageiq)
[![License](http://img.shields.io/badge/license-APACHE2-blue.svg)](https://www.apache.org/licenses/LICENSE-2.0.html)


[![Build history for master branch](https://buildstats.info/travisci/chart/ManageIQ/manageiq?branch=master&buildCount=50)](https://travis-ci.org/ManageIQ/manageiq/branches)

## Discover, Optimize, and Control your Hybrid IT

### Manage containers, virtual machines, networks, and storage from a single platform

ManageIQ is an open-source Management Platform that delivers the insight, control, and
automation that enterprises need to address the challenges of managing hybrid
IT environments.  It has the following feature sets:

* **Insight**: Discovery, Monitoring, Utilization, Performance, Reporting, Analytics, Chargeback, and Trending.
* **Control**: Security, Compliance, Alerting, Policy-Based Resource and Configuration Management.
* **Automate**: IT Process, Task and Event, Provisioning, Workload Management and Orchestration.
* **Integrate**: Systems Management, Tools and Processes, Event Consoles, CMDB, RBA, and Web Services.

## Get Started

*  [**Download community builds** for your platform](http://manageiq.org/download/)
*  [**Fork the source** to contribute](https://github.com/ManageIQ/manageiq)
*  [**Learn** to use ManageIQ](https://www.youtube.com/user/ManageIQVideo)

## Learn more

*  [**Read** developer guides](https://github.com/ManageiQ/guides)
*  [**Chat** with contributors on Gitter](https://gitter.im/ManageIQ/manageiq)
*  [**File or view bug reports and feature requests** using Issues on Github](https://github.com/ManageIQ/manageiq/issues?state=open)
*  [**Ask** questions of ManageIQ experts](http://talk.manageiq.org/)
*  [**Discuss** ManageIQ with developers and power users](http://talk.manageiq.org/)

We respectfully ask that you do not directly email any manageiq committers with
questions or problems. The community is best served when discussions are held in
public.

## License

See [LICENSE.txt](LICENSE.txt)

## Export Notice

By downloading ManageIQ software, you acknowledge that you understand all of the
following: ManageIQ software and technical information may be subject to the
U.S. Export Administration Regulations (the "EAR") and other U.S. and foreign
laws and may not be exported, re-exported or transferred (a) to any country
listed in Country Group E:1 in Supplement No. 1 to part 740 of the EAR
(currently, Cuba, Iran, North Korea, Sudan & Syria); (b) to any prohibited
destination or to any end user who has been prohibited from participating in
U.S. export transactions by any federal agency of the U.S. government; or (c)
for use in connection with the design, development or production of nuclear,
chemical or biological weapons, or rocket systems, space launch vehicles, or
sounding rockets, or unmanned air vehicle systems. You may not download ManageIQ
software or technical information if you are located in one of these countries
or otherwise subject to these restrictions. You may not provide ManageIQ
software or technical information to individuals or entities located in one of
these countries or otherwise subject to these restrictions. You are also
responsible for compliance with foreign law requirements applicable to the
import, export and use of ManageIQ software and technical information.
# Shared Example Groups

Note that these shared example groups may be utilized outside of the core
project; for example, provider gems utilize and run `:floating_ip` for their
specific provider. Edit and remove these files with caution.
# manageiq-providers-<%= provider_name %>

[![Gem Version](https://badge.fury.io/rb/manageiq-providers-<%= provider_name %>.svg)](http://badge.fury.io/rb/manageiq-providers-<%= provider_name %>)
[![Build Status](https://travis-ci.org/ManageIQ/manageiq-providers-<%= provider_name %>.svg)](https://travis-ci.org/ManageIQ/manageiq-providers-<%= provider_name %>)
[![Code Climate](https://codeclimate.com/github/ManageIQ/manageiq-providers-<%= provider_name %>.svg)](https://codeclimate.com/github/ManageIQ/manageiq-providers-<%= provider_name %>)
[![Test Coverage](https://codeclimate.com/github/ManageIQ/manageiq-providers-<%= provider_name %>/badges/coverage.svg)](https://codeclimate.com/github/ManageIQ/manageiq-providers-<%= provider_name %>/coverage)
[![Dependency Status](https://gemnasium.com/ManageIQ/manageiq-providers-<%= provider_name %>.svg)](https://gemnasium.com/ManageIQ/manageiq-providers-<%= provider_name %>)
[![Security](https://hakiri.io/github/ManageIQ/manageiq-providers-<%= provider_name %>/master.svg)](https://hakiri.io/github/ManageIQ/manageiq-providers-<%= provider_name %>/master)

[![Chat](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/ManageIQ/manageiq-providers-<%= provider_name %>?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
[![Translate](https://img.shields.io/badge/translate-zanata-blue.svg)](https://translate.zanata.org/zanata/project/view/manageiq-providers-<%= provider_name %>)

ManageIQ plugin for the <%= class_name %> provider.

## Development

See the section on pluggable providers in the [ManageIQ Developer Setup](http://manageiq.org/docs/guides/developer_setup)

For quick local setup run `bin/setup`, which will clone the core ManageIQ repository under the *spec* directory and setup necessary config files. If you have already cloned it, you can run `bin/update` to bring the core ManageIQ code up to date.

## License

The gem is available as open source under the terms of the [Apache License 2.0](http://www.apache.org/licenses/LICENSE-2.0).

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request
Tasks (.rake files) in this directory will be available in the main ManageIQ app.
They can be executed in the provider gem via the app: namespace

bin/rails app:<task>

Task private to the provider should go into lib/tasks/tasks_private.
ResourceFeeder
==============

Simple feeds for resources

NOTE: This plugin depends on the latest version of simply_helpful, available here:
http://dev.rubyonrails.org/svn/rails/plugins/simply_helpful/
# ManageIQ Docker Appliance

This image provides ManageIQ using the [podified frontend image](https://github.com/ManageIQ/manageiq-pods/tree/master/images/miq-app-frontend) as a base along with PostgreSQL.

## Build

A typical build takes very little time to complete.
It needs to be initiated from the root directory of the manageiq git repository

```
docker build -t manageiq/manageiq .
```

## Run

### On standard distribution

The first time you run the container, it will initialize the database, **please allow 2-4 mins** for MIQ to respond.

```
docker run -di -p 80:80 -p 443:443 manageiq/manageiq
```
Please note you can ommit some ports from the run command if you don't need to use them

### On Atomic host

```
atomic install -n <name> manageiq
atomic run -n <name> manageiq
atomic stop -n <name>  manageiq
atomic uninstall -n <name> manageiq
```

## Pull and use latest image from Docker Hub

### On standard distribution
```
docker run -di -p 80:80 -p 443:443 docker.io/manageiq/manageiq
```

### On Atomic host

```
atomic install docker.io/manageiq/manageiq
atomic run docker.io/manageiq/manageiq
```
Note due to resource limitations you can not run more than a single container of manageiq on the same Atomic host

## Access
The web interface is exposed at port 443. Default login credentials.

Point your web browser to :

```
https://<your-ip-address>
```

For console access, please use docker exec from docker host :
```
docker exec -ti <container-id> bash -l
```

## Logging

Use `docker logs <container-id>` to view logs
# miqssh miqscp miqcollect miqgrep and miqtail utilities

These tools allow for running commands and copying files and searching log files against multiple ManageIQ workers in an environment based on groups defined in hosts files.

Also, even if you do have pssh or other tools for running commands on multiple systems, the new miqgrep, miqgrep -r, miqtail, and miqtail -r are worth a look.

Different transport mechanisms are now supported and can be selected by updating the .config file.  By default, Ansible is used since it can work in parallel and is included by default with ManageIQ.  Ansible is now the recommended transport for best functionality.

**Note that this program can enable you to do things faster, including mistakes, use at your own risk.**

# Command Descriptions:

miqssh (connect to each host in group and run provided commands)

miqscp (copy file TO each host in group)

miqcollect (copy file FROM each host in group)

miqgrep (connect to each host in group and grep log_file for pattern or request_id and associated task_ids and collate all results and display using less)

miqtail (Use multitail to tail log_file and optionally grep for pattern or request_id and associated task_ids)

miqstatus (run rake evm:status on each host in group)

miqworkermemcheck (search for memory exceeded messages in automation.log)

# Installation:

See INSTALL.txt in this directory.

# Usages:
## miqssh
```

DESCRIPTION: ssh and run command with args

USAGE: miqssh [-g group] [-s] command args

DETAILS:

  -s to run serially

AVAILABLE GROUPS (default is all):

  all
  all_no_db
  db
  ui
  workers
  zone1
  zone2

To see matching hosts for a given group, use:

miqssh [-q] -g <group> list
  -q to suppress header

```
## miqscp
```

DESCRIPTION: push files out using scp

USAGE: miqscp [-g group] [-s] local_file remote_dest_dir

DETAILS:
 
  Only one file is supported at a time

  -s to run serially

AVAILABLE GROUPS (default is all):

  all
  all_no_db
  db
  ui
  workers
  zone1
  zone2

To see matching hosts for a given group, use:

miqscp [-q] -g <group> list
  -q to suppress header

```
## miqcollect
```

DESCRIPTION: pull files in using scp

USAGE: miqcollect [-g group] [-s] remote_file local_dest_dir

DETAILS:
 
  Wildcards are accepted for remote_file but should only match one file
 
  local_files are appended with remote hostname

  -s to run serially

AVAILABLE GROUPS (default is all):

  all
  all_no_db
  db
  ui
  workers
  zone1
  zone2

To see matching hosts for a given group, use:

miqcollect [-q] -g <group> list
  -q to suppress header

```
## miqgrep
```

DESCRIPTION: grep log_file for pattern or request_id and associated task_ids and collate all results and display using less

USAGE: miqgrep [-g group] [-s] [-a] [-i] [-o outputfile] [-Q] (pattern | -r request_id) [log_file]

DETAILS:

  -i is optional to ignore case with grep

  pattern may be specified as a regex suitable for egrep taking care to prevent the shell from interpretation
  pattern may be specified as 'nogrep' to have no grep or use cat instead of grep
  -r request_id maybe used to search for a request_id and associated task_ids
    request_id can be provided with or without commas

  -o outputfile can be used to save output to outputfile
  -Q can be used to not less the output file automatically

  log_file is optional and defaults to automation.log
    For ManageIQ logs, log_file can be in the format of evm or evm.log
    For any other files, use /the/full/path/to/file

  -a can be used to also grep archived logs

  -s to run serially

AVAILABLE GROUPS (default is all):

  all
  all_no_db
  db
  ui
  workers
  zone1
  zone2

To see matching hosts for a given group, use:

miqgrep [-q] -g <group> list
  -q to suppress header

```
## miqtail
```

DESCRIPTION: multitail and grep pattern or request_id and associated task_ids

USAGE: miqtail [-g group] [-s] [-i] [-l] (pattern | -r request_id) [log_file]

DETAILS:

  -i is optional to ignore case with grep

  pattern may be specified as a regex suitable for egrep taking care to prevent the shell from interpretation
  pattern may be specified as 'nogrep' to have no grep or use cat instead of grep
  -r request_id maybe used to search for a request_id and associated task_ids
    request_id can be provided with or without commas

  log_file is optional and defaults to automation.log
    For ManageIQ logs, log_file can be in the format of evm or evm.log
    For any other files, use /the/full/path/to/file

  -l can be used to place output in separate window panes, by default output is merged

  In multitail:
    Move around the buffer similar to less by pressing 'b'
    Exit whatever context you are in by pressing 'q'

  -s to run serially

AVAILABLE GROUPS (default is all):

  all
  all_no_db
  db
  ui
  workers
  zone1
  zone2

To see matching hosts for a given group, use:

miqtail [-q] -g <group> list
  -q to suppress header

```


# Examples:
## miqssh
```
$ miqssh uptime

*** miq01 ***
 16:19:34 up  5:43,  0 users,  load average: 3.10, 3.06, 3.09

*** miq02 ***
 16:19:47 up  1:15,  0 users,  load average: 0.16, 0.07, 0.01

*** miq03 ***
 16:19:53 up  1:15,  0 users,  load average: 0.07, 0.15, 0.14
```
## miqscp
```
$ miqscp README.md /tmp/

*** miq01 ***
README.md                                               100% 1020     1.0KB/s   00:00    

*** miq02 ***
README.md                                               100% 1020     1.0KB/s   00:00    
```
## miqcollect
```
$ miqcollect /etc/hostname /tmp/

*** miq1 ***
hostname                                                100%   22    39.2KB/s   00:00    

*** miq2 ***
hostname                                                100%    6     9.0KB/s   00:00    

*** miq3 ***
hostname                                                100%    6     9.5KB/s   00:00    

$ ls /tmp/*hostname*
/tmp/hostname-miq1  /tmp/hostname-miq2  /tmp/hostname-miq3
```
## miqgrep pattern
```
$ miqgrep "MiqEventHandler#log_status" evm

*** miq1 ***

*** miq2 ***

*** miq3 ***

*** collating results ***

[miq1] [----] I, [2017-08-11T19:06:20.698103 #2949:b81140]  INFO -- : Q-task_id([log_status]) MIQ(MiqEventHandler#log_status) [Event Handler] Worker ID [1000000001071], PID [2922], GUID [c0f9c28a-7ed6-11e7-8b18-525400431635], Last Heartbeat [2017-08-11 23:06:19 UTC], Process Info: Memory Usage [310091776], Memory Size [652206080], Proportional Set Size: [203949000], Memory % [3.01], CPU Time [735.0], CPU % [0.09], Priority [27]
[miq2] [----] I, [2017-08-11T19:06:25.187956 #2765:623130]  INFO -- : Q-task_id([log_status]) MIQ(MiqEventHandler#log_status) [Event Handler] Worker ID [1000000002270], PID [2756], GUID [f99103f2-7eda-11e7-a70f-5254003dad57], Last Heartbeat [2017-08-11 23:06:14 UTC], Process Info: Memory Usage [338751488], Memory Size [672755712], Proportional Set Size: [235704000], Memory % [3.28], CPU Time [726.0], CPU % [0.11], Priority [27]
[miq1] [----] I, [2017-08-11T19:11:22.361405 #2949:b81140]  INFO -- : Q-task_id([log_status]) MIQ(MiqEventHandler#log_status) [Event Handler] Worker ID [1000000001071], PID [2922], GUID [c0f9c28a-7ed6-11e7-8b18-525400431635], Last Heartbeat [2017-08-11 23:11:14 UTC], Process Info: Memory Usage [310091776], Memory Size [652206080], Proportional Set Size: [203977000], Memory % [3.01], CPU Time [785.0], CPU % [0.09], Priority [27]
[miq2] [----] I, [2017-08-11T19:11:24.019597 #2765:623130]  INFO -- : Q-task_id([log_status]) MIQ(MiqEventHandler#log_status) [Event Handler] Worker ID [1000000002270], PID [2756], GUID [f99103f2-7eda-11e7-a70f-5254003dad57], Last Heartbeat [2017-08-11 23:11:21 UTC], Process Info: Memory Usage [338751488], Memory Size [672755712], Proportional Set Size: [235704000], Memory % [3.28], CPU Time [774.0], CPU % [0.12], Priority [27]
```
## miqgrep -r request_id
```
$ miqgrep -r 1,000,000,000,088

*** looking for tasks associated with request_id: 1000000000088 ***

*** looking for request_id: 1000000000088 and task_ids: 1000000000088 ***

*** miq1 ***

*** miq2 ***

*** miq3 ***

*** collating results ***

[miq2] [----] I, [2017-08-11T19:30:25.616820 #2773:3e3f758]  INFO -- : Q-task_id([service_template_provision_task_1000000000087]) Instantiating [/System/Process/REQUEST?MiqProvisionRequest%3A%3Amiq_provision_request=1000000000088&MiqRequest%3A%3Amiq_request=1000000000088&MiqServer%3A%3Amiq_server=1000000000001&User%3A%3Auser=1000000000001&message=get_vmname&object_name=REQUEST&request=UI_PROVISION_INFO&vmdb_object_type=miq_provision_request]
[miq2] [----] I, [2017-08-11T19:30:25.664169 #2773:3e3f758]  INFO -- : Q-task_id([service_template_provision_task_1000000000087]) Updated namespace [/System/Process/REQUEST?MiqProvisionRequest%3A%3Amiq_provision_request=1000000000088&MiqRequest%3A%3Amiq_request=1000000000088&MiqServer%3A%3Amiq_server=1000000000001&User%3A%3Auser=1000000000001&message=get_vmname&object_name=REQUEST&request=UI_PROVISION_INFO&vmdb_object_type=miq_provision_request  ManageIQ/System]
...
```
## miqtail pattern
```
$ miqtail "ERROR|WARN" evm

Running: multitail -L "ssh miq1 tail -f /var/www/miq/vmdb/log/evm.log \| egrep \"ERROR\|WARN\" | sed -e 's/^/[miq1] /'" -L "ssh miq2 tail -f /var/www/miq/vmdb/log/evm.log \| egrep \"ERROR\|WARN\" | sed -e 's/^/[miq2] /'" -L "ssh miq3 tail -f /var/www/miq/vmdb/log/evm.log \| egrep \"ERROR\|WARN\" | sed -e 's/^/[miq3] /'"

[miq1] [----] E, [2017-08-11T18:22:56.974519 #2939:b81140] ERROR -- : <RHEVM> Ovirt::Service#resource_get: class = Errno::EHOSTUNREACH, message=Failed to open TCP connection to rhvm1.hemlockhill.org:443 (No route to host - connect(2) for "rhvm1.hemlockhill.org" port 443), URI=https://rhvm1.hemlockhill.org/ovirt-engine/api
[miq1] [----] W, [2017-08-11T18:22:56.975316 #2939:b81140]  WARN -- : MIQ(ManageIQ::Providers::Redhat::InfraManager#verify_credentials_for_rhevm) Failed to open TCP connection to rhvm1.hemlockhill.org:443 (No route to host - connect(2) for "rhvm1.hemlockhill.org" port 443)
[miq1] [----] W, [2017-08-11T18:22:56.975570 #2939:b81140]  WARN -- : MIQ(ManageIQ::Providers::Redhat::InfraManager#authentication_check_no_validation) type: [:default] for [1000000000002] [rhvm1] Validation failed: unreachable, Failed to open TCP connection to rhvm1.hemlockhill.org:443 (No route to host - connect(2) for "rhvm1.hemlockhill.org" port 443)
[miq1] [----] W, [2017-08-11T18:22:56.976243 #2939:b81140]  WARN -- : MIQ(AuthUseridPassword#validation_failed) [ExtManagementSystem] [1000000000002], previously valid on: 2017-04-19 04:48:07 UTC, previous status: [Unreachable]
[miq1] [----] W, [2017-08-11T18:22:56.981000 #2931:b81140]  WARN -- : MIQ(ManageIQ::Providers::Vmware::InfraManager#verify_credentials) #<Errno::EHOSTUNREACH: No route to host - connect(2) for "vcenter1.hemlockhill.org" port 443 (vcenter1.hemlockhill.org:443)>
[miq1] [----] W, [2017-08-11T18:22:56.981450 #2931:b81140]  WARN -- : MIQ(ManageIQ::Providers::Vmware::InfraManager#authentication_check_no_validation) type: ["default"] for [1000000000001] [vcenter1] Validation failed: unreachable, No route to host - connect(2) for "vcenter1.hemlockhill.org" port 443 (vcenter1.hemlockhill.org:443)
[miq1] [----] W, [2017-08-11T18:22:56.982164 #2931:b81140]  WARN -- : MIQ(AuthUseridPassword#validation_failed) [ExtManagementSystem] [1000000000001], previously valid on: 2017-04-19 04:59:44 UTC, previous status: [Unreachable]
[miq2] [----] W, [2017-08-11T18:36:44.479934 #2738:623130]  WARN -- : MIQ(ManageIQ::Providers::Foreman::ConfigurationManager::RefreshParser#configuration_profile_inv_to_hashes) hostgroup openstack missing: location

```
## miqtail -r request_id
```
$ miqtail -r 1,000,000,000,088

*** looking for tasks associated with request_id: 1000000000088 ***

*** looking for request_id: 1000000000088 and task_ids: 1000000000088 ***

Running: multitail -L "ssh miq1 tail -f /var/www/miq/vmdb/log/automation.log \| egrep \"1000000000088\|1000000000088\" | sed -e 's/^/[miq1] /'" -L "ssh miq2 tail -f /var/www/miq/vmdb/log/automation.log \| egrep \"1000000000088\|1000000000088\" | sed -e 's/^/[miq2] /'" -L "ssh miq3 tail -f /var/www/miq/vmdb/log/automation.log \| egrep \"1000000000088\|1000000000088\" | sed -e 's/^/[miq3] /'"

[miq2] [----] I, [2017-08-11T19:31:06.042900 #2765:623130]  INFO -- : Q-task_id([miq_provision_request_1000000000088]) Followed  Relationship [miqaedb:/infrastructure/VM/Provisioning/Profile/EvmGroup-super_administrator#get_vmname]
[miq2] [----] I, [2017-08-11T19:31:06.043258 #2765:623130]  INFO -- : Q-task_id([miq_provision_request_1000000000088]) Followed  Relationship [miqaedb:/System/Request/UI_PROVISION_INFO#create]
[miq2] [----] I, [2017-08-11T19:31:09.194610 #2773:623130]  INFO -- : Q-task_id([miq_provision_1000000000088]) Instantiating [/System/Process/AUTOMATION?MiqProvision%3A%3Amiq_provision=1000000000088&MiqServer%3A%3Amiq_server=1000000000001&User%3A%3Auser=1000000000001&object_name=AUTOMATION&request=vm_provision&vmdb_object_type=miq_provision]

```
# Sample miqhosts file:

```
# This file is a sample.  See miqhosts-gen script to generate this file by querying the VMDB.
#
# hostname_or_ip  <white space>	groups to assign host to separated by commas.
#
# Lines starting with a # are ignored.
#
miqdb01.example.com		db
miqui01.example.com		ui
miqwrk01.example.com		workers,zone1
miqwrk02.example.com		workers,zone1
miqwrk03.example.com		workers,zone2
miqwrk04.example.com		workers,zone2
```
