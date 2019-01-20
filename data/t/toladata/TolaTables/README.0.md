All icons are taken from Font Awesome (http://fontawesome.io/) project.
The Font Awesome font is licensed under the SIL OFL 1.1:
- http://scripts.sil.org/OFL

SVG icons source: https://github.com/encharm/Font-Awesome-SVG-PNG
Font-Awesome-SVG-PNG is licensed under the MIT license (see file license
in current folder).
Roboto webfont source: https://www.google.com/fonts/specimen/Roboto
Weights used in this project: Light (300), Regular (400), Bold (700)
This file will be a guide on how write an independent app that allows users
to import data from a data system of your choosing.

#App folder
Goes in datasources/

#Getting your app to run
In order for your app to run it must be in the list of apps:
To do this put the name of your app LOCAL_APPS list in the tola/settings/base.py file

#new models
Before running your server you'll have to run migrations in order for the server to use your apps
models

#using existing models
To use existing models use this import
from silo.models import <Model name here>

#navigating to your page
By default tolatables will create a subdomain for use in your apps urls.py file. The name of this
subdomain is your apps name.
In addition tolatables will automatically add a link to your app on the import data dropdown menu.
It'll be of the form "Import from YOUR_APPS_NAME". If you wish to change what appears in
YOUR_APPS_NAME add:
  verbose_name = "NEW_NAME"
to the apps.py file

#to add your type
In order for tola to read your filetype you will somehow need to add your data source to the
read_type database
App Name:
commcare
