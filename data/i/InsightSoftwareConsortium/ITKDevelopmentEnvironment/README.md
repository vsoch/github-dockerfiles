ITK Development Environment
===========================
A repository of scripts to set up an ITK development environment
----------------------------------------------------------------

These scripts will download and build an ITK
development environment including both ITK and SimpleITK:

* on your local box using Docker, or;
* in a local virtual machine using VirtualBox and Vagrant, or;
* on a virtual machine in the cloud using salt

Docker
------

Docker_ is a light-weight, high performance, low resource alternative to the
Vagrant/Salt solutions below.

Docker images are available for GitHub continuous integration testing of the
`ITK Software
Guide <https://github.com/InsightSoftwareConsortium/ITKSoftwareGuide>`_ and `ITK
Modules <https://github.com/InsightSoftwareConsortium/ITKModuleTemplate>`_. For
more information on how to use these image, see the provided links.

VirtualBox Virtual Machine
--------------------------

1. Install VirtualBox_
#. Install Vagrant_
#. Install `Salty Vagrant`_  (``vagrant plugin install vagrant-salt``)
#. Download a base linux box from the `ITK Midas Community`_ or `VagrantBox.es`_ (``vagrant box add DebianWheezy32 http://midas3.kitware.com/midas/download/bitstream/324026/wheezy32.box``)
#. Go to the *Vagrant* directory of this repository (``cd Vagrant``)
#. Run ``vagrant up``

Debian Wheezy in the Cloud
---------------------------

1. Install git and clone the `ITKDevelopmentEnvironment` project:

::

  aptitude install git
  git clone https://github.com/InsightSoftwareConsortium/ITKDevelopmentEnvironment

2. `Install salt`_.
3. Run salt:

::

  mkdir -p /srv && cd /srv
  ln -s ~/ITKDevelopmentEnvironment/Salt/salt
  salt-call --local state.highstate

.. _Docker: http://docker.io
.. _VirtualBox: https://www.virtualbox.org/
.. _Vagrant: http://www.vagrantup.com/
.. _Salty Vagrant: https://github.com/saltstack/salty-vagrant
.. _VagrantBox.es: http://www.vagrantbox.es/
.. _Install salt: http://docs.saltstack.com/topics/installation/debian.html
.. _ITK Midas Community: http://midas3.kitware.com/midas/community/12
