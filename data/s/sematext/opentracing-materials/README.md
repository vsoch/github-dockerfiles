# opentracing-materials

[OpenTracing](http://opentracing.io/) aims to provide a consistent and tracer-agnostic API for distributed transaction instrumentation. This repository contains a number of examples and scenarios for different programming languages, frameworks, libraries, etc.

# Getting started

Because OpenTracing is just an API/standard, you need to deploy a distributed tracer that is able to ingest/store the spans.

The easiest way to bootstrap a tracer is via Docker. For example, to run the [Zipkin](http://zipkin.io/) server inside container:

```bash
$  docker run -d –name zipkin -p 9411:9411 openzipkin/zipkin
```

After that, Docker daemon will expose the port 9411 on the host machine so you can browse the UI on http://localhost:9411 and explore the traces.

![zipkin ui](https://github.com/sematext/opentracing-materials/blob/master/zipkin-ui.png)

# Java

## opentracing-common

Thin abstraction layer atop OpenTracing API that deals with tracer's initialization, span creation, context injection/extraction, etc. To build the artifact use `mvn`:

```bash
$ mvn clean install
```
Include as dependency in your `pom.xml`:

```
<dependency>
  <groupId>com.sematext.opentracing</groupId>
  <artifactId>opentracing-common</artifactId>
  <version>1.0-SNAPSHOT</version>
</dependency>
```

Tracer's initialization is done via `TracerInitializer` implementation. See the example below:

```java
TracerInitializer tracerInitializer = new TracerInitializer(Tracers.ZIPKIN);
tracerInitializer.setup("localhost", 9411, "component-name");
```
Use `SpanTemplate` to start a span:

```java
SpanOperations spanOps = new SpanTemplate();

try (ActiveSpan span = spanOps.startActive("create-app")) {
    span.setTag("db.instance", "apps");
    span.setTag("db.type", "sql");
    span.setTag("db.statement", sql);
    jdbcTemplate.update(sql, Collections.singletonMap("name", name));
}
```

## opentracing-jdbc

Spring Boot app that demonstrates how to trace JDBC calls. It exposes a REST API with these two operations:

- **GET** /app (lists current apps)
- **POST** /app/{name} (adds a new app)

Run it with `mvn spring-boot:run`.

The info about apps is persisted in an embedded **H2** database. Use the following commands to see how they trigger the creation of spans with associated OpenTracing tags:

```bash
$ curl -v -XPOST http://localhost:8080/app/slack
$ curl -v -XGET http://localhost:8080/app
```
## opentracing-{injector,extractor}

Demonstrates context propagation capabilities across JVM process boundaries. `opentracing-injector` encodes and injects the span context into HTTP headers (it actually injects `trace` and `span` identifiers). Then, it makes an HTTP request to `opentracing-extractor` which decodes the headers and constructs a propagated span context. The parent span context is used to start a new span inside the trace.

![ctx propagation](https://github.com/sematext/opentracing-materials/blob/master/inject-extract.png)

# Python

Install the needed dependencies:

```bash
$ pip install -r requierements.txt
```

**NOTE:** Jaeger Python client is not compatible with Python **3** (although there is work in progress to fix that). You'll need to run `pip install` against Python **2.7**. If you want to avoid altering your current Python env, please consider using [virtualenv](https://virtualenv.pypa.io/en/stable/).

## initializer.py

Module that encapsulates common tasks related to tracer initialization/registration. Tracer initialization is done via `TracerInitializer` class:

```python
initializer = TracerInitializer('jaeger')
initializer.setup('localhost', 5775, 'opentracing-python')
```

## basic.py

A trivial example of using OpenTracing API. Starts a single span, attaches some tags to it and sends it to the tracer.

## flask_tracing.py

This module bootstraps a simple Flask app. You can start it with:

```bash
$ python2.7 flask_tracing.py
[2017-08-21 14:43:26.038214] INFO: flask-opentracing: jaeger tracer initialized on endpoint localhost:5775
[2017-08-21 14:43:26.042258] INFO: flask-opentracing: Tracing single endpoint. Browse to http://localhost:5000/api/octi
```

This will instrument the endpoints that are annotated with `@tracer.trace`. If you want to instrument all available endpoints, pass the `--trace-all` flag:

```bash
$ python2.7 flask_tracing.py --trace-all
[2017-08-21 14:46:28.128563] INFO: flask-opentracing: jaeger tracer initialized on endpoint localhost:5775
[2017-08-21 14:46:28.132731] INFO: flask-opentracing: Tracing all endpoints. Browse to http://localhost:5000/api/octi
```

