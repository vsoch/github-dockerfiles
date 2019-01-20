# LARA Cypress tests

## Setup and configuration

First, install NPM packages and Cypress:

```
npm install
```

Then, you need to provide credentials of an admin user (=> user able to import and delete activities) for 
test environments that you are planning to use:

 - dev
 - staging
 - production
 
Note that these credentials must work on `/user/sign_in` page, e.g. http://authoring.staging.concord.org/users/sign_in. 
You **can't** use Portal to login (tests should not depend on Portal).

These credentials and any other user-specific configuration should be specified in `config/user-config.json`. 
Copy existing sample and modify it:

```
cp config/user-config.sample.json config/user-config.json
```

Also, If you are using dev environment, you might want to change local LARA URL depending on your docker 
setup. You might need to modify `baseUrl` option defined in `config/user-config.json` in the `dev` section.

Other environment properties (e.g. LARA URLs) are specified in `config/environments.json` file (e.g. LARA URLs).
This file should not be changed unless some new configuration is added. 

## Additional notes about configuration

You can also temporarily overwrite any configuration option using env variables with `CYPRESS_` prefix. E.g.:

- `CYPRESS_username=johndoe@test.email npm run test:dev`
- `CYPRESS_baseUrl=http://localhost:3000 npm run test:dev`

## Running tests

- `npm run test:dev`
- `npm run test:staging`
- `npm run test:production`

## Writing tests, workflow and patterns

1. Most of the tests will require some activity or sequence to exist. This test material should be stored in 
`cypres/fixtures` directory, as an exported JSON. That way it's possible to test one material in various environments.

    ```javascript
    context('Test example', function () {
      let activityUrl
      beforeEach(() => {
        cy.login()
        cy.importMaterial("activities/test-activity.json").then(url =>
          activityUrl = url
        )
      })
      afterEach(() => {
        cy.deleteMaterial(activityUrl)
      })
      
      it('some test case', () => {
        // ...
      })
    })
    ``` 

    Note that the activity should be always deleted in `afterEach`. This block is executed even 
    if the test fails.

2. Tests should not depend on other tests. In case of LARA, it means that every test should import and delete activity.
 Otherwise, if an activity is reused, it means that some run state is already present and that might affect the test
 execution. It's okay to test such behavior, but that should be probably just one, longer test. 

3. Use `[Cypress]` prefix for test activity and sequence names, as it's quite likely that some activities
won't get deleted in the process. It will be easy to clean them up. `importMaterial` command will fail if the material
is missing this prefix.

4. Take a look at `cypres/support/commands.js`. This file implements LARA-specific helpers that will make test 
implementation simpler. Existing commands at the moment:

    - login
    - logout
    - importMaterial
    - deleteMaterial
    - requestWithToken (CSRF)
    - visitActivityPage

Examples of tests following these recommendations:
- `cypress/integration/runtime/state-saving.js`
- `cypress/integration/runtime/multiple-choice-question.js`
- `cypress/integration/runtime/sequence-completed-activity.js`
