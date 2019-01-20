# attachHoverState

A function that replicates the `:hover` event and stores it in the `state`.

## Usage

```
const style = {
  base: {},
  hover: {},
};

getInitialState() {
  return {
    hover: false
  };
}

getStyle() {
  return Object.assign(
    {},
    style.base,
    this.state.hover ? style.hover : null
  );
}

<Component {...attachHoverState(this)} style={this.getStyle()} />
```

# Tray

A component that is pinned to either the left or the right of its parent with 100% height.

## Usage

```
<Tray>
  <Tray.Group>
    <Tray.Item />
  </Tray.Group>
</Tray>
```

## Properties

### Tray

#### `fixed`

_Optional_. Sets the `position` to be `fixed` instead of `absolute`. Options are;

* Not supplied: `false`
* `true` or `false`

#### `align`

_Optional_. Positions the `Tray` on the left or the right. Options are;

* Not supplied: `Tray.align.LEFT`
* `Tray.align.LEFT` or `Tray.align.RIGHT`

### Tray.Group

#### `title`

_Optional_. Title of the group. Options are;

* Not supplied: `null`,
* Any `string`

### Tray.Item

None.

### Any direct child

Any direct decendant of `Tray`, regardless of the type (`Tray.Group`, `div`, `Bar`).

#### `sticky`

_Optional_. `Tray` will group all `sticky` children, calculate the height, and then set an explcit height for both the `sticky` and `non-sticky` children. Useful if you need to scroll a `Tray-Group`.# Link

A wrapper around React.DOM.A, with a few common traits.
Often used for create actions.

## Usage

```
<Link>Click Me!</Link>
<Link small>Click Me!</Link>
<Link fill>Click Me!</Link>
<Link fillCenter>Click Me!</Link>

```

## Properties

### `small`

Slightly smaller link.

### `route`

The element should be `Router.Link` instead of a standard `a`.

### `fill`

Block style filling its container.

### `fillCenter`

Block style filling its container and centered.

### More

