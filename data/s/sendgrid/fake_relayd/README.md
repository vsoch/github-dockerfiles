## fake_relayd

fake_relayd is a simple TCP server to mimic some of relayd functionalities. fake_relayd allows the user to test at the black box level by generating some of the relayd error responses by setting specific details base64 encoded in ips field:

* Disconnect on request
* Return internal error (throttle error, hourly limits reached, etc.)
* Return external errors (connection timed out, connection refused)
* Delay before replying

## How To Install

```bash
go get github.com/sendgrid/fake_relayd
```

## Use Case

Generate request as shown in below examples where ips field has base64 encoded values with error specific details

## Usage

Start the server

```
go run main.go
```

**Disconnect on request**
Set mxdomain=2s-disconnect-domain.com
Set ips field as {"connection_delay":"2s", "error_message":"no response", "error_source":"", "ipchosen":"172.16.8.21"}
Create the request as below with base64 encoded value of ips field, the request will disconnect without any response after 2 seconds

```
$ (echo '{"mxdomain":"2s-disconnect-domain.com", "userid":180, "ips":["eyJjb25uZWN0aW9uX2RlbGF5IjoiMnMiLCAiZXJyb3JfbWVzc2FnZSI6Im5vIHJlc3BvbnNlIiwgImVycm9yX3NvdXJjZSI6IiIsICJpcGNob3NlbiI6IjE3Mi4xNi44LjIxIn0="], "mxport":25, "mxip":"172.16.5.1"}' && cat) | telnet 0.0.0.0 50171
Trying 0.0.0.0...
Connected to 0.0.0.0.
Escape character is '^]'.

<2 second wait ...>
Connection closed by foreign host.
```

**Error response - internal, with 25s delay**
Set mxdomain=25s-delay-internal-error.com
Set ips field as {"connection_delay":"25s", "error_message":"some internal error", "error_source":"internal", "ipchosen":"172.16.8.21"}
Create the request as below with base64 encoded value of ips field, the request will generate an internal error response after 25s

```
$ (echo '{"mxdomain":"25s-delay-internal-error.com", "userid":180, "ips":["eyJjb25uZWN0aW9uX2RlbGF5IjoiMjVzIiwgImVycm9yX21lc3NhZ2UiOiJzb21lIGludGVybmFsIGVycm9yIiwgImVycm9yX3NvdXJjZSI6ImludGVybmFsIiwgImlwY2hvc2VuIjoiMTcyLjE2LjguMjEifQ=="], "mxport":25, "mxip":"172.16.5.1"}' && cat) | telnet 0.0.0.0 50171
Trying 0.0.0.0...
Connected to 0.0.0.0.
Escape character is '^]'.

<25 second wait ...>

{"error":"some internal error","error_source":"internal"}
```

**Error response - external, with 25s delay**
Set mxdomain=25s-delay-external-error.com
Set ips field as {"connection_delay":"25s", "error_message":"some external error", "error_source":"external", "ipchosen":"172.16.8.21"}
Create the request as below with base64 encoded value of ips field, the request will generate an external error response after 25s

```
$ (echo '{"mxdomain":"25s-delay-external-error.com", "userid":180, "ips":["eyJjb25uZWN0aW9uX2RlbGF5IjoiMjVzIiwgImVycm9yX21lc3NhZ2UiOiJzb21lIGV4dGVybmFsIGVycm9yIiwgImVycm9yX3NvdXJjZSI6ImV4dGVybmFsIiwgImlwY2hvc2VuIjoiMTcyLjE2LjguMjEifQ=="], "mxport":25, "mxip":"172.16.5.1"}' && cat) | telnet 0.0.0.0 50171
Trying 0.0.0.0...
Connected to 0.0.0.0.
Escape character is '^]'.

<25 second wait ...>

{"error":"some external error","error_source":"external"}
```

**Error response - external, no delay**
Set mxdomain=0s-delay-external-error.com
Set ips field as {"connection_delay":"0s", "error_message":"some external error", "error_source":"external", "ipchosen":"172.16.8.21"}
Create the request as below with base64 encoded value of ips field, the request will generate an external error response with no delay

```
$ (echo '{"mxdomain":"0s-delay-external-error.com", "userid":180, "ips":["eyJjb25uZWN0aW9uX2RlbGF5IjoiMHMiLCAiZXJyb3JfbWVzc2FnZSI6InNvbWUgZXh0ZXJuYWwgZXJyb3IiLCAiZXJyb3Jfc291cmNlIjoiZXh0ZXJuYWwiLCAiaXBjaG9zZW4iOiIxNzIuMTYuOC4yMSJ9"], "mxport":25, "mxip":"172.16.5.1"}' && cat) | telnet 0.0.0.0 50171
Trying 0.0.0.0...
Connected to 0.0.0.0.
Escape character is '^]'.

{"error":"some external error","error_source":"external"}
```

**Error response - smtp**
Set mxdomain=foo-smtp-error.com
Set ips field as {"connection_delay":"10s", "error_message":"foo smtp error", "error_source":"err string", "ipchosen":"1.2.3.4"}
Create the request as below with base64 encoded value of ips field, the request will generate an smtp error response after 10s

```
$ (echo '{"mxdomain":"foo-smtp-error.com", "userid":180, "ips":["eyJjb25uZWN0aW9uX2RlbGF5IjoiMTBzIiwgImVycm9yX21lc3NhZ2UiOiJmb28gc210cCBlcnJvciIsICJlcnJvcl9zb3VyY2UiOiJlcnIgc3RyaW5nIiwgImlwY2hvc2VuIjoiMS4yLjMuNCJ9"], "mxport":25, "mxip":"172.16.5.1"}' && cat) | telnet 0.0.0.0 50171
Trying 0.0.0.0...
Connected to 0.0.0.0.
Escape character is '^]'.

{"error":"foo smtp error","error_source":"err string"}
```

