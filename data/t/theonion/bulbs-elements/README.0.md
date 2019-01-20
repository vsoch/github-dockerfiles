# `<share-tools>`

Attributes
  * `share-url`  Used in all nested share tools. Default: `window.location.toString()`
  * `share-title` *(required)* sed in all nested share tools.

#### `<share-via-*>`

All elements that named `<share-via-*>` take an `icon` and `label` attribute.

Attributes
  * `icon` Render an icon for the share tool.
  * `label` Render a label for the share tool.

#### `<share-via-facebook>`
  * _No attributes_

#### `<share-via-twitter>`

Attributes
  * `twitter-handle` *(required)* Used to construct the tweet share message.

#### `<share-via-email>`

Attributes
  * message (required)* Used to construct the email share message.

# Clicktracking

The `<share-via-*>` elements have a `data-track-label` attribute set (Facebook, Twitter, Email). Set `data-track-action` and `data-track-category` somewhere above them and clicktracking will be your reward.

# Example:

```html
<share-tools
  share-title="Share This!"
  share-url="//example.org/share-me"
  data-track-category="Super Cool Category"
  data-track-action="Share"
>
  <share-via-facebook icon label></share-via-facebook>
  <share-via-twitter icon label twitter-handle="theonion"></share-via-twitter>
  <share-via-email icon label message="via theonion.com"></share-via-email>
</share-tools>
```

Campaign Display
================

The `campaign-display` renders campaign sponsorship information for a given campaign.  Given a valid campaign URL, `campaign-display` will render the campaign information including the sponsor name, sponsor logo and premable text. You know, this thing:

