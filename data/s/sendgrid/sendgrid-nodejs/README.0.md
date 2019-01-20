# Introduction

This is an example project for using a Docker container as a [SendGrid](https://sendgrid.com) [inbound parse email](https://sendgrid.com/docs/for-developers/parsing-email/setting-up-the-inbound-parse-webhook/) webhooks and [event webhooks](https://sendgrid.com/docs/for-developers/tracking-events/getting-started-event-webhook/)

# Prerequisites

* [Docker CE 18](https://www.docker.com/get-started)
* (Optional for development) A local Kubernetes installation
* SendGrid Account with inbound parse enabled to send form data (default)
    * [Setup Inbound Parse Webhook](https://sendgrid.com/docs/for-developers/parsing-email/setting-up-the-inbound-parse-webhook/)
* SendGrid Account with event webhooks enabled
    * [Getting Started with Event Webhook](https://sendgrid.com/docs/for-developers/tracking-events/getting-started-event-webhook/)
* [Ngrok](https://ngrok.com/) or Internet accessible URL

# Usage Locally (aka for Development)

* `mkdir <project>`
* `cd <project>`
* `git clone https://github.com/sendgrid/sendgrid-nodejs.git`
* `cp -R sendgrid-nodejs/examples/inbound-parse-docker/* .`
* `rm -rf sendgrid-nodejs/`
* Build the container: `docker-compose build`
* Run the container: `docker-compose up`
* (Optional to save your self both commands above) Build & Run the container: `docker-compose up --build`
* Run ngrok: `ngrok http 3000`
* For inbound parse:
  * Create an entry in the [Settings > Inbound Parse](https://app.sendgrid.com/settings/parse) with the ngrok URL.  Use the `https` ngrok entry.
  * Send an email to your inbound parse email address.
* For event webhook
  * Configure the [Settings > Mail Settings > Event Notification](https://app.sendgrid.com/settings/mail_settings)

NOTE: ngrok has a "replay" feature so you don't have to keep sending emails to yourself.  You can access that when ngrok is running at [http://127.0.0.1:4040/inspect/http](http://127.0.0.1:4040/inspect/http)

# Modifying the application

At the moment, the `app.js` only prints data to the console.  You can extend this project by adding more business logic to the `/parse_webhook` or `/event_webhook` routes, contained in the [routes/inbound-parse.js](routes/inbound-parse.js) and [routes/events.js](routes/events.js).

## A note on processing events

### Inbound Parse Webhook

The [routes/inbound-parse.js](routes/inbound-parse.js) route uses the [express-formidable](https://github.com/utatti/express-formidable) middleware to process the form data sent by SendGrid's Inbound Parse Webhook.  

The events are available in the `/parse_webhook` route in the `req.fields` object.  The [app.js](app.js) contains logging statements for the elements that are available to you.  It may be useful to review the [example-webhook-payload.txt](example-webhook-payload.txt) for what the form data looks like when extending this application.

Attachments: `express-formidable` automatically decodes and stores the images to the `/tmp` directory in the container.  This is configurable by passing a configuration object to the middleware:

```js
app.use(formidable({
  encoding: 'utf-8',
  uploadDir: '/my/dir',
  multiples: true, // req.files to be arrays of files
});
```

### Events Webhook

The [routes/events.js](routes/events.js) route receives data in JSON format.

Additionally, the [docker-compose](docker-compose.yml) has a volume mapping commented out if you'd prefer to store them in persistent storage outside of the container.

# Deployment to Kubernetes

* In order for Kubernetes to use the container described in this project, the container must be built and stored in a container registry.  You can choose to use a private registry in your cloud provider or a public registry (e.g., Docker Hub).  You can also run a development environment of Kubernetes via [Docker for Mac or Windows](https://www.docker.com/get-started)
* In this project, the [Kubernetes (k8s) manifest](k8s/inbound-parse.yml) uses the `imagePullPolicy: IfNotPresent` to pull from a local registry on the dev machine running Kubernetes as part of Docker.  If you were deploying to Google Cloud, for example, you should disable that option.
* `kubectl` is used to deploy.  You should already have a working `kubectl context`.  From the root of the project execute: `kubectl apply -f k8s/inbound-parse.yml`

# Resources

* [Kubernetes Developer Docs](https://kubernetes.io/docs/user-journeys/users/application-developer/foundational/)
* [Install Kubernetes UI in Docker for Windows/Mac](https://www.ntweekly.com/2018/05/25/deploy-kubernetes-web-ui-dashboard-docker-windows/)
* [Deploy and Expose Apps in Kubernetes](https://www.ntweekly.com/2018/06/10/deploy-expose-applications-kubernetes-docker-windows/)
* [Download Docker](https://www.docker.com/get-started)


# License

See [LICENSE](LICENSE)

This documentation provides examples for specific SendGrid v3 API use cases. Please [open an issue](https://github.com/sendgrid/sendgrid-nodejs/issues) or make a pull request for any email use cases you would like us to document here. Thank you!

# Email Use Cases
* [Send a Single Email to a Single Recipient](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/single-email-single-recipient.md)
* [Send a Single Email to Multiple Recipients](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/single-email-multiple-recipients.md)
* [Send Multiple Emails to Multiple Recipients](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/multiple-emails-multiple-recipients.md)
* [CC, BCC and Reply To](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/cc-bcc-reply-to.md)
* [Flexible Email Address Fields](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/flexible-address-fields.md)
* [Handling Success/Failure/Errors](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/success-failure-errors.md)
* [Show Email Activity](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/email-activity.md)
* [Advanced Usage](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/advanced.md)
  * [Transactional Templates](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/transactional-templates.md)
  * [Legacy Transactional Templates](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/transactional-legacy-templates.md)
  * [Attachments](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/attachments.md)
  * [Customization Per Recipient](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/customization.md)
  * [Manually Providing Content](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/manual-content.md)
  * [Specifying Time to Send At](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/time-to-send.md)
  * [Specifying Custom Headers](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/custom-headers.md)
  * [Specifying Categories](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/categories.md)
  * [Kitchen Sink - an example with all settings used](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/kitchen-sink.md)

# Non-mail Use Cases
* [How to Setup a Domain Whitelabel](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/domain-white-label.md)
* [How to View Email Statistics](https://github.com/sendgrid/sendgrid-nodejs/blob/master/use-cases/email-stats.md)
# Email Subscription Widget with Double Opt-In

Note: This is not an officially supported SendGrid library

This is an open source repository to add a flexible email subscription widget, like the one shown below, to any website using [SendGrid](https://sendgrid.com/). After following these directions, you'll be able to add a snippet of HTML to any website that will collect email addresses for your app or business. This widget utilizes [double opt-in](https://sendgrid.com/docs/Glossary/opt_in_email.html) functionality, which means users must confirm their email addresses by clicking an email that is automatically sent to their provided email address.

![alt text](https://github.com/devchas/sendgrid_subscription_widget/blob/master/server/static/sample-form.png "Sample Form")

## Requirements

Before following these instructions, you must:
* Have a SendGrid account - [sign up here](https://sendgrid.com/pricing/)
* Sign up for a [free Heroku account](https://signup.heroku.com/)

## Instructions

### Initial SendGrid Set-up - Create API Key & Contact List
To begin, you will first need to create an API key on SendGrid's website. Once logged in, go to Settings -> API Keys, and click the blue button in the top right corner of the website.  You will be creating a General API key, which must have *Full Access* to *Mail Send* and *Marketing Campaigns*.  Keep this API key in a *safe* and *private* location.  You will need it later.

### Fork this Repository to Create Your Copy
If you are unfamiliar with Github, just click the button that reads *Fork* in the top right of this page. Doing this will provide you with your copy.  You'll need to change a few basic settings in your copy.

### Deploy to Heroku

**Make sure you Fork this repository before clicking the Deploy to Heroku button below**

Click the button below to deploy this app to the Heroku account you created earlier.  Once complete, locate the URL of your app.  You will need this for the following step.

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

Once the app is deployed, you may want to connect your forked Github repository to your Heroku app for easy deployment. You can do this by navigating to the *Deploy* tab within your app on Heroku and following the instructions.

### Update Your App Settings in Your Forked Repository on Github
Navigate to settings.js in your forked copy of the repository and change each of the four variables to the appropriate values. You can find your app's URL by opening your app or navigating to the *Activity* tab in Heroku and scrolling to the middle of the page to the domains section. See the example below.

```javascript
exports.url = 'https://your_heroku_app_name.herokuapp.com';
exports.senderEmail = "sender@example.com";
exports.senderName = "Sender Name";

// set 'exports.listId = null' to add contact to all contacts, but no specific list
exports.listID = 651138;

// set 'exports.templateId = null' to opt out of using a template
exports.templateId = "dbc810ec-b776-4345-b0c7-02e2bbcd2ab4"
```

#### Add Contact to a Custom Marketing List (Optional)
By default, the widget is configured to save a new contact to your master list of ALL CONTACTS. However, you may choose to save new contacts to a specified custom list as well. To do so, you must first create a new contact list by navigating to Marketing Campaigns -> Contacts, and then click the blue button in the top right corner of the page. Once the list is created, you will require the list ID.  You can find this number by navigating to the list and looking at the URL.  The list ID will be the numbers following the last forward slash.  For example, the list ID of a list with URL of https://sendgrid.com/marketing_campaigns/lists/651138 would be 651138. Once you have created a new list, change the value of exports.listId to the ID of that marketing list.  This value is null by default.

#### Use a Transactional Template (Optional)
You may also send your confirmation email using [transactional email templates](https://sendgrid.com/solutions/transactional-email-templates/) to give your email a more professional look and feel.  To do so, you must first create a template by following the steps provided in [this guide](https://sendgrid.com/docs/User_Guide/Transactional_Templates/index.html). Once you have created a custom transactional email template, change the value of the exports.templateId to the ID of the template you created. If you choose to use templates, **you must include a substitution tag named "link_insert"**. This will be substituted with the link that signs up a user in the double opt-in process. (Example template below)

![alt text](https://github.com/devchas/sendgrid_subscription_widget/blob/master/server/static/template.png "Transactional Email Template")

#### Edit the Form with Your Custom URL
Navigate to the index.html file (server -> static -> index.html) and change the action in the form to reflect your app's URL. Remember to leave "/confirmEmail" at the end. The text in this file is what you will embed in your website. See below for an example.

```html
<form action="https://your_heroku_app_name.herokuapp.com/confirmEmail" method="post">
	<fieldset>
		<legend>Enter Your Information</legend>
		<label for="email">Email:</label>
		<input type="text" name="email" placeholder="hello@example.com" /><br>
		<label for="first_name">First Name:</label>		
		<input type="text" name="first_name" placeholder="John" /><br>
		<label for="last_name">Last Name:</label>
		<input type="text" name="last_name" placeholder="Doe" /><br>
		<button type="submit" value="Submit" />SIGN UP</button>
	</fieldset>
</form>
```

*Remember to always re-deploy your app after making any changes.*

### Add API Key as Environmental Variable on Heroku
Next, configure your API key as an environmental variable, which can be done either through Heroku's user interface or the Heroku CLI as shown in [these directions](https://devcenter.heroku.com/articles/config-vars). Updating the environment variable in your Heroku account can be done by logging into your Heroku account, navigate to your newly deployed app, and clicking settings. Inside the settings page, you will see an option to "Reveal Config Vars".  You must name your variable holding your API key *SG_API_KEY*.

### Enable Event Webhook
The final step is to enable the event webhook on your SendGrid account. This will allow the opt-in component of the signup to function correctly. To set up an event webhook, navigate to Settings -> Mail Settings, and then click on *Event Notification*.  

Make sure the toggle in the top left of that section is set to *ON*. Click edit. Enter the root URL of your Heroku app + '/signup'. The following is an example URL: https://your_heroku_app_name.herokuapp.com/signup. 

For the types of events to receive, make sure to select only *Clicked*. Then, click the blue checkbox in the top right corner of the section to save changes.


### Test Your Widget
To quickly test that your subscription widget is working correctly, you may navigate to the root URL of your Heroku app and enter an email that you have access to. If everything is working, you should receive an email with a link to confirm your subscription. Upon clicking this link, the email should be added to the SendGrid contact list you created earlier.

## Usage and Customization

### Usage

To use this widget, once you've followed the setup steps above, drop all of the text from the index.html file you altered earlier into any website.

### Customization

You may change the look and feel of the form or create a new one.  The form will continue to work so long as the action is what you specified earlier, the method is a POST, and there is an input element with name *email*.  The default widget comes with three fields: 1) email, 2) first name, 3) last name.  You may remove first and/or last name if you so choose.  Also, you may change the form's styling by adjusting the CSS contained in index.html.

#### Adding New Fields
You may also add [custom fields](https://sendgrid.com/docs/User_Guide/Marketing_Campaigns/custom_fields.html) to the form to save other information about your users during the sign up process. To do so, simply add an input field with the name(s) of your custom field(s). If you add a custom field to your form that does not already exist in your SendGrid account, one will automatically be created with the name specified in the form. The example below shows a form with the custom field "favorite_color".

```html
<form action="https://your_heroku_app_name.herokuapp.com/confirmEmail" method="post">
	<fieldset>
		<legend>Enter Your Information</legend>
		<label for="email">Email:</label>
		<input type="text" name="email" placeholder="hello@example.com" /><br>
		<label for="first_name">First Name:</label>		
		<input type="text" name="first_name" placeholder="John" /><br>
		<label for="last_name">Last Name:</label>
		<input type="text" name="last_name" placeholder="Doe" /><br>
		<label for="favorite_color">Favorite Color:</label>
		<input type="text" name="favorite_color" placeholder="Blue" /><br>
		<button type="submit" value="Submit" />SIGN UP</button>
	</fieldset>
</form>
```

You may also change the look of the check-inbox.html and success.html files, both of which are located in the static folder with index.html.  These are the pages that users will be directed to upon entering their email and clicking the confirmation link, respectively.

Finally, you may change the content of the confirmation email by changing the *mailText* variable in the contact_list_controller.js file, which is located in the controllers folder. However, be sure to keep the link intact. If you choose to use a transactional email template, the template will produce the mail text, and you may ignore this step.

```javascript
mailText = "Thanks for signing up! Click <a href='" + url + "'>this link</a> \
	to sign up!  This link will be active for 24 hours."
```
 
[![BuildStatus](https://travis-ci.org/sendgrid/sendgrid-nodejs.svg?branch=master)](https://travis-ci.org/sendgrid/sendgrid-nodejs)
[![npm version](https://badge.fury.io/js/%40sendgrid%2Fclient.svg)](https://www.npmjs.com/org/sendgrid)
[![Email Notifications Badge](https://dx.sendgrid.com/badge/nodejs)](https://dx.sendgrid.com/newsletter/nodejs)

**This package is part of a monorepo, please see [this README](https://github.com/sendgrid/sendgrid-nodejs/blob/master/README.md) for details.**

To be notified when this package is updated, please subscribe to email [notifications](https://dx.sendgrid.com/newsletter/nodejs) for releases and breaking changes.

<a name="contribute"></a>
# How to Contribute

We encourage contribution to our libraries (you might even score some nifty swag), please see our [CONTRIBUTING](https://github.com/sendgrid/sendgrid-nodejs/blob/master/CONTRIBUTING.md) guide for details.

* [Feature Request](https://github.com/sendgrid/sendgrid-nodejs/tree/master/CONTRIBUTING.md#feature-request)
* [Bug Reports](https://github.com/sendgrid/sendgrid-nodejs/tree/master/CONTRIBUTING.md#submit-a-bug-report)
* [Improvements to the Codebase](https://github.com/sendgrid/sendgrid-nodejs/tree/master/CONTRIBUTING.md#improvements-to-the-codebase)

<a name="troubleshooting"></a>
# Troubleshooting

Please see our [troubleshooting guide](https://github.com/sendgrid/sendgrid-nodejs/blob/master/TROUBLESHOOTING.md) for common library issues.

<a name="about"></a>
# About

@sendgrid/contact-importer is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

@sendgrid/contact-importer is maintained and funded by SendGrid, Inc. The names and logos for @sendgrid/contact-importer are trademarks of SendGrid, Inc.

![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)
[![BuildStatus](https://travis-ci.org/sendgrid/sendgrid-nodejs.svg?branch=master)](https://travis-ci.org/sendgrid/sendgrid-nodejs)
[![npm version](https://badge.fury.io/js/%40sendgrid%2Fclient.svg)](https://www.npmjs.com/org/sendgrid)
[![Email Notifications Badge](https://dx.sendgrid.com/badge/nodejs)](https://dx.sendgrid.com/newsletter/nodejs)

**This package is part of a monorepo, please see [this README](https://github.com/sendgrid/sendgrid-nodejs/blob/master/README.md) for details.**

# Inbound Parse Service for the [Sendgrid Inbound Parse API](https://sendgrid.com/docs/API_Reference/Webhooks/inbound_email.html)
This package helps get you started consuming and processing [Inbound Parse](https://sendgrid.com/docs/API_Reference/Webhooks/inbound_email.html) data.

To be notified when this package is updated, please subscribe to email [notifications](https://dx.sendgrid.com/newsletter/nodejs) for releases and breaking changes.

## Prerequisites

- Node.js version 6, 7 or 8
- A SendGrid account, [sign up for free](https://sendgrid.com/free?source=sendgrid-nodejs) to send up to 40,000 emails for the first 30 days or check out [our pricing](https://sendgrid.com/pricing?source=sendgrid-nodejs).

## Obtain an API Key

Grab your API Key from the [SendGrid UI](https://app.sendgrid.com/settings/api_keys).

# Install Package

The following recommended installation requires [npm](https://npmjs.org/). If you are unfamiliar with npm, see the [npm docs](https://npmjs.org/doc/). Npm comes installed with Node.js since node version 0.8.x, therefore, you likely already have it.

```sh
npm install --save @sendgrid/inbound-mail-parser
```

You may also use [yarn](https://yarnpkg.com/en/) to install.

```sh
yarn add @sendgrid/inbound-mail-parser
```

<a name="contribute"></a>
# How to Contribute

We encourage contribution to our libraries (you might even score some nifty swag), please see our [CONTRIBUTING](https://github.com/sendgrid/sendgrid-nodejs/blob/master/CONTRIBUTING.md) guide for details.

* [Feature Request](https://github.com/sendgrid/sendgrid-nodejs/tree/master/CONTRIBUTING.md#feature-request)
* [Bug Reports](https://github.com/sendgrid/sendgrid-nodejs/tree/master/CONTRIBUTING.md#submit-a-bug-report)
* [Improvements to the Codebase](https://github.com/sendgrid/sendgrid-nodejs/tree/master/CONTRIBUTING.md#improvements-to-the-codebase)

<a name="troubleshooting"></a>
# Troubleshooting

Please see our [troubleshooting guide](https://github.com/sendgrid/sendgrid-nodejs/blob/master/TROUBLESHOOTING.md) for common library issues.

<a name="about"></a>
# About

@sendgrid/inbound-mail-parser is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

@sendgrid/inbound-mail-parser is maintained and funded by SendGrid, Inc. The names and logos for @sendgrid/inbound-mail-parser are trademarks of SendGrid, Inc.

![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)[![BuildStatus](https://travis-ci.org/sendgrid/sendgrid-nodejs.svg?branch=master)](https://travis-ci.org/sendgrid/sendgrid-nodejs)
[![npm version](https://badge.fury.io/js/%40sendgrid%2Fclient.svg)](https://www.npmjs.com/org/sendgrid)
[![Email Notifications Badge](https://dx.sendgrid.com/badge/nodejs)](https://dx.sendgrid.com/newsletter/nodejs)

**This package is part of a monorepo, please see [this README](https://github.com/sendgrid/sendgrid-nodejs/blob/master/README.md) for details.**

# Client for the Sendgrid v3 Web API
This client library is used by the other [SendGrid service packages](https://www.npmjs.com/org/sendgrid) to make requests to the [Sendgrid v3 Web API](https://sendgrid.com/docs/API_Reference/api_v3.html). You can also use it independently to make custom requests to the SendGrid v3 Web API and other HTTP APIs.

To be notified when this package is updated, please subscribe to email [notifications](https://dx.sendgrid.com/newsletter/nodejs) for releases and breaking changes.

# Installation

## Prerequisites

- Node.js version 6, 7 or 8
- A SendGrid account, [sign up for free](https://sendgrid.com/free?source=sendgrid-nodejs) to send up to 40,000 emails for the first 30 days or check out [our pricing](https://sendgrid.com/pricing?source=sendgrid-nodejs).

## Obtain an API Key

Grab your API Key from the [SendGrid UI](https://app.sendgrid.com/settings/api_keys).

## Setup Environment Variables

Do not hardcode your [SendGrid API Key](https://app.sendgrid.com/settings/api_keys) into your code. Instead, use an environment variable or some other secure means of protecting your SendGrid API Key. Following is an example of using an environment variable.

Update the development environment with your [SENDGRID_API_KEY](https://app.sendgrid.com/settings/api_keys), for example:

```bash
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
```

## Install Package

The following recommended installation requires [npm](https://npmjs.org/). If you are unfamiliar with npm, see the [npm docs](https://npmjs.org/doc/). Npm comes installed with Node.js since node version 0.8.x, therefore, you likely already have it.

```sh
npm install --save @sendgrid/client
```

You may also use [yarn](https://yarnpkg.com/en/) to install.

```sh
yarn add @sendgrid/client
```

<a name="general"></a>
## General v3 Web API Usage Example

Please see [USAGE.md](https://github.com/sendgrid/sendgrid-nodejs/blob/master/packages/client/USAGE.md) for all endpoint examples for the [SendGrid v3 Web API](https://sendgrid.com/docs/API_Reference/api_v3.html).

```js
const client = require('@sendgrid/client');
client.setApiKey(process.env.SENDGRID_API_KEY);
const request = {
  method: 'GET',
  url: '/v3/api_keys'
};
client.request(request)
.then(([response, body]) => {
  console.log(response.statusCode);
  console.log(body);
})
```

## Add a Custom Default Header
```js
client.setDefaultHeader('User-Agent', 'Some user agent string');
```

## Change Request Defaults
```js
client.setDefaultRequest('baseUrl', 'https://api.sendgrid.com/');
```

## Overwrite Promise Implementation
You can overwrite the promise implementation you want the client to use. Defaults to the ES6 `Promise`:

```js
global.Promise = require('bluebird');
```

## Instantiate Client Instances Manually
```js
const {Client} = require('@sendgrid/client');
const sgClient1 = new Client();
const sgClient2 = new Client();
sgClient1.setApiKey('KEY1');
sgClient2.setApiKey('KEY2');
```

<a name="announcements"></a>
# Announcements

All updates to this library are documented in our [CHANGELOG](https://github.com/sendgrid/sendgrid-nodejs/blob/master/CHANGELOG.md) and [releases](https://github.com/sendgrid/sendgrid-nodejs/releases). You may also subscribe to email [release notifications](https://dx.sendgrid.com/newsletter/nodejs) for releases and breaking changes.

<a name="roadmap"></a>
# Roadmap

If you are interested in the future direction of this project, please take a look at our open [issues](https://github.com/sendgrid/sendgrid-nodejs/issues) and [pull requests](https://github.com/sendgrid/sendgrid-nodejs/pulls). We would love to hear your feedback.

<a name="contribute"></a>
# How to Contribute

We encourage contribution to our libraries (you might even score some nifty swag), please see our [CONTRIBUTING](https://github.com/sendgrid/sendgrid-nodejs/blob/master/CONTRIBUTING.md) guide for details.

* [Feature Request](https://github.com/sendgrid/sendgrid-nodejs/tree/master/CONTRIBUTING.md#feature-request)
* [Bug Reports](https://github.com/sendgrid/sendgrid-nodejs/tree/master/CONTRIBUTING.md#submit-a-bug-report)
* [Improvements to the Codebase](https://github.com/sendgrid/sendgrid-nodejs/tree/master/CONTRIBUTING.md#improvements-to-the-codebase)

<a name="troubleshooting"></a>
# Troubleshooting

Please see our [troubleshooting guide](https://github.com/sendgrid/sendgrid-nodejs/blob/master/TROUBLESHOOTING.md) for common library issues.

<a name="about"></a>
# About

@sendgrid/client is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

@sendgrid/client is maintained and funded by SendGrid, Inc. The names and logos for @sendgrid/client are trademarks of SendGrid, Inc.

![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)
[![BuildStatus](https://travis-ci.org/sendgrid/sendgrid-nodejs.svg?branch=master)](https://travis-ci.org/sendgrid/sendgrid-nodejs)
[![npm version](https://badge.fury.io/js/%40sendgrid%2Fclient.svg)](https://www.npmjs.com/org/sendgrid)
[![Email Notifications Badge](https://dx.sendgrid.com/badge/nodejs)](https://dx.sendgrid.com/newsletter/nodejs)

**This package is part of a monorepo, please see [this README](https://github.com/sendgrid/sendgrid-nodejs/blob/master/README.md) for details.**

# Support classes and helpers for the Sendgrid NodeJS libraries
This is a collection of classes and helpers used internally by the
[Sendgrid NodeJS libraries](https://www.npmjs.com/org/sendgrid).

Note that not all objects represented in the Sendgrid API have helper classes assigned to them because it is not expected that developers will use these classes themselves. They are primarily for internal use and developers are expected to use the publicly exposed API in the [various endpoint services](https://www.npmjs.com/org/sendgrid).

To be notified when this package is updated, please subscribe to email [notifications](https://dx.sendgrid.com/newsletter/nodejs) for releases and breaking changes.

## Mail class
Used to compose a `Mail` object that converts itself to proper JSON for use with the [Sendgrid v3 API](https://sendgrid.com/docs/API_Reference/api_v3.html). This class supports a slightly different API to make sending emails easier in many cases by not having to deal with personalization arrays, instead offering a more straightforward interface for composing emails.

## Attachment class
Used by the inbound mail parser to compose `Attachment` objects.

## Personalization class
Used by the Mail class to compose `Personalization` objects.

## Email address
`Helper` class to represent an email address with name/email. Used by both the `Mail` and `Personalization` classes to deal with email addresses of various formats.

## Helpers
Internal helpers that mostly speak for themselves.

<a name="contribute"></a>
# How to Contribute

We encourage contribution to our libraries (you might even score some nifty swag), please see our [CONTRIBUTING](https://github.com/sendgrid/sendgrid-nodejs/blob/master/CONTRIBUTING.md) guide for details.

* [Feature Request](https://github.com/sendgrid/sendgrid-nodejs/tree/master/CONTRIBUTING.md#feature-request)
* [Bug Reports](https://github.com/sendgrid/sendgrid-nodejs/tree/master/CONTRIBUTING.md#submit-a-bug-report)
* [Improvements to the Codebase](https://github.com/sendgrid/sendgrid-nodejs/tree/master/CONTRIBUTING.md#improvements-to-the-codebase)

<a name="about"></a>
# About

@sendgrid/helpers are guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

@sendgrid/helpers are maintained and funded by SendGrid, Inc. The names and logos for @sendgrid/helpers are trademarks of SendGrid, Inc.

![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)
[![BuildStatus](https://travis-ci.org/sendgrid/sendgrid-nodejs.svg?branch=master)](https://travis-ci.org/sendgrid/sendgrid-nodejs)
[![npm version](https://badge.fury.io/js/%40sendgrid%2Fclient.svg)](https://www.npmjs.com/org/sendgrid)
[![Email Notifications Badge](https://dx.sendgrid.com/badge/nodejs)](https://dx.sendgrid.com/newsletter/nodejs)

**This package is part of a monorepo, please see [this README](https://github.com/sendgrid/sendgrid-nodejs/blob/master/README.md) for details.**

# Mail Service for the Sendgrid v3 Web API
This is a dedicated service for interaction with the mail endpoint of the [Sendgrid v3 API](https://sendgrid.com/docs/API_Reference/api_v3.html).

To be notified when this package is updated, please subscribe to email [notifications](https://dx.sendgrid.com/newsletter/nodejs) for releases and breaking changes.

# Installation

## Prerequisites

- Node.js version 6, 7 or 8
- A SendGrid account, [sign up for free](https://sendgrid.com/free?source=sendgrid-nodejs) to send up to 40,000 emails for the first 30 days or check out [our pricing](https://sendgrid.com/pricing?source=sendgrid-nodejs).

## Obtain an API Key

Grab your API Key from the [SendGrid UI](https://app.sendgrid.com/settings/api_keys).

## Setup Environment Variables

Do not hardcode your [SendGrid API Key](https://app.sendgrid.com/settings/api_keys) into your code. Instead, use an environment variable or some other secure means of protecting your SendGrid API Key. Following is an example of using an environment variable.

Update the development environment with your [SENDGRID_API_KEY](https://app.sendgrid.com/settings/api_keys), for example:

```bash
echo "export SENDGRID_API_KEY='YOUR_API_KEY'" > sendgrid.env
echo "sendgrid.env" >> .gitignore
source ./sendgrid.env
```

## Install Package

The following recommended installation requires [npm](https://npmjs.org/). If you are unfamiliar with npm, see the [npm docs](https://npmjs.org/doc/). Npm comes installed with Node.js since node version 0.8.x, therefore, you likely already have it.

```sh
npm install --save @sendgrid/mail
```

You may also use [yarn](https://yarnpkg.com/en/) to install.

```sh
yarn add @sendgrid/mail
```

<a name="quick-start"></a>
# Quick Start, Hello Email

The following is the minimum needed code to send a simple email. Use this example, and modify the `to` and `from` variables:

For more complex use cases, please see [USE_CASES.md](https://github.com/sendgrid/sendgrid-nodejs/blob/master/packages/mail/USE_CASES.md).

```js
const sgMail = require('@sendgrid/mail');
sgMail.setApiKey(process.env.SENDGRID_API_KEY);
const msg = {
  to: 'test@example.com',
  from: 'test@example.com',
  subject: 'Sending with SendGrid is Fun',
  text: 'and easy to do anywhere, even with Node.js',
  html: '<strong>and easy to do anywhere, even with Node.js</strong>',
};
sgMail.send(msg);
```

After executing the above code, you should have an email in the inbox of the recipient. You can check the status of your email [in the UI](https://app.sendgrid.com/email_activity?). Alternatively, we can post events to a URL of your choice using our [Event Webhook](https://sendgrid.com/docs/API_Reference/Webhooks/event.html). This gives you data about the events that occur as SendGrid processes your email.

<a name="troubleshooting"></a>
# Troubleshooting

Please see our [troubleshooting guide](https://github.com/sendgrid/sendgrid-nodejs/blob/master/TROUBLESHOOTING.md) for common library issues.

<a name="announcements"></a>
# Announcements

All updates to this library are documented in our [CHANGELOG](https://github.com/sendgrid/sendgrid-nodejs/blob/master/CHANGELOG.md) and [releases](https://github.com/sendgrid/sendgrid-nodejs/releases). You may also subscribe to email [release notifications](https://dx.sendgrid.com/newsletter/nodejs) for releases and breaking changes.

<a name="roadmap"></a>
# Roadmap

If you are interested in the future direction of this project, please take a look at our open [issues](https://github.com/sendgrid/sendgrid-nodejs/issues) and [pull requests](https://github.com/sendgrid/sendgrid-nodejs/pulls). We would love to hear your feedback!

<a name="contribute"></a>
# How to Contribute

We encourage contribution to our libraries (you might even score some nifty swag), please see our [CONTRIBUTING](https://github.com/sendgrid/sendgrid-nodejs/blob/master/CONTRIBUTING.md) guide for details.

* [Feature Request](https://github.com/sendgrid/sendgrid-nodejs/tree/master/CONTRIBUTING.md#feature-request)
* [Bug Reports](https://github.com/sendgrid/sendgrid-nodejs/tree/master/CONTRIBUTING.md#submit-a-bug-report)
* [Improvements to the Codebase](https://github.com/sendgrid/sendgrid-nodejs/tree/master/CONTRIBUTING.md#improvements-to-the-codebase)

<a name="troubleshooting"></a>
# Troubleshooting

Please see our [troubleshooting guide](https://github.com/sendgrid/sendgrid-nodejs/blob/master/TROUBLESHOOTING.md) for common library issues.

<a name="about"></a>
# About

@sendgrid/mail is guided and supported by the SendGrid [Developer Experience Team](mailto:dx@sendgrid.com).

@sendgrid/mail is maintained and funded by SendGrid, Inc. The names and logos for @sendgrid/mail are trademarks of SendGrid, Inc.

![SendGrid Logo](https://uiux.s3.amazonaws.com/2016-logos/email-logo%402x.png)