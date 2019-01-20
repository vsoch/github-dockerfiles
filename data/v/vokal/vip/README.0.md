Instructions
============

Install the package with:

    go get gopkg.in/check.v1
    
Import it with:

    import "gopkg.in/check.v1"

and use _check_ as the package name inside the code.

For more details, visit the project page:

* http://labix.org/gocheck

and the API documentation:

* https://gopkg.in/check.v1
q
==========

`q` is a queue used to concurrently process jobs.
```Go
// buffer size for the queue to hold jobs on. 
Queue = q.New(buff)
```
Returns a new q.Queue.

```Go
// n is the number of workers which will
Queue.Start(n)
```
Initializes the workers, now the Queue is ready to start processing jobs.


```Go
// j is a Job, anything which implements the Run() method
Queue.Push(j)
```

Pushes jobs onto the queue.  A Job is anything thing that implements `Run()` which is responsible 
for Processing the job.


If you want to halt the Queue to prevent an additional jobs from being processed
`Queue.Quit <- true` will halt the queue.  However after the Queue has halted any Jobs that were processing will complete. 


![Q](http://upload.wikimedia.org/wikipedia/commons/thumb/6/65/Desmond_Llewelyn_01.jpg/250px-Desmond_Llewelyn_01.jpg)
go-ini
======

INI parsing library for Go (golang).

View the API documentation [here](http://godoc.org/github.com/vaughan0/go-ini).

Usage
-----

Parse an INI file:

```go
import "github.com/vaughan0/go-ini"

file, err := ini.LoadFile("myfile.ini")
```

Get data from the parsed file:

```go
name, ok := file.Get("person", "name")
if !ok {
  panic("'name' variable missing from 'person' section")
}
```

Iterate through values in a section:

```go
for key, value := range file["mysection"] {
  fmt.Printf("%s => %s\n", key, value)
}
```

Iterate through sections in a file:

```go
for name, section := range file {
  fmt.Printf("Section name: %s\n", name)
}
```

File Format
-----------

INI files are parsed by go-ini line-by-line. Each line may be one of the following:

  * A section definition: [section-name]
  * A property: key = value
  * A comment: #blahblah _or_ ;blahblah
  * Blank. The line will be ignored.

Properties defined before any section headers are placed in the default section, which has
the empty string as it's key.

Example:

```ini
# I am a comment
; So am I!

[apples]
colour = red or green
shape = applish

[oranges]
shape = square
colour = blue
```
# groupcache

## Summary

groupcache is a caching and cache-filling library, intended as a
replacement for memcached in many cases.

For API docs and examples, see http://godoc.org/github.com/golang/groupcache

## Comparison to memcached

### **Like memcached**, groupcache:

 * shards by key to select which peer is responsible for that key

### **Unlike memcached**, groupcache:

 * does not require running a separate set of servers, thus massively
   reducing deployment/configuration pain.  groupcache is a client
   library as well as a server.  It connects to its own peers.

 * comes with a cache filling mechanism.  Whereas memcached just says
   "Sorry, cache miss", often resulting in a thundering herd of
   database (or whatever) loads from an unbounded number of clients
   (which has resulted in several fun outages), groupcache coordinates
   cache fills such that only one load in one process of an entire
   replicated set of processes populates the cache, then multiplexes
   the loaded value to all callers.

 * does not support versioned values.  If key "foo" is value "bar",
   key "foo" must always be "bar".  There are neither cache expiration
   times, nor explicit cache evictions.  Thus there is also no CAS,
   nor Increment/Decrement.  This also means that groupcache....

 * ... supports automatic mirroring of super-hot items to multiple
   processes.  This prevents memcached hot spotting where a machine's
   CPU and/or NIC are overloaded by very popular keys/values.

 * is currently only available for Go.  It's very unlikely that I
   (bradfitz@) will port the code to any other language.

## Loading process

In a nutshell, a groupcache lookup of **Get("foo")** looks like:

(On machine #5 of a set of N machines running the same code)

 1. Is the value of "foo" in local memory because it's super hot?  If so, use it.

 2. Is the value of "foo" in local memory because peer #5 (the current
    peer) is the owner of it?  If so, use it.

 3. Amongst all the peers in my set of N, am I the owner of the key
    "foo"?  (e.g. does it consistent hash to 5?)  If so, load it.  If
    other callers come in, via the same process or via RPC requests
    from peers, they block waiting for the load to finish and get the
    same answer.  If not, RPC to the peer that's the owner and get
    the answer.  If the RPC fails, just load it locally (still with
    local dup suppression).

## Users

groupcache is in production use by dl.google.com (its original user),
parts of Blogger, parts of Google Code, parts of Google Fiber, parts
of Google production monitoring systems, etc.

## Presentations

See http://talks.golang.org/2013/oscon-dl.slide

## Help

Use the golang-nuts mailing list for any discussion or questions.
mux
===
[![Build Status](https://travis-ci.org/gorilla/mux.png?branch=master)](https://travis-ci.org/gorilla/mux)

gorilla/mux is a powerful URL router and dispatcher.

Read the full documentation here: http://www.gorillatoolkit.org/pkg/mux
context
=======
[![Build Status](https://travis-ci.org/gorilla/context.png?branch=master)](https://travis-ci.org/gorilla/context)

gorilla/context is a general purpose registry for global request variables.

Read the full documentation here: http://www.gorillatoolkit.org/pkg/context
# Imaging

[![GoDoc](https://godoc.org/github.com/disintegration/imaging?status.svg)](https://godoc.org/github.com/disintegration/imaging)
[![Build Status](https://travis-ci.org/disintegration/imaging.svg?branch=master)](https://travis-ci.org/disintegration/imaging)
[![Coverage Status](https://coveralls.io/repos/github/disintegration/imaging/badge.svg?branch=master)](https://coveralls.io/github/disintegration/imaging?branch=master)

Package imaging provides basic image manipulation functions (resize, rotate, flip, crop, etc.). 
This package is based on the standard Go image package and works best along with it. 

Image manipulation functions provided by the package take any image type 
that implements `image.Image` interface as an input, and return a new image of 
`*image.NRGBA` type (32bit RGBA colors, not premultiplied by alpha).

## Installation

Imaging requires Go version 1.2 or greater.

    go get -u github.com/disintegration/imaging
    
## Documentation

http://godoc.org/github.com/disintegration/imaging

## Usage examples

A few usage examples can be found below. See the documentation for the full list of supported functions. 

### Image resizing
```go
// resize srcImage to size = 128x128px using the Lanczos filter
dstImage128 := imaging.Resize(srcImage, 128, 128, imaging.Lanczos)

// resize srcImage to width = 800px preserving the aspect ratio
dstImage800 := imaging.Resize(srcImage, 800, 0, imaging.Lanczos)

// scale down srcImage to fit the 800x600px bounding box
dstImageFit := imaging.Fit(srcImage, 800, 600, imaging.Lanczos)

// resize and crop the srcImage to fill the 100x100px area
dstImageFill := imaging.Fill(srcImage, 100, 100, imaging.Center, imaging.Lanczos)
```

Imaging supports image resizing using various resampling filters. The most notable ones:
- `NearestNeighbor` - Fastest resampling filter, no antialiasing.
- `Box` - Simple and fast averaging filter appropriate for downscaling. When upscaling it's similar to NearestNeighbor.
- `Linear` - Bilinear filter, smooth and reasonably fast.
- `MitchellNetravali` - А smooth bicubic filter.
- `CatmullRom` - A sharp bicubic filter. 
- `Gaussian` - Blurring filter that uses gaussian function, useful for noise removal.
- `Lanczos` - High-quality resampling filter for photographic images yielding sharp results, but it's slower than cubic filters.

The full list of supported filters:  NearestNeighbor, Box, Linear, Hermite, MitchellNetravali, CatmullRom, BSpline, Gaussian, Lanczos, Hann, Hamming, Blackman, Bartlett, Welch, Cosine. Custom filters can be created using ResampleFilter struct.

**Resampling filters comparison**

Original image. Will be resized from 512x512px to 128x128px. 

![srcImage](http://disintegration.github.io/imaging/in_lena_bw_512.png)

Filter | Resize result
---|---
`imaging.NearestNeighbor` | ![dstImage](http://disintegration.github.io/imaging/out_resize_down_nearest.png) 
`imaging.Box` | ![dstImage](http://disintegration.github.io/imaging/out_resize_down_box.png)
`imaging.Linear` | ![dstImage](http://disintegration.github.io/imaging/out_resize_down_linear.png)
`imaging.MitchellNetravali` | ![dstImage](http://disintegration.github.io/imaging/out_resize_down_mitchell.png)
`imaging.CatmullRom` | ![dstImage](http://disintegration.github.io/imaging/out_resize_down_catrom.png)
`imaging.Gaussian` | ![dstImage](http://disintegration.github.io/imaging/out_resize_down_gaussian.png)
`imaging.Lanczos` | ![dstImage](http://disintegration.github.io/imaging/out_resize_down_lanczos.png)

**Resize functions comparison**

Original image:

![srcImage](http://disintegration.github.io/imaging/in.jpg)

Resize the image to width=100px and height=100px:

```go
dstImage := imaging.Resize(srcImage, 100, 100, imaging.Lanczos)
```
![dstImage](http://disintegration.github.io/imaging/out-comp-resize.jpg) 

Resize the image to width=100px preserving the aspect ratio:

```go
dstImage := imaging.Resize(srcImage, 100, 0, imaging.Lanczos)
```
![dstImage](http://disintegration.github.io/imaging/out-comp-fit.jpg) 

Resize the image to fit the 100x100px boundng box preserving the aspect ratio:

```go
dstImage := imaging.Fit(srcImage, 100, 100, imaging.Lanczos)
```
![dstImage](http://disintegration.github.io/imaging/out-comp-fit.jpg) 

Resize and crop the image with a center anchor point to fill the 100x100px area:

```go
dstImage := imaging.Fill(srcImage, 100, 100, imaging.Center, imaging.Lanczos)
```
![dstImage](http://disintegration.github.io/imaging/out-comp-fill.jpg) 

### Gaussian Blur
```go
dstImage := imaging.Blur(srcImage, 0.5)
```

Sigma parameter allows to control the strength of the blurring effect.

Original image | Sigma = 0.5 | Sigma = 1.5
---|---|---
![srcImage](http://disintegration.github.io/imaging/in_lena_bw_128.png) | ![dstImage](http://disintegration.github.io/imaging/out_blur_0.5.png) | ![dstImage](http://disintegration.github.io/imaging/out_blur_1.5.png)

### Sharpening
```go
dstImage := imaging.Sharpen(srcImage, 0.5)
```

Uses gaussian function internally. Sigma parameter allows to control the strength of the sharpening effect.

Original image | Sigma = 0.5 | Sigma = 1.5
---|---|---
![srcImage](http://disintegration.github.io/imaging/in_lena_bw_128.png) | ![dstImage](http://disintegration.github.io/imaging/out_sharpen_0.5.png) | ![dstImage](http://disintegration.github.io/imaging/out_sharpen_1.5.png)

### Gamma correction
```go
dstImage := imaging.AdjustGamma(srcImage, 0.75)
```

Original image | Gamma = 0.75 | Gamma = 1.25
---|---|---
![srcImage](http://disintegration.github.io/imaging/in_lena_bw_128.png) | ![dstImage](http://disintegration.github.io/imaging/out_gamma_0.75.png) | ![dstImage](http://disintegration.github.io/imaging/out_gamma_1.25.png)

### Contrast adjustment
```go
dstImage := imaging.AdjustContrast(srcImage, 20)
```

Original image | Contrast = 20 | Contrast = -20
---|---|---
![srcImage](http://disintegration.github.io/imaging/in_lena_bw_128.png) | ![dstImage](http://disintegration.github.io/imaging/out_contrast_p20.png) | ![dstImage](http://disintegration.github.io/imaging/out_contrast_m20.png)

### Brightness adjustment
```go
dstImage := imaging.AdjustBrightness(srcImage, 20)
```

Original image | Brightness = 20 | Brightness = -20
---|---|---
![srcImage](http://disintegration.github.io/imaging/in_lena_bw_128.png) | ![dstImage](http://disintegration.github.io/imaging/out_brightness_p20.png) | ![dstImage](http://disintegration.github.io/imaging/out_brightness_m20.png)


### Complete code example
Here is the code example that loads several images, makes thumbnails of them
and combines them together side-by-side.

```go
package main

import (
    "image"
    "image/color"
    
    "github.com/disintegration/imaging"
)

func main() {

    // input files
    files := []string{"01.jpg", "02.jpg", "03.jpg"}

    // load images and make 100x100 thumbnails of them
    var thumbnails []image.Image
    for _, file := range files {
        img, err := imaging.Open(file)
        if err != nil {
            panic(err)
        }
        thumb := imaging.Thumbnail(img, 100, 100, imaging.CatmullRom)
        thumbnails = append(thumbnails, thumb)
    }

    // create a new blank image
    dst := imaging.New(100*len(thumbnails), 100, color.NRGBA{0, 0, 0, 0})

    // paste thumbnails into the new image side by side
    for i, thumb := range thumbnails {
        dst = imaging.Paste(dst, thumb, image.Pt(i*100, 0))
    }

    // save the combined image to file
    err := imaging.Save(dst, "dst.jpg")
    if err != nil {
        panic(err)
    }
}
```

To regenerate the regression test data, run `go generate` inside the exif
package directory and commit the changes to *regress_expected_test.go*.

### Vips for go

This package is powered by the blazingly fast [libvips](https://github.com/jcupitt/libvips) image
processing library, originally created in 1989 at Birkbeck College and currently maintained by 
[JohnCupitt](https://github.com/jcupitt).

This is a loosely port of [sharp](https://github.com/lovell/sharp) an awesome module for node.js
built by [Lovell Fuller](https://github.com/lovell)

The typical use case for this high speed package is to convert large images of many formats
to smaller, web-friendly JPEG, PNG images of varying dimensions.

The performance of JPEG resizing is typically 8x faster than ImageMagick and GraphicsMagick, based
mainly on the number of CPU cores available.

When generating JPEG output all metadata is removed and Huffman tables optimised without having to
use separate command line tools like [jpegoptim](https://github.com/tjko/jpegoptim) and
[jpegtran](http://jpegclub.org/jpegtran/).

## Installation

    go get github.com/daddye/vips

* [libvips](https://github.com/jcupitt/libvips) v7.38.5+

_libvips_ can take advantage of [liborc](http://code.entropywave.com/orc/) if present. 

### Install libvips on Mac OS

    brew install homebrew/science/vips  --without-fftw --without-libexif --without-libgf \
    	--without-little-cms --without-orc --without-pango

### Install libvips on Linux

Compiling from source is recommended:

    sudo apt-get install automake build-essential git gobject-introspection \
      libglib2.0-dev libjpeg-turbo8-dev libpng12-dev gtk-doc-tools
    git clone https://github.com/jcupitt/libvips.git
    cd libvips
    ./bootstrap.sh
    ./configure --enable-debug=no --without-python --without-fftw --without-libexif \
      --without-libgf --without-little-cms --without-orc --without-pango --prefix=/usr
    make
    sudo make install
    sudo ldconfig

## Usage

You can use package from the command line (`go install github.com/daddye/vips/vips-cmd`):

    vips-cmd -file test.jpg -width 400 -height 600 > /tmp/test.jpg

Or simply importing the package and then:

```go
options := vips.Options{
	Width:        800,
	Height:       600,
	Crop:         false,
	Extend:       vips.EXTEND_WHITE,
	Interpolator: vips.BILINEAR,
	Gravity:      vips.CENTRE,
	Quality:      95,
}
f, _ := os.Open("/tmp/test.jpg")
inBuf, _ := ioutil.ReadAll(f)
buf, err := vips.Resize(inBuf, options)
if err != nil {
	fmt.Fprintln(os.Stderr, err)
	return
}
// do some with your resized image `buf`
```

## Performance

Test by @lovell

### Test environment

* Intel Xeon [L5520](http://ark.intel.com/products/40201/Intel-Xeon-Processor-L5520-8M-Cache-2_26-GHz-5_86-GTs-Intel-QPI) 2.27GHz 8MB cache
* Ubuntu 13.10
* libvips 7.38.5

### The contenders

* [imagemagick-native](https://github.com/mash/node-imagemagick-native) - Supports Buffers only and blocks main V8 thread whilst processing.
* [imagemagick](https://github.com/rsms/node-imagemagick) - Supports filesystem only and "has been unmaintained for a long time".
* [gm](https://github.com/aheckmann/gm) - Fully featured wrapper around GraphicsMagick.
* [sharp](https://github.com/lovell/sharp) - Caching within libvips disabled to ensure a fair comparison.

### The task

Decompress a 2725x2225 JPEG image, resize and crop to 720x480, then compress to JPEG.

### Results

| Module                | Input  | Output | Ops/sec | Speed-up |
| :-------------------- | :----- | :----- | ------: | -------: |
| imagemagick-native    | buffer | buffer |    0.97 |        1 |
| imagemagick           | file   | file   |    2.49 |      2.6 |
| gm                    | buffer | file   |    3.72 |      3.8 |
| gm                    | buffer | buffer |    3.80 |      3.9 |
| gm                    | file   | file   |    3.67 |      3.8 |
| gm                    | file   | buffer |    3.67 |      3.8 |
| sharp                 | buffer | file   |   13.62 |     14.0 |
| sharp                 | buffer | buffer |   12.43 |     12.8 |
| sharp                 | file   | file   |   13.02 |     13.4 |
| sharp                 | file   | buffer |   11.15 |     11.5 |
| sharp +sharpen        | file   | buffer |   10.26 |     10.6 |
| sharp +progressive    | file   | buffer |    9.44 |      9.7 |
| sharp +sequentialRead | file   | buffer |   11.94 |     12.3 |

You can expect much greater performance with caching enabled (default) and using 16+ core machines.

## Thanks

This module would never have been possible without the help and code contributions of the following people:

* [Lovell Fuller](https://github.com/lovell)
* [John Cupitt](https://github.com/jcupitt)
* [Pierre Inglebert](https://github.com/pierreinglebert)
* [Jonathan Ong](https://github.com/jonathanong)
* [Chanon Sajjamanochai](https://github.com/chanon)
* [Juliano Julio](https://github.com/julianojulio)

## License

Copyright (C) 2014 Davide D'Agostino

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the "Software"),
to deal in the Software without restriction, including without limitation
the rights to use, copy, modify, merge, publish, distribute, sublicense,
and/or sell copies of the Software, and to permit persons to whom the
Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included
in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE
OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
