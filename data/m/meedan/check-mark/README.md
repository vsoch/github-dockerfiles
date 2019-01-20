# Check

[![Travis](https://travis-ci.org/meedan/check-mark.svg?branch=develop)](https://travis-ci.org/meedan/check-mark/)

A browser extension and mobile application for [Check](https://meedan.com/en/check/).

## Browser Extension

### Download

Available for [Mozilla Firefox](https://addons.mozilla.org/firefox/addon/check/) and [Google Chrome](https://chrome.google.com/webstore/detail/check/afafaiilokmpfmkfjjgfenfneoafojie).

### Development

The JavaScript code lives in `src`. Static files like HTML, Manifest and images live in `public`.

Copy `config.js.example` to `config.js` and define your configurations.

You can compile the code with `npm run build`. It was developed and tested with Node 7. After the code is compiled, it will be under `build`. After you installed the extension (see below how to do it), you don't need to re-install it when you make code changes.

#### Running the extension in Google Chrome

* Visit `chrome://extensions`
* Enable "Developer mode"
* Click "Load unpacked extension..."
* Pick the `build` directory
* The extension will appear on the toolbar

#### Running the extension in Firefox

* Visit `about:debugging`
* Click "Load Temporary Add-on"
* Pick the `manifest.json` file inside `build` directory
* The extension will appear on the toolbar

#### Localization

As usual, localization is done on [Transifex](https://www.transifex.com/meedan/check-2/browser-extension/). You must have the `tx` client [installed](http://docs.transifex.com/client/setup/) on your computer and [configured](https://docs.transifex.com/client/client-configuration) to communicate with the Transifex server. You can send new strings to Transifex by running `npm run transifex:upload` and you can download translations from Transifex by running `npm run transifex:download`.

#### Releasing new versions

First, you need to edit `public/manifest.json` and increment the version number.

* QA: `npm run release:qa`
* Live: `npm run release:live`

Releases are available under `releases`. After that, you need to upload `releases/live/live.zip` and `releases/qa/qa.zip` to Chrome Store and Firefox Store.

#### Tests

* You need `zip`, `rspec`, `geckodriver` and `chromedriver`.
* Copy `test/config.yml.example` to `test/config.yml` and adjust the configurations.
* Tests can be run with `npm run test`.

## Mobile Application

### Development

For the first time only, run `npm run prepare-android`. You may also need to open the application on your device, shake it, and set the IP of the host computer and port 8081 at "Dev Settings".

Copy `config.js.example` to `config.js` and define your configurations. Connect your device to your computer and run `npm run build-android`. This command must keep running. If it exits, run again. The application will be launched on your phone.

You can also generate a APK that doesn't depend on the development server. In order to do that, execute `npm run generate-apk` and the APK will be at `android/app/build/outputs/apk/app-release.apk`. 

### TODO

* Avoid that a new instance of the app is triggered when sharing content with already running app (https://github.com/meedan/react-native-share-menu/issues/25)
