# Ln v2

Natural Logging, v2, provides a cleaned up API and adherence to the latest SendGrid logging archetype. Required keys such as `processed` time, `app` name, and `event` are ensured to always be present. This logger has dropped support for syslog as these logs should be populated by the `logger` utility in production. The loggerAPI has been cleaned up and is more friendly than before.

### Examples

See [the example code]("https://github.com/sendgrid/ln/blob/master/example/main.go").
```
package main

import (
	"context"

	"github.com/sendgrid/ln/v2"
)

func main() {
	logger := ln.New("my_app")

	logger.Add("persistent key", "here").Add("another key", "there")

	logger.Println("hello, world!")
	/*
		{
		   	"app": "my_app",
		   	"event": "debug",
		   	"message": "hello, world!",
			"persistent key": "here",
			"another key": "there",
		   	"processed": 1505751141
		}
	*/

	logger.PrintKV("my event",
		"key 1", "value 1",
		"key 2", 2,
	)
	/*
		{
		   	"app": "my_app",
		   	"event": "my event",
		   	"key 1": "value 1",
		   	"key 2": 2,
			"persistent key": "here",
			"another key": "there",
		   	"processed": 1505751141
		}
	*/

	foo := EventFoo{"Henry", 42}
	logger.Event("my next event", &foo)
	/*
		{
			"name": "Henry",
			"age": 42,
			"app": "my_app",
			"event": "my next event",
			"processed": 1505753705,
			"persistent key": "here",
			"another key": "there",
		}
	*/

	ctx := logger.CtxAdd(context.Background(), "user_id", 42)
	SomeFunc(ctx)
}

func SomeFunc(ctx context.Context) {
	logger := ln.CtxGet(ctx)
	logger.Println("still here")
	/*
		{
			"app": "my_app",
			"event": "debug",
			"message": "still here",
			"processed": 1505751141,
			"persistent key": "here",
			"another key": "there",
			"user_id": 42
		}
	*/
}

type EventFoo struct {
	Name string `json:"name"`
	Age  int    `json:"age"`
}


```

There is also a level logger! You can do all the things above, but inject a `.Info()`, `.Warn()`, `.Error()`, or `.Debug()` before the print action.

```
logger := ln.New("my_app")
logger.SetLevel(ln.DebugLevel)
logger.Debug().Println("hello, world!")
```

There are also child loggers. They inherit the settings of the parent logger.
```
logger := ln.New("my_app")
child := logger.Child()
```

For testing, you may want to verify that you logged what you wanted. This is easy with `ln`. In your test case, just set create a `ln.NewLockBuffer()` and pass it to `logger.SetOutput()`. Your code will still create all the same logs as before, but your `LockBuffer` will contain the logs.

```
func TestThing(t *testing.T) {
	logBuf := ln.NewLockBuffer()
	logger := ln.New("testing").SetOutput(logBuf)

	functionThatLogs(logger)

	if !strings.Contains(logBuf.String(), "my expected log entry") {
		t.Error("missing expected log entry")
	}

```