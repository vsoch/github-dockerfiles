Monocle
=======

_Live transform and cache your images at load time_

## Table of content

- [The problem](#the-problem)
- [Our solution](#our-solution)
- [Examples](#examples)
- [Try it](#try-it)
- [Caching considerations](#caching-considerations)
- [Image helpers - TBD](#image-helpers)
- [Credits](#credits)
- [License - TBD](#license)

## The problem

Dealing with images is a common requirement when putting a website together.

The _classic_ way to deal with large images is to create series of resized
images, and use the closest image in size on the frontend.

```html
 <img src='http://images.crowdtap.com/complicated_path/monocle-original.png'/>
 <img src='http://images.crowdtap.com/complicated_path/monocle-large.png'/>
 <img src='http://images.crowdtap.com/complicated_path/monocle-medium.png'/>
 <img src='http://images.crowdtap.com/complicated_path/monocle-small.png'/>
```

results in this:

![Monocle Original](doc/images/monocle-original.png)
![Monocle Big](doc/images/monocle-large.png)
![Monocle Medium](doc/images/monocle-medium.png)
![Monocle Small](doc/images/monocle-small.png)

If the image place holder is too big for your resized image, you will end up
with a **pixelated** image, on the other end if it is too small, you will
**lose bandwidth**, and your loadtime will be impacted. This classic approach
is sub-optimal.

## Our solution

We think we have a better way to deal with images using _**live transformation and caching**_.

Instead of transforming images in advanced, and loading them using their hard coded names,
we ask monocle to load the original image from the source, and append
transformation parameters to the URL. This way you only need *one reference* to
the original image in your model and database, the transformation parameters
are choosen when implementing the frontend part of your website, there is no
need to guess in advance. The monocle approach is very agile in that sense.

## Examples

Assuming the Monocle service is running on `http://monocle.ec2.crowdtap.com/transform_image`, and the source of the image we are resizing is `https://raw.githubusercontent.com/crowdtap/monocle/master/doc/images/monocle-original.png`, we can do the following...

### Resize to 150px size...

```html
 <img src='http://monocle.ec2.crowdtap.com/transform_image?src=https://raw.githubusercontent.com/crowdtap/monocle/master/doc/images/monocle-original.png&resize=150'/>
```

![Monocle Small](http://dgj5ep7xp9u24.cloudfront.net/transform_image?src=https://raw.githubusercontent.com/crowdtap/monocle/master/doc/images/monocle-original.png&resize=150)

Notice how the `src` for the image is url encoded.

### Add a black and white filter and mirror...

```html
 <img src='http://monocle.ec2.crowdtap.com/transform_image?src=https://raw.githubusercontent.com/crowdtap/monocle/master/doc/images/monocle-original.png&resize=150&greyscale=true&flop=true'/>
```

![Monocle Small](http://dgj5ep7xp9u24.cloudfront.net/transform_image?src=https://raw.githubusercontent.com/crowdtap/monocle/master/doc/images/monocle-original.png&resize=150&greyscale=true&flop=true)

### Rotate by 45 degrees...

```html
 <img src='http://monocle.crowdtap.com/transform_image?src=https://raw.githubusercontent.com/crowdtap/monocle/master/doc/images/monocle-original.png&resize=150&greyscale=true&flop=true&rotate=45'/>
```

![Monocle Small](http://dgj5ep7xp9u24.cloudfront.net/transform_image?src=https://raw.githubusercontent.com/crowdtap/monocle/master/doc/images/monocle-original.png&resize=150&greyscale=true&flop=true&rotate=45)

### And more...

```html
 <img src='http://monocle.crowdtap.com/transform_image?src=http://images.crowdtap.com/images/monocle-original.png&resize=150&greyscale=true&flop=true&jcn=true'/>
```

![Monocle Small](http://dgj5ep7xp9u24.cloudfront.net/transform_image?src=https://raw.githubusercontent.com/crowdtap/monocle/master/doc/images/monocle-original.png&resize=150&greyscale=true&flop=true&jcn=true)

An extensive list of parameters you can use are available in the [Dragonfly documentation](http://markevans.github.io/dragonfly/file.ImageMagick.html)

### Cleaning up monocle url

The Monocle URL structure are readable but they are not really clean. Having a fully specified URL (the image source) within a url is dirty.

Monocle URL with query string parameters (used above):

`http://monocle.crowdtap.com/transform_image?src=https://raw.githubusercontent.com/crowdtap/monocle/master/doc/images/monocle-original.png&resize=150`

There are two ways in which you can clean it up:

#### Slash syntax

route: `/transform_image/q/`

Parameters:

`src=https://raw.githubusercontent.com/crowdtap/monocle/master/doc/images/monocle-original.png&resize=150&greyscale=true&flop=true&jcn=true`

URL encode the src & use `/` separators to specify parameters:

`src/https%3A%2F%2Fraw.githubusercontent.com%2Fcrowdtap%2Fmonocle%2Fmaster%2Fdoc%2Fimages%2Fmonocle-original.png/resize/150`

Use it like this:

`http://monocle.crowdtap.com/transform_image/q/src/https%3A%2F%2Fraw.githubusercontent.com%2Fcrowdtap%2Fmonocle%2Fmaster%2Fdoc%2Fimages%2Fmonocle-original.png/resize/150`

Which results in:

![Monocle Small](http://dgj5ep7xp9u24.cloudfront.net/transform_image/q/src/https%3A%2F%2Fraw.githubusercontent.com%2Fcrowdtap%2Fmonocle%2Fmaster%2Fdoc%2Fimages%2Fmonocle-original.png/resize/150)

#### Base 64 encoding

route: `/transform_image/qe/`

You can use the following format:

Parameters:

`src=https://raw.githubusercontent.com/crowdtap/monocle/master/doc/images/monocle-original.png&resize=150&greyscale=true&flop=true&jcn=true`

URL encode the src & use `/` separators to specify parameters:

`src/https%3A%2F%2Fraw.githubusercontent.com%2Fcrowdtap%2Fmonocle%2Fmaster%2Fdoc%2Fimages%2Fmonocle-original.png/resize/150`

Base 64:

`c3JjL2h0dHBzJTNBJTJGJTJGcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSUyRmNyb3dkdGFwJTJG
bW9ub2NsZSUyRm1hc3RlciUyRmRvYyUyRmltYWdlcyUyRm1vbm9jbGUtb3JpZ2luYWwucG5nL3Jl
c2l6ZS8xNTA=`

You can use it as follow:

`http://monocle.crowdtap.com/transform_image/qe/c3JjL2h0dHBzJTNBJTJGJTJGcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSUyRmNyb3dkdGFwJTJG
bW9ub2NsZSUyRm1hc3RlciUyRmRvYyUyRmltYWdlcyUyRm1vbm9jbGUtb3JpZ2luYWwucG5nL3Jl
c2l6ZS8xNTA=`

Which results in:

![Monocle Small](http://dgj5ep7xp9u24.cloudfront.net/transform_image/qe/c3JjL2h0dHBzJTNBJTJGJTJGcmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSUyRmNyb3dkdGFwJTJGbW9ub2NsZSUyRm1hc3RlciUyRmRvYyUyRmltYWdlcyUyRm1vbm9jbGUtb3JpZ2luYWwucG5nL3Jlc2l6ZS8xNTA=)


## Caching considerations

Resizing a given image over an over is very inefficient, hence the need for a
caching mechanism. Caches are beyond the scope of this documentation, though
adding a caching layer on top of your service is easy. At Crowdtap we are using
Cloudfront, the caching and CDN service from Amazon.

There is a small problem though, the query parameters are not taken into
consideration by most caching services, therefore we use an _alternate URL
syntax_ to load the images from Monocle.

Instead of using query parameters:

```html
 <img src='http://monocle.crowdtap.com/transform_image?src=http://images.crowdtap.com/images/monocle-original.png&resize=150'/>
```

Hence the route is reorganized using a series of `param/value` where values are URL encoded:

```html
 <img src='http://monocle.crowdtap.com/transform_image/q/src/http%3A%2F%2Fimages.crowdtap.com%2Fimages%2Fmonocle-original.png/resize/150'/>
```

Now the route will be recorded by the cache. The next time a visitor hits that
route it will be served by the cache directly, and the Monocle backend service
will not be called.

## Frontend Helper

For JS applications, we recommend using
[Enhance](https://github.com/crowdtap/enhance) to resize images on the fly using
Monocle and display high density pictures for Hi DPI screens when needed.

## Credits

Monocle is relying on a series of softwares to work.

- [ImageMagick](http://www.imagemagick.org/script/index.php), an excellent command line image processing tool.
- [Dragonfly](https://github.com/markevans/dragonfly) "A Ruby Rack-based gem for on-the-fly processing" (This is based on ImageMagick)
- [Magickly](http://magickly.jux.com/) Image manipulation as a (plugin-able) service (This is base on Dragonfly)

:+1: & Kudos to the people behind these projects.

## License - TBD
