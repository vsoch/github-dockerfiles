# geordi - a user analytics capture engine

Geordi is a REST server built with [Loopback](http://loopback.io/) and running on [node.js](https://nodejs.org/en/).
Its purpose is to collect user behaviour events from Zooniverse Web Applications for analytics, experiments and any other form of analysis, event capture or user monitoring.
It receives posted events via its REST endpoint `http://<geordi-server>/api/events/` and stores the resulting events in a MySQL database for analysis.

## Posting an event to Geordi

To try out posting an event to Geordi, you could use cURL, a REST client (I recommend [Advanced REST client](https://chrome.google.com/webstore/detail/advanced-rest-client/hgmloofddffdnphfgcellkdfbfbjeloo) for Google Chrome, or your own script.

When posting an event, you must provide the fields `userID`, `type` and `projectToken`. A number of other fields are optional and can be posted along with the event. See the next section for more details on the fields you can use.

Here is an example of posting via cURL (line breaks and spacing added for readability):
```
curl    
  --request POST    
  --header 'Content-Type: application/json'    
  --data 
          '{
             "userID":"alex",
             "type":"identify",
             "subjectID":"ASG001d692", 
             "relatedID":"zebra",
             "projectToken":"serengeti"   
           }'
  http://geordi.staging.zooniverse.org/api/events
```

Here is an example of how to post to Geordi from JavaScript:

```
$ = require('jqueryify')
User = require 'zooniverse/lib/models/user'
Subject = require 'models/subject'

eventData = {}
eventData['browserTime'] = Date.now()
eventData['projectToken'] = "galaxy_zoo"
eventData['subjectID'] = Subject.current?.zooniverseId
eventData['userID'] = User.current?.zooniverse_id
eventData['serverURL'] = location.origin
eventData['type'] = "classify"
eventData['data'] = JSON.stringify({"someExtraData":12345,"andSomeMore":"XHY-112"})

$.ajax({
  url: "http://geordi.staging.zooniverse.org/api/events/",
  type: 'POST',
  contentType: 'application/json; charset=utf-8',
  data: JSON.stringify(eventData),
  dataType: 'json'
}).done(function(data, textStatus, jqXHR) {
  console.log('logged to Geordi successfully');
  console.log(data);
}).fail(function(jqXHR, textStatus, errorThrown) {
  console.log('error occurred while logging to Geordi');
  console.log(textStatus);
  console.log(errorThrown);
}).always(function() {
  console.log('finished logging to Geordi');
})
```

A lot of this work can be done for you if you use the [npm geordi-client module](https://github.com/zooniverse/geordi-client). See that project's Github [README.md](https://github.com/zooniverse/geordi-client/blob/master/README.md) for information on how to use the Geordi client.

## What data does Geordi collect?

Geordi stores the following information for each event `POST`ed:

* `id` - a unique sequential integer ID for the event. This is never passed in and is auto-generated by the server. This is the only field where chronological order is guaranteed, so use this in preference to time fields when analysing the order in which things happened.
* `time` - the date and time in UTC of the event (according to the server) (optional, auto-generated if omitted))
* `browserTime` - the date and time in UTC of the event (according to the browser (optional, NULL if omitted))
* `userID` - the zooniverse user ID of the person performing the event. This will always be a string, and should be `"(anonymous)"` for non-logged in users. Can be calculated using the [zooniverse-user-string-getter library](https://github.com/zooniverse/zooniverse-user-string-getter) on npm. (required)
* `type` - the event type to identify the type of the event. This can be anything you like, some examples are `classify`, `view`, `talk`, `tweet`, `identify`, `interventionDismissed`, `competitionEnter` (required)
* `subjectID` - the zooniverse subject ID of the subject upon which the event was performed. (optional)
* `relatedID` - a string containing an additional piece of information you wish to store (e.g. name of animal being identified, key of intervention being delivered, classification ID for classification being created, etc). NOTE: This may be deprecated in future. Use the more versatile `data` instead.
* `projectToken` - the unique identifier for the zooniverse project for which we are logging the event. This should correspond to that used on [Heimdall](http://heimdall.zooniverse.org/), for example `"serengeti"` or `"galaxy_zoo"`
* `data` - a JSON string, or a simple string, containing any additional data you wish to store about the event. Note that if you switch between plain strings and JSON strings, this will pollute the data and make processing harder. It is recommended to stick with either all JSON strings or all plain strings for each event type. (optional)
* `userSeq` - this field will be used to store a sequential integer counter, starting from 1, for this user. Every subsequent event for this user will result in an increment to this counter, regardless of any sessions and across all projects. This is calculated by the server and need not be specified. If set, the specified value will take precedence. (optional, auto-generated if omitted))
* `sessionNumber` - this field will be used to store a sequential integer session number, starting from 1, for this user. A new session will start every time more than 30 minutes has elapsed since the last posted event (across all projects).  This is calculated by the server and need not be specified. If set, the specified value will take precedence. (optional, auto-generated if omitted))
* `eventNumber` - this field will be used to store a sequential integer event number, starting from 1, for this session, for this user. This is calculated by the server and need not be specified. If set, the specified value will take precedence. (optional, auto-generated if omitted))
* `serverURL` - the originating URL of the client. This is useful when you have for example a staging app and a production app posting to the same event server, and you want to separate the event logs by server. This is calculated by the server and need not be specified. If set, the specified value will take precedence. (optional, auto-generated if omitted))
* `clientIP` - the IP address of the user's browser. This is useful for distinguishing non-logged in users or different usages of the same user account from different locations. This is calculated by the server and need not be specified. If set, the specified value will take precedence. (optional, auto-generated if omitted))
* `experiment` - if the [Zooniverse Experiment Server](https://github.com/zooniverse/ZooniverseExperimentServer) is in use, or indeed another experiment server, the experiment name for the currently running experiment can be passed in and stored against the event. (optional)
* `cohort` - if the [Zooniverse Experiment Server](https://github.com/zooniverse/ZooniverseExperimentServer) is in use, or indeed another experiment server, the cohort of this user that is in effect at the time of the event can be passed in and stored against the event. (optional)
* `errorCode` - if an error occurred, this can be used to specify an error code to identify what type of error occurred. (optional)
* `errorDescription` - if an error occurred, this can be used to specify details of the error that occurred. (optional)

Again, the only fields that must be posted by the client making the request are `userID`, `type` and `projectToken`. Everything else is optional and/or auto-generated.

## Reading data from Geordi

Geordi collects its events into a MySQL database, from where you can query the event logs, save CSVs, join with other tables, etc. 

Please take care not to modify the live "event" table in the MySQL DB as it is continually written to from multiple projects. 

For more details on accessing the database, see below. I recommend using a GUI such as [Sequel Pro](http://www.sequelpro.com/) for OS X, [HeidiSQL](http://www.heidisql.com/) for Windows, or phpMyAdmin.

Geordi also logs all events to the "Zooniverse Global" Google Analytics account. This does not allow viewing of individual events, but can be useful for exploring the data in aggregate. The events can be found under "Behavior > Events" or, if you have access, via [this link](https://www.google.com/analytics/web/?hl=en#report/content-event-overview/a1224199w25826018p97262563/). The event type is passed as the "Event Action" in Google Analytics, and the userID is passed as the Event Label.

## History

Created for the [MICO](http://www.mico-project.eu/) project, Geordi was conceived as an API server to capture simple user interaction event history from Zooniverse web applications both to analyse user behaviour and to collect the results of experimental interventions.
Since then it has been adapted for general use as an analytics collector for other scenarios such as competition entries, intervention opt outs, and more.

It is called Geordi after Geordi LaForge from Star Trek, whose visor allows him to see far beyond what is normally visible to humans. And also because its creator Alex B is from North East England, not far from Newcastle-upon-Tyne (where the Geordies come from).

## Using the Zooniverse Geordi Servers

We have two servers, one for staging at http://geordi.staging.zooniverse.org/ and one for production at http://geordi.zooniverse.org/.

Currently staging is running v2.2 (which includes the new `browserTime`, `data`, `serverURL`, `clientIP`, `userSeq`, `sessionNumber` and `eventNumber` parameters).
Production is running v2.1, (which includes the new `browserTime`, `data`, `serverURL`, `sessionNumber` and `eventNumber` parameters but not `clientIP` or `userSeq` or automatic filling of session and event number).
Production will be updated once the current Galaxy Zoo intervention experiment is concluded.

The credentials for accessing the production server either with read-write access or read-only access are in the Zooniverse password repository, and the production `datasources.json` file is in the S3 production configs directory. The staging server credentials are stored here on github in the `datasources.json` file in `config/docker` directory.

Note: It is recommended that for all analysis and reading of Geordi data you use the read-only account. The full account should only be used for admin.

## Running your own instance of Geordi

### Requirements

You'll need to have the following services running:

* [MySQL](https://www.mysql.com/)
** Ubuntu/Debian: `sudo apt-get install mysql-server`
** OS X (with [homebrew](http://homebrew.io)): `brew install mysql`

### Installation

We only support running Geordi via Docker and Docker Compose. If you'd like to run it manually outside a container, see the above Requirements sections to get started, and run through the [Loopback Getting Started tutorial](https://docs.strongloop.com/display/public/LB/Getting+started+with+LoopBack) after which setting up Geordi should seem a lot simpler.

#### Setup Docker Engine and Docker Compose

* Docker Engine & Compose

  * [OS X](https://docs.docker.com/compose/install/)
  * [Ubuntu](https://docs.docker.com/compose/install/)

#### Install and Start Geordi Server

0. Clone the repository `git clone https://github.com/zooniverse/Geordi`.

0. Install Docker and Docker Compose from the appropriate link above.

0. Create and run the application containers by running `docker-compose up`

0. Geordi should be running on port 3030 on your computer, see `docker-compose.yml` for specific details.

#### A note on database configuration

Note that the connection to the database is configured in `datasources.json` which lives in the `server` directory. We do not store our copy of the file on Github as it contains our password credentials. You can find the production file in our S3 bucket under production_configs. You can create your own `datasources.json` file by referring to the loopback documentation [here](https://docs.strongloop.com/display/public/LB/datasources.json). You should use `geordi-mysql` as the data source name. 