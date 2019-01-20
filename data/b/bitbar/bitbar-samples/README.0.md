## Android Espresso Sample
##### Sample Android App to demonstrate Espresso tests

**Use Android Studio:**

clean, rebuild.
run `"BitbarSampleTests"`

or

**From command line:**

```./gradlew clean connectedAndroidTest```


Apks to upload to testdroid cloud will be in (after project is built):

`/BitbarSampleApp/app/build/outputs/apk`

***To run Espresso tests in cloud:***

<pre>
Create new <b>"Android Instrumentation"</b> project.
Upload <b>""app-debug.apk"</b> as the <b>""application"</b> file.
Upload <b>""app-debug-androidTest.apk"</b> as the <b>""test"</b> file.
Set as "Custom test runner" value: <b>android.support.test.runner.AndroidJUnitRunner</b>
Set this as screenshots directory: <b>/sdcard/Pictures/Screenshots</b> 
</pre>


These commands can be set in `"Use test cases from:"` option in "4. Advanced options:" section in a new cloud test run, if `"class"` is selected:

run tests in class:
```
com.bitbar.testdroid.sampletests.BitbarSampleTests
```

run a test in a class:
```
com.bitbar.testdroid.sampletests.BitbarSampleTests#wrongAnswerTest
```
# Ruby Test Run Launcher

This is a sample Ruby test run launcher in Ruby. You can use this to launch
tests in Bitbar cloud or creating new projects.
# Template for Robot Framework

- Libs folder: Place for self made libraries.
- Tests folder: Contains test files. Resource ``${PROJECTROOT}${/}resources${/}common.robot`` should be included under ``*** settings ***`` on each test file so they can use common resources. Write all test files under this folder.
- Resources folder: Contains generic keywords and settings (common.robot), also other files required by the tests. Add all common keywords to common.robot and add all required extra features to this folder.


# How to install requirements:
- pip install -r ./resources/requirements.txt

# Running tests locally:
There are two runner scripts for running the tests locally, ``run_android.py`` and ``run_ios.py``

- ``python run_<OS>.py`` Runs the whole suite. For example ``python run_android.py`` runs all the Android tests.
- ``python run_<OS>.py -i <tag name>`` Runs tests that contains ``[Tags]    <tag name>``
- ``python run_<OS>.py --test <name>`` Runs tests that contains name ``<name>`` in them.
- ``python run_<OS>.py --suite <name>`` Runs the suite containing ``<name>``.
- ``python run_<OS>.py --dryrun`` Runs everything as a dryrun
- ``-x <xunit_output_file>`` command line option can be used to generate report in xUnit compatible XML format. So for example ``python run_<OS>.py -x xunit`` will run all the test and create ``xunit.xml`` file relatively to the output directory of other test results.

