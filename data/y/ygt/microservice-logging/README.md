# Microservice Logging

This is a machine-readable first, human-readable second, JSON-based logging micro-library suitable for a wide variety of microservice uses. Currently [Your Golf Travel](http://www.yourgolftravel.com/) are using this for our production microservice architecture, based upon Google's 'Kontainer' Engine ([Kubernetes](http://kubernetes.io/)), [Docker](https://www.docker.com/) and Heroku's [12-factor app](http://12factor.net/) pattern.

The logging library is provided in a number of language formats:
* [Node.js](node)
  - JavaScript ES6
  - For more details see the Node-specific [README](node/README.md)
* [Ruby](ruby)
  - For more details see the Ruby-specific [README](ruby/README.md)
* [Elixir](elixir)
  - currently just a placeholder
* [Go](go)
  - currently just a placeholder

# Design considerations

The design goals of this library were:
* Write logs as JSON
* One line per log entry
* One JSON object per log entry
* Each log entry contains a severity[1]
* Each log entry contains an ISO8601 UTC timestamp
* Each log entry contains the name of the service that wrote it
* Each log entry pertains to an 'event'
* Stack traces are written inside a single JSON log object rather than sprawling over several lines

[1] It turns out that there isn't a single authoriative standard for severity levels, we chose to go with DEBUG, INFO, WARNING, ERROR and CRITICAL as our choices. Sometimes people use FATAL, or even EMERGENCY, but we're fairly certain that we don't need anything of a higher priority than CRITICAL. Your mileage may vary, so we made it trivially configurable.

Much of the work that led to this library was inspired by the book [I <3 Logs](http://www.goodreads.com/book/show/23237460-i-heart-logs) by LinkedIn principle engineer Jay Kreps. The decision to produce a consistent JSON-based logging format that could be then used with analytics lead us to a Google StackDriver logging format that looks something like:

```
{
  "metadata": {
    "severity": "INFO",
    "projectId": "MLP",
    "serviceName": "container.googleapis.com",
    "zone": "europe-west1-b",
    "labels": {
      "container.googleapis.com/cluster_name": "MLP",
      "compute.googleapis.com/resource_type": "instance",
      "compute.googleapis.com/resource_name": "fluentd-cloud-logging-gke-mlp-29fed122-node-xpt9",
      "container.googleapis.com/instance_id": "3044771269853068901",
      "container.googleapis.com/pod_name": "rainbow-dash-658671670-qlm1i",
      "compute.googleapis.com/resource_id": "3044771269853068901",
      "container.googleapis.com/stream": "stdout",
      "container.googleapis.com/namespace_name": "default",
      "container.googleapis.com/container_name": "rainbow-dash"
    },
    "timestamp": "2016-07-13T11:34:18.000Z",
    "projectNumber": "1014870031406"
  },
  "insertId": "xut21yg1zaougl",
  "log": "rainbow-dash",
  "structPayload": {
    "event_type": "booking",
    "user": "fox@yourgolftravel.com",
    "service": "booking",
    "correlation_id": "bf6f5ea3-614b-42f5-8e73-43deea2d1838",
    "timestamp": "2016-07-13T11:34:18.448Z",
    "booking": {
      "notes": "",
      "teeTimes": [
        {
          "courseId": "31415-926-5358979323",
          "pax": 2,
          "timeId": "31415-926-5358979323:1130021520081208191610170003000000",
          "reservationId": "31415-926-0002890450",
          "date": "2016-10-17T00:00:00.000Z"
        },
        {
          "courseId": "27182-818-2845904523",
          "pax": 2,
          "timeId": "44005-204-0000000001:1102021240060606131610180005000000",
          "reservationId": "27182-818-0002890451",
          "date": "2016-10-18T00:00:00.000Z"
        }
      ],
      "sessionId": "14142-300-0000995250",
      "venueId": "14142-135-6237309504"
    }
  }
}
```

The logs in StackDriver are divided into two sections, the first of these - 'metadata' - is provided by the platform, this includes the severity: 'INFO' in this case; and the location of the source of the log: a Docker service running on a GKE cluster.

The application's part of the log StackDriver refers to as the 'structPayload' - for this we decided on certain constant attributes (event_type, user, service, timestamp, correlation_id) and we then augment them with other attributes that are entirely event specific e.g. booking details.

Although your logs are probably not using StackDriver, the format of your logs will probably look somewhat similar - there will be some universal things that you want: the severity, the timestamp, the name of the service that produced the log, etc. together with some log event specific data that cannot be determined in advance.

# LICENSE

This work is licensed under the MIT license - see the [LICENSE](LICENSE) file for further details.
