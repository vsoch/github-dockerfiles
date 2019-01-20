# This is a build system for [CredibilityCoalition.org](https://credibilitycoalition.org)

This is an environment for fast, synchronized browser refreshing as you edit Sass, HTML and JavaScript.

## Quick start

0. Install `npm` and `node` (eg via the Node installer or on a Mac using `brew install node`)
0. Install Ruby 2.x (eg with [rvm](https://rvm.io))
0. `npm i && npm run build` to build the site
0. `npm run test` to run the tests
0. `npm start` to serve the site at [http://localhost:4567](http://localhost:4567)
0. Edit .scss, .html and .js files. The browser should live-reload.

## This is a [Middleman](http://middlemanapp.com/) site

[Middleman](http://middlemanapp.com/) compiles our static site `build` from files in `source`.

Middleman is a Ruby and Markdown templating & routing system. When you work with Middleman you are generating a static site that is generated in a `build` directory, but you only see the `source` files while you are working. When you are ready to make the static build of all your pages with all your templating logic re-run, you do `middleman build` and commit the build directory — in Meedan’s case, the build system does it for you so you don't need to build before you deploy.

The build directory is ignored and rebuilt by the deployment process.

## Local development

*:warning: Don't edit the files in `./build` :) *

To work on the HTML and Sass, edit the files in `./source`. `npm start` will start the Middleman compiler for both the stylesheets ([Sass](sass-lang.com/)) and the HTML.

Middleman runs with livereload and should refresh the page automatically when you make changes.

Note: It does not do a full `build` on every save. It only live-updates files that have already been built. So if you make changes to a config file, or add new files you will likely need to run `middleman build`.

## Adding a new partner logo

- Use an svg file if possible, and optimize it with [svgo](https://github.com/svg/svgo).
- For jpg or png files, create two versions, `@1x` (at least 100px) and `@2x` (at least 200px). Render both sizes (eg with [Sketch.app](https://www.sketchapp.com/ "Sketch - Professional Digital Design for Mac")) then do another pass on optimizing them. To optimize them you can do the best work with a bitmap program with good optimization settings ([Acorn](https://www.acorns.com/ "Acorns - Home")) or use the gulp task `gulp imagemin`. Check to make sure the file size is in the range of the other logos before committing a logo that is too big. The smaller size should be about 10k, the larger no more than 30k. Probably use a jpg for smallest file size. (Tip: If you're using Acorn or Photoshop, during the web export, try setting quality below 15%.)
- Add the name of the file to the partner json file as described below.

Once you have the new images, update the data files `supporter_logos.json` or `check_partners.json` to include data about the new file, for example:

```
{
  "name": "witness",
  "url": "https://witness.org/",
  "type": "png"
}
```

The template loops through these values to create the logo-list sections. So, this will add the images to the page.

## Adding a new team member

Hooray, a new Meedani! Like the logos, team member information is stored as JSON data. Take a peek in `data/team_members.json` and add a member (in alphabetical order) like so:

```
{
  "name": "meedani",
  "fullname": "Me Meedani",
  "title": "Senior Advisor"
}
```

Add a @1x version (200px, under 10kb) and a @2x version (400px, under 20kb) to `images/team/`.

## Adding a new page

- Create a `page__[pagename].scss` which imports the `shared` sass. That will ensure the basic CSS is in place for the page.
- Add markup to `source/localizable`
- Add copy to `locales/en.yml` (and other locales as appropriate)
- If you are adding it to the top level navigation: Add the page name to pages array in the `partials/_nav.erb` template and add the page name to the pages array in `source/stylesheets/nav.scss`. That will ensure it appears and is styled correctly when active.

## Releasing new versions

Use `npm version (major|minor|patch)` to tag a new version in the [SemVer](http://semver.org/) style.

Then push your new commits and the new release with: `git push && git push --tags`

## Sass structure

- Middleman compiles and Live-reloads the Sass for you.
- There are two files for each page: `shared.scss` and `page__[pagename].scss`. That `@imports` everything else. (We have separate sass files for each page to ensure that we send the fewest possible lines of CSS to each page.)
- Then we import our Sass components, pages, and utility files from `source/stylesheets`.
- We use Sass formatting guideliness that are captured in a `.stylelintrc` file — you can use a stylelint linter in your editor of choice by following instructions on the [Stylelint website](https://stylelint.io/)

Note: we are serving the site with [HTTP/2](https://http2.github.io/ "HTTP/2") so we no longer use image sprites, and we don't bundle all our CSS into a single file.


## Travis

Tests are run automatically when you push to github, using [Travis](https://travis-ci.org/ "Travis CI - Test and Deploy Your Code with Confidence").