# Running tests on the Cloud:
- From ``common.robot`` choose the correct ``${APP_ANDROID}`` or ``${APP_IOS}`` path by uncommenting the one with ``application.apk`` or ``application.ipa`` and commenting out other paths.
- ``create-test-zip-android.sh`` and ``create-test-zip-ios.sh`` will create .zip files containing all necessary files for cloud execution. Scripts output ``tests-robot-android.zip`` and ``tests-robot-ios.zip`` files that can be uploaded to Testdroid Cloud for test execution.
- By default the tests will be run as server-side Appium and the driver is configured to use ``localhost`` address as: ``${REMOTE_URL}    http://localhost:4723/wd/hub``
- Framework can be configured also to run the tests as client-side Appium. To do this, the ``localhost`` address has to be replaced with ``appium.bitbar.com``. Also following additional capabilities have to be added:
	- ``testdroid_username``
	- ``testdroid_password``
	- ``testdroid_target``
	- ``testdroid_project``
	- ``testdroid_testrun``
	- ``testdroid_device``
	- ``testdroid_app``
	- ``BundleID``

	More information about desired capabilities for client-side Appium can be found from Testdroid [Appium Documentation](http://docs.bitbar.com/testing/appium/desired-caps/)

# References
- [Robot Framework User Guide](http://robotframework.org/robotframework/latest/RobotFrameworkUserGuide.html)
- [Appium Library Keyword Documentation](http://jollychang.github.io/robotframework-appiumlibrary/doc/AppiumLibrary.html)
- [robotframework.org](http://robotframework.org/)
# Java Image Recognition Sample

This Java project shows how to create Akaze image recognition tests together with Appium mobile automation framework for use in [Bitbar Testing](http://bitbar.com/testing) mobile device cloud. This project is particularly suited for automated tests on mobile apps that don't have platform specific native elements.

The project uses the Bitbar Sample App, will install it on the device, then check that the Bitbar logo is displayed on the screen using image recognition. The reference Bitbar logo image is located at: *queryimages/bitbar_logo.png*

The project uses:

- [mobile-opencv-image-recognition-library](https://github.com/bitbar/opencv-library) - Library that handles OpenCV related logic

- [Bitbar Testing](http://bitbar.com/testing) - Web service for automated testing on
  real mobile devices. You'll need to have an active account for launching the tests in cloud.

- [OpenCV](http://opencv.org/) - Open Source Computer Vision

- [A-KAZE Features](https://github.com/bitbar/akaze) - Image recognition programs using OpenCV.

- [Maven](https://maven.apache.org/) - Compiles and launches the test code.

# Info on OpenCV and Akaze

We use the akaze-match program from [A-KAZE Features](https://github.com/pablofdezalc/akaze) to find the matching keypoints from two images and save them to a json file. [OpenCV](http://opencv.org/) java bindings are used for processing the json file with keypoints and finding the homography of the wanted image in a scene (screenshot).

The AkazeImageFinder.java class found within the [mobile-opencv-image-recognition-library](https://github.com/bitbar/opencv-library) will run `akaze_match`, then use the keypoints from json to try to identify a given image inside a scene and return the corners of the image found. In our case, we look for specific images from *./queryimages/* folder and try to find them on a screenshot taken from device.

Once the image is located, we can:

- tap it
- drag it
- swipe the screen with it
- etc

All image recognition related methods are implemented in the TestdroidImageRecognition.java class. The class has different functions for first finding the coordinates of the image and then injecting gestures on the device screen. Appium mobile automation framework is used for the automated gestures.

## Installing dependencies

1. A-KAZE Features

   The A-KAZE C++ implementation can optionally be found and built from: [Bitbar Akaze fork](https://github.com/bitbar/akaze). This project already contains the *./lib/\<platform\>/akaze/* folder with pre-built binaries for Linux, OS X and Windows. Only the akaze_match binary is currently in use.


All other dependencies are fetched by Maven automatically.


## Run tests locally from Command Line with Maven

The project uses Bitbar Sample apps, which are available in this repository at [apps/builds](https://github.com/bitbar/testdroid-samples/tree/master/apps/builds). By default, the tested application is assumed to be found at the root of the project with name `application.apk` or `application.ipa` depending on the tested platform. The BitbarIOSSample.ipa application file will also need to be first re-signed for your own test devices, if you'd like to use try it out locally.

You'll also need to have an Appium server launched. For iOS, the UDID of the device should be pre-set in the server settings.

Run the tests with maven using:

    mvn -Dtest=<TestClass> test

For example, to run only the test `mainPageTest` from test class AndroidSample.java you would use:

    mvn -Dtest=AndroidSample#mainPageTest test

To first clean all the previous test result files, add keyword `clean` to the command:

    mvn -Dtest=AndroidSample#mainPageTest clean test

You can also use an IDE to launch the tests. Make sure the project is correctly imported as a Maven project and that the `pom.xml` file has been discovered for Maven's dependency management.

**Reports**

The reports, screenshots and everything else will be found under:
*./target/reports/*

## Run tests as Server Side Appium in [Bitbar Testing](http://bitbar.com/testing)

You will need a Bitbar Testing cloud project of type `Appium Android server side` or `Appium iOS server side` according to the target platform.

Once you have your cloud project created, use the following scripts to create the test zip from your project:

    ./createAndroidZip.sh
or

    ./createiOSZip.sh

Now that you have your test zip and the application file (this sample uses the Bitbar Sample Apps available at [apps/builds](https://github.com/bitbar/testdroid-samples/tree/master/apps/builds), you're ready to create a testrun in your project at the [test cloud](https://cloud.bitbar.com). Upload the app and test zip in the appropriate pages, choose the device group and finally make sure you have set high enough timeout for your tests in the Advanced options (default is 10 minutes).

If you change the name of your Android or iOS test class, you will need to update it to the run-tests_android.sh and run-tests_ios.sh TEST and TEST_CASE variables as appropriate:

    # Name of the desired test class and optionally specific test case, eg: AndroidSample#mainPageTest
    TEST=${TEST:="AndroidSample"}
    # OPTIONAL: add the name of TestCases to be used with the `mvn test` command
    # Leave blank to test the whole class!
    TEST_CASE="#mainPageTest"

# Calabash Android example for BitbarSampleApp

## Run locally

Run `run_local_tests.sh` to run the test on local device.

## Create test zip

Run `create_test_zip.sh` to create BitbarSampleAppTests.zip file.

## Run in Testdroid Cloud

Testdroid Cloud Python API client must be installed. Check out https://github.com/bitbar/testdroid-api-client-python for details.

1. Create test zip file with `create_test_zip.sh`
1. Insert credentials to `run_test_in_testdroid_cloud.py` or export `TESTDROID_USERNAME` and `TESTDROID_PASSWORD`
2. Run `run_test_in_testdroid_cloud.py`


# Calabash Android example for Testdroid application

## Run locally

Run `run_local_tests.sh` to run the test on local device.
NOTE 1: When running first time, run apk resigning (see run_local_tests.sh)
NOTE 2: You can run tests using different tags or configure profiles in cucumber.yml 


## Create test zip

Run `create_test_zip.sh` to create TestdroidTests.zip file.

## Run in Testdroid Cloud

Testdroid Cloud Python API client must be installed. Check out https://github.com/bitbar/testdroid-api-client-python for details.

1. Create test zip file with `create_test_zip.sh`
1. Insert credentials to `run_test_in_testdroid_cloud.py` or export `TESTDROID_USERNAME` and `TESTDROID_PASSWORD`
2. Run `run_test_in_testdroid_cloud.py`

Sample app / project to demonstrate Detox in Bitbar cloud. Project is based on `demo-react-native` example from Wix/detox repo:
https://github.com/wix/detox/tree/master/examples/demo-react-native

Note that only Android works on real devices at the moment (android 5.0 and up), iOS can only be run with simulators.

Detox
-------------


Install (with Homebrew) (for local use / test developement)
-------------

source: https://github.com/wix/detox/blob/master/docs/Introduction.GettingStarted.md

	- For simulator (iOS)
	Install appleSimUtils:

	1. brew tap wix/brew
	2. brew install applesimutils

	Install Detox command line tools (detox-cli)
	1. npm install -g detox-cli



Build project and run test locally in short
-------------------- 


	1. clone repo, go to detox/sample-react-native-bitbar -folder
	
	2. Install dependencies
 		- `npm install`
	
	3. Start detox server (for Android real device)
		- `"${PWD}/node_modules/.bin/detox" run-server &`
	
	4. Connect Android device to detox server port
		- `adb reverse tcp:8099 tcp:8099` 
	
	5. Build app
		- change device id in package.json `android.device.release.local` configuration
		- (Android) `"${PWD}/node_modules/.bin/detox" build --configuration android.device.release.local`
		- (iOS) `"${PWD}/node_modules/.bin/detox" build --configuration ios.sim.release`
	
	6. Run test
		- (Android) `"${PWD}/node_modules/.bin/detox" test --configuration android.device.release.local`
		- (iOS) `"${PWD}/node_modules/.bin/detox" test --configuration ios.sim.release`



How to make `demo-react-native` project run on Bitbar cloud (Android)
-----------------------------------------------------

modified content to add to vanilla project (`demo-react-native` example) is highlighted.


**add to package.json:**

mocha-jenkins-reporter:
for test result xml creation.

<pre>
"devDependencies": {
    "detox": "^7.2.0",
    "mocha": "^4.0.1",
    <b>"mocha-jenkins-reporter": "^0.3.10"</b>
  },
</pre>


build configuration for Android real device:

device type:

<pre>
"type": "android.<b>attached</b>" = real device
"type": "android.<b>emulator</b>" = emulator
</pre>


address to connect the device (with sessionId):

```
"session": {
          "server": "ws://localhost:8099",
          "sessionId": "test"
        }
```

<pre>
"detox": {
    "test-runner": "mocha",
    "specs": "e2e",
    "runner-config": "e2e/mocha.opts",
    "configurations": {
      "android.emu.debug": {
        "binaryPath": "android/app/build/outputs/apk/debug/app-debug.apk",
        "build": "pushd android && ./gradlew assembleDebug assembleAndroidTest -DtestBuildType=debug && popd",
        "type": "android.emulator",
        "name": "Nexus_5X_API_24_-_GPlay"
      },
      "android.emu.release": {
        "binaryPath": "android/app/build/outputs/apk/release/app-release.apk",
        "build": "pushd android && ./gradlew assembleRelease assembleAndroidTest -DtestBuildType=release && popd",
        "type": "android.emulator",
        "name": "Nexus_5X_API_24_-_GPlay"
      }<b>,
      "android.device.release": {
        "binaryPath": "android/app/build/outputs/apk/release/app-release.apk",
        "build": "pushd android && ./gradlew assembleRelease assembleAndroidTest -DtestBuildType=release && popd",
        "session": {
          "server": "ws://localhost:8099",
          "sessionId": "test"
        },
        "type": "android.attached",
        "name": "ADD_DEVICE_ID_HERE"
      }"</b>
</pre>


note:
`"name": "ADD_DEVICE_ID_HERE"`
value for this is fetched from `run-tests-android.sh` file and if it is changed manually here it will stop working. 
For local machine runs, add a new configuration and use it for local runs (just copy "android.device.release" block and rename it "android.device.release.local" or something)


**e2e/mocha.opts:**

<pre>
--recursive
--timeout 60000
--bail
<b>--reporter mocha-jenkins-reporter
--reporter-options junit_report_path=test-report.xml</b>
</pre>

`--bail` makes all tests to fail (not run) when a test fails, to continue running tests after a failure, remove it from mocha.opts.


**run-tests.sh:**

cloud expects to see this file included in test files, contents of it will replaced with "run-tests-android.sh" (use "zip-test-files-android.sh" script)

**run-tests-android.sh:**

screenshots will be stored in project root/screenshots folder

```
screenshots folder creation:
export SCREENSHOTSFOLDER=$PWD/screenshots
rm -rf "$SCREENSHOTSFOLDER"
mkdir -p "$SCREENSHOTSFOLDER"
```

<pre>
install dependencies:
<b>npm install</b>

launch detox server:
<b>"${PWD}/node_modules/.bin/detox" run-server &</b>

connect device to detox server port:
<b>adb reverse tcp:8099 tcp:8099</b>

pass device id to package.json:
<b>sed -i.bu "s/ADD_DEVICE_ID_HERE/$UDID/"       package.json</b>

run detox test:
<b>"${PWD}/node_modules/.bin/detox" test --configuration android.device.release --loglevel verbose > detox.log 2>&1</b>
</pre>


when the project is built, apks are in this location:
`android/app/build/outputs/apk/`

if modifications to tests are made, project needs to be rebuilt with this command (locally):
`"${PWD}/node_modules/.bin/detox" build --configuration android.device.release`
(use `release` build, debug build needs "react-native packager" running at the machine and it is not configured in this sample project)


How to create an Android cloud test run:
-------------------------------

- use `"zip-test-files-android.sh"` script to create a test package to upload to Bitbar cloud

- create "Appium Android server side" project (test does not use Appium, no detox type project yet available)

- upload apk-file to the cloud project (apk can be whatever because this uploaded apk is a dummy apk just to make the cloud happy (the apk will be installed on the device so it must be a working apk but it is not used in testing))

- upload `"android-test-files.zip"` zip-file created with "zip-test-files-android.sh" script to the cloud project



How to make `demo-react-native` project run on Bitbar cloud (iOS)
-----------------------------------------------------

iOS runs will be simulator runs, not real device. Device name must be manually set in package.json:


<pre>
{
      "ios.sim.release": {
        "binaryPath": "ios/build/Build/Products/Release-iphonesimulator/sampleproject.app",
        "build": "export RCT_NO_LAUNCH_PACKAGER=true && xcodebuild -project ios/sampleproject.xcodeproj -scheme sampleproject -configuration Release -sdk iphonesimula$
        "type": "ios.simulator",
         <b>"name": "iPhone 7 Plus"</b>
      }
</pre>


when the project is built (release), app will be in this location:
`ios/build/Build/Products/Release-iphonesimulator/sampleproject.app`

if modifications to tests are made, project needs to be rebuilt with this command (locally):
`"${PWD}/node_modules/.bin/detox" build --configuration ios.sim.release`
(use `release` build, debug build needs "react-native packager" running at the machine and it is not configured in this sample project)


How to create an iOS simulator cloud test run:
-------------------------------

- use `"zip-test-files-ios.sh"` script to create a test package to upload to Bitbar cloud

- create "Appium iOS server side" project (test does not use Appium, no detox type project yet available)

- upload ipa-file to the cloud project (ipa can be whatever because this uploaded ipa is a dummy ipa just to make the cloud happy (the ipa will be installed on the device so it must be a working ipa but it is not used in testing))

- upload `"ios-test-files.zip"` zip-file created with "zip-test-files-ios.sh" script to the cloud project
## Example Test Apps

These apps are meant to be used with Testdroid sample tests also located in this repository. The three available apps are:

* *BitbarIOSSAmple.ipa* - example native mobile app for testing with iOS devices

* *BitbarSampleApp.apk* - example native mobile app for testing with Android devices

* *Testdroid.apk* - example hybrid application to test hybrid testing on Android devices

## Testdroid Sample
##### Testdroid sample Android App used as base to demo testing frameworks
**Note:**
Use Android Studio
Appium Sample in Java
=====================

This folder includes sample Appium tests using Java for Android and iOS, which can be run in [Bitbar Cloud](https://cloud.bitbar.com/).

This example can be run either using client side execution or server side execution. To find more information about these possibilities, visit <http://docs.bitbar.com/testing/appium/>

# Client Side Test Execution
## Prerequisites
1. Install Java
	- Currently the example project is targeting Java 1.7. To change that, modify the target and source field in pom.xml

	```
	<plugin>
		<groupId>org.apache.maven.plugins</groupId>
		<artifactId>maven-compiler-plugin</artifactId>
		<version>3.6.0</version>
		<configuration>
			<source>1.7</source>
			<target>1.7</target>
		</configuration>
	</plugin>
	```
2. Install Maven
	-	<http://maven.apache.org/>

## Android
Download Sample Application [BitbarSampleApp.apk](https://github.com/bitbar/testdroid-samples/blob/master/apps/builds/BitbarSampleApp.apk)

Run the following command in the root directory of the project:

```
mvn clean test \
-Dtest=AndroidAppiumExampleTest \
-DexecutionType=clientside \
-DapiKey=<your_bitbar_apiKey> \
-DapplicationPath=</path/to/BitbarSampleApp.apk>
```

in which

- \<your\_bitbar\_apiKey\> is your apiKey to Bitbar cloud. The apiKey is available under 'My account' in [Bitbar cloud](https://cloud.bitbar.com/).
- \</path/to/BitbarSampleApp.apk\> is the path to the downloaded sample application



## iOS
Download Sample Application  [BitbarIOSSample.ipa](https://github.com/bitbar/testdroid-samples/blob/master/apps/builds/BitbarIOSSample.ipa)

Run the following command in the root directory of the project:

```
mvn clean test \
-Dtest=IosAppiumExampleTest \
-DexecutionType=clientside \
-DapiKey=<your_bitbar_apiKey> \
-DapplicationPath=</path/to/BitbarIOSSample.ipa>
```

in which

- \<your\_bitbar\_apiKey\> is your apiKey. The apiKey is available under 'My account' in [Bitbar Cloud](https://cloud.bitbar.com/).
- \</path/to/BitbarIOSSample.ipa\> is the path to the downloaded sample application

## Notes
### applicationPath-argument
The applicationPath-argument is only required if the application has not yet been uploaded to Bitbar cloud project. When the applicationPath-argument is provided, the application will be automatically uploaded to Bitbar cloud before the actual test execution starts. If the application has already been uploaded, you can omit the parameter. In this case Bitbar cloud will use the latest application that has been uploaded.

## Upload Test Results
When using Client Side test execution, the test results have to be uploaded to Bitbar in order for it to correctly visualize the test run's success and test cases that have been run.

### OSX, Linux and Windows with Cygwin
On OSX, Linux and Windows machines with Cygwin this process can be automated by running the <i>run_client_side_test_and_export_results.sh</i> script. When this script is used, it replaces the "mvn clean test" part of the test execution command. For example for android you could run it as follows:

```
./run_client_side_test_and_export_results.sh \
-Dtest=AndroidAppiumExampleTest \
-DexecutionType=clientside \
-DapiKey=<your_bitbar_apiKey> \
-DapplicationPath=</path/to/BitbarSampleApp.apk>
```

### Windows
On Windows machines not running Cygwin this process can be automated by running the <i>windows\_client\_side\_test\_and_export\_results.bat</i> script. [Curl](https://curl.haxx.se/download.html) has to be installed and in the Path in order for the .bat script to work.

```
windows_client_side_test_and_export_results.bat ^
-Dtest=AndroidAppiumExampleTest ^
-DexecutionType=clientside ^
-DapiKey=<your_bitbar_apiKey> ^
-DapplicationPath=</path/to/BitbarSampleApp.apk>
```

# Server Side Test Execution
Create a zip file containing the project, which will be uploaded to [Bitbar Cloud](https://cloud.bitbar.com/).

* On OSX/Linux machines you can just run the following command at the project's root directory:

	`./zip_project.sh` This creates a zip package called: <b>server\_side\_test\_package.zip</b>

* You can also manually zip the project's sources. You have to include at least the following files in the zip package. Note that these files have to be at the root of the zip file, i.e. not inside any additional directory.
 	* run-tests.sh
	* pom.xml
	* src/


# Project Structure

## Test Cases
This is where the (Test)Magic happens. The test logic of the example test cases is located in:

- <b>Android:</b> <i>src/test/java/com/testdroid/appium/android/sample/AndroidAppiumExampleTest.java</i>

- <b>iOS:</b> <i>src/test/java/com/testdroid/appium/ios/sample/IosAppiumExampleTest.java</i>

<b>These are the files you want to edit when testing your own application based on this template.</b>

## Session initialization

The logic related to setting up the test session is located in:

- <i>src/test/java/com/testdroid/appium/BaseTest.java</i>

This functionality is inherited by the test cases as follows:

- <b>Android:</b> BaseTest.java --> BaseAndroidTest.java --> AndroidAppiumExampleTest.java
- <b>iOS:</b> BaseTest.java --> BaseIOSTest.java --> IosAppiumExampleTest.java

<b>Most likely you won't have to edit these files at all.</b>

## Desired Capabilities
The desired capabilities are fetched from a properties-file. The properties-files are located in <i>src/test/resources/</i> and are specific to the test execution type and OS version that is under test:

- <b>Android Server Side</b>: desiredCapabilities.android.serverside.properties
- <b>Android Client Side</b>: desiredCapabilities.android.clientside.properties
- <b>iOS Server Side</b>: desiredCapabilities.ios.serverside.properties
- <b>iOS Client Side</b>: desiredCapabilities.ios.clientside.properties

The properties-files are in the following format:
```
<desired_capability_name>=<desired_capability_value>
```
The desired capabilities can be divided to Appium-specific desired capabilities (such as <i>platformName</i> and <i>deviceName</i>) and Bitbar-specific desired capabilities (such as <i>testdroid_device</i> or <i>testdroid_project</i>).

The Bitbar-specific desired capabilities have to only be defined for Client Side Test Execution.

For more information about Bitbar specific capabilites, please refer to
<http://docs.bitbar.com/testing/appium/desired-caps/>

# Helpful Resources
- [Complete list of available devices](https://cloud.bitbar.com/#public/devices)
- [Bitbar Documentation](http://docs.bitbar.com/)
# Appium Ruby Samples

Bitbar can be used to run Appium tests against real devices to test
native Android or iOS applications, hybrid (Android & iOS) or for web
testing (Safari on iOS and Chrome on Android).

You'll find here all steps you need to start running your mobile tests
against real devices in Bitbar cloud. Before continuing with
running with these scripts you should register with [Bitbar
service](https://cloud.bitbar.com/).

For more detailed guides on Appium please refer to the [documentation
online](http://appium.io/slate/en/master/?python#about-appium).

## Quick Start

* Install [Bundler](http://bundler.io/) to install all necessary gems
and dependencies.

* Install necessary gems and dependencies. Run in current directory:

    bundle install

* Update your test script (testdroid_*.rb) with necessary information
  (see below).

* Start test case run with eg.:

    rspec testdroid_android.rb

## Common Necessary Settings

There are some common settings that you need to set in all scripts
regardless of the app type that you are testing. Each testdroid_*.rb
file needs to be updated with the following values.

Here are all the values that you need to edit:

* *screen_shot_dir* - where should screenshots be stored on your local drive

* *testdroid_username* - your email that you registered with to
   Bitbar cloud.  **Rather use testdroid_apiKey.**

* *testdroid_password* - your Bitbar cloud password.  **Rather use
   testdroid_apiKey.**

* *testdroid_apiKey* - a personal unique key that allows you to
   connect to Bitbar cloud without the need to use your username
   and passwords in your tests. You can find your api key under "My
   account" in [Bitbar cloud](https://cloud.bitbar.com/) UI.

* *testdroid_project* - has a default value, but you might want to add
  your own name to this. Project name is visible in your project view
  in Bitbar cloud. Each project must have a unique name

* *testdroid_testrun* - name or number of this test run. Test run
  names can be modified even at every test run

* *testdroid_app* - should be the name of the app you uploaded to
  cloud. Eg. if you uploaded your app using a script this would look
  something like this:
  'f4660af0-10f3-46e9-932b-0622f497b0d2/Testdroid.apk' If you uploaded
  your app through the Bitbar cloud web UI, you can use here the
  value 'latest' that refers to the latest uploaded app file.

## Native iOS Specific Settings

Example script: testdroid_appiumdriver_ios.rb

To run your Appium tests against your native iOS application with real
devices you need to edit the testdroid_appiumdriver_ios.rb script.

In addition to the above mentioned Appium capabilities for iOS testing
you need set

* *bundleId* - this is your application's unique name

## Native Android Specific Settings

Example script: testdroid_android.rb

To configure this script for testing your own app, in addition to the
common settings done above, you need to change the following values.

* *appPackage* - Java package of the Android app you want to run

* *appActivity* - activity name for the Android activity you want to
  launch from your package. Typically this is the main activity.

## Web App Specific Settings

Example: testdroid_selendroid.rb and testdroid_webdriver_ios.rb

For a more complete explanation on testing hybrid application take a
look at Appium
[documentation](https://github.com/appium/appium/blob/master/docs/en/advanced-concepts/hybrid.md).


## Tips

* To run tests against your previously uploaded app you can simply set
  your *testdroid_app* desired capability value to 'latest'


* To find available free devices in Bitbar cloud, you can use this Ruby [tool](https://github.com/bootstraponline/testdroid_device_finder)

## License

See the
[LICENSE](https://github.com/bitbar/testdroid-samples/blob/master/LICENSE)
file.
# Nightwatch Testdroid Example

## Client Side Test Execution
### Setup
* Install Gulp

	```
	$ npm install -g gulp
	```

* Install NPM Dependencies

	```
	$ npm install
	```
    
* Add your apiKey to ./.credentials.json

   Create a file called ".credentials.json" in the project's root and add your testdroid apiKey to it as described below:
	
	    {
	        "apiKey": "YOUR_TESTDROID_CLOUD_APIKEY"
	    }


* Modify the nightwatch.json-file according to your project

### Run the test 

* To run the test on iOS

	```
	$ gulp ios
	```

* To run the test on Android
	
	```
	$ gulp android
	```

## Server Side Test Execution
### Setup
* Create a zip file to be uploaded to Testdroid

	* If you have Gulp installed, run the following command at the project's root folder:
		
		```
		$ gulp zip
		```
		This creates a zip-file of the project to the "dist"-folder.
	* Zip the project manually

### Run the test
On Testdroid cloud

* Create an Appium server side project
* Create a new testrun in new server side project
* Upload tested application (apk/ipa) through the “Application” step
	* When doing web-testing as in this example, you can upload any application as it will not be used. You can, for example, download an application from here :
	https://github.com/bitbar/testdroid-samples/tree/master/apps/builds
* Upload the zip with scripts through the “Upload test file” step
* Choose device group to use or create a new group for this run
* Start testrun



# Bitbar Appium Sample


The capabilities has been set to run tests for Bitbar Sample Android
app. Before running tests modify Tests.cs and
 replace
TESTDROID_USERNAME and TESTDROID_PASSWORD with your user
credentials. Set the SCREENSHOT_FOLDER to an existing directory on
your system.

**Note:** Instead of using *testdroid_username* and
  *testdroid_password* desired capabilities to identify to Bitbar
  Cloud you should rather use *testdroid_apiKey*. Your personal apiKey is
  found in cloud.bitbar.com under 'My account'.


#### Windows

Launch the AppiumTest.sln on Visual Studio and make sure that NUnit Test Adapter is installed through the Extension Manager. Use Test Explorer to run the test.

#### UNIX

### Download dependencies

`nuget install Test123/packages.config -OutputDirectory packages`

### Build Test Package

`xbuild`

### Run tests
`nunit-console Test123/bin/Debug/TestdroidAndroidSample.dll`


# Appium Python Samples

Bitbar can be used to run Appium tests against real devices to test
native Android or iOS applications, hybrid (Android & iOS) or for web
testing (Safari on iOS and Chrome on Android).

You'll find here all steps you need to start running your mobile tests
against real devices in Bitbar cloud. Before continuing with running with
these scripts you should register with [Bitbar service](https://cloud.bitbar.com/).

For more detailed guides on Appium please refer to their
[documentation
online](http://appium.io/slate/en/master/?python#about-appium).

# Uploading Your App To Cloud

Uploading an app is easiest using the `upload.py` script and using
apiKey identification. The apiKey is found under "My Account" in
Bitbar cloud. For the upload to be successful the full path to the
app (apk or ipa) needs to be provided.

If no app is provided on command line, then the Bitbar Sample Android app is
uploaded.

```bash
$ python upload.py -h
usage: upload.py [-h] [-k APIKEY] [-a APP_PATH] [-u URL]

Upload a mobile app to Bitbar cloud and get a handle to it

optional arguments:
  -h, --help            show this help message and exit
  -k APIKEY, --apikey APIKEY
                        User's apiKey to identify to cloud, or set environment
                        variable TESTDROID_APIKEY
  -a APP_PATH, --app_path APP_PATH
                        Path to app to upload or set environment variable
                        TESTDROID_APP_PATH. Current value is:
                        '../../../apps/builds/Testdroid.apk'
  -u URL, --url URL     Bitbar cloud url to upload app or set environment
                        variable TESTDROID_UPLOAD_URL. Current value is:
                        'https://appium.bitbar.com/upload'
```

The below example shows how to upload a hybrid Android demo app to Bitbar Cloud.

```bash
$ python upload.py -k xg8x...YXto -a ../../../apps/builds/Testdroid.apk
Filename to use in Bitbar capabilities in your test: 719f52c4-43c2-4c25-b91b-08884f049d3a/Testdroid.apk
```

The response message provides the application's cloud file name that
is the path to use with `testdroid_app` capability. From the above
example the path to store is:
'719f52c4-43c2-4c25-b90b-08884f049d3a/Testdroid.apk'.


# Common Settings in Example Tests

There are some common settings needed to run any of the example tests,
regardless of the app type being tested. Each `testdroid_*.py` file
needs to have the following values set as environment variables or set
in the files. Values can also be given as command line parameters to
`run-test.py` script.

Common values used in tests:

* *screenshot_dir* - where should screenshots be stored on your local drive

* *testdroid_username* - your email that you registered with to
   Bitbar cloud.  **Rather use testdroid_apiKey.**

* *testdroid_password* - your Bitbar cloud password. **Rather use
   testdroid_apiKey.**

* *testdroid_apiKey* - a personal unique key allowing you to connect
   to Bitbar cloud without using username and passwords in
   tests. Api key is found under "My account" in [Bitbar cloud](https://cloud.bitbar.com/) UI.

* *testdroid_project* - the project name in Bitbar cloud. Each
  project's name is unique. A project's name can be modified later on if needed.

* *testdroid_testrun* - name of this test run inside of
  `testdroid_project`. Each test run can have the same name, but it is
  recommended to set it dynamically (e.g. with timestamp or device
  name). If no test run name is given, the system automatically names
  it in "Test Run x".

* *testdroid_app* - name of the app uploaded using `upload.py`
  script. Example filename could be
  'f4660af0-10f4-46e9-932b-0622f497b0d2/Testdroid.apk' To rerun using
  last uploaded app testdroid_app can be set to *latest*

## Example Run

```bash
$ python run-test.py -k xYY5...PeOA6 -s /tmp/screens/ -p "iOS" -t testdroid_ios -a "latest"
testSample (testdroid_ios.TestdroidIOS) ... Searching Available Free iOS Device...
Found device 'Apple iPad Mini A1432 9.2.1'

Starting Appium test using device 'Apple iPad Mini A1432 9.2.1'
15:59:00: WebDriver request initiated. Waiting for response, this typically takes 2-3 mins
15:59:58: WebDriver response received
15:59:58: view1: Finding buttons
15:59:59: view1: Clicking button [0] - RadioButton 1
16:00:00: view1: Typing in textfield[0]: Testdroid user
16:00:08: view1: Tapping at position (384, 0.95) - Estimated position of SpaceBar
16:00:10: view1: Taking screenshot screenshot1.png
16:00:14: view1: Hiding Keyboard
16:00:17: view1: Taking screenshot screenshot2.png
16:00:21: view1: Clicking button[6] - OK  Button
16:00:22: view2: Taking screenshot screenshot3.png
16:00:26: view2: Finding buttons
16:00:28: view2: Clicking button[0] - Back/OK button
16:00:29: view1: Finding buttons
16:00:30: view1: Clicking button[2] - RadioButton 2
16:00:31: view1: Clicking button[6] - OK Button
16:00:32: view1: Taking screenshot screenshot4.png
16:00:36: view1: Sleeping 3 before quitting webdriver.
16:00:39: Quitting
ok

```

## Native iOS Example

Example script: `testdroid_ios.py`

To run iOS native app tests additional parameter is required to be provided:

* **bundleId** - this is your application's unique name

```bash
$ python run-test.py -k xYY5...PeOA6 -s /tmp/screens/ -p "iOS" -r `date +%R` -a "latest" --bundle_id "com.bitbar.testdroid.BitbarIOSSample" -t testdroid_ios  
```

This parameter is not needed if running against the sample BitbarIOSSample.ipa application, as it's set inside of the sample script.


## Native Android Example

Example script: `testdroid_android.py`

To run an Appium test against a native Android application Appium needs to the
following additional information:

* **app_package** - Java package of the Android app you want to run

* **app_activity** - activity name for the Android activity you want to
  launch from your package. Typically this is the main activity.

For running the sample applications and tests these do not need to be set as they are set inside of the sample scripts if no parameter is given.

```bash
python run-test.py -k xYY5...PeOA6 -s /tmp/screens -a 830571c8-51f1-4cd1-ad91-82e76c00a1b0/BitbarSampleApp.apk -p "Android Native" -r  `date +%R` -t testdroid_android
```

## Hybrid Android Specific Settings

Example: `testdroid_android_hybrid.py`

Additional parameters needed to run a hybrid app:

* **app_package** - Java package of the Android app you want to run

* **app_activity** - activity name for the Android activity you want to
  launch from your package. Typically this is the main activity.

The above parameters are already set into the test scripts, so they are not mandatory for the sample tests. For other apps they are.

```bash
python run-test.py -k xYY5...PeOA6 -s /tmp/screens/ -t testdroid_android_hybrid -p "Android Hybrid"  -r `date +%R` --app b9608704-b55d-4b71-83d4-d8027c67b49a/Testdroid.apk
```

## Safari Browser Testing

Does not need any specific settings.

Example: `testdroid_safari.py`

```bash
python run-test.py -k xYY5hc8PXAXsBBd1G3ijnb18wlqPeOA6 -s /tmp/screens/ -t testdroid_safari -p "Safari browser"  -r `date +%R`
```

##  Chrome Browser Testing

Does not need any special settings.

Example: `testdroid_chrome.py`

```bash
python run-test.py -k xYY5hc8PXAXsBBd1G3ijnb18wlqPeOA6 -s /tmp/screens/ -t testdroid_chrome -p "Chrome browser"  -r `date +%R`
```

# License

See the [LICENSE](https://github.com/bitbar/testdroid-samples/blob/master/LICENSE) file.
Appium Sample in Ruby
=====================

This folder includes sample Appium tests using Ruby for Android and iOS, which can be run in [Bitbar Cloud](https://cloud.bitbar.com/).


# Server Side Test Execution
Create a zip file containing the project, which will be uploaded to [Bitbar Cloud](https://cloud.bitbar.com/).

* On OSX/Linux machines you can just run the following command at the project's root directory:

    `./createAndroidZip.sh` This creates a zip package called: <b>android-test.zip</b>
    `./createiOSZip.sh` This creates a zip package called: <b>ios-test.zip</b>

* You can also manually zip the project's sources. You have to include at least the following files in the zip package. Note that these files have to be at the root of the zip file, i.e. not inside any additional directory.
    * run-tests.sh
    * Gemfile
    * setup_appium.rb
    * android_sample_spec.rb / ios_sample_spec.rb

## Quick Start

* Install [Bundler](http://bundler.io/) to install all necessary gems
and dependencies.

* Install necessary gems and dependencies. Run in current directory:

bundle install

* Update your test script (setup_appium.rb) with necessary information
(see below).

* Start test case run with eg.:

rspec android_sample.rb

or run following command at the project's root directory:
`./run-tests_android.sh`
`./run-tests_ios.sh`

## Common Necessary Settings

There are some common settings that you need to set in all scripts
regardless of the app type that you are testing.

Here are all the values that you need to edit:

* *app_file_android* - your android app.
* *app_file_ios* - your android app.

## Native iOS Specific Settings

To configure this script for testing your own app edit the setup_appium.rb script,
in addition to the common settings done above, you need to change the following values.

In addition to the above mentioned Appium capabilities for iOS testing
you need set

* *bundleId* - this is your application's unique name

## Native Android Specific Settings

To configure this script for testing your own app edit the setup_appium.rb script,
in addition to the common settings done above, you need to change the following values.

* *appPackage* - Java package of the Android app you want to run

* *appActivity* - activity name for the Android activity you want to
launch from your package. Typically this is the main activity.

# Helpful Resources
- [Complete list of available devices](https://cloud.bitbar.com/#public/devices)
- [Bitbar Documentation](http://docs.bitbar.com/)
Intro
=====


This folder contains a sample Appium server side test case for Android
and iOS environments. To read more about server and client Appium runs
in Bitbar Cloud, check our online documentation from `http://docs.bitbar.com/testing/appium/index.html`.

Folder Content
--------------

This folder contains the following files:

* `TestdroidAppiumTest.py` and `BitbarSampleAppTest.py` are the actual
  test files written in Python. The test execution uses Python's
  unittest framework for test execution.

* `requirements.txt` lists the required Python packagesthat need to be
  installed for the test to be executable, eg. AppiumPythonClient.

* `run-tests_ios.sh` and `run-tests_android.sh` are environment
  specific Bash shell scripts that need to be renamed to
  `run-tests.sh` so it will be executed by Bitbar Cloud when the test
  is started on some device. Depending on environment you are testing,
  you'll need to use the iOS or Android version of this script.

* `create-zip.sh` is a script that packages the test files into a zip
  file. The output of this file needs to be uploaded to your server
  side test run. You need to provide parameter `ios` or `android`
  depending which environment you want to use.

  # Jenkins with Bitbar plugin

This is a simple Dockerfile for starting a Jenkins instance with the Bitbar cloud plugin and API client installed.

1. `docker build --tag bitbar-jenkins .`
1. `docker run -p 8080:8080 -p 50000:50000 -v jenkins_home:/var/jenkins_home jenkins/jenkins:lts`
1. Go to <http://localhost:8080/> and complete the wizard
    1. Install suggested plugins
    1. Create admin user
    1. Create your build# XCTEST Example Project

Basic calculator app for iOS done with swift. Calculator can do addition and subtraction operations.

Project includes examples of unit tests written using XCTest framework.

## Building the IPA

Guide on how to build the IPA is available at Bitbar Testing [online documentation](http://docs.bitbar.com/testing/xcode/ipa/).

## Test Packaging

To run the XCTests in Bitbar Testing cloud, the tests need to be packaged into a zip-package.
The guide in how to do this is [available online](http://docs.bitbar.com/testing/xcode/xctest/).
