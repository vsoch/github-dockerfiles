# Event Data Bus

<img src="doc/ouroboros.png" align="right" style="float: right">

The Event Data Bus is an internal component of the Event Data service. It is a central service that accepts data from Event Data Agents and distributes to other services. It is a piece of common infrastructure shared by Crossref and DataCite, and enables the various public-facing services offered under the Crossref Event Data and DataCite Event Data.

The Event Data Bus is responsible for the following:

 - ensuring compliance of Events with the schema
 - ensuring uniqueness of Event IDs
 - being a central place where Events can be sent
 - serve as a permanent archive of all Events
 - serve as the canonical time-stamper for Events, enforcing approximate monotonicity of time (not strict, but within an hour or so)
 - serve as a fan-out for the various services that DataCite and Crossref want to operate
 - updating the archive in exceptional circumstances

All access to the service is authenticated, so it is not available to the public.

The Event Data Bus also serves as a development and integration target for users writing agents. It is available as a Docker container.

## Design

The Event Data Bus is a simple service that accepts, stores and forwards Events. It is designed to be a transparent interface between Agents and consumers, modelled on the Lagotto API. It has one method for sending data (`POST` from an Agent) and one method for recieving data (`POST` from the Event Bus to a downstream service). It also provides HTTP access to daily archives.

### Ownership of Data and Registration Agencies

The service is operated by Crossref on behalf of both Crossref and DataCite. Data in the Event Bus is provided by agents, which are operated by Crossref or DataCite or a third party under authorization of Crossref or DataCite. The data may therefore reference (i.e. have a subject and/or object) content that belongs to Crossref or DataCite. 

The Event Bus is not a public-facing service, and it will feed into services offered by Crossref and DataCite. Those downstream services are responsible for filtering data according to their own criteria. In principle Events may occur that don't concern either content that belongs to Crossref or DataCite, e.g. assertions about links between two third-party properties, e.g. Wikipedia and arXiv to pick a fictitious example. Each downstream service will have its own requirements for which data to include.

### Immutability

Once an Event has been created it cannot be deleted. The principle of a stable, citable data-set is at the foundation of Crossref Event Data. However under some circumstances it may be required to remove some data from an Event.

Every Event 'belongs' to the Agent that created it, and there is approximately one Agent per source. Each source may have different concerns regarding change. For example, Twitter stipulates that if a Tweet is deleted then the data must also be deleted. In this case, the Twitter agent would update the Event to remove the Tweet ID and Author (which are the only Twitter-owned data that is contained in the Event). It would not delete the Event (which would then represent that "someone on Twitter tweeted this DOI, we don't know who"). Twitter is currently the **only** source where we foresee editing happening.

**Agents should not routinely update Events.** If issues like data quality arise then there are other reporting mechanisms.

### Authorization and authentication

All access must be authenticated. Authentication is done with JWT. For any connection to be accepted a JWT must be signed with the correct secret. In the production service, the secret is owned by the party operating the service (Crossref). In testing, the secret is "`TEST`". More than one secret can be configured, which allows for a staged replacement of the secret without interruption to service.

JWTs should be sent in an `Authorization` HTTP header, e.g. 

    Authorization: Bearer «JWT»

The following claim is required to read data:

 - `sub` to identify the party sending/requesting data. E.g. `crossref-widget-service`, `datacite` or an agent's `source-id`. 

Every subscription is tied to the `sub`, which means if you want to delete or change a subscription you must use a token with the same `sub` field.

In addition the following is required to send data:

 - `src`, which is the `source_id` in the Event message

The `source_id` of every Event must match the `src` field of the token. This means that we can trace the sender of an Event and also authorize any future changes to the Event. This means that either a different JWT must be supplied to every Agent, or that they all share one. 

### Storage

