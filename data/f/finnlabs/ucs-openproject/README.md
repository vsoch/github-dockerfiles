# OpenProject version for UCS

This repo contains the scripts required to make OpenProject work on the UCS
distribution.

We're following the Docker approach, outlined at
<http://docs.software-univention.de/app-tutorial.html#docker:example:prerequisites>.

## Prerequisites

First, you need to launch a UCS instance on EC2. At the time of writing
(2016/04/27), the latest AMI is `ami-08be0c7b`. If it no longer exists, search
in the **Community AMIs** for `ucs`.

Once the instance has launched, you need to ssh into it using the `root` user,
and then follow the instructions displayed in the message of the day (i.e.
change the root password, and connect to the UCS web management UI to finish
the installation).

After that, you need to make sure you have the necessary packages installed for
local development:

```bash
ucr set repository/online/unmaintained='yes'
apt-get install -y univention-appcenter-dev univention-appcenter-docker univention-appcenter
univention-app dev-setup-local-appcenter
```

Finally, you need to setup the OpenProject APT repository that holds the
packages you want to release on UCS:

```bash
wget -qO - https://deb.packager.io/key | sudo apt-key add -
echo "deb https://deb.packager.io/gh/opf/openproject-ce wheezy stable/5" | sudo tee /etc/apt/sources.list.d/openproject-ce.list
sudo apt-get update
```

## Testing the UCS installation locally

Register the app (do it every time you change stuff):

```bash
./bin/test-local
#=> ... Component: openproject_20160427
```

If you've made changes, re-run the test-local script by specifying the same
component than on the first run:

```bash
COMPONENT=openproject_20160427 ./bin/test-local
```

Install the app:

```bash
univention-app install openproject
```

Remove the app:

```bash
univention-app remove openproject
```

Tip: if you want to test a new version of the `openproject.inst` script without
the need to remove and re-register, and re-install the app, you can do it as
follows (don't forget to increase `VERSION`):

```bash
cp dist/openproject.join /usr/lib/univention-install/50openproject.inst
univention-run-join-scripts
```

Logs are available in `/var/log/univention/join.log`. Adding a `set -x` while
you're testing your script might be a good idea to see what's going on.

## Releasing a new version

Update the `.ini` file with the proper OpenProject version.

Make sure the `VERSION` numbers have been incremented if you've made changes to
the `inst`/`uinst` files.

Use the provided `Makefile` to generate the required tarball with the right
structure as per the documentation at
<http://docs.software-univention.de/app-tutorial.html#provide>.

```
make all
```

This will package everything into an `openproject.tar.gz` file. You can then
upload it using the form at <https://upload.univention.de/upload.php>.

## Important

* Only increment the `VERSION` numbers of the `inst`/`uinst` when you've made
  changes.

* The `inst` join script MUST BE IDEMPOTENT! See
  https://docs.software-univention.de/developer-reference.html#join:write. Make
sure that you're not overwriting any configuration file that may have been
updated by the package or the user.

## Tips

Re-run the joinscript step with a newer version, without uninstalling/re-installing the app:

```
cp dist/openproject.inst /usr/lib/univention-install/50openproject.inst
univention-run-join-scripts
```

Look at logs of join scripts:

```
cat /var/log/univention/join.log
```

Testing a package upgrade before releasing to the official app center:

```
univention-app remove openproject --do-not-backup
ucr set repository/app_center/server=appcenter-test.software-univention.de
univention-app install openproject=5.0.15
univention-app upgrade openproject
```

## Release a new version to the AppCenter with the selfservice app

Build the docker image that will be used to run the commands:

    docker build -t finnlabs/ucs .

Add your UCS username and password for the self-service center to a ucs.env file:

    echo "USERNAME=crohr" > ucs.env
    echo "PASSWORD=p4ssw0rd" >> ucs.env

You can now launch a docker container to play with the release script:

    docker run --rm -it --env-file ucs.env -v $(pwd):/workspace finnlabs/ucs bash
    VERSION=6.0.4 BRANCH=stable/6 ./bin/publish

The above command will update the Version number in the ini file from the
`dist/` folder, fetch the packages from the given BRANCH, and zip everything
into a `openproject.tar.gz` file. This file will then be sent to the UCS API to
create a new app version from it (untested yet, upload fails).

Note that ideally you should re-download the tarball for the previous version
and unpack it into `dist/` before releasing a new version. This is because UCS
may have made some changes on their side. You could do that with (replace
`openproject_20160909154556` with the latest component published in the App
Center):

    ./bin/univention-appcenter-selfservice download 4.1 openproject_20160909154556
    tar xzf openproject_20160909154556.tar.gz -C dist/

The selfservice UI is available from
<https://selfservice.software-univention.de/univention-management-console/#module=appcenter-selfservice::0:>.
