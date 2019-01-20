
# EventLogging

EventLogging is a set of abstractions for dealing with streams of structured
and schema-ed data.  It was originally developed to collect metrics from MediaWiki using the [EventLogging Extension](https://www.mediawiki.org/wiki/Extension:EventLogging).  It has evolved beyond its original use case, and can now be used for building flows of stream data.

**Table of Contents**  *generated with [DocToc](http://doctoc.herokuapp.com/)*

- [Overview](#overview)
- [Installation](#installation)
- [EventLogging URIs](#eventlogging-uris)
- [Event Structure](#event-structure)
    - [Schemas](#schemas)
        - [Schema Repositories](#schema-repositories)
        - [Meta](#meta)
            - [EventCapsule (mediawiki extension)](#eventcapsule-mediawiki-extension)
            - [Event Meta](#event-meta)
- [Components](#components)
    - [eventlogging-consumer](#eventlogging-consumer)
    - [eventlogging-processor](#eventlogging-processor)
    - [eventlogging-forwarder](#eventlogging-forwarder)
    - [eventlogging-multiplexer](#eventlogging-multiplexer)
    - [eventlogging-service](#eventlogging-service)
- [Consumer Handler Plugins](#consumer-handler-plugins)
- [Examples](#examples)
- [Logging](#logging)

# Overview

EventLogging takes streams of structured and schema-ed (possibly not valid) data as input, and then outputs them again.  Along the way, the data may be
validated or transformed.  EventLogging is not a full realtime stream processor
like Storm or Samza.  Instead, it is more like unix pipes.  Using the EventLogging URI format, you can easily address inputs and outputs as URIs.

Some quick examples:

```bash

# Consume from a Kafka topic to a file
eventlogging-consumer kafka:///broker1:9092?topic=test&zookeeper_connect=zk1:2181 stdout://

# Consume from ZeroMQ and write to MySQL
eventlogging-consumer tcp://localhost:2181 mysql://user:pw@mysql.host/db

# Forward from one input to multiple inputs
evenltogging-forwarder stdin:// stdout:// file:///tmp/outfile kafka:///broker1:9092?topic=testout

```

For more information and history, read:

- https://www.mediawiki.org/wiki/Extension:EventLogging/Guide
- https://wikitech.wikimedia.org/wiki/Analytics/EventLogging
- https://www.mediawiki.org/wiki/Extension:EventLogging

# Installation

The file ``setup.py`` lists the numerous dependencies under
``install_requires``. Running ``setup.py install`` configures the
server/eventlogging library and adds the programs in bin to your
path.


# EventLogging URIs

EventLogging inputs and outputs are configured using URIs.  This is done by writing pluggable handlers that know how to read or write particular URI schemes.  The handlers take keyword arguments which are populated from the URI query parameters.  E.g. If `tcp://localhost:2181?raw=True`.  was provided as the output argument to eventlogging-consumer, then the `@writes('tcp')` handler would be invoked with `raw=True` as one of the keyword arguments.

This allows for easy addition of inputs and outputs to any EventLogging component.


# Event Structure

For now, EventLogging only works with JSON data.  `eventlogging-processor` can be used to intake encoded JSON strings of varying formats and transform to JSON streams.  Most other EventLogging components expect newline delimited JSON objects as input.

## Schemas

Each JSON event object is expected to conform to a [JSON Schema](http://json-schema.org/).  Unless the JSON Schema specifies a [$schema](http://spacetelescope.github.io/understanding-json-schema/reference/schema.html), the JSON schema is expected to be [draft-03](http://json-schema.org/draft-03/schema#).  Schemas may be written in JSON or YAML.


### Schema Repositories
EventLogging was originally designed with a single remote schema repository: [meta.wikimedia.org](https://meta.wikimedia.org/w/index.php?title=Special%3AAllPages&from=&to=&namespace=470).  At the moment, it still only supports this one remote repository.  Recently support has been added for pluggable local file based repositories.  Local repositories are currently only used by `eventlogging-service`, but more flexible repository support is planned.

### Meta

EventLogging schemas are mostly unspecified.  However, there are a few fields that all events are required to have.  These fields must be present in the event meta data.  When EventLogging was originally written for Mediawiki events, the schema chosen for event meta data was tightly coupled with Mediawiki.  More recently, a more generic event meta data format has been created.

In either case, it is important that every event is tagged with uniquely identifying schema information, called a `scid` (schema id).  The scid is stored differently in the two different meta data cases, but the purpose is the same.


#### EventCapsule (mediawiki extension)

EventCapsules (./eventlogging/capsule.py) wrap the actual event content with a meta data parent object.  This meta schema has fields that are Mediawiki specific, and should only be used for events generated via the [EventLogging Mediawiki Extension](https://www.mediawiki.org/wiki/Extension:EventLogging).  Events of this kind are usually intaken and parsed using `eventlogging-processor` and a custom format.  These events will have the client generated event content data in the `event` field of the EventCapsule object.

`scids` are obtained from EventCapsule objects via the `schema` and `revision` fields, to make up the `(schema, revision)` `scid` tuple.

These schemas are expected to be draft-03 JSON Schemas.

E.g.
```javascript
{'additionalProperties': False,
 'description': 'A wrapper around event objects that encodes generic metadata',
 'properties': {
  'event': {u'additionalProperties': False,
   'description': 'Logs an edit conflict',
   'properties': {'namespace': {'description': 'The namespace of the page',
     'required': True,
     'type': 'integer'},
    'pageId': {'description': 'The page ID of the page being moved',
     'required': True,
     'type': 'integer'},
    'revId': {'description': 'The revision ID',
     'required': True,
     'type': 'integer'},
    'title': {'description': 'The title of the page, in DB form with no namespace prefix',
     'required': True,
     'type': 'string'},
    'userId': {'description': 'User ID of the user affected by conflict (0 for anons)',
     'required': True,
     'type': 'integer'},
    'userText': {'description': 'Username or IP address of the user affected by conflict',
     'required': True,
     'type': 'string'}},
   'title': 'EditConflict'},
  'recvFrom': {'description': 'Hostname of server emitting the log line',
   'required': True,
   'type': 'string'},
  'revision': {'description': 'Revision ID of event schema',
   'required': True,
   'type': 'integer'},
  'schema': {'description': 'Title of event schema',
   'required': True,
   'type': 'string'},
  'seqId': {'description': 'Udp2log sequence ID', 'type': 'integer'},
  'timestamp': {'description': 'Unix timestamp of event',
   'format': 'utc-millisec',
   'required': True,
   'type': 'number'},
  'topic': {'description': 'The queue topic name this event belongs in',
   'type': 'string'},
  'userAgent': {'description': 'User Agent from HTTP request',
   'required': False,
   'type': 'string'},
  'uuid': {'description': 'Unique event identifier',
   'format': 'uuid5-hex',
   'required': True,
   'type': 'string'},
  'webHost': {'description': "Request host. 'window.location.hostname' on client-side events; $_SERVER['HTTP_HOST'] on server.",
   'type': 'string'},
  'wiki': {'description': "$wgDBName (for example: 'enwiki')",
   'required': True,
   'type': 'string'}},
 'title': 'EventCapsule'}
```


#### Event Meta

Event Meta objects are a newer more generic way to design event schemas with meta data.  Instead of wrapping the event content, each event is expected to have a `meta` key that is a sub object containing the event's meta data.  This meta data must also contain an `scid`.  Unlike EventCapsule, the `scid` is obtained from the `schema_uri` field.  The `schema_uri` can be any URI, but it must end in `<schema_name>/<schema_revision>`.  This grants more flexibility in locating the actual schema from remote or local URIs, while still allowing EventLogging to ID a schema using the same `scid` tuple format it uses for EventCapsule style events.

The meta schema itself is not yet maintained as a standalone schema, although this is planned for future work.  Currently, the meta schema is provided along with the schema for each event.

In addition to `schema_uri`, all event meta schemas must also provide `id` and `dt`.

Wikimedia maintains event schemas of this format at [mediawiki/event-schemas](https://github.com/wikimedia/mediawiki-event-schemas/tree/master/jsonschema/mediawiki).

E.g.

```yaml
title: MediaWiki Page Delete
description: Represents a MW Page Delete event
$schema: http://json-schema.org/draft-04/schema#
type: object
properties:
  # global event fields
  meta:
    type: object
    properties:
      topic:
        type: string
        description: the queue topic name this message belongs to
      schema_uri:
        type: string
        description: >
          The URI identifying the jsonschema for this event.  This may be just
          a short uri containing only the name and revision at the end of the
          URI path.  e.g. schema_name/12345 is acceptable.  This field
          is not required.
      uri:
        type: string
        format: uri
        description: the unique URI identifying the event
      request_id:
        type: string
        pattern: '^[a-fA-F0-9]{8}(-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}$'
        description: the unique UUID v1 ID of the event derived from the X-Request-Id header
      id:
        type: string
        pattern: '^[a-fA-F0-9]{8}(-[a-fA-F0-9]{4}){3}-[a-fA-F0-9]{12}$'
        description: the unique ID of this event; should match the dt field
      dt:
        type: string
        format: date-time
        description: the time stamp of the event, in ISO8601 format
      domain:
        type: string
        description: the domain the event pertains to
    required:
      - topic
      - uri
      - id
      - dt
      - domain
  # event-specific fields
  title:
    type: string
    description: the title of the page
  page_id:
    type: integer
    minimum: 1
    description: the page ID of the deleted page
  user_id:
    type: integer
    description: the user that performed the delete
  user_text:
    type: string
    description: the text representation of the user
  summary:
    type: string
    description: the summary comment left by the user
required:
  - meta
  - title
````


# Components

There are several EventLogging process components, and each has a special purpose.

## eventlogging-consumer
Consumes an event stream and writes it to a configured output. Input stream and
target data store are specified using URIs.
## eventlogging-processor
Transforms raw log stream to JSON event stream.  This intakes
raw line delimited strings in arbitrary format, transforms them into
JSON strings, parses them as JSON objects, validates them against a
JSON schema, and then produces each validated event to the configured outputs.

## eventlogging-forwarder
Arbitrary input -> outputs forwarding. Reads line-oriented input from
an input stream and writes to configured outputs.  No JSON parsing or
JSON schema validation is done.  This can also optionally prepend
sequence numbers to each line.

## eventlogging-multiplexer
Reads messages from one or more inputs and publish a muxed output stream
containing all messages from all inputs.


## eventlogging-service

HTTP service that intakes JSON events via an HTTP POST, parses, validates, and produces them to configured outputs.

# Consumer Handler Plugins
`eventlogging-consumer` will attempt to load custom user created reader and writer handler plugins from the `EVENTLOGGING_PLUGIN_DIR` environment variable. It will automatically import *.py files in this directory.  This allows `eventlogging-consumer` to work with custom scheme URI handlers for reading or writing events.  You can use this to read or write to/from a to a new queue or database, or use it to do special filtering or transformation on events before

```python
# /home/me/el-plugins/newqueue_writer.py
from eventlogging import reads, writes, stream
from newqueue import NewQueue

@reads('newqueue')
def newqueue_reader(queuename):
    newqueue_client = NewQueue(queuename)
    newqueue_iterator = newqueue_client.get_iterator()
    return stream(newqueue_iterator)

@writes('newqueue')
def newqueue_writer(queuename):
    newqueue_client = NewQueue(queuename)
    while True:
        event = (yield)
        newqueue_client.write(event)
```

```bash
export EVENTLOGGING_PLUGIN_DIR=/home/me/el-plugins

# start an eventlogging-consumer consuming
# from NewQueue queue named 'input' and outputting
# to NewQueue queue named 'output'.
eventlogging-consumer newqueue:///?queuename=input newqueue:///?queuename=output
```

# Examples
## Consume from Kafka, filter using grep, produce to Kafka topics based on a field value
```bash
eventlogging-forwarder 'kafka:///broker1:9092?zookeeper_connect=zk1:2181&topic=my_topic&identity=my_consumer_group' stdout:// | \
grep 'must match me' | \
eventlogging-consumer stdin:// kafka:///broker1:9092?topic=my_new_topic_with_{my_field}
```

Breaking this down:

The first line starts an `eventlogging-forwarder` consuming from the Kafka topic
'my_topic', and committing consumer group offsets to Kafka under the consumer group 'my_consumer_group'.  It then outputs each event it consumes to stdout.  This uses a forwarder instead of a consumer because we don't need to do any JSON parsing.  We assume that all of the events in the 'my_topic' topic are valid events.

We use a standard unix pipe to send this output to grep to filter for events that contain the string 'must match me' somewhere.  This is then piped into an `eventlogging-consumer`.

The `eventlogging-consumer` reads the filted events from stdin, and then writes them to a Kafka topic.  The Kafka topic given here will be interpolated against the event itself.  The topic given is '=my_new_topic_with_{my_field}'.  The event then must have a field called `my_field`.  The actual topic produced to will be dynamic based on the value of `my_field` in the event.  I.e., if the value of `my_field` is 'find', then the actual topic prodced to will be 'my_new_topic_with_find'._



# Logging
By default, eventlogging logs at INFO level.  Set the environment variable LOG_LEVEL
if you wish to change this to a differnet level.  E.g.
  export LOG_LEVEL=DEBUG && bin/eventlogging-processor ...
