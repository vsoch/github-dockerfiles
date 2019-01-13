Generic single-database configuration.The OpenShift `python` cartridge documentation can be found at:
http://openshift.github.io/documentation/oo_cartridge_guide.html#python

For information about .openshift directory, consult the documentation:
http://openshift.github.io/documentation/oo_user_guide.html#the-openshift-directory
For information about action hooks, consult the documentation:

http://openshift.github.io/documentation/oo_user_guide.html#action-hooks
For information about markers, consult the documentation:

https://docs.openshift.org/origin-m4/oo_user_guide.html#using-cartridges
https://docs.openshift.org/origin-m4/oo_cartridge_guide.html#markers-7

Run scripts or jobs on a periodic basis
=======================================
Any scripts or jobs added to the minutely, hourly, daily, weekly or monthly
directories will be run on a scheduled basis (frequency is as indicated by the
name of the directory) using run-parts.

run-parts ignores any files that are hidden or dotfiles (.*) or backup
files (*~ or *,)  or named *.{rpmsave,rpmorig,rpmnew,swp,cfsaved}

The presence of two specially named files jobs.deny and jobs.allow controls
how run-parts executes your scripts/jobs.
   jobs.deny  ===> Prevents specific scripts or jobs from being executed.
   jobs.allow ===> Only execute the named scripts or jobs (all other/non-named
                   scripts that exist in this directory are ignored).

The principles of jobs.deny and jobs.allow are the same as those of cron.deny
and cron.allow and are described in detail at: 
   http://docs.redhat.com/docs/en-US/Red_Hat_Enterprise_Linux/6/html/Deployment_Guide/ch-Automating_System_Tasks.html#s2-autotasks-cron-access

See: man crontab or above link for more details and see the the weekly/
     directory for an example.

PLEASE NOTE: The Cron cartridge must be installed in order to run the configured jobs.

For more information about cron, consult the documentation:
https://docs.openshift.org/origin-m4/oo_cartridge_guide.html#cron
Run scripts or jobs on a weekly basis
=====================================
Any scripts or jobs added to this directory will be run on a scheduled basis
(weekly) using run-parts.

run-parts ignores any files that are hidden or dotfiles (.*) or backup
files (*~ or *,)  or named *.{rpmsave,rpmorig,rpmnew,swp,cfsaved} and handles
the files named jobs.deny and jobs.allow specially.

In this specific example, the chronograph script is the only script or job file
executed on a weekly basis (due to white-listing it in jobs.allow). And the
README and chrono.dat file are ignored either as a result of being black-listed
in jobs.deny or because they are NOT white-listed in the jobs.allow file.

For more details, please see ../README.cron file.

