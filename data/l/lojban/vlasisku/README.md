Lojban Mediawiki Server
=======================

This repo cotnains the code used to run the Lojban vlasisku Server, which runs
inside a pair of Docker containers, one for the web server and one for the IRC
bots.

CHECK STUFF IN WHEN YOUR CHANGES ARE DONE!!!
--------------------------------------------

This repo should always have what we're using in production; if you change
something, please check it in!

Requirements To Run Yourself
----------------------------

Docker.  That should be it.

Run setup.sh and then run_docker.sh

You can run the tests in another window with:

        $ docker exec -it lojban_vlasisku nosetests -v --with-doctest


How To Reach The Server
-----------------------

	$ ssh sampre_vs@jukni.lojban.org 

Login is via ssh key, so if you think you should have access but that doesn't
work, email webmaster@lojban.org or find rlpowell in #lojban on freenode irc.

How To Restart The Server
-------------------------

	$ systemctl --user restart vlasisku

	$ systemctl --user restart vlasisku_bots

How To Test Changes
-------------------

Make whatever changes you want, typically to Dockerfile or the source files,
and run:

	$ ./run_docker -t

This will run the server on an alternate port.
You can reach the test instance at http://test-vs.lojban.org/

How To Show What Should Be Running
----------------------------------

        $ systemctl --user --no-page -t service -a
        UNIT                  LOAD   ACTIVE   SUB     DESCRIPTION
        dbus.service          loaded active   running D-Bus User Message Bus
        vlasisku.service      loaded active   running Site/Webserver for vlasisku.lojban.org
        vlasisku_bots.service loaded inactive dead    Site/Webserver for vlasisku.lojban.org
        
        LOAD   = Reflects whether the unit definition was properly loaded.
        ACTIVE = The high-level unit activation state, i.e. generalization of SUB.
        SUB    = The low-level unit activation state, values depend on unit type.
        
        3 loaded units listed.
        To show all installed unit files use 'systemctl list-unit-files'.

How To Show What Is Actually Running
------------------------------------

        $ systemctl --user status
        ● jukni.digitalkingdom.org
            State: running
             Jobs: 0 queued
           Failed: 0 units
            Since: Sat 2018-01-06 22:54:47 PST; 6 days ago
           CGroup: /user.slice/user-1087.slice/user@1087.service
                   ├─dbus.service
                   │ └─25260 /usr/bin/dbus-daemon --session --address=systemd: --nofork --nopidfile --systemd-activation --syslog-only
                   ├─init.scope
                   │ ├─30255 /usr/lib/systemd/systemd --user
                   │ └─30257 (sd-pam)
                   └─vlasisku.service
                     └─21277 /bin/bash -x /home/sampre_vs/vlasisku/run_docker.sh 2>&1

How To Interact With The Instances Directly
-------------------------------------------

	$udo docker exec -it lojban_vlasisku bash 

This will give you a shell on the production web instance; modify as
appropriate for other instances.

How To See Instance Logs
------------------------

	$ journalctl -f -t vlasisku

This will give you the logs on the production web instance.

For test instances, use the run scripts directly, and then the logs will simply
be printed into your terminal.

Thanks
======

* dag, for all of the original code
* Twey, for compiling the grammatical class usage scales.
* Adam Lopresto, for the Perl code compound2affixes mimics.
