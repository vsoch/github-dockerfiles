# These examples utilize the 'Most Popular' and 'Semantic' public APIs from The New York Times.
### To run the `servers` examples, you'll need to generate a set of API keys and embed them in the appropriate config files.
  1. If you haven't already, register for API keys by requesting a key here: http://developer.nytimes.com/signup
  3. Create a key for the "Most Popular API" and the "Semantic API" and add them to the proper 'config.json' and '.env' files.

# servers
* Contains several examples using the `gizmo/server` package.

# pubsub
* Contains several examples using the `gizmo/pubsub` package.

## nyt
* Contains a small API client used throughout the example.
# Example on how to use AWS SNS + SQS for pub/sub communication

We're going to set up two services to follow the pub/sub pattern using AWS SNS and AWS SQS.  One service is api-sns-pub and the other service is sqs-sub.  They can both be found at https://github.com/NYTimes/gizmo/tree/master/examples/pubsub. For more information about pub/sub pattern, SNS, and SQS check out http://www.infoq.com/articles/AmazonPubSub. 

### High level overview

1. Create SNS Topic 
2. Create SQS Queue
3. Create GCP Pubsub Project
4. Get the SQS Queue to subscribe to the SNS Topic
5. Set up api-sns-pub example service to send messages to the SNS Topic
6. Set up sqs-sub example service to listen to the SQS Queue

### Set up a topic with AWS SNS console
1. Login to your AWS account
2. Go to https://console.aws.amazon.com/sns
3. Click on "Topics" on the left hand side
4. Click "Create new topic" 
5. Topic Name = TestTopic  (or whatever you want)
6. TestTopic = TestTopic  (or whatever you want)

### Set up an AWS SQS Queue with AWS console 
1. Go to https://console.aws.amazon.com/sqs
*  Click on Create New Queue 
*  Queue Name = TestQueue (or whatever you want)
*  Click on "TestQueue" and then click "Queue Actions" dropdown and chooose "Subscribe Queue to SNS Topic"
*  Choose the topic we created earlier (TestTopic) from the correct region and then hit "Subscribe"

### Set up a GCP Pubsub Project with GCP console
1. Go to https://console.cloud.google.com
*  Select an Existing project/Click on Create New Project
*  Go to https://console.cloud.google.com/cloudpubsub
*  Click on New Topic
*  Click on your created topic options (three dots)
*  Click on New Subscription

### Change SNS Subscription to Raw Message Delivery
1. Go to https://console.aws.amazon.com/sns
* Click on the blue ARN text next to "TestTopic" to take you to the "Topic Details: TestTopic" page
* Click on the checkmark besides the ARN Subscription ID, which is from your SQS "TestQueue"
* Click "Edit Subscription Attributes" from the dropdown menu titled "Other Subscription Actions"
* Turn on "Raw Message Delivery"

### Set up logging files
1. gizmo logs to the directory specified in config.json.  The example project is pointing to `/var/nyt/logs/cats-publisher/` for the api-sns-pub service, `/var/nyt/logs/cats-subscriber/` for the sqs-sub service, `/var/nyt/logs/cats-pub/` for the cli-sns-pub service and `/var/nyt/logs/dogs-pubsub/` for the gcp-pubsub service
* You must create this directory and add access.log and app.log inside it.
* You might not have permission to run the following commands in which case you'll have to put sudo before them.
* In your terminal run `mkdir -p /var/nyt/logs/`
* run `cd /var/nyt/logs/`
* run `mkdir cats-publisher`
* run `mkdir cats-subscriber`
* run `mkdir cats-pub`
* run `mkdir dogs-pubsub`
* run `touch cats-publisher/access.log`
* run `touch cats-publisher/app.log`
* run `touch cats-subscriber/app.log`
* run `touch cats-pub/app.log`
* run `touch dogs-pubsub/app.log`
* To allow the api-sns-pub server to access these files run the following commands:
* `chmod -R 777 cats-publisher/`
* `chmod -R 777 cats-subscriber/`
* `chmod -R 777 cats-pub/`
* `chmod -R 777 dogs-pubsub/`

