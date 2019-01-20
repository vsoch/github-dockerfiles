# Features

The features folder is for code that logically belongs together, but is included in multiple places in the app. An example of this is Feedback, which affects the Classifier and the Project Builder.
# Feedback

## Architecture

- `lab` - Containers and components related to setting feedback settings in the Project Builder.
- `classifer` - Containers and components for the feedback modal in the classifier.
- `shared` - Shared code used by both the project builder and the classifier.
  - `strategies` - the different methods for reconciling subject metadata and the workflow-defined rules. Each exports the code for both the lab and classifier, keeping all related code in the same place.

## How to set up feedback on a project

**Requires the general feedback experimental option to be enabled.**

### Workflow

1. In the project builder, navigate to your workflow, and find the feedback section in the bottom right.
1. Start creating a new rule by clicking the button.
1. Define a unique id for the rule, check the boxes for whether you want feedback to be shown on success, failure or both. Where enabled, a default message must be defined.
1. Select a strategy for your rule. See the Strategies section below for more information.
1. Define any additional options required by the chosen strategy, and save the new rule.

### Subjects

1. Assemble your images, and create a `manifest.csv` file.
1. For each subject where you want a feedback rule enabled, add the following columns:

  - `#feedback_N_id` **(required)** - corresponds to the desired rule ID you created in the workflow.
  - `#feedback_N_successMessage` (optional) - a success message specific to this subject that overrides the default success message set on the workflow.
  - `#feedback_N_failureMessage` (optional) - a failure message specific to this subject that overrides the default failure message set on the workflow.

  `N` must be an integer. This lets you define multiple rules on one subject.

## Strategies

A strategy is the method for reconciling a user's annotations and the known data defined on the subject. The following strategies are available:

### Radial

Uses the point tool. Determines whether any points lie within a defined tolerance of a point defined on the subject metadata.

#### Additional workflow options

- **Default tolerance** - a default tolerance value around the point defined on the subject.

#### Additional Subject metadata fields

- `#feedback_N_x` **(required)** - the X coordinate for the known point.
- `#feedback_N_y` **(required)** - the Y coordinate for the known point.
- `#feedback_N_tolerance` (optional) - the radius around the known point for a valid annotation. Defaults the the value defined on the workflow if not set.

### Dud

Determines whether there should be any annotations or not. There are no additional workflow options or subject fields required.
## Strategies

A strategy tells the feedback processor how to define, validate, and process a set of feedback rules. For example, the `radial` strategy is used to determine whether a point annotation is within a given radius or not.

### API

A feedback strategy **must** export the following:

- `createRule` [function] - a function that accepts `subjectRule` and  `workflowRule` as an argument, and merges them to create a canonical representation of the rule.
- `id` [string] - a unique string identifying the strategy.
- `reducer` [function] - a function that accepts a canonical `rule` and `annotations`, and reduces them to a rule with a new property, `success` (boolean). It should also include any successful annotations as an array.
- `title` [string] - the human-readable name of the strategy, used in the Project Builder.

Optionally, it can also export:

- `labComponent` - a form component used to configure additional default options in the Project Builder.
- `validations` [array] - an array of functions, each of which accept the feedback definition as an argument, and which return a boolean. Define this if you're going to add extra default options using `labComponent`.

### Caveats

- The `reducer` function needs to be passed the rule it's checking, and the _entire_ annotation object for that task. This allows the `dud` strategy to check there are no annotations, without having to write a separate API for it.
# Feedback Strategy: Dud

Determines whether an annotation is empty or not.

## Subject metadata fields

A single subject can have multiple feedback rules. To group the metadata fields for a single feedback rule together, `N` should be an integer that is identical for each rule, e.g.:

```
#feedback_1_id,,#feedback_2_id...
```

- `#feedback_N_id` (**required**) - ID of the corresponding workflow task rule.
- `#feedback_N_successMessage` (optional) - message to show when the target is correctly annotated. Overrides the default success message set on the workflow task rule.
- `#feedback_N_failureMessage` (optional) - message to show when the target is incorrectly annotated. Overrides the default failure message set on the workflow task rule.
# Feedback Strategy: Column

Determines whether a column is within a given tolerance.

## Subject metadata fields

- `#feedback_N_id` (**required**) - ID of the corresponding workflow task rule.
- `#feedback_N_x` (**required**) - x value of the target column.
- `#feedback_N_width` (**required**) - width value of the target column.
- `#feedback_N_tolerance` (optional) - Margin of error around the target column. Overrides the default tolerance set on the workflow task rule.
- `#feedback_N_successMessage` (optional) - message to show when the target is correctly annotated. Overrides the default success message set on the workflow task rule.
- `#feedback_N_failureMessage` (optional) - message to show when the target is incorrectly annotated. Overrides the default failure message set on the workflow task rule.
# Feedback Strategy: Radial

Determines whether a point is within a given tolerance.

## Subject metadata fields

A single subject can have multiple feedback rules. To group the metadata fields for a single feedback rule together, `N` should be an integer that is identical for each rule, e.g.:

```
#feedback_1_id,#feedback_1_x,#feedback_1_y,#feedback_2_id,#feedback_2_x,#feedback_2_y...
```