See the react documentation for more information. [http://facebook.github.io/react/docs/]
# Lightbox

Viewer for groups of images and documents. Includes rendering methods for images, and an iframe rendering method suitable for PDF and HTML documents.

## Usage

```
<Lightbox
  fullscreen={false}
  hide={false}
  initialIndex={0}
  onChange={function() {/* The shown asset has changed */}}
  style={{outline: '1px solid pink'}}
  assets={assets}
/>
```

## Properties

### `fullscreen`

Boolean property, whether to display the lightbox as "fullscreen" (i.e. absolutely positioned at 0 on every side).

_**Note**: The Lightbox will make no effort to break out of a container constricting it, so `fullscreen` can actually be used to just make it take up the size of its parent._

### `hide`

Boolean property, if `true`, the lightbox will not be displayed.

### `initialIndex`

Index of asset to display on first render.

### `onChange`

Function called when the shown asset is changed.

### `onClose`

Function, if supplied, a "close" button will be shown in the Lightbox toolbar, which will call this function when clicked.

### `style`

React style object, which will be assigned to the `.Lightbox` element.

### `prependMenuItems` and `appendMenuItems`

Arrays of renderable things ("nodes" in React terms) that get, surprisingly,
prepended or appended to the existing items in the menu.

### `assets`

Array of assets to render in the Lightbox. They should be objects with the following properties;

* `media`, the MIME type of the asset.
* `title`, the title or file name of the asset.
* `path`, the URL of the asset itself.
* `container`, a React class implementing a container for this asset (optional,
	negates the requirement for `media`).
* `element`, a React element to use directly instead of instantiating one
	internally (optional, negates the requirement for `media` and `path`).
# Pie Badge

A graph component to show the progress of some sort of process. Displays a checkmark when finished.

## Usage

```
<AvatarWithPie
  complete={4}
  total={9}
  backgroundColor="#21323a"
  src="http://www.gravatar.com/avatar/82dccacb221d0a037aa2b60f3cf94d5d?s=50"
  firstName="Nathan"
  lastName="Hutchison"
  size={Avatar.sizes.l}
/>
```

## Properties

### `complete`

The number of items completed. Should be less than or equal to `total`.

### `total`

The total number of items to complete. Must be greater than or equal to `complete`.

### `backgroundColor`

A CSS colour to display around the pie badge. This lets it fake transparency.
# Card

A card looking component.


## Usage

```
<Card
  title="Card title"
/>
```

## Properties

#### `title`

_Optional_. Card title. Options are;

* Any string

#### `indicatorColor`

_Optional_. Color of the stripe on the card. Options are;

* Not supplied: hidden
* Any color value

# LinkGroup

An element to contain `Link` components, which displays children in a group.

## Usage

```
<LinkGroup>
  <Link>Left</Link>
  <Link>Middle</Link>
  <Link>Right</Link>
</LinkGroup>
```

## `Link` Properties

### `route`

_Required_. Sets the `Link` component to use `Router.Link`.

### `query`

_Required_. Take a look [here](https://github.com/rackt/react-router/blob/master/examples/query-params/app.js).

### `default`

_Optional_. If no query is present, `default` will be the active link. This is useful if someone removes the `?query=` param from the url.
# Steps

UI control for showing completed and total steps of a process

## Usage

```
<Steps
  count={10}
  current={5}
/>
```

## Properties

### `count`

Total number of steps in the process.

### `current`

Number of completed steps. Should be less than or equal to `count`.
# DeleteButton

A red, circled cross rendered using the `close-filled` icon in SVG format.

## Usage

```
<DeleteButton />
```

## Properties

No custom properties apply.
# Navigation

A wrapper component with a logical api that glues `Bar` and `Tray`.

## Usage

```
<Navigation />
```

## Properties

#### `onTrayBlur`

_Optional_. Callback function for when a user wants to close the tray (clicking the `overlay` or the initiating icon). Options are;

* Not supplied: `function() {}`
* Any `function`

#### `barItems`

_Required_. `Array` of elements to show in the navigation bar. See [`Bar`](#Bar). Options are;

* `Array`

#### `showLeftTray` / `showRightTray`

_Optional_. Make the respective tray visible.

#### `rightTrayContent` / `leftTrayContent`

_Optional_. Groups of items. Options are;

* Not supplied: `[]`
* `Array`:
```javascript
[{
  title: 'group title',
  items: [
    <Item />,
    <Item />,
  ]
}]
```
* `title` is _optional_.

#### `scrollOffset`

_Optional_. The offset for `CovertHeader`. Options are;

* Not supplied: `0`
* Any integer
# Prompt

React-native replacement for JavaScript `prompt()`

## Usage

```
{this.state.showPrompt &&
  <Prompt
    onCancel={function() {/* Respond to "Cancel" */}}
    onOk={function() {/* Respond to "OK" */}}
    title="Sea shell census"
    cancelable={false}
    cancelText="Cancel"
    okText="OK"
    content="How many sea shells did you sell?"
    defaultValue="127"
    validateInput={function(value) {/* Return true if value is valid */}}
  />
}
```

## Properties

### `onCancel`

Function to call when the user cancels the prompt.

### `onOk`

Function to call when the user clicks "OK" in the prompt.

### `title`

Title to display in the prompt.

### `cancelable`

Whether the prompt shows the "Cancel" and close buttons, and responds to pressing Escape.

### `cancelText`

Text to display on the "Cancel" button. Defaults to "Cancel".

### `okText`

Text to display on the "OK" button. Defaults to "OK".

### `content`

Optional content to display above the prompt textbox.

### `defaultValue`

The default value for the prompt to show in the textbox.

### `validateInput`

Function which will be passed the entered value to determine if it can be accepted.
# Button

A wrapper around `React.DOM.button`, with a few common traits

## Usage

```
<Button success>Ok</Button>
<Button cancel>Cancel</Button>
<Button small>GO!</Button>
<Button danger>WARNING!</Button>
```

## Properties

### `small`

Slightly smaller button.

### `skeleton`

A button with no borders or background.

### `cancel`

A button used for cancelling edits and alert dialogs.

### `success`

A button used for confirmation.

### `danger`

A button used for potentially destructive actions (such as delete).

### More

Other properties are passed to the `button` element, information on supported attributes can be found [in the React docs](http://facebook.github.io/react/docs/tags-and-attributes.html#supported-attributes)
# Icon

A selection of SVG-based icons

## Usage

```
<Icon
  type="user-female"
  component={React.createFactory('span')}
/>
```

## Properties

### `type`

The type of icon. Available types are;

* `action-redo`
* `action-undo`
* `add`
* `addressbook`
* `anchor`
* `arrow-down`
* `arrow-left`
* `arrow-right`
* `arrow-up`
* `badge`
* `bag`
* `ban`
* `bar-chart`
* `basket`
* `basket-loaded`
* `bell`
* `book-open`
* `briefcase`
* `bubble`
* `bubbles`
* `bug-pin`
* `bulb`
* `calculator`
* `calendar`
* `call-end`
* `call-in`
* `call-out`
* `camcorder`
* `camera`
* `check`
* `chemistry`
* `clock`
* `close`
* `close-filled`
* `cloud-download`
* `cloud-upload`
* `compass`
* `control-end`
* `control-forward`
* `control-pause`
* `control-play`
* `control-rewind`
* `control-start`
* `credit-card`
* `crop`
* `cup`
* `cursor`
* `cursor-move`
* `desktop`
* `diamond`
* `direction`
* `directions`
* `disc`
* `dislike`
* `doc`
* `docs`
* `drawer`
* `drop`
* `earphones`
* `earphones-alt`
* `emoticon-smile`
* `energy`
* `envelope`
* `envelope-letter`
* `envelope-open`
* `equalizer`
* `eye`
* `eyeglasses`
* `feed`
* `film`
* `fire`
* `flag`
* `folder`
* `folder-filled`
* `folder-alt`
* `frame`
* `game-controller`
* `ghost`
* `globe`
* `globe-alt`
* `graduation`
* `graph`
* `grid`
* `handbag`
* `heart`
* `heart-filled`
* `home`
* `hourglass`
* `info`
* `key`
* `layers`
* `like`
* `link`
* `list`
* `lock`
* `lock-open`
* `login`
* `logout`
* `loop`
* `magic-wand`
* `magnet`
* `magnifier`
* `magnifier-add`
* `magnifier-remove`
* `map`
* `microphone`
* `mouse`
* `moustache`
* `music-tone`
* `music-tone-alt`
* `nav-down`
* `nav-left`
* `nav-right`
* `nav-up`
* `note`
* `notebook`
* `paper-clip`
* `paper-plane`
* `pencil`
* `phone-vertical`
* `picture`
* `pie-chart`
* `pin`
* `plane`
* `playlist`
* `plus`
* `pointer`
* `power`
* `present`
* `printer`
* `puzzle`
* `question`
* `refresh`
* `reload`
* `rocket`
* `screen-desktop`
* `screen-smartphone`
* `screen-tablet`
* `settings`
* `settings-filled`
* `share`
* `share-alt`
* `shield`
* `shuffle`
* `size-actual`
* `size-fullscreen`
* `social-dribbble`
* `social-dropbox`
* `social-facebook`
* `social-tumblr`
* `social-twitter`
* `social-youtube`
* `sort`
* `sort-disabled`
* `sort-down`
* `sort-up`
* `speech`
* `speedometer`
* `star`
* `star-filled`
* `support`
* `symbol-female`
* `symbol-male`
* `tag`
* `target`
* `trash`
* `trophy`
* `umbrella`
* `user`
* `user-filled`
* `user-female`
* `user-follow`
* `user-follow-filled`
* `user-following`
* `user-unfollow`
* `users`
* `users-filled`
* `vector`
* `volume-1`
* `volume-1-filled`
* `volume-2`
* `volume-2-filled`
* `volume-off`
* `volume-off-filled`
* `wallet`
* `wrench`

### `component`

Optional. The type of element, or React component, to render the icon inside.
# Scroll Event Mixin

React component mixin for detecting when the page is scrolled.

## Usage

```javascript
React.createClass({
  mixins: [ScrollEventMixin({
    interval: 100,
    timeout: 300
  })],

  onScrollStart() {
    /* Scrolling has started */
  },

  onScrollEnd() {
    /* Scrolling has ended */
  }
});
```

## Properties

### `interval`

How often to update the scrolling status, in milliseconds. Defaults to 100.

### `timeout`

Time to wait before declaring scrolling to have ended, in milliseconds. Defaults to 200.
# DateFormatter

Utilities for formatting dates, used across [Macropod](https://macropod.com) products for consistent dates.

## Usage

```
let formattedDate = DateFormatter.dateTime(new Date());
```

## Methods

All methods accept at least one parameter, `date`, which is the Date string or object from which to derive the time.

### `date`

Standardised formatting for a date only.

### `dateTime`

Standardised formatting for a date with time.

### `time`

Standardised formatting for a time only.

### `custom` (deprecated)

Accepts a second parameter, `format`, which is a custom format string for rendering.
This string is passed to [Fecha](https://github.com/taylorhakes/fecha), whose spec for format strings is [available here](https://github.com/taylorhakes/fecha#formatting-tokens).

_**Note**: It is considered poor practice to use this method over calling Fecha's own format function directly in cases where you want a custom date format. The purpose of this utility is to keep it consistent, and this goes against that._
# Loading

A component to indicate loading progress.

## Usage

```
<Loading
  size="small"
/>
```

## Properties

### `size`

The size of loading icon to show. Options are;

* Not Supplied: "normal" size, 40px wide.
* `"medium"`: 29px wide.
* `"small"`: 16px wide.
# Avatar with Pie

A user `Avatar` which has an attached `PieBadge` component.

## Usage

```
<AvatarWithPie
  complete={4}
  total={9}
  backgroundColor="#21323a"
  src="http://www.gravatar.com/avatar/82dccacb221d0a037aa2b60f3cf94d5d?s=50&d=404"
  title="Nathan Hutchison"
  size={Avatar.sizes.l}
/>
```

## Properties

### `complete`

The number of items completed. Should be less than or equal to `total`.

### `total`

The total number of items to complete. Must be greater than or equal to `complete`.

### `backgroundColor`

A CSS colour to display around the pie badge. This lets it fake transparency.

### `size`

The size of the avatar to display; either `'s'` (20px), `'m'` (35px) or `'l'` (50px).

### `src`

The URL of this user's avatar.

_**Note**: If you are using Gravatars, you should use the appropriate size for the display (see `size` above for the appropriate sizes), multiplied by `window.devicePixelRatio` for high-resolution display support. You should also specify for the method for missing avatars for be 404 (`d=404`)._

### `circle`

Boolean property; if set, the avatar will be rendered in a circle.

### `title`

The full name of the user. Overrides the value of the `firstName` property if supplied.

### `firstName` (deprecated)

The first name of the user whose avatar this is.

### `lastName` (deprecated)

The last name of the user whose avatar this is.

### `email` (deprecated)

This user's email address. Will be used to determing the Gravatar URL if no `src` attribute is supplied.
# Bar

A component that acts a lot like a 'header'.

## Usage

```
<Bar>
  <div align={{Bar.align.left}} />
</Bar>
```


## Statics

### `align`

Defines which wrapper you want the child element inserted into (`left`, `center` or `right`):

```js
<Bar>
  <div align={{Bar.align.left}} />
</Bar>
```
# Alert

React-native replacement for JavaScript `alert()`

## Usage

```
{this.state.showAlert &&
  <Alert
    onCancel={function() {/* Respond to "Cancel" */}}
    onOk={function() {/* Respond to "OK" */}}
    title="This is the title of the Alert."
    cancelable={true}
    cancelText="Cancel"
    okText="OK"
    okDisabled={false}
    danger={false}
    >
    This is the content of the Alert.
  </Alert>
}
```

## Properties

### `onCancel`

Function to call when the user cancels the alert.

### `onOk`

Function to call when the user clicks "OK" in the alert.

### `title`

Title to display in the alert.

### `cancelable`

Whether the alert shows the "Cancel" and close buttons, and responds to pressing Escape.

### `cancelText`

Text to display on the "Cancel" button. Defaults to "Cancel".

### `okText`

Text to display on the "OK" button. Defaults to "OK".

### `okDisabled`

Whether the "OK" button should show up disabled.

### `danger`

Whether the "OK" button should show up as `<Button danger/>` indicating a destructive action.
# Markdown Snippet

A small component to display a snippet of markdown in a document.

## Usage

```
<MarkdownSnippet markdown="# Your markdown goes here" />
```

## Properties

### `markdown`

The unformatted markdown text to render

### `defaultStyles`

If set to false, doesn't apply the component's Markdown styles and relies on external or browser provided styles

### `linkTarget`

Allows setting the `target` attribute of generated Markdown links. Valid values are `"_self"`, `"_blank"`, `"_parent"` and `"_top"`.
# LinkPreservingQueryParameters

A React Router [Link](https://rackt.github.io/react-router/#Link) factory, producing instances of the Link which preserve the requested query parameters.

## Usage

```
const LinkWithinAuthContext = LinkPreservingQueryParametersFactory(['redirect_uri', 'product']);

<LinkWithinAuthContext to="register" />
```

## `LinkPreservingQueryParametersFactory` Parameters

### `queryParameters`

Array of query parameters to preserve in the generated link.

## Link API

The returned React object has the same API as React Router's [Link](https://rackt.github.io/react-router/#Link), with the exteption that the `query` prop will merge any object you supply with the preserved parameters.
# Avatar

A user avatar with three sizes, Gravatar and custom image URL support.

## Usage

```
<Avatar
  src="http://www.gravatar.com/avatar/82dccacb221d0a037aa2b60f3cf94d5d?s=50&d=404"
  title="Nathan Hutchison"
  size={Avatar.sizes.l}
/>
```

## Properties

### `size`

The size of the avatar to display; either `'s'` (20px), `'m'` (35px) or `'l'` (50px).

### `title`

The full name of the user. Overrides the value of the `firstName` property if supplied.

### `src`

The URL of this user's avatar.

_**Note**: If you are using Gravatars, you should use the appropriate size for the display (see `size` above for the appropriate sizes), multiplied by `window.devicePixelRatio` for high-resolution display support. You should also specify for the method for missing avatars for be 404 (`d=404`)._

### `circle`

Boolean property; if set, the avatar will be rendered in a circle.

### `firstName` (deprecated)

The first name of the user whose avatar this is.

### `lastName` (deprecated)

The last name of the user whose avatar this is.

### `email` (deprecated)

This user's email address. Will be used to determing the Gravatar URL if no `src` attribute is supplied.
# SuitClassSet

Class property formatter based on, and enforcing the [SUIT CSS naming conventions](https://github.com/suitcss/suit/blob/cb2adfea6ad26a2c6af9f2c1bc880e966854e709/doc/naming-conventions.md).

## Usage

```javascript
const elementClasses = new SuitClassSet('MyComponent');

elementClasses.addModifier('foo');

elementClasses.addState('bar');

elementClasses.addUtility('baz');

element.class = elementClasses.toString();
```

## Constructor

Creates a new SuitClassSet instance, and sets the component name, from which each class name will be derived.

## Methods

### `add` methods

Each of the `add` methods accepts and number of arguments, each in the following formats;

* A `string` representing a single class.
* An `Array`, with each item being a `string` representing a single class.
* A plain `Object`, whose enumerable keys represent a single class. If a key's associated value is falsy, the class will be excluded from output.

_**Note**: at present camel/snake case for each type of name is not required, but that may become the case in the future. Please follow the rules in the SUIT CSS naming conventions as closely as possible._

#### `addModifier`

Adds a [Modifier](https://github.com/suitcss/suit/blob/cb2adfea6ad26a2c6af9f2c1bc880e966854e709/doc/naming-conventions.md#componentname--modifiername) class to the set. For example, adding `'foo'` would add a class called `'MyComponent--foo'`.

#### `addState`

Adds a [State](https://github.com/suitcss/suit/blob/cb2adfea6ad26a2c6af9f2c1bc880e966854e709/doc/naming-conventions.md#componentnameis-stateofcomponent) class to the set. For example, adding `'bar'` would add a class called `'is-bar'`.

#### `addUtility`

Adds a [Utility](https://github.com/suitcss/suit/blob/cb2adfea6ad26a2c6af9f2c1bc880e966854e709/doc/naming-conventions.md#u-utilityname) class to the set. For example, adding `'baz'` would add a class called `'u-baz'`.

### `createDescendent`

Creates a new `SuitClassSet` instance for a [descendent](https://github.com/suitcss/suit/blob/cb2adfea6ad26a2c6af9f2c1bc880e966854e709/doc/naming-conventions.md#componentname-descendentname) of the current one.

Accepts one argument, which is the descendent name. For example, calling `createDescendent` with `bar` would create a new `SuitClassSet` instance whose base component name is `MyComponent-bar`.

### `toArray`

Generates an array of class name strings based on the current state of the set.

### `toString`

Returns all class names as one string, suitable for use in DOM `class`, or React `className` properties.
