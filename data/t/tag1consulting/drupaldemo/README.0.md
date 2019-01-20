This directory structure contains the settings and configuration files specific
to your site or sites and is an integral part of multisite configuration.

The sites/all/ subdirectory structure should be used to place your custom and
downloaded extensions including modules, themes, and third party libraries.

Downloaded installation profiles should be placed in the /profiles directory
in the Drupal root.

In multisite configuration, extensions found in the sites/all directory
structure are available to all sites. Alternatively, the sites/your_site_name/
subdirectory pattern may be used to restrict extensions to a specific
site instance.

See the respective README.txt files in sites/all/themes and sites/all/modules
for additional information about obtaining and organizing extensions.

See INSTALL.txt in the Drupal root for information about single-site
installation or multisite configuration.
This directory should be used to place downloaded and custom libraries (such as
JavaScript libraries) which are used by contributed or custom modules.
Themes allow you to change the look and feel of your Drupal site. You can use
themes contributed by others or create your own.

WHAT TO PLACE IN THIS DIRECTORY?
--------------------------------

Placing downloaded and custom themes in this directory separates downloaded and
custom themes from Drupal core's themes. This allows Drupal core to be updated
without overwriting these files.

DOWNLOAD ADDITIONAL THEMES
--------------------------

Contributed themes from the Drupal community may be downloaded at
https://www.drupal.org/project/project_theme.

MULTISITE CONFIGURATION
-----------------------

In multisite configurations, themes found in this directory are available to
all sites. Alternatively, the sites/your_site_name/themes directory pattern
may be used to restrict themes to a specific site instance.

MORE INFORMATION
-----------------

Refer to the "Appearance" section of the README.txt in the Drupal root directory
for further information on customizing the appearance of Drupal with custom
themes.
Modules extend your site functionality beyond Drupal core.

WHAT TO PLACE IN THIS DIRECTORY?
--------------------------------

Placing downloaded and custom modules in this directory separates downloaded and
custom modules from Drupal core's modules. This allows Drupal core to be updated
without overwriting these files.

DOWNLOAD ADDITIONAL MODULES
---------------------------

Contributed modules from the Drupal community may be downloaded at
https://www.drupal.org/project/project_module.

ORGANIZING MODULES IN THIS DIRECTORY
------------------------------------

You may create subdirectories in this directory, to organize your added modules,
without breaking the site. Some common subdirectories include "contrib" for
contributed modules, and "custom" for custom modules. Note that if you move a
module to a subdirectory after it has been enabled, you may need to clear the
Drupal cache so it can be found. (Alternatively, you can disable the module
before moving it and then re-enable it after the move.)

MULTISITE CONFIGURATION
-----------------------

In multisite configurations, modules found in this directory are available to
all sites. Alternatively, the sites/your_site_name/modules directory pattern
may be used to restrict modules to a specific site instance.

MORE INFORMATION
----------------

Refer to the "Developing for Drupal" section of the README.txt in the Drupal
root directory for further information on extending Drupal with custom modules.
Installation profiles define additional steps that run after the base
installation provided by Drupal core when Drupal is first installed.

WHAT TO PLACE IN THIS DIRECTORY?
--------------------------------

Place downloaded and custom installation profiles in this directory.
Installation profiles are generally provided as part of a Drupal distribution.
They only impact the installation of your site. They do not have any effect on
an already running site.

DOWNLOAD ADDITIONAL DISTRIBUTIONS
---------------------------------

Contributed distributions from the Drupal community may be downloaded at
https://www.drupal.org/project/project_distribution.

MULTISITE CONFIGURATION
-----------------------

In multisite configurations, installation profiles found in this directory are
available to all sites during their initial site installation.

MORE INFORMATION
----------------

Refer to the "Installation profiles" section of the README.txt in the Drupal
root directory for further information on extending Drupal with custom profiles.

This directory should be used to place downloaded translations
for installing Drupal core.

This directory should be used to place downloaded translations
for installing Drupal core.

This directory is reserved for core theme files. Custom or contributed themes
should be placed in their own subdirectory of the sites/all/themes directory.
For multisite installations, they can also be placed in a subdirectory under
/sites/{sitename}/themes/, where {sitename} is the name of your site (e.g.,
www.example.com). This will allow you to more easily update Drupal core files.

For more details, see: http://drupal.org/node/176043


ABOUT STARK
-----------

The Stark theme is provided for demonstration purposes; it uses Drupal's default
HTML markup and CSS styles. It can be used as a troubleshooting tool to
determine whether module-related CSS and JavaScript are interfering with a more
complex theme, and can be used by designers interested in studying Drupal's
default markup without the interference of changes commonly made by more complex
themes.

To avoid obscuring CSS added to the page by Drupal or a contrib module, the
Stark theme itself has no styling, except just enough CSS to arrange the page in
a traditional "Header, sidebars, content, and footer" layout. See the layout.css
file for more information.


ABOUT DRUPAL THEMING
--------------------

To learn how to build your own custom theme and override Drupal's default code,
see the Theming Guide: http://drupal.org/theme-guide

See the sites/all/themes/README.txt for more information on where to place your
custom themes to ensure easy maintenance and upgrades.

This directory is reserved for core module files. Custom or contributed modules
should be placed in their own subdirectory of the sites/all/modules directory.
For multisite installations, they can also be placed in a subdirectory under
/sites/{sitename}/modules/, where {sitename} is the name of your site (e.g.,
www.example.com). This will allow you to more easily update Drupal core files.

For more details, see: http://drupal.org/node/176043

These files are useful in tests that upload files or otherwise need to
manipulate files, in which case they are copied to the files directory as
specified in the site settings. Dummy files can also be generated by tests in
order to save space.
