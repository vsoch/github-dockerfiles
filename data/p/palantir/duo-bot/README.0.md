Package validator
================
<img align="right" src="https://raw.githubusercontent.com/go-playground/validator/v9/logo.png">
[![Join the chat at https://gitter.im/go-playground/validator](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/go-playground/validator?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)
![Project status](https://img.shields.io/badge/version-9.3.5-green.svg)
[![Build Status](https://semaphoreci.com/api/v1/joeybloggs/validator/branches/v9/badge.svg)](https://semaphoreci.com/joeybloggs/validator)
[![Coverage Status](https://coveralls.io/repos/go-playground/validator/badge.svg?branch=v9&service=github)](https://coveralls.io/github/go-playground/validator?branch=v9)
[![Go Report Card](https://goreportcard.com/badge/github.com/go-playground/validator)](https://goreportcard.com/report/github.com/go-playground/validator)
[![GoDoc](https://godoc.org/gopkg.in/go-playground/validator.v9?status.svg)](https://godoc.org/gopkg.in/go-playground/validator.v9)
![License](https://img.shields.io/dub/l/vibe-d.svg)

Package validator implements value validations for structs and individual fields based on tags.

It has the following **unique** features:

-   Cross Field and Cross Struct validations by using validation tags or custom validators.  
-   Slice, Array and Map diving, which allows any or all levels of a multidimensional field to be validated.  
-   Handles type interface by determining it's underlying type prior to validation.
-   Handles custom field types such as sql driver Valuer see [Valuer](https://golang.org/src/database/sql/driver/types.go?s=1210:1293#L29)
-   Alias validation tags, which allows for mapping of several validations to a single tag for easier defining of validations on structs
-   Extraction of custom defined Field Name e.g. can specify to extract the JSON name while validating and have it available in the resulting FieldError
-   Customizable i18n aware error messages.
-   Default validator for the [gin](https://github.com/gin-gonic/gin) web framework; upgrading from v8 to v9 in gin see [here](https://github.com/go-playground/validator/tree/v9/examples/gin-upgrading-overriding)

Installation
------------

Use go get.

	go get gopkg.in/go-playground/validator.v9

Then import the validator package into your own code.

	import "gopkg.in/go-playground/validator.v9"

Error Return Value
-------

Validation functions return type error

They return type error to avoid the issue discussed in the following, where err is always != nil:

* http://stackoverflow.com/a/29138676/3158232
* https://github.com/go-playground/validator/issues/134

Validator only InvalidValidationError for bad validation input, nil or ValidationErrors as type error; so, in your code all you need to do is check if the error returned is not nil, and if it's not check if error is InvalidValidationError ( if necessary, most of the time it isn't ) type cast it to type ValidationErrors like so:

```go
err := validate.Struct(mystruct)
validationErrors := err.(validator.ValidationErrors)
 ```

Usage and documentation
------

Please see http://godoc.org/gopkg.in/go-playground/validator.v9 for detailed usage docs.

##### Examples:

- [Simple](https://github.com/go-playground/validator/blob/v9/examples/simple/main.go)
- [Custom Field Types](https://github.com/go-playground/validator/blob/v9/examples/custom/main.go)
- [Struct Level](https://github.com/go-playground/validator/blob/v9/examples/struct-level/main.go)
- [Translations & Custom Errors](https://github.com/go-playground/validator/blob/v9/examples/translations/main.go)
- [Gin upgrade and/or override validator](https://github.com/go-playground/validator/tree/v9/examples/gin-upgrading-overriding)
- [wash - an example application putting it all together](https://github.com/bluesuncorp/wash)

Benchmarks
------
###### Run on i5-7600 16 GB DDR4-2400 using Go version go1.8 linux/amd64
```go
BenchmarkFieldSuccess-4                                       	20000000	        74.3 ns/op	       0 B/op	       0 allocs/op
BenchmarkFieldSuccessParallel-4                               	50000000	        31.5 ns/op	       0 B/op	       0 allocs/op
BenchmarkFieldFailure-4                                       	 3000000	       556 ns/op	     208 B/op	       4 allocs/op
BenchmarkFieldFailureParallel-4                               	20000000	        88.7 ns/op	     208 B/op	       4 allocs/op
BenchmarkFieldDiveSuccess-4                                   	 2000000	       630 ns/op	     201 B/op	      11 allocs/op
BenchmarkFieldDiveSuccessParallel-4                           	10000000	       173 ns/op	     201 B/op	      11 allocs/op
BenchmarkFieldDiveFailure-4                                   	 1000000	      1350 ns/op	     412 B/op	      16 allocs/op
BenchmarkFieldDiveFailureParallel-4                           	 5000000	       250 ns/op	     412 B/op	      16 allocs/op
BenchmarkFieldCustomTypeSuccess-4                             	10000000	       202 ns/op	      32 B/op	       2 allocs/op
BenchmarkFieldCustomTypeSuccessParallel-4                     	20000000	        63.5 ns/op	      32 B/op	       2 allocs/op
BenchmarkFieldCustomTypeFailure-4                             	 5000000	       568 ns/op	     208 B/op	       4 allocs/op
BenchmarkFieldCustomTypeFailureParallel-4                     	20000000	        87.5 ns/op	     208 B/op	       4 allocs/op
BenchmarkFieldOrTagSuccess-4                                  	 2000000	       703 ns/op	      16 B/op	       1 allocs/op
BenchmarkFieldOrTagSuccessParallel-4                          	 3000000	       447 ns/op	      16 B/op	       1 allocs/op
BenchmarkFieldOrTagFailure-4                                  	 3000000	       604 ns/op	     224 B/op	       5 allocs/op
BenchmarkFieldOrTagFailureParallel-4                          	 5000000	       353 ns/op	     224 B/op	       5 allocs/op
BenchmarkStructLevelValidationSuccess-4                       	10000000	       190 ns/op	      32 B/op	       2 allocs/op
BenchmarkStructLevelValidationSuccessParallel-4               	30000000	        59.9 ns/op	      32 B/op	       2 allocs/op
BenchmarkStructLevelValidationFailure-4                       	 2000000	       705 ns/op	     304 B/op	       8 allocs/op
BenchmarkStructLevelValidationFailureParallel-4               	10000000	       146 ns/op	     304 B/op	       8 allocs/op
BenchmarkStructSimpleCustomTypeSuccess-4                      	 5000000	       361 ns/op	      32 B/op	       2 allocs/op
BenchmarkStructSimpleCustomTypeSuccessParallel-4              	20000000	       101 ns/op	      32 B/op	       2 allocs/op
BenchmarkStructSimpleCustomTypeFailure-4                      	 1000000	      1210 ns/op	     424 B/op	       9 allocs/op
BenchmarkStructSimpleCustomTypeFailureParallel-4              	10000000	       196 ns/op	     440 B/op	      10 allocs/op
BenchmarkStructFilteredSuccess-4                              	 2000000	       757 ns/op	     288 B/op	       9 allocs/op
BenchmarkStructFilteredSuccessParallel-4                      	10000000	       167 ns/op	     288 B/op	       9 allocs/op
BenchmarkStructFilteredFailure-4                              	 3000000	       619 ns/op	     256 B/op	       7 allocs/op
BenchmarkStructFilteredFailureParallel-4                      	10000000	       134 ns/op	     256 B/op	       7 allocs/op
BenchmarkStructPartialSuccess-4                               	 2000000	       687 ns/op	     256 B/op	       6 allocs/op
BenchmarkStructPartialSuccessParallel-4                       	10000000	       159 ns/op	     256 B/op	       6 allocs/op
BenchmarkStructPartialFailure-4                               	 1000000	      1281 ns/op	     480 B/op	      11 allocs/op
BenchmarkStructPartialFailureParallel-4                       	10000000	       218 ns/op	     480 B/op	      11 allocs/op
BenchmarkStructExceptSuccess-4                                	 1000000	      1041 ns/op	     496 B/op	      12 allocs/op
BenchmarkStructExceptSuccessParallel-4                        	10000000	       140 ns/op	     240 B/op	       5 allocs/op
BenchmarkStructExceptFailure-4                                	 1000000	      1014 ns/op	     464 B/op	      10 allocs/op
BenchmarkStructExceptFailureParallel-4                        	10000000	       201 ns/op	     464 B/op	      10 allocs/op
BenchmarkStructSimpleCrossFieldSuccess-4                      	 5000000	       364 ns/op	      72 B/op	       3 allocs/op
BenchmarkStructSimpleCrossFieldSuccessParallel-4              	20000000	       103 ns/op	      72 B/op	       3 allocs/op
BenchmarkStructSimpleCrossFieldFailure-4                      	 2000000	       789 ns/op	     304 B/op	       8 allocs/op
BenchmarkStructSimpleCrossFieldFailureParallel-4              	10000000	       174 ns/op	     304 B/op	       8 allocs/op
BenchmarkStructSimpleCrossStructCrossFieldSuccess-4           	 3000000	       522 ns/op	      80 B/op	       4 allocs/op
BenchmarkStructSimpleCrossStructCrossFieldSuccessParallel-4   	10000000	       146 ns/op	      80 B/op	       4 allocs/op
BenchmarkStructSimpleCrossStructCrossFieldFailure-4           	 2000000	       879 ns/op	     320 B/op	       9 allocs/op
BenchmarkStructSimpleCrossStructCrossFieldFailureParallel-4   	10000000	       225 ns/op	     320 B/op	       9 allocs/op
BenchmarkStructSimpleSuccess-4                                	10000000	       223 ns/op	       0 B/op	       0 allocs/op
BenchmarkStructSimpleSuccessParallel-4                        	20000000	        63.3 ns/op	       0 B/op	       0 allocs/op
BenchmarkStructSimpleFailure-4                                	 2000000	      1097 ns/op	     424 B/op	       9 allocs/op
BenchmarkStructSimpleFailureParallel-4                        	10000000	       182 ns/op	     424 B/op	       9 allocs/op
BenchmarkStructComplexSuccess-4                               	 1000000	      1362 ns/op	     128 B/op	       8 allocs/op
BenchmarkStructComplexSuccessParallel-4                       	 5000000	       359 ns/op	     128 B/op	       8 allocs/op
BenchmarkStructComplexFailure-4                               	  300000	      6446 ns/op	    3040 B/op	      53 allocs/op
BenchmarkStructComplexFailureParallel-4                       	 1000000	      1203 ns/op	    3040 B/op	      53 allocs/op
```

Complementary Software
----------------------

Here is a list of software that complements using this library either pre or post validation.

* [form](https://github.com/go-playground/form) - Decodes url.Values into Go value(s) and Encodes Go value(s) into url.Values. Dual Array and Full map support.
* [Conform](https://github.com/leebenson/conform) - Trims, sanitizes & scrubs data based on struct tags.

How to Contribute
------

Make a pull request...

License
------
Distributed under MIT License, please see license file within the code for more details.
# YAML support for the Go language

Introduction
------------

The yaml package enables Go programs to comfortably encode and decode YAML
values. It was developed within [Canonical](https://www.canonical.com) as
part of the [juju](https://juju.ubuntu.com) project, and is based on a
pure Go port of the well-known [libyaml](http://pyyaml.org/wiki/LibYAML)
C library to parse and generate YAML data quickly and reliably.

Compatibility
-------------

The yaml package supports most of YAML 1.1 and 1.2, including support for
anchors, tags, map merging, etc. Multi-document unmarshalling is not yet
implemented, and base-60 floats from YAML 1.1 are purposefully not
supported since they're a poor design and are gone in YAML 1.2.

Installation and usage
----------------------

The import path for the package is *gopkg.in/yaml.v2*.

To install it, run:

    go get gopkg.in/yaml.v2

API documentation
-----------------

If opened in a browser, the import path itself leads to the API documentation:

  * [https://gopkg.in/yaml.v2](https://gopkg.in/yaml.v2)

API stability
-------------

The package API for yaml v2 will remain stable as described in [gopkg.in](https://gopkg.in).


License
-------

The yaml package is licensed under the Apache License 2.0. Please see the LICENSE file for details.


Example
-------

```Go
package main

import (
        "fmt"
        "log"

        "gopkg.in/yaml.v2"
)

var data = `
a: Easy!
b:
  c: 2
  d: [3, 4]
`

type T struct {
        A string
        B struct {
                RenamedC int   `yaml:"c"`
                D        []int `yaml:",flow"`
        }
}

func main() {
        t := T{}
    
        err := yaml.Unmarshal([]byte(data), &t)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- t:\n%v\n\n", t)
    
        d, err := yaml.Marshal(&t)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- t dump:\n%s\n\n", string(d))
    
        m := make(map[interface{}]interface{})
    
        err = yaml.Unmarshal([]byte(data), &m)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- m:\n%v\n\n", m)
    
        d, err = yaml.Marshal(&m)
        if err != nil {
                log.Fatalf("error: %v", err)
        }
        fmt.Printf("--- m dump:\n%s\n\n", string(d))
}
```

This example will generate the following output:

```
--- t:
{Easy! {2 [3 4]}}

--- t dump:
a: Easy!
b:
  c: 2
  d: [3, 4]


--- m:
map[a:Easy! b:map[c:2 d:[3 4]]]

--- m dump:
a: Easy!
b:
  c: 2
  d:
  - 3
  - 4
```

# go-colorable

Colorable writer for windows.

For example, most of logger packages doesn't show colors on windows. (I know we can do it with ansicon. But I don't want.)
This package is possible to handle escape sequence for ansi color on windows.

## Too Bad!

![](https://raw.githubusercontent.com/mattn/go-colorable/gh-pages/bad.png)


## So Good!

![](https://raw.githubusercontent.com/mattn/go-colorable/gh-pages/good.png)

## Usage

```go
logrus.SetFormatter(&logrus.TextFormatter{ForceColors: true})
logrus.SetOutput(colorable.NewColorableStdout())

logrus.Info("succeeded")
logrus.Warn("not correct")
logrus.Error("something error")
logrus.Fatal("panic")
```

You can compile above code on non-windows OSs.

## Installation

```
$ go get github.com/mattn/go-colorable
```

# License

MIT

# Author

Yasuhiro Matsumoto (a.k.a mattn)
# go-isatty

[![Build Status](https://travis-ci.org/mattn/go-isatty.svg?branch=master)](https://travis-ci.org/mattn/go-isatty) [![Coverage Status](https://coveralls.io/repos/github/mattn/go-isatty/badge.svg?branch=master)](https://coveralls.io/github/mattn/go-isatty?branch=master)

isatty for golang

## Usage

```go
package main

import (
	"fmt"
	"github.com/mattn/go-isatty"
	"os"
)

func main() {
	if isatty.IsTerminal(os.Stdout.Fd()) {
		fmt.Println("Is Terminal")
	} else if isatty.IsCygwinTerminal(os.Stdout.Fd()) {
		fmt.Println("Is Cygwin/MSYS2 Terminal")
	} else {
		fmt.Println("Is Not Terminal")
	}
}
```

## Installation

```
$ go get github.com/mattn/go-isatty
```

## License

MIT

## Author

Yasuhiro Matsumoto (a.k.a mattn)

## Thanks

* k-takata: base idea for IsCygwinTerminal

    https://github.com/k-takata/go-iscygpty
## locales
<img align="right" src="https://raw.githubusercontent.com/go-playground/locales/master/logo.png">![Project status](https://img.shields.io/badge/version-0.11.1-green.svg)
[![Build Status](https://semaphoreci.com/api/v1/joeybloggs/locales/branches/master/badge.svg)](https://semaphoreci.com/joeybloggs/locales)
[![Go Report Card](https://goreportcard.com/badge/github.com/go-playground/locales)](https://goreportcard.com/report/github.com/go-playground/locales)
[![GoDoc](https://godoc.org/github.com/go-playground/locales?status.svg)](https://godoc.org/github.com/go-playground/locales)
![License](https://img.shields.io/dub/l/vibe-d.svg)
[![Gitter](https://badges.gitter.im/go-playground/locales.svg)](https://gitter.im/go-playground/locales?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

Locales is a set of locales generated from the [Unicode CLDR Project](http://cldr.unicode.org/) which can be used independently or within
an i18n package; these were built for use with, but not exclusive to, [Universal Translator](https://github.com/go-playground/universal-translator).

Features
--------
- [x] Rules generated from the latest [CLDR](http://cldr.unicode.org/index/downloads) data, v30.0.3
- [x] Contains Cardinal, Ordinal and Range Plural Rules
- [x] Contains Month, Weekday and Timezone translations built in
- [x] Contains Date & Time formatting functions
- [x] Contains Number, Currency, Accounting and Percent formatting functions
- [x] Supports the "Gregorian" calendar only ( my time isn't unlimited, had to draw the line somewhere )

Full Tests
--------------------
I could sure use your help adding tests for every locale, it is a huge undertaking and I just don't have the free time to do it all at the moment;
any help would be **greatly appreciated!!!!** please see [issue](https://github.com/go-playground/locales/issues/1) for details.

Installation
-----------

Use go get 

```shell
go get github.com/go-playground/locales
```  

NOTES
--------
You'll notice most return types are []byte, this is because most of the time the results will be concatenated with a larger body
of text and can avoid some allocations if already appending to a byte array, otherwise just cast as string.

Usage
-------
```go
package main

import (
	"fmt"
	"time"

	"github.com/go-playground/locales/currency"
	"github.com/go-playground/locales/en_CA"
)

func main() {

	loc, _ := time.LoadLocation("America/Toronto")
	datetime := time.Date(2016, 02, 03, 9, 0, 1, 0, loc)

	l := en_CA.New()

	// Dates
	fmt.Println(l.FmtDateFull(datetime))
	fmt.Println(l.FmtDateLong(datetime))
	fmt.Println(l.FmtDateMedium(datetime))
	fmt.Println(l.FmtDateShort(datetime))

	// Times
	fmt.Println(l.FmtTimeFull(datetime))
	fmt.Println(l.FmtTimeLong(datetime))
	fmt.Println(l.FmtTimeMedium(datetime))
	fmt.Println(l.FmtTimeShort(datetime))

	// Months Wide
	fmt.Println(l.MonthWide(time.January))
	fmt.Println(l.MonthWide(time.February))
	fmt.Println(l.MonthWide(time.March))
	// ...

	// Months Abbreviated
	fmt.Println(l.MonthAbbreviated(time.January))
	fmt.Println(l.MonthAbbreviated(time.February))
	fmt.Println(l.MonthAbbreviated(time.March))
	// ...

	// Months Narrow
	fmt.Println(l.MonthNarrow(time.January))
	fmt.Println(l.MonthNarrow(time.February))
	fmt.Println(l.MonthNarrow(time.March))
	// ...

	// Weekdays Wide
	fmt.Println(l.WeekdayWide(time.Sunday))
	fmt.Println(l.WeekdayWide(time.Monday))
	fmt.Println(l.WeekdayWide(time.Tuesday))
	// ...

	// Weekdays Abbreviated
	fmt.Println(l.WeekdayAbbreviated(time.Sunday))
	fmt.Println(l.WeekdayAbbreviated(time.Monday))
	fmt.Println(l.WeekdayAbbreviated(time.Tuesday))
	// ...

	// Weekdays Short
	fmt.Println(l.WeekdayShort(time.Sunday))
	fmt.Println(l.WeekdayShort(time.Monday))
	fmt.Println(l.WeekdayShort(time.Tuesday))
	// ...

	// Weekdays Narrow
	fmt.Println(l.WeekdayNarrow(time.Sunday))
	fmt.Println(l.WeekdayNarrow(time.Monday))
	fmt.Println(l.WeekdayNarrow(time.Tuesday))
	// ...

	var f64 float64

	f64 = -10356.4523

	// Number
	fmt.Println(l.FmtNumber(f64, 2))

	// Currency
	fmt.Println(l.FmtCurrency(f64, 2, currency.CAD))
	fmt.Println(l.FmtCurrency(f64, 2, currency.USD))

	// Accounting
	fmt.Println(l.FmtAccounting(f64, 2, currency.CAD))
	fmt.Println(l.FmtAccounting(f64, 2, currency.USD))

	f64 = 78.12

	// Percent
	fmt.Println(l.FmtPercent(f64, 0))

	// Plural Rules for locale, so you know what rules you must cover
	fmt.Println(l.PluralsCardinal())
	fmt.Println(l.PluralsOrdinal())

	// Cardinal Plural Rules
	fmt.Println(l.CardinalPluralRule(1, 0))
	fmt.Println(l.CardinalPluralRule(1.0, 0))
	fmt.Println(l.CardinalPluralRule(1.0, 1))
	fmt.Println(l.CardinalPluralRule(3, 0))

	// Ordinal Plural Rules
	fmt.Println(l.OrdinalPluralRule(21, 0)) // 21st
	fmt.Println(l.OrdinalPluralRule(22, 0)) // 22nd
	fmt.Println(l.OrdinalPluralRule(33, 0)) // 33rd
	fmt.Println(l.OrdinalPluralRule(34, 0)) // 34th

	// Range Plural Rules
	fmt.Println(l.RangePluralRule(1, 0, 1, 0)) // 1-1
	fmt.Println(l.RangePluralRule(1, 0, 2, 0)) // 1-2
	fmt.Println(l.RangePluralRule(5, 0, 8, 0)) // 5-8
}
```

NOTES:
-------
These rules were generated from the [Unicode CLDR Project](http://cldr.unicode.org/), if you encounter any issues
I strongly encourage contributing to the CLDR project to get the locale information corrected and the next time 
these locales are regenerated the fix will come with.

I do however realize that time constraints are often important and so there are two options:

1. Create your own locale, copy, paste and modify, and ensure it complies with the `Translator` interface.
2. Add an exception in the locale generation code directly and once regenerated, fix will be in place.

Please to not make fixes inside the locale files, they WILL get overwritten when the locales are regenerated.

License
------
Distributed under MIT License, please see license file in code for more details.
## universal-translator
<img align="right" src="https://raw.githubusercontent.com/go-playground/universal-translator/master/logo.png">![Project status](https://img.shields.io/badge/version-0.16.0-green.svg)
[![Build Status](https://semaphoreci.com/api/v1/joeybloggs/universal-translator/branches/master/badge.svg)](https://semaphoreci.com/joeybloggs/universal-translator)
[![Coverage Status](https://coveralls.io/repos/github/go-playground/universal-translator/badge.svg)](https://coveralls.io/github/go-playground/universal-translator)
[![Go Report Card](https://goreportcard.com/badge/github.com/go-playground/universal-translator)](https://goreportcard.com/report/github.com/go-playground/universal-translator)
[![GoDoc](https://godoc.org/github.com/go-playground/universal-translator?status.svg)](https://godoc.org/github.com/go-playground/universal-translator)
![License](https://img.shields.io/dub/l/vibe-d.svg)
[![Gitter](https://badges.gitter.im/go-playground/universal-translator.svg)](https://gitter.im/go-playground/universal-translator?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge)

Universal Translator is an i18n Translator for Go/Golang using CLDR data + pluralization rules

Why another i18n library?
--------------------------
Because none of the plural rules seem to be correct out there, including the previous implementation of this package,
so I took it upon myself to create [locales](https://github.com/go-playground/locales) for everyone to use; this package 
is a thin wrapper around [locales](https://github.com/go-playground/locales) in order to store and translate text for 
use in your applications.

Features
--------
- [x] Rules generated from the [CLDR](http://cldr.unicode.org/index/downloads) data, v30.0.3
- [x] Contains Cardinal, Ordinal and Range Plural Rules
- [x] Contains Month, Weekday and Timezone translations built in
- [x] Contains Date & Time formatting functions
- [x] Contains Number, Currency, Accounting and Percent formatting functions
- [x] Supports the "Gregorian" calendar only ( my time isn't unlimited, had to draw the line somewhere )
- [x] Support loading translations from files
- [x] Exporting translations to file(s), mainly for getting them professionally translated
- [ ] Code Generation for translation files -> Go code.. i.e. after it has been professionally translated
- [ ] Tests for all languages, I need help with this, please see [here](https://github.com/go-playground/locales/issues/1)

Installation
-----------

Use go get 

```shell
go get github.com/go-playground/universal-translator
```

Usage & Documentation
-------

Please see https://godoc.org/github.com/go-playground/universal-translator for usage docs

##### Examples:

- [Basic](https://github.com/go-playground/universal-translator/tree/master/examples/basic)
- [Full - no files](https://github.com/go-playground/universal-translator/tree/master/examples/full-no-files)
- [Full - with files](https://github.com/go-playground/universal-translator/tree/master/examples/full-with-files)

File formatting
--------------
All types, Plain substitution, Cardinal, Ordinal and Range translations can all be contained withing the same file(s);
they are only separated for easy viewing.

##### Examples:

- [Formats](https://github.com/go-playground/universal-translator/tree/master/examples/file-formats)

##### Basic Makeup
NOTE: not all fields are needed for all translation types, see [examples](https://github.com/go-playground/universal-translator/tree/master/examples/file-formats)
```json
{
    "locale": "en",
    "key": "days-left",
    "trans": "You have {0} day left.",
    "type": "Cardinal",
    "rule": "One",
    "override": false
}
```
|Field|Description|
|---|---|
|locale|The locale for which the translation is for.|
|key|The translation key that will be used to store and lookup each translation; normally it is a string or integer.|
|trans|The actual translation text.|
|type|The type of translation Cardinal, Ordinal, Range or "" for a plain substitution(not required to be defined if plain used)|
|rule|The plural rule for which the translation is for eg. One, Two, Few, Many or Other.(not required to be defined if plain used)|
|override|If you wish to override an existing translation that has already been registered, set this to 'true'. 99% of the time there is no need to define it.|

Help With Tests
---------------
To anyone interesting in helping or contributing, I sure could use some help creating tests for each language.
Please see issue [here](https://github.com/go-playground/locales/issues/1) for details.

License
------
Distributed under MIT License, please see license file in code for more details.
# errors [![Travis-CI](https://travis-ci.org/pkg/errors.svg)](https://travis-ci.org/pkg/errors) [![AppVeyor](https://ci.appveyor.com/api/projects/status/b98mptawhudj53ep/branch/master?svg=true)](https://ci.appveyor.com/project/davecheney/errors/branch/master) [![GoDoc](https://godoc.org/github.com/pkg/errors?status.svg)](http://godoc.org/github.com/pkg/errors) [![Report card](https://goreportcard.com/badge/github.com/pkg/errors)](https://goreportcard.com/report/github.com/pkg/errors)

Package errors provides simple error handling primitives.

`go get github.com/pkg/errors`

The traditional error handling idiom in Go is roughly akin to
```go
if err != nil {
        return err
}
```
which applied recursively up the call stack results in error reports without context or debugging information. The errors package allows programmers to add context to the failure path in their code in a way that does not destroy the original value of the error.

## Adding context to an error

The errors.Wrap function returns a new error that adds context to the original error. For example
```go
_, err := ioutil.ReadAll(r)
if err != nil {
        return errors.Wrap(err, "read failed")
}
```
## Retrieving the cause of an error

Using `errors.Wrap` constructs a stack of errors, adding context to the preceding error. Depending on the nature of the error it may be necessary to reverse the operation of errors.Wrap to retrieve the original error for inspection. Any error value which implements this interface can be inspected by `errors.Cause`.
```go
type causer interface {
        Cause() error
}
```
`errors.Cause` will recursively retrieve the topmost error which does not implement `causer`, which is assumed to be the original cause. For example:
```go
switch err := errors.Cause(err).(type) {
case *MyError:
        // handle specifically
default:
        // unknown error
}
```

[Read the package documentation for more information](https://godoc.org/github.com/pkg/errors).

## Contributing

We welcome pull requests, bug fixes and issue reports. With that said, the bar for adding new symbols to this package is intentionally set high.

Before proposing a change, please discuss your change by raising an issue.

## Licence

BSD-2-Clause
[![Build Status](https://travis-ci.org/valyala/bytebufferpool.svg)](https://travis-ci.org/valyala/bytebufferpool)
[![GoDoc](https://godoc.org/github.com/valyala/bytebufferpool?status.svg)](http://godoc.org/github.com/valyala/bytebufferpool)
[![Go Report](http://goreportcard.com/badge/valyala/bytebufferpool)](http://goreportcard.com/report/valyala/bytebufferpool)

# bytebufferpool

An implementation of a pool of byte buffers with anti-memory-waste protection.

The pool may waste limited amount of memory due to fragmentation.
This amount equals to the maximum total size of the byte buffers
in concurrent use.

# Benchmark results
Currently bytebufferpool is fastest and most effective buffer pool written in Go.

You can find results [here](https://omgnull.github.io/go-benchmark/buffer/).

# bytebufferpool users

* [fasthttp](https://github.com/valyala/fasthttp)
* [quicktemplate](https://github.com/valyala/quicktemplate)
fasttemplate
============

Simple and fast template engine for Go.

Fasttemplate peforms only a single task - it substitutes template placeholders
with user-defined values. At high speed :)

Take a look at [quicktemplate](https://github.com/valyala/quicktemplate) if you  need fast yet powerful html template engine.

*Please note that fasttemplate doesn't do any escaping on template values
unlike [html/template](http://golang.org/pkg/html/template/) do. So values
must be properly escaped before passing them to fasttemplate.*

Fasttemplate is faster than [text/template](http://golang.org/pkg/text/template/),
[strings.Replace](http://golang.org/pkg/strings/#Replace),
[strings.Replacer](http://golang.org/pkg/strings/#Replacer)
and [fmt.Fprintf](https://golang.org/pkg/fmt/#Fprintf) on placeholders' substitution.

Below are benchmark results comparing fasttemplate performance to text/template,
strings.Replace, strings.Replacer and fmt.Fprintf:

```
$ go test -bench=. -benchmem
PASS
BenchmarkFmtFprintf-4                   	 2000000	       790 ns/op	       0 B/op	       0 allocs/op
BenchmarkStringsReplace-4               	  500000	      3474 ns/op	    2112 B/op	      14 allocs/op
BenchmarkStringsReplacer-4              	  500000	      2657 ns/op	    2256 B/op	      23 allocs/op
BenchmarkTextTemplate-4                 	  500000	      3333 ns/op	     336 B/op	      19 allocs/op
BenchmarkFastTemplateExecuteFunc-4      	 5000000	       349 ns/op	       0 B/op	       0 allocs/op
BenchmarkFastTemplateExecute-4          	 3000000	       383 ns/op	       0 B/op	       0 allocs/op
BenchmarkFastTemplateExecuteFuncString-4	 3000000	       549 ns/op	     144 B/op	       1 allocs/op
BenchmarkFastTemplateExecuteString-4    	 3000000	       572 ns/op	     144 B/op	       1 allocs/op
BenchmarkFastTemplateExecuteTagFunc-4   	 2000000	       743 ns/op	     144 B/op	       3 allocs/op
```


Docs
====

See http://godoc.org/github.com/valyala/fasttemplate .


Usage
=====

```go
	template := "http://{{host}}/?q={{query}}&foo={{bar}}{{bar}}"
	t := fasttemplate.New(template, "{{", "}}")
	s := t.ExecuteString(map[string]interface{}{
		"host":  "google.com",
		"query": url.QueryEscape("hello=world"),
		"bar":   "foobar",
	})
	fmt.Printf("%s", s)

	// Output:
	// http://google.com/?q=hello%3Dworld&foo=foobarfoobar
```


Advanced usage
==============

```go
	template := "Hello, [user]! You won [prize]!!! [foobar]"
	t, err := fasttemplate.NewTemplate(template, "[", "]")
	if err != nil {
		log.Fatalf("unexpected error when parsing template: %s", err)
	}
	s := t.ExecuteFuncString(func(w io.Writer, tag string) (int, error) {
		switch tag {
		case "user":
			return w.Write([]byte("John"))
		case "prize":
			return w.Write([]byte("$100500"))
		default:
			return w.Write([]byte(fmt.Sprintf("[unknown tag %q]", tag)))
		}
	})
	fmt.Printf("%s", s)

	// Output:
	// Hello, John! You won $100500!!! [unknown tag "foobar"]
```
A [go](http://www.golang.org) (or 'golang' for search engine friendliness) implementation of [JSON Web Tokens](http://self-issued.info/docs/draft-ietf-oauth-json-web-token.html)

[![Build Status](https://travis-ci.org/dgrijalva/jwt-go.svg?branch=master)](https://travis-ci.org/dgrijalva/jwt-go)

**BREAKING CHANGES:*** Version 3.0.0 is here. It includes _a lot_ of changes including a few that break the API.  We've tried to break as few things as possible, so there should just be a few type signature changes.  A full list of breaking changes is available in `VERSION_HISTORY.md`.  See `MIGRATION_GUIDE.md` for more information on updating your code.

**NOTICE:** A vulnerability in JWT was [recently published](https://auth0.com/blog/2015/03/31/critical-vulnerabilities-in-json-web-token-libraries/).  As this library doesn't force users to validate the `alg` is what they expected, it's possible your usage is effected.  There will be an update soon to remedy this, and it will likey require backwards-incompatible changes to the API.  In the short term, please make sure your implementation verifies the `alg` is what you expect.


## What the heck is a JWT?

JWT.io has [a great introduction](https://jwt.io/introduction) to JSON Web Tokens.

In short, it's a signed JSON object that does something useful (for example, authentication).  It's commonly used for `Bearer` tokens in Oauth 2.  A token is made of three parts, separated by `.`'s.  The first two parts are JSON objects, that have been [base64url](http://tools.ietf.org/html/rfc4648) encoded.  The last part is the signature, encoded the same way.

The first part is called the header.  It contains the necessary information for verifying the last part, the signature.  For example, which encryption method was used for signing and what key was used.

The part in the middle is the interesting bit.  It's called the Claims and contains the actual stuff you care about.  Refer to [the RFC](http://self-issued.info/docs/draft-jones-json-web-token.html) for information about reserved keys and the proper way to add your own.

## What's in the box?

This library supports the parsing and verification as well as the generation and signing of JWTs.  Current supported signing algorithms are HMAC SHA, RSA, RSA-PSS, and ECDSA, though hooks are present for adding your own.

## Examples

See [the project documentation](https://godoc.org/github.com/dgrijalva/jwt-go) for examples of usage:

* [Simple example of parsing and validating a token](https://godoc.org/github.com/dgrijalva/jwt-go#example-Parse--Hmac)
* [Simple example of building and signing a token](https://godoc.org/github.com/dgrijalva/jwt-go#example-New--Hmac)
* [Directory of Examples](https://godoc.org/github.com/dgrijalva/jwt-go#pkg-examples)

## Extensions

This library publishes all the necessary components for adding your own signing methods.  Simply implement the `SigningMethod` interface and register a factory method using `RegisterSigningMethod`.  

Here's an example of an extension that integrates with the Google App Engine signing tools: https://github.com/someone1/gcp-jwt-go

## Compliance

This library was last reviewed to comply with [RTF 7519](http://www.rfc-editor.org/info/rfc7519) dated May 2015 with a few notable differences: 

* In order to protect against accidental use of [Unsecured JWTs](http://self-issued.info/docs/draft-ietf-oauth-json-web-token.html#UnsecuredJWT), tokens using `alg=none` will only be accepted if the constant `jwt.UnsafeAllowNoneSignatureType` is provided as the key.

## Project Status & Versioning

This library is considered production ready.  Feedback and feature requests are appreciated.  The API should be considered stable.  There should be very few backwards-incompatible changes outside of major version updates (and only with good reason).

This project uses [Semantic Versioning 2.0.0](http://semver.org).  Accepted pull requests will land on `master`.  Periodically, versions will be tagged from `master`.  You can find all the releases on [the project releases page](https://github.com/dgrijalva/jwt-go/releases).

While we try to make it obvious when we make breaking changes, there isn't a great mechanism for pushing announcements out to users.  You may want to use this alternative package include: `gopkg.in/dgrijalva/jwt-go.v2`.  It will do the right thing WRT semantic versioning.

## Usage Tips

### Signing vs Encryption

A token is simply a JSON object that is signed by its author. this tells you exactly two things about the data:

* The author of the token was in the possession of the signing secret
* The data has not been modified since it was signed

It's important to know that JWT does not provide encryption, which means anyone who has access to the token can read its contents. If you need to protect (encrypt) the data, there is a companion spec, `JWE`, that provides this functionality. JWE is currently outside the scope of this library.

### Choosing a Signing Method

There are several signing methods available, and you should probably take the time to learn about the various options before choosing one.  The principal design decision is most likely going to be symmetric vs asymmetric.

Symmetric signing methods, such as HSA, use only a single secret. This is probably the simplest signing method to use since any `[]byte` can be used as a valid secret. They are also slightly computationally faster to use, though this rarely is enough to matter. Symmetric signing methods work the best when both producers and consumers of tokens are trusted, or even the same system. Since the same secret is used to both sign and validate tokens, you can't easily distribute the key for validation.

Asymmetric signing methods, such as RSA, use different keys for signing and verifying tokens. This makes it possible to produce tokens with a private key, and allow any consumer to access the public key for verification.

### JWT and OAuth

It's worth mentioning that OAuth and JWT are not the same thing. A JWT token is simply a signed JSON object. It can be used anywhere such a thing is useful. There is some confusion, though, as JWT is the most common type of bearer token used in OAuth2 authentication.

Without going too far down the rabbit hole, here's a description of the interaction of these technologies:

* OAuth is a protocol for allowing an identity provider to be separate from the service a user is logging in to.  For example, whenever you use Facebook to log into a different service (Yelp, Spotify, etc), you are using OAuth.
* OAuth defines several options for passing around authentication data. One popular method is called a "bearer token". A bearer token is simply a string that _should_ only be held by an authenticated user. Thus, simply presenting this token proves your identity. You can probably derive from here why a JWT might make a good bearer token.
* Because bearer tokens are used for authentication, it's important they're kept secret. This is why transactions that use bearer tokens typically happen over SSL.
 
## More

Documentation can be found [on godoc.org](http://godoc.org/github.com/dgrijalva/jwt-go).

The command line utility included in this project (cmd/jwt) provides a straightforward example of token creation and parsing as well as a useful tool for debugging your own integration.  You'll also find several implementation examples in to documentation.
# Overview

**duo_client** - Demonstration client to call Duo API methods
with Go.

# Duo Auth API

The Duo Auth API provides a low-level API for adding strong two-factor
authentication to applications that cannot directly display rich web
content.

For more information see the Duo Auth API guide:

<http://www.duosecurity.com/docs/authapi>
# [Echo] (https://echo.labstack.com) [![GoDoc](http://img.shields.io/badge/go-documentation-blue.svg?style=flat-square)](http://godoc.org/github.com/labstack/echo) [![License](http://img.shields.io/badge/license-mit-blue.svg?style=flat-square)](https://raw.githubusercontent.com/labstack/echo/master/LICENSE) [![Build Status](http://img.shields.io/travis/labstack/echo.svg?style=flat-square)](https://travis-ci.org/labstack/echo) [![Coverage Status](http://img.shields.io/coveralls/labstack/echo.svg?style=flat-square)](https://coveralls.io/r/labstack/echo) [![Join the chat at https://gitter.im/labstack/echo](https://img.shields.io/badge/gitter-join%20chat-brightgreen.svg?style=flat-square)](https://gitter.im/labstack/echo) [![Twitter](https://img.shields.io/badge/twitter-@labstack-55acee.svg?style=flat-square)](https://twitter.com/labstack)

## Feature Overview

- Optimized HTTP router which smartly prioritize routes
- Build robust and scalable RESTful APIs
- Group APIs
- Extensible middleware framework
- Define middleware at root, group or route level
- Data binding for JSON, XML and form payload
- Handy functions to send variety of HTTP responses
- Centralized HTTP error handling
- Template rendering with any template engine
- Define your format for the logger
- Highly customizable
- Automatic TLS via Let’s Encrypt
- HTTP/2 support

## Performance

![Performance](https://i.imgur.com/F2V7TfO.png)

## [Get Started](https://echo.labstack.com/guide)

## Support Us

- :star: the project
- [Donate](https://echo.labstack.com/support-echo)
- :earth_americas: spread the word
- [Contribute](#contribute) to the project

## Contribute

**Use issues for everything**

- For a small change, just send a PR.
- For bigger changes open an issue for discussion before sending a PR.
- PR should have:
  - Test case
  - Documentation
  - Example (If it makes sense)
- You can also contribute by:
  - Reporting issues
  - Suggesting new features or enhancements
  - Improve/fix documentation

## Credits
- [Vishal Rana](https://github.com/vishr) - Author
- [Nitin Rana](https://github.com/nr17) - Consultant
- [Contributors](https://github.com/labstack/echo/graphs/contributors)

## License

[MIT](https://github.com/labstack/echo/blob/master/LICENSE)
# Color

Style terminal text.

## Installation

```sh
go get github.com/labstack/gommon/color
```

## Windows?

Try [cmder](http://bliker.github.io/cmder) or https://github.com/mattn/go-colorable

## [Usage](https://github.com/labstack/gommon/blob/master/color/color_test.go)

```sh
import github.com/labstack/gommon/color
```

### Colored text

```go
color.Println(color.Black("black"))
color.Println(color.Red("red"))
color.Println(color.Green("green"))
color.Println(color.Yellow("yellow"))
color.Println(color.Blue("blue"))
color.Println(color.Magenta("magenta"))
color.Println(color.Cyan("cyan"))
color.Println(color.White("white"))
color.Println(color.Grey("grey"))
```
![Colored Text](http://i.imgur.com/8RtY1QR.png)

### Colored background

```go
color.Println(color.BlackBg("black background", color.Wht))
color.Println(color.RedBg("red background"))
color.Println(color.GreenBg("green background"))
color.Println(color.YellowBg("yellow background"))
color.Println(color.BlueBg("blue background"))
color.Println(color.MagentaBg("magenta background"))
color.Println(color.CyanBg("cyan background"))
color.Println(color.WhiteBg("white background"))
```
![Colored Background](http://i.imgur.com/SrrS6lw.png)

### Emphasis

```go
color.Println(color.Bold("bold"))
color.Println(color.Dim("dim"))
color.Println(color.Italic("italic"))
color.Println(color.Underline("underline"))
color.Println(color.Inverse("inverse"))
color.Println(color.Hidden("hidden"))
color.Println(color.Strikeout("strikeout"))
```
![Emphasis](http://i.imgur.com/3RSJBbc.png)

### Mix and match

```go
color.Println(color.Green("bold green with white background", color.B, color.WhtBg))
color.Println(color.Red("underline red", color.U))
color.Println(color.Yellow("dim yellow", color.D))
color.Println(color.Cyan("inverse cyan", color.In))
color.Println(color.Blue("bold underline dim blue", color.B, color.U, color.D))
```
![Mix and match](http://i.imgur.com/jWGq9Ca.png)

### Enable/Disable the package

```go
color.Disable()
color.Enable()
```

### New instance

```go
c := New()
c.Green("green")
```
# Bytes

- Format bytes integer to human readable bytes string.
- Parse human readable bytes string to bytes integer.

## Installation

```go
go get github.com/labstack/gommon/bytes
```

## [Usage](https://github.com/labstack/gommon/blob/master/bytes/bytes_test.go)

### Format

```go
println(bytes.Format(13231323))
```

`12.62MB`

### Parse

```go
b, _ = Parse("2M")
println(b)
```

`2097152`
## WORK IN PROGRESS

### Usage

[log_test.go](log_test.go)
Overview [![Build Status](https://travis-ci.org/magiconair/properties.svg?branch=master)](https://travis-ci.org/magiconair/properties)
========

#### Current version: 1.7.2

properties is a Go library for reading and writing properties files.

It supports reading from multiple files or URLs and Spring style recursive
property expansion of expressions like `${key}` to their corresponding value.
Value expressions can refer to other keys like in `${key}` or to environment
variables like in `${USER}`.  Filenames can also contain environment variables
like in `/home/${USER}/myapp.properties`.

Properties can be decoded into structs, maps, arrays and values through
struct tags.

Comments and the order of keys are preserved. Comments can be modified
and can be written to the output.

The properties library supports both ISO-8859-1 and UTF-8 encoded data.

Starting from version 1.3.0 the behavior of the MustXXX() functions is
configurable by providing a custom `ErrorHandler` function. The default has
changed from `panic` to `log.Fatal` but this is configurable and custom
error handling functions can be provided. See the package documentation for
details.

Read the full documentation on [GoDoc](https://godoc.org/github.com/magiconair/properties)   [![GoDoc](https://godoc.org/github.com/magiconair/properties?status.png)](https://godoc.org/github.com/magiconair/properties)

Getting Started
---------------

```go
import (
	"flag"
	"github.com/magiconair/properties"
)

func main() {
	// init from a file
	p := properties.MustLoadFile("${HOME}/config.properties", properties.UTF8)

	// or multiple files
	p = properties.MustLoadFiles([]string{
			"${HOME}/config.properties",
			"${HOME}/config-${USER}.properties",
		}, properties.UTF8, true)

	// or from a map
	p = properties.LoadMap(map[string]string{"key": "value", "abc": "def"})

	// or from a string
	p = properties.MustLoadString("key=value\nabc=def")

	// or from a URL
	p = properties.MustLoadURL("http://host/path")

	// or from multiple URLs
	p = properties.MustLoadURL([]string{
			"http://host/config",
			"http://host/config-${USER}",
		}, true)

	// or from flags
	p.MustFlag(flag.CommandLine)

	// get values through getters
	host := p.MustGetString("host")
	port := p.GetInt("port", 8080)

	// or through Decode
	type Config struct {
		Host    string        `properties:"host"`
		Port    int           `properties:"port,default=9000"`
		Accept  []string      `properties:"accept,default=image/png;image;gif"`
		Timeout time.Duration `properties:"timeout,default=5s"`
	}
	var cfg Config
	if err := p.Decode(&cfg); err != nil {
		log.Fatal(err)
	}
}

```

Installation and Upgrade
------------------------

```
$ go get -u github.com/magiconair/properties
```

License
-------

2 clause BSD license. See [LICENSE](https://github.com/magiconair/properties/blob/master/LICENSE) file for details.

ToDo
----
* Dump contents with passwords and secrets obscured
# mapstructure

mapstructure is a Go library for decoding generic map values to structures
and vice versa, while providing helpful error handling.

This library is most useful when decoding values from some data stream (JSON,
Gob, etc.) where you don't _quite_ know the structure of the underlying data
until you read a part of it. You can therefore read a `map[string]interface{}`
and use this library to decode it into the proper underlying native Go
structure.

## Installation

Standard `go get`:

```
$ go get github.com/mitchellh/mapstructure
```

## Usage & Example

For usage and examples see the [Godoc](http://godoc.org/github.com/mitchellh/mapstructure).

The `Decode` function has examples associated with it there.

## But Why?!

Go offers fantastic standard libraries for decoding formats such as JSON.
The standard method is to have a struct pre-created, and populate that struct
from the bytes of the encoded format. This is great, but the problem is if
you have configuration or an encoding that changes slightly depending on
specific fields. For example, consider this JSON:

```json
{
  "type": "person",
  "name": "Mitchell"
}
```

Perhaps we can't populate a specific structure without first reading
the "type" field from the JSON. We could always do two passes over the
decoding of the JSON (reading the "type" first, and the rest later).
However, it is much simpler to just decode this into a `map[string]interface{}`
structure, read the "type" key, then use something like this library
to decode it into the proper structure.
# Logrus <img src="http://i.imgur.com/hTeVwmJ.png" width="40" height="40" alt=":walrus:" class="emoji" title=":walrus:"/>&nbsp;[![Build Status](https://travis-ci.org/Sirupsen/logrus.svg?branch=master)](https://travis-ci.org/Sirupsen/logrus)&nbsp;[![GoDoc](https://godoc.org/github.com/Sirupsen/logrus?status.svg)](https://godoc.org/github.com/Sirupsen/logrus)

**Seeing weird case-sensitive problems?** See [this
issue](https://github.com/sirupsen/logrus/issues/451#issuecomment-264332021).
This change has been reverted. I apologize for causing this. I greatly
underestimated the impact this would have. Logrus strives for stability and
backwards compatibility and failed to provide that.

Logrus is a structured logger for Go (golang), completely API compatible with
the standard library logger. [Godoc][godoc]. **Please note the Logrus API is not
yet stable (pre 1.0). Logrus itself is completely stable and has been used in
many large deployments. The core API is unlikely to change much but please
version control your Logrus to make sure you aren't fetching latest `master` on
every build.**

Nicely color-coded in development (when a TTY is attached, otherwise just
plain text):

![Colored](http://i.imgur.com/PY7qMwd.png)

With `log.SetFormatter(&log.JSONFormatter{})`, for easy parsing by logstash
or Splunk:

```json
{"animal":"walrus","level":"info","msg":"A group of walrus emerges from the
ocean","size":10,"time":"2014-03-10 19:57:38.562264131 -0400 EDT"}

{"level":"warning","msg":"The group's number increased tremendously!",
"number":122,"omg":true,"time":"2014-03-10 19:57:38.562471297 -0400 EDT"}

{"animal":"walrus","level":"info","msg":"A giant walrus appears!",
"size":10,"time":"2014-03-10 19:57:38.562500591 -0400 EDT"}

{"animal":"walrus","level":"info","msg":"Tremendously sized cow enters the ocean.",
"size":9,"time":"2014-03-10 19:57:38.562527896 -0400 EDT"}

{"level":"fatal","msg":"The ice breaks!","number":100,"omg":true,
"time":"2014-03-10 19:57:38.562543128 -0400 EDT"}
```

With the default `log.SetFormatter(&log.TextFormatter{})` when a TTY is not
attached, the output is compatible with the
[logfmt](http://godoc.org/github.com/kr/logfmt) format:

```text
time="2015-03-26T01:27:38-04:00" level=debug msg="Started observing beach" animal=walrus number=8
time="2015-03-26T01:27:38-04:00" level=info msg="A group of walrus emerges from the ocean" animal=walrus size=10
time="2015-03-26T01:27:38-04:00" level=warning msg="The group's number increased tremendously!" number=122 omg=true
time="2015-03-26T01:27:38-04:00" level=debug msg="Temperature changes" temperature=-4
time="2015-03-26T01:27:38-04:00" level=panic msg="It's over 9000!" animal=orca size=9009
time="2015-03-26T01:27:38-04:00" level=fatal msg="The ice breaks!" err=&{0x2082280c0 map[animal:orca size:9009] 2015-03-26 01:27:38.441574009 -0400 EDT panic It's over 9000!} number=100 omg=true
exit status 1
```

#### Example

The simplest way to use Logrus is simply the package-level exported logger:

```go
package main

import (
  log "github.com/Sirupsen/logrus"
)

func main() {
  log.WithFields(log.Fields{
    "animal": "walrus",
  }).Info("A walrus appears")
}
```

Note that it's completely api-compatible with the stdlib logger, so you can
replace your `log` imports everywhere with `log "github.com/Sirupsen/logrus"`
and you'll now have the flexibility of Logrus. You can customize it all you
want:

```go
package main

import (
  "os"
  log "github.com/Sirupsen/logrus"
)

func init() {
  // Log as JSON instead of the default ASCII formatter.
  log.SetFormatter(&log.JSONFormatter{})

  // Output to stdout instead of the default stderr
  // Can be any io.Writer, see below for File example
  log.SetOutput(os.Stdout)

  // Only log the warning severity or above.
  log.SetLevel(log.WarnLevel)
}

func main() {
  log.WithFields(log.Fields{
    "animal": "walrus",
    "size":   10,
  }).Info("A group of walrus emerges from the ocean")

  log.WithFields(log.Fields{
    "omg":    true,
    "number": 122,
  }).Warn("The group's number increased tremendously!")

  log.WithFields(log.Fields{
    "omg":    true,
    "number": 100,
  }).Fatal("The ice breaks!")

  // A common pattern is to re-use fields between logging statements by re-using
  // the logrus.Entry returned from WithFields()
  contextLogger := log.WithFields(log.Fields{
    "common": "this is a common field",
    "other": "I also should be logged always",
  })

  contextLogger.Info("I'll be logged with common and other field")
  contextLogger.Info("Me too")
}
```

For more advanced usage such as logging to multiple locations from the same
application, you can also create an instance of the `logrus` Logger:

```go
package main

import (
  "github.com/Sirupsen/logrus"
)

// Create a new instance of the logger. You can have any number of instances.
var log = logrus.New()

func main() {
  // The API for setting attributes is a little different than the package level
  // exported logger. See Godoc.
  log.Out = os.Stdout

  // You could set this to any `io.Writer` such as a file
  // file, err := os.OpenFile("logrus.log", os.O_CREATE|os.O_WRONLY, 0666)
  // if err == nil {
  //  log.Out = file
  // } else {
  //  log.Info("Failed to log to file, using default stderr")
  // }

  log.WithFields(logrus.Fields{
    "animal": "walrus",
    "size":   10,
  }).Info("A group of walrus emerges from the ocean")
}
```

#### Fields

Logrus encourages careful, structured logging though logging fields instead of
long, unparseable error messages. For example, instead of: `log.Fatalf("Failed
to send event %s to topic %s with key %d")`, you should log the much more
discoverable:

```go
log.WithFields(log.Fields{
  "event": event,
  "topic": topic,
  "key": key,
}).Fatal("Failed to send event")
```

We've found this API forces you to think about logging in a way that produces
much more useful logging messages. We've been in countless situations where just
a single added field to a log statement that was already there would've saved us
hours. The `WithFields` call is optional.

In general, with Logrus using any of the `printf`-family functions should be
seen as a hint you should add a field, however, you can still use the
`printf`-family functions with Logrus.

#### Default Fields

Often it's helpful to have fields _always_ attached to log statements in an
application or parts of one. For example, you may want to always log the
`request_id` and `user_ip` in the context of a request. Instead of writing
`log.WithFields(log.Fields{"request_id": request_id, "user_ip": user_ip})` on
every line, you can create a `logrus.Entry` to pass around instead:

```go
requestLogger := log.WithFields(log.Fields{"request_id": request_id, user_ip: user_ip})
requestLogger.Info("something happened on that request") # will log request_id and user_ip
requestLogger.Warn("something not great happened")
```

#### Hooks

You can add hooks for logging levels. For example to send errors to an exception
tracking service on `Error`, `Fatal` and `Panic`, info to StatsD or log to
multiple places simultaneously, e.g. syslog.

Logrus comes with [built-in hooks](hooks/). Add those, or your custom hook, in
`init`:

```go
import (
  log "github.com/Sirupsen/logrus"
  "gopkg.in/gemnasium/logrus-airbrake-hook.v2" // the package is named "aibrake"
  logrus_syslog "github.com/Sirupsen/logrus/hooks/syslog"
  "log/syslog"
)

func init() {

  // Use the Airbrake hook to report errors that have Error severity or above to
  // an exception tracker. You can create custom hooks, see the Hooks section.
  log.AddHook(airbrake.NewHook(123, "xyz", "production"))

  hook, err := logrus_syslog.NewSyslogHook("udp", "localhost:514", syslog.LOG_INFO, "")
  if err != nil {
    log.Error("Unable to connect to local syslog daemon")
  } else {
    log.AddHook(hook)
  }
}
```
Note: Syslog hook also support connecting to local syslog (Ex. "/dev/log" or "/var/run/syslog" or "/var/run/log"). For the detail, please check the [syslog hook README](hooks/syslog/README.md).

| Hook  | Description |
| ----- | ----------- |
| [Airbrake "legacy"](https://github.com/gemnasium/logrus-airbrake-legacy-hook) | Send errors to an exception tracking service compatible with the Airbrake API V2. Uses [`airbrake-go`](https://github.com/tobi/airbrake-go) behind the scenes. |
| [Airbrake](https://github.com/gemnasium/logrus-airbrake-hook) | Send errors to the Airbrake API V3. Uses the official [`gobrake`](https://github.com/airbrake/gobrake) behind the scenes. |
| [Amazon Kinesis](https://github.com/evalphobia/logrus_kinesis) | Hook for logging to [Amazon Kinesis](https://aws.amazon.com/kinesis/) |
| [Amqp-Hook](https://github.com/vladoatanasov/logrus_amqp) | Hook for logging to Amqp broker (Like RabbitMQ) |
| [Bugsnag](https://github.com/Shopify/logrus-bugsnag/blob/master/bugsnag.go) | Send errors to the Bugsnag exception tracking service. |
| [DeferPanic](https://github.com/deferpanic/dp-logrus) | Hook for logging to DeferPanic |
| [ElasticSearch](https://github.com/sohlich/elogrus) | Hook for logging to ElasticSearch|
| [Fluentd](https://github.com/evalphobia/logrus_fluent) | Hook for logging to fluentd |
| [Go-Slack](https://github.com/multiplay/go-slack) | Hook for logging to [Slack](https://slack.com) |
| [Graylog](https://github.com/gemnasium/logrus-graylog-hook) | Hook for logging to [Graylog](http://graylog2.org/) |
| [Hiprus](https://github.com/nubo/hiprus) | Send errors to a channel in hipchat. |
| [Honeybadger](https://github.com/agonzalezro/logrus_honeybadger) | Hook for sending exceptions to Honeybadger |
| [InfluxDB](https://github.com/Abramovic/logrus_influxdb) | Hook for logging to influxdb |
| [Influxus] (http://github.com/vlad-doru/influxus) | Hook for concurrently logging to [InfluxDB] (http://influxdata.com/) |
| [Journalhook](https://github.com/wercker/journalhook) | Hook for logging to `systemd-journald` |
| [KafkaLogrus](https://github.com/goibibo/KafkaLogrus) | Hook for logging to kafka |
| [LFShook](https://github.com/rifflock/lfshook) | Hook for logging to the local filesystem |
| [Logentries](https://github.com/jcftang/logentriesrus) | Hook for logging to [Logentries](https://logentries.com/) |
| [Logentrus](https://github.com/puddingfactory/logentrus) | Hook for logging to [Logentries](https://logentries.com/) |
| [Logmatic.io](https://github.com/logmatic/logmatic-go) | Hook for logging to [Logmatic.io](http://logmatic.io/) |
| [Logrusly](https://github.com/sebest/logrusly) | Send logs to [Loggly](https://www.loggly.com/) |
| [Logstash](https://github.com/bshuster-repo/logrus-logstash-hook) | Hook for logging to [Logstash](https://www.elastic.co/products/logstash) |
| [Mail](https://github.com/zbindenren/logrus_mail) | Hook for sending exceptions via mail |
| [Mongodb](https://github.com/weekface/mgorus) | Hook for logging to mongodb |
| [NATS-Hook](https://github.com/rybit/nats_logrus_hook) | Hook for logging to [NATS](https://nats.io) |
| [Octokit](https://github.com/dorajistyle/logrus-octokit-hook) | Hook for logging to github via octokit |
| [Papertrail](https://github.com/polds/logrus-papertrail-hook) | Send errors to the [Papertrail](https://papertrailapp.com) hosted logging service via UDP. |
| [PostgreSQL](https://github.com/gemnasium/logrus-postgresql-hook) | Send logs to [PostgreSQL](http://postgresql.org) |
| [Pushover](https://github.com/toorop/logrus_pushover) | Send error via [Pushover](https://pushover.net) |
| [Raygun](https://github.com/squirkle/logrus-raygun-hook) | Hook for logging to [Raygun.io](http://raygun.io/) |
| [Redis-Hook](https://github.com/rogierlommers/logrus-redis-hook) | Hook for logging to a ELK stack (through Redis) |
| [Rollrus](https://github.com/heroku/rollrus) | Hook for sending errors to rollbar |
| [Scribe](https://github.com/sagar8192/logrus-scribe-hook) | Hook for logging to [Scribe](https://github.com/facebookarchive/scribe)|
| [Sentry](https://github.com/evalphobia/logrus_sentry) | Send errors to the Sentry error logging and aggregation service. |
| [Slackrus](https://github.com/johntdyer/slackrus) | Hook for Slack chat. |
| [Stackdriver](https://github.com/knq/sdhook) | Hook for logging to [Google Stackdriver](https://cloud.google.com/logging/) |
| [Sumorus](https://github.com/doublefree/sumorus) | Hook for logging to [SumoLogic](https://www.sumologic.com/)|
| [Syslog](https://github.com/Sirupsen/logrus/blob/master/hooks/syslog/syslog.go) | Send errors to remote syslog server. Uses standard library `log/syslog` behind the scenes. |
| [TraceView](https://github.com/evalphobia/logrus_appneta) | Hook for logging to [AppNeta TraceView](https://www.appneta.com/products/traceview/) |
| [Typetalk](https://github.com/dragon3/logrus-typetalk-hook) | Hook for logging to [Typetalk](https://www.typetalk.in/) |
| [logz.io](https://github.com/ripcurld00d/logrus-logzio-hook) | Hook for logging to [logz.io](https://logz.io), a Log as a Service using Logstash |

#### Level logging

Logrus has six logging levels: Debug, Info, Warning, Error, Fatal and Panic.

```go
log.Debug("Useful debugging information.")
log.Info("Something noteworthy happened!")
log.Warn("You should probably take a look at this.")
log.Error("Something failed but I'm not quitting.")
// Calls os.Exit(1) after logging
log.Fatal("Bye.")
// Calls panic() after logging
log.Panic("I'm bailing.")
```

You can set the logging level on a `Logger`, then it will only log entries with
that severity or anything above it:

```go
// Will log anything that is info or above (warn, error, fatal, panic). Default.
log.SetLevel(log.InfoLevel)
```

It may be useful to set `log.Level = logrus.DebugLevel` in a debug or verbose
environment if your application has that.

#### Entries

Besides the fields added with `WithField` or `WithFields` some fields are
automatically added to all logging events:

1. `time`. The timestamp when the entry was created.
2. `msg`. The logging message passed to `{Info,Warn,Error,Fatal,Panic}` after
   the `AddFields` call. E.g. `Failed to send event.`
3. `level`. The logging level. E.g. `info`.

#### Environments

Logrus has no notion of environment.

If you wish for hooks and formatters to only be used in specific environments,
you should handle that yourself. For example, if your application has a global
variable `Environment`, which is a string representation of the environment you
could do:

```go
import (
  log "github.com/Sirupsen/logrus"
)

init() {
  // do something here to set environment depending on an environment variable
  // or command-line flag
  if Environment == "production" {
    log.SetFormatter(&log.JSONFormatter{})
  } else {
    // The TextFormatter is default, you don't actually have to do this.
    log.SetFormatter(&log.TextFormatter{})
  }
}
```

This configuration is how `logrus` was intended to be used, but JSON in
production is mostly only useful if you do log aggregation with tools like
Splunk or Logstash.

#### Formatters

The built-in logging formatters are:

* `logrus.TextFormatter`. Logs the event in colors if stdout is a tty, otherwise
  without colors.
  * *Note:* to force colored output when there is no TTY, set the `ForceColors`
    field to `true`.  To force no colored output even if there is a TTY  set the
    `DisableColors` field to `true`. For Windows, see
    [github.com/mattn/go-colorable](https://github.com/mattn/go-colorable).
  * All options are listed in the [generated docs](https://godoc.org/github.com/sirupsen/logrus#TextFormatter).
* `logrus.JSONFormatter`. Logs fields as JSON.
  * All options are listed in the [generated docs](https://godoc.org/github.com/sirupsen/logrus#JSONFormatter).

Third party logging formatters:

* [`logstash`](https://github.com/bshuster-repo/logrus-logstash-hook). Logs fields as [Logstash](http://logstash.net) Events.
* [`prefixed`](https://github.com/x-cray/logrus-prefixed-formatter). Displays log entry source along with alternative layout.
* [`zalgo`](https://github.com/aybabtme/logzalgo). Invoking the P͉̫o̳̼̊w̖͈̰͎e̬͔̭͂r͚̼̹̲ ̫͓͉̳͈ō̠͕͖̚f̝͍̠ ͕̲̞͖͑Z̖̫̤̫ͪa͉̬͈̗l͖͎g̳̥o̰̥̅!̣͔̲̻͊̄ ̙̘̦̹̦.

You can define your formatter by implementing the `Formatter` interface,
requiring a `Format` method. `Format` takes an `*Entry`. `entry.Data` is a
`Fields` type (`map[string]interface{}`) with all your fields as well as the
default ones (see Entries section above):

```go
type MyJSONFormatter struct {
}

log.SetFormatter(new(MyJSONFormatter))

func (f *MyJSONFormatter) Format(entry *Entry) ([]byte, error) {
  // Note this doesn't include Time, Level and Message which are available on
  // the Entry. Consult `godoc` on information about those fields or read the
  // source of the official loggers.
  serialized, err := json.Marshal(entry.Data)
    if err != nil {
      return nil, fmt.Errorf("Failed to marshal fields to JSON, %v", err)
    }
  return append(serialized, '\n'), nil
}
```

#### Logger as an `io.Writer`

Logrus can be transformed into an `io.Writer`. That writer is the end of an `io.Pipe` and it is your responsibility to close it.

```go
w := logger.Writer()
defer w.Close()

srv := http.Server{
    // create a stdlib log.Logger that writes to
    // logrus.Logger.
    ErrorLog: log.New(w, "", 0),
}
```

Each line written to that writer will be printed the usual way, using formatters
and hooks. The level for those entries is `info`.

This means that we can override the standard library logger easily:

```go
logger := logrus.New()
logger.Formatter = &logrus.JSONFormatter{}

// Use logrus for standard log output
// Note that `log` here references stdlib's log
// Not logrus imported under the name `log`.
log.SetOutput(logger.Writer())
```

#### Rotation

Log rotation is not provided with Logrus. Log rotation should be done by an
external program (like `logrotate(8)`) that can compress and delete old log
entries. It should not be a feature of the application-level logger.

#### Tools

| Tool | Description |
| ---- | ----------- |
|[Logrus Mate](https://github.com/gogap/logrus_mate)|Logrus mate is a tool for Logrus to manage loggers, you can initial logger's level, hook and formatter by config file, the logger will generated with different config at different environment.|
|[Logrus Viper Helper](https://github.com/heirko/go-contrib/tree/master/logrusHelper)|An Helper arround Logrus to wrap with spf13/Viper to load configuration with fangs! And to simplify Logrus configuration use some behavior of [Logrus Mate](https://github.com/gogap/logrus_mate). [sample](https://github.com/heirko/iris-contrib/blob/master/middleware/logrus-logger/example) |

#### Testing

Logrus has a built in facility for asserting the presence of log messages. This is implemented through the `test` hook and provides:

* decorators for existing logger (`test.NewLocal` and `test.NewGlobal`) which basically just add the `test` hook
* a test logger (`test.NewNullLogger`) that just records log messages (and does not output any):

```go
logger, hook := NewNullLogger()
logger.Error("Hello error")

assert.Equal(1, len(hook.Entries))
assert.Equal(logrus.ErrorLevel, hook.LastEntry().Level)
assert.Equal("Hello error", hook.LastEntry().Message)

hook.Reset()
assert.Nil(hook.LastEntry())
```

#### Fatal handlers

Logrus can register one or more functions that will be called when any `fatal`
level message is logged. The registered handlers will be executed before
logrus performs a `os.Exit(1)`. This behavior may be helpful if callers need
to gracefully shutdown. Unlike a `panic("Something went wrong...")` call which can be intercepted with a deferred `recover` a call to `os.Exit(1)` can not be intercepted.

```
...
handler := func() {
  // gracefully shutdown something...
}
logrus.RegisterExitHandler(handler)
...
```

#### Thread safety

By default Logger is protected by mutex for concurrent writes, this mutex is invoked when calling hooks and writing logs.
If you are sure such locking is not needed, you can call logger.SetNoLock() to disable the locking.

Situation when locking is not needed includes:

* You have no hooks registered, or hooks calling is already thread-safe.

* Writing to logger.Out is already thread-safe, for example:

  1) logger.Out is protected by locks.

  2) logger.Out is a os.File handler opened with `O_APPEND` flag, and every write is smaller than 4k. (This allow multi-thread/multi-process writing)

     (Refer to http://www.notthewizard.com/2014/06/17/are-files-appends-really-atomic/)
# File system notifications for Go

[![GoDoc](https://godoc.org/github.com/fsnotify/fsnotify?status.svg)](https://godoc.org/github.com/fsnotify/fsnotify) [![Go Report Card](https://goreportcard.com/badge/github.com/fsnotify/fsnotify)](https://goreportcard.com/report/github.com/fsnotify/fsnotify)

fsnotify utilizes [golang.org/x/sys](https://godoc.org/golang.org/x/sys) rather than `syscall` from the standard library. Ensure you have the latest version installed by running:

```console
go get -u golang.org/x/sys/...
```

Cross platform: Windows, Linux, BSD and macOS.

|Adapter   |OS        |Status    |
|----------|----------|----------|
|inotify   |Linux 2.6.27 or later, Android\*|Supported [![Build Status](https://travis-ci.org/fsnotify/fsnotify.svg?branch=master)](https://travis-ci.org/fsnotify/fsnotify)|
|kqueue    |BSD, macOS, iOS\*|Supported [![Build Status](https://travis-ci.org/fsnotify/fsnotify.svg?branch=master)](https://travis-ci.org/fsnotify/fsnotify)|
|ReadDirectoryChangesW|Windows|Supported [![Build status](https://ci.appveyor.com/api/projects/status/ivwjubaih4r0udeh/branch/master?svg=true)](https://ci.appveyor.com/project/NathanYoungman/fsnotify/branch/master)|
|FSEvents  |macOS         |[Planned](https://github.com/fsnotify/fsnotify/issues/11)|
|FEN       |Solaris 11    |[In Progress](https://github.com/fsnotify/fsnotify/issues/12)|
|fanotify  |Linux 2.6.37+ | |
|USN Journals |Windows    |[Maybe](https://github.com/fsnotify/fsnotify/issues/53)|
|Polling   |*All*         |[Maybe](https://github.com/fsnotify/fsnotify/issues/9)|

\* Android and iOS are untested.

Please see [the documentation](https://godoc.org/github.com/fsnotify/fsnotify) and consult the [FAQ](#faq) for usage information.

## API stability

fsnotify is a fork of [howeyc/fsnotify](https://godoc.org/github.com/howeyc/fsnotify) with a new API as of v1.0. The API is based on [this design document](http://goo.gl/MrYxyA). 

All [releases](https://github.com/fsnotify/fsnotify/releases) are tagged based on [Semantic Versioning](http://semver.org/). Further API changes are [planned](https://github.com/fsnotify/fsnotify/milestones), and will be tagged with a new major revision number.

Go 1.6 supports dependencies located in the `vendor/` folder. Unless you are creating a library, it is recommended that you copy fsnotify into `vendor/github.com/fsnotify/fsnotify` within your project, and likewise for `golang.org/x/sys`.

## Contributing

Please refer to [CONTRIBUTING][] before opening an issue or pull request.

## Example

See [example_test.go](https://github.com/fsnotify/fsnotify/blob/master/example_test.go).

## FAQ

**When a file is moved to another directory is it still being watched?**

No (it shouldn't be, unless you are watching where it was moved to).

**When I watch a directory, are all subdirectories watched as well?**

No, you must add watches for any directory you want to watch (a recursive watcher is on the roadmap [#18][]).

**Do I have to watch the Error and Event channels in a separate goroutine?**

As of now, yes. Looking into making this single-thread friendly (see [howeyc #7][#7])

**Why am I receiving multiple events for the same file on OS X?**

Spotlight indexing on OS X can result in multiple events (see [howeyc #62][#62]). A temporary workaround is to add your folder(s) to the *Spotlight Privacy settings* until we have a native FSEvents implementation (see [#11][]).

**How many files can be watched at once?**

There are OS-specific limits as to how many watches can be created:
* Linux: /proc/sys/fs/inotify/max_user_watches contains the limit, reaching this limit results in a "no space left on device" error.
* BSD / OSX: sysctl variables "kern.maxfiles" and "kern.maxfilesperproc", reaching these limits results in a "too many open files" error.

[#62]: https://github.com/howeyc/fsnotify/issues/62
[#18]: https://github.com/fsnotify/fsnotify/issues/18
[#11]: https://github.com/fsnotify/fsnotify/issues/11
[#7]: https://github.com/howeyc/fsnotify/issues/7

[contributing]: https://github.com/fsnotify/fsnotify/blob/master/CONTRIBUTING.md

## Related Projects

* [notify](https://github.com/rjeczalik/notify)
* [fsevents](https://github.com/fsnotify/fsevents)

Go UUID implementation
========================

[![license](http://img.shields.io/badge/license-MIT-blue.svg)](https://raw.githubusercontent.com/twinj/uuid/master/LICENSE)
[![GoDoc](http://godoc.org/github.com/twinj/uuid?status.png)](http://godoc.org/github.com/twinj/uuid)
[![Build Status](https://ci.appveyor.com/api/projects/status/github/twinj/uuid?branch=master&svg=true)](https://ci.appveyor.com/project/myesui/uuid)
[![Build Status](https://travis-ci.org/twinj/uuid.png?branch=master)](https://travis-ci.org/twinj/uuid)
[![Coverage Status](https://coveralls.io/repos/github/twinj/uuid/badge.svg?branch=master)](https://coveralls.io/github/twinj/uuid?branch=master)

**This project is currently pre 1.0.0**

This package provides RFC 4122 and DCE 1.1 compliant UUIDs.
It will generate the following:

* Version 1: based on a Timestamp and MAC address as Node id
* Version 2: based on DCE Security - Experimental
* Version 3: based on MD5 hash
* Version 4: based on cryptographically secure random numbers
* Version 5: based on SHA-1 hash

Functions NewV1, NewV2, NewV3, NewV4, NewV5, New, NewHex and Parse() for
generating version 1, 2, 3, 4 and 5 Uuid's

# Requirements

Any supported version of Go.

# Design considerations

* V1 UUIDs should be properly sequential. This can cause the Generator to work
more slowly compared to other implementations. It can however be manually tuned
to have performance that is on par. This is achieved by setting the Timestamp
Resolution. Benchmark tests have been provided to help determine the best
setting for your server

    Proper test coverage has determined thant the UUID timestamp spinner works
    correctly, across multiple clock resolutions. The generator produces
    timestamps that roll out sequentially and will only modify the clock
    sequence on very rare circumstances.

    It is highly recommended that you register a uuid.Saver if you use V1 or V2
    UUIDs as it will ensure a higher probability of uniqueness.

        Example V1 output:
        5fb1a280-30f0-11e6-9614-005056c00001
        5fb1a281-30f0-11e6-9614-005056c00001
        5fb1a282-30f0-11e6-9614-005056c00001
        5fb1a283-30f0-11e6-9614-005056c00001
        5fb1a284-30f0-11e6-9614-005056c00001
        5fb1a285-30f0-11e6-9614-005056c00001
        5fb1a286-30f0-11e6-9614-005056c00001
        5fb1a287-30f0-11e6-9614-005056c00001
        5fb1a288-30f0-11e6-9614-005056c00001
        5fb1a289-30f0-11e6-9614-005056c00001
        5fb1a28a-30f0-11e6-9614-005056c00001
        5fb1a28b-30f0-11e6-9614-005056c00001
        5fb1a28c-30f0-11e6-9614-005056c00001
        5fb1a28d-30f0-11e6-9614-005056c00001
        5fb1a28e-30f0-11e6-9614-005056c00001
        5fb1a28f-30f0-11e6-9614-005056c00001
        5fb1a290-30f0-11e6-9614-005056c00001

* The V1 UUID generator should work on all app servers
    To achieve this there are no Os locking threads or file system dependant
    storage. The uuid.Saver interface exists for the user to provide their own
    storage implementations. The package provides a uuid.Saver
    which works on a standard OS environment.
* The V4 UUID should allow the user to choose how to handle any error that
can occur in the CPRNG. The default is to panic.
* The package should be able to handle multiple instances of Generator's so a
* user can produce UUIDs from multiple sources.

# Recent Changes

* Added ability for user defined Generator's which can be setup with your own
retrieval functions for a Node Id, Timestamp and Random data for a UUID; more
details in docs.
* Now builds in Windows, OsX and Linux, with test coverage checking and code
quality checks.
* Added V2 UUIDs
* Improved builds and 100% test coverage
* Library overhaul to cleanup exports that are not useful for a user
* Improved and fixed file system uuid.Saver interface, breaking changes.
    To use a uuid.Saver make sure you pass it in via the
    uuid.RegisterSaver(Saver) function before a UUID is generated, so as to
    take affect. This is because only one attempt at system initialisation can
    be attempted.

## Installation

Use the `go` tool:

	$ go get github.com/twinj/uuid

# Typical Usage

See [documentation and examples](http://godoc.org/github.com/twinj/uuid)
for more information.

## All UUIDs

    import "github.com/twinj/uuid"

    id, _ := uuid.Parse("6ba7b810-9dad-11d1-80b4-00c04fd430c8")

    if uuid.Equal(id, uuid.NameSpaceDNS) {
        fmt.Println("Alas these are equal")
    }

    if uuid.Compare(id, uuid.NameSpaceDNS) == 0 {
        fmt.Println("They are also equal")
    }

    if uuid.Compare(id, uuid.NameSpaceX500) == -1 {
        fmt.Println("id < uuid.NameSpaceX500")
    }

    if uuid.Compare(uuid.NameSpaceX50, id) == 1 {
        fmt.Println("uuid.NameSpaceX500 > id")
    }

    // Default Format is FormatCanonical
    fmt.Println(uuid.Formatter(id, uuid.FormatCanonicalCurly))

    uuid.SwitchFormat(uuid.FormatCanonicalBracket)


## Version 1 and 2 UUIDs

    import "github.com/twinj/uuid"

    // An uuid.Init or uuid.Register* function must be called before any V1 or
    // V2 UUIDs, only needs 1 call.
    uuid.Init()

    id := uuid.NewV1()
    fmt.Println(id)
    fmt.Printf("version %s variant %x: %s\n", u1.Version(), u1.Variant(), id)

    id = uuid.NewV2(uuid.DomainUser)
    fmt.Println(id)
    fmt.Printf("version %s variant %x: %s\n", u1.Version(), u1.Variant(), id)

    // If you wish to register a saving mechanism to keep track of your UUID
    // It is recommeneded to add a Saver so as to reduce risk in UUID
    // collisions
    saver := new(savers.FileSystemSaver)
    saver.Report = true
    saver.Duration = time.Second * 3

    // Must be called before any V1 or V2 UUIDs. Do not call uuid.Init if
    // registering a Saver
    uuid.RegisterSaver(saver)

## Version 3 and 5 UUIDs

    import "github.com/twinj/uuid"

    // Does not need to be called first but is recommended
    uuid.Init()

    id := uuid.NewV3(uuid.NameSpaceURL, uuid.Name("www.example.com"))
    fmt.Println(id)
    fmt.Printf("version %s variant %x: %s\n", u1.Version(), u1.Variant(), id)

    id := uuid.NewV5(uuid.NameSpaceURL, uuid.Name("www.example.com"))
    fmt.Println(id)
    fmt.Printf("version %s variant %x: %s\n", u1.Version(), u1.Variant(), id)

    id = uuid.NewV5(uuid.NameSpaceURL, id)
    fmt.Println(id)
    fmt.Printf("version %s variant %x: %s\n", u1.Version(), u1.Variant(), id)

## Version 4 UUIDs

    import "github.com/twinj/uuid"

    // Does not need to be called first but is recommended
    uuid.Init()

    // A V4 UUID will panic by default if the systems CPRNG fails - this can
    // be changed by registering your own generator
    u4 := uuid.NewV4()
    fmt.Println(id)
    fmt.Printf("version %d variant %x: %s\n", u4.Version(), u4.Variant(), u4)

## Custom Generators

    import "github.com/twinj/uuid"

    // Improve resolution for V1 and 2 UUIDs
    // The resolution correlates to how many ids can be created before waiting
    // for the next unique timestamp. The default is a low 1024, this equates
    // to Ids that can be created in 100 nanoseconds. It is low to encourage
    // you to set it.
    uuid.RegisterGenerator(GeneratorConfig{Resolution: 18465})

    // Provide your own node Id or MAC address
    uuid.RegisterGenerator(GeneratorConfig{
        Id: func() uuid.Node{
            // My Node Id
            // If this returns nil a random one will be generated
        },
    })

    // Replace the default Timestamp spinner with your own.
    uuid.RegisterGenerator(GeneratorConfig{
        Next: func()(uuid.Timestamp){
            // My own Timestamp function...
            // Resolution will become reduendant if you set this.
            // The package will increment the clock sequence if you produce equal Timestamps
        },
    })

    // Replace the default crypto/rand.Read CPRNG with your own.
    uuid.RegisterGenerator(GeneratorConfig{
        Random: func([]byte)(int, error){
            // My CPRNG function...
        },
    })

    // Replace the default error handler for V4 UUIDs. This function is called
    // when there is an error in the CPRNG. The default function causes a panic.
    // You can change that behaviour and handle the error by checking for nil
    // on a NewV4() call.
    //  id := NewV4()
    //  if id == nil {
    //      err := uuid.Error()
    //      // handle error
    //  }
    // Trying again could fix the problem. Errors could be due to a lack of
    // system entropy or some other serious issue. These issues are rare,
    // however, having the tools to handle such issues is important.
    // This approach was taken as each user of this package will want to handle
    // this differently.
    uuid.RegisterGenerator(GeneratorConfig{
        HandleError: func(error)bool{
            // My HandleError function...
            // If this returns true the V4 generator will try again - if it
            //      fails again the NewV4() function will exit with a nil
            // If this returns false the NewV4() function will exit with a nil
        },
    })
    
    // You can also just manage your own completely.
    gen := NewGenerator(GeneratorConfig{})
    
    id := gen.NewV4()
    

## Coverage

* go test -coverprofile cover.out github.com/twinj/uuid
* go tool cover -html=cover.out -o cover.html

## Links

* [RFC 4122](http://www.ietf.org/rfc/rfc4122.txt)
* [DCE 1.1: Authentication and Security Services](http://pubs.opengroup.org/onlinepubs/9629399/apdxa.htm)

## Copyright

Copyright (C) 2016 twinj@github.com
See [LICENSE](https://github.com/twinj/uuid/tree/master/LICENSE)
file for details.
# buffruneio

[![Tests Status](https://travis-ci.org/pelletier/go-buffruneio.svg?branch=master)](https://travis-ci.org/pelletier/go-buffruneio)
[![GoDoc](https://godoc.org/github.com/pelletier/go-buffruneio?status.svg)](https://godoc.org/github.com/pelletier/go-buffruneio)

Buffruneio is a wrapper around bufio to provide buffered runes access with
unlimited unreads.

```go
import "github.com/pelletier/go-buffruneio"
```

## Examples

```go
import (
    "fmt"
    "github.com/pelletier/go-buffruneio"
    "strings"
)

reader := buffruneio.NewReader(strings.NewReader("abcd"))
fmt.Println(reader.ReadRune()) // 'a'
fmt.Println(reader.ReadRune()) // 'b'
fmt.Println(reader.ReadRune()) // 'c'
reader.UnreadRune()
reader.UnreadRune()
fmt.Println(reader.ReadRune()) // 'b'
fmt.Println(reader.ReadRune()) // 'c'
```

## Documentation

The documentation and additional examples are available at
[godoc.org](http://godoc.org/github.com/pelletier/go-buffruneio).

## Contribute

Feel free to report bugs and patches using GitHub's pull requests system on
[pelletier/go-toml](https://github.com/pelletier/go-buffruneio). Any feedback is
much appreciated!

## LICENSE

Copyright (c) 2016 Thomas Pelletier

Permission is hereby granted, free of charge, to any person obtaining a copy of
this software and associated documentation files (the "Software"), to deal in
the Software without restriction, including without limitation the rights to
use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of
the Software, and to permit persons to whom the Software is furnished to do so,
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER
IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN
CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# go-toml

Go library for the [TOML](https://github.com/mojombo/toml) format.

This library supports TOML version
[v0.4.0](https://github.com/toml-lang/toml/blob/master/versions/en/toml-v0.4.0.md)

[![GoDoc](https://godoc.org/github.com/pelletier/go-toml?status.svg)](http://godoc.org/github.com/pelletier/go-toml)
[![license](https://img.shields.io/github/license/pelletier/go-toml.svg)](https://github.com/pelletier/go-toml/blob/master/LICENSE)
[![Build Status](https://travis-ci.org/pelletier/go-toml.svg?branch=master)](https://travis-ci.org/pelletier/go-toml)
[![Coverage Status](https://coveralls.io/repos/github/pelletier/go-toml/badge.svg?branch=master)](https://coveralls.io/github/pelletier/go-toml?branch=master)
[![Go Report Card](https://goreportcard.com/badge/github.com/pelletier/go-toml)](https://goreportcard.com/report/github.com/pelletier/go-toml)

## Features

Go-toml provides the following features for using data parsed from TOML documents:

* Load TOML documents from files and string data
* Easily navigate TOML structure using TomlTree
* Line & column position data for all parsed elements
* Query support similar to JSON-Path
* Syntax errors contain line and column numbers

Go-toml is designed to help cover use-cases not covered by reflection-based TOML parsing:

* Semantic evaluation of parsed TOML
* Informing a user of mistakes in the source document, after it has been parsed
* Programatic handling of default values on a case-by-case basis
* Using a TOML document as a flexible data-store

## Import

    import "github.com/pelletier/go-toml"

## Usage

### Example

Say you have a TOML file that looks like this:

```toml
[postgres]
user = "pelletier"
password = "mypassword"
```

Read the username and password like this:

```go
import (
    "fmt"
    "github.com/pelletier/go-toml"
)

config, err := toml.LoadFile("config.toml")
if err != nil {
    fmt.Println("Error ", err.Error())
} else {
    // retrieve data directly
    user := config.Get("postgres.user").(string)
    password := config.Get("postgres.password").(string)

    // or using an intermediate object
    configTree := config.Get("postgres").(*toml.TomlTree)
    user = configTree.Get("user").(string)
    password = configTree.Get("password").(string)
    fmt.Println("User is ", user, ". Password is ", password)

    // show where elements are in the file
    fmt.Println("User position: %v", configTree.GetPosition("user"))
    fmt.Println("Password position: %v", configTree.GetPosition("password"))

    // use a query to gather elements without walking the tree
    results, _ := config.Query("$..[user,password]")
    for ii, item := range results.Values() {
      fmt.Println("Query result %d: %v", ii, item)
    }
}
```

## Documentation

The documentation and additional examples are available at
[godoc.org](http://godoc.org/github.com/pelletier/go-toml).

## Tools

Go-toml provides two handy command line tools:

* `tomll`: Reads TOML files and lint them.

    ```
    go install github.com/pelletier/go-toml/cmd/tomll
    tomll --help
    ```
* `tomljson`: Reads a TOML file and outputs its JSON representation.

    ```
    go install github.com/pelletier/go-toml/cmd/tomljson
    tomljson --help
    ```

## Contribute

Feel free to report bugs and patches using GitHub's pull requests system on
[pelletier/go-toml](https://github.com/pelletier/go-toml). Any feedback would be
much appreciated!

### Run tests

You have to make sure two kind of tests run:

1. The Go unit tests
2. The TOML examples base

You can run both of them using `./test.sh`.

## License

The MIT License (MIT). Read [LICENSE](LICENSE).
# HCL

[![GoDoc](https://godoc.org/github.com/hashicorp/hcl?status.png)](https://godoc.org/github.com/hashicorp/hcl) [![Build Status](https://travis-ci.org/hashicorp/hcl.svg?branch=master)](https://travis-ci.org/hashicorp/hcl)

HCL (HashiCorp Configuration Language) is a configuration language built
by HashiCorp. The goal of HCL is to build a structured configuration language
that is both human and machine friendly for use with command-line tools, but
specifically targeted towards DevOps tools, servers, etc.

HCL is also fully JSON compatible. That is, JSON can be used as completely
valid input to a system expecting HCL. This helps makes systems
interoperable with other systems.

HCL is heavily inspired by
[libucl](https://github.com/vstakhov/libucl),
nginx configuration, and others similar.

## Why?

A common question when viewing HCL is to ask the question: why not
JSON, YAML, etc.?

Prior to HCL, the tools we built at [HashiCorp](http://www.hashicorp.com)
used a variety of configuration languages from full programming languages
such as Ruby to complete data structure languages such as JSON. What we
learned is that some people wanted human-friendly configuration languages
and some people wanted machine-friendly languages.

JSON fits a nice balance in this, but is fairly verbose and most
importantly doesn't support comments. With YAML, we found that beginners
had a really hard time determining what the actual structure was, and
ended up guessing more often than not whether to use a hyphen, colon, etc.
in order to represent some configuration key.

Full programming languages such as Ruby enable complex behavior
a configuration language shouldn't usually allow, and also forces
people to learn some set of Ruby.

Because of this, we decided to create our own configuration language
that is JSON-compatible. Our configuration language (HCL) is designed
to be written and modified by humans. The API for HCL allows JSON
as an input so that it is also machine-friendly (machines can generate
JSON instead of trying to generate HCL).

Our goal with HCL is not to alienate other configuration languages.
It is instead to provide HCL as a specialized language for our tools,
and JSON as the interoperability layer.

## Syntax

For a complete grammar, please see the parser itself. A high-level overview
of the syntax and grammar is listed here.

  * Single line comments start with `#` or `//`

  * Multi-line comments are wrapped in `/*` and `*/`. Nested block comments
    are not allowed. A multi-line comment (also known as a block comment)
    terminates at the first `*/` found.

  * Values are assigned with the syntax `key = value` (whitespace doesn't
    matter). The value can be any primitive: a string, number, boolean,
    object, or list.

  * Strings are double-quoted and can contain any UTF-8 characters.
    Example: `"Hello, World"`

  * Multi-line strings start with `<<EOF` at the end of a line, and end
    with `EOF` on its own line ([here documents](https://en.wikipedia.org/wiki/Here_document)).
    Any text may be used in place of `EOF`. Example:
```
<<FOO
hello
world
FOO
```

  * Numbers are assumed to be base 10. If you prefix a number with 0x,
    it is treated as a hexadecimal. If it is prefixed with 0, it is
    treated as an octal. Numbers can be in scientific notation: "1e10".

  * Boolean values: `true`, `false`

  * Arrays can be made by wrapping it in `[]`. Example:
    `["foo", "bar", 42]`. Arrays can contain primitives,
    other arrays, and objects. As an alternative, lists
    of objects can be created with repeated blocks, using
    this structure:

    ```hcl
    service {
        key = "value"
    }

    service {
        key = "value"
    }
    ```

Objects and nested objects are created using the structure shown below:

```
variable "ami" {
    description = "the AMI to use"
}
```
This would be equivalent to the following json:
``` json
{
  "variable": {
      "ami": {
          "description": "the AMI to use"
        }
    }
}
```

## Thanks

Thanks to:

  * [@vstakhov](https://github.com/vstakhov) - The original libucl parser
    and syntax that HCL was based off of.

  * [@fatih](https://github.com/fatih) - The rewritten HCL parser
    in pure Go (no goyacc) and support for a printer.
![afero logo-sm](https://cloud.githubusercontent.com/assets/173412/11490338/d50e16dc-97a5-11e5-8b12-019a300d0fcb.png)

A FileSystem Abstraction System for Go

[![Build Status](https://travis-ci.org/spf13/afero.svg)](https://travis-ci.org/spf13/afero) [![Build status](https://ci.appveyor.com/api/projects/status/github/spf13/afero?branch=master&svg=true)](https://ci.appveyor.com/project/spf13/afero) [![GoDoc](https://godoc.org/github.com/spf13/afero?status.svg)](https://godoc.org/github.com/spf13/afero) [![Join the chat at https://gitter.im/spf13/afero](https://badges.gitter.im/Dev%20Chat.svg)](https://gitter.im/spf13/afero?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

# Overview

Afero is an filesystem framework providing a simple, uniform and universal API
interacting with any filesystem, as an abstraction layer providing interfaces,
types and methods. Afero has an exceptionally clean interface and simple design
without needless constructors or initialization methods.

Afero is also a library providing a base set of interoperable backend
filesystems that make it easy to work with afero while retaining all the power
and benefit of the os and ioutil packages.

Afero provides significant improvements over using the os package alone, most
notably the ability to create mock and testing filesystems without relying on the disk.

It is suitable for use in a any situation where you would consider using the OS
package as it provides an additional abstraction that makes it easy to use a
memory backed file system during testing. It also adds support for the http
filesystem for full interoperability.


## Afero Features

* A single consistent API for accessing a variety of filesystems
* Interoperation between a variety of file system types
* A set of interfaces to encourage and enforce interoperability between backends
* An atomic cross platform memory backed file system
* Support for compositional (union) file systems by combining multiple file systems acting as one
* Specialized backends which modify existing filesystems (Read Only, Regexp filtered)
* A set of utility functions ported from io, ioutil & hugo to be afero aware


# Using Afero

Afero is easy to use and easier to adopt.

A few different ways you could use Afero:

* Use the interfaces alone to define you own file system.
* Wrap for the OS packages.
* Define different filesystems for different parts of your application.
* Use Afero for mock filesystems while testing

## Step 1: Install Afero

First use go get to install the latest version of the library.

    $ go get github.com/spf13/afero

Next include Afero in your application.
```go
import "github.com/spf13/afero"
```

## Step 2: Declare a backend

First define a package variable and set it to a pointer to a filesystem.
```go
var AppFs afero.Fs = afero.NewMemMapFs()

or

var AppFs afero.Fs = afero.NewOsFs()
```
It is important to note that if you repeat the composite literal you
will be using a completely new and isolated filesystem. In the case of
OsFs it will still use the same underlying filesystem but will reduce
the ability to drop in other filesystems as desired.

## Step 3: Use it like you would the OS package

Throughout your application use any function and method like you normally
would.

So if my application before had:
```go
os.Open('/tmp/foo')
```
We would replace it with a call to `AppFs.Open('/tmp/foo')`.

`AppFs` being the variable we defined above.


## List of all available functions

File System Methods Available:
```go
Chmod(name string, mode os.FileMode) : error
Chtimes(name string, atime time.Time, mtime time.Time) : error
Create(name string) : File, error
Mkdir(name string, perm os.FileMode) : error
MkdirAll(path string, perm os.FileMode) : error
Name() : string
Open(name string) : File, error
OpenFile(name string, flag int, perm os.FileMode) : File, error
Remove(name string) : error
RemoveAll(path string) : error
Rename(oldname, newname string) : error
Stat(name string) : os.FileInfo, error
```
File Interfaces and Methods Available:
```go
io.Closer
io.Reader
io.ReaderAt
io.Seeker
io.Writer
io.WriterAt

Name() : string
Readdir(count int) : []os.FileInfo, error
Readdirnames(n int) : []string, error
Stat() : os.FileInfo, error
Sync() : error
Truncate(size int64) : error
WriteString(s string) : ret int, err error
```
In some applications it may make sense to define a new package that
simply exports the file system variable for easy access from anywhere.

## Using Afero's utility functions

Afero provides a set of functions to make it easier to use the underlying file systems.
These functions have been primarily ported from io & ioutil with some developed for Hugo.

The afero utilities support all afero compatible backends.

The list of utilities includes:

```go
DirExists(path string) (bool, error)
Exists(path string) (bool, error)
FileContainsBytes(filename string, subslice []byte) (bool, error)
GetTempDir(subPath string) string
IsDir(path string) (bool, error)
IsEmpty(path string) (bool, error)
ReadDir(dirname string) ([]os.FileInfo, error)
ReadFile(filename string) ([]byte, error)
SafeWriteReader(path string, r io.Reader) (err error)
TempDir(dir, prefix string) (name string, err error)
TempFile(dir, prefix string) (f File, err error)
Walk(root string, walkFn filepath.WalkFunc) error
WriteFile(filename string, data []byte, perm os.FileMode) error
WriteReader(path string, r io.Reader) (err error)
```
For a complete list see [Afero's GoDoc](https://godoc.org/github.com/spf13/afero)

They are available under two different approaches to use. You can either call
them directly where the first parameter of each function will be the file
system, or you can declare a new `Afero`, a custom type used to bind these
functions as methods to a given filesystem.

### Calling utilities directly

```go
fs := new(afero.MemMapFs)
f, err := afero.TempFile(fs,"", "ioutil-test")

```

### Calling via Afero

```go
fs := afero.NewMemMapFs
afs := &Afero{Fs: fs}
f, err := afs.TempFile("", "ioutil-test")
```

## Using Afero for Testing

There is a large benefit to using a mock filesystem for testing. It has a
completely blank state every time it is initialized and can be easily
reproducible regardless of OS. You could create files to your heart’s content
and the file access would be fast while also saving you from all the annoying
issues with deleting temporary files, Windows file locking, etc. The MemMapFs
backend is perfect for testing.

* Much faster than performing I/O operations on disk
* Avoid security issues and permissions
* Far more control. 'rm -rf /' with confidence
* Test setup is far more easier to do
* No test cleanup needed

One way to accomplish this is to define a variable as mentioned above.
In your application this will be set to afero.NewOsFs() during testing you
can set it to afero.NewMemMapFs().

It wouldn't be uncommon to have each test initialize a blank slate memory
backend. To do this I would define my `appFS = afero.NewOsFs()` somewhere
appropriate in my application code. This approach ensures that Tests are order
independent, with no test relying on the state left by an earlier test.

Then in my tests I would initialize a new MemMapFs for each test:
```go
func TestExist(t *testing.T) {
	appFS := afero.NewMemMapFs()
	// create test files and directories
	appFS.MkdirAll("src/a", 0755)
	afero.WriteFile(appFS, "src/a/b", []byte("file b"), 0644)
	afero.WriteFile(appFS, "src/c", []byte("file c"), 0644)
	name := "src/c"
	_, err := appFS.Stat(name)
	if os.IsNotExist(err) {
		t.Errorf("file \"%s\" does not exist.\n", name)
	}
}
```

# Available Backends

## Operating System Native

### OsFs

The first is simply a wrapper around the native OS calls. This makes it
very easy to use as all of the calls are the same as the existing OS
calls. It also makes it trivial to have your code use the OS during
operation and a mock filesystem during testing or as needed.

```go
appfs := afero.NewOsFs()
appfs.MkdirAll("src/a", 0755))
```

## Memory Backed Storage

### MemMapFs

Afero also provides a fully atomic memory backed filesystem perfect for use in
mocking and to speed up unnecessary disk io when persistence isn’t
necessary. It is fully concurrent and will work within go routines
safely.

```go
mm := afero.NewMemMapFs()
mm.MkdirAll("src/a", 0755))
```

#### InMemoryFile

As part of MemMapFs, Afero also provides an atomic, fully concurrent memory
backed file implementation. This can be used in other memory backed file
systems with ease. Plans are to add a radix tree memory stored file
system using InMemoryFile.

## Network Interfaces

### SftpFs

Afero has experimental support for secure file transfer protocol (sftp). Which can
be used to perform file operations over a encrypted channel.

## Filtering Backends

### BasePathFs

The BasePathFs restricts all operations to a given path within an Fs.
The given file name to the operations on this Fs will be prepended with
the base path before calling the source Fs.

```go
bp := afero.NewBasePathFs(afero.NewOsFs(), "/base/path")
```

### ReadOnlyFs

A thin wrapper around the source Fs providing a read only view.

```go
fs := afero.NewReadOnlyFs(afero.NewOsFs())
_, err := fs.Create("/file.txt")
// err = syscall.EPERM
```

# RegexpFs

A filtered view on file names, any file NOT matching
the passed regexp will be treated as non-existing.
Files not matching the regexp provided will not be created.
Directories are not filtered.

```go
fs := afero.NewRegexpFs(afero.NewMemMapFs(), regexp.MustCompile(`\.txt$`))
_, err := fs.Create("/file.html")
// err = syscall.ENOENT
```

### HttpFs

Afero provides an http compatible backend which can wrap any of the existing
backends.

The Http package requires a slightly specific version of Open which
returns an http.File type.

Afero provides an httpFs file system which satisfies this requirement.
Any Afero FileSystem can be used as an httpFs.

```go
httpFs := afero.NewHttpFs(<ExistingFS>)
fileserver := http.FileServer(httpFs.Dir(<PATH>)))
http.Handle("/", fileserver)
```

## Composite Backends

Afero provides the ability have two filesystems (or more) act as a single
file system.

### CacheOnReadFs

The CacheOnReadFs will lazily make copies of any accessed files from the base
layer into the overlay. Subsequent reads will be pulled from the overlay
directly permitting the request is within the cache duration of when it was
created in the overlay.

If the base filesystem is writeable, any changes to files will be
done first to the base, then to the overlay layer. Write calls to open file
handles like `Write()` or `Truncate()` to the overlay first.

To writing files to the overlay only, you can use the overlay Fs directly (not
via the union Fs).

Cache files in the layer for the given time.Duration, a cache duration of 0
means "forever" meaning the file will not be re-requested from the base ever.

A read-only base will make the overlay also read-only but still copy files
from the base to the overlay when they're not present (or outdated) in the
caching layer.

```go
base := afero.NewOsFs()
layer := afero.NewMemMapFs()
ufs := afero.NewCacheOnReadFs(base, layer, 100 * time.Second)
```

### CopyOnWriteFs()

The CopyOnWriteFs is a read only base file system with a potentially
writeable layer on top.

Read operations will first look in the overlay and if not found there, will
serve the file from the base.

Changes to the file system will only be made in the overlay.

Any attempt to modify a file found only in the base will copy the file to the
overlay layer before modification (including opening a file with a writable
handle).

Removing and Renaming files present only in the base layer is not currently
permitted. If a file is present in the base layer and the overlay, only the
overlay will be removed/renamed.

```go
	base := afero.NewOsFs()
	roBase := afero.NewReadOnlyFs(base)
	ufs := afero.NewCopyOnWriteFs(roBase, afero.NewMemMapFs())

	fh, _ = ufs.Create("/home/test/file2.txt")
	fh.WriteString("This is a test")
	fh.Close()
```

In this example all write operations will only occur in memory (MemMapFs)
leaving the base filesystem (OsFs) untouched.


## Desired/possible backends

The following is a short list of possible backends we hope someone will
implement:

* SSH
* ZIP
* TAR
* S3

# About the project

## What's in the name

Afero comes from the latin roots Ad-Facere.

**"Ad"** is a prefix meaning "to".

**"Facere"** is a form of the root "faciō" making "make or do".

The literal meaning of afero is "to make" or "to do" which seems very fitting
for a library that allows one to make files and directories and do things with them.

The English word that shares the same roots as Afero is "affair". Affair shares
the same concept but as a noun it means "something that is made or done" or "an
object of a particular type".

It's also nice that unlike some of my other libraries (hugo, cobra, viper) it
Googles very well.

## Release Notes

* **0.10.0** 2015.12.10
  * Full compatibility with Windows
  * Introduction of afero utilities
  * Test suite rewritten to work cross platform
  * Normalize paths for MemMapFs
  * Adding Sync to the file interface
  * **Breaking Change** Walk and ReadDir have changed parameter order
  * Moving types used by MemMapFs to a subpackage
  * General bugfixes and improvements
* **0.9.0** 2015.11.05
  * New Walk function similar to filepath.Walk
  * MemMapFs.OpenFile handles O_CREATE, O_APPEND, O_TRUNC
  * MemMapFs.Remove now really deletes the file
  * InMemoryFile.Readdir and Readdirnames work correctly
  * InMemoryFile functions lock it for concurrent access
  * Test suite improvements
* **0.8.0** 2014.10.28
  * First public version
  * Interfaces feel ready for people to build using
  * Interfaces satisfy all known uses
  * MemMapFs passes the majority of the OS test suite
  * OsFs passes the majority of the OS test suite

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Contributors

Names in no particular order:

* [spf13](https://github.com/spf13)
* [jaqx0r](https://github.com/jaqx0r)
* [mbertschler](https://github.com/mbertschler)
* [xor-gate](https://github.com/xor-gate)

## License

Afero is released under the Apache 2.0 license. See
[LICENSE.txt](https://github.com/spf13/afero/blob/master/LICENSE.txt)
![viper logo](https://cloud.githubusercontent.com/assets/173412/10886745/998df88a-8151-11e5-9448-4736db51020d.png)

Go configuration with fangs!

Many Go projects are built using Viper including:

* [Hugo](http://gohugo.io)
* [EMC RexRay](http://rexray.readthedocs.org/en/stable/)
* [Imgur's Incus](https://github.com/Imgur/incus)
* [Nanobox](https://github.com/nanobox-io/nanobox)/[Nanopack](https://github.com/nanopack)
* [Docker Notary](https://github.com/docker/Notary)
* [BloomApi](https://www.bloomapi.com/)
* [doctl](https://github.com/digitalocean/doctl)

[![Build Status](https://travis-ci.org/spf13/viper.svg)](https://travis-ci.org/spf13/viper) [![Join the chat at https://gitter.im/spf13/viper](https://badges.gitter.im/Join%20Chat.svg)](https://gitter.im/spf13/viper?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge) [![GoDoc](https://godoc.org/github.com/spf13/viper?status.svg)](https://godoc.org/github.com/spf13/viper)


## What is Viper?

Viper is a complete configuration solution for go applications including 12 factor apps. It is designed
to work within an application, and can handle all types of configuration needs
and formats. It supports:

* setting defaults
* reading from JSON, TOML, YAML, HCL, and Java properties config files
* live watching and re-reading of config files (optional)
* reading from environment variables
* reading from remote config systems (etcd or Consul), and watching changes
* reading from command line flags
* reading from buffer
* setting explicit values

Viper can be thought of as a registry for all of your applications
configuration needs.

## Why Viper?

When building a modern application, you don’t want to worry about
configuration file formats; you want to focus on building awesome software.
Viper is here to help with that.

Viper does the following for you:

1. Find, load, and unmarshal a configuration file in JSON, TOML, YAML, HCL, or Java properties formats.
2. Provide a mechanism to set default values for your different
   configuration options.
3. Provide a mechanism to set override values for options specified through
   command line flags.
4. Provide an alias system to easily rename parameters without breaking existing
   code.
5. Make it easy to tell the difference between when a user has provided a
   command line or config file which is the same as the default.

Viper uses the following precedence order. Each item takes precedence over the
item below it:

 * explicit call to Set
 * flag
 * env
 * config
 * key/value store
 * default

Viper configuration keys are case insensitive.

## Putting Values into Viper

### Establishing Defaults

A good configuration system will support default values. A default value is not
required for a key, but it's useful in the event that a key hasn’t been set via
config file, environment variable, remote configuration or flag.

Examples:

```go
viper.SetDefault("ContentDir", "content")
viper.SetDefault("LayoutDir", "layouts")
viper.SetDefault("Taxonomies", map[string]string{"tag": "tags", "category": "categories"})
```

### Reading Config Files

Viper requires minimal configuration so it knows where to look for config files.
Viper supports JSON, TOML, YAML, HCL, and Java Properties files. Viper can search multiple paths, but
currently a single Viper instance only supports a single configuration file.
Viper does not default to any configuration search paths leaving defaults decision
to an application.

Here is an example of how to use Viper to search for and read a configuration file.
None of the specific paths are required, but at least one path should be provided
where a configuration file is expected.

```go
viper.SetConfigName("config") // name of config file (without extension)
viper.AddConfigPath("/etc/appname/")   // path to look for the config file in
viper.AddConfigPath("$HOME/.appname")  // call multiple times to add many search paths
viper.AddConfigPath(".")               // optionally look for config in the working directory
err := viper.ReadInConfig() // Find and read the config file
if err != nil { // Handle errors reading the config file
	panic(fmt.Errorf("Fatal error config file: %s \n", err))
}
```

### Watching and re-reading config files

Viper supports the ability to have your application live read a config file while running.

Gone are the days of needing to restart a server to have a config take effect,
viper powered applications can read an update to a config file while running and
not miss a beat.

Simply tell the viper instance to watchConfig.
Optionally you can provide a function for Viper to run each time a change occurs.

**Make sure you add all of the configPaths prior to calling `WatchConfig()`**

```go
		viper.WatchConfig()
		viper.OnConfigChange(func(e fsnotify.Event) {
			fmt.Println("Config file changed:", e.Name)
		})
```

### Reading Config from io.Reader

Viper predefines many configuration sources such as files, environment
variables, flags, and remote K/V store, but you are not bound to them. You can
also implement your own required configuration source and feed it to viper.

```go
viper.SetConfigType("yaml") // or viper.SetConfigType("YAML")

// any approach to require this configuration into your program.
var yamlExample = []byte(`
Hacker: true
name: steve
hobbies:
- skateboarding
- snowboarding
- go
clothing:
  jacket: leather
  trousers: denim
age: 35
eyes : brown
beard: true
`)

viper.ReadConfig(bytes.NewBuffer(yamlExample))

viper.Get("name") // this would be "steve"
```

### Setting Overrides

These could be from a command line flag, or from your own application logic.

```go
viper.Set("Verbose", true)
viper.Set("LogFile", LogFile)
```

### Registering and Using Aliases

Aliases permit a single value to be referenced by multiple keys

```go
viper.RegisterAlias("loud", "Verbose")

viper.Set("verbose", true) // same result as next line
viper.Set("loud", true)   // same result as prior line

viper.GetBool("loud") // true
viper.GetBool("verbose") // true
```

### Working with Environment Variables

Viper has full support for environment variables. This enables 12 factor
applications out of the box. There are four methods that exist to aid working
with ENV:

 * `AutomaticEnv()`
 * `BindEnv(string...) : error`
 * `SetEnvPrefix(string)`
 * `SetEnvReplacer(string...) *strings.Replacer`

_When working with ENV variables, it’s important to recognize that Viper
treats ENV variables as case sensitive._

Viper provides a mechanism to try to ensure that ENV variables are unique. By
using `SetEnvPrefix`, you can tell Viper to use add a prefix while reading from
the environment variables. Both `BindEnv` and `AutomaticEnv` will use this
prefix.

`BindEnv` takes one or two parameters. The first parameter is the key name, the
second is the name of the environment variable. The name of the environment
variable is case sensitive. If the ENV variable name is not provided, then
Viper will automatically assume that the key name matches the ENV variable name,
but the ENV variable is IN ALL CAPS. When you explicitly provide the ENV
variable name, it **does not** automatically add the prefix.

One important thing to recognize when working with ENV variables is that the
value will be read each time it is accessed. Viper does not fix the value when
the `BindEnv` is called.

`AutomaticEnv` is a powerful helper especially when combined with
`SetEnvPrefix`. When called, Viper will check for an environment variable any
time a `viper.Get` request is made. It will apply the following rules. It will
check for a environment variable with a name matching the key uppercased and
prefixed with the `EnvPrefix` if set.

`SetEnvReplacer` allows you to use a `strings.Replacer` object to rewrite Env
keys to an extent. This is useful if you want to use `-` or something in your
`Get()` calls, but want your environmental variables to use `_` delimiters. An
example of using it can be found in `viper_test.go`.

#### Env example

```go
SetEnvPrefix("spf") // will be uppercased automatically
BindEnv("id")

os.Setenv("SPF_ID", "13") // typically done outside of the app

id := Get("id") // 13
```

### Working with Flags

Viper has the ability to bind to flags. Specifically, Viper supports `Pflags`
as used in the [Cobra](https://github.com/spf13/cobra) library.

Like `BindEnv`, the value is not set when the binding method is called, but when
it is accessed. This means you can bind as early as you want, even in an
`init()` function.

The `BindPFlag()` method provides this functionality.

Example:

```go
serverCmd.Flags().Int("port", 1138, "Port to run Application server on")
viper.BindPFlag("port", serverCmd.Flags().Lookup("port"))
```

The use of [pflag](https://github.com/spf13/pflag/) in Viper does not preclude
the use of other packages that use the [flag](https://golang.org/pkg/flag/)
package from the standard library. The pflag package can handle the flags
defined for the flag package by importing these flags. This is accomplished
by a calling a convenience function provided by the pflag package called
AddGoFlagSet().

Example:

```go
package main

import (
	"flag"
	"github.com/spf13/pflag"
)

func main() {
	pflag.CommandLine.AddGoFlagSet(flag.CommandLine)
	pflag.Parse()
    ...
}
```

#### Flag interfaces

Viper provides two Go interfaces to bind other flag systems if you don't use `Pflags`.

`FlagValue` represents a single flag. This is a very simple example on how to implement this interface:

```go
type myFlag struct {}
func (f myFlag) HasChanged() bool { return false }
func (f myFlag) Name() string { return "my-flag-name" }
func (f myFlag) ValueString() string { return "my-flag-value" }
func (f myFlag) ValueType() string { return "string" }
```

Once your flag implements this interface, you can simply tell Viper to bind it:

```go
viper.BindFlagValue("my-flag-name", myFlag{})
```

`FlagValueSet` represents a group of flags. This is a very simple example on how to implement this interface:

```go
type myFlagSet struct {
	flags []myFlag
}

func (f myFlagSet) VisitAll(fn func(FlagValue)) {
	for _, flag := range flags {
		fn(flag)
	}
}
```

Once your flag set implements this interface, you can simply tell Viper to bind it:

```go
fSet := myFlagSet{
	flags: []myFlag{myFlag{}, myFlag{}},
}
viper.BindFlagValues("my-flags", fSet)
```

### Remote Key/Value Store Support

To enable remote support in Viper, do a blank import of the `viper/remote`
package:

`import _ "github.com/spf13/viper/remote"`

Viper will read a config string (as JSON, TOML, YAML or HCL) retrieved from a path
in a Key/Value store such as etcd or Consul.  These values take precedence over
default values, but are overridden by configuration values retrieved from disk,
flags, or environment variables.

Viper uses [crypt](https://github.com/xordataexchange/crypt) to retrieve
configuration from the K/V store, which means that you can store your
configuration values encrypted and have them automatically decrypted if you have
the correct gpg keyring.  Encryption is optional.

You can use remote configuration in conjunction with local configuration, or
independently of it.

`crypt` has a command-line helper that you can use to put configurations in your
K/V store. `crypt` defaults to etcd on http://127.0.0.1:4001.

```bash
$ go get github.com/xordataexchange/crypt/bin/crypt
$ crypt set -plaintext /config/hugo.json /Users/hugo/settings/config.json
```

Confirm that your value was set:

```bash
$ crypt get -plaintext /config/hugo.json
```

See the `crypt` documentation for examples of how to set encrypted values, or
how to use Consul.

### Remote Key/Value Store Example - Unencrypted

```go
viper.AddRemoteProvider("etcd", "http://127.0.0.1:4001","/config/hugo.json")
viper.SetConfigType("json") // because there is no file extension in a stream of bytes, supported extensions are "json", "toml", "yaml", "yml", "properties", "props", "prop"
err := viper.ReadRemoteConfig()
```

### Remote Key/Value Store Example - Encrypted

```go
viper.AddSecureRemoteProvider("etcd","http://127.0.0.1:4001","/config/hugo.json","/etc/secrets/mykeyring.gpg")
viper.SetConfigType("json") // because there is no file extension in a stream of bytes,  supported extensions are "json", "toml", "yaml", "yml", "properties", "props", "prop"
err := viper.ReadRemoteConfig()
```

### Watching Changes in etcd - Unencrypted

```go
// alternatively, you can create a new viper instance.
var runtime_viper = viper.New()

runtime_viper.AddRemoteProvider("etcd", "http://127.0.0.1:4001", "/config/hugo.yml")
runtime_viper.SetConfigType("yaml") // because there is no file extension in a stream of bytes, supported extensions are "json", "toml", "yaml", "yml", "properties", "props", "prop"

// read from remote config the first time.
err := runtime_viper.ReadRemoteConfig()

// unmarshal config
runtime_viper.Unmarshal(&runtime_conf)

// open a goroutine to watch remote changes forever
go func(){
	for {
	    time.Sleep(time.Second * 5) // delay after each request

	    // currently, only tested with etcd support
	    err := runtime_viper.WatchRemoteConfig()
	    if err != nil {
	        log.Errorf("unable to read remote config: %v", err)
	        continue
	    }

	    // unmarshal new config into our runtime config struct. you can also use channel
	    // to implement a signal to notify the system of the changes
	    runtime_viper.Unmarshal(&runtime_conf)
	}
}()
```

## Getting Values From Viper

In Viper, there are a few ways to get a value depending on the value's type.
The following functions and methods exist:

 * `Get(key string) : interface{}`
 * `GetBool(key string) : bool`
 * `GetFloat64(key string) : float64`
 * `GetInt(key string) : int`
 * `GetString(key string) : string`
 * `GetStringMap(key string) : map[string]interface{}`
 * `GetStringMapString(key string) : map[string]string`
 * `GetStringSlice(key string) : []string`
 * `GetTime(key string) : time.Time`
 * `GetDuration(key string) : time.Duration`
 * `IsSet(key string) : bool`

One important thing to recognize is that each Get function will return a zero
value if it’s not found. To check if a given key exists, the `IsSet()` method
has been provided.

Example:
```go
viper.GetString("logfile") // case-insensitive Setting & Getting
if viper.GetBool("verbose") {
    fmt.Println("verbose enabled")
}
```
### Accessing nested keys

The accessor methods also accept formatted paths to deeply nested keys. For
example, if the following JSON file is loaded:

```json
{
    "host": {
        "address": "localhost",
        "port": 5799
    },
    "datastore": {
        "metric": {
            "host": "127.0.0.1",
            "port": 3099
        },
        "warehouse": {
            "host": "198.0.0.1",
            "port": 2112
        }
    }
}

```

Viper can access a nested field by passing a `.` delimited path of keys:

```go
GetString("datastore.metric.host") // (returns "127.0.0.1")
```

This obeys the precedence rules established above; the search for the path
will cascade through the remaining configuration registries until found.

For example, given this configuration file, both `datastore.metric.host` and
`datastore.metric.port` are already defined (and may be overridden). If in addition
`datastore.metric.protocol` was defined in the defaults, Viper would also find it.

However, if `datastore.metric` was overridden (by a flag, an environment variable,
the `Set()` method, …) with an immediate value, then all sub-keys of
`datastore.metric` become undefined, they are “shadowed” by the higher-priority
configuration level.

Lastly, if there exists a key that matches the delimited key path, its value
will be returned instead. E.g.

```json
{
    "datastore.metric.host": "0.0.0.0",
    "host": {
        "address": "localhost",
        "port": 5799
    },
    "datastore": {
        "metric": {
            "host": "127.0.0.1",
            "port": 3099
        },
        "warehouse": {
            "host": "198.0.0.1",
            "port": 2112
        }
    }
}

GetString("datastore.metric.host") // returns "0.0.0.0"
```

### Extract sub-tree

Extract sub-tree from Viper.

For example, `viper` represents:

```json
app:
  cache1:
    max-items: 100
    item-size: 64
  cache2:
    max-items: 200
    item-size: 80
```

After executing:

```go
subv := viper.Sub("app.cache1")
```

`subv` represents:

```json
max-items: 100
item-size: 64
```

Suppose we have:

```go
func NewCache(cfg *Viper) *Cache {...}
```

which creates a cache based on config information formatted as `subv`.
Now it's easy to create these 2 caches separately as:

```go
cfg1 := viper.Sub("app.cache1")
cache1 := NewCache(cfg1)

cfg2 := viper.Sub("app.cache2")
cache2 := NewCache(cfg2)
```

### Unmarshaling

You also have the option of Unmarshaling all or a specific value to a struct, map,
etc.

There are two methods to do this:

 * `Unmarshal(rawVal interface{}) : error`
 * `UnmarshalKey(key string, rawVal interface{}) : error`

Example:

```go
type config struct {
	Port int
	Name string
	PathMap string `mapstructure:"path_map"`
}

var C config

err := Unmarshal(&C)
if err != nil {
	t.Fatalf("unable to decode into struct, %v", err)
}
```

## Viper or Vipers?

Viper comes ready to use out of the box. There is no configuration or
initialization needed to begin using Viper. Since most applications will want
to use a single central repository for their configuration, the viper package
provides this. It is similar to a singleton.

In all of the examples above, they demonstrate using viper in it's singleton
style approach.

### Working with multiple vipers

You can also create many different vipers for use in your application. Each will
have it’s own unique set of configurations and values. Each can read from a
different config file, key value store, etc. All of the functions that viper
package supports are mirrored as methods on a viper.

Example:

```go
x := viper.New()
y := viper.New()

x.SetDefault("ContentDir", "content")
y.SetDefault("ContentDir", "foobar")

//...
```

When working with multiple vipers, it is up to the user to keep track of the
different vipers.

## Q & A

Q: Why not INI files?

A: Ini files are pretty awful. There’s no standard format, and they are hard to
validate. Viper is designed to work with JSON, TOML or YAML files. If someone
really wants to add this feature, I’d be happy to merge it. It’s easy to specify
which formats your application will permit.

Q: Why is it called “Viper”?

A: Viper is designed to be a [companion](http://en.wikipedia.org/wiki/Viper_(G.I._Joe))
to [Cobra](https://github.com/spf13/cobra). While both can operate completely
independently, together they make a powerful pair to handle much of your
application foundation needs.

Q: Why is it called “Cobra”?

A: Is there a better name for a [commander](http://en.wikipedia.org/wiki/Cobra_Commander)?
[![Build Status](https://travis-ci.org/spf13/pflag.svg?branch=master)](https://travis-ci.org/spf13/pflag)
[![Go Report Card](https://goreportcard.com/badge/github.com/spf13/pflag)](https://goreportcard.com/report/github.com/spf13/pflag)
[![GoDoc](https://godoc.org/github.com/spf13/pflag?status.svg)](https://godoc.org/github.com/spf13/pflag)

## Description

pflag is a drop-in replacement for Go's flag package, implementing
POSIX/GNU-style --flags.

pflag is compatible with the [GNU extensions to the POSIX recommendations
for command-line options][1]. For a more precise description, see the
"Command-line flag syntax" section below.

[1]: http://www.gnu.org/software/libc/manual/html_node/Argument-Syntax.html

pflag is available under the same style of BSD license as the Go language,
which can be found in the LICENSE file.

## Installation

pflag is available using the standard `go get` command.

Install by running:

    go get github.com/spf13/pflag

Run tests by running:

    go test github.com/spf13/pflag

## Usage

pflag is a drop-in replacement of Go's native flag package. If you import
pflag under the name "flag" then all code should continue to function
with no changes.

``` go
import flag "github.com/spf13/pflag"
```

There is one exception to this: if you directly instantiate the Flag struct
there is one more field "Shorthand" that you will need to set.
Most code never instantiates this struct directly, and instead uses
functions such as String(), BoolVar(), and Var(), and is therefore
unaffected.

Define flags using flag.String(), Bool(), Int(), etc.

This declares an integer flag, -flagname, stored in the pointer ip, with type *int.

``` go
var ip *int = flag.Int("flagname", 1234, "help message for flagname")
```

If you like, you can bind the flag to a variable using the Var() functions.

``` go
var flagvar int
func init() {
    flag.IntVar(&flagvar, "flagname", 1234, "help message for flagname")
}
```

Or you can create custom flags that satisfy the Value interface (with
pointer receivers) and couple them to flag parsing by

``` go
flag.Var(&flagVal, "name", "help message for flagname")
```

For such flags, the default value is just the initial value of the variable.

After all flags are defined, call

``` go
flag.Parse()
```

to parse the command line into the defined flags.

Flags may then be used directly. If you're using the flags themselves,
they are all pointers; if you bind to variables, they're values.

``` go
fmt.Println("ip has value ", *ip)
fmt.Println("flagvar has value ", flagvar)
```

There are helpers function to get values later if you have the FlagSet but
it was difficult to keep up with all of the flag pointers in your code.
If you have a pflag.FlagSet with a flag called 'flagname' of type int you
can use GetInt() to get the int value. But notice that 'flagname' must exist
and it must be an int. GetString("flagname") will fail.

``` go
i, err := flagset.GetInt("flagname")
```

After parsing, the arguments after the flag are available as the
slice flag.Args() or individually as flag.Arg(i).
The arguments are indexed from 0 through flag.NArg()-1.

The pflag package also defines some new functions that are not in flag,
that give one-letter shorthands for flags. You can use these by appending
'P' to the name of any function that defines a flag.

``` go
var ip = flag.IntP("flagname", "f", 1234, "help message")
var flagvar bool
func init() {
	flag.BoolVarP(&flagvar, "boolname", "b", true, "help message")
}
flag.VarP(&flagVal, "varname", "v", "help message")
```

Shorthand letters can be used with single dashes on the command line.
Boolean shorthand flags can be combined with other shorthand flags.

The default set of command-line flags is controlled by
top-level functions.  The FlagSet type allows one to define
independent sets of flags, such as to implement subcommands
in a command-line interface. The methods of FlagSet are
analogous to the top-level functions for the command-line
flag set.

## Setting no option default values for flags

After you create a flag it is possible to set the pflag.NoOptDefVal for
the given flag. Doing this changes the meaning of the flag slightly. If
a flag has a NoOptDefVal and the flag is set on the command line without
an option the flag will be set to the NoOptDefVal. For example given:

``` go
var ip = flag.IntP("flagname", "f", 1234, "help message")
flag.Lookup("flagname").NoOptDefVal = "4321"
```

Would result in something like

| Parsed Arguments | Resulting Value |
| -------------    | -------------   |
| --flagname=1357  | ip=1357         |
| --flagname       | ip=4321         |
| [nothing]        | ip=1234         |

## Command line flag syntax

```
--flag    // boolean flags, or flags with no option default values
--flag x  // only on flags without a default value
--flag=x
```

Unlike the flag package, a single dash before an option means something
different than a double dash. Single dashes signify a series of shorthand
letters for flags. All but the last shorthand letter must be boolean flags
or a flag with a default value

```
// boolean or flags where the 'no option default value' is set
-f
-f=true
-abc
but
-b true is INVALID

// non-boolean and flags without a 'no option default value'
-n 1234
-n=1234
-n1234

// mixed
-abcs "hello"
-absd="hello"
-abcs1234
```

Flag parsing stops after the terminator "--". Unlike the flag package,
flags can be interspersed with arguments anywhere on the command line
before this terminator.

Integer flags accept 1234, 0664, 0x1234 and may be negative.
Boolean flags (in their long form) accept 1, 0, t, f, true, false,
TRUE, FALSE, True, False.
Duration flags accept any input valid for time.ParseDuration.

## Mutating or "Normalizing" Flag names

It is possible to set a custom flag name 'normalization function.' It allows flag names to be mutated both when created in the code and when used on the command line to some 'normalized' form. The 'normalized' form is used for comparison. Two examples of using the custom normalization func follow.

**Example #1**: You want -, _, and . in flags to compare the same. aka --my-flag == --my_flag == --my.flag

``` go
func wordSepNormalizeFunc(f *pflag.FlagSet, name string) pflag.NormalizedName {
	from := []string{"-", "_"}
	to := "."
	for _, sep := range from {
		name = strings.Replace(name, sep, to, -1)
	}
	return pflag.NormalizedName(name)
}

myFlagSet.SetNormalizeFunc(wordSepNormalizeFunc)
```

**Example #2**: You want to alias two flags. aka --old-flag-name == --new-flag-name

``` go
func aliasNormalizeFunc(f *pflag.FlagSet, name string) pflag.NormalizedName {
	switch name {
	case "old-flag-name":
		name = "new-flag-name"
		break
	}
	return pflag.NormalizedName(name)
}

myFlagSet.SetNormalizeFunc(aliasNormalizeFunc)
```

## Deprecating a flag or its shorthand
It is possible to deprecate a flag, or just its shorthand. Deprecating a flag/shorthand hides it from help text and prints a usage message when the deprecated flag/shorthand is used.

**Example #1**: You want to deprecate a flag named "badflag" as well as inform the users what flag they should use instead.
```go
// deprecate a flag by specifying its name and a usage message
flags.MarkDeprecated("badflag", "please use --good-flag instead")
```
This hides "badflag" from help text, and prints `Flag --badflag has been deprecated, please use --good-flag instead` when "badflag" is used.

**Example #2**: You want to keep a flag name "noshorthandflag" but deprecate its shortname "n".
```go
// deprecate a flag shorthand by specifying its flag name and a usage message
flags.MarkShorthandDeprecated("noshorthandflag", "please use --noshorthandflag only")
```
This hides the shortname "n" from help text, and prints `Flag shorthand -n has been deprecated, please use --noshorthandflag only` when the shorthand "n" is used.

Note that usage message is essential here, and it should not be empty.

## Hidden flags
It is possible to mark a flag as hidden, meaning it will still function as normal, however will not show up in usage/help text.

**Example**: You have a flag named "secretFlag" that you need for internal use only and don't want it showing up in help text, or for its usage text to be available.
```go
// hide a flag by specifying its name
flags.MarkHidden("secretFlag")
```

## Supporting Go flags when using pflag
In order to support flags defined using Go's `flag` package, they must be added to the `pflag` flagset. This is usually necessary
to support flags defined by third-party dependencies (e.g. `golang/glog`).

**Example**: You want to add the Go flags to the `CommandLine` flagset
```go
import (
	goflag "flag"
	flag "github.com/spf13/pflag"
)

var ip *int = flag.Int("flagname", 1234, "help message for flagname")

func main() {
	flag.CommandLine.AddGoFlagSet(goflag.CommandLine)
	flag.Parse()
}
```

## More info

You can see the full reference documentation of the pflag package
[at godoc.org][3], or through go's standard documentation system by
running `godoc -http=:6060` and browsing to
[http://localhost:6060/pkg/github.com/ogier/pflag][2] after
installation.

[2]: http://localhost:6060/pkg/github.com/ogier/pflag
[3]: http://godoc.org/github.com/ogier/pflag
cast
====
[![GoDoc](https://godoc.org/github.com/spf13/cast?status.svg)](https://godoc.org/github.com/spf13/cast)
[![Build Status](https://api.travis-ci.org/spf13/cast.svg?branch=master)](https://travis-ci.org/spf13/cast)
[![Go Report Card](https://goreportcard.com/badge/github.com/spf13/cast)](https://goreportcard.com/report/github.com/spf13/cast)

Easy and safe casting from one type to another in Go

Don’t Panic! ... Cast

## What is Cast?

Cast is a library to convert between different go types in a consistent and easy way.

Cast provides simple functions to easily convert a number to a string, an
interface into a bool, etc. Cast does this intelligently when an obvious
conversion is possible. It doesn’t make any attempts to guess what you meant,
for example you can only convert a string to an int when it is a string
representation of an int such as “8”. Cast was developed for use in
[Hugo](http://hugo.spf13.com), a website engine which uses YAML, TOML or JSON
for meta data.

## Why use Cast?

When working with dynamic data in Go you often need to cast or convert the data
from one type into another. Cast goes beyond just using type assertion (though
it uses that when possible) to provide a very straightforward and convenient
library.

If you are working with interfaces to handle things like dynamic content
you’ll need an easy way to convert an interface into a given type. This
is the library for you.

If you are taking in data from YAML, TOML or JSON or other formats which lack
full types, then Cast is the library for you.

## Usage

Cast provides a handful of To_____ methods. These methods will always return
the desired type. **If input is provided that will not convert to that type, the
0 or nil value for that type will be returned**.

Cast also provides identical methods To_____E. These return the same result as
the To_____ methods, plus an additional error which tells you if it successfully
converted. Using these methods you can tell the difference between when the
input matched the zero value or when the conversion failed and the zero value
was returned.

The following examples are merely a sample of what is available. Please review
the code for a complete set.

### Example ‘ToString’:

    cast.ToString("mayonegg")         // "mayonegg"
    cast.ToString(8)                  // "8"
    cast.ToString(8.31)               // "8.31"
    cast.ToString([]byte("one time")) // "one time"
    cast.ToString(nil)                // ""

	var foo interface{} = "one more time"
    cast.ToString(foo)                // "one more time"


### Example ‘ToInt’:

    cast.ToInt(8)                  // 8
    cast.ToInt(8.31)               // 8
    cast.ToInt("8")                // 8
    cast.ToInt(true)               // 1
    cast.ToInt(false)              // 0

	var eight interface{} = 8
    cast.ToInt(eight)              // 8
    cast.ToInt(nil)                // 0

![cobra logo](https://cloud.githubusercontent.com/assets/173412/10886352/ad566232-814f-11e5-9cd0-aa101788c117.png)

Cobra is both a library for creating powerful modern CLI applications as well as a program to generate applications and command files.

Many of the most widely used Go projects are built using Cobra including:

* [Kubernetes](http://kubernetes.io/)
* [Hugo](http://gohugo.io)
* [rkt](https://github.com/coreos/rkt)
* [etcd](https://github.com/coreos/etcd)
* [Docker](https://github.com/docker/docker)
* [Docker (distribution)](https://github.com/docker/distribution)
* [OpenShift](https://www.openshift.com/)
* [Delve](https://github.com/derekparker/delve)
* [GopherJS](http://www.gopherjs.org/)
* [CockroachDB](http://www.cockroachlabs.com/)
* [Bleve](http://www.blevesearch.com/)
* [ProjectAtomic (enterprise)](http://www.projectatomic.io/)
* [Parse (CLI)](https://parse.com/)
* [GiantSwarm's swarm](https://github.com/giantswarm/cli)
* [Nanobox](https://github.com/nanobox-io/nanobox)/[Nanopack](https://github.com/nanopack)


[![Build Status](https://travis-ci.org/spf13/cobra.svg "Travis CI status")](https://travis-ci.org/spf13/cobra)
[![CircleCI status](https://circleci.com/gh/spf13/cobra.png?circle-token=:circle-token "CircleCI status")](https://circleci.com/gh/spf13/cobra)
[![GoDoc](https://godoc.org/github.com/spf13/cobra?status.svg)](https://godoc.org/github.com/spf13/cobra) 

![cobra](https://cloud.githubusercontent.com/assets/173412/10911369/84832a8e-8212-11e5-9f82-cc96660a4794.gif)

# Overview

Cobra is a library providing a simple interface to create powerful modern CLI
interfaces similar to git & go tools.

Cobra is also an application that will generate your application scaffolding to rapidly
develop a Cobra-based application.

Cobra provides:
* Easy subcommand-based CLIs: `app server`, `app fetch`, etc.
* Fully POSIX-compliant flags (including short & long versions)
* Nested subcommands
* Global, local and cascading flags
* Easy generation of applications & commands with `cobra create appname` & `cobra add cmdname`
* Intelligent suggestions (`app srver`... did you mean `app server`?)
* Automatic help generation for commands and flags
* Automatic detailed help for `app help [command]`
* Automatic help flag recognition of `-h`, `--help`, etc.
* Automatically generated bash autocomplete for your application
* Automatically generated man pages for your application
* Command aliases so you can change things without breaking them
* The flexibilty to define your own help, usage, etc.
* Optional tight integration with [viper](http://github.com/spf13/viper) for 12-factor apps

Cobra has an exceptionally clean interface and simple design without needless
constructors or initialization methods.

Applications built with Cobra commands are designed to be as user-friendly as
possible. Flags can be placed before or after the command (as long as a
confusing space isn’t provided). Both short and long flags can be used. A
command need not even be fully typed.  Help is automatically generated and
available for the application or for a specific command using either the help
command or the `--help` flag.

# Concepts

Cobra is built on a structure of commands, arguments & flags.

**Commands** represent actions, **Args** are things and **Flags** are modifiers for those actions.

The best applications will read like sentences when used. Users will know how
to use the application because they will natively understand how to use it.

The pattern to follow is
`APPNAME VERB NOUN --ADJECTIVE.`
    or
`APPNAME COMMAND ARG --FLAG`

A few good real world examples may better illustrate this point.

In the following example, 'server' is a command, and 'port' is a flag:

    > hugo server --port=1313

In this command we are telling Git to clone the url bare.

    > git clone URL --bare

## Commands

Command is the central point of the application. Each interaction that
the application supports will be contained in a Command. A command can
have children commands and optionally run an action.

In the example above, 'server' is the command.

A Command has the following structure:

```go
type Command struct {
    Use string // The one-line usage message.
    Short string // The short description shown in the 'help' output.
    Long string // The long message shown in the 'help <this-command>' output.
    Run func(cmd *Command, args []string) // Run runs the command.
}
```

## Flags

A Flag is a way to modify the behavior of a command. Cobra supports
fully POSIX-compliant flags as well as the Go [flag package](https://golang.org/pkg/flag/).
A Cobra command can define flags that persist through to children commands
and flags that are only available to that command.

In the example above, 'port' is the flag.

Flag functionality is provided by the [pflag
library](https://github.com/ogier/pflag), a fork of the flag standard library
which maintains the same interface while adding POSIX compliance.

## Usage

Cobra works by creating a set of commands and then organizing them into a tree.
The tree defines the structure of the application.

Once each command is defined with its corresponding flags, then the
tree is assigned to the commander which is finally executed.

# Installing
Using Cobra is easy. First, use `go get` to install the latest version
of the library. This command will install the `cobra` generator executible
along with the library:

    > go get -v github.com/spf13/cobra/cobra

Next, include Cobra in your application:

```go
import "github.com/spf13/cobra"
```

# Getting Started

While you are welcome to provide your own organization, typically a Cobra based
application will follow the following organizational structure.

```
  ▾ appName/
    ▾ cmd/
        add.go
        your.go
        commands.go
        here.go
      main.go
```

In a Cobra app, typically the main.go file is very bare. It serves, one purpose, to initialize Cobra.

```go
package main

import (
	"fmt"
	"os"

	"{pathToYourApp}/cmd"
)

func main() {
	if err := cmd.RootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(-1)
	}
}
```

## Using the Cobra Generator

Cobra provides its own program that will create your application and add any
commands you want. It's the easiest way to incorporate Cobra into your application.

In order to use the cobra command, compile it using the following command:

    > go install github.com/spf13/cobra/cobra

This will create the cobra executable under your go path bin directory!

### cobra init

The `cobra init [yourApp]` command will create your initial application code
for you. It is a very powerful application that will populate your program with
the right structure so you can immediately enjoy all the benefits of Cobra. It
will also automatically apply the license you specify to your application.

Cobra init is pretty smart. You can provide it a full path, or simply a path
similar to what is expected in the import.

```
cobra init github.com/spf13/newAppName
```

### cobra add

Once an application is initialized Cobra can create additional commands for you.
Let's say you created an app and you wanted the following commands for it:

* app serve
* app config
* app config create

In your project directory (where your main.go file is) you would run the following:

```
cobra add serve
cobra add config
cobra add create -p 'configCmd'
```

Once you have run these three commands you would have an app structure that would look like:

```
  ▾ app/
    ▾ cmd/
        serve.go
        config.go
        create.go
      main.go
```

at this point you can run `go run main.go` and it would run your app. `go run
main.go serve`, `go run main.go config`, `go run main.go config create` along
with `go run main.go help serve`, etc would all work.

Obviously you haven't added your own code to these yet, the commands are ready
for you to give them their tasks. Have fun.

### Configuring the cobra generator

The cobra generator will be easier to use if you provide a simple configuration
file which will help you eliminate providing a bunch of repeated information in
flags over and over.

An example ~/.cobra.yaml file:

```yaml
author: Steve Francia <spf@spf13.com>
license: MIT
```

You can specify no license by setting `license` to `none` or you can specify
a custom license:

```yaml
license:
  header: This file is part of {{ .appName }}.
  text: |
    {{ .copyright }}

    This is my license. There are many like it, but this one is mine.
    My license is my best friend. It is my life. I must master it as I must
    master my life.  
```

## Manually implementing Cobra

To manually implement cobra you need to create a bare main.go file and a RootCmd file.
You will optionally provide additional commands as you see fit.

### Create the root command

The root command represents your binary itself.


#### Manually create rootCmd

Cobra doesn't require any special constructors. Simply create your commands.

Ideally you place this in app/cmd/root.go:

```go
var RootCmd = &cobra.Command{
	Use:   "hugo",
	Short: "Hugo is a very fast static site generator",
	Long: `A Fast and Flexible Static Site Generator built with
                love by spf13 and friends in Go.
                Complete documentation is available at http://hugo.spf13.com`,
	Run: func(cmd *cobra.Command, args []string) {
		// Do Stuff Here
	},
}
```

You will additionally define flags and handle configuration in your init() function.

for example cmd/root.go:

```go
func init() {
	cobra.OnInitialize(initConfig)
	RootCmd.PersistentFlags().StringVar(&cfgFile, "config", "", "config file (default is $HOME/.cobra.yaml)")
	RootCmd.PersistentFlags().StringVarP(&projectBase, "projectbase", "b", "", "base project directory eg. github.com/spf13/")
	RootCmd.PersistentFlags().StringP("author", "a", "YOUR NAME", "Author name for copyright attribution")
	RootCmd.PersistentFlags().StringVarP(&userLicense, "license", "l", "", "Name of license for the project (can provide `licensetext` in config)")
	RootCmd.PersistentFlags().Bool("viper", true, "Use Viper for configuration")
	viper.BindPFlag("author", RootCmd.PersistentFlags().Lookup("author"))
	viper.BindPFlag("projectbase", RootCmd.PersistentFlags().Lookup("projectbase"))
	viper.BindPFlag("useViper", RootCmd.PersistentFlags().Lookup("viper"))
	viper.SetDefault("author", "NAME HERE <EMAIL ADDRESS>")
	viper.SetDefault("license", "apache")
}
```

### Create your main.go

With the root command you need to have your main function execute it.
Execute should be run on the root for clarity, though it can be called on any command.

In a Cobra app, typically the main.go file is very bare. It serves, one purpose, to initialize Cobra.

```go
package main

import (
	"fmt"
	"os"

	"{pathToYourApp}/cmd"
)

func main() {
	if err := cmd.RootCmd.Execute(); err != nil {
		fmt.Println(err)
		os.Exit(-1)
	}
}
```


### Create additional commands

Additional commands can be defined and typically are each given their own file
inside of the cmd/ directory.

If you wanted to create a version command you would create cmd/version.go and
populate it with the following:

```go
package cmd

import (
	"github.com/spf13/cobra"
	"fmt"
)

func init() {
	RootCmd.AddCommand(versionCmd)
}

var versionCmd = &cobra.Command{
	Use:   "version",
	Short: "Print the version number of Hugo",
	Long:  `All software has versions. This is Hugo's`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("Hugo Static Site Generator v0.9 -- HEAD")
	},
}
```

### Attach command to its parent


If you notice in the above example we attach the command to its parent. In
this case the parent is the rootCmd. In this example we are attaching it to the
root, but commands can be attached at any level.

```go
RootCmd.AddCommand(versionCmd)
```

### Remove a command from its parent

Removing a command is not a common action in simple programs, but it allows 3rd
parties to customize an existing command tree.

In this example, we remove the existing `VersionCmd` command of an existing
root command, and we replace it with our own version:

```go
mainlib.RootCmd.RemoveCommand(mainlib.VersionCmd)
mainlib.RootCmd.AddCommand(versionCmd)
```

## Working with Flags

Flags provide modifiers to control how the action command operates.

### Assign flags to a command

Since the flags are defined and used in different locations, we need to
define a variable outside with the correct scope to assign the flag to
work with.

```go
var Verbose bool
var Source string
```

There are two different approaches to assign a flag.

### Persistent Flags

A flag can be 'persistent' meaning that this flag will be available to the
command it's assigned to as well as every command under that command. For
global flags, assign a flag as a persistent flag on the root.

```go
RootCmd.PersistentFlags().BoolVarP(&Verbose, "verbose", "v", false, "verbose output")
```

### Local Flags

A flag can also be assigned locally which will only apply to that specific command.

```go
RootCmd.Flags().StringVarP(&Source, "source", "s", "", "Source directory to read from")
```


## Example

In the example below, we have defined three commands. Two are at the top level
and one (cmdTimes) is a child of one of the top commands. In this case the root
is not executable meaning that a subcommand is required. This is accomplished
by not providing a 'Run' for the 'rootCmd'.

We have only defined one flag for a single command.

More documentation about flags is available at https://github.com/spf13/pflag

```go
package main

import (
	"fmt"
	"strings"

	"github.com/spf13/cobra"
)

func main() {

	var echoTimes int

	var cmdPrint = &cobra.Command{
		Use:   "print [string to print]",
		Short: "Print anything to the screen",
		Long: `print is for printing anything back to the screen.
            For many years people have printed back to the screen.
            `,
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Println("Print: " + strings.Join(args, " "))
		},
	}

	var cmdEcho = &cobra.Command{
		Use:   "echo [string to echo]",
		Short: "Echo anything to the screen",
		Long: `echo is for echoing anything back.
            Echo works a lot like print, except it has a child command.
            `,
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Println("Print: " + strings.Join(args, " "))
		},
	}

	var cmdTimes = &cobra.Command{
		Use:   "times [# times] [string to echo]",
		Short: "Echo anything to the screen more times",
		Long: `echo things multiple times back to the user by providing
            a count and a string.`,
		Run: func(cmd *cobra.Command, args []string) {
			for i := 0; i < echoTimes; i++ {
				fmt.Println("Echo: " + strings.Join(args, " "))
			}
		},
	}

	cmdTimes.Flags().IntVarP(&echoTimes, "times", "t", 1, "times to echo the input")

	var rootCmd = &cobra.Command{Use: "app"}
	rootCmd.AddCommand(cmdPrint, cmdEcho)
	cmdEcho.AddCommand(cmdTimes)
	rootCmd.Execute()
}
```

For a more complete example of a larger application, please checkout [Hugo](http://gohugo.io/).

## The Help Command

Cobra automatically adds a help command to your application when you have subcommands.
This will be called when a user runs 'app help'. Additionally, help will also
support all other commands as input. Say, for instance, you have a command called
'create' without any additional configuration; Cobra will work when 'app help
create' is called.  Every command will automatically have the '--help' flag added.

### Example

The following output is automatically generated by Cobra. Nothing beyond the
command and flag definitions are needed.

    > hugo help

    hugo is the main command, used to build your Hugo site.

    Hugo is a Fast and Flexible Static Site Generator
    built with love by spf13 and friends in Go.

    Complete documentation is available at http://gohugo.io/.

    Usage:
      hugo [flags]
      hugo [command]

    Available Commands:
      server          Hugo runs its own webserver to render the files
      version         Print the version number of Hugo
      config          Print the site configuration
      check           Check content in the source directory
      benchmark       Benchmark hugo by building a site a number of times.
      convert         Convert your content to different formats
      new             Create new content for your site
      list            Listing out various types of content
      undraft         Undraft changes the content's draft status from 'True' to 'False'
      genautocomplete Generate shell autocompletion script for Hugo
      gendoc          Generate Markdown documentation for the Hugo CLI.
      genman          Generate man page for Hugo
      import          Import your site from others.

    Flags:
      -b, --baseURL="": hostname (and path) to the root, e.g. http://spf13.com/
      -D, --buildDrafts[=false]: include content marked as draft
      -F, --buildFuture[=false]: include content with publishdate in the future
          --cacheDir="": filesystem path to cache directory. Defaults: $TMPDIR/hugo_cache/
          --canonifyURLs[=false]: if true, all relative URLs will be canonicalized using baseURL
          --config="": config file (default is path/config.yaml|json|toml)
      -d, --destination="": filesystem path to write files to
          --disableRSS[=false]: Do not build RSS files
          --disableSitemap[=false]: Do not build Sitemap file
          --editor="": edit new content with this editor, if provided
          --ignoreCache[=false]: Ignores the cache directory for reading but still writes to it
          --log[=false]: Enable Logging
          --logFile="": Log File path (if set, logging enabled automatically)
          --noTimes[=false]: Don't sync modification time of files
          --pluralizeListTitles[=true]: Pluralize titles in lists using inflect
          --preserveTaxonomyNames[=false]: Preserve taxonomy names as written ("Gérard Depardieu" vs "gerard-depardieu")
      -s, --source="": filesystem path to read files relative from
          --stepAnalysis[=false]: display memory and timing of different steps of the program
      -t, --theme="": theme to use (located in /themes/THEMENAME/)
          --uglyURLs[=false]: if true, use /filename.html instead of /filename/
      -v, --verbose[=false]: verbose output
          --verboseLog[=false]: verbose logging
      -w, --watch[=false]: watch filesystem for changes and recreate as needed

    Use "hugo [command] --help" for more information about a command.


Help is just a command like any other. There is no special logic or behavior
around it. In fact, you can provide your own if you want.

### Defining your own help

You can provide your own Help command or your own template for the default command to use.

The default help command is

```go
func (c *Command) initHelp() {
	if c.helpCommand == nil {
		c.helpCommand = &Command{
			Use:   "help [command]",
			Short: "Help about any command",
			Long: `Help provides help for any command in the application.
        Simply type ` + c.Name() + ` help [path to command] for full details.`,
			Run: c.HelpFunc(),
		}
	}
	c.AddCommand(c.helpCommand)
}
```

You can provide your own command, function or template through the following methods:

```go
command.SetHelpCommand(cmd *Command)

command.SetHelpFunc(f func(*Command, []string))

command.SetHelpTemplate(s string)
```

The latter two will also apply to any children commands.

## Usage

When the user provides an invalid flag or invalid command, Cobra responds by
showing the user the 'usage'.

### Example
You may recognize this from the help above. That's because the default help
embeds the usage as part of its output.

    Usage:
      hugo [flags]
      hugo [command]

    Available Commands:
      server          Hugo runs its own webserver to render the files
      version         Print the version number of Hugo
      config          Print the site configuration
      check           Check content in the source directory
      benchmark       Benchmark hugo by building a site a number of times.
      convert         Convert your content to different formats
      new             Create new content for your site
      list            Listing out various types of content
      undraft         Undraft changes the content's draft status from 'True' to 'False'
      genautocomplete Generate shell autocompletion script for Hugo
      gendoc          Generate Markdown documentation for the Hugo CLI.
      genman          Generate man page for Hugo
      import          Import your site from others.

    Flags:
      -b, --baseURL="": hostname (and path) to the root, e.g. http://spf13.com/
      -D, --buildDrafts[=false]: include content marked as draft
      -F, --buildFuture[=false]: include content with publishdate in the future
          --cacheDir="": filesystem path to cache directory. Defaults: $TMPDIR/hugo_cache/
          --canonifyURLs[=false]: if true, all relative URLs will be canonicalized using baseURL
          --config="": config file (default is path/config.yaml|json|toml)
      -d, --destination="": filesystem path to write files to
          --disableRSS[=false]: Do not build RSS files
          --disableSitemap[=false]: Do not build Sitemap file
          --editor="": edit new content with this editor, if provided
          --ignoreCache[=false]: Ignores the cache directory for reading but still writes to it
          --log[=false]: Enable Logging
          --logFile="": Log File path (if set, logging enabled automatically)
          --noTimes[=false]: Don't sync modification time of files
          --pluralizeListTitles[=true]: Pluralize titles in lists using inflect
          --preserveTaxonomyNames[=false]: Preserve taxonomy names as written ("Gérard Depardieu" vs "gerard-depardieu")
      -s, --source="": filesystem path to read files relative from
          --stepAnalysis[=false]: display memory and timing of different steps of the program
      -t, --theme="": theme to use (located in /themes/THEMENAME/)
          --uglyURLs[=false]: if true, use /filename.html instead of /filename/
      -v, --verbose[=false]: verbose output
          --verboseLog[=false]: verbose logging
      -w, --watch[=false]: watch filesystem for changes and recreate as needed

### Defining your own usage
You can provide your own usage function or template for Cobra to use.

The default usage function is:

```go
return func(c *Command) error {
	err := tmpl(c.Out(), c.UsageTemplate(), c)
	return err
}
```

Like help, the function and template are overridable through public methods:

```go
command.SetUsageFunc(f func(*Command) error)

command.SetUsageTemplate(s string)
```

## PreRun or PostRun Hooks

It is possible to run functions before or after the main `Run` function of your command. The `PersistentPreRun` and `PreRun` functions will be executed before `Run`. `PersistentPostRun` and `PostRun` will be executed after `Run`.  The `Persistent*Run` functions will be inherited by children if they do not declare their own.  These functions are run in the following order:

- `PersistentPreRun`
- `PreRun`
- `Run`
- `PostRun`
- `PersistentPostRun`

An example of two commands which use all of these features is below.  When the subcommand is executed, it will run the root command's `PersistentPreRun` but not the root command's `PersistentPostRun`:

```go
package main

import (
	"fmt"

	"github.com/spf13/cobra"
)

func main() {

	var rootCmd = &cobra.Command{
		Use:   "root [sub]",
		Short: "My root command",
		PersistentPreRun: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside rootCmd PersistentPreRun with args: %v\n", args)
		},
		PreRun: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside rootCmd PreRun with args: %v\n", args)
		},
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside rootCmd Run with args: %v\n", args)
		},
		PostRun: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside rootCmd PostRun with args: %v\n", args)
		},
		PersistentPostRun: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside rootCmd PersistentPostRun with args: %v\n", args)
		},
	}

	var subCmd = &cobra.Command{
		Use:   "sub [no options!]",
		Short: "My subcommand",
		PreRun: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside subCmd PreRun with args: %v\n", args)
		},
		Run: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside subCmd Run with args: %v\n", args)
		},
		PostRun: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside subCmd PostRun with args: %v\n", args)
		},
		PersistentPostRun: func(cmd *cobra.Command, args []string) {
			fmt.Printf("Inside subCmd PersistentPostRun with args: %v\n", args)
		},
	}

	rootCmd.AddCommand(subCmd)

	rootCmd.SetArgs([]string{""})
	_ = rootCmd.Execute()
	fmt.Print("\n")
	rootCmd.SetArgs([]string{"sub", "arg1", "arg2"})
	_ = rootCmd.Execute()
}
```


## Alternative Error Handling

Cobra also has functions where the return signature is an error. This allows for errors to bubble up to the top,
providing a way to handle the errors in one location. The current list of functions that return an error is:

* PersistentPreRunE
* PreRunE
* RunE
* PostRunE
* PersistentPostRunE

If you would like to silence the default `error` and `usage` output in favor of your own, you can set `SilenceUsage`
and `SilenceErrors` to `true` on the command. A child command respects these flags if they are set on the parent
command.

**Example Usage using RunE:**

```go
package main

import (
	"errors"
	"log"

	"github.com/spf13/cobra"
)

func main() {
	var rootCmd = &cobra.Command{
		Use:   "hugo",
		Short: "Hugo is a very fast static site generator",
		Long: `A Fast and Flexible Static Site Generator built with
                love by spf13 and friends in Go.
                Complete documentation is available at http://hugo.spf13.com`,
		RunE: func(cmd *cobra.Command, args []string) error {
			// Do Stuff Here
			return errors.New("some random error")
		},
	}

	if err := rootCmd.Execute(); err != nil {
		log.Fatal(err)
	}
}
```

## Suggestions when "unknown command" happens

Cobra will print automatic suggestions when "unknown command" errors happen. This allows Cobra to behave similarly to the `git` command when a typo happens. For example:

```
$ hugo srever
Error: unknown command "srever" for "hugo"

Did you mean this?
        server

Run 'hugo --help' for usage.
```

Suggestions are automatic based on every subcommand registered and use an implementation of [Levenshtein distance](http://en.wikipedia.org/wiki/Levenshtein_distance). Every registered command that matches a minimum distance of 2 (ignoring case) will be displayed as a suggestion.

If you need to disable suggestions or tweak the string distance in your command, use:

```go
command.DisableSuggestions = true
```

or

```go
command.SuggestionsMinimumDistance = 1
```

You can also explicitly set names for which a given command will be suggested using the `SuggestFor` attribute. This allows suggestions for strings that are not close in terms of string distance, but makes sense in your set of commands and for some which you don't want aliases. Example:

```
$ kubectl remove
Error: unknown command "remove" for "kubectl"

Did you mean this?
        delete

Run 'kubectl help' for usage.
```

## Generating Markdown-formatted documentation for your command

Cobra can generate a Markdown-formatted document based on the subcommands, flags, etc. A simple example of how to do this for your command can be found in [Markdown Docs](doc/md_docs.md).

## Generating man pages for your command

Cobra can generate a man page based on the subcommands, flags, etc. A simple example of how to do this for your command can be found in [Man Docs](doc/man_docs.md).

## Generating bash completions for your command

Cobra can generate a bash-completion file. If you add more information to your command, these completions can be amazingly powerful and flexible.  Read more about it in [Bash Completions](bash_completions.md).

## Debugging

Cobra provides a ‘DebugFlags’ method on a command which, when called, will print
out everything Cobra knows about the flags for each command.

### Example

```go
command.DebugFlags()
```

## Release Notes
* **0.9.0** June 17, 2014
  * flags can appears anywhere in the args (provided they are unambiguous)
  * --help prints usage screen for app or command
  * Prefix matching for commands
  * Cleaner looking help and usage output
  * Extensive test suite
* **0.8.0** Nov 5, 2013
  * Reworked interface to remove commander completely
  * Command now primary structure
  * No initialization needed
  * Usage & Help templates & functions definable at any level
  * Updated Readme
* **0.7.0** Sept 24, 2013
  * Needs more eyes
  * Test suite
  * Support for automatic error messages
  * Support for help command
  * Support for printing to any io.Writer instead of os.Stderr
  * Support for persistent flags which cascade down tree
  * Ready for integration into Hugo
* **0.1.0** Sept 3, 2013
  * Implement first draft

## Extensions

Libraries for extending Cobra:

* [cmdns](https://github.com/gosuri/cmdns): Enables name spacing a command's immediate children. It provides an alternative way to structure subcommands, similar to `heroku apps:create` and `ovrclk clusters:launch`.

## ToDo
* Launch proper documentation site

## Contributing

1. Fork it
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Contributors

Names in no particular order:

* [spf13](https://github.com/spf13),
[eparis](https://github.com/eparis),
[bep](https://github.com/bep), and many more!

## License

Cobra is released under the Apache 2.0 license. See [LICENSE.txt](https://github.com/spf13/cobra/blob/master/LICENSE.txt)


[![Bitdeli Badge](https://d2weczhvl823v0.cloudfront.net/spf13/cobra/trend.png)](https://bitdeli.com/free "Bitdeli Badge")
jWalterWeatherman
=================

Seamless printing to the terminal (stdout) and logging to a io.Writer
(file) that’s as easy to use as fmt.Println.

![and_that__s_why_you_always_leave_a_note_by_jonnyetc-d57q7um](https://cloud.githubusercontent.com/assets/173412/11002937/ccd01654-847d-11e5-828e-12ebaf582eaf.jpg)
Graphic by [JonnyEtc](http://jonnyetc.deviantart.com/art/And-That-s-Why-You-Always-Leave-a-Note-315311422)

JWW is primarily a wrapper around the excellent standard log library. It
provides a few advantages over using the standard log library alone.

1. Ready to go out of the box. 
2. One library for both printing to the terminal and logging (to files).
3. Really easy to log to either a temp file or a file you specify.


I really wanted a very straightforward library that could seamlessly do
the following things.

1. Replace all the println, printf, etc statements thought my code with
   something more useful
2. Allow the user to easily control what levels are printed to stdout
3. Allow the user to easily control what levels are logged
4. Provide an easy mechanism (like fmt.Println) to print info to the user
   which can be easily logged as well 
5. Due to 2 & 3 provide easy verbose mode for output and logs
6. Not have any unnecessary initialization cruft. Just use it.

# Usage

## Step 1. Use it
Put calls throughout your source based on type of feedback.
No initialization or setup needs to happen. Just start calling things.

Available Loggers are:

 * TRACE
 * DEBUG
 * INFO
 * WARN
 * ERROR
 * CRITICAL
 * FATAL

These each are loggers based on the log standard library and follow the
standard usage. Eg.

```go
    import (
        jww "github.com/spf13/jwalterweatherman"
    )

    ...

    if err != nil {

        // This is a pretty serious error and the user should know about
        // it. It will be printed to the terminal as well as logged under the
        // default thresholds.

        jww.ERROR.Println(err)
    }

    if err2 != nil {
        // This error isn’t going to materially change the behavior of the
        // application, but it’s something that may not be what the user
        // expects. Under the default thresholds, Warn will be logged, but
        // not printed to the terminal. 

        jww.WARN.Println(err2)
    }

    // Information that’s relevant to what’s happening, but not very
    // important for the user. Under the default thresholds this will be
    // discarded.

    jww.INFO.Printf("information %q", response)

```

NOTE: You can also use the library in a non-global setting by creating an instance of a Notebook:

```go
notepad = jww.NewNotepad(jww.LevelInfo, jww.LevelTrace, os.Stdout, ioutil.Discard, "", log.Ldate|log.Ltime)
notepad.WARN.Println("Some warning"")
```

_Why 7 levels?_

Maybe you think that 7 levels are too much for any application... and you
are probably correct. Just because there are seven levels doesn’t mean
that you should be using all 7 levels. Pick the right set for your needs.
Remember they only have to mean something to your project.

## Step 2. Optionally configure JWW

Under the default thresholds :

 * Debug, Trace & Info goto /dev/null
 * Warn and above is logged (when a log file/io.Writer is provided)
 * Error and above is printed to the terminal (stdout)

### Changing the thresholds

The threshold can be changed at any time, but will only affect calls that
execute after the change was made.

This is very useful if your application has a verbose mode. Of course you
can decide what verbose means to you or even have multiple levels of
verbosity.


```go
    import (
        jww "github.com/spf13/jwalterweatherman"
    )

    if Verbose {
        jww.SetLogThreshold(jww.LevelTrace)
        jww.SetStdoutThreshold(jww.LevelInfo)
    }
```

Note that JWW's own internal output uses log levels as well, so set the log
level before making any other calls if you want to see what it's up to.


### Setting a log file

JWW can log to any `io.Writer`:


```go

    jww.SetLogOutput(customWriter) 

```


# More information

This is an early release. I’ve been using it for a while and this is the
third interface I’ve tried. I like this one pretty well, but no guarantees
that it won’t change a bit.

I wrote this for use in [hugo](http://hugo.spf13.com). If you are looking
for a static website engine that’s super fast please checkout Hugo.
