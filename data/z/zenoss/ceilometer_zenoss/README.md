ceilometer_zenoss
=================

This Ceilometer dispatcher plugin ships raw event and metering data from
ceilometer to Zenoss for storage in the Zenoss event and performance databases.

This integration is done by publishing messages to Zenoss's RabbitMQ server.

A zenoss-specific event_definitions.yaml file is included.  This is the same
as the stock ceilometer one, with some additional traits added to the compute
notification events.

This dispatcher should be installed on all nodes running any ceilometer, but
particularly those running ceilometer-collector or ceilometer-agent-notification.

Compatibility
-------------
Version 1.0.1 for Kilo and prior; 1.2.0 for Liberty and newer.

Installation
------------

To install the most recent released version from source:
 * sudo pip -q install --force-reinstall https://github.com/zenoss/ceilometer_zenoss/archive/master.zip
 * sudo cp /usr/lib/python2.7/site-packages/ceilometer_zenoss/event_definitions.yaml /etc/ceilometer/

For versions 1.1.0 and newer, RPMs are available as well.

Configuration
-------------

Several changes are required in /etc/ceilometer/ceilometer.conf.

For Newton and higher, in the [event] section, add the line::

    drop_unmatched_notifications = true

For Liberty and prior, in the [DEFAULT] section, add the line::

    dispatcher=zenoss

For Mitaka and higher, in the [DEFAULT] section, add the lines::

    meter_dispatchers = zenoss
    event_dispatchers = zenoss

Place them after any other dispatchers you may already be using, such as "database",
which stores data in the ceilometer database.   If you are only using ceilometer to
feed zenoss, you do not need any other dispatchers enabled.

In the [notification] section, change the line::

    # Save event details.
    store_events=True

Add a section at the bottom to the file to configure the zenoss dispatcher::
    
    [dispatcher_zenoss]
  
    # Device name that this openstack region is registered as in the zenoss UI
    zenoss_device = <device name>
    
    # Zenoss AMQP Server
    amqp_hostname = <zenoss hostname>
    amqp_port = 5672
    amqp_userid = <zenoss amqp userid>
    amqp_password = <zenoss amqp password>
    amqp_virtual_host = <zenoss amqp virtual host>

For more details on configuring these properly, consult the documentation for
the OpenstackInfrastructure ZenPack.

Changes
----------------

* Version 1.0.0
  -  Initial release

* Version 1.0.1
  -  Modified oslo packages import logic for Juno and Kilo

* Version 1.1.0
  -  Modified event traits processing logic for Liberty
  -  Modified package entry points and ZenossDispatcher base classes for Mitaka

* Version 1.1.2
  - Fix bug that can cause failure to reconnect to amqp host after connection is interrupted. (ZPS-460)

* Version 1.2.0
  - Add dispatcher_zenoss config options during init to workarougnd changes in Ocata.
