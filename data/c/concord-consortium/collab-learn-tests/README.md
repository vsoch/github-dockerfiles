# CLUE Cypress tests
## Setup and configuration
Install NPM packages and Cypress
```
npm install
```

## Running tests

- `npm run test:local`
- `npm run test:dev`
- `npm run test:branch` (requires change in environments.json to add the branch name)
- `npm run test:master`
- `npm run test:production`

## Additional notes about configuration

You can also temporarily overwrite any configuration option using env variables with `CYPRESS_` prefix. E.g.:
- `CYPRESS_baseUrl=https://collaborative-learning.concord.org/branch/fix-data-attributes npm run test:dev`

## Writing tests, workflow and patterns

1. Tests should not depend on other tests.
2. Take a look at `cypress/support/commands.js`. This file implements LARA-specific helpers that will make test 
implementation simpler. Existing commands at the moment:

    - setupGroup
    - upLoadFile
    - clearQAData