### Set up api-sns-pub example server
1. run `go get github.com/NYTimes/gizmo` inside your $GOPATH folder
* run `cd $GOPATH/src/github.com/NYTimes/gizmo/examples/pubsub/api-sns-pub`
* run `go get ./...`
* update the config.json file to point to your newly created ARN for "Topic".  Example: `arn:aws:sns:us-east-1:123456789:TestTopic`
* also update the config.json file to contain your AccessKey and SecretKey
* ensure that the region in your config.json file is the same as the region you created your SNS Topic and SQS Queue 
* run `go install ./...`
* run `api-sns-pub` (this should be in your $GOPATH/bin folder)
* Your api-sns-pub server should now be running! 

### Push a message to your topic
1. Call the server using a PUT request to `localhost:8080/svc/nyt/cats` with a body like the following json:
```
{
	"url":"http://www.nytiems.com/cats-article",
	"title":"cats cats cats"
}
```
2. CURL example: `curl -X PUT -H "Content-Type: application/json" -d '{"url":"http://www.nytiems.com/cats-article","title":"cats cats cats"}' localhost:8080/svc/nyt/cats`
3. You should see `{"status":"success!"}`
4. If you check your SQS Queue, you should now have one message in it

### Read a message from your SQS Queue 
1. run `cd $GOPATH/src/github.com/NYTimes/gizmo/examples/pubsub/sqs-sub`
*  run `go get ./...`
*  update the config.json file to contain your AccessKey and SecretKey
*  also make sure it points to the correct region 
*  run `go install ./...`
*  run `sqs-sub`
*  Your sqs-sub server should now be running!  
*  You should have seen the message(s) you sent earlier that were stacked on the SQS Queue
*  Now, when you run your `PUT /svc/nyt/cats` request, it will update the SNS, which SQS is subscribed to, and your sqs-sub service is polling the SQS Queue.  If there is a message on the queue, it will be deleted from the queue and read by sqs-sub.

<br />
<h4> Congrats on setting up pub/sub communication with AWS SNS + SQS! </h4>
<br />

### Troubleshooting
* Make sure the region your created your SNS topic and SQS Queue matches the region in your config.json files.  
* Make sure the Access Key and Secret Access Key you passed into the config.json have appropriate credentials for communicating with SNS and SQS
## `cli-sns-pub` 
* example of a simple CLI utility that emits two messages to Google Cloud Plattforn via a `gizmo/pubsub/GCPMultiPublisher`.

### The config in this example is loaded via environment variables and it utilizes the default `gizmo/config.Config`. Before running, fill in some GCP credentials and `source` the local '.env' file.# `api-sns-pub` 
* example mixing `gizmo/server.SimpleServer`, `gizmo/server.JSONService` and `gizmo/pubsub.SNSPublisher`. 
* JSON API will accept a message and then publish it to an Amazon SNS topic.

### The config in this example is loaded via a local JSON file and the default `gizmo/config.Config` struct.
## `sqs-sub`
* example of a small daemon process consumes an Amazon SQS queue via a `gizmo/pubsub.SQSPublisher`. 

### The config in this example is loaded via a local JSON config file into the default `gizmo/config.Config` struct.
## `cli-sns-pub` 
* example of a simple CLI utility that emits an message to AmazonSNS via a `gizmo/pubsub.SNSPublisher`. 

