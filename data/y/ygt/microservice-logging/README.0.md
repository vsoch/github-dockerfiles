# Ruby JSON logger

This library provides a minimal JSON logging interface suitable for use in microservices - see the parent project [here](https://github.com/ygt/microservice-logging)

## Install

	gem install microservice_logging

## Examples of use

Examples of use can be found in the tests.

Instantiate a new logger like this:
	
	require 'microservices_logging'
	require 'time'
	
	MY_EVENTS = [
		:http_request,
		:exception,
		:startup,
		:my_event,
		:my_other_event
	]
	
	log = MicroservicesLogger.new(
		:service_name => 'my_super_service',
		:clock = Time,
		:output => $stdout,
		:events => MY_EVENTS
	)

You can then use the logger by invoking it like so:

	log.startup.error({ message: "Emergency! There's an Emergency going on" })
	
This will output:

	{"service":"my super service","timestamp":1468333486800,"event_type":"startup","severity":"ERROR","message":"Emergency! There's an Emergency going on"}

Although, obviously, the timestamp attribute will be different - this is the number of seconds since the epoch, in case you were wondering. If you want to add specific information (like request data) you can do so like this:

	log.http_request.info({
		correlation_id: '6889828a-6708-46f7-beec-870cf7b4ab6f',
		request: { method: 'GET' },
		response: { status_code: 200 }
	})

Which prints:

	{"service":"my super service","timestamp":1468333607265,"event_type":"http_request","severity":"INFO","correlation_id":"6889828a-6708-46f7-beec-870cf7b4ab6f","request":{"method":"GET"},"response":{"status":200}}

# Hacking on the library

Pull Requests are most welcome - if you want to build and run the tests then simply:

	make build check

You will of course need make, Docker, etc.

All PRs that break the test suite will be politely declined :-)

# LICENSE

See [LICENSE](../LICENSE) file in parent project (MIT).
