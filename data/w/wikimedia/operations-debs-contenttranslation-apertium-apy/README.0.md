# Language Names

## SQL Files

### Generated - DO NOT EDIT

- `scraped.sql` contains language names from the Unicode CLDR. It is created
  by `scraper.py`.
- `scraped-sil.sql` contains language names from SIL International. It is
  created by `scraper-sil.py`.

### Manual - EDIT

- `manual.sql` contains 'fixes' and 'additions' to the scraped data.
- `variants.sql` contains additions to the scraped data for language variants.
- `turkic.sql` contains Turkic language names.

## Scripts

To run `scraper.py`, first install some dependencies:

    sudo apt-get install libxml2-dev libxslt-dev
    sudo pip3 install lxml

`scraper-sil.py` has no external dependencies.
Testing
=======

The tests require some test data.

To install the test data on Debian-based systems, first install core
tools as show at http://wiki.apertium.org/wiki/Debian and then do

    sudo apt-get install apertium-sme-nob apertium-es-en
    mkdir ~/apy-testdata
    cd ~/apy-testdata
    git clone --depth 1 https://github.com/apertium/apertium-nno
    cd apertium-nno
    ./autogen.sh
    make -j4

Now go back to the APy directory, and do

    NONPAIRS=~/apy-testdata python3 -m unittest tests/test*.py

to run the tests.
# -*- mode:markdown -*-

To run APY with systemd, edit `apy.service` and change the `User`
field to have the username of the user who should run APY, and
`ExecStart` to how you start APY. Then do

    sudo cp tools/systemd/apy.service /etc/systemd/system/
	sudo systemctl daemon-reload  # Make systemd notice the new apy.service file
	sudo systemctl enable apy     # Make APY start on boot
	sudo systemctl start apy      # Make APY start now

To show the status of the daemon, along with the most recent log
output:

    sudo systemctl status apy

To restart APY:

    sudo systemctl restart apy

To browse the full APY logs:

    sudo journalctl _SYSTEMD_UNIT=apy.service

(You can also browse logs since last boot with `-b` or since yesterday
and so on, see http://0pointer.de/blog/projects/journalctl.html for
some examples.)
