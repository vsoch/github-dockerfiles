<h1 align="center">
  <p align="center">Docusaurus</p>
  <a href="https://docusaurus.io"><img src="https://docusaurus.io/img/slash-introducing.svg" alt="Docusaurus"></a>
</h1>

<p align="center">
  <a href="https://www.npmjs.com/package/docusaurus"><a href="#backers" alt="sponsors on Open Collective"><img src="https://opencollective.com/Docusaurus/backers/badge.svg" /></a> <a href="#sponsors" alt="Sponsors on Open Collective"><img src="https://opencollective.com/Docusaurus/sponsors/badge.svg" /></a> <img src="https://img.shields.io/npm/v/docusaurus.svg?style=flat" alt="npm version"></a>
  <a href="https://circleci.com/gh/facebook/Docusaurus"><img src="https://circleci.com/gh/facebook/Docusaurus.svg?style=shield" alt="CircleCI Status"></a>
  <a href="CONTRIBUTING.md#pull-requests"><img src="https://img.shields.io/badge/PRs-welcome-brightgreen.svg" alt="PRs Welcome"></a>
  <a href="https://discord.gg/docusaurus"><img src="https://img.shields.io/badge/chat-on%20discord-7289da.svg" alt="Chat"></a>
  <a href="https://github.com/prettier/prettier"><img alt="code style: prettier" src="https://img.shields.io/badge/code_style-prettier-ff69b4.svg?style=flat-square"></a>
  <a href="https://github.com/facebook/jest"><img src="https://img.shields.io/badge/tested_with-jest-99424f.svg" alt="Tested with Jest"></a>
</p>

## Introduction

Docusaurus is a project for easily building, deploying, and maintaining open source project websites.

