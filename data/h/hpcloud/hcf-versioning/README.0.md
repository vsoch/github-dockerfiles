#+TITLE: git-notary
#+SUBTITLE: a versioning experiment for git
#+LATEX: \pagebreak

* Overview

~git-notary~ generates canonical version tags from versioning notes.

** Why would I want this?

~git-notary~ may be helpful if you want to use Semantic Versioning in a project
with many contributors and some manner of branch-oriented workflow. Tracking
versioning information with a ~VERSION~ file seems like a great idea, but has
some quirks.

** An Example Scenario

Consider the following (simplified) scenario:

#+BEGIN_EXAMPLE
  ,*   e44e210 - (HEAD -> develop) Merge branch 'bar' into develop
  |\
  | * e1793f3 - (bar) PATCH
  | * f231d3b - MAJOR 
  | * 5c69653 - MAJOR
  ,* |   67543e1 - Merge branch 'foo' into develop
  |\ \
  | |/
  |/|
  | * ea81623 - (foo) MAJOR
  | * 8b773db - PATCH
  | * 6613b79 - MINOR
  |/
  ,* 21c36f3 - (master) MINOR
  ,* 64357c2 - MINOR
  ,* 9ebfd7d - MINOR
  ,* cc5d832 - PATCH
  ,* ebc851f - MINOR
  ,* a75790f - PATCH
  ,* 572a9e8 - MAJOR
  ,* a990127 - (tag: 0.0.0) INITIAL
#+END_EXAMPLE

In this example, two branches (~foo~ and ~bar~) were created from ~master~
(~21c36f3~). Both branches know that ~1.4.0~ is the latest tag (at the time they
branched). Let's assume these branches do not conflict with each other.

With a ~VERSION~ file, a project generally chooses one of two places to update it:

- Updates occur in the branch. In this case, once either branch is merged, the
  other is in conflict with it.
- Updates occur in the trunk. In this case, the trunk now contains code that did
  not originate in a branch. Again, the first merged is safe, but the other is
  in a conflicting state.

If ~foo~ merges first, the expected version post-merge is ~2.0.0~.

If ~bar~ merges first, the expected version is ~3.0.1~.

At ~e44e210~ (~HEAD~ of ~develop~), the final version should be ~4.0.1~, but if
the merge order were reversed, it should be ~4.0.0~. This gets worse as the
number of active branches increases.

* Assumptions

- Versioning is important.
- Versions should communicate scope of change.
- Humans can signal the scope of their own changes.
- Machines can figure out the rest.

* Installation

Download the latest release of ~git-notary~ and place it somewhere in your ~$PATH~.
#+LATEX: \pagebreak

* Usage

** Add new versioning information

#+BEGIN_SRC shell
  git-notary new <version> [object] [namespace]
#+END_SRC

Where <version> is one of (major, minor, patch).

** Undo a version

#+BEGIN_SRC shell
  git-notary undo [object] [namespace]
#+END_SRC

** Fetch versioning notes

#+BEGIN_SRC shell
  git-notary fetch [remote] [namespace]
#+END_SRC

** Push versioning notes

#+BEGIN_SRC shell
  git-notary push [remote] [namespace]
#+END_SRC

** Extract Notes

#+BEGIN_SRC shell
  git-notary notes [branch] [base] [namespace]
#+END_SRC

** Compute Versions from Notes

#+BEGIN_SRC shell
  git-notary notes | git-notary versions [initial]
#+END_SRC

** Generate Tags from Versions

#+BEGIN_SRC shell
  git-notary notes | git-notary versions | git-notary tags [--apply]
#+END_SRC

* License

~git-notary~ is available under the [[https://tldrlegal.com/license/mit-license][MIT License]]. See ~LICENSE.txt~ for the full text.

* Contributors
- [[https://colstrom.github.io/][Chris Olstrom]] | [[mailto:chris@olstrom.com][e-mail]] | [[https://twitter.com/ChrisOlstrom][Twitter]]
git-vendor
==========
A git command for managing vendored dependencies.

`git-vendor` is a wrapper around `git-subtree` commands for checking out and updating vendored dependencies.

By default `git-vendor` conforms to the pattern used for vendoring golang dependencies:

* Dependencies are stored under `vendor/` directory in the repo.
* Dependencies are stored under the fully qualified project path.
    * e.g. `https://github.com/brettlangdon/forge` will be stored under `vendor/github.com/brettlangdon/forge`.

## Usage
See https://brettlangdon.github.io/git-vendor for the current MAN page documentation.

`git-vendor` provides the following commands:

* `git vendor add [--prefix <dir>] <name> <repository> [<ref>]` - add a new vendored dependency.
* `git vendor list [<name>]` - list current vendored dependencies, their source, and current vendored ref.
* `git vendor update <name> [<ref>]` - update a vendored dependency.

## Installation
Manually:

```bash
git clone https://github.com/brettlangdon/git-vendor
cd ./git-vendor
make
```

One-liner:
```bash
curl -sSL https://git.io/vzN5m | sudo bash /dev/stdin
```

[Homebrew](http://brew.sh) (thanks to @liamstask):
```bash
brew install git-vendor
```

## Example

```bash
$ # Checkout github.com/brettlangdon/forge@v0.1.6 under vendor/github.com/brettlangdon/forge
$ git vendor add forge https://github.com/brettlangdon/forge v0.1.6
+ git subtree add --prefix vendor/github.com/brettlangdon/forge --message 'Add "forge" from "https://github.com/brettlangdon/forge@v0.1.6"

git-vendor-name: forge
git-vendor-dir: vendor/github.com/brettlangdon/forge
git-vendor-repository: https://github.com/brettlangdon/forge
git-vendor-ref: v0.1.6
' https://github.com/brettlangdon/forge v0.1.6 --squash
git fetch https://github.com/brettlangdon/forge v0.1.6
warning: no common commits
remote: Counting objects: 405, done.
remote: Total 405 (delta 0), reused 0 (delta 0), pack-reused 404
Receiving objects: 100% (405/405), 68.31 KiB | 0 bytes/s, done.
Resolving deltas: 100% (227/227), done.
From https://github.com/brettlangdon/forge
 * tag               v0.1.6     -> FETCH_HEAD
Added dir 'vendor/github.com/brettlangdon/forge'

$ # List current vendored dependencies
$ git vendor list
forge@v0.1.6:
	name:	forge
	dir:	vendor/github.com/brettlangdon/forge
	repo:	https://github.com/brettlangdon/forge
	ref:	v0.1.6
	commit:	3335840c5f0ad9e821006588f1b16a3385d9c318

$ # Update existing dependency to a newer version
$ git vendor update forge v0.1.7
From https://github.com/brettlangdon/forge
 * tag               v0.1.7     -> FETCH_HEAD
Merge made by the 'recursive' strategy.
 vendor/github.com/brettlangdon/forge/forge_test.go | 2 ++
 vendor/github.com/brettlangdon/forge/scanner.go    | 4 ++++
 vendor/github.com/brettlangdon/forge/test.cfg      | 1 +
 3 files changed, 7 insertions(+)

$ # List current vendored dependencies
$ git vendor list
forge@v0.1.7:
	name:	forge
	dir:	vendor/github.com/brettlangdon/forge
	repo:	https://github.com/brettlangdon/forge
	ref:	v0.1.7
	commit:	071c5f108e0af39bf67a87fc766ea9bfb72b9ee7

```
