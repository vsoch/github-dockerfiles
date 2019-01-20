
![Jive Derby](./raspi/public/images/jive-derby-logo.png "Jive Derby")

The following documentation is available to understand how the Jive Derby operates from the ground up.  Feel free to use this solution to power your own Jive Derby and/or as a reference for building multi-faceted Jive Add-Ons.

# Architecture Overview
![Jive Derby Architecture Overview](./architecture-overview.png "Jive Derby Architecture Overview")

## Local Environment - Raspberry Pi 3

For more details, see [README](./raspi/README.md)

## Cloud Environment - Amazon AWS

For more details, see the [README](./service/README.md)

## External References
* [Deconstructing the Jive Derby ](https://community.jivesoftware.com/docs/DOC-227242) <br/>
A detailed breakdown of all supporting aspects of the Jive Derby, including Jive components and cloud design.

* [Jive Derby - Rules and Restrictions](https://community.jivesoftware.com/groups/jiveworld17/blog/2017/03/30/on-your-mark-get-set-lets-derby#comment-3310025) <br/>
An example of a Jive Derby announcement with rules and car specifications.

# Special Recognition
As with most awesome projects, it is never done on an island.  The following are some companies who were pivotal in making the Jive Derby experience come to life.

<div align="center">
<img alt="Silicon Labs" src="http://www.silabs.com/etc/designs/siliconlabs/global/images/logo.png"/>
</div>

Special thanks to the team at [Silicon Labs](https://www.silabs.com) for the [inspiration](http://www.silabs.com/products/development-tools/wireless/bluetooth/thunderboard-react-derby-car-kit) and support with their awesome (and easy to use) environmental sensors, such as the Thunderboard [React](http://www.silabs.com/products/development-tools/wireless/bluetooth/thunderboard-react-kit-sensor-cloud-connectivity) and [Sense](http://www.silabs.com/products/development-tools/wireless/bluetooth/thunderboard-sense-kit).

----

<div align="center">
  <span style="font-size: 2em; font-weight: bold;"><a href="http://www.derbymagic.com/">Derby Magic</a></span>
</div>

Special thanks to **Robert** at [DerbyMagic.com](http://www.derbymagic.com) for not only stocking the Derby Track, Electronic Timer and supporting Lego hardware, but also for sharing his technical knowledge regarding the specs for the Derby Timer and solenoid starter, which allowed us to fully automate the race experience from our Raspberry Pi!  If you have a desire to run the Jive Derby on your own, we strongly recommend giving Derby Magic a shout.

----

<div align="center">
  <span style="font-size: 2em; font-weight: bold;"><a href="https://www.ngrok.com/">ngrok</a></span>
</div>

Special Thanks [Alan Shreve](https://twitter.com/inconshreveable) at [ngrok](https://www.ngrok.com) for creating an amazing and invaluable tool with such great features.  Not only does ngrok expedite the development life-cycle for cloud-based solutions, it (in this case), enables secure on-the-ground bootstrapping of locally run services to be discovered with minimal requirements on the available internet service!