![](https://raw.githubusercontent.com/theonion/bulbs-elements/master/examples/fixtures/campaign-display/campaign-display-example.png)


Examples:
---------

### Default campaign-display

```html
<campaign-display
  placement="my-custom-placement"
  src="http://localhost:8080/fixtures/campaign-display/campaign.json"
  preamble-text="Presented by"></campaign-display>
```
will produce:

```html
<div class="campaign-display" data-label="http://example.com">
  <div data-ad-unit="campaign-pixel" data-targeting="{"dfp_placement":"my-custom-placement"}"></div>
  <div class="campaign-display-logo">
    <a href="http://example.com">
      <div data-type="image" data-image-id="1234" data-crop="original">
        <div></div>
      </div>
    </a>
  </div>
  <span class="campaign-display-preamble">Presented by</span>
  <span class="campaign-display-sponsor-name">
    <a href="http://example.com">
      <span>Example Campaign</span>
    </a>
  </span>
</div>
```

### No logo

```html
<campaign-display
  placement="my-custom-placement"
  src="http://localhost:8080/fixtures/campaign-display/campaign.json"
  preamble-text="Sponsored by"
  name-only></campaign-display>
```

will produce: 

```html
<div class="campaign-display" data-label="http://example.com">
  <div data-ad-unit="campaign-pixel" data-targeting="{"dfp_placement": "my-custom-placement"}"></div>
  <span class="campaign-display-preamble">Sponsored by</span>
  <span class="campaign-display-sponsor-name">
    <a href="http://example.com">
      <span>Example Campaign</span>
    </a>
  </span>
</div>
```

### No Pixel

```html
<campaign-display
  placement="my-custom-placement"
  src="http://localhost:8080/fixtures/campaign-display/campaign.json"
  preamble-text="Sponsored by"
  no-pixel></campaign-display>
```

will produce: 

```html
<div class="campaign-display" data-label="http://example.com">
  <span class="campaign-display-preamble">Sponsored by</span>
  <span class="campaign-display-sponsor-name">
    <a href="http://example.com">
      <span>Example Campaign</span>
    </a>
  </span>
</div>
```

### Logo only

```html
<campaign-display
  placement="my-custom-placement"
  src="http://localhost:8080/fixtures/campaign-display/campaign.json"
  preamble-text="Sponsored by"
  image-only></campaign-display>
```

will produce: 

```html
<div class="campaign-display" data-label="http://example.com">
  <div data-ad-unit="campaign-pixel" data-targeting="{"dfp_placement": "my-custom-placement"}"></div>
  <div class="campaign-display-logo">
    <a href="http://example.com">
      <div data-type="image" data-image-id="1234" data-crop="original">
        <div></div>
      </div>
    </a>
  </div>
  <span class="campaign-display-preamble">Sponsored by</span>
  <span class="campaign-display-sponsor-name">
    <a href="http://example.com">
      <span>Example Campaign</span>
    </a>
  </span>
</div>
```
Usage

with src attr:
```html
<video src="/video.mp4" is="bulbs-cinemagraph" cinemagraph-duration="1.55"/>
```

with source element
```html
<video is="bulbs-cinemagraph" cinemagraph-duration="1.55">
  <source src="/video.mp4"/>
</video>
```
Duration needs to be figured out and set by hand to prevent the ios polyfill from showing a frame of black at the loop seam.
# `<bulbs-ellipsize>`

Attributes
  * `line-count`  number of lines you want your string to be

# Example:

```html
<bulbs-ellipsize line-count="3">
  Example text
</bulbs-ellipsize>
```

# `<bulbs-pinned-element>`

Wrapper that moves content inside a car in a vertical rail relative to the window. Rail takes the height and width of its parent container.

## Attributes

* `offset-top-px` *(optional)* offset in pixels to adjust measurements by. For example, if you have a sticky header, use this to allow the car to stick in the window below the fixed header.

## Example

```html
<parent-element class="foobar">
  <bulbs-pinned-element pinned-to=".foobar">
  </bulbs-pinned-element>
</parent-element>
```
# `<lazy-iframe>`

This operates just like an `<iframe>`, except it will not create an actual `<iframe>`
DOM node until the `<lazy-iframe>` is within `200px` of the viewport boundary.

It takes all attributes a normal `<iframe>` would take.

# bulbs-article-body

Provides some basic functionality every article body element needs. The element this is applied to must be a div.

Example usage:

```
<div is="bulbs-article-body">
  <!-- your article body content -->
</div>
```

## Dingbats
A span will be added to the last element in the article body with a class `site-dingbat`. The span will initially be empty, so style the `site-dingbat` class to customize it and get it to show up.

## iframe Resizing
All elements matching `iframe.onionstudios-playlist` will be registered with [iFrameResize](https://github.com/davidjbradshaw/iframe-resizer).
# `<bulbs-video>`

This element has many related elements. It is up to question whether they should
hoisted up to top-level directories under 'elements/', or left where they are
in `elements/bulbs-video/elements`

There are three stand-alone elements:

* `<bulbs-video>`
* `<bulbs-video-meta>`
* `<bulbs-video-summary>`

These elements all require a `src` attribute that points at the videohub
video json detail endpoint: `//www.onionstudios.com/video/1234.json`.
(Other endpoints may return the same data structure and are valid.)

And five elements in the `<bulbs-video-carousel>` family. These could likely
be extracted into a more generic carousel element, but for now they have been
built specifically to the requirements of the video carousel.

* `<bulbs-video-carousel>`
* `<bulbs-video-carousel-slider>`
* `<bulbs-video-carousel-item>`
* `<bulbs-video-carousel-previous>`
* `<bulbs-video-carousel-next>`

All the `<bulbs-video-carousel-*>` elements MUST be a child of a
`<bulb-video-carousel>` element.

`-carousel-item>` elements MUST be a child of a `-carousel-slider>` element.

`-previous>` and `-next>` elements may be placed anywhere within the
`<bulbs-video-carousel>`. element

`-carousel-item>` takes an `href` attribute. This is used to manage initial state,
such as paging to the correct item on page load. It also makes the element
behave like a link.

An example implementation:

```html
<bulbs-video-carousel class="fancy-video-carousel">
  <header>
    <h1> Fancy Video Carousel </h1>
    <a href="//example.org">Leave the Fancy Video Carousel</a>
  </header>

  <div>
    <bulbs-video src="//videohub/1234.json"></bulbs-video>
    <bulb-video-meta src="//videohub/1234.json"></bulbs-video>
    <button class="fancy-fun"> Fancy Button Just For Fun </button>
  </div>

  <bulb-video-carousel-slider>
    <bulbs-video-carousel-item href="//example.org/carousel/1">
      <bulbs-video-summary src="//videohub/1235.json"></bulbs-video-summary>
    </bulbs-video-carousel-item>

    <bulbs-video-carousel-item href="//example.org/carousel/2">
      <bulbs-video-summary src="//videohub/1236.json"></bulbs-video-summary>
    </bulbs-video-carousel-item>

    <bulbs-video-carousel-item href="//example.org/carousel/3>
      <bulbs-video-summary src="//videohub/1237.json"></bulbs-video-summary>
    </bulbs-video-carousel-item
  </bulb-video-carousel-slider>

  <footer>
    <bulbs-video-carousel-previous></bulbs-video-carousel-previous>
    <bulbs-video-carousel-next></bulbs-video-carousel-next>
  </footer>
</bulbs-video-carousel>
```
