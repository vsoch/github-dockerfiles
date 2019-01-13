..  Copyright (C) 2017 Alpha Griffin
..  @%@~LICENSE~@%@
..  TF_curses
..  /README.rst
..  __author__ = Ruckusist

====================================
Alpha Griffin TF_Curses
====================================
|travisCI| |coverall| |docs| |chat|

A Front end for the AlphaGriffin TF_Utilities


Starting a Project
------------------

TODO List:
    * complete .ebuild and pip installs
    * complete sphinx deployment - ok
    * come up with an actual version control system.
    * setup tox, coverage, coverall,



Initial Commit
--------------

Details for this(first) commit:

1. Setup the installability of the package.
2. Setup travis-ci.
3. Make sure all(best-we-can) folder path conventions are obsesrved.


Installing
----------

To install this project manually: ``python setup.py install``, this is the only way so far. :(


Preferred Methods of use are in order:
-- Gentoo Support
as root user:
 >>> echo "=dev_python/tf_curses **" >> /etc/portage/package.accept_keywords/tf_curses
 >>> emerge dev_python/tf_curses --ask --verbose --update-use

-- Pypi Support
 >>> pip install tf_curses

-- BSD Support
    Todo.

-- Mac OSX Support
    Todo.

-- Ubuntu Support
    Todo.

-- Windows Support
    Someone else Todo.

Usage
-----
 >>> tf_curses

.. |docs| image:: https://readthedocs.org/projects/tf-curses/badge/?version=latest
    :target: http://tf-curses.readthedocs.io/en/latest/?badge=latest
    :alt: Documentation Status
.. |chat| image:: https://img.shields.io/gitter/room/nwjs/nw.js.svg
    :target: https://gitter.im/AlphaGriffin/Lobby
.. |coverall| image:: https://coveralls.io/repos/github/Ruckusist/tf_curses/badge.svg?branch=master
    :target: https://coveralls.io/github/Ruckusist/tf_curses?branch=master
.. |travisCI| image:: https://travis-ci.org/AlphaGriffin/TF_Curses.svg?branch=master
    :target: https://travis-ci.org/AlphaGriffin/TF_Curses