- `#feedback_N_id` (**required**) - ID of the corresponding workflow task rule.
- `#feedback_N_x` (**required**) - x value of the target circle.
- `#feedback_N_y` (**required**) - y value of the target circle.
- `#feedback_N_tolerance` (optional) - radius of the target circle. Overrides the default tolerance set on the workflow task rule.
- `#feedback_N_successMessage` (optional) - message to show when the target is correctly annotated. Overrides the default success message set on the workflow task rule.
- `#feedback_N_failureMessage` (optional) - message to show when the target is incorrectly annotated. Overrides the default failure message set on the workflow task rule.
# Feedback Strategy: Single Answer Question

Determines whether the user has correctly answered a question with a single answer, or no answer.

## Subject metadata fields

A single subject can have multiple feedback rules. To group the metadata fields for a single feedback rule together, `N` should be an integer that is identical for each rule, e.g.:

```
#feedback_1_id,#feedback_1_answer,#feedback_2_id,#feedback_2_answer...
```

- `#feedback_N_id` (**required**) - ID of the corresponding workflow task rule.
- `#feedback_N_answer` (**required**) - index of the correct answer for the corresponding workflow task. Like the answers, this should be zero-indexed, so if the first answer is the correct one, this value should be `0`; if the second answer, `1`, and so on. Setting this to `-1` means there should be no answer, if an answer isn't required.
- `#feedback_N_successMessage` (optional) - message to show when the target is correctly annotated. Overrides the default success message set on the workflow task rule.
- `#feedback_N_failureMessage` (optional) - message to show when the target is incorrectly annotated. Overrides the default failure message set on the workflow task rule.
# Ducks: Redux Reducer Bundles

via https://github.com/erikras/ducks-modular-redux

I find as I am building my redux app, one piece of functionality at a time, I keep needing to add  `{actionTypes, actions, reducer}` tuples for each use case. I have been keeping these in separate files and even separate folders, however 95% of the time, it's only one reducer/actions pair that ever needs their associated actions.

To me, it makes more sense for these pieces to be bundled together in an isolated module that is self contained, and can even be packaged easily into a library.

## The Proposal

### Example

See also: [Common JS Example](CommonJs.md).

```javascript
// widgets.js

// Actions
const LOAD   = 'my-app/widgets/LOAD';
const CREATE = 'my-app/widgets/CREATE';
const UPDATE = 'my-app/widgets/UPDATE';
const REMOVE = 'my-app/widgets/REMOVE';

// Reducer
export default function reducer(state = {}, action = {}) {
  switch (action.type) {
    // do reducer stuff
    default: return state;
  }
}

// Action Creators
export function loadWidgets() {
  return { type: LOAD };
}

export function createWidget(widget) {
  return { type: CREATE, widget };
}

export function updateWidget(widget) {
  return { type: UPDATE, widget };
}

export function removeWidget(widget) {
  return { type: REMOVE, widget };
}
```
### Rules

A module...

1. MUST `export default` a function called `reducer()`
2. MUST `export` its action creators as functions
3. MUST have action types in the form `npm-module-or-app/reducer/ACTION_TYPE`
3. MAY export its action types as `UPPER_SNAKE_CASE`, if an external reducer needs to listen for them, or if it is a published reusable library

These same guidelines are recommended for `{actionType, action, reducer}` bundles that are shared as reusable Redux libraries.

### Name

Java has jars and beans. Ruby has gems. I suggest we call these reducer bundles "ducks", as in the last syllable of "redux".

### Usage

You can still do:

```javascript
import { combineReducers } from 'redux';
import * as reducers from './ducks/index';

const rootReducer = combineReducers(reducers);
export default rootReducer;
```

You can still do:

```javascript
import * as widgetActions from './ducks/widgets';
```
...and it will only import the action creators, ready to be passed to `bindActionCreators()`.

There will be some times when you want to `export` something other than an action creator. That's okay, too. The rules don't say that you can *only* `export` action creators. When that happens, you'll just have to enumerate the action creators that you want. Not a big deal.

```javascript
import {loadWidgets, createWidget, updateWidget, removeWidget} from './ducks/widgets';
// ...
bindActionCreators({loadWidgets, createWidget, updateWidget, removeWidget}, dispatch);
```

### Example

[React Redux Universal Hot Example](https://github.com/erikras/react-redux-universal-hot-example) uses ducks. See [`/src/redux/modules`](https://github.com/erikras/react-redux-universal-hot-example/tree/master/src/redux/modules).

[Todomvc using ducks.](https://github.com/goopscoop/ga-react-tutorial/tree/6-reduxActionsAndReducers)

### Implementation

The migration to this code structure was [painless](https://github.com/erikras/react-redux-universal-hot-example/commit/3fdf194683abb7c40f3cb7969fd1f8aa6a4f9c57), and I foresee it reducing much future development misery.

Please submit any feedback via an issue or a tweet to [@erikras](https://twitter.com/erikras). It will be much appreciated.

Happy coding!

-- Erik Rasmussen

---

![C'mon! Let's migrate all our reducers!](migrate.jpg)
> Photo credit to [Airwolfhound](https://www.flickr.com/photos/24874528@N04/3453886876/).