**Internal deferral - one**
Set mxdomain=throttle-internal-deferral.com
Set ips field as {"connection_delay":"0s", "error_message":"Email was deferred due to the following reason(s): [IPs were throttled by recipient server]", "error_source":"internal", "ipchosen":"172.16.8.21"}
Create the request as below with base64 encoded value of ips field, the request will generate an error indicating IPs were throttled by recipient server

```
$ (echo '{"mxdomain":"throttle-internal-deferral.com", "userid":180, "ips":["eyJjb25uZWN0aW9uX2RlbGF5IjoiMHMiLCAiZXJyb3JfbWVzc2FnZSI6IkVtYWlsIHdhcyBkZWZlcnJlZCBkdWUgdG8gdGhlIGZvbGxvd2luZyByZWFzb24ocyk6IFtJUHMgd2VyZSB0aHJvdHRsZWQgYnkgcmVjaXBpZW50IHNlcnZlcl0iLCAiZXJyb3Jfc291cmNlIjoiaW50ZXJuYWwiLCAiaXBjaG9zZW4iOiIxNzIuMTYuOC4yMSJ9"], "mxport":25, "mxip":"172.16.5.1"}' && cat) | telnet 0.0.0.0 50171
Trying 0.0.0.0...
Connected to 0.0.0.0.
Escape character is '^]'.

{"error":"Email was deferred due to the following reason(s): [IPs were throttled by recipient server]","error_source":"internal"}
```

**Internal deferral - two**
Set mxdomain=hourlimit-throttle-internal-deferral.com
Set ips field as {"connection_delay":"0s", "error_message":"Email was deferred due to the following reason(s): [IPs were throttled by recipient server, IPs reached ISP-suggested hourly limits: https://sendgrid.com/docs/Classroom/Troubleshooting/Delivery_Issues/email_was_deferred_due_to_the_following_reasons_ip_deferrals_messages.html]", "error_source":"internal", "ipchosen":"172.16.8.21"}
Create the request as below with base64 encoded value of ips field, the request will return an error indicating some IPs were throttled by recipient server, and the rest were restricted by hourly limit

```
$ (echo '{"mxdomain":"hourlimit-throttle-internal-deferral", "userid":180, "ips":["eyJjb25uZWN0aW9uX2RlbGF5IjoiMHMiLCAiZXJyb3JfbWVzc2FnZSI6IkVtYWlsIHdhcyBkZWZlcnJlZCBkdWUgdG8gdGhlIGZvbGxvd2luZyByZWFzb24ocyk6IFtJUHMgd2VyZSB0aHJvdHRsZWQgYnkgcmVjaXBpZW50IHNlcnZlciwgSVBzIHJlYWNoZWQgSVNQLXN1Z2dlc3RlZCBob3VybHkgbGltaXRzOiBodHRwczovL3NlbmRncmlkLmNvbS9kb2NzL0NsYXNzcm9vbS9Ucm91Ymxlc2hvb3RpbmcvRGVsaXZlcnlfSXNzdWVzL2VtYWlsX3dhc19kZWZlcnJlZF9kdWVfdG9fdGhlX2ZvbGxvd2luZ19yZWFzb25zX2lwX2RlZmVycmFsc19tZXNzYWdlcy5odG1sXSIsICJlcnJvcl9zb3VyY2UiOiJpbnRlcm5hbCIsICJpcGNob3NlbiI6IjE3Mi4xNi44LjIxIn0="], "mxport":25, "mxip":"172.16.5.1"}' && cat) | telnet 0.0.0.0 50171
Trying 0.0.0.0...
Connected to 0.0.0.0.
Escape character is '^]'.

{"error":"Email was deferred due to the following reason(s): [IPs were throttled by recipient server, IPs reached ISP-suggested hourly limits: https://sendgrid.com/docs/Classroom/Troubleshooting/Delivery_Issues/email_was_deferred_due_to_the_following_reasons_ip_deferrals_messages.html]","error_source":"internal"}
```

## Config File

None yet

## Docker Use Cases

You can also use this in docker-compose like so,

```yaml
# fake_relayd

relayd:
    image: docker.sendgrid.net/sendgrid/fake_relayd
    networks:
        network:
            ipv4_address: 172.33.0.101
```

## Sample Logs

Logs show the requesting IP address and the size of the request; error events when handling the request; info event with details of the response

```
{"address":"0.0.0.0:50171","app":"fake_relayd","event":"start","processed":1526362374}
{"app":"fake_relayd","event":"debug","message":"Request of 237 bytes read from 127.0.0.1:56263","processed":1526362378,"remote_addr":"127.0.0.1:56263"}
{"app":"fake_relayd","event":"debug","processed":1526362378,"remote_addr":"127.0.0.1:56263","response_type":"no response"}
{"app":"fake_relayd","event":"debug","message":"Request of 243 bytes read from 127.0.0.1:56405","processed":1526363441,"remote_addr":"127.0.0.1:56405"}
{"app":"fake_relayd","event":"debug","processed":1526363451,"remote_addr":"127.0.0.1:56405","response_type":"foo-smtp-error.com"}
```

## Tests

You can run tests like normal with `$ go test`, however, you can make the tests show application level logging with `$ go test -show_logs`.

## Command Port

fake_relayd listens on the port 6777 that always returns {"response":"done"}.

```
$ telnet localhost 6777
Trying ::1...
Connected to localhost.
Escape character is '^]'.
{"cmd":"limit", "ip":"0.0.0.0", "limit":4000}
{"response":"done"}
"quit"
Connection closed by foreign host.
```