- **Simple to Start** Docusaurus is built to be easy to [get up and running](https://docusaurus.io/docs/en/installation.html) in as little time possible. We've built Docusaurus to handle the website build process so you can focus on your project.
- **Localizable** Docusaurus ships with [localization support](https://docusaurus.io/docs/en/translation.html) via CrowdIn. Empower and grow your international community by translating your documentation.
- **Customizable** While Docusaurus ships with the key pages and sections you need to get started, including a home page, a docs section, a [blog](https://docusaurus.io/docs/en/blog.html), and additional support pages, it is also [customizable](https://docusaurus.io/docs/en/custom-pages.html) as well to ensure you have a site that is [uniquely yours](https://docusaurus.io/docs/en/api-pages.html).

## Installation

Docusaurus is available as the [`docusaurus` package](https://www.npmjs.com/package/docusaurus) on [npm](https://www.npmjs.com).

We have also released the [`docusaurus-init` package](https://www.npmjs.com/package/docusaurus-init) to make [getting started](https://docusaurus.io/docs/en/installation.html) with Docusaurus even easier.

## Contact

We have a few channels for contact:

- [Discord](https://discord.gg/docusaurus) with two text channels:
  - `#docusaurus-users` for those using Docusaurus.
  - `#docusaurus-dev` for those wanting to contribute to the Docusaurus core.
- [@docusaurus](https://twitter.com/docusaurus) on Twitter
- [GitHub Issues](https://github.com/facebook/docusaurus/issues)

## Contributors

This project exists thanks to all the people who contribute. [[Contribute](CONTRIBUTING.md)]. <a href="https://github.com/facebook/Docusaurus/graphs/contributors"><img src="https://opencollective.com/Docusaurus/contributors.svg?width=890&button=false" /></a>

## Backers

Thank you to all our backers! 🙏 [[Become a backer](https://opencollective.com/Docusaurus#backer)]

<a href="https://opencollective.com/Docusaurus#backers" target="_blank"><img src="https://opencollective.com/Docusaurus/backers.svg?width=890"></a>

## Sponsors

Support this project by becoming a sponsor. Your logo will show up here with a link to your website. [[Become a sponsor](https://opencollective.com/Docusaurus#sponsor)]

<a href="https://opencollective.com/Docusaurus/sponsor/0/website" target="_blank"><img src="https://opencollective.com/Docusaurus/sponsor/0/avatar.svg"></a> <a href="https://opencollective.com/Docusaurus/sponsor/1/website" target="_blank"><img src="https://opencollective.com/Docusaurus/sponsor/1/avatar.svg"></a>

## License

Docusaurus is [MIT licensed](./LICENSE).

The Docusaurus documentation (e.g., `.md` files in the `/docs` folder) is [Creative Commons licensed](./LICENSE-docs).
This website was created with [Docusaurus](https://docusaurus.io/).

# What's In This Document

* [Get Started in 5 Minutes](#get-started-in-5-minutes)
* [Directory Structure](#directory-structure)
* [Editing Content](#editing-content)
* [Adding Content](#adding-content)
* [Full Documentation](#full-documentation)

# Get Started in 5 Minutes

1. Make sure all the dependencies for the website are installed:

```sh
# Install dependencies
$ yarn
```
2. Run your dev server:

```sh
# Start the site
$ yarn start
```

## Directory Structure

Your project file structure should look something like this

```
my-docusaurus/
  docs/
    doc-1.md
    doc-2.md
    doc-3.md
  website/
    blog/
      2016-3-11-oldest-post.md
      2017-10-24-newest-post.md
    core/
    node_modules/
    pages/
    static/
      css/
      img/
    package.json
    sidebar.json
    siteConfig.js
```

# Editing Content

## Editing an existing docs page

Edit docs by navigating to `docs/` and editing the corresponding document:

`docs/doc-to-be-edited.md`

```markdown
---
id: page-needs-edit
title: This Doc Needs To Be Edited
---

Edit me...
```

For more information about docs, click [here](https://docusaurus.io/docs/en/navigation)

## Editing an existing blog post

Edit blog posts by navigating to `website/blog` and editing the corresponding post:

`website/blog/post-to-be-edited.md`
```markdown
---
id: post-needs-edit
title: This Blog Post Needs To Be Edited
---

Edit me...
```

For more information about blog posts, click [here](https://docusaurus.io/docs/en/adding-blog)

# Adding Content

## Adding a new docs page to an existing sidebar

1. Create the doc as a new markdown file in `/docs`, example `docs/newly-created-doc.md`:

```md
---
id: newly-created-doc
title: This Doc Needs To Be Edited
---

My new content here..
```

1. Refer to that doc's ID in an existing sidebar in `website/sidebar.json`:

```javascript
// Add newly-created-doc to the Getting Started category of docs
{
  "docs": {
    "Getting Started": [
      "quick-start",
      "newly-created-doc" // new doc here
    ],
    ...
  },
  ...
}
```

For more information about adding new docs, click [here](https://docusaurus.io/docs/en/navigation)

## Adding a new blog post

1. Make sure there is a header link to your blog in `website/siteConfig.js`:

`website/siteConfig.js`
```javascript
headerLinks: [
    ...
    { blog: true, label: 'Blog' },
    ...
]
```

2. Create the blog post with the format `YYYY-MM-DD-My-Blog-Post-Title.md` in `website/blog`:

`website/blog/2018-05-21-New-Blog-Post.md`

```markdown
---
author: Frank Li
authorURL: https://twitter.com/foobarbaz
authorFBID: 503283835
title: New Blog Post
---

Lorem Ipsum...
```

For more information about blog posts, click [here](https://docusaurus.io/docs/en/adding-blog)

## Adding items to your site's top navigation bar

1. Add links to docs, custom pages or external links by editing the headerLinks field of `website/siteConfig.js`:

`website/siteConfig.js`
```javascript
{
  headerLinks: [
    ...
    /* you can add docs */
    { doc: 'my-examples', label: 'Examples' },
    /* you can add custom pages */
    { page: 'help', label: 'Help' },
    /* you can add external links */
    { href: 'https://github.com/facebook/Docusaurus', label: 'GitHub' },
    ...
  ],
  ...
}
```

For more information about the navigation bar, click [here](https://docusaurus.io/docs/en/navigation)

## Adding custom pages

1. Docusaurus uses React components to build pages. The components are saved as .js files in `website/pages/en`:
1. If you want your page to show up in your navigation header, you will need to update `website/siteConfig.js` to add to the `headerLinks` element:

`website/siteConfig.js`
```javascript
{
  headerLinks: [
    ...
    { page: 'my-new-custom-page', label: 'My New Custom Page' },
    ...
  ],
  ...
}
```

For more information about custom pages, click [here](https://docusaurus.io/docs/en/custom-pages).

# Full Documentation

Full documentation can be found on the [website](https://docusaurus.io/).
## `docusaurus-init`

An initialization script for [Docusaurus](https://docusaurus.io).

### What does it do?

Docusaurus was designed from the ground up to be easily installed and used to get your website up an running quickly. To install Docusaurus, we have created an easy script that will get all of the infrastructure setup for you:

1. Have Node >= 8.x installed. Yarn >= 1.5 is recommended as well.
1. Go into the root of your GitHub repo directory where you will be creating the docs.
1. `npx docusaurus-init`

> If you don't have Node 8.2+ or if you prefer to install Docusaurus globally, run yarn global add docusaurus-init or npm install --global docusaurus-init. After that, run docusaurus-init.

Find out more in the [official docs](https://docusaurus.io/docs/en/installation).
# Docusaurus 2

## Development Server

```bash
yarn start # open http://localhost:3000/ 
```

## Production Build

```bash
yarn build # check website/build
```
