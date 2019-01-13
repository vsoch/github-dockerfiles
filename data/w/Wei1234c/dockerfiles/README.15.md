# Jupyter Notebook

The Jupyter HTML notebook is a web-based notebook environment for interactive computing.

Dev quickstart:

* ensure that you have node/npm installed (e.g. `brew install node` on OS X)
* Clone this repo and cd into it
* `pip install --pre -e .`

_NOTE_: For Debian/Ubuntu systems, if you're installing the system node you need
to use the 'nodejs-legacy' package and not the 'node' package.

Launch with:

    jupyter notebook

Example installation (tested on Ubuntu Trusty):

```
sudo apt-get install nodejs-legacy npm python-virtualenv python-dev
# ensure setuptools/pip are up-to-date
pip install --upgrade setuptools pip
git clone https://github.com/jupyter/notebook.git
cd notebook
pip install --pre -e .
jupyter notebook
```

For FreeBSD:
```
cd /usr/ports/www/npm
sudo make install    # (Be sure to select the "NODE" option)
cd /usr/ports/devel/py-pip
sudo make install
cd /usr/ports/devel/py-virtualenv
sudo make install
cd /usr/ports/shells/bash
sudo make install
mkdir -p ~/.virtualenvs
python2.7 -m virtualenv ~/.virtualenvs/notebook
bash
source ~/.virtualenvs/notebook/bin/activate
pip install --upgrade setuptools pip pycurl
git clone https://github.com/jupyter/notebook.git
cd notebook
pip install -r requirements.txt -e .
jupyter notebook
```
# IPython Notebook JavaScript Tests

This directory includes regression tests for the web notebook. These tests
depend on [CasperJS](http://casperjs.org/), which in turn requires a recent
version of [PhantomJS](http://phantomjs.org/).

The JavaScript tests are organized into subdirectories that match those in
`static` (`base', `notebook`, `services`, `tree`, etc.).

To run all of the JavaScript tests do:

```
iptest js
```

To run the JavaScript tests in a single subdirectory (`notebook` in this
case) do:

```
iptest js/notebook
```

The file `util.js` contains utility functions for tests, including a path to
a running notebook server on localhost (http://127.0.0.1) with the port
number specified as a command line argument to the test suite. Port 8888 is
used if `--port=` is not specified. When you run these tests using `iptest`
you do not, however, have to start a notebook server yourself; that is done
automatically.
git hooks for IPython

add these to your `.git/hooks`

For now, we just have `post-checkout` and `post-merge`,
both of which update submodules and attempt to rebuild css sourcemaps,
so make sure that you have a fully synced repo whenever you checkout or pull.

To use these hooks, run `./install-hooks.sh`. 
If you havn't initialised and updated the submodules manually, you will then need to run `git checkout master` to activate the hooks (even if you already have `master` checked out).
