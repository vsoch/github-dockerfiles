# Kodi Web Interface - Chorus2
The default Web Interface for Kodi.

A great modern Web UI for Kodi. Browse your Music, Movies or TV Shows from the comfort of your
own web browser. You can play media via Kodi or stream it in your browser. Works best with Chrome
but plays well with most modern browsers.

Successor to [Chorus](https://github.com/jez500/chorus). 
A complete rebuild using Coffee Script, Backbone, Marionette and much, much more.


## Author
[Jeremy Graham ](http://jez.me) with help from [these kind people](https://github.com/xbmc/chorus2/graphs/contributors)


## Current state
Pretty good, most things work really well. Other things need [polish/finishing/fixing](https://github.com/xbmc/chorus2/issues). 
Still considered beta software, expect bugs, changes, nuclear war, etc.

## Getting it working
As of Kodi v17, Chorus2 comes pre-installed out of the box, you just need to enable it and tick a few boxes.

### Enabling & Configuring
Kodi > Settings (cog) > Services > Control

* Enable "Allow control of Kodi via HTTP"
* Select Web interface
* Select "Kodi web interface - Chorus2"
* Enable "Allow programs on this system to control Kodi"
* Enable "Allow programs on other systems to control Kodi"

**For security reasons you should set a username and password to prevent unauthorised access**

### Manual install
For Kodi v16 and below or if you want to get the latest version ASAP, an install via zip is the easiest way to go. Grab the
latest release of `webinterface.default.2.X.X.zip` from the [releases page](https://github.com/xbmc/chorus2/releases) then
install it [like this](http://kodi.wiki/view/Add-on_manager#How_to_install_from_a_ZIP_file). **NOTE:** Chorus2 is intended to
be used with the latest version of Kodi and some (or all) things might not work in older versions due to API changes.

### Using it
Point your web browser to `http://localhost:8080` - replace `localhost` with your IP address if using remotely and if
you have changed your port to something other than `8080` be sure to change that too. More information and advanced
usage can be found over on the [Kodi Wiki page](http://kodi.wiki/view/Web_interface).

## Feature requests / Bugs
Add them to the [list](https://github.com/xbmc/chorus2/issues). For bugs please include Kodi version, Web browser version,
Chorus version and any errors that display in the console. For feature requests, checkout the API browser to see if your
request is currently possible.


## Streaming 
Disclaimer: The success of this depends on the file formats vs what the browser supports.  In general most things work.

### Audio streaming
In the top right there are some tabs, two of them are named Kodi and Local, this is how you toggle what player the UI
is controlling.  In Local mode the logo and accents are pinky-red, In Kodi mode the logo is the Kodi blue. When you 
are in a given mode, actions affect that player, so if you click Play on a track when in Local mode, it will play 
through the browser, likewise, when in Kodi mode all commands are sent to Kodi.  You can also add media to other 
playlists by clicking the menu buttons (three dots vertical) on most media items.

### Video streaming
Video streaming via HTML5 "sort of" works, it really depends on the codec used. An embedded VLC player is also available with better codec support.
This looks like the best we can get until Kodi supports transcoding.
**Chrome users**: Chrome has removed support for vlc/divx plugins so streaming a video requires a [Chrome friendly codec](https://en.wikipedia.org/wiki/HTML5_video#Browser_support).
For best results use Chrome with mp4 video that has 2 channel audio (5.1 audio doesn't seem to work).

## Kodi settings via the web interface
You can change most of the settings you would find in Kodi via the settings page in the web interface.
Some settings have been omitted as they require interaction with the GUI and others are just a basic text field with no options.

## Kodi API browser
There is a hidden feature in Chorus that allows you to play with the Kodi API and see what is capable via the JSON-RPC
interface. If you are building an app or addon that uses the API this can be super useful for both finding and testing
all the methods and types available. If you are thinking about a new feature for Chorus, this is also a great place to
test if it is possible (and fast track development by adding a working example to an issue). You can find the API browser
via "Chorus Lab" (bottom right 3 vertical dots > "The Lab") or directly via `http://localhost:8080/#lab/api-browser`.

## Contributing
If you would like to make this project better I would appreciate any help. There is a develop branch for each version of
Kodi. Please do pull requests against the `dev` branch for the correct version (even better if you can do a PR for both).
Leia (v18) dev branch is `18.x-dev`, Krypton (v17) dev branch is `17.x-dev`. See the
[developers documentation](https://github.com/xbmc/chorus2/tree/master/src/lang/en/developers.md) for information about
getting a dev environment up and running then compiling the project using docker.

### Translations
I only know English so definitely need help with this. I also don't know heaps about javascript multilingual stuff but
thanks to [@mizaki](https://github.com/mizaki) we have a structure ready to go. So it should be nice and easy to translate the UI.

At the moment, there are [a handful](https://github.com/xbmc/chorus2/tree/master/src/lang/_strings) of languages available
but more can be easily added. More strings are always being added so always consider english as the source of truth.

So if you see something in english but want it in your language, I need you! To contribute, send me a PR on a new branch
against `18.x-dev` and/or `17.x-dev`, or if you don't know git, a link to the language file.

Language Files [here](https://github.com/xbmc/chorus2/tree/master/src/lang). 
*English is the only real complete translation file so start with that as your base.*

## Donate
Are you a fan of Chorus? You can [buy Jeremy a beer](https://www.paypal.com/cgi-bin/webscr?cmd=_donations&business=ZCGV976794JHE&lc=AU&item_name=Chorus%20Beer%20Fund&currency_code=AUD&bn=PP%2dDonationsBF%3abtn_donate_SM%2egif%3aNonHosted) to say thanks :)

## License

This program is free software; you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation; either version 2 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
[along with this program](https://github.com/xbmc/chorus2/blob/master/LICENSE);
if not, write to the Free Software Foundation, Inc., 51 Franklin Street,
Fifth Floor, Boston, MA 02110-1301 USA.

[Click here for more information ](https://github.com/xbmc/chorus2/blob/master/src/lang/en/license.md).


## Screenshots

### Homepage (now playing)
![alt text](https://raw.githubusercontent.com/xbmc/chorus2/master/dist/screenshots/now-playing.jpg "Homepage/Now Playing")

### Search results
![alt text](https://raw.githubusercontent.com/xbmc/chorus2/master/dist/screenshots/search.jpg "Search")

### Artists
![alt text](https://raw.githubusercontent.com/xbmc/chorus2/master/dist/screenshots/artists.jpg "Artists")

![alt text](https://raw.githubusercontent.com/xbmc/chorus2/master/dist//screenshots/artist.jpg "Artist")

### Video library
![alt text](https://raw.githubusercontent.com/xbmc/chorus2/master/dist/screenshots/tv.jpg "TV")

### Filtering
![alt text](https://raw.githubusercontent.com/xbmc/chorus2/master/dist/screenshots/movie.jpg "Movies")

### Settings
![alt text](https://raw.githubusercontent.com/xbmc/chorus2/master/dist/screenshots/settings.jpg "Settings")

### Add-ons
![alt text](https://raw.githubusercontent.com/xbmc/chorus2/master/dist/screenshots/addons.jpg "Add-ons")

### Editing media
![alt text](https://raw.githubusercontent.com/xbmc/chorus2/master/dist/screenshots/edit-media.jpg "Editing Media")
Why is there two addon.xml files in this folder?
================================================

This aids development by allowing interchanging between 2 different addon ids. The release addon
id is `webinterface.default` and the development addon id is `webinterface.defaultdev`. This means
you can have the development code unaffected by Kodi updates as it can live in a user folder.

This works well if you symlink the `dist` folder to `webinterface.defaultdev` in the user addons folder.
It lives next to the userdata folder which can be found here: http://kodi.wiki/view/userdata

Eg. `ln -s ~/repos/chorus2/dist ~/.kodi/addons/webinterface.defaultdev`

Toggling the xml in the dist folder can be done using `build.sh`.

* To activate the development addon.xml run `./build.sh dev`
* When a release build is created addon.xml gets reverted back. Eg `./build.xml 2.5.0` where 2.5.0 is the version number.

NOTE:

* When committing any changes to `dist/addon.xml` it should always be the release version with the id `webinterface.default`
* Each time `build.sh` is run it will replace `dist/addon.xml` with the appropriate version so any changes to `dist/addon.xml` should be done to `src/addon.release.xml`
# Translations

To update the language files you just need to know a bit of GIT. This page should help
with the structure of language files.

## Where are the language files?

There are two places where language override files are stored. The LANG_CODE is the two
letter code for that language. Eg: en, fr, de

### Strings

`src/lang/_strings/LANG_CODE.po`

* This is strings used throughout the application. In general, only update `msgstr`.
* If there is no `msgstr` for the string, then copy from en.po and update, Eg de.po.
``` 
msgctxt ""
msgid "Select a filter"
msgstr "Filter wählen"
```

### Pages

`src/lang/LANG_CODE/PAGE.md`

* These are full pages that can be overridden with a different language.
* The pages are in [markdown](https://en.wikipedia.org/wiki/Markdown).
* If there is no *PAGE*.md for yor language then copy from the en folder and edit.
* Only create a *PAGE*.md for a full translation

## Adding a new language

**Example:** If your new language is `French` it would have a *LANG_KEY* of `fr`.

### Tell the app about it

You also need to tell the application to have it as an option. So you edit this file:
`/src/js/helpers/translate.js.coffee` and add `fr: "French"` to the languages in `getLanguages`

### Duplicate the folder/file structure of en

Copy the files you want to override with the new language:

* **Strings:** copy `/src/_strings/en.po` to `/src/_strings/fr.po`
* **Pages:** copy `/src/en/readme.md` to `/src/fr/readme.md`

## Testing

To test you need to do a build, however if you follow the existing structure you shouldn't need to.

If **do** you want to test your language in the app with a build, you can:

1. Ensure `nodejs`, `npm` are installed
2. `cd /chorus/folder`
3. `npm install` (only the first time)
4. `grunt lang` (this will rebuild only the languages in the `dist/lang` folder)
5. Refresh Chorus
  
## Fallback

Translations should fallback to English unless the `msgid` is set in a `LANG_CODE.po` file. 
Or if a page `LANG_CODE/PAGE.md` exists.

## Submitting an update

Send a pull request through [GitHub](https://github.com/jez500/chorus2) on a new branch is the best way.
Would consider updates via other methods.