### The config in this example is loaded via environment variables and it utilizes the default `gizmo/config.Config`. Before running, fill in some AWS credentials and `source` the local '.env' file. 
# `api-kafka-websocket-pubsub` 
* This is an example based on a prototype from an NYTimes hack week. It mixes `gizmo/server.SimpleServer`, `gizmo/server.SimpleService`, `gizmo/pubsub.KafkaPublisher`, `gizmo/pubsub.KafkaSubscriber` and `gorilla/websocket` and was used to test out realtime, collaborative crossword games.
* The server offers 3 endpoints to allow users to:
  1. Create a new topic on Kafka (visit http://localhost:8080/svc/v1/create to get a 'stream ID')
  2. Upgrade a request to a websocket connection and expose the topic over it
  3. Serve an HTML page that demos the service.(visit http://localhost:8080/svc/v1/demo/{stream_id from 'create'})

### This demo requires Kafka and Zookeeper to be installed and running locally by default.
  * To install and run on OS X, run: `brew install kafka` and then `zookeeper-server-start.sh /usr/local/etc/kafka/zookeeper.properties` to run Zookeeper and `kafka-server-start.sh /usr/local/etc/kafka/server.properties` to start a Kafka broker.

### The config in this example is loaded via a local JSON file and the default `gizmo/config.Config` struct.
# The 'Reading List' Example

This example implements a clone of NYT's 'saved articles API' that allows users to save, delete and retrieve nytimes.com article URLs.

This service utilizes Google Cloud Datastore and is set up to be built and published to Google Container Registry, deployed to Google Container Engine and monitored by Google Cloud Tracing.

Instead of utilizing NYT's auth, this example leans on Google OAuth and Google Cloud Endpoints for user identity.

To run locally, have the latest version of `gcloud` installed and execute the `./run_local.sh` script to start up the Datastore emulator and the reading list server.

A few highlights of this service worth calling out:

* [service.yaml](service.yaml)
  * An Open API specification that describes the endpoints in this service.
* [gen-proto.sh](gen-proto.sh)
  * A script that relies on github.com/NYTimes/openapi2proto to generate a gRPC service spec with HTTP annotations from the Open API spec along with the Go/Cloud Endpoint stubs via protoc.
* [service.go](service.go)
  * The actual [kit.Service](http://godoc.org/github.com/NYTimes/gizmo/server/kit#Service) implementation.
* [http_client.go](http_client.go)
  * A go-kit client for programmatically accessing the API via HTTP/JSON.
* [cmd/cli/main.go](cmd/cli/main.go)
  * A CLI wrapper around the gRPC client.
* [.drone.yml](.drone.yml)
  * An example configuration file for [Drone CI](http://readme.drone.io/) using the [NYTimes/drone-gke](https://github.com/nytimes/drone-gke) plugin for managing automated deployments to Google Container Engine.
* [cloud-endpoints/service-ce-prd.yaml](cloud-endpoints/service-ce-prd.yaml)
  * A service configuration for Google Cloud Endpoints.

This example [mirrors an example](https://github.com/NYTimes/marvin/tree/master/examples/reading-list#the-reading-list-example) in gizmo's sibling server for Google App Engine, marvin.
# The Reading List CLI

Use `gcloud auth application-default login` to generate credentials.

Alternatively, you can use the `-creds` flag that points to the path of a Google service account JSON key file.

If running locally, use `-insecure` and `-fakeID` to inject user identity.

## Usage

```
Usage of ./cli:
  -creds string
    	the path of the service account credentials file. if empty, uses Google Application Default Credentials.
  -delete
    	delete this URL from the list (requires -mode update)
  -fakeID string
    	for local development - a user ID to inject into the request
  -host string
    	the host of the reading list server (default "localhost:8081")
  -insecure
    	use an insecure connection
  -limit int
    	limit for the number of links to return when listing links (default 20)
  -mode string
    	(list|update) (default "list")
  -url string
    	the URL to add or delete
```
## `kit`
* example using a `gizmo/server/kit.Service`. 
* one endpoint will serve JSON of the most popular NYT articles and another will serve JSON listing recent articles in The New York Times about 'cats'.
* this service is also available via gRPC.
## `json`
* example using a `gizmo/server.JSONService` with a `gizmo/server.SimpleServer`. 
* one endpoint will serve JSON of the most popular NYT articles and another will serve JSON listing recent articles in The New York Times about 'cats'.

### The config in this example is loaded via a local JSON file and a custom config struct that is composed of a `gizmo/config.Server` struct.
## `mixed`
* example using a `gizmo/server.MixedService` with a `gizmo/server.SimpleServer`.
* one endpoint will serve JSON of the most popular NYT articles and another will serve an HTML page listing recent articles in The New York Times about 'cats'. 
* this example is very similar to the `simple` example, but makes use of the available `JSONMiddleware` method in a `gizmo/server.MixedService`.

### The config in this example is loaded via a local JSON file and a custom config struct that is composed of a `gizmo/config.Server` struct.
## `mysql-saved-items`
* example using a `gizmo/server.JSONService` with a `gizmo/server.SimpleServer` using MySQL for persistence.
* this is a simple implementation of [nytimes.com/saveditems](http://www.nytimes.com/saveditems). It provides 3 endpoints to create, delete and list 'saved items' for a single user.

### The config in this example is loaded via a local JSON file and a custom config struct that is composed of a `gizmo/config.Config` struct.
## `simple`
* example using a `gizmo/server.SimpleService` with a `gizmo/server.SimpleServer`.
* one endpoint will serve JSON of the most popular NYT articles and another will serve an HTML page listing recent articles in The New York Times about 'cats'.

### The config in this example is loaded via environment variables and a custom config struct that is composed of a `gizmo/config.Server` struct. To load the config, `source` the local `.env` file before running.
## This is a simple client for a couple public New York Times APIs. The client and its related types are used throughout the gizmo toolkit examples.
# Welcome to the 2nd generation of Gizmo servers 🚀!

Gizmo's intentions from the beginning were to eventually join forces with the wonders of the [go-kit toolkit](https://github.com/go-kit/kit). This package is meant to embody that goal.

The `kit` server is composed of multiple [kit/transport/http.Servers](https://godoc.org/github.com/go-kit/kit/transport/http#Server) that are tied together with a common HTTP mux, HTTP options and middlewares. By default all HTTP endpoints will be encoded as JSON, but developers may override each [HTTPEndpoint](https://godoc.org/github.com/NYTimes/gizmo/server/kit#HTTPEndpoint) to use whatever encoding they need. If users need to use gRPC, they can can register the same endpoints to serve both HTTP and gRPC requests on two different ports.

This server expects to be configured via environment variables. The available variables can be found by inspecting the [Config struct](https://godoc.org/github.com/NYTimes/gizmo/server/kit#Config) within this package. If no health check or [warm up](https://cloud.google.com/appengine/docs/standard/go111/how-instances-are-managed#warmup_requests) endpoints are defined, this server will automatically register basic endpoints there to return a simple "200 OK" response.

Since NYT uses Google Cloud, deploying this server to that environment provides additional perks:

* If running in the [App Engine 2nd Generation runtime (Go >=1.11)](https://cloud.google.com/appengine/docs/standard/go111/), servers will:
  * Automatically catch any panics and send them to Stackdriver Error reporting
  * Automatically use Stackdriver logging and, if `kit.LogXXX` functions are used, logs will be trace enabled and will be combined with their parent access log in the Stackdriver logging console.
  * Automatically register Stackdriver exporters for Open Census trace and monitoring. Most Google Cloud clients (like [Cloud Spanner](https://godoc.org/cloud.google.com/go/spanner)) will detect this and emit the traces. Users can also add their own trace and monitoring spans via [the Open Census clients](https://godoc.org/go.opencensus.io/trace#example-StartSpan).


For an example of how to build a server that utilizes this package, see the [Reading List example](https://github.com/NYTimes/gizmo/tree/master/examples/servers/reading-list#the-reading-list-example).