All permanent storage is done on AWS S3. The service relies on the S3 read-after-write consistency, which is now [available in all regions](http://docs.aws.amazon.com/AmazonS3/latest/dev/Introduction.html#ConsistencyModel). Discussion in 'Durability' section.

Subscription data is stored in Redis.

## Sending Events

Events are sent by Agents by `POST`ing to `/events`. The `Authorization` header should contain a valid JTW, and the `sub` should match the `source_id` found in the Event.

The content of the message should be a single JSON-serialized Event, sent with the `application/json` `Content-Type`. 

The Event Bus will ignore the `timestamp` field and supply itself. The field cannot be specified by the Agent when it creates or updates the Event.

The following response codes will be returned:

 - 201 - correctly formatted, unique Event received
 - 400 - does not conform to schema
 - 401 - JWT token not present or correct
 - 403 - claims in JWT token don't match sent or updated Event
 - 409 - Event with duplicate ID sent

On receipt of a 201, the Event has been stored.

## Subscribing

A client can subscribe to the Bus by sending a message. There are two kinds of subscription:

 - with a `live` subscription Events are sent on immediately, one by one.
 - with a `batch` subscription the archive Events are sent every 24 hrs.

To subscribe send a `POST` to `/subscriptions`. The body of the post should be JSON, and both types of subscription have the same format. It should contain the following fields:

 - `id`, which can be used to refer to the subscription later
 - `type`, one of `live` or `batch`
 - `url`, the endpoint to `POST` to
 - `headers`, a dictionary of headers that should be sent to the endpoint, if you want

Example:

    {
      "id": "example",
      "type": "«live or batch»",
      "url": "http://example.com/post-url",
      "headers": {
        "Token": "abcdefgh"
      }
    }

To alter a subscription (e.g. change URL or headers) send a PUT to `/subscription/«id»` with the above fields altered. The `id` in the URL must match the ID in the payload. After this the subscription will be altered with whatever new information is supplied.

To delete a subscription, send a DELETE to `/subscription/«id»`.

### Live subscription

The Event Bus sends data on to consumers immediately when they subscribe with a live subscription.

After a subscription is set up the service will start sending Events as a `POST` to the endpoint at the supplied URL. All succesfully accepted Events are passed straight through from the input to subscribers, with the given HTTP headers added. The format of Events is exactly the same as that in which they were received, with the `timestamp` header added. You can configure authentication with your own service by setting the appropriate headers. Alternatively you can do this with query parameters.

### Batch subscription.

The Event Bus creates a daily archive approximately every 24 hours. When the archive is ready a notification is sent to all batch subscribers as a `POST` to the endpoint at the supplied URL. The content of the notification is a URL where the data can be fetched:

    {
      "url": "http://archive.eventdata.crossref.org/archive/2016-11-01/events.json"
    }

The specified headers will be sent. 

Note that whilst each event is around 1 Kilobyte, the daily archive can be 50 Megabytes.

## Durability

### Subscription deliverability

A the Event Bus will try to deliver a message a set number of times (see [Parameters](#parameters)). After that it will fail (which will be recorded in logs).

Events are forwarded as they arrive but there is no guarantee that they will be delivered in the same order or within a particular time-frame. Events may be delivered out-of-order under two circumstances:

 - If an Event is sent to a client but the original delivery fails, it may be re-tried, and the re-try may happen after a later Event is successfully sent.
 - If two Events arrive at a similar time but are sent to different load-balanced instances, they may be processed at different speeds.

### Data durability

A `POST`ed Event is not acknowledged until it has been written to storage. If delivery fails, the agent should consider that it has not been accepted and try again. 

The system will not accept the same Event twice (with identity specified by the `id` field) which means an agent can re-try sending Events if they failed. 

### Self validation

A consuming system may make a `live` and a `batch` subscription. It can store and use the `live` Events as they are sent. At approximately 24 hour intervals, when the `batch` data is sent the agent can verify that it received all of the Event IDs.

### Edited Events

Events will be edited very infrequently. One of the principles of Event Data is the immutability of an Event. However, in exceptional circumstances where we are compelled to, some data must be edited. It is not possible to delete an Event, but it is possible to edit and over-write some data.

When a `DELETE` is sent for an existing Event, the following fields are set on the Event:

 - `updated` - datestamp event was deleted
 - `update_action` - set to `"deleted"`

The following fields are removed:

 - `subj` - any subj metadata
 - `obj` - any obj metadata

The following field is set:

 - `subj_id` - this is set to `http://eventdata.crossref.org/removed`

This effectively marks the Event as having been deleted. It also retains enough information about the object, source and timestamp of the Event that consumers who have already used the event are not left in an inconsistent state.

### S3 Concerns

Every Event is written to a new S3 object. S3 guarantees read-after-write semantics when new objects are created, which means that the daily archive will have access to all Events.

When an Event is updated (in exceptional circumstances), the archive file and Event object are updated. This means that for a brief period after an update the archive file will be eventually consistent.

## Schema

All Events are subject to the Event schema. If an Event is sent that does not conform to the schema, a 400 error response is returned. The schema is checked into source control and provided in the `resources/schema.json`. This means that the version of the schema is coupled to the version of the codebase.

## API Endpoints

 - `GET` `/subscriptions` - list subscriptions owned by user
 - `GET` `/events/archive/«YYYY-MM-DD»/«prefix»` - retrieve archive of Events for given day
 - `GET` `/events/archive/«YYYY-MM-DD»/«prefix»/ids` - retrieve archive of Event IDs for given day
 - `POST` `/events/` - send a new Event

## Running the service

Two services must be run. The main bus worker handles accepting and broadcasting data, and should be run with replication. The schedule worker should be run with replication of 1, and is responsible for creating daily archives.

### Starting and stopping

The service responds gracefully to `SIGTERM` by stopping access (i.e. the HTTP server stops responding to all endpoints), and then delivering all outgoing messages, then exiting. On successful exit, a 0 exit code is returned. If there was an error, an exit code of 1 is returned (all errors will be recorded in the log). This behaviour enables a rolling update to a group of instances in a cluster.

### Load balancing

This application may be load balanced without further configuration. Every instance is responsible for delivering its own messages. In production, running three services allows for failover and updating.

### Running a mock instance for integration tests

The service runs as an Integration test target. For this, it stores all data in Redis and does not require access to S3. All data is also deleted at start-up.

To run the Event Bus in Mock mode provide the `MOCK=TRUE` environment variable.

A self-contained Docker image is provided, see below.

### Production Deployment

The Event Data Bus should be deployed as part of the wider Event Data system. It connects to the following services:

 - Redis
 - AWS S3
 - Event Data Status Service

## Configuration Parameters

The Event Bus uses the Crossref Event Data global configuration namespace. All configuration variables are required. Some have defaults.

Note that during development and testing Docker Compose refers to the `.env` file for some of these.

 - `BUS_PORT`
 - `BUS_REDIS_DB`
 - `BUS_REDIS_HOST`
 - `BUS_REDIS_PORT`
 - `BUS_S3_BUCKET_NAME`
 - `BUS_S3_KEY`
 - `BUS_S3_REGION_NAME`
 - `BUS_S3_SECRET`
 - `BUS_STORAGE` - where to put permanent storage, "redis" or "s3". "redis" is only for testing. | s3 | No |
 - `BUS_BROADCAST_CONFIG` - JSON string containing the broadcast configuration
 - `GLOBAL_JWT_SECRETS`
 - `GLOBAL_STATUS_TOPIC`
 - `GLOBAL_KAFKA_BOOTSTRAP_SERVERS`

The Broadcast configuration file is a JSON file containing an array of downstream targets. Targets can be the following types:

 - `http-post-live` - Events are POSTed to an HTTP endpoint as they appear
 - `kafka-live` - Events are sent to an Apache Kafka Topic as they appear

When the type is `http-post-list` the following fields should be supplied:

 - `jwt` a JWT token to be passed in a Authorization Bearer header
 - `endpoint` a URL to POST to

When the type is `kafka-live` the following fields should be supplied:

 - `bootstrap-servers` - Kafka bootstrap servers config
 - `topic` - Kafka topic name

The format of the broadcast configuraiton file is {type -> {label -> {values}} dictionary. A complete example:

    {
      "http-post-live": {
        "example.com post": {
          "jwt": "abcdefgh",
          "endpoint": "http://example.com/events"
        }
      },
      "kafka-live": {
        "my kafka": {
          "bootstrap-servers": "localhost:9092,other:9092",
          "topic": "my-topic"
        }
      }
    }

## Tests

Tests are split into three sections:
 - Unit tests test only self-contained functions.
 - Component tests require Redis. Most tests live here.
 - Integration tests require a live S3 instance on an AWS account.

Three Docker Compose files are provided, including various levels of configuration and a Redis container. 

Note that integration and component tests must be run separately because they have different top-level configurations (specifically the value of the `STORAGE`);

### Unit tests

Unit tests are for functions. They can be run in any context.

 - `time docker-compose -f docker-compose-unit-tests.yml run -w /usr/src/app test lein test :unit`

### Component tests

These are generally at the API level and require Redis to be configured. They mock out S3 dependencies using Redis for convenience. Use the Mock image to use a bundled Redis instance:

 - `time docker-compose -f docker-compose-component-tests.yml run -w /usr/src/app test lein test :component`

### Integration tests

**Note: there are currently no integration tests.** Previously extant integration tests have been refactored into the Event Data Common library.

These run at the API level and test integration with S3, and therefore must be configured for S3. The actual test suite executed is component tests, except configured to run against S3. You must include a .env file with the following keys:

 - `BUS_S3_KEY`
 - `BUS_S3_SECRET`
 - `BUS_S3_BUCKET_NAME`
 - `BUS_S3_REGION_NAME`

Then

 - `time docker-compose -f docker-compose-integration-tests.yml run -w /usr/src/app test lein test :integration`

If the bucket is not empty, tests will still pass, but it may take a long time to clear the bucket. The AWS command-line tools provide a quick parallel way to empty a bucket **but exercise caution**:

 - `source .env && aws s3 rm --region $BUS_S3_REGION_NAME --recursive s3://$BUS_S3_BUCKET_NAME`

## Docker

### Production

This should be run with Docker Swarm for load-balancing, service discovery and fail-over. Details can be found in the Event Data System repository.

Bus workers:

 - command: `lein run`

Single archive schedule workers:

 - command: `lein run schedule`


### Running a demo instance for development

During development when changes are being made to the local repository you can run the mock container and mount the source code directory as a volume. 

    docker-compose -f docker-compose-demo.yml run -w /usr/src/app demo lein run

To rebuild

    docker-compose -f docker-compose-demo.yml build demo

Check token 

    curl --verbose  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyIxIjoiMSIsInN1YiI6Indpa2lwZWRpYSJ9.w7zV2vtKNzrNDfgr9dfRpv6XYnspILRli_V5vd1J29Q" http://localhost:8002/auth-test

Send event

    curl --verbose --header "Content-Type: application/json" --data "{\"total\":1,\"id\":\"d24e5449-7835-44f4-b7e6-289da4900cd0\",\"message_action\":\"create\",\"subj_id\":\"https:\\/\\/es.wikipedia.org\\/wiki\\/Se%C3%B1alizaci%C3%B3n_paracrina\",\"subj\":{\"pid\":\"https:\\/\\/es.wikipedia.org\\/wiki\\/Se%C3%B1alizaci%C3%B3n_paracrina\",\"title\":\"Se\\u00f1alizaci\\u00f3n paracrina\",\"issued\":\"2016-09-25T23:58:58.000Z\",\"URL\":\"https:\\/\\/es.wikipedia.org\\/wiki\\/Se%C3%B1alizaci%C3%B3n_paracrina\",\"type\":\"entry-encyclopedia\"},\"source_id\":\"wikipedia\",\"relation_type_id\":\"references\",\"obj_id\":\"https:\\/\\/doi.org\\/10.1093\\/EMBOJ\\/20.15.4132\",\"occurred_at\":\"2016-09-25T23:58:58Z\"}"  -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyIxIjoiMSIsInN1YiI6Indpa2lwZWRpYSJ9.w7zV2vtKNzrNDfgr9dfRpv6XYnspILRli_V5vd1J29Q" http://localhost:8002/events

Start mock container with bash:

    docker run --entrypoint=/bin/bash -p 9990:9990  -a stdout -it crossref/event-data-event-bus-mock

## License

Copyright © Crossref

Distributed under the The MIT License (MIT).
