[![Build Status](https://travis-ci.org/serverdensity/sd-agent-core-plugins.svg?branch=master)](https://travis-ci.org/serverdensity/sd-agent-core-plugins)
<!---[![Build status](https://ci.appveyor.com/api/projects/status/?svg=true)](https://ci.appveyor.com/project/)-->
# Server Density Agent Core Plugins

This repository contains the Agent Plugins that Server Density officially develops and supports.

# Installing the Plugins

The [Server Density Agent](https://github.com/serverdensity/sd-agent) linux repositories contain all core plugins from this repository, so to get started using them, simply ensure that you have the repository enabled on your server. Instructions are available for [RHEL/CentOS](https://support.serverdensity.com/hc/en-us/articles/212729448-CentOS-Red-Hat-servers) and [Debian/Ubuntu](https://support.serverdensity.com/hc/en-us/articles/213334967-Debian-Ubuntu-servers)

You may install any individual core integration via its own `sd-agent-<plugin_name>` package, e.g. `sd-agent-nginx`.

For a check with underscores in its name, its package name replaces underscores with dashes. For example, the `powerdns_recursor` check is packaged as `sd-agent-powerdns-recursor`.

# Configuring the Plugins

For most plugins you simply need to install the relevant package and rename the configuration file to remove the `.example` suffix. Configuration optons may be required in the plugin configuration file. More details for each plugin can be found at our [support site](https://support.serverdensity.com/hc/)

# Reporting Issues

For more information on plugins, please reference our [documentation](http://support.serverdensity.com). You can also email us at [hello@serverdensity.com](mailto:hello@serverdensity.com) to connect with us.

# Quick development Setup

To get started developing with the integrations-core repo you will need: `gem` and `python`.

We’ve written a gem and a set of scripts to help you get set up, ease development, and provide testing. To begin:

- Run `gem install bundler`
- Run `bundle install`

Once the required Ruby gems have been installed by Bundler, you can easily create a Python environment:

- Run `rake setup_env`. This will install a Python virtual environment along
  with all the components necessary for integration development (including the
  core agent used by the integrations). Some basic software might be needed to
  install the python dependencies like `gcc` and `libssl-dev`.
- Run `source venv/bin/activate` to activate the installed Python virtual
  environment. To exit the virtual environment, run `deactivate`. You can learn
  more about the Python virtual environment on the Virtualenv documentation.

This is a quick setup but from that point you should be able to run the default test suit `rake ci:run`.
