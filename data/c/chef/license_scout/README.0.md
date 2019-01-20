defmodule Mix.Tasks.Readme do
  use Mix.Task

  @shortdoc "Build README.md by including module docs"

  @moduledoc """
  Imagine a README.md that contains

      # Overview

      <!-- moduledoc: Earmark -->

      # Typical calling sequence

      <!-- doc: Earmark.to_html -->

  Run this task, and the README will be updated with the appropriate
  documentation. Markers are also added, so running it again
  will update the doc in place.
  """

  def run([]) do
    Mix.Task.run "compile", []
    File.read!("README.md")
    |> remove_old_doc
    |> add_updated_doc
    |> write_back
  end

  @new_doc ~R/(\s* <!-- \s+ (module)?doc: \s* (\S+?) \s+ -->).*\n/x

  @existing_doc ~R/
     (?:^|\n+)(\s* <!-- \s+ (module)?doc: \s* (\S+?) \s+ -->).*\n
     (?: .*?\n )+?
     \s* <!-- \s end(?:module)?doc: \s+ \3 \s+ --> \s*?
  /x

  defp remove_old_doc(readme) do
    Regex.replace(@existing_doc, readme, fn (_, hdr, _, _) ->
        hdr
    end)
  end

  defp add_updated_doc(readme) do
    Regex.replace(@new_doc, readme, fn (_, hdr, type, name) ->
      "\n" <> hdr <> "\n" <>
      doc_for(type, name) <>
      Regex.replace(~r/!-- /, hdr, "!-- end") <> "\n"
    end)
  end

  defp doc_for("module", name) do
    module = String.to_atom("Elixir." <> name)

    A
    docs = case Code.ensure_loaded(module) do
      {:module, _} ->
        if function_exported?(module, :__info__, 1) do
          case Code.get_docs(module, :moduledoc) do
            {_, docs} when is_binary(docs) ->
              docs
            _ -> nil
          end
        else
          nil
        end
      _ -> nil
    end

    docs # || "No module documentation available for #{name}\n"
  end

  defp doc_for("", name) do
    names = String.split(name, ".")
    [ func | modules ] = Enum.reverse(names)
    module = Enum.reverse(modules) |> Enum.join(".")
    module = String.to_atom("Elixir." <> module)
    func   = String.to_atom(func)

    markdown = case Code.ensure_loaded(module) do
      {:module, _} ->
        if function_exported?(module, :__info__, 1) do
          docs = Code.get_docs(module, :docs)
          Enum.find_value(docs, fn ({{fun, _}, _line, _kind, _args, doc}) ->
            fun == func && doc
          end)
        else
          nil
        end
      _ -> nil
    end

    markdown || "No function documentation available for #{name}\n"
  end


  defp write_back(readme) do
    IO.puts :stderr,
      (case File.write("README.md", readme) do
        :ok -> "README.md updated"
        {:error, reason} ->
           "README.md: #{:file.format_error(reason)}"
      end)
  end
end


# SPDX-License-Identifier: Apache-2.0
defmodule InchEx.Setup.ReadmeBadge do
  @readme_filename "README.md"

  def run? do
    File.exists?(@readme_filename)
  end

  def run(output) do
    if run? do
      IO.puts ""
      extract_url(output) |> get_badge_url |> textify |> InchEx.Setup.print
    end
  end

  defp textify(badge_url) do
    """
    ## Documentation as first-class citizen

    You can now add this badge to your #{@readme_filename}:

        #{badge_url}
    """
  end

  defp extract_url(text) do
    [_, url] = Regex.run(~r/URL:\ (.+)$/, text)
    url
  end

  defp get_badge_url(project_url) do
    "[![Inline docs](#{project_url}.svg)](#{project_url})"
  end
end

# Earmark—A Pure Elixir Markdown Processor

[![Build Status](https://travis-ci.org/pragdave/earmark.svg?branch=master)](https://travis-ci.org/pragdave/earmark)
[![Hex.pm](https://img.shields.io/hexpm/v/earmark.svg)](https://hex.pm/packages/earmark)
[![Hex.pm](https://img.shields.io/hexpm/dw/earmark.svg)](https://hex.pm/packages/earmark)
[![Hex.pm](https://img.shields.io/hexpm/dt/earmark.svg)](https://hex.pm/packages/earmark)
<!-- moduledoc: Earmark -->

## Dependency

    { :earmark, "> x.y.z" }

## Usage

### API

    * `Earmark.as_html`
      {:ok, html_doc, []}                = Earmark.as_html(markdown)
      {:error, html_doc, error_messages} = Earmark.as_html(markdown)

    * `Earmark.as_html!`
      html_doc = Earmark.as_html!(markdown, options)

      Any error messages are printed to _stderr_.

#### Options:
#
Options can be passed into `as_html` or `as_html!` according to the documentation.

      html_doc = Earmark.as_html!(markdown)

      html_doc = Earmark.as_html!(markdown, options)

Formats the error_messages returned by `as_html` and adds the filename to each.
Then prints them to stderr and just returns the html_doc

### Command line

    $ mix escript.build
    $ ./earmark file.md

Some options defined in the `Earmark.Options` struct can be specified as command line switches.

Use

    $ ./earmark --help

to find out more, but here is a short example

    $ ./earmark --smartypants false --code-class-prefix "a- b-" file.md

will call

    Earmark.as_html!( ..., %Earmark.Options{smartypants: false, code_class_prefix: "a- b-"})


## Supports

Standard [Gruber markdown][gruber].

[gruber]: <http://daringfireball.net/projects/markdown/syntax>

## Extensions

### Github Flavored Markdown


GFM is supported by default, however as GFM is a moving target and all GFM extension do not make sense in a general context, Earmark does not support all of it, here is a list of what is supported:

* StrikeThrough

      iex(13)> Earmark.as_html! ["~~hello~~"]
      "<p><del>hello</del></p>\n"

* Syntax Highlighting

The generated code blocks have a corresponding `class` attribute:



      iex(11)> Earmark.as_html! ["```elixir", "   [] |> Enum.into(%{})", "```"]
      "<pre><code class=\"elixir\">   [] |&gt; Enum.into(%{})</code></pre>\n"


which can be customized with the `code_class_prefix` option


      iex(12)> Earmark.as_html! ["```elixir", "   [] |> Enum.into(%{})", "```"] , %Earmark.Options{code_class_prefix: "lang-"}
      "<pre><code class=\"elixir lang-elixir\">   [] |&gt; Enum.into(%{})</code></pre>\n"



* Tables

Are supported as long as they are preceded by an empty line.

        State | Abbrev | Capital
        ----: | :----: | -------
        Texas | TX     | Austin
        Maine | ME     | Augusta

Tables may have leading and trailing vertical bars on each line

        | State | Abbrev | Capital |
        | ----: | :----: | ------- |
        | Texas | TX     | Austin  |
        | Maine | ME     | Augusta |

Tables need not have headers, in which case all column alignments
default to left.

        | Texas | TX     | Austin  |
        | Maine | ME     | Augusta |

Currently we assume there are always spaces around interior vertical
bars. It isn't clear what the expectation is.

### Adding HTML attributes with the IAL extension

#### To block elements

HTML attributes can be added to any block-level element. We use
the Kramdown syntax: add the line `{:` _attrs_ `}` following the block.

_attrs_ can be one or more of:

* `.className`
* `#id`
* name=value, name="value", or name='value'

For example:

        # Warning
        {: .red}

        Do not turn off the engine
        if you are at altitude.
        {: .boxed #warning spellcheck="true"}


#### To links or images

It is possible to add IAL attributes to generated links or images in the following
format.

      iex> markdown = "[link](url) {: .classy}"
      ...> Earmark.as_html(markdown)
      { :ok, "<p><a href=\"url\" class=\"classy\">link</a></p>\n", []}


For both cases, malformed attributes are ignored and warnings are issued.

      iex> [ "Some text", "{:hello}" ] |> Enum.join("\n") |> Earmark.as_html()
      {:error, "<p>Some text</p>\n", [{:warning, 2,"Illegal attributes [\"hello\"] ignored in IAL"}]}

It is possible to escape the IAL in both forms if necessary

      iex> markdown = "[link](url)\\{: .classy}"
      ...> Earmark.as_html(markdown)
      {:ok, "<p><a href=\"url\">link</a>{: .classy}</p>\n", []}


This of course is not necessary in code blocks or text lines
containing an IAL-like string, as in the following example

      iex> markdown = "hello {:world}"
      ...> Earmark.as_html!(markdown)
      "<p>hello {:world}</p>\n"

## Limitations

* Block-level HTML is correctly handled only if each HTML
  tag appears on its own line. So

        <div>
        <div>
        hello
        </div>
        </div>

  will work. However. the following won't

        <div>
        hello</div>

* John Gruber's tests contain an ambiguity when it comes to
  lines that might be the start of a list inside paragraphs.

  One test says that

        This is the text
        * of a paragraph
        that I wrote

  is a single paragraph. The "*" is not significant. However, another
  test has

        *   A list item
            * an another

  and expects this to be a nested list. But, in reality, the second could just
  be the continuation of a paragraph.

  I've chosen always to use the second interpretation—a line that looks like
  a list item will always be a list item.

* Rendering of block and inline elements.

  Block or void HTML elements that are at the absolute beginning of a line end
  the preceding paragraph.

  Thusly

        mypara
        <hr>

  Becomes

        <p>mypara</p>
        <hr>

  While

        mypara
         <hr>

  will be transformed into

        <p>mypara
         <hr></p>

## Integration

### Syntax Highlighting

All backquoted or fenced code blocks with a language string are rendered with the given
language as a _class_ attribute of the _code_ tag.

For example:

      iex> [
      ...>    "```elixir",
      ...>    " @tag :hello",
      ...>    "```"
      ...> ] |> Earmark.as_html!()
      "<pre><code class=\"elixir\"> @tag :hello</code></pre>\n"

will be rendered as shown in the doctest above.


If you want to integrate with a syntax highlighter with different conventions you can add more classes by specifying prefixes that will be
put before the language string.

Prism.js for example needs a class `language-elixir`. In order to achieve that goal you can add `language-`
as a `code_class_prefix` to `Earmark.Options`.

In the following example we want more than one additional class, so we add more prefixes.

      Earmark.as_html!(..., %Earmark.Options{code_class_prefix: "lang- language-"})

which is rendering

       <pre><code class="elixir lang-elixir language-elixir">...

As for all other options `code_class_prefix` can be passed into the `earmark` executable as follows:

      earmark --code-class-prefix "language- lang-" ...

## Security

  Please be aware that Markdown is not a secure format. It produces
  HTML from Markdown and HTML. It is your job to sanitize and or
  filter the output of `Earmark.as_html` if you cannot trust the input
  and are to serve the produced HTML on the Web.

## Author

Copyright © 2014 Dave Thomas, The Pragmatic Programmers
@/+pragdave,  dave@pragprog.com

Licensed under the same terms as Elixir, which is Apache 2.0.
<!-- endmoduledoc: Earmark -->

# Details
<!-- doc: Earmark.as_html -->
Given a markdown document (as either a list of lines or
a string containing newlines), returns a tuple containing either
`{:ok, html_doc}`, or `{:error, html_doc, error_messages}`
Where `html_doc` is an HTML representation of the markdown document and
`error_messages` is a list of strings representing information concerning
the errors that occurred during parsing.

The options are a `%Earmark.Options{}` structure:

* `renderer`: ModuleName

  The module used to render the final document. Defaults to
  `Earmark.HtmlRenderer`

* `gfm`: boolean

  True by default. Turns on the supported Github Flavored Markdown extensions

* `breaks`: boolean

  Only applicable if `gfm` is enabled. Makes all line breaks
  significant (so every line in the input is a new line in the
  output.

* `smartypants`: boolean

  Turns on smartypants processing, so quotes become curly, two
  or three hyphens become en and em dashes, and so on. True by
  default.

So, to format the document in `original` and disable smartypants,
you'd call

    alias Earmark.Options
    Earmark.as_html(original, %Options{smartypants: false})

<!-- enddoc: Earmark.as_html -->


## Plugins
<!-- moduledoc: Earmark.Plugin -->
Plugins are modules that implement a render function. Right now that is `as_html`.

### API

#### Plugin Registration

When invoking `Earmark.as_html(some_md, options)` we can register plugins inside the `plugins` map, where
each plugin is a value pointed to by the prefix triggering it.

Prefixes are appended to `"$$"` and lines starting by that string will be rendered by the registered plugin.

`%Earmark.Options{plugins: %{"" => CommentPlugin}}` would trigger the `CommentPlugin` for each block of
lines prefixed by `$$`, while `%Earmark.Options{plugins: %{"cp" => CommentPlugin}}` would do the same for
blocks of lines prefixed by `$$cp`.

Please see the documentation of `Plugin.define` for a convenience function that helps creating the necessary
`Earmark.Options` structs for the usage of plugins.

#### Plugin Invocation

`as_html` (or other render functions in the future) is invoked with a list of pairs containing the text
and line number of the lines in the block. As an example, if our plugin was registered with the default prefix
of `""` and the markdown to be converted was:

      # Plugin output ahead
      $$ line one
      $$
      $$ line two

`as_html` would be invoked as follows:

      as_html([{"line one", 2}, {"", 3}, {"line two", 4})

#### Plugin Output

Earmark's render function will invoke the plugin's render function as explained above. It can then integrate the
return value of the function into the generated rendering output if it complies to the following criteria.

1. It returns a string
1. It returns a list of strings
1. It returns a pair of lists containing a list of strings and a list of error/warning tuples.
Where the tuples are of the form `{:error | :warning, line_number, descriptive_text}`

#### A complete example

      iex> defmodule MyPlug do
      ...>   def as_html(lines) do
      ...>     # to demonstrate the three possible return values
      ...>     case render(lines) do
      ...>       {[line], []} -> line
      ...>       {lines, []} -> lines
      ...>       tuple       -> tuple
      ...>     end
      ...>   end
      ...>
      ...>   defp render(lines) do
      ...>     Enum.map(lines, &render_line/1) |> Enum.split_with(&ok?/1)
      ...>   end
      ...>
      ...>   defp render_line({"", _}), do: "<hr/>"
      ...>   defp render_line({"line one", _}), do: "<p>first line</p>\n"
      ...>   defp render_line({line, lnb}), do: {:error, lnb, line}
      ...>
      ...>   defp ok?({_, _, _}), do: false
      ...>   defp ok?(_), do: true
      ...> end
      ...>
      ...> lines = [
      ...>   "# Plugin Ahead",
      ...>   "$$ line one",
      ...>   "$$",
      ...>   "$$ line two",
      ...> ]
      ...> Earmark.as_html(lines, Earmark.Plugin.define(MyPlug))
      {:error, "<h1>Plugin Ahead</h1>\n<p>first line</p>\n<hr/>", [{ :error, 4, "line two"}]}

#### Plugins, reusing Earmark

As long as you avoid endless recursion there is absolutely no problem to call `Earmark.as_html` in your plugin, consider the following
example in which the plugin will parse markdown and render html verbatim (which is stupid, that is what Earmark already does for you,
but just to demonstrate the possibilities):

      iex> defmodule Again do
      ...>   def as_html(lines) do
      ...>     text_lines = Enum.map(lines, fn {str, _} -> str end)
      ...>     {_, html, errors} = Earmark.as_html(text_lines)
      ...>     { Enum.join([html | text_lines]), errors }
      ...>   end
      ...> end
      ...>  lines = [
      ...>    "$$a * one",
      ...>    "$$a * two",
      ...>  ]
      ...>  Earmark.as_html(lines, Earmark.Plugin.define({Again, "a"}))
      {:ok, "<ul>\n<li>one\n</li>\n<li>two\n</li>\n</ul>\n* one* two", []}
<!-- endmoduledoc: Earmark.Plugin -->

## Contributing

Pull Requests are happily accepted.

Please be aware of one _caveat_ when correcting/improving README.md.
Parts of the README.md are automatically generated by the mix task `readme`.
The generated parts are delimited by comment pairs like
    <!-- moduledoc: Earmark -->

## Dependency

    { :earmark, "> x.y.z" }

## Usage

### API

    * `Earmark.as_html`
      {:ok, html_doc, []}                = Earmark.as_html(markdown)
      {:error, html_doc, error_messages} = Earmark.as_html(markdown)

    * `Earmark.as_html!`
      html_doc = Earmark.as_html!(markdown, options)

      Any error messages are printed to _stderr_.

#### Options:
#
Options can be passed into `as_html` or `as_html!` according to the documentation.

      html_doc = Earmark.as_html!(markdown)

      html_doc = Earmark.as_html!(markdown, options)

Formats the error_messages returned by `as_html` and adds the filename to each.
Then prints them to stderr and just returns the html_doc

### Command line

    $ mix escript.build
    $ ./earmark file.md

Some options defined in the `Earmark.Options` struct can be specified as command line switches.

Use

    $ ./earmark --help

to find out more, but here is a short example

    $ ./earmark --smartypants false --code-class-prefix "a- b-" file.md

will call

    Earmark.as_html!( ..., %Earmark.Options{smartypants: false, code_class_prefix: "a- b-"})


## Supports

Standard [Gruber markdown][gruber].

[gruber]: <http://daringfireball.net/projects/markdown/syntax>

## Extensions

### Github Flavored Markdown


GFM is supported by default, however as GFM is a moving target and all GFM extension do not make sense in a general context, Earmark does not support all of it, here is a list of what is supported:

* StrikeThrough

      iex(13)> Earmark.as_html! ["~~hello~~"]
      "<p><del>hello</del></p>\n"

* Syntax Highlighting

The generated code blocks have a corresponding `class` attribute:



      iex(11)> Earmark.as_html! ["```elixir", "   [] |> Enum.into(%{})", "```"]
      "<pre><code class=\"elixir\">   [] |&gt; Enum.into(%{})</code></pre>\n"


which can be customized with the `code_class_prefix` option


      iex(12)> Earmark.as_html! ["```elixir", "   [] |> Enum.into(%{})", "```"] , %Earmark.Options{code_class_prefix: "lang-"}
      "<pre><code class=\"elixir lang-elixir\">   [] |&gt; Enum.into(%{})</code></pre>\n"



* Tables

Are supported as long as they are preceded by an empty line.

        State | Abbrev | Capital
        ----: | :----: | -------
        Texas | TX     | Austin
        Maine | ME     | Augusta

Tables may have leading and trailing vertical bars on each line

        | State | Abbrev | Capital |
        | ----: | :----: | ------- |
        | Texas | TX     | Austin  |
        | Maine | ME     | Augusta |

Tables need not have headers, in which case all column alignments
default to left.

        | Texas | TX     | Austin  |
        | Maine | ME     | Augusta |

Currently we assume there are always spaces around interior vertical
bars. It isn't clear what the expectation is.

### Adding HTML attributes with the IAL extension

#### To block elements

HTML attributes can be added to any block-level element. We use
the Kramdown syntax: add the line `{:` _attrs_ `}` following the block.

_attrs_ can be one or more of:

* `.className`
* `#id`
* name=value, name="value", or name='value'

For example:

        # Warning
        {: .red}

        Do not turn off the engine
        if you are at altitude.
        {: .boxed #warning spellcheck="true"}


#### To links or images

It is possible to add IAL attributes to generated links or images in the following
format.

      iex> markdown = "[link](url) {: .classy}"
      ...> Earmark.as_html(markdown)
      { :ok, "<p><a href=\"url\" class=\"classy\">link</a></p>\n", []}


For both cases, malformed attributes are ignored and warnings are issued.

      iex> [ "Some text", "{:hello}" ] |> Enum.join("\n") |> Earmark.as_html()
      {:error, "<p>Some text</p>\n", [{:warning, 2,"Illegal attributes [\"hello\"] ignored in IAL"}]}

It is possible to escape the IAL in both forms if necessary

      iex> markdown = "[link](url)\\{: .classy}"
      ...> Earmark.as_html(markdown)
      {:ok, "<p><a href=\"url\">link</a>{: .classy}</p>\n", []}


This of course is not necessary in code blocks or text lines
containing an IAL-like string, as in the following example

      iex> markdown = "hello {:world}"
      ...> Earmark.as_html!(markdown)
      "<p>hello {:world}</p>\n"

## Limitations

* Block-level HTML is correctly handled only if each HTML
  tag appears on its own line. So

        <div>
        <div>
        hello
        </div>
        </div>

  will work. However. the following won't

        <div>
        hello</div>

* John Gruber's tests contain an ambiguity when it comes to
  lines that might be the start of a list inside paragraphs.

  One test says that

        This is the text
        * of a paragraph
        that I wrote

  is a single paragraph. The "*" is not significant. However, another
  test has

        *   A list item
            * an another

  and expects this to be a nested list. But, in reality, the second could just
  be the continuation of a paragraph.

  I've chosen always to use the second interpretation—a line that looks like
  a list item will always be a list item.

* Rendering of block and inline elements.

  Block or void HTML elements that are at the absolute beginning of a line end
  the preceding paragraph.

  Thusly

        mypara
        <hr>

  Becomes

        <p>mypara</p>
        <hr>

  While

        mypara
         <hr>

  will be transformed into

        <p>mypara
         <hr></p>

## Integration

### Syntax Highlighting

All backquoted or fenced code blocks with a language string are rendered with the given
language as a _class_ attribute of the _code_ tag.

For example:

      iex> [
      ...>    "```elixir",
      ...>    " @tag :hello",
      ...>    "```"
      ...> ] |> Earmark.as_html!()
      "<pre><code class=\"elixir\"> @tag :hello</code></pre>\n"

will be rendered as shown in the doctest above.


If you want to integrate with a syntax highlighter with different conventions you can add more classes by specifying prefixes that will be
put before the language string.

Prism.js for example needs a class `language-elixir`. In order to achieve that goal you can add `language-`
as a `code_class_prefix` to `Earmark.Options`.

In the following example we want more than one additional class, so we add more prefixes.

      Earmark.as_html!(..., %Earmark.Options{code_class_prefix: "lang- language-"})

which is rendering

       <pre><code class="elixir lang-elixir language-elixir">...

As for all other options `code_class_prefix` can be passed into the `earmark` executable as follows:

      earmark --code-class-prefix "language- lang-" ...

## Security

  Please be aware that Markdown is not a secure format. It produces
  HTML from Markdown and HTML. It is your job to sanitize and or
  filter the output of `Earmark.as_html` if you cannot trust the input
  and are to serve the produced HTML on the Web.

## Author

Copyright © 2014 Dave Thomas, The Pragmatic Programmers
@/+pragdave,  dave@pragprog.com

Licensed under the same terms as Elixir, which is Apache 2.0.
    <!-- endmoduledoc: Earmark -->
    <!-- endmoduledoc: Earmark -->

or
    <!-- doc: Earmark.as_html -->
Given a markdown document (as either a list of lines or
a string containing newlines), returns a tuple containing either
`{:ok, html_doc}`, or `{:error, html_doc, error_messages}`
Where `html_doc` is an HTML representation of the markdown document and
`error_messages` is a list of strings representing information concerning
the errors that occurred during parsing.

The options are a `%Earmark.Options{}` structure:

* `renderer`: ModuleName

  The module used to render the final document. Defaults to
  `Earmark.HtmlRenderer`

* `gfm`: boolean

  True by default. Turns on the supported Github Flavored Markdown extensions

* `breaks`: boolean

  Only applicable if `gfm` is enabled. Makes all line breaks
  significant (so every line in the input is a new line in the
  output.

* `smartypants`: boolean

  Turns on smartypants processing, so quotes become curly, two
  or three hyphens become en and em dashes, and so on. True by
  default.

So, to format the document in `original` and disable smartypants,
you'd call

    alias Earmark.Options
    Earmark.as_html(original, %Options{smartypants: false})

    <!-- enddoc: Earmark.as_html -->
    <!-- enddoc: Earmark.as_html -->

Please modify the associated docstrings instead.

## Author

Copyright © 2014 Dave Thomas, The Pragmatic Programmers
@/+pragdave,  dave@pragprog.com

# LICENSE

Same as Elixir, which is Apache License v2.0. Please refer to [LICENSE](LICENSE) for details.

SPDX-License-Identifier: Apache-2.0
# InchEx [![Inline docs](http://inch-ci.org/github/rrrene/inch_ex.svg?branch=master)](http://inch-ci.org/github/rrrene/inch_ex)

InchEx provides a Mix task to give you hints where to improve your inline docs. One Inch at a time.

[Inch CI](http://inch-ci.org) is the corresponding web service that provides continuous coverage analysis for open source projects.



## What can it do?

InchEx is a utility that suggests places in your codebase where documentation can be improved.

If there are no inline-docs yet, InchEx can tell you where to start.



## Installation

Add InchEx as a dependency in your `mix.exs` file.

```elixir
defp deps do
  [{:inch_ex, only: :docs}]
end
```

After you are done, run this in your shell to fetch the new dependency:

    $ MIX_ENV=docs mix deps.get


## Usage

To run Inch, simply type

    $ MIX_ENV=docs mix inch

and you will get something like the following:

```bash
    $ MIX_ENV=docs mix inch

    # Properly documented, could be improved:

    ┃  B  ↑  Foo.complicated/5

    # Undocumented:

    ┃  U  ↑  Foo
    ┃  U  ↗  Foo.filename/1

    Grade distribution (undocumented, C, B, A):  █  ▁ ▄ ▄
```

If you have Inch installed it will run locally. If not, it will use the API of [inch-ci.org](http://inch-ci.org/) to display results. If you want to specify a certain Inch version you have installed (e.g. for testing), you can set the `INCH_PATH` environment variable.



## Adding a project to Inch CI

[Inch CI](https://inch-ci.org/) is a web service based on Inch, that provides an evaluation of a project's docs and a corresponding badge:

> [![Inline docs](http://inch-ci.org/github/rrrene/inch_ex.svg?branch=master)](http://inch-ci.org/github/rrrene/inch_ex)

Adding your project to [Inch CI](https://inch-ci.org/) and getting a badge is easy:

```bash
    $ MIX_ENV=docs mix inchci.add

                             Adding project to Inch CI ...

    Successfully created build #1
    URL: http://inch-ci.org/github/rrrene/inch_ex

    [ snip ]
```

There is a blog post for [a screenshot and more information](http://trivelop.de/2015/05/19/elixir-inchci-add/).



## Philosophy

Inch was created to help people document their code, therefore it may be more important to look at **what it does not** do than at what it does.

* It does not aim for "fully documented" or "100% documentation coverage".
* It does not tell you to document all your code (neither does it tell you not to).
* It does not impose rules on how your documentation should look like.
* It does not require that, e.g."every method's documentation should be a single line under 80 characters not ending in a period" or that "every class and module should provide a code example of their usage".

Inch takes a more relaxed approach towards documentation measurement and tries to show you places where your codebase *could* use more documentation.



### The Grade System

Inch assigns grades to each module, function, macro or callback in a codebase, based on how complete the docs are.

The grades are:

* `A` - Seems really good
* `B` - Properly documented, but could be improved
* `C` - Needs work
* `U` - Undocumented

Using this system has some advantages compared to plain coverage scores:

* You can get an `A` even if you "only" get 90 out of 100 possible points.
* Getting a `B` is basically good enough.
* Undocumented objects are assigned a special grade, instead of scoring 0%.

The last point might be the most important one: If objects are undocumented, there is nothing to evaluate. Therefore you can not simply give them a bad rating, because they might be left undocumented intentionally.



### Priorities ↑ ↓

Every class, module, constant and method in a codebase is assigned a priority which reflects how important Inch thinks it is to be documented.

This process follows some reasonable rules, like

* it is more important to document public methods than private ones
* it is more important to document methods with many parameters than methods without parameters
* it is not important to document objects marked as `@doc false`

Priorities are displayed as arrows. Arrows pointing north mark high priority objects, arrows pointing south mark low priority objects.



### No overall scores or grades

Inch does not give you a grade for your whole codebase.

"Why?" you might ask. Look at the example below:

    Grade distribution (undocumented, C, B, A):  ▄  ▁ ▄ █

In this example there is a part of code that is still undocumented, but
the vast majority of code is rated A or B.

This tells you three things:

* There is a significant amount of documentation present.
* The present documentation seems good.
* There are still undocumented methods.

Inch does not really tell you what to do from here. It suggests objects and
files that could be improved to get a better rating, but that is all. This
way, it is perfectly reasonable to leave parts of your codebase
undocumented.

Instead of reporting

    coverage: 67.1%  46 ouf of 140 checks failed

and leaving you with a bad feeling, Inch tells you there are still
undocumented objects without judging.

This provides a lot more insight than an overall grade could, because an overall grade for the above example would either be an `A` (if the evaluation ignores undocumented objects) or a weak `C` (if the evaluation includes them).

The grade distribution does a much better job of painting the bigger picture.



## Further information

I will point you to the [original Inch README](https://github.com/rrrene/inch#philosophy) for more information about the Inch project.



## Contributing

1. [Fork it!](http://github.com/rrrene/inch_ex/fork)
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request



## Author

René Föhring (@rrrene)



## Credits

InchEx ows its existence to the extensive study and "code borrowing" from ExDoc.



## License

InchEx is released under the MIT License. See the LICENSE file for further
details.
# Poison

[![Travis](https://img.shields.io/travis/devinus/poison.svg?style=flat-square)](https://travis-ci.org/devinus/poison)
[![Hex.pm](https://img.shields.io/hexpm/v/poison.svg?style=flat-square)](https://hex.pm/packages/poison)
[![Hex.pm](https://img.shields.io/hexpm/dt/poison.svg?style=flat-square)](https://hex.pm/packages/poison)
[![Gratipay](https://img.shields.io/gratipay/devinus.svg?style=flat-square)](https://gratipay.com/devinus)

Poison is a new JSON library for Elixir focusing on wicked-fast **speed**
without sacrificing **simplicity**, **completeness**, or **correctness**.

Poison takes several approaches to be the fastest JSON library for Elixir.

Poison uses extensive [sub binary matching][1], a **hand-rolled parser** using
several techniques that are [known to benefit HiPE][2] for native compilation,
[IO list][3] encoding and **single-pass** decoding.

Preliminary benchmarking has sometimes put Poison's performance closer to
`jiffy`, and almost always faster than existing Elixir libraries.

## Installation

First, add Poison to your `mix.exs` dependencies:

```elixir
def deps do
  [{:poison, "~> 1.5"}]
end
```

Then, update your dependencies:

```sh-session
$ mix deps.get
```

## Usage

```elixir
defmodule Person do
  @derive [Poison.Encoder]
  defstruct [:name, :age]
end

Poison.encode!(%Person{name: "Devin Torres", age: 27})
#=> "{\"name\":\"Devin Torres\",\"age\":27}"

Poison.decode!(~s({"name": "Devin Torres", "age": 27}), as: Person)
#=> %Person{name: "Devin Torres", age: 27}

Poison.decode!(~s({"people": [{"name": "Devin Torres", "age": 27}]}),
  as: %{"people" => [Person]})
#=> %{"people" => [%Person{age: 27, name: "Devin Torres"}]}
```

Every component of Poison -- the encoder, decoder, and parser -- are all usable
on their own without buying into other functionality. For example, if you were
interested purely in the speed of parsing JSON without a decoding step, you
could simply call `Poison.Parser.parse`.

## Parser

```iex
iex> Poison.Parser.parse!(~s({"name": "Devin Torres", "age": 27}))
%{"name" => "Devin Torres", "age" => 27}
iex> Poison.Parser.parse!(~s({"name": "Devin Torres", "age": 27}), keys: :atoms!)
%{name: "Devin Torres", age: 27}
```

Note that `keys: :atoms!` reuses existing atoms, i.e. if `:name` was not
allocated before the call, you will encounter an `argument error` message.

You can use the `keys: :atoms` variant to make sure all atoms are created as
needed.  However, unless you absolutely know what you're doing, do **not** do
it.  Atoms are not garbage-collected, see
[Erlang Efficiency Guide](http://www.erlang.org/doc/efficiency_guide/commoncaveats.html)
for more info:

> Atoms are not garbage-collected. Once an atom is created, it will never be
> removed. The emulator will terminate if the limit for the number of atoms
> (1048576 by default) is reached.

## Encoder

```iex
iex> IO.puts Poison.Encoder.encode([1, 2, 3], [])
"[1,2,3]"
```

Anything implementing the Encoder protocol is expected to return an
[IO list][4] to be embedded within any other Encoder's implementation and
passable to any IO subsystem without conversion.

```elixir
defimpl Poison.Encoder, for: Person do
  def encode(%{name: name, age: age}, options) do
    Poison.Encoder.BitString.encode("#{name} (#{age})", options)
  end
end
```

For maximum performance, make sure you `@derive [Poison.Encoder]` for any struct
you plan on encoding.

## Benchmarking

```sh-session
$ mix deps.get
$ MIX_ENV=bench mix compile.protocols
$ MIX_ENV=bench elixir -pa _build/bench/lib/\*/ebin -pa _build/bench/consolidated -S mix bench
```

## License

Poison is released into the public domain (see `UNLICENSE`).
Poison is also optionally available under the ISC License (see `LICENSE`),
meant especially for jurisdictions that do not recognize public domain works.

[1]: http://www.erlang.org/euc/07/papers/1700Gustafsson.pdf
[2]: http://www.erlang.org/workshop/2003/paper/p36-sagonas.pdf
[3]: http://jlouisramblings.blogspot.com/2013/07/problematic-traits-in-erlang.html
[4]: http://prog21.dadgum.com/70.html
# ExDoc

[![Build Status](https://secure.travis-ci.org/elixir-lang/ex_doc.svg?branch=master "Build Status")](http://travis-ci.org/elixir-lang/ex_doc)
[![Coverage Status](https://coveralls.io/repos/github/elixir-lang/ex_doc/badge.svg?branch=master)](https://coveralls.io/github/elixir-lang/ex_doc?branch=master)
[![Ebert](https://ebertapp.io/github/elixir-lang/ex_doc.svg)](https://ebertapp.io/github/elixir-lang/ex_doc)

ExDoc is a tool to generate documentation for your Elixir projects. In case you are looking for documentation for Elixir itself, [check out Elixir's website][elixir-lang].

To learn about how to document your projects check out [Elixir's writing documentation page][hex-writing-docs].

## Using ExDoc with Mix

To use ExDoc in your Mix projects, first add ExDoc as a dependency:

```elixir
def deps do
  [{:ex_doc, "~> 0.16", only: :dev, runtime: false}]
end
```

After adding ExDoc as a dependency, run `mix deps.get` to install it.

ExDoc will automatically pull in information from your projects, like the application and version. However, you may want to set `:name`, `:source_url` and `:homepage_url` to have a nicer output from ExDoc, such as:

```elixir
def project do
  [app: :my_app,
   version: "0.1.0-dev",
   deps: deps(),

   # Docs
   name: "MyApp",
   source_url: "https://github.com/USER/PROJECT",
   homepage_url: "http://YOUR_PROJECT_HOMEPAGE",
   docs: [main: "MyApp", # The main page in the docs
          logo: "path/to/logo.png",
          extras: ["README.md"]]]
end
```

Now you are ready to generate your project documentation with `mix docs`.

To see all options available when generating docs, run `mix help docs`. You may have to run `mix docs` or `mix compile` first.

## Using ExDoc via command line

You can ExDoc via the command line as follows:

1. Install ExDoc as an escript:

    ```console
    $ mix escript.install hex ex_doc
    ```

2. Then you are ready to use it in your projects. First, move into your project directory and make sure it is already compiled:

    ```console
    $ cd PATH_TO_YOUR_PROJECT
    $ mix compile
    ```

3. Next invoke the ex_doc executable from your project:

    ```console
    $ ex_doc "PROJECT_NAME" "PROJECT_VERSION" path/to/project/ebin -m "PROJECT_MODULE" -u "https://github.com/GITHUB_USER/GITHUB_REPO" -l path/to/logo.png
    ```

4. By default, ex_doc produces HTML files, but, you can also create a EPUB document passing the option `--formatter epub`:

    ```console
    $ PATH_TO_YOUR_EXDOC/bin/ex_doc "PROJECT_NAME" "PROJECT_VERSION" path/to/project/ebin -m "PROJECT_MODULE" -u "https://github.com/GITHUB_USER/GITHUB_REPO" -l path/to/logo.png -f epub
    ```

For example, here are some acceptable values:

    PROJECT_NAME    => Ecto
    PROJECT_VERSION => 0.1.0
    PROJECT_MODULE  => Ecto (the main module provided by the library)
    GITHUB_USER     => elixir-lang
    GITHUB_REPO     => ecto

## Auto-linking

ExDoc will automatically generate links across modules and functions if you enclose them in backticks:

  * By referring to a module, function, type or callback from your project, such as `` `MyModule` ``, ExDoc will automatically link to those
  * By referring to a module, function, type or callback from Elixir, such as `` `String` ``, ExDoc will automatically link to Elixir's stable documentation
  * By referring to a module or function from erlang, such as (`` `:erlang` ``), ExDoc will automatically link to the Erlang documentation
  * By referring to a module, function, type or callback from any of your dependencies, such as `` `MyDep` ``, ExDoc will automatically link to that dependency documentation on [hexdocs.pm](http://hexdocs.pm/) (the link can be configured by setting `docs: [deps: [my_dep: "https://path/to/docs/"]]` in your `mix.exs`)

ExDoc supports linking to modules (`` `MyModule` ``), functions (`` `MyModule.function/1` ``), types (`` `t:MyModule.type/2` ``) and callbacks (`` `c:MyModule.callback/3` ``). If you want to link a function, type or callback in the current module, you may skip the module name, such as `` `function/1` ``.

## Changing the Markdown tool

In the examples above, we have used [Earmark][] to convert Markdown to HTML. If you prefer, you can also use cmark (in C).

### Cmark

[Cmark][cmark] is a CommonMark parser written in C. To use cmark add the elixir NIF wrapper [cmark.ex][cmark.ex] as a dependency to your project:

```elixir
{:cmark, "~> 0.6", only: :dev}
```

Update your project configuration to use Cmark:

```elixir
docs: [markdown_processor: ExDoc.Markdown.Cmark]
```

# License

ExDoc source code is released under Apache 2 License. The generated contents, however, are under different licenses based on projects used to help render HTML, including CSS, JS, and other assets.

Check the [LICENSE](LICENSE) file for more information.

[earmark]: http://github.com/pragdave/earmark
[elixir-lang]: http://elixir-lang.org/
[cmark]: https://github.com/jgm/cmark
[cmark.ex]: https://github.com/asaaki/cmark.ex
[devinus/markdown]: http://github.com/devinus/markdown
[hex-writing-docs]: https://hexdocs.pm/elixir/writing-documentation.html
# mingw Cookbook

[![Cookbook Version](http://img.shields.io/cookbook/v/mingw.svg)][cookbook] [![Build Status](http://img.shields.io/travis/chef-cookbooks/mingw.svg?branch=master)][travis]

Installs a mingw/msys based compiler tools chain on windows. This is required for compiling C software from source.

## Requirements

### Platforms

- Windows

### Chef

- Chef 12+

### Cookbooks

- seven_zip
- compat_resource

## Usage

Add this cookbook as a dependency to your cookbook in its `metadata.rb` and include the default recipe in one of your recipes.

```ruby
# metadata.rb
depends 'mingw'
```

```ruby
# your recipe.rb
include_recipe 'mingw::default'
```

Use the `msys2_package` resource in any recipe to fetch msys2 based packages.
Use the `mingw_get` resource in any recipe to fetch mingw packages.
Use the `mingw_tdm_gcc` resource to fetch a version of the TDM GCC compiler.

By default, you should prefer the msys2 packages as they are newer and better supported.  C/C++ compilers on windows use various different exception formats and you need to pick the right one for your task.  In the 32-bit world, you have SJLJ (set-jump/long-jump) based exception handling and DWARF-2 (shortened to DW2) based exception handling.  SJLJ produces code that can happily throw exceptions across stack frames of code compiled by MSVC.  DW2 involves more extensive metadata but produces code that cannot unwind MSVC generated stack-frames - hence you need to ensure that you don't have any code that throws across a "system call".  Certain languages and runtimes have specific requirements as to the exception format supported.  As an example, if you are building code for Rust, you will probably need a modern gcc from msys2 with DW2 support as that's what the panic/exception formatter in Rust depends on.  In a 64-bit world, you may still use SJLJ but compilers all commonly support SEH (structured exception handling).

Of course, to further complicate matters, different versions of different compilers support different exception handling.  The default compilers that come with mingw_get are 32-bit only compilers and support DW2.  The TDM compilers come in 3 flavors: a 32-bit only version with SJLJ support, a 32-bit only version with DW2 support and a "multilib" compiler which supports only SJLJ in 32-bit mode but can produce 64-bit SEH code.  The standard library support varies drastically between these various compiler flavors (even within the same version).  In msys2, you can install a mingw-w64 based compilers for either 32-bit DW2 support or 64-bit SEH support.  If all this hurts your brain, I can only apologize.

## Resources

### msys2_package
- ':install' - Installs an msys2 package using pacman.
- ':remove' - Uninstalls any existing msys2 package.
- ':upgrade' - Upgrades the specified package using pacman.

All options also automatically attempt to install a 64-bit based msys2 base file system at the root path specified.  Note that you probably won't need a "32-bit" msys2 unless you are actually on a 32-bit only platform.  You can still install both 32 and 64-bit compilers and libraries in a 64-bit msys2 base file system.

#### Parameters

- `package` - An msys2 pacman package (or meta-package) to fetch and install. You may use a legal package wild-card pattern here if you are installing. This is the name attribute.
- `root` - The root directory where msys2 tools will be installed. This directory must not contain any spaces in order to pacify old posix tools and most Makefiles.

#### Examples

To get the core msys2 developer tools in `C:\msys2`

```ruby
msys2_package 'base-devel' do
  root 'C:\msys2'
end
```

### mingw_get

#### Actions

- `:install` - Installs a mingw package from sourceforge using mingw-get.exe.
- `:remove` - Uninstalls a mingw package.
- `:upgrade` - Upgrades a mingw package (even to a lower version).

#### Parameters

- `package` - A mingw-get package (or meta-package) to fetch and install. You may use a legal package wild-card pattern here if you are installing. This is the name attribute.
- `root` - The root directory where msys and mingw tools will be installed. This directory must not contain any spaces in order to pacify old posix tools and most Makefiles.

#### Examples

To get the core msys developer tools in `C:\mingw32`

```ruby
mingw_get 'msys-base=2013072300-msys-bin.meta' do
  root 'C:\mingw32'
end
```

### mingw_tdm_gcc

#### Actions

- `:install` - Installs the TDM compiler toolchain at the given path. This only gives you a compiler. If you need any support tooling such as make/grep/awk/bash etc., see `mingw_get`.

#### Parameters

- `flavor` - Either `:sjlj_32` or `:seh_sjlj_64`. TDM-64 is a 32/64-bit multi-lib "cross-compiler" toolchain that builds 64-bit by default. It uses structured exception handling (SEH) in 64-bit code and setjump-longjump exception handling (SJLJ) in 32-bit code. TDM-32 only builds 32-bit binaries and uses SJLJ.
- `root` - The root directory where compiler tools and runtime will be installed. This directory must not contain any spaces in order to pacify old posix tools and most Makefiles.
- `version` - The version of the compiler to fetch and install. This is the name attribute. Currently, '5.1.0' is supported.

#### Examples

To get the 32-bit TDM GCC compiler in `C:\mingw32`

```ruby
mingw_tdm_gcc '5.1.0' do
  flavor :sjlj_32
  root 'C:\mingw32'
end
```

## License & Authors

**Author:** Cookbook Engineering Team ([cookbooks@chef.io](mailto:cookbooks@chef.io))

**Copyright:** 2009-2016, Chef Software, Inc.

```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

[cookbook]: https://supermarket.chef.io/cookbooks/mingw
[travis]: http://travis-ci.org/chef-cookbooks/mingw
omnibus Cookbook
================

[![Cookbook Version](https://img.shields.io/cookbook/v/omnibus.svg)](https://supermarket.chef.io/cookbooks/omnibus)

Prepares a machine to be an Omnibus builder.

This project is managed by the CHEF Release Engineering team. For more information on the Release Engineering team's contribution, triage, and release process, please consult the [CHEF Release Engineering OSS Management Guide](https://docs.google.com/a/opscode.com/document/d/1oJB0vZb_3bl7_ZU2YMDBkMFdL-EWplW1BJv_FXTUOzg/edit).

Announcement
------------
Starting with omnibus cookbook version 4.0.0:
* Chef 11 is no longer supported, since 12.5.1 is required to use [chef-ingredient](https://github.com/chef-cookbooks/chef-ingredient). If needed, you can pin to omnibus version `3.2.x` to preserve the old functionality.
* Instead of compiling everything from source in this cookbook, the [omnibus-toolchain](https://github.com/chef/omnibus-toolchain) package will be installed. This package contains patch, bash, make, git, ruby, rubygems, and bundler (built from [omnibus-software](https://github.com/chef/omnibus-software) definitions).

Requirements
------------
This cookbook requires Chef 12.5.1+.

For a full list of supported platforms and external cookbook requirements, please see the `metadata.rb` file at the root of the cookbook.

Recipes
-------
The default recipe is the main entrypoint for the cookbook and does the following:

- Ensures all required Omnibus-related directories are created and owned by the build user.
- Ensures a sane build tool-chain is installed and configured (using the [build-essential](http://community.opscode.com/cookbooks/build-essential) cookbook)
- Ensures the necessary tools to run an Omnibus project (ruby, git, etc) are installed (using the [omnibus-toolchain](https://github.com/chef/omnibus-toolchain) package)
- Includes a platform-specific recipe to apply additional tweaks as appropriate.

All other recipes should be treated as "private" and are not meant to be used individually. They only exist to support the `default` recipe.


Attributes
----------
| Attribute     | Default                                               | Description                                              |
|---------------|-------------------------------------------------------|----------------------------------------------------------|
| `build_user`  | `omnibus`                                             | The user to execute Omnibus builds as                    |
| `base_dir`    | Windows: `C:/omnibus-ruby` *nix: `/var/cache/omnibus` | The "base" directory where Omnibus will store its data. |

Resources
---------

### omnibus_build

This resource is used to execute a build of an Omnibus project.

#### Attributes

| Attribute          | Default                                               | Description                           |
|--------------------|-------------------------------------------------------|---------------------------------------|
| `project_name`     |                                                       | The name of the Omnibus project to build |
| `project_dir`      |                                                       | The directory to install Omnibus |
| `install_dir`      | `/opt/<PROJECT>`                                      | The installation of the project being built |
| `base_dir`         | Windows: `C:/omnibus-ruby` *nix: `/var/cache/omnibus` | The base directory for Omnibus |
| `log_level`        | `:internal`                                           | Log level used during the build. Valid values include: `:internal, :debug, :info, :warn, :error, :fatal` |
| `config_file`      | `<PROJECT_DIR>/omnibus.rb`                            | Omnibus configuration file used for the build. |
| `config_overrides` | `{}`                                                  | Overrides for one or more Omnibus config options |
| `expire_cache`     | `false`                                               | Indiciates the Omnibus cache (including git cache) should be wiped before building.  |
| `build_user`       | `node['omnibus']['build_user']`                       | The user to execute the Omnibus build as. |
| `environment`      | `{}`                                                  | Environment variables to set in the underlying build process. |

#### Example Usage

```ruby
omnibus_build 'harmony' do
  project\_dir 'https://github.com/chef/omnibus-harmony.git'
  log_level :internal
  config_override(
    append_timestamp: true
  )
end
```

Usage
-----
Include the `omnibus::default` recipe in your node's run list and override the cookbook's default attributes as desired. At the very least you will want to override `node['omnibus']['install_dir']` to match the installation directory of your Omnibus project.

Using Test Kitchen with Docker
------------------------------

The following assumes you are on a Mac OS X workstation and have installed and
started [Kitematic](https://kitematic.com/).

* Install [kitchen-docker](https://github.com/portertech/kitchen-docker) into your local ChefDK install:
```
$ chef gem install kitchen-docker
Successfully installed kitchen-docker-2.3.0
1 gem installed
```

* Set environment variables to point kitchen-docker at your local Kitematic instance:
```
# Bash
export DOCKER_HOST=tcp://192.168.99.100:2376
export DOCKER_CERT_PATH=$HOME/.docker/machine/certs
export DOCKER_TLS_VERIFY=1

# Fish
set -gx DOCKER_HOST "tcp://192.168.99.100:2376"
set -gx DOCKER_CERT_PATH "$HOME/.docker/machine/certs"
set -gx DOCKER_TLS_VERIFY 1
```

* Run Test Kitchen with the provided `.kitchen.docker.yml`:
```
KITCHEN_LOCAL_YAML=.kitchen.docker.yml kitchen verify languages-ruby-ubuntu-1204
```

License & Authors
-----------------
- Author: Seth Vargo (<sethvargo@gmail.com>)
- Author: Yvonne Lam (<yvonne@chef.io>)
- Author: Seth Chisamore (<schisamo@chef.io>)
- Author: Stephen Delano (<stephen@chef.io>)

```text
Copyright 2012-2016, Chef Software, Inc. (<legal@chef.io>)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
remote_install Cookbook
=======================

[![Build Status](https://travis-ci.org/chef-cookbooks/remote_install.svg?branch=master)](http://travis-ci.org/chef-cookbooks/remote_install)
[![Cookbook Version](https://img.shields.io/cookbook/v/remote_install.svg)](https://supermarket.chef.io/cookbooks/remote_install)

Provides a highly-opinionated way to download, extract, and compile software from a remote source.

This project is managed by the CHEF Release Engineering team. For more information on the Release Engineering team's contribution, triage, and release process, please consult the [CHEF Release Engineering OSS Management Guide](https://docs.google.com/a/opscode.com/document/d/1oJB0vZb_3bl7_ZU2YMDBkMFdL-EWplW1BJv_FXTUOzg/edit).


Usage
-----
Install bash:

```ruby
remote_install 'bash' do
  source 'http://ftp.gnu.org/gnu/bash/bash-4.3.tar.gz'
  version '4.3'
  checksum 'afc687a28e0e24dc21b988fa159ff9dbcf6b7caa92ade8645cc6d5605cd024d4'
  build_command './configure'
  compile_command 'make'
  install_command 'make install'
end
```

The `remote_install` resource has the following attributes:

| Attribute         | Description
| ----------------- | -----------
| `source`          | the URL to download
| `checksum`        | the SHA256 checksum for the downlaoded asset from `source`
| `build_command`   | the command to "build"
| `compile_command` | the command to "compile"
| `install_command` | the command to "install"
| `environment`     | the environment to set while building


License & Authors
-----------------
- Author: Seth Vargo (<sethvargo@gmail.com>)
- Author: Yvonne Lam (<yvonne@chef.io>)
- Author: Seth Chisamore (<schisamo@chef.io>)

```text
Copyright 2014, Chef Software, Inc. (<legal@chef.io>)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
dmg Cookbook
============

[![Build Status](https://travis-ci.org/chef-cookbooks/dmg.svg?branch=master)](https://travis-ci.org/chef-cookbooks/dmg)
[![Cookbook Version](https://img.shields.io/cookbook/v/dmg.svg)](https://supermarket.chef.io/cookbooks/dmg)

Lightweight resource and provider to install OS X applications (.app) from dmg files.


Requirements
------------
#### Platforms
- Mac OS X

#### Chef
- Chef 11+

#### Cookbooks
- none


Resources/Providers
-------------------
### dmg_package

This resource will install a DMG "Package". It will retrieve the DMG from a remote URL, mount it using OS X's `hdid`, copy the application (.app directory) to the specified destination (/Applications), and detach the image using `hdiutil`. The dmg file will be stored in the `Chef::Config[:file_cache_path]`. If you want to install an application that has already been downloaded (not using the `source` parameter), copy it to the appropriate location. You can find out what directory this is with the following command on the node to run chef:

```bash
knife exec -E 'p Chef::Config[:file_cache_path]' -c /etc/chef/client.rb
```

Optionally, the LWRP can install an "mpkg" or "pkg" package using installer(8).

#### Actions
- :install - Installs the application.

#### Parameter attributes:
- `app` - This is the name of the application used by default for the /Volumes directory and the .app directory copied to /Applications.
- `source` - remote URL for the dmg to download if specified. Default is nil.
- `file` - local dmg full file path. Default is nil.
- `owner` - owner that should own the package installation.
- `destination` - directory to copy the .app into. Default is /Applications.
- `checksum` - sha256 checksum of the dmg to download. Default is nil.
- `type` - type of package, "app", "pkg" or "mpkg". Default is "app". When using "pkg" or "mpkg", the destination must be /Applications.
- `volumes_dir` - Directory under /Volumes where the dmg is mounted. Not all dmgs are mounted into a /Volumes location matching the name of the dmg. If not specified, this will use the name attribute.
- `package_id` - Package id registered with pkgutil when a pkg or mpkg is installed
- `dmg_name` - Specify the name of the dmg if it is not the same as `app`, or if the name has spaces.
- `dmg_passphrase` - Specify a passphrase to use to unencrypt the dmg while mounting.
- `accept_eula` - Specify whether to accept the EULA.  Certain dmgs require acceptance of EULA before mounting.  Can be true or false, defaults to false.
- `headers` - Allows custom HTTP headers (like cookies) to be set on the remote_file resource.

#### Examples
Install `/Applications/Tunnelblick.app` from the primary download site.

```ruby
dmg_package 'Tunnelblick' do
  source   'http://tunnelblick.googlecode.com/files/Tunnelblick_3.1.2.dmg'
  checksum 'a3fae60b6833175f32df20c90cd3a3603a'
  action   :install
end
```

Install Google Chrome. Uses the `dmg_name` because the application name has spaces. Installs in `/Applications/Google Chrome.app`.

```ruby
dmg_package 'Google Chrome' do
  dmg_name 'googlechrome'
  source   'https://dl-ssl.google.com/chrome/mac/stable/GGRM/googlechrome.dmg'
  checksum '7daa2dc5c46d9bfb14f1d7ff4b33884325e5e63e694810adc58f14795165c91a'
  action   :install
end
```

Install Dropbox. Uses `volumes_dir` because the mounted directory is different than the name of the application directory. Installs in `/Applications/Dropbox.app`.

```ruby
dmg_package 'Dropbox' do
  volumes_dir 'Dropbox Installer'
  source      'http://www.dropbox.com/download?plat=mac'
  checksum    'b4ea620ca22b0517b75753283ceb82326aca8bc3c86212fbf725de6446a96a13'
  action      :install
end
```

Install MacIrssi to `~/Applications` from the local file downloaded to the cache path into an Applications directory in the current user's home directory. Chef should run as a non-root user for this.

```ruby
directory "#{ENV['HOME']}/Applications"

dmg_package 'MacIrssi' do
  destination "#{ENV['HOME']}/Applications"
  action      :install
end
```

Install Virtualbox to `/Applications` from the .mpkg:

```ruby
dmg_package 'Virtualbox' do
  source 'http://dlc.sun.com.edgesuite.net/virtualbox/4.0.8/VirtualBox-4.0.8-71778-OSX.dmg'
  type   'mpkg'
end
```

Install pgAdmin to `/Applications` and automatically accept the EULA:

```ruby
dmg_package 'pgAdmin3' do
  source   'http://wwwmaster.postgresql.org/redir/198/h/pgadmin3/release/v1.12.3/osx/pgadmin3-1.12.3.dmg'
  checksum '9435f79d5b52d0febeddfad392adf82db9df159196f496c1ab139a6957242ce9'
  accept_eula true
end
```

Install Silverlight, with idempotence check based on pkgutil:

```ruby
dmg_package 'Silerlight' do
  source     'http://silverlight.dlservice.microsoft.com/download/D/C/2/DC2D5838-9138-4D25-AA92-52F61F7C51E6/runtime/Silverlight.dmg'
  type       'pkg'
  checksum   '6d4a0ad4552d9815531463eb3f467fb8cf4bffcc'
  package_id 'com.microsoft.installSilverlightPlugin'
end
```


License & Authors
-----------------

**Author:** Cookbook Engineering Team (<cookbooks@chef.io>)

**Copyright:** 2011-2015, Chef Software, Inc.
```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
Chef Sugar
==========
[![Gem Version](http://img.shields.io/gem/v/chef-sugar.svg?style=flat-square)][gem]
[![Build Status](http://img.shields.io/travis/sethvargo/chef-sugar.svg?style=flat-square)][travis]

[gem]: https://rubygems.org/gems/chef-sugar
[travis]: http://travis-ci.org/sethvargo/chef-sugar

Chef Sugar is a Gem & Chef Recipe that includes series of helpful sugar of the Chef core and other resources to make a cleaner, more lean recipe DSL, enforce DRY principles, and make writing Chef recipes an awesome experience!


Installation
------------
If you want to develop/hack on chef-sugar, please see the Contributing.md.

If you are using Berkshelf, add `chef-sugar` to your `Berksfile`:

```ruby
cookbook 'chef-sugar'
```

Otherwise, you can use `knife` or download the tarball directly from the community site:

```ruby
knife cookbook site install chef-sugar
```


Usage
-----
In order to use Chef Sugar in your Chef Recipes, you'll first need to include it:

```ruby
include_recipe 'chef-sugar::default'
```

Alternatively you can put it in a base role or recipe and it will be included subsequently.

Requiring the Chef Sugar Gem will automatically extend the Recipe DSL, `Chef::Resource`, and `Chef::Provider` with helpful convenience methods.

### Module Method
If you are working outside of the Recipe DSL, you can use the module methods instead of the Recipe DSL. In general, the module methods have the same name as their Recipe-DSL counterparts, but require the node object as a parameter. For example:

In a Recipe:

```ruby
# cookbook/recipes/default.rb
do_something if windows?
```

In a Library as a singleton:

```ruby
# cookbook/libraries/default.rb
def only_on_windows(&block)
  yield if Chef::Sugar::PlatformFamily.windows?(@node)
end
```

In a Library as a Mixin:

```ruby
# cookbook/libraries/default.rb
include Chef::Sugar::PlatformFamily

def only_on_windows(&block)
  yield if windows?(@node)
end
```


API
---
**Note:** For the most extensive API documentation, please see the YARD documentation.

### Architecture
**Note:** Some of the architecture commands begin with an underscore (`_`) because Ruby does not permit methods to start with a numeric.

- `_64_bit?`
- `_32_bit?`
- `intel?`
- `sparc?`
- `ppc64?`
- `ppc64le?`
- `powerpc?`

#### Examples
```ruby
execute 'build[my binary]' do
  command '...'
  not_if  { _64_bit? }
end
```

### Cloud
- `azure?`
- `cloud?`
- `digitalocean?`
- `ec2?`
- `eucalyptus?`
- `gce?`
- `linode?`
- `openstack?`
- `cloudstack?`
- `rackspace?`

#### Examples
```ruby
template '/tmp/config' do
  variables(
    # See also: best_ip_for
    ipaddress: cloud? ? node['local_ipv4'] : node['public_ipv4']
  )
end
```

### Core Extensions
**Note:** Core extensions are **not** included by default. You must require the `chef/sugar/core_extensions` module manually to gain access to these APIs:

```ruby
require 'chef/sugar/core_extensions'
```

- `String#satisfies?`
- `String#satisfied_by?`
- `Array#satisfied_by?`
- `Object#blank?`

#### Examples
```ruby
# Checking version constraints
'1.0.0'.satisfies?('~> 1.0') #=> true
'~> 1.0'.satisfied_by?('1.0') #=> true
```

```ruby
# Check for an object's presence
''.blank? #=> true
['hello'].blank? #=> false
```

### Data Bag
- `encrypted_data_bag_item` - a handy DSL method for loading encrypted data bag items the same way you load a regular data bag item; this requires `Chef::Config[:encrypted_data_bag_secret]` is set!
- `encrypted_data_bag_item_for_environment` - find the encrypted data bag entry for the current node's Chef environment.
- `data_bag_item_for_environment` - find the data bag entry for the current node's Chef environment.

#### Examples
```ruby
encrypted_data_bag_item('accounts', 'hipchat')
```

```ruby
encrypted_data_bag_item_for_environment('accounts', 'github')
```

```ruby
data_bag_item_for_environment('accounts', 'github')
```

### Docker
Chef Sugar looks for hints to see if the node being converged is a Docker container. When [Ohai supports checking other nodes](https://github.com/opscode/ohai/pull/428), Chef Sugar will automatically pick up the information.

- `docker?`

#### Examples
```ruby
template '/runme' do
  only_if { docker?(node) }
end
```

### Attributes
Chef Sugar adds more Chef-like DSL to attribute definitions. Instead of using the Ruby hash syntax, you can define attributes using nested namespaces. This DSL may be more friendly to non-Ruby developers. It can safely be mixed-and-matched with the standard syntax.

```ruby
# This is functionally the same as default['apache2']['config']['root'] = '/var/www'
namespace 'apache2' do
  namespace 'config' do
    root '/var/www'
  end
end
```

```ruby
# Specify multiple keys instead of nesting namespaces
namespace 'apache2', 'config' do
  root '/var/www'
end
```

```ruby
# Specify different nested precedence levels
namespace 'apache2', precedence: normal do
  namespace 'config', precedence: override do
    root '/var/www' #=> override['apache2']['config']['root'] = '/var/www'
  end
end
```

### Constraints
- `constraints` - create a new constraint (or requirement) that can be used to test version validations.
- `chef_version` - (DSL only) a wrapper for `version(Chef::VERSION)`
- `version` - create a new version that can be used to test constraint validation.

#### Examples
```ruby
# Check if a version is satisfied by a constraint
version('1.2.3').satisfies?('~> 1.2.0')
```

```ruby
# Check if a constraint is satisfied by a version
constraint('~> 1.2.0').satisfied_by?('1.2.3')
```

```ruby
# Support multiple constraints
version('1.2.3').satisfies?('> 1.2', '< 2.0')
constraint('> 1.2', '< 2.0').satisfied_by?('1.2.3')
```

```ruby
# Only perform an operation if Chef is at a certain version
package 'apache2' do
  not_if { chef_version.satisfies?('~> 11.0') } # Ignore Chef 11
end
```

### Kernel
- `require_chef_gem` - "safely" require a gem. Loading a gem with Chef is sometimes difficult and confusing. The errors that Chef produces are also sometimes not very intuitive. In the event you require a gem to exist on the system, you can use `require_chef_gem`, which will attempt to require the gem and then produce helpful output if the gem is not installed:

        Chef could not load the gem `#{name}'! You may need to install the gem
        manually with `gem install #{name}', or include a recipe before you can
        use this resource. Please consult the documentation for this cookbook
        for proper usage.

#### Examples
```ruby
# LWRP
require_chef_gem 'pry'
```

```ruby
class Chef
  class Provider
    class MyProvider > Provider
      require_chef_gem 'pry'
    end
  end
end
```

### Init
- `systemd?` - detect if init system is systemd
- `upstart?` - detect if init system is upstart
- `runit?` - detect if init system is runit

#### Examples
```ruby
systemd_service 'my-service' do
  description 'My Service'
  install do
    wanted_by 'multi-user.target'
  end
  service do
    exec_start '/usr/bin/myserviced'
  end
  action [:create, :enable, :start]
  only_if { systemd? }
end

cookbook_file '/etc/init/my-service.conf' do
  source 'my-service.conf'
  only_if { upstart? }
end
```

### IP
- `best_ip_for` - determine the best IP address for the given "other" node, preferring local IP addresses over public ones.

#### Examples
```ruby
redis = search('node', 'role:redis').first

template '/tmp/config' do
  variables(
    ipaddress: best_ip_for(redis)
  )
end
```

### Node

Additional methods for the `node` object

- `deep_fetch` - safely fetch a nested attribute.
- `deep_fetch!` - fetch a nested attribute, raising a more semantic error if the key does not exist.
- `in?` - determine if the node is in the given Chef environment.

#### Examples
```ruby
credentials = if node.in?('production')
                Chef::EncryptedDataBag.new('...')
              else
                data_bag('...')
              end
```

```ruby
node.deep_fetch('apache2', 'config', 'root') => node['apache2']['config']['root']
```

### Platform
- `amazon_linux?`
- `centos?`
- `linux_mint?`
- `oracle_linux?`
- `redhat_enterprise_linux?`
- `scientific_linux?`
- `ubuntu?`
- `solaris2?`
- `aix?`
- `smartos?`
- `omnios?`
- `raspbian?`
- `nexus?`
- `ios_xr?`

There are also a series of dynamically defined matchers that map named operating system release versions and comparison operators in the form "#{platform}\_#{operator}\_#{name}?". For example:

- `debian_after_squeeze?`
- `linuxmint_after_or_at_olivia?`
- `mac_os_x_lion?`
- `ubuntu_before_lucid?`
- `ubuntu_before_or_at_maverick?`
- `solaris_10?`
- `solaris_11?`

To get a full list, run the following in IRB:

```ruby
require 'chef/sugar'
puts Chef::Sugar::Platform.instance_methods
```

#### Examples
```ruby
if ubuntu?
  execute 'apt-get update'
end
```

### Platform Family
- `arch_linux?`
- `debian?`
- `fedora?`
- `freebsd?`
- `gentoo?`
- `linux?`
- `mac_os_x?`
- `openbsd?`
- `rhel?`
- `slackware?`
- `suse?`
- `windows?`
- `wrlinux?`

#### Examples
```ruby
node['attribute'] = if windows?
                      'C:\Foo\BarDrive'
                    else
                      '/foo/bar_drive'
                    end
```

### Ruby
**Note:** The applies to the Ruby found at `node['languages']['ruby']`.

- `ruby_20?`
- `ruby_19?`

#### Examples
```ruby
log 'This has been known to fail on Ruby 2.0' if ruby_20?
```

### Run Context
- `includes_recipe?` - determines if the current run context includes the recipe

```ruby
if includes_recipe?('apache2::default')
  apache_module 'my_module' do
    # ...
  end
end
```

### Shell
- `which`
- `dev_null`
- `installed?`
- `installed_at_version?`
- `version_for`

#### Examples
```ruby
log "Using `mongo` at `#{which('mongo')}`"

if installed?('apt')
  execute 'apt-get update'
end

execute 'install[thing]' do
  command "... 2>&1 #{dev_null}"
  not_if  { installed_at_version?('thing', node['thing']['version']) }
end

log "Skipping git install, version is at #{version_for('mongo', '-v')}"
```

### Vagrant
- `vagrant?`

#### Examples
```ruby
http_request 'http://...' do
  not_if { vagrant? }
end
```

### Virtualization
- `kvm?`
- `lxc?`
- `virtualbox?`
- `vmware?`
- `openvz?`

#### Examples
```ruby
service 'ntpd' do
  action [:enable, :start]
  not_if { lxc? }
end
```

### Filters
- `at_compile_time` - accepts a block of resources to run at compile time
- `before` - insert resource in the collection before the given resource
- `after` - insert resource in the collection after the given resource

#### Examples
```ruby
at_compile_time do
  package 'apache2'
end

# This is equivalent to
package 'apache2' do
  action :nothing
end.run_action(:install)
```

```ruby
before 'service[apache2]' do
  log 'I am before the apache 2 service fires!'
end
```

```ruby
after 'service[apache2]' do
  log 'I am after the apache 2 service fires!'
end
```


License & Authors
-----------------
- Author: Seth Vargo (sethvargo@gmail.com)

```text
Copyright 2013-2015 Seth Vargo

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
# build-essential Cookbook

[![Cookbook Version](http://img.shields.io/cookbook/v/build-essential.svg)][cookbook] [![Build Status](https://travis-ci.org/chef-cookbooks/build-essential.svg?branch=master)](https://travis-ci.org/chef-cookbooks/build-essential)

Installs packages required for compiling C software from source. Use this cookbook if you wish to compile C programs, or install RubyGems with native extensions. Contains a resource, 'build_essential', as as well as a default recipe that simply calls that same resource.

## Requirements

### Platforms

- Debian/Ubuntu
- RHEL/CentOS/Scientific/Amazon/Oracle
- openSUSE / SUSE Enterprise Linux
- SmartOS
- Fedora
- Mac OS X
- FreeBSD

### Chef

- Chef 12.1+

### Cookbooks

- seven_zip
- mingw

**Note for Debian platform family:** On Debian platform-family systems, it is recommended that `apt-get update` be run, to ensure that the package cache is updated. It's not in the scope of this cookbook to do that, as it can [create a duplicate resource](https://tickets.chef.io/browse/CHEF-3694). We recommend using the [apt](https://supermarket.chef.io/cookbooks/apt) cookbook to do this.

## Attributes

Attribute                                    |             Default             | Description
-------------------------------------------- | :-----------------------------: | --------------------------------------------------------------
`node['build-essential']['compile_time']`    |             `false`             | Execute resources at compile time
`node['build-essential']['msys2']['path']`   | `#{ENV['SYSTEMDRIVE']\\msys2`   | Destination for msys2 build tool chain (Windows only)

## Usage

### Recipe Usage

The recipe simply calls the build_essential resource, but it ideal for adding to roles or node run lists.

Include the build-essential recipe in your run list:

```sh
knife node run_list add NODE "recipe[build-essential::default]"
```

or add the build-essential recipe as a dependency and include it from inside another cookbook:

```ruby
include_recipe 'build-essential::default'
```

### Gems with C extensions

For RubyGems that include native C extensions you wish to use with Chef, you should do the following.

- Set the `compile_time` attribute to true in your wrapper cookbook or role:

  ```ruby
   # Wrapper attribute
   default['build-essential']['compile_time'] = true
  ```

  ```ruby
   # Role
   default_attributes(
     'build-essential' => {
       'compile_time' => true
     }
   )
  ```

- Ensure that the C libraries, which include files and other assorted "dev"

  type packages, are installed in the compile phase after the build-essential

  recipe is executed. For example:

  ```ruby
   include_recipe 'build-essential::default'

   package('mypackage-devel') { action :nothing }.run_action(:install)
  ```

- Use the `chef_gem` resource in your recipe to install the gem with the native

  extension:

  ```ruby
   chef_gem 'gem-with-native-extension'
  ```

### Resource Usage

The cookbook includes a resource 'build_essential' that can be included in your cookbook to install the necessary build-essential packages

Simple package installation during the client run:

```ruby
build_essential 'some name you choose'
```

Package installation during the compile phase:

```ruby
build_essential 'some name you choose' do
  compile_time false
end
```

## License & Authors

**Author:** Cookbook Engineering Team ([cookbooks@chef.io](mailto:cookbooks@chef.io))

**Copyright:** 2009-2015, Chef Software, Inc.

```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

[cookbook]: https://supermarket.chef.io/cookbooks/build-essential
[travis]: http://travis-ci.org/chef-cookbooks/build-essential
# yum-epel Cookbook
[![Build Status](https://travis-ci.org/chef-cookbooks/yum-epel.svg?branch=master)](http://travis-ci.org/chef-cookbooks/yum-epel) [![Cookbook Version](https://img.shields.io/cookbook/v/yum-epel.svg)](https://supermarket.chef.io/cookbooks/yum-epel)

Extra Packages for Enterprise Linux (or EPEL) is a Fedora Special Interest Group that creates, maintains, and manages a high quality set of additional packages for Enterprise Linux, including, but not limited to, Red Hat Enterprise Linux (RHEL), CentOS and Scientific Linux (SL), Oracle Linux (OL).

The yum-epel cookbook takes over management of the default repositoryids shipped with epel-release. It allows attribute manipulation of `epel`, `epel-debuginfo`, `epel-source`, `epel-testing`, `epel-testing-debuginfo`, and `epel-testing-source`.

## Requirements
### Platforms
- RHEL/CentOS and derivatives

### Chef
- Chef 11+

### Cookbooks
- yum version 3.6.3 or higher

## Attributes
The following attributes are set by default

```ruby
default['yum-epel']['repositories'] = %w{epel epel-debuginfo epel-source epel-testing epel-testing-debuginfo epel-testing-source}
```

```ruby
default['yum']['epel']['repositoryid'] = 'epel'
default['yum']['epel']['description'] = 'Extra Packages for Enterprise Linux 6 - $basearch'
default['yum']['epel']['mirrorlist'] = 'http://mirrors.fedoraproject.org/mirrorlist?repo=epel-5&arch=$basearch'
default['yum']['epel']['gpgkey'] = 'http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6'
default['yum']['epel']['failovermethod'] = 'priority'
default['yum']['epel']['gpgcheck'] = true
default['yum']['epel']['enabled'] = true
default['yum']['epel']['managed'] = true
```

```ruby
default['yum']['epel-debuginfo']['repositoryid'] = 'epel-debuginfo'
default['yum']['epel-debuginfo']['description'] = 'Extra Packages for Enterprise Linux 6 - $basearch - Debug'
default['yum']['epel-debuginfo']['mirrorlist'] = 'https://mirrors.fedoraproject.org/metalink?repo=epel-debug-6&arch=$basearch'
default['yum']['epel-debuginfo']['gpgkey'] = 'http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6'
default['yum']['epel-debuginfo']['failovermethod'] = 'priority'
default['yum']['epel-debuginfo']['gpgcheck'] = true
default['yum']['epel-debuginfo']['enabled'] = false
default['yum']['epel-debuginfo']['managed'] = false
```

```ruby
default['yum']['epel-source']['repositoryid'] = 'epel-source'
default['yum']['epel-source']['description'] = 'Extra Packages for Enterprise Linux 6 - $basearch - Source'
default['yum']['epel-source']['mirrorlist'] = 'http://mirrors.fedoraproject.org/mirrorlist?repo=epel-source-6&arch=$basearch'
default['yum']['epel-source']['gpgkey'] = 'http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6'
default['yum']['epel-source']['failovermethod'] = 'priority'
default['yum']['epel-source']['gpgcheck'] = true
default['yum']['epel-source']['enabled'] = false
default['yum']['epel-source']['managed'] = false
```

```ruby
default['yum']['epel-testing']['repositoryid'] = 'epel-testing'
default['yum']['epel-testing']['description'] = 'Extra Packages for Enterprise Linux 6 - Testing - $basearch'
default['yum']['epel-testing']['mirrorlist'] = 'https://mirrors.fedoraproject.org/metalink?repo=testing-epel6&arch=$basearch'
default['yum']['epel-testing']['gpgkey'] = 'http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6r'
default['yum']['epel-testing']['failovermethod'] = 'priority'
default['yum']['epel-testing']['gpgcheck'] = true
default['yum']['epel-testing']['enabled'] = false
default['yum']['epel-testing']['managed'] = false
```

```ruby
default['yum']['epel-testing-debuginfo']['repositoryid'] = 'epel-testing-debuginfo'
default['yum']['epel-testing-debuginfo']['description'] = 'Extra Packages for Enterprise Linux 6 - Testing - $basearch Debug'
default['yum']['epel-testing-debuginfo']['mirrorlist'] = 'https://mirrors.fedoraproject.org/metalink?repo=testing-debug-epel6&arch=$basearch'
default['yum']['epel-testing-debuginfo']['gpgkey'] = 'http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6'
default['yum']['epel-testing-debuginfo']['failovermethod'] = 'priority'
default['yum']['epel-testing-debuginfo']['gpgcheck'] = true
default['yum']['epel-testing-debuginfo']['enabled'] = false
default['yum']['epel-testing-debuginfo']['managed'] = false
```

```ruby
default['yum']['epel-testing-source']['repositoryid'] = 'epel-testing-source'
default['yum']['epel-testing-source']['description'] = 'Extra Packages for Enterprise Linux 6 - Testing - $basearch Source'
default['yum']['epel-testing-source']['mirrorlist'] = 'https://mirrors.fedoraproject.org/metalink?repo=testing-source-epel6&arch=$basearch'
default['yum']['epel-testing-source']['gpgkey'] = 'http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6'
default['yum']['epel-testing-source']['failovermethod'] = 'priority'
default['yum']['epel-testing-source']['gpgcheck'] = true
default['yum']['epel-testing-source']['enabled'] = false
default['yum']['epel-testing-source']['managed'] = false
```

## Recipes
- default - Walks through node attributes and feeds a yum_resource
- parameters. The following is an example a resource generated by the
- recipe during compilation.

```ruby
  yum_repository 'epel' do
    mirrorlist 'http://mirrors.fedoraproject.org/mirrorlist?repo=epel-5&arch=$basearch'
    description 'Extra Packages for Enterprise Linux 5 - $basearch'
    enabled true
    gpgcheck true
    gpgkey 'http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL'
  end
```

## Usage Example
To disable the epel repository through a Role or Environment definition

```
default_attributes(
  :yum => {
    :epel => {
      :enabled => {
        false
       }
     }
   }
 )
```

Uncommonly used repositoryids are not managed by default. This is speeds up integration testing pipelines by avoiding yum-cache builds that nobody cares about. To enable the epel-testing repository with a wrapper cookbook, place the following in a recipe:

```ruby
node.default['yum']['epel-testing']['enabled'] = true
node.default['yum']['epel-testing']['managed'] = true
include_recipe 'yum-epel'
```

## More Examples
Point the epel repositories at an internally hosted server.

```ruby
node.default['yum']['epel']['enabled'] = true
node.default['yum']['epel']['mirrorlist'] = nil
node.default['yum']['epel']['baseurl'] = 'https://internal.example.com/centos/6/os/x86_64'
node.default['yum']['epel']['sslverify'] = false

include_recipe 'yum-epel'
```

## License & Authors
**Author:** Cookbook Engineering Team ([cookbooks@chef.io](mailto:cookbooks@chef.io))

**Copyright:** 2011-2016, Chef Software, Inc.

```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
[![Cookbook Version](http://img.shields.io/cookbook/v/seven_zip.svg)](https://supermarket.chef.io/cookbooks/seven_zip)
[![Build Status](https://secure.travis-ci.org/daptiv/seven_zip.svg?branch=master)](http://travis-ci.org/daptiv/seven_zip)

seven_zip Cookbook
==============
[7-Zip](http://www.7-zip.org/) is a file archiver with a high compression ratio. This cookbook installs the full 7-zip suite of tools (GUI and CLI). This cookbook replaces the older [7-zip cookbook](https://github.com/sneal/7-zip).


Requirements
------------
### Platforms
- Windows XP
- Windows Vista
- Windows Server 2003 R2
- Windows 7
- Windows Server 2008 (R1, R2)
- Windows 8, 8.1
- Windows Server 2012 (R1, R2)

### Chef
- Chef >= 11.6

### Cookbooks
- windows


Attributes
----------
- (optional) `node['seven_zip']['home']` - specify location for 7-zip installation.
- (optional) `node['seven_zip']['syspath']` - if true, adds 7-zip directory to system path.

Resource/Provider
-----------------
### seven_zip_archive

Extracts a 7-zip compatible archive (iso, zip, 7z etc) to the specified destination directory.

#### Actions
- `:extract` - Extract a 7-zip compatible archive

#### Attribute Parameters
- `path` - Name attribute. The destination to extract to.
- `source` - The file path to the archive to extract.
- `overwrite` - Defaults to false. If true, the destination files will be overwritten.
- `checksum` - The archive file checksum.

#### Examples
Extract 7-zip source files to `C:\seven_zip_source`.

```ruby
seven_zip_archive 'seven_zip_source' do
  path      'C:\seven_zip_source'
  source    'http://www.7-zip.org/a/7z1514-src.7z'
  overwrite true
  checksum  '3713aed72728eae8f6649e4803eba0b3676785200c76df6269034c520df4bbd5'
end
```

Usage
-----
### default
Downloads and installs 7-zip.

License & Authors
-----------------
- Author:: Seth Chisamore (<schisamo@chef.io>)
- Author:: Shawn Neal (<sneal@sneal.net>)

```text
Copyright:: 2011-2016, Chef Software, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
# compat_resource cookbook

[![Build Status](https://travis-ci.org/chef-cookbooks/compat_resource.svg?branch=master)](https://travis-ci.org/chef-cookbooks/compat_resource)
[![Cookbook Version](https://img.shields.io/cookbook/v/compat_resource.svg)](https://supermarket.chef.io/cookbooks/compat_resource)


This cookbook brings the custom resource syntax from Chef 12.5 to earlier Chef 12.X releases.

## Converting cookbooks from the old resource model to the new

### Boilerplate

1. Depend on compat_resource
   - Descend resources from ChefCompat::Resource
   - Set resource_name in the class instead of the constructor
2. Convert Attributes to Properties
   - Rename attribute -> property
   - Move set_or_return -> property
   - Take kind_of/equal_to/regexes and make them types
   - Use true/false/nil instead of TrueClass/FalseClass/NilClass
   - Remove default: nil (it's the default)
3. Convert Top-Level Providers to Actions
   - Create any resources that don't already exist (for example in
     multi-provider cases) and descend from the base resource
   - Remove allowed_actions / @actions
   - @action -> default_action
   - Move `provides` and `action :x` to the resource
   - Remove use_inline_resources and def whyrun_safe?
   - Move other methods to `action_class.class_eval do`

Now you have everything in a resource, are using properties, and have gotten rid
of a bunch of boilerplate. Of course, this is just getting it *moved*. Now you
can start to really use the new features. And if you're making resources for
the first time, congrats--you probably didn't have to do very much of this :)

### Advanced Concepts

1. Resource Inheritance
2. Resources That Are Different On Each OS?
3. Coercion: Handling User Input
4. Lazy Defaults
5. Using Load Current Resource
6. Using Converge If Changed
7. Defaults Are For Creation
8. Shared types: using a type multiple places



Requirements
------------
#### Platforms
- All platforms supported by Chef

#### Chef
- Chef 12.0+

#### Cookbooks
- none


## Usage

To use this cookbook, put `depends 'compat_resource'` in the metadata.rb of your cookbook. Once this is done, you can use all the new custom resource features to define resources. It Just Works.

For example, if you create resources/myresource.rb, myresource can use `property`, `load_current_value` and `action` (no need to create a provider). If you want to create Resource classes directly, extend from `ChefCompat::Resource` instead of `Chef::Resource`. Properties, current value loading, converge_if_changed, and resource_name will all function the same across versions.

## Custom Resources?

Curious about how to use custom resources? Here are the 12.5 docs:

- Docs: https://docs.chef.io/custom_resources.html
- Slides: https://docs.chef.io/decks/custom_resources.html


##License & Authors

**Author:** John Keiser (<jkeiser@chef.io>)

**Copyright:** 2015, Chef Software, Inc.
```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
# chef_handler Cookbook
[![Build Status](https://travis-ci.org/chef-cookbooks/chef_handler.svg?branch=master)](https://travis-ci.org/chef-cookbooks/chef_handler) [![Cookbook Version](https://img.shields.io/cookbook/v/chef_handler.svg)](https://supermarket.chef.io/cookbooks/chef_handler)

Creates a configured handler path for distributing [Chef report and exception handlers](http://docs.chef.io/handlers.html).  Also exposes an LWRP for enabling Chef handlers from within recipe code (as opposed to hard coding in the client.rb file).  This is useful for cookbook authors who may want to ship a product specific handler (see the `cloudkick` cookbook for an example) with their cookbook.

## Requirements
### Platforms
- Debian/Ubuntu
- RHEL/CentOS/Scientific/Amazon/Oracle
- Windows

### Chef
- Chef 11+

### Cookbooks
- none

## Attributes
`node['chef_handler']['handler_path']` - location to drop off handlers directory, default is a folder named 'handlers' in Chef's file cache directory

## Custom Resources
### chef_handler
Requires, configures and enables handlers on the node for the current Chef run.  Also has the ability to pass arguments to the handlers initializer.  This allows initialization data to be pulled from a node's attribute data.

It is best to declare `chef_handler` resources early on in the compile phase so they are available to fire for any exceptions during the Chef run.  If you have a base role you would want any recipes that register Chef handlers to come first in the run_list.

#### Actions
- `:enable:` Enables the Chef handler for the current Chef run on the current node
- `:disable:` Disables the Chef handler for the current Chef run on the current node

#### Attribute Parameters
- `class_name:` name attribute. The name of the handler class (can be module name-spaced).
- `source:` full path to the handler file.  can also be a gem path if the handler ships as part of a Ruby gem.  can also be nil, in which case the file must be loaded as a library.
- `arguments:` an array of arguments to pass the handler's class initializer
- `supports:` type of Chef Handler to register as, i.e. :report, :exception or both. default is `:report => true, :exception => true`

#### Example

```ruby
    # register the Chef::Handler::JsonFile handler
    # that ships with the Chef gem
    chef_handler "Chef::Handler::JsonFile" do
      source "chef/handler/json_file"
      arguments :path => '/var/chef/reports'
      action :enable
    end

    # do the same but during the compile phase
    chef_handler "Chef::Handler::JsonFile" do
      source "chef/handler/json_file"
      arguments :path => '/var/chef/reports'
      action :nothing
    end.run_action(:enable)

    # handle exceptions only
    chef_handler "Chef::Handler::JsonFile" do
      source "chef/handler/json_file"
      arguments :path => '/var/chef/reports'
      supports :exception => true
      action :enable
    end


    # enable the CloudkickHandler which was
    # dropped off in the default handler path.
    # passes the oauth key/secret to the handler's
    # intializer.
    chef_handler "CloudkickHandler" do
      source "#{node['chef_handler']['handler_path']}/cloudkick_handler.rb"
      arguments [node['cloudkick']['oauth_key'], node['cloudkick']['oauth_secret']]
      action :enable
    end

    # enable the MyCorp::MyLibraryHandler handler which was dropped off in a
    # standard chef library file.
    chef_handler "MyCorp::MyLibraryHandler" do
      action :enable
    end
```

## Usage
### default
Put the recipe `chef_handler` at the start of the node's run list to make sure that custom handlers are dropped off early on in the Chef run and available for later recipes.

For information on how to write report and exception handlers for Chef, please see the Chef wiki pages: [https://docs.chef.io/handlers.html](https://docs.chef.io/handlers.html)

### json_file
Leverages the `chef_handler` LWRP to automatically register the `Chef::Handler::JsonFile` handler that ships as part of Chef. This handler serializes the run status data to a JSON file located at `/var/chef/reports`.

## Unit Testing
chef_handler provides built in [chefspec](https://github.com/sethvargo/chefspec) matchers for assisting unit tests. These matchers will only be loaded if chefspec is already loaded. Following is an example of asserting against the jsonfile handler:

```ruby
  expect(runner).to enable_chef_handler("Chef::Handler::JsonFile").with(
    source: "chef/handler/json_file",
    arguments: { :path => '/var/chef/reports'},
    supports: {:exception => true}
    )
  end
```

## License & Authors
**Author:** Cookbook Engineering Team ([cookbooks@chef.io](mailto:cookbooks@chef.io))

**Copyright:** 2011-2016, Chef Software, Inc.

```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
This directory contains Chef handlers to distribute to your nodes.
# Git Cookbook
[![Build Status](https://travis-ci.org/chef-cookbooks/git.svg?branch=master)](https://travis-ci.org/chef-cookbooks/git) [![Cookbook Version](https://img.shields.io/cookbook/v/git.svg)](https://supermarket.chef.io/cookbooks/git)


Installs git_client from package or source. Optionally sets up a git service under xinetd.

## Scope
This cookbook is concerned with the Git SCM utility. It does not address ecosystem tooling or related projects.

## Requirements
### Platforms
The following platforms have been tested with Test Kitchen:

```
|--------------+-------|
| centos-5     | X     |
|--------------+-------|
| centos-6     | X     |
|--------------+-------|
| centos-7     | X     |
|--------------+-------|
| fedora-23    | X     |
|--------------+-------|
| debian-7     | X     |
|--------------+-------|
| debian-8     | X     |
|--------------+-------|
| ubuntu-12.04 | X     |
|--------------+-------|
| ubuntu-14.04 | X     |
|--------------+-------|
| ubuntu-16.04 | X     |
|--------------+-------|
```

### Chef
- Chef 11+

### Cookbooks
- depends 'build-essential' - For compiling from source
- depends 'dmg' - For OSX Support
- depends 'windows' - For Windows support
- depends 'yum-epel' - For older RHEL platform_family support

## Usage
- Add `git::default`, `git::source` or `git::windows` to your run_list
- OR
- Add `depends 'git', '~> 4.3'` to your cookbook's metadata.rb
- include_recipe one of the recipes from your cookbook
- OR
- Use the git_client resource directly, the same way you'd use core
- Chef resources (file, template, directory, package, etc).

## Resources Overview
- `git_client`: Manages a Git client installation on a machine. Acts
  as a singleton when using the (default) package provider. Source
  provider available as well.

- `git_service`: Sets up a Git service via xinetd. WARNING: This is
  insecure and will probably be removed in the future

- `git_config`: Sets up Git configuration on a node.

### git_client
The `git_client` resource manages the installation of a Git client on a machine.

#### Example

```
git_client 'default' do
  action :install
end
```

### git_config
The `git_config` resource manages the configuration of Git client on a
machine.

#### Example

``` ruby
git_config 'url.https://github.com/.insteadOf' do
  value 'git://github.com/'
  scope 'system'
  options '--add'
end
```

#### Properties
Currently, there are distinct sets of resource properties, used by the providers for source, package, osx, and windows.

# used by linux package providers
- `package_name` - Package name to install on Linux machines. Defaults to a calculated value based on platform.
- `package_version` - Defaults to nil.
- `package_action` - Defaults to `:install`

# used by source providers
- `source_prefix` - Defaults to '/usr/local'
- `source_url` - Defaults to a calculated URL based on source_version
- `source_version` - Defaults to 2.7.4
- `source_use_pcre` - configure option for build. Defaults to false
- `source_checksum` - Defaults to a known value for the 2.7.4 source tarball

# used by OSX package providers
- `osx_dmg_app_name` - Defaults to 'git-2.7.1-intel-universal-mavericks'
- `osx_dmg_package_id` - Defaults to 'GitOSX.Installer.git271.git.pkg'
- `osx_dmg_volumes_dir` - Defaults to 'Git 2.7.1 Mavericks Intel Universal'
- `osx_dmg_url` - Defaults to Sourceforge
- `osx_dmg_checksum` - Defaults to the value for 2.7.1

# used by the Windows package providers
- `windows_display_name` - Windows display name
- `windows_package_url` - Defaults to the Internet
- `windows_package_checksum` - Defaults to the value for 2.7.4

## Recipes
This cookbook ships with ready to use, attribute driven recipes that utilize the `git_client` and `git_service` resources. As of cookbook 4.x, they utilize the same attributes layout scheme from the 3.x. Due to some overlap, it is currently impossible to simultaneously install the Git client as a package and from source by using the "manipulate a the node attributes and run a recipe" technique. If you need both, you'll need to utilize the git_client resource in a recipe.

## Attributes
### Windows
- `node['git']['version']` - git version to install
- `node['git']['url']` - URL to git package
- `node['git']['checksum']` - package SHA256 checksum
- `node['git']['display_name']` - `windows_package` resource Display Name (makes the package install idempotent)

### Mac OS X
- `node['git']['osx_dmg']['url']` - URL to git package
- `node['git']['osx_dmg']['checksum']` - package SHA256 checksum

### Linux
- `node['git']['prefix']` - git install directory
- `node['git']['version']` - git version to install
- `node['git']['url']` - URL to git tarball
- `node['git']['checksum']` - tarball SHA256 checksum
- `node['git']['use_pcre']` - if true, builds git with PCRE enabled

## License & Authors
- Author:: Joshua Timberman ([joshua@chef.io](mailto:joshua@chef.io))
- Author:: Sean OMeara ([sean@chef.io](mailto:sean@chef.io))
- Copyright:: 2009-2016, Chef Software, Inc.

```
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
# languages

Resources to install compilers and other support for various languages.

# Using Test Kitchen with Docker

The following assumes you are on a Mac OS X workstation and have installed and
started [Kitematic](https://kitematic.com/).

* Install [kitchen-docker](https://github.com/portertech/kitchen-docker) into your local ChefDK install:
```
$ chef gem install kitchen-docker
Successfully installed kitchen-docker-2.3.0
1 gem installed
```

* Set environment variables to point kitchen-docker at your local Kitematic instance:
```
# Bash
export DOCKER_HOST=tcp://192.168.99.100:2376
export DOCKER_CERT_PATH=$HOME/.docker/machine/certs
export DOCKER_TLS_VERIFY=1

# Fish
set -gx DOCKER_HOST "tcp://192.168.99.100:2376"
set -gx DOCKER_CERT_PATH "$HOME/.docker/machine/certs"
set -gx DOCKER_TLS_VERIFY 1
```

* Run Test Kitchen with the provided `.kitchen.docker.yml`:
```
KITCHEN_LOCAL_YAML=.kitchen.docker.yml kitchen verify languages-ruby-ubuntu-1204
```
# freebsd Cookbook
[![Build Status](https://travis-ci.org/chef-cookbooks/freebsd.svg?branch=master)](http://travis-ci.org/chef-cookbooks/freebsd) [![Cookbook Version](https://img.shields.io/cookbook/v/freebsd.svg)](https://supermarket.chef.io/cookbooks/freebsd)

Sets up ports and pkgng on FreeBSD systems

## Requirements
### Platforms
- FreeBSD 9/10

### Chef
- Chef 11+

### Cookbooks
- none

## Attributes

Attribute                                 | Default | Description
----------------------------------------- | ------- | ------------------------------------------
`node['freebsd']['compiletime_portsnap']` | `false` | Execute portsnap resources at compile time

## Supported Versions
This cookbook will support stable and release [versions](https://www.freebsd.org/security/index.html#sup) of the FreeBSD Platform. More information on this subject can be found at [issue23](https://github.com/chef-cookbooks/freebsd/issues/23).

## Usage
### freebsd::pkgng
This recipe ensures `pkg` (aka `pkgng`), FreeBSD's next generation package management tool, is installed and configured.

This recipe is only useful on FreeBSD versions before 10 as `pkg` ships in the base install of FreeBSD 10+. That being said the recipe is safe to include on the runlists of FreeBSD 10 nodes and will mostly operate in a no-op mode.

### freebsd::portsnap
This recipe ensures the Ports Collection collection is fully up to date.

This recipe should appear first in the run list of FreeBSD nodes to ensure that the package cache is up to date before managing any `package` resources with Chef.

## Resources/Providers
### port_options
Provides an easy way to set port options from within a cookbook.

It can be used in two different ways:
- template-based: specifying a source will write it to the correct destination with no change;
- options hash: if a options hash is passed instead, it will be merged on top of default and current options, and the result will be written back.

Note that the options hash take simple options names as keys and a boolean as value; when saving to file, this is converted to the format that FreeBSD ports expect:

Option Key Name | Option Value | Options File
--------------- | ------------ | -------------------
APACHE          | true         | WITH_APACHE=true
APACHE          | false        | WITHOUT_APACHE=true

#### Actions

Action | Description                                                 | Default
------ | ----------------------------------------------------------- | -------
create | create the port options file according to the given options | Yes

#### Attributes

Attribute | Description
--------- | ---------------------------------------------------------------------------------------------------------------
name      | The name of the port whose options file you want to manipulate;
source    | if the attribute is set, it will be used to look up a template, which will then be saved as a port options file
options   | a hash with the option name as the key, and a boolean as value.

#### Examples

```ruby
# freebsd-php5-options will be written out as /var/db/ports/php5/options
freebsd_port_options "php5" do
  source "freebsd-php5-options.erb"
  action :create
end

# Default options will be read from /usr/ports/lang/php5;
# current options from /var/db/ports/php5/options (if exists);
# the APACHE options will be set to true, the others will be unchanged
freebsd_port_options "php5" do
  options "APACHE" => true
  action :create
end
```

## License & Authors
- Author: Andrea Campi ([andrea.campi@zephirworks.com](mailto:andrea.campi@zephirworks.com))
- Author: Seth Chisamore ([schisamo@chef.io](mailto:schisamo@chef.io))

```text
Copyright 2010-2012, ZephirWorks
Copyright 2012-2015, Chef Software, Inc. (<legal@chef.io>)

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
# Windows Cookbook

[![Build Status](https://travis-ci.org/chef-cookbooks/windows.svg?branch=master)](http://travis-ci.org/chef-cookbooks/windows) [![Cookbook Version](https://img.shields.io/cookbook/v/windows.svg)](https://supermarket.chef.io/cookbooks/windows)

Provides a set of Windows-specific primitives (Chef resources) meant to aid in the creation of cookbooks/recipes targeting the Windows platform.

## Requirements

### Platforms

- Windows Vista
- Windows 7
- Windows Server 2008 (R1, R2)
- Windows 8, 8.1
- Windows Server 2012 (R1, R2)

### Chef

- Chef 11+

### Cookbooks

- chef_handler (`windows::reboot_handler` leverages the chef_handler LWRP)

## Attributes

- `node['windows']['allow_pending_reboots']` - used to configure the `WindowsRebootHandler` (via the `windows::reboot_handler` recipe) to act on pending reboots. default is true (ie act on pending reboots). The value of this attribute only has an effect if the `windows::reboot_handler` is in a node's run list.
- `node['windows']['allow_reboot_on_failure']` - used to register the `WindowsRebootHandler` (via the `windows::reboot_handler` recipe) as an exception handler too to act on reboots not only at the end of successful Chef runs, but even at the end of failed runs. default is false (ie reboot only after successful runs). The value of this attribute only has an effect if the `windows::reboot_handler` is in a node's run list.

## Resource/Provider

### windows_auto_run

#### Actions

- `:create` - Create an item to be run at login
- `:remove` - Remove an item that was previously setup to run at login

#### Attribute Parameters

- `name` - Name attribute. The name of the value to be stored in the registry
- `program` - The program to be run at login
- `args` - The arguments for the program

#### Examples

Run BGInfo at login

```ruby
windows_auto_run 'BGINFO' do
  program 'C:/Sysinternals/bginfo.exe'
  args    '\'C:/Sysinternals/Config.bgi\' /NOLICPROMPT /TIMER:0'
  not_if  { Registry.value_exists?(AUTO_RUN_KEY, 'BGINFO') }
  action  :create
end
```

### windows_batch

This resource is now deprecated and will be removed in a future version of this cookbook. Chef >= 11.6.0 includes a built-in [batch](https://docs.chef.io/resource_batch.html) resource.

Execute a batch script using the cmd.exe interpreter (much like the script resources for bash, csh, powershell, perl, python and ruby). A temporary file is created and executed like other script resources, rather than run inline. By their nature, Script resources are not idempotent, as they are completely up to the user's imagination. Use the `not_if` or `only_if` meta parameters to guard the resource for idempotence.

#### Actions

- `:run` - run the batch file

#### Attribute Parameters

- `command` - name attribute. Name of the command to execute.
- `code` - quoted string of code to execute.
- `creates` - a file this command creates - if the file exists, the command will not be run.
- `cwd` - current working directory to run the command from.
- `flags` - command line flags to pass to the interpreter when invoking.
- `user` - A user name or user ID that we should change to before running this command.
- `group` - A group name or group ID that we should change to before running this command.

#### Examples

```ruby
windows_batch 'unzip_and_move_ruby' do
  code <<-EOH
  7z.exe x #{Chef::Config[:file_cache_path]}/ruby-1.8.7-p352-i386-mingw32.7z  -oC:\\source -r -y
  xcopy C:\\source\\ruby-1.8.7-p352-i386-mingw32 C:\\ruby /e /y
  EOH
end
```

```ruby
windows_batch 'echo some env vars' do
  code <<-EOH
  echo %TEMP%
  echo %SYSTEMDRIVE%
  echo %PATH%
  echo %WINDIR%
  EOH
end
```

### windows_certificate

Installs a certificate into the Windows certificate store from a file, and grants read-only access to the private key for designated accounts. Due to current limitations in winrm, installing certificated remotely may not work if the operation requires a user profile. Operations on the local machine store should still work.

#### Actions

- `:create` - creates or updates a certificate.
- `:delete` - deletes a certificate.
- `:acl_add` - adds read-only entries to a certificate's private key ACL.

#### Attribute Parameters

- `source` - name attribute. The source file (for create and acl_add), thumprint (for delete and acl_add) or subject (for delete).
- `pfx_password` - the password to access the source if it is a pfx file.
- `private_key_acl` - array of 'domain\account' entries to be granted read-only access to the certificate's private key. This is not idempotent.
- `store_name` - the certificate store to maniplate. One of MY (default : personal store), CA (trusted intermediate store) or ROOT (trusted root store).
- `user_store` - if false (default) then use the local machine store; if true then use the current user's store.

#### Examples

```ruby
# Add PFX cert to local machine personal store and grant accounts read-only access to private key
windows_certificate "c:/test/mycert.pfx" do
    pfx_password    "password"
    private_key_acl    ["acme\fred", "pc\jane"]
end
```

```ruby
# Add cert to trusted intermediate store
windows_certificate "c:/test/mycert.cer" do
    store_name    "CA"
end
```

```ruby
# Remove all certicates matching the subject
windows_certificate "me.acme.com" do
    action :delete
end
```

### windows_certificate_binding

Binds a certificate to an HTTP port in order to enable TLS communication.

#### Actions

- `:create` - creates or updates a binding.
- `:delete` - deletes a binding.

#### Attribute Parameters

- `cert_name` - name attribute. The thumprint(hash) or subject that identifies the certicate to be bound.
- `name_kind` - indicates the type of cert_name. One of :subject (default) or :hash.
- `address` - the address to bind against. Default is 0.0.0.0 (all IP addresses).
- `port` - the port to bind against. Default is 443.
- `app_id` - the GUID that defines the application that owns the binding. Default is the values used by IIS.
- `store_name` - the store to locate the certificate in. One of MY (default : personal store), CA (trusted intermediate store) or ROOT (trusted root store).

#### Examples

```ruby
# Bind the first certificate matching the subject to the default TLS port
windows_certificate_binding "me.acme.com" do
end
```

```ruby
# Bind a cert from the CA store with the given hash to port 4334
windows_certificate_binding "me.acme.com" do
    cert_name    "d234567890a23f567c901e345bc8901d34567890"
    name_kind    :hash
    store_name    "CA"
    port        4334
end
```

### windows_feature

Windows Roles and Features can be thought of as built-in operating system packages that ship with the OS. A server role is a set of software programs that, when they are installed and properly configured, lets a computer perform a specific function for multiple users or other computers within a network. A Role can have multiple Role Services that provide functionality to the Role. Role services are software programs that provide the functionality of a role. Features are software programs that, although they are not directly parts of roles, can support or augment the functionality of one or more roles, or improve the functionality of the server, regardless of which roles are installed. Collectively we refer to all of these attributes as 'features'.

This resource allows you to manage these 'features' in an unattended, idempotent way.

There are two providers for the `windows_features` which map into Microsoft's two major tools for managing roles/features: [Deployment Image Servicing and Management (DISM)](http://msdn.microsoft.com/en-us/library/dd371719%28v=vs.85%29.aspx) and [Servermanagercmd](http://technet.microsoft.com/en-us/library/ee344834%28WS.10%29.aspx) (The CLI for Server Manager). As Servermanagercmd is deprecated, Chef will set the default provider to `Chef::Provider::WindowsFeature::DISM` if DISM is present on the system being configured. The default provider will fall back to `Chef::Provider::WindowsFeature::ServerManagerCmd`.

For more information on Roles, Role Services and Features see the [Microsoft TechNet article on the topic](http://technet.microsoft.com/en-us/library/cc754923.aspx). For a complete list of all features that are available on a node type either of the following commands at a command prompt:

```text
dism /online /Get-Features
servermanagercmd -query
```

#### Actions

- `:install` - install a Windows role/feature
- `:remove` - remove a Windows role/feature

#### Attribute Parameters

- `feature_name` - name of the feature/role to install. The same feature may have different names depending on the provider used (ie DHCPServer vs DHCP; DNS-Server-Full-Role vs DNS).
- `all` - Boolean. Optional. Default: false. DISM provider only. Forces all dependencies to be installed.
- `source` - String. Optional. DISM provider only. Uses local repository for feature install.

#### Providers

- **Chef::Provider::WindowsFeature::DISM**: Uses Deployment Image Servicing and Management (DISM) to manage roles/features.
- **Chef::Provider::WindowsFeature::ServerManagerCmd**: Uses Server Manager to manage roles/features.
- **Chef::Provider::WindowsFeaturePowershell**: Uses Powershell to manage roles/features. (see [COOK-3714](https://tickets.opscode.com/browse/COOK-3714)

#### Examples

Enable the node as a DHCP Server

```ruby
windows_feature 'DHCPServer' do
  action :install
end
```

Enable TFTP

```ruby
windows_feature 'TFTP' do
  action :install
end
```

Enable .Net 3.5.1 on Server 2012 using repository files on DVD and install all dependencies

```ruby
windows_feature "NetFx3" do
  action :install
  all true
  source "d:\sources\sxs"
end
```

Disable Telnet client/server

```ruby
%w[TelnetServer TelnetClient].each do |feature|
  windows_feature feature do
    action :remove
  end
end
```

Add SMTP Feature with powershell provider

```ruby
windows_feature "smtp-server" do
  action :install
  all true
  provider :windows_feature_powershell
end
```

### windows_font

Installs a font.

Font files should be included in the cookbooks

#### Actions

- `:install` - install a font to the system fonts directory.

#### Attribute Parameters

- `file` - The name of the font file name to install. The path defaults to the files/default directory of the cookbook you're calling windows_font from. Defaults to the resource name.
- `source` - Set an alternate path to the font file.

#### Examples

```ruby
windows_font 'Code New Roman.otf'
```

### windows_http_acl

Sets the Access Control List for an http URL to grant non-admin accounts permission to open HTTP endpoints.

#### Actions

- `:create` - creates or updates the ACL for a URL.
- `:delete` - deletes the ACL from a URL.

#### Attribute Parameters

- `url` - the name of the url to be created/deleted.
- `user` - the name (domain\user) of the user or group to be granted permission to the URL. Mandatory for create. Only one user or group can be granted permission so this replaces any previously defined entry.

#### Examples

```ruby
windows_http_acl 'http://+:50051/' do
    user 'pc\\fred'
end
```

```ruby
windows_http_acl 'http://+:50051/' do
    action :delete
end
```

### windows_package

This resource is now deprecated and will be removed in a future version of this cookbook. Chef >= 12.6.0 includes a built-in [package](https://docs.chef.io/resource_windows_package.html) resource.

Manage Windows application packages in an unattended, idempotent way.

The following application installers are currently supported:

- MSI packages
- InstallShield
- Wise InstallMaster
- Inno Setup
- Nullsoft Scriptable Install System

If the proper installer type is not passed into the resource's installer_type attribute, the provider will do it's best to identify the type by introspecting the installation package. If the installation type cannot be properly identified the `:custom` value can be passed into the installer_type attribute along with the proper flags for silent/quiet installation (using the `options` attribute..see example below).

**PLEASE NOTE** - For proper idempotence the resource's `package_name` should be the same as the 'DisplayName' registry value in the uninstallation data that is created during package installation. The easiest way to definitively find the proper 'DisplayName' value is to install the package on a machine and search for the uninstall information under the following registry keys:

- `HKEY_LOCAL_MACHINE\Software\Microsoft\Windows\CurrentVersion\Uninstall`
- `HKEY_CURRENT_USER\Software\Microsoft\Windows\CurrentVersion\Uninstall`
- `HKEY_LOCAL_MACHINE\Software\Wow6464Node\Microsoft\Windows\CurrentVersion\Uninstall`

For maximum flexibility the `source` attribute supports both remote and local installation packages.

#### Actions

- `:install` - install a package
- `:remove` - remove a package. The remove action is completely hit or miss as many application uninstallers do not support a full silent/quiet mode.

#### Attribute Parameters

- `package_name` - name attribute. The 'DisplayName' of the application installation package.
- `source` - The source of the windows installer. This can either be a URI or a local path.
- `installer_type` - They type of windows installation package. Valid values include :msi, :inno, :nsis, :wise, :installshield, :custom. If this value is not provided, the provider will do it's best to identify the installer type through introspection of the file.
- `checksum` - useful if source is remote, the SHA-256 checksum of the file--if the local file matches the checksum, Chef will not download it
- `options` - Additional options to pass the underlying installation command
- `timeout` - set a timeout for the package download (default 600 seconds)
- `version` - The version number of this package, as indicated by the 'DisplayVersion' value in one of the 'Uninstall' registry keys. If the given version number does equal the 'DisplayVersion' in the registry, the package will be installed.
- `success_codes` - set an array of possible successful installation return codes. Previously this was hardcoded, but certain MSIs may have a different return code, e.g. 3010 for reboot required. Must be an array, and defaults to `[0, 42, 127]`.

#### Examples

Install PuTTY (InnoSetup installer)

```ruby
windows_package 'PuTTY version 0.60' do
  source 'http://the.earth.li/~sgtatham/putty/latest/x86/putty-0.60-installer.exe'
  installer_type :inno
  action :install
end
```

Install 7-Zip (MSI installer)

```ruby
windows_package '7-Zip 9.20 (x64 edition)' do
  source 'http://downloads.sourceforge.net/sevenzip/7z920-x64.msi'
  action :install
end
```

Install Notepad++ (Y U No Emacs?) using a local installer

```ruby
windows_package 'Notepad++' do
  source 'c:/installation_files/npp.5.9.2.Installer.exe'
  action :install
end
```

Install VLC for that Xvid (NSIS installer)

```ruby
windows_package 'VLC media player 1.1.10' do
  source 'http://superb-sea2.dl.sourceforge.net/project/vlc/1.1.10/win32/vlc-1.1.10-win32.exe'
  action :install
end
```

Install Firefox as custom installer and manually set the silent install flags

```ruby
windows_package 'Mozilla Firefox 5.0 (x86 en-US)' do
  source 'http://archive.mozilla.org/pub/mozilla.org/mozilla.org/firefox/releases/5.0/win32/en-US/Firefox%20Setup%205.0.exe'
  options '-ms'
  installer_type :custom
  action :install
end
```

Google Chrome FTW (MSI installer)

```ruby
windows_package 'Google Chrome' do
  source 'https://dl-ssl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B806F36C0-CB54-4A84-A3F3-0CF8A86575E0%7D%26lang%3Den%26browser%3D3%26usagestats%3D0%26appname%3DGoogle%2520Chrome%26needsadmin%3Dfalse/edgedl/chrome/install/GoogleChromeStandaloneEnterprise.msi'
  action :install
end
```

Remove Google Chrome

```ruby
windows_package 'Google Chrome' do
  action :remove
end
```

Remove 7-Zip

```ruby
windows_package '7-Zip 9.20 (x64 edition)' do
  action :remove
end
```

### windows_printer_port

Create and delete TCP/IPv4 printer ports.

#### Actions

- `:create` - Create a TCIP/IPv4 printer port. This is the default action.
- `:delete` - Delete a TCIP/IPv4 printer port

#### Attribute Parameters

- `ipv4_address` - Name attribute. Required. IPv4 address, e.g. '10.0.24.34'
- `port_name` - Port name. Optional. Defaults to 'IP_' + `ipv4_address`
- `port_number` - Port number. Optional. Defaults to 9100.
- `port_description` - Port description. Optional.
- `snmp_enabled` - Boolean. Optional. Defaults to false.
- `port_protocol` - Port protocol, 1 (RAW), or 2 (LPR). Optional. Defaults to 1.

#### Examples

Create a TCP/IP printer port named 'IP_10.4.64.37' with all defaults

```ruby
windows_printer_port '10.4.64.37' do
  action :create
end
```

Delete a printer port

```ruby
windows_printer_port '10.4.64.37' do
  action :delete
end
```

Delete a port with a custom port_name

```ruby
windows_printer_port '10.4.64.38' do
  port_name 'My awesome port'
  action :delete
end
```

Create a port with more options

```ruby
windows_printer_port '10.4.64.39' do
  port_name 'My awesome port'
  snmp_enabled true
  port_protocol 2
end
```

### windows_printer

Create Windows printer. Note that this doesn't currently install a printer driver. You must already have the driver installed on the system.

The Windows Printer LWRP will automatically create a TCP/IP printer port for you using the `ipv4_address` property. If you want more granular control over the printer port, just create it using the `windows_printer_port` LWRP before creating the printer.

#### Actions

- `:create` - Create a new printer
- `:delete` - Delete a new printer

#### Attribute Parameters

- `device_id` - Name attribute. Required. Printer queue name, e.g. 'HP LJ 5200 in fifth floor copy room'
- `comment` - Optional string describing the printer queue.
- `default` - Boolean. Optional. Defaults to false. Note that Windows sets the first printer defined to the default printer regardless of this setting.
- `driver_name` - String. Required. Exact name of printer driver. Note that the printer driver must already be installed on the node.
- `location` - Printer location, e.g. 'Fifth floor copy room', or 'US/NYC/Floor42/Room4207'
- `shared` - Boolean. Defaults to false.
- `share_name` - Printer share name.
- `ipv4_address` - Printer IPv4 address, e.g. '10.4.64.23'. You don't have to be able to ping the IP addresss to set it. Required.

An error of "Set-WmiInstance : Generic failure" is most likely due to the printer driver name not matching or not being installed.

#### Examples

Create a printer

```ruby
windows_printer 'HP LaserJet 5th Floor' do
  driver_name 'HP LaserJet 4100 Series PCL6'
  ipv4_address '10.4.64.38'
end
```

Delete a printer. Note: this doesn't delete the associated printer port. See `windows_printer_port` above for how to delete the port.

```ruby
windows_printer 'HP LaserJet 5th Floor' do
  action :delete
end
```

### windows_reboot

This resource is now deprecated and will be removed in a future version of this cookbook. Chef >= 12.0.0 includes a built-in [reboot](https://docs.chef.io/resource_reboot.html) resource.

Sets required data in the node's run_state to notify `WindowsRebootHandler` a reboot is requested. If Chef run completes successfully a reboot will occur if the `WindowsRebootHandler` is properly registered as a report handler. As an action of `:request` will cause a node to reboot every Chef run, this resource is usually notified by other resources...ie restart node after a package is installed (see example below).

#### Actions

- `:request` - requests a reboot at completion of successful Cher run. requires `WindowsRebootHandler` to be registered as a report handler.
- `:cancel` - remove reboot request from node.run_state. this will cancel _ALL_ previously requested reboots as this is a binary state.

#### Attribute Parameters

- `timeout` - Name attribute. timeout delay in seconds to wait before proceeding with the requested reboot. default is 60 seconds
- `reason` - comment on the reason for the reboot. default is 'Chef Software Chef initiated reboot'

#### Examples

If the package installs, schedule a reboot at end of chef run

```ruby
windows_reboot 60 do
  reason 'cause chef said so'
  action :nothing
end

windows_package 'some_package' do
  action :install
  notifies :request, 'windows_reboot[60]'
end
```

Cancel the previously requested reboot

```ruby
windows_reboot 60 do
  action :cancel
end
```

### windows_registry

This resource is now deprecated and will be removed in a future version of this cookbook. Chef >= 11.6.0 includes a built-in [registry_key](https://docs.chef.io/resource_registry_key.html) resource.

Creates and modifies Windows registry keys.

_Change in v1.3.0: The Win32 classes use `::Win32` to avoid namespace conflict with `Chef::Win32` (introduced in Chef 0.10.10)._

#### Actions

- `:create` - create a new registry key with the provided values.
- `:modify` - modify an existing registry key with the provided values.
- `:force_modify` - modify an existing registry key with the provided values. ensures the value is actually set by checking multiple times. useful for fighting race conditions where two processes are trying to set the same registry key. This will be updated in the near future to use 'RegNotifyChangeKeyValue' which is exposed by the WinAPI and allows a process to register for notification on a registry key change.
- `:remove` - removes a value from an existing registry key

#### Attribute Parameters

- `key_name` - name attribute. The registry key to create/modify.
- `values` - hash of the values to set under the registry key. The individual hash items will become respective 'Value name' => 'Value data' items in the registry key.
- `type` - Type of key to create, defaults to REG_SZ. Must be a symbol, see the overview below for valid values.

#### Registry key types

- `:binary` - REG_BINARY
- `:string` - REG_SZ
- `:multi_string` - REG_MULTI_SZ
- `:expand_string` - REG_EXPAND_SZ
- `:dword` - REG_DWORD
- `:dword_big_endian` - REG_DWORD_BIG_ENDIAN
- `:qword` - REG_QWORD

#### Examples

Make the local windows proxy match the one set for Chef

```ruby
proxy = URI.parse(Chef::Config[:http_proxy])
windows_registry 'HKCU\Software\Microsoft\Windows\CurrentVersion\Internet Settings' do
  values 'ProxyEnable' => 1, 'ProxyServer' => "#{proxy.host}:#{proxy.port}", 'ProxyOverride' => '<local>'
end
```

Enable Remote Desktop and poke the firewall hole

```ruby
windows_registry 'HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server' do
  values 'FdenyTSConnections' => 0
end
```

Delete an item from the registry

```ruby
windows_registry 'HKCU\Software\Test' do
  #Key is the name of the value that you want to delete the value is always empty
  values 'ValueToDelete' => ''
  action :remove
end
```

Add a REG_MULTI_SZ value to the registry

```ruby
windows_registry 'HKCU\Software\Test' do
  values 'MultiString' => ['line 1', 'line 2', 'line 3']
  type :multi_string
end
```

### windows_shortcut

Creates and modifies Windows shortcuts.

#### Actions

- `:create` - create or modify a windows shortcut

#### Attribute Parameters

- `name` - name attribute. The shortcut to create/modify.
- `target` - what the shortcut links to
- `arguments` - arguments to pass to the target when the shortcut is executed
- `description` - description of the shortcut
- `cwd` - Working directory to use when the target is executed
- `iconlocation` - Icon to use, in the format of `"path, index"` where index is which icon in that file to use (See [WshShortcut.IconLocation](https://msdn.microsoft.com/en-us/library/3s9bx7at.aspx))

#### Examples

Add a shortcut all users desktop:

```ruby
require 'win32ole'
all_users_desktop = WIN32OLE.new("WScript.Shell").SpecialFolders("AllUsersDesktop")

windows_shortcut "#{all_users_desktop}/Notepad.lnk" do
  target "C:\\WINDOWS\\notepad.exe"
  description "Launch Notepad"
  iconlocation "C:\\windows\\notepad.exe, 0"
end
```

#### Library Methods

```ruby
Registry.value_exists?('HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run','BGINFO')
Registry.key_exists?('HKLM\SOFTWARE\Microsoft')
BgInfo = Registry.get_value('HKLM\SOFTWARE\Microsoft\Windows\CurrentVersion\Run','BGINFO')
```

### windows_path

#### Actions

- `:add` - Add an item to the system path
- `:remove` - Remove an item from the system path

#### Attribute Parameters

- `path` - Name attribute. The name of the value to add to the system path

#### Examples

Add Sysinternals to the system path

```ruby
windows_path 'C:\Sysinternals' do
  action :add
end
```

Remove 7-Zip from the system path

```ruby
windows_path 'C:\7-Zip' do
  action :remove
end
```

### windows_task

Creates, deletes or runs a Windows scheduled task. Requires Windows Server 2008 due to API usage.

#### Actions

- `:create` - creates a task (or updates existing if user or command has changed)
- `:delete` - deletes a task
- `:run` - runs a task
- `:end` - ends a task
- `:change` - changes the un/pw or command of a task
- `:enable` - enable a task
- `:disable` - disable a task

#### Attribute Parameters

- `task_name` - name attribute, The task name. ("Task Name" or "/Task Name")
- `force` - When used with create, will update the task.
- `command` - The command the task will run.
- `cwd` - The directory the task will be run from.
- `user` - The user to run the task as. (defaults to 'SYSTEM')
- `password` - The user's password. (requires user)
- `run_level` - Run with `:limited` or `:highest` privileges.
- `frequency` - Frequency with which to run the task. (default is :hourly. Other valid values include :minute, :hourly, :daily, :weekly, :monthly, :once, :on_logon, :onstart, :on_idle) :once requires start_time
- `frequency_modifier` - Multiple for frequency. (15 minutes, 2 days). Monthly tasks may also use these values": ('FIRST', 'SECOND', 'THIRD', 'FOURTH', 'LAST', 'LASTDAY')
- `start_day` - Specifies the first date on which the task runs. Optional string (MM/DD/YYYY)
- `start_time` - Specifies the start time to run the task. Optional string (HH:mm)
- `interactive_enabled` - (Allow task to run interactively or non-interactively. Requires user and password.)
- `day` - For monthly or weekly tasks, the day(s) on which the task runs. (MON - SUN, *, 1 - 31)
- `months` - The Months of the year on which the task runs. (JAN, FEB, MAR, APR, MAY, JUN, JUL, AUG, SEP, OCT, NOV, DEC, *). Multiple months should be comma delimited.
- `idle_time` - For :on_idle frequency, the time (in minutes) without user activity that must pass to trigger the task. (1 - 999)

#### Examples

Create a `chef-client` task with TaskPath `\` running every 15 minutes

```ruby
windows_task 'chef-client' do
  user 'Administrator'
  password '$ecR3t'
  cwd 'C:\\chef\\bin'
  command 'chef-client -L C:\\tmp\\'
  run_level :highest
  frequency :minute
  frequency_modifier 15
end
```

Update `chef-client` task with new password and log location

```ruby
windows_task 'chef-client' do
  user 'Administrator'
  password 'N3wPassW0Rd'
  cwd 'C:\\chef\\bin'
  command 'chef-client -L C:\\chef\\logs\\'
  action :change
end
```

Delete a taks named `old task`

```ruby
windows_task 'old task' do
  action :delete
end
```

Enable a task named `chef-client`

```ruby
windows_task 'chef-client' do
  action :enable
end
```

Disable a task named `ProgramDataUpdater` with TaskPath `\Microsoft\Windows\Application Experience\`

```ruby
windows_task '\Microsoft\Windows\Application Experience\ProgramDataUpdater' do
  action :disable
end
```

### windows_zipfile

Most version of Windows do not ship with native cli utility for managing compressed files. This resource provides a pure-ruby implementation for managing zip files. Be sure to use the `not_if` or `only_if` meta parameters to guard the resource for idempotence or action will be taken every Chef run.

#### Actions

- `:unzip` - unzip a compressed file
- `:zip` - zip a directory (recursively)

#### Attribute Parameters

- `path` - name attribute. The path where files will be (un)zipped to.
- `source` - source of the zip file (either a URI or local path) for :unzip, or directory to be zipped for :zip.
- `overwrite` - force an overwrite of the files if they already exist.
- `checksum` - for :unzip, useful if source is remote, if the local file matches the SHA-256 checksum, Chef will not download it.

#### Examples

Unzip a remote zip file locally

```ruby
windows_zipfile 'c:/bin' do
  source 'http://download.sysinternals.com/Files/SysinternalsSuite.zip'
  action :unzip
  not_if {::File.exists?('c:/bin/PsExec.exe')}
end
```

Unzip a local zipfile

```ruby
windows_zipfile 'c:/the_codez' do
  source 'c:/foo/baz/the_codez.zip'
  action :unzip
end
```

Create a local zipfile

```ruby
windows_zipfile 'c:/foo/baz/the_codez.zip' do
  source 'c:/the_codez'
  action :zip
end
```

## Libraries

### WindowsHelper

Helper that allows you to use helpful functions in windows

#### installed_packages

Returns a hash of all DisplayNames installed

```ruby
# usage in a recipe
::Chef::Recipe.send(:include, Windows::Helper)
hash_of_installed_packages = installed_packages
```

#### is_package_installed?

- `package_name` - The name of the package you want to query to see if it is installed
- `returns` - true if the package is installed, false if it the package is not installed

Download a file if a package isn't installed

```ruby
# usage in a recipe to not download a file if package is already installed
::Chef::Recipe.send(:include, Windows::Helper)
is_win_sdk_installed = is_package_installed?('Windows Software Development Kit')

remote_file 'C:\windows\temp\windows_sdk.zip' do
  source 'http://url_to_download/windows_sdk.zip'
  action :create_if_missing
  not_if {is_win_sdk_installed}
end
```

Do something if a package is installed

```ruby
# usage in a provider
include Windows::Helper
if is_package_installed?('Windows Software Development Kit')
  # do something if package is installed
end
```

## Exception/Report Handlers

### WindowsRebootHandler

Required reboots are a necessary evil of configuring and managing Windows nodes. This report handler (ie fires at the end of Chef runs) acts on requested (Chef initiated) or pending (as determined by the OS per configuration action we performed) reboots. The `allow_pending_reboots` initialization argument should be set to false if you do not want the handler to automatically reboot a node if it has been determined a reboot is pending. Reboots can still be requested explicitly via the `windows_reboot` LWRP.

### Initialization Arguments

- `allow_pending_reboots` - indicator on whether the handler should act on a the Window's 'pending reboot' state. default is true
- `timeout` - timeout delay in seconds to wait before proceeding with the reboot. default is 60 seconds
- `reason` - comment on the reason for the reboot. default is 'Chef Software Chef initiated reboot'

## Windows ChefSpec Matchers

The Windows cookbook includes custom [ChefSpec](https://github.com/sethvargo/chefspec) matchers you can use to test your own cookbooks that consume Windows cookbook LWRPs.

### Example Matcher Usage

```ruby
expect(chef_run).to install_windows_package('Node.js').with(
  source: 'http://nodejs.org/dist/v0.10.26/x64/node-v0.10.26-x64.msi')
```

### Windows Cookbook Matchers

- create_windows_auto_run
- remove_windows_auto_run
- run_windows_batch
- create_windows_certificate
- delete_windows_certificate
- add_acl_to_windows_certificate
- create_windows_certificate_binding
- delete_windows_certificate_binding
- install_windows_feature
- remove_windows_feature
- delete_windows_feature
- install_windows_font
- create_windows_http_acl
- delete_windows_http_acl
- install_windows_package
- remove_windows_package
- set_windows_pagefile
- add_windows_path
- remove_windows_path
- create_windows_printer
- delete_windows_printer
- create_windows_printer_port
- delete_windows_printer_port
- request_windows_reboot
- cancel_windows_reboot
- create_windows_registry
- modify_windows_registry
- force_modify_windows_registry
- remove_windows_registry
- create_windows_shortcut
- create_windows_shortcut
- create_windows_task
- disable_windows_task
- enable_windows_task
- delete_windows_task
- run_windows_task
- change_windows_task
- unzip_windows_zipfile_to
- zip_windows_zipfile_to

## Usage

Place an explicit dependency on this cookbook (using depends in the cookbook's metadata.rb) from any cookbook where you would like to use the Windows-specific resources/providers that ship with this cookbook.

```ruby
depends 'windows'
```

### default

Convenience recipe that installs supporting gems for many of the resources/providers that ship with this cookbook.

### reboot_handler

Leverages the `chef_handler` LWRP to register the `WindowsRebootHandler` report handler that ships as part of this cookbook. By default this handler is set to automatically act on pending reboots. If you would like to change this behavior override `node['windows']['allow_pending_reboots']` and set the value to false. For example:

```ruby
name 'base'
description 'base role'
override_attributes(
  'windows' => {
    'allow_pending_reboots' => false
  }
)
```

This will still allow a reboot to be explicitly requested via the `windows_reboot` LWRP.

By default, the handler will only be registered as a report handler, meaning that it will only fire at the end of successful Chef runs. If the run fails, pending or requested reboots will be ignored. This can lead to a situation where some package was installed and notified a reboot request via the `windows_reboot` LWRP, and then the run fails for some unrelated reason, and the reboot request gets dropped because the resource that notified the reboot request will already be up-to-date at the next run and will not request a reboot again, and thus the requested reboot will never be performed. To change this behavior and register the handler as an exception handler that fires at the end of failed runs too, override `node['windows']['allow_reboot_on_failure']` and set the value to true.

## License & Authors

- Author:: Seth Chisamore ([schisamo@chef.io](mailto:schisamo@chef.io))
- Author:: Doug MacEachern ([dougm@vmware.com](mailto:dougm@vmware.com))
- Author:: Paul Morton ([pmorton@biaprotect.com](mailto:pmorton@biaprotect.com))
- Author:: Doug Ireton ([doug.ireton@nordstrom.com](mailto:doug.ireton@nordstrom.com))

```text
Copyright 2011-2016, Chef Software, Inc.
Copyright 2010, VMware, Inc.
Copyright 2011, Business Intelligence Associates, Inc
Copyright 2012, Nordstrom, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
apt Cookbook
============
[![Build Status](https://img.shields.io/travis/chef-cookbooks/apt.svg)][travis]
[![Cookbook Version](https://img.shields.io/cookbook/v/apt.svg)][cookbook]

[cookbook]: https://community.chef.io/cookbooks/apt
[travis]: https://travis-ci.org/chef-cookbooks/apt

This cookbook includes recipes to execute apt-get update to ensure the local APT package cache is up to date. There are recipes for managing the apt-cacher-ng caching proxy and proxy clients. It also includes a LWRP for managing APT repositories in /etc/apt/sources.list.d as well as an LWRP for pinning packages via /etc/apt/preferences.d.


Requirements
------------
**Version 2.0.0+ of this cookbook requires Chef 11.0.0 or later**. If your Chef version is earlier than 11.0.0, use version 1.10.0 of this cookbook.

Version 1.8.2 to 1.10.0 of this cookbook requires **Chef 10.16.4** or later.

If your Chef version is earlier than 10.16.4, use version 1.7.0 of this cookbook.

### Platform
Please refer to the [TESTING file](TESTING.md) to see the currently (and passing) tested platforms. The release was tested on:

* Ubuntu 10.04
* Ubuntu 12.04
* Ubuntu 13.04
* Debian 7.1
* Debian 6.0 (have with manual testing)

May work with or without modification on other Debian derivatives.


-------
### default
This recipe manually updates the timestamp file used to only run `apt-get update` if the cache is more than one day old.

This recipe should appear first in the run list of Debian or Ubuntu nodes to ensure that the package cache is up to date before managing any `package` resources with Chef.

This recipe also sets up a local cache directory for preseeding packages.

**Including the default recipe on a node that does not support apt (such as Windows) results in a noop.**

### cacher-client
Configures the node to use the `apt-cacher-ng` server as a client.

#### Bypassing the cache
Occasionally you may come across repositories that do not play nicely when the node is using an `apt-cacher-ng` server. You can configure `cacher-client` to bypass the server and connect directly to the repository with the `cache_bypass` attribute.

To do this, you need to override the `cache_bypass` attribute with an array of repositories, with each array key as the repository URL and value as the protocol to use:

```json
{
    "apt": {
        "cache_bypass": {
            "URL": "PROTOCOL"
        }
    }
}
```

For example, to prevent caching and directly connect to the repository at `download.oracle.com` via http:

```json
{
    "apt": {
        "cache_bypass": {
            "download.oracle.com": "http"
        }
    }
}
```

### cacher-ng
Installs the `apt-cacher-ng` package and service so the system can provide APT caching. You can check the usage report at http://{hostname}:3142/acng-report.html.

If you wish to help the `cacher-ng` recipe seed itself, you must now explicitly include the `cacher-client` recipe in your run list **after** `cacher-ng` or you will block your ability to install any packages (ie. `apt-cacher-ng`).

### unattended-upgrades

Installs and configures the `unattended-upgrades` package to provide automatic package updates. This can be configured to upgrade all packages or to just install security updates by setting `['apt']['unattended_upgrades']['allowed_origins']`.

To pull just security updates, you'd set `allowed_origins` to something link `["Ubuntu trusty-security"]` (for Ubuntu trusty) or `["Debian wheezy-security"]` (for Debian wheezy). 


Attributes
----------

### General 
* `['apt']['compile_time_update']` - force the default recipe to run `apt-get update` at compile time.
* `['apt']['periodic_update_min_delay']` - minimum delay (in seconds) beetween two actual executions of `apt-get update` by the `execute[apt-get-update-periodic]` resource, default is '86400' (24 hours)

### Caching

* `['apt']['cacher_ipaddress']` - use a cacher server (or standard proxy server) not available via search
* `['apt']['cacher_interface']` - interface to connect to the cacher-ng service, no default.
* `['apt']['cacher_port']` - port for the cacher-ng service (either client or server), default is '3142'
* `['apt']['cacher_ssl_support']` - indicates whether the cacher supports upstream SSL servers, default is 'false'
* `['apt']['cacher_dir']` - directory used by cacher-ng service, default is '/var/cache/apt-cacher-ng'
* `['apt']['cacher-client']['restrict_environment']` - restrict your node to using the `apt-cacher-ng` server in your Environment, default is 'false'
* `['apt']['compiletime']` - force the `cacher-client` recipe to run before other recipes. It forces apt to use the proxy before other recipes run. Useful if your nodes have limited access to public apt repositories. This is overridden if the `cacher-ng` recipe is in your run list. Default is 'false'
* `['apt']['cache_bypass']` - array of URLs to bypass the cache. Accepts the URL and protocol to  fetch directly from the remote repository and not attempt to cache

### Unattended Upgrades

* `['apt']['unattended_upgrades']['enable']` - enables unattended upgrades, default is false
* `['apt']['unattended_upgrades']['update_package_lists']` - automatically update package list (`apt-get update`) daily, default is true
* `['apt']['unattended_upgrades']['allowed_origins']` - array of allowed apt origins from which to pull automatic upgrades, defaults to a guess at the system's main origin and should almost always be overridden
* `['apt']['unattended_upgrades']['package_blacklist']` - an array of package which should never be automatically upgraded, defaults to none
* `['apt']['unattended_upgrades']['auto_fix_interrupted_dpkg']` - attempts to repair dpkg state with `dpkg --force-confold --configure -a` if it exits uncleanly, defaults to false (contrary to the unattended-upgrades default)
* `['apt']['unattended_upgrades']['minimal_steps']` - Split the upgrade into the smallest possible chunks. This makes the upgrade a bit slower but it has the benefit that shutdown while a upgrade is running is possible (with a small delay). Defaults to false.
* `['apt']['unattended_upgrades']['install_on_shutdown']` - Install upgrades when the machine is shuting down instead of doing it in the background while the machine is running. This will (obviously) make shutdown slower. Defaults to false.
* `['apt']['unattended_upgrades']['mail']` - Send email to this address for problems or packages upgrades. Defaults to no email.
* `['apt']['unattended_upgrades']['mail_only_on_error']` - If set, email will only be set on upgrade errors. Otherwise, an email will be sent after each upgrade. Defaults to true.
* `['apt']['unattended_upgrades']['remove_unused_dependencies']` Do automatic removal of new unused dependencies after the upgrade. Defaults to false.
* `['apt']['unattended_upgrades']['automatic_reboot']` - Automatically reboots *without confirmation* if a restart is required after the upgrade. Defaults to false.
* `['apt']['unattended_upgrades']['dl_limit']` - Limits the bandwidth used by apt to download packages. Value given as an integer in kb/sec. Defaults to nil (no limit).

### Configuration for APT

* `['apt']['confd']['install_recommends']` - Consider recommended packages as a dependency for installing. (default: true)
* `['apt']['confd']['install_suggests']` - Consider suggested packages as a dependency for installing. (default: false)

Libraries
---------
There is an `interface_ipaddress` method that returns the IP address for a particular host and interface, used by the `cacher-client` recipe. To enable it on the server use the `['apt']['cacher_interface']` attribute.

Resources/Providers
-------------------
### `apt_repository`
This LWRP provides an easy way to manage additional APT repositories. Adding a new repository will notify running the `execute[apt-get-update]` resource immediately.

#### Actions
- :add: creates a repository file and builds the repository listing (default)
- :remove: removes the repository file

#### Attribute Parameters
- repo_name: name attribute. The name of the channel to discover
- uri: the base of the Debian distribution
- distribution: this is usually your release's codename...ie something like `karmic`, `lucid` or `maverick`
- components: package groupings... when in doubt use `main`
- arch: constrain package to a particular arch like `i386`, `amd64` or even `armhf` or `powerpc`. Defaults to nil.
- trusted: treat all packages from this repository as authenticated regardless of signature
- deb_src: whether or not to add the repository as a source repo as well - value can be `true` or `false`, default `false`.
- keyserver: the GPG keyserver where the key for the repo should be retrieved
- key: if a `keyserver` is provided, this is assumed to be the fingerprint, otherwise it can be either the URI to the GPG key for the repo, or a cookbook_file.
- key_proxy: if set, pass the specified proxy via `http-proxy=` to GPG.
- cookbook: if key should be a cookbook_file, specify a cookbook where the key is located for files/default. Defaults to nil, so it will use the cookbook where the resource is used.

#### Examples

Add the Zenoss repo:

```ruby
apt_repository 'zenoss' do
  uri        'http://dev.zenoss.org/deb'
  components ['main', 'stable']
end
```

Enable Ubuntu [multiverse](https://help.ubuntu.com/community/Repositories/Ubuntu) repositories:

```ruby
apt_repository 'security-ubuntu-multiverse' do
  uri        'http://security.ubuntu.com/ubuntu'
  distribution 'trusty-security'
  components ['multiverse']
  deb_src 'true'
end
```

Add the Nginx PPA, autodetect the key and repository url:

```ruby
apt_repository 'nginx-php' do
  uri          'ppa:nginx/stable'
  distribution node['lsb']['codename']
end
```

Add the JuJu PPA, grab the key from the keyserver, and add source repo:

```ruby
apt_repository 'juju' do
  uri 'http://ppa.launchpad.net/juju/stable/ubuntu'
  components ['main']
  distribution 'trusty'
  key 'C8068B11'
  keyserver 'keyserver.ubuntu.com'
  action :add
  deb_src true
end
```

Add the Cloudera Repo of CDH4 packages for Ubuntu 12.04 on AMD64:

```ruby
apt_repository 'cloudera' do
  uri          'http://archive.cloudera.com/cdh4/ubuntu/precise/amd64/cdh'
  arch         'amd64'
  distribution 'precise-cdh4'
  components   ['contrib']
  key          'http://archive.cloudera.com/debian/archive.key'
end
```

Remove Zenoss repo:

```ruby
apt_repository 'zenoss' do
  action :remove
end
```

### `apt_preference`
This LWRP provides an easy way to pin packages in /etc/apt/preferences.d. Although apt-pinning is quite helpful from time to time please note that Debian does not encourage its use without thorough consideration.

Further information regarding apt-pinning is available via http://wiki.debian.org/AptPreferences.

#### Actions
- :add: creates a preferences file under /etc/apt/preferences.d
- :remove: Removes the file, therefore unpin the package

#### Attribute Parameters
- package_name: name attribute. The name of the package
- glob: Pin by glob() expression or regexp surrounded by /.
- pin: The package version/repository to pin
- pin_priority: The pinning priority aka "the highest package version wins"

#### Examples
Pin libmysqlclient16 to version 5.1.49-3:

```ruby
apt_preference 'libmysqlclient16' do
  pin          'version 5.1.49-3'
  pin_priority '700'
end
```

Unpin libmysqlclient16:

```ruby
apt_preference 'libmysqlclient16' do
  action :remove
end
```

Pin all packages from dotdeb.org:

```ruby
apt_preference 'dotdeb' do
  glob         '*'
  pin          'origin packages.dotdeb.org'
  pin_priority '700'
end
```


Usage
-----
Put `recipe[apt]` first in the run list. If you have other recipes that you want to use to configure how apt behaves, like new sources, notify the execute resource to run, e.g.:

```ruby
template '/etc/apt/sources.list.d/my_apt_sources.list' do
  notifies :run, 'execute[apt-get update]', :immediately
end
```

The above will run during execution phase since it is a normal template resource, and should appear before other package resources that need the sources in the template.

Put `recipe[apt::cacher-ng]` in the run_list for a server to provide APT caching and add `recipe[apt::cacher-client]` on the rest of the Debian-based nodes to take advantage of the caching server.

If you want to cleanup unused packages, there is also the `apt-get autoclean` and `apt-get autoremove` resources provided for automated cleanup.


License & Authors
-----------------
- Author:: Joshua Timberman (joshua@chef.io)
- Author:: Matt Ray (matt@chef.io)
- Author:: Seth Chisamore (schisamo@chef.io)

```text
Copyright:: 2009-2015, Chef Software, Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
# Homebrew Cookbook
[![Build Status](https://travis-ci.org/chef-cookbooks/homebrew.svg?branch=master)](http://travis-ci.org/chef-cookbooks/homebrew) [![Cookbook Version](https://img.shields.io/cookbook/v/homebrew.svg)](https://supermarket.chef.io/cookbooks/homebrew)

This cookbook installs [Homebrew](http://mxcl.github.com/homebrew/) and under Chef 11 and earlier versions, its package provider replaces MacPorts as the _default package provider_ for the package resource on OS X systems.

# Requirements
Chef 12: The package provider is not necessary on Chef 12, as the default [OS X package provider](https://github.com/chef/chef-rfc/blob/master/rfc016-homebrew-osx-package-provider.md) is homebrew.

Chef <= 11: The package provider will be set as the default provider for OS X.

## Prerequisites
In order for this recipe to work, your userid must own `/usr/local`. This is outside the scope of the cookbook because it's possible that you'll run the cookbook as your own user, not root and you'd have to be root to take ownership of the directory. Easiest way to get started:

```bash
sudo chown -R `whoami`:staff /usr/local
```

Bear in mind that this will take ownership of the entire folder and its contents, so if you've already got stuff in there (eg MySQL owned by a `mysql` user) you'll need to be a touch more careful. This is a recommendation from the Homebrew project.

**Note** This cookbook _only_ supports installing in `/usr/local`. While the Homebrew project itself allows for alternative installations, this cookbook doesn't.

## Platform
- Mac OS X (10.6+)

The only platform supported by Homebrew itself at the time of this writing is Mac OS X. It should work fine on Server edition as well, and on platforms that Homebrew supports in the future.

## Cookbooks
- build-essential: homebrew itself doesn't work well if XCode is not installed.

# Attributes
- `node['homebrew']['owner']` - The user that will own the Homebrew installation and packages. Setting this will override the default behavior which is to use the non-privileged user that has invoked the Chef run (or the `SUDO_USER` if invoked with sudo). The default is `nil`.
- `node['homebrew']['auto-update']` - Whether the default recipe should automatically update homebrew each run or not. The default is `true` to maintain compatibility. Set to false or nil to disable. Note that disabling this feature may cause formula to not work.
- `node['homebrew']['formulas']` - An Array of formula that should be installed using homebrew by default, used only in the `homebrew::install_formulas` recipe.
  - To install the most recent version, include just the recipe name: `- simple_formula`
  - To install a specific version, specify both its name and version:

    ```
    - name: special-version-formula
      version: 1.2.3
    ```

  - To install the HEAD of a formula, specify both its name and `head: true`:

    ```
    - name: head-tracking-formula
      head: true
    ```

- `node['homebrew']['casks']` - An Array of casks that should be installed using brew cask by default, used only in the `homebrew::install_casks` recipe.
- `node['homebrew']['taps']` - An Array of taps that should be installed using brew tap by default, used only in the `homebrew::install_taps` recipe.

# Resources and Providers
This cookbook includes a package resource provider to use homebrew. Under Chef 12+, this is not necessary, and the code doesn't actually get used on Chef 12+. This was preserved to maintain backwards compatiblity with older versions of Chef.

## package / homebrew\_package
This cookbook provides a package provider called `homebrew_package` which will install/remove packages using Homebrew. This becomes the default provider for `package` if your platform is Mac OS X.

As this extends the built-in package resource/provider in Chef, it has all the resource attributes and actions available to the package resource. However, a couple notes:
- Homebrew itself doesn't have a notion of "upgrade" per se. The "upgrade" action will simply perform an install, and if the Homebrew Formula for the package is newer, it will upgrade.
- Likewise, Homebrew doesn't have a purge, but the "purge" action will act like "remove".

### Examples

```ruby
package 'mysql' do
  action :install
end

homebrew_package 'mysql'

package 'mysql' do
  provider Chef::Provider::Package::Homebrew
end

package 'wireshark' do
  options '--with-qt --devel'
end
```

### homebrew\_tap
LWRP for `brew tap`, a Homebrew command used to add additional formula repositories. From the `brew` man page:

```text
tap [tap]
       Tap a new formula repository from GitHub, or list existing taps.

       tap is of the form user/repo, e.g. brew tap homebrew/dupes.
```

Default action is `:tap` which enables the repository. Use `:untap` to disable a tapped repository.

#### Examples

```ruby
homebrew_tap 'homebrew/dupes'

homebrew_tap 'homebrew/dupes' do
  action :untap
end
```

## homebrew\_cask
LWRP for `brew cask`, a Homebrew-style CLI workflow for the administration of Mac applications distributed as binaries. It's implemented as a homebrew "external command" called cask.

[homebrew-cask on GitHub](https://github.com/caskroom/homebrew-cask)

### Prerequisites
You must have the homebrew-cask repository tapped.

```ruby
homebrew_tap 'caskroom/cask'
```

And then install the homebrew cask package before using this LWRP.

```ruby
package "brew-cask" do
  action :install
  end
```

You can include the `homebrew::cask` recipe to do this.

### Examples

```ruby
homebrew_cask "google-chrome"

homebrew_cask "google-chrome" do
  action :uncask
end
```

Default action is `:cask` which installs the Application binary . Use `:uncask` to uninstall a an Application.

[View the list of available Casks](https://github.com/caskroom/homebrew-cask/tree/master/Casks)

# Usage
We strongly recommend that you put "recipe[homebrew]" in your node's run list, to ensure that it is available on the system and that Homebrew itself gets installed. Putting an explicit dependency in the metadata will cause the cookbook to be downloaded and the library loaded, thus resulting in changing the package provider on Mac OS X, so if you have systems you want to use the default (Mac Ports), they would be changed to Homebrew.

The default recipe also ensures that Homebrew is installed and up to date if the auto update attribute (above) is true (default).

# License and Authors
This cookbook is maintained by CHEF. The original author, maintainer and copyright holder is Graeme Mathieson. The cookbook remains licensed under the Apache License version 2.

[Original blog post by Graeme](https://woss.name/articles/converging-your-home-directory-with-chef/)

Author:: Graeme Mathieson ([mathie@woss.name](mailto:mathie@woss.name))

Author:: Joshua Timberman ([joshua@chef.io](mailto:joshua@chef.io))

```text
Copyright:: 2011, Graeme Mathieson
Copyright:: 2012-2015, Chef Software, Inc. <legal@chef.io>

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
# yum Cookbook
[![Build Status](https://travis-ci.org/chef-cookbooks/yum.svg?branch=master)](http://travis-ci.org/chef-cookbooks/yum) [![Cookbook Version](https://img.shields.io/cookbook/v/yum.svg)](https://supermarket.chef.io/cookbooks/yum) [![Code Climate](https://codeclimate.com/github/chef-cookbooks/yum/badges/gpa.svg)](https://codeclimate.com/github/chef-cookbooks/yum)

The Yum cookbook exposes the `yum_globalconfig` and `yum_repository` resources that allows a user to both control global behavior and make individual Yum repositories available for use. These resources aim to allow the user to configure all options listed in the `yum.conf` man page, found at [http://linux.die.net/man/5/yum.conf](http://linux.die.net/man/5/yum.conf)

## NOTES
WARNING: Yum cookbook version 3.0.0 and above contain non-backwards compatible breaking changes and will not work with cookbooks written against the 2.x and 1.x series. Changes have been made to the yum_repository resource, and the yum_key resource has been eliminated entirely. Recipes have been eliminated and moved into their own cookbooks. Please lock yum to the 2.x series in your Chef environments until all dependent cookbooks have been ported.

## Requirements
### Platforms
- RHEL/CentOS and derivatives
- Fedora

### Chef
- Chef 11+

### Cookbooks
- none

## Resources/Providers
### yum_repository
This resource manages a yum repository configuration file at /etc/yum.repos.d/`repositoryid`.repo. When the file needs to be repaired, it calls yum-makecache so packages in the repo become available to the next resource.

#### Example

```ruby
# add the Zenoss repository
yum_repository 'zenoss' do
  description "Zenoss Stable repo"
  baseurl "http://dev.zenoss.com/yum/stable/"
  gpgkey 'http://dev.zenoss.com/yum/RPM-GPG-KEY-zenoss'
  action :create
end

# add the EPEL repo
yum_repository 'epel' do
  description 'Extra Packages for Enterprise Linux'
  mirrorlist 'http://mirrors.fedoraproject.org/mirrorlist?repo=epel-6&arch=$basearch'
  gpgkey 'http://dl.fedoraproject.org/pub/epel/RPM-GPG-KEY-EPEL-6'
  action :create
end
```

```ruby
# delete CentOS-Media repo
yum_repository 'CentOS-Media' do
  action :delete
end
```

#### Actions
- `:create` - creates a repository file and builds the repository listing
- `:delete` - deletes the repository file
- `:makecache` - update yum cache

#### Parameters
- `baseurl` -  Must be a URL to the directory where the yum repository's 'repodata' directory lives. Can be an http://, ftp:// or file:// URL. You can specify multiple URLs in one baseurl statement.
- `cost` - relative cost of accessing this repository. Useful for weighing one repo's packages as greater/less than any other. defaults to 1000
- `clean_metadata` - Run "yum clean metadata <reponame>" during repository creation. defaults to true.
- `description` - Maps to the 'name' parameter in a repository .conf. Descriptive name for the repository channel. This directive must be specified.
- `enabled` - Either `true` or `false`. This tells yum whether or not use this repository.
- `enablegroups` -  Either `true` or `false`. Determines whether yum will allow the use of package groups for this repository. Default is `true` (package groups are allowed).
- `exclude` - List of packages to exclude from updates or installs. This should be a space separated list in a single string. Shell globs using wildcards (eg. * and ?) are allowed.
- `failovermethod` - Either 'roundrobin' or 'priority'.
- `fastestmirror_enabled` - Either `true` or `false`
- `gpgcheck` - Either `true` or `false`. This tells yum whether or not it should perform a GPG signature check on packages. When this is set in the [main] section it sets the default for all repositories. The default is `true`.
- `gpgkey` - A URL pointing to the ASCII-armored GPG key file for the repository. This option is used if yum needs a public key to verify a package and the required key hasn't been imported into the RPM database. If this option is set, yum will automatically import the key from the specified URL.
- `http_caching` - Either 'all', 'packages', or 'none'. Determines how upstream HTTP caches are instructed to handle any HTTP downloads that Yum does. Defaults to 'all'
- `includepkgs` -  Inverse of exclude. This is a list of packages you want to use from a repository. If this option lists only one package then that is all yum will ever see from the repository. Defaults to an empty list.
- `keepalive` - Either `true` or `false`. This tells yum whether or not HTTP/1.1 keepalive should be used with this repository.
- `make_cache` - Optional, Default is `true`, if `false` then `yum -q makecache` will not be ran
- `max_retries` - Set the number of times any attempt to retrieve a file should retry before returning an error. Setting this to '0' makes yum try forever. Default is '10'.
- `metadata_expire` - Time (in seconds) after which the metadata will expire. So that if the current metadata downloaded is less than this many seconds old then yum will not update the metadata against the repository. If you find that yum is not downloading information on updates as often as you would like lower the value of this option. You can also change from the default of using seconds to using days, hours or minutes by appending a d, h or m respectively. The default is 6 hours, to compliment yum-updatesd running once an hour. It's also possible to use the word "never", meaning that the metadata will never expire. Note that when using a metalink file the metalink must always be newer than the metadata for the repository, due to the validation, so this timeout also applies to the metalink file.
- `mirrorlist` - Specifies a URL to a file containing a list of baseurls. This can be used instead of or with the baseurl option. Substitution variables, described below, can be used with this option. As a special hack is the mirrorlist URL contains the word "metalink" then the value of mirrorlist is copied to metalink (if metalink is not set)
- `mirror_expire` - Time (in seconds) after which the mirrorlist locally cached will expire. If the current mirrorlist is less than this many seconds old then yum will not download another copy of the mirrorlist, it has the same extra format as metadata_expire. If you find that yum is not downloading the mirrorlists as often as you would like lower the value of this option.
- `mirrorlist_expire` - alias for mirror_expire
- `mode` - Permissions mode of .repo file on disk. Useful for scenarios where secrets are in the repo file. If set to '600', normal users will not be able to use yum search, yum info, etc. Defaults to '0644'
- `priority` - When the yum-priorities plug-in is enabled, you set priorities on repository entries, where N is an integer from 1 to 99. The default priority for repositories is 99.
- `proxy` - URL to the proxy server that yum should use.
- `proxy_username` -  username to use for proxy
- `proxy_password` - password for this proxy
- `report_instanceid` - Report instance ID when using Amazon Linux AMIs and repositories
- `repositoryid` - Must be a unique name for each repository, one word. Defaults to name attribute.
- `sensitive` - Optional, Default is `false`, if `true` then content of repository file is hidden from chef run output.
- `source` - Use a custom template source instead of the default one in the yum cookbook
- `sslcacert` - Path to the directory containing the databases of the certificate authorities yum should use to verify SSL certificates. Defaults to none - uses system default
- `sslclientcert` - Path to the SSL client certificate yum should use to connect to repos/remote sites Defaults to none.
- `sslclientkey` - Path to the SSL client key yum should use to connect to repos/remote sites Defaults to none.
- `sslverify` - Either `true` or `false`. Determines if yum will verify SSL certificates/hosts. Defaults to `true`
- `timeout` - Number of seconds to wait for a connection before timing out. Defaults to 30 seconds. This may be too short of a time for extremely overloaded sites.

### yum_globalconfig
This renders a template with global yum configuration parameters. The default recipe uses it to render `/etc/yum.conf`. It is flexible enough to be used in other scenarios, such as building RPMs in isolation by modifying `installroot`.

#### Example

```ruby
yum_globalconfig '/my/chroot/etc/yum.conf' do
  cachedir '/my/chroot/etc/yum.conf'
  keepcache 'yes'
  debuglevel '2'
  installroot '/my/chroot'
  action :create
end
```

#### Parameters
`yum_globalconfig` can take most of the same parameters as a `yum_repository`, plus more, too numerous to describe here. Below are a few of the more commonly used ones. For a complete list, please consult the `yum.conf` man page, found here: [http://linux.die.net/man/5/yum.conf](http://linux.die.net/man/5/yum.conf)
- `cachedir` - Directory where yum should store its cache and db files. The default is '/var/cache/yum'.
- `keepcache` - Either `true` or `false`. Determines whether or not yum keeps the cache of headers and packages after successful installation. Default is `false`
- `debuglevel` - Debug message output level. Practical range is 0-10. Default is '2'.
- `exclude` - List of packages to exclude from updates or installs. This should be a space separated list. Shell globs using wildcards (eg. * and ?) are allowed.
- `installonlypkgs` = List of package provides that should only ever be installed, never updated. Kernels in particular fall into this category. Defaults to kernel, kernel-bigmem, kernel-enterprise, kernel-smp, kernel-debug, kernel-unsupported, kernel-source, kernel-devel, kernel-PAE, kernel-PAE-debug.
- `logfile` - Full directory and file name for where yum should write its log file.
- `exactarch` -  Either `true` or `false`. Set to `true` to make 'yum update' only update the architectures of packages that you have installed. ie: with this enabled yum will not install an i686 package to update an x86_64 package. Default is `true`
- `gpgcheck` - Either `true` or `false`. This tells yum whether or not it should perform a GPG signature check on the packages gotten from this repository.

## Recipes
- `default` - Configures `yum_globalconfig[/etc/yum.conf]` with values found in node attributes at `node['yum']['main']`
- `dnf_yum_compat` - Installs the yum package using dnf on Fedora systems to provide support for the package resource in recipes. This is necessary as Chef does not yet (as of Q4 2015) have native support for DNF. This recipe should be 1st on a Fedora runlist

## Attributes
The following attributes are set by default

```ruby
default['yum']['main']['cachedir'] = '/var/cache/yum/$basearch/$releasever'
default['yum']['main']['keepcache'] = false
default['yum']['main']['debuglevel'] = nil
default['yum']['main']['exclude'] = nil
default['yum']['main']['logfile'] = '/var/log/yum.log'
default['yum']['main']['exactarch'] = nil
default['yum']['main']['obsoletes'] = nil
default['yum']['main']['installonly_limit'] = nil
default['yum']['main']['installonlypkgs'] = nil
default['yum']['main']['installroot'] = nil
```

## Related Cookbooks
Recipes from older versions of this cookbook have been moved individual cookbooks. Recipes for managing platform yum configurations and installing specific repositories can be found in one (or more!) of the following cookbook.
- yum-centos
- yum-fedora
- yum-amazon
- yum-epel
- yum-elrepo
- yum-repoforge
- yum-ius
- yum-percona
- yum-pgdg

## Usage
Put `depends 'yum'` in your metadata.rb to gain access to the yum_repository resource.

## License & Authors
- Author:: Eric G. Wolfe
- Author:: Matt Ray ([matt@chef.io](mailto:matt@chef.io))
- Author:: Joshua Timberman ([joshua@chef.io](mailto:joshua@chef.io))
- Author:: Sean OMeara ([someara@chef.io](mailto:someara@chef.io))

```text
Copyright:: 2011 Eric G. Wolfe
Copyright:: 2013-2016 Chef Software, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
# chef-ingredient Cookbook
[![Build Status](https://travis-ci.org/chef-cookbooks/chef-ingredient.svg?branch=master)](https://travis-ci.org/chef-cookbooks/chef-ingredient) [![Cookbook Version](https://img.shields.io/cookbook/v/chef-ingredient.svg)](https://supermarket.chef.io/cookbooks/chef-ingredient)

This cookbook provides primitives - helpers and resources - to manage Chef Software, Inc.'s products and add-ons including, but not limited to:

- Chef Server 12
- Chef Analytics
- Chef Delivery
- Chef Push
- Supermarket

It will perform component installation and configuration. It provides no recipes. Instead, wrapper cookbooks should be created using the resources that this cookbook provides.

## Maintainers and Support

This cookbook is maintained and supported by Chef's engineering services team. This cookbook runs through our internal Chef Delivery system, and changes must be approved by a member of engineering services.

## Requirements

Chef version 12.5.0 or higher, latest/current version is always recommended.

For local development, you need ChefDK 0.9.0 or newer.

### Platform

- Ubuntu 12.04, 14.04
- CentOS 6, 7

## Resources

### chef_server_ingredient

This is a backwards compatibility shim for the `chef_ingredient` resource.

This may be removed in a future version.

### chef_ingredient

A "chef ingredient" is the core package itself, or products or add-on components published by Chef Software, Inc. This resource manages the installation, configuration, and running the `ctl reconfigure` of individual packages.

By default, `chef_ingredient` will install using the `packages.chef.io` stable repository depending on the platform. However, it can be configured to use a custom repository by setting the `node['chef-ingredient']['custom-repo-recipe']` attribute (nil by default).

#### Actions

- `install` - (default) Configures the package repository and installs the specified package.
- `uninstall` - Uninstalls the specified package.
- `remove` - Alias for uninstall
- `reconfigure` - Performs the `ctl reconfigure` command for the package.

#### Properties

- `product_name`: (name attribute) The product name. See the [PRODUCT_MATRIX.md](https://github.com/chef/mixlib-install/blob/master/PRODUCT_MATRIX.md). For example, `chef-server`, `analytics`, `delivery`, `manage`, etc.
- `config`: String content that will be added to the configuration file of the given product.
- `ctl_command`: The "ctl" command, e.g., `chef-server-ctl`. This should be automatically detected by the library helper method `chef_ctl_command`, but may need to be specified if something changes, like a new add-on is made available.
- `options`: Options passed to the `package` resource used for installation.
- `version`: Package version to install. Can be specified in various semver-alike ways: `12.0.4`, `12.0.3-rc.3`, and also `:latest`/`'latest'`. Do not use this property when specifying `package_source`. Default is `:latest`, which will install the latest package from the repository.
- `channel`: Channel to install the products from. It can be `:stable` (default), `:current` or `:unstable`.
- `package_source`: Full path to a location where the package is located. If present, this file is used for installing the package. Default `nil`.
- `timeout`: The amount of time (in seconds) to wait to fetch the installer before timing out. Default: default timeout of the Chef package resource - `900` seconds.
- `accept_license`: A boolean value that specifies if license should be accepted if it is asked for during `reconfigure`action. This option is applicable to only these products: manage, analytics, reporting and compliance. Default: `false`.

### omnibus_service

Manages a sub-service within the context of a Chef product package. For example the `rabbitmq` service that is run for the Chef Server.

#### Actions

This delegates to the ctl command the service management command specified in the action. Not all the service management commands are supported, however, as not all of them would make sense when used in a recipe. This resource is primarily used for sending or receiving notifications. See the example section.

#### Properties

- `ctl_command`: The "ctl" command, e.g. `chef-server-ctl`. This should be automatically detected by the library helper method `chef_ctl_command`, but may need to be specified if something changes, like a  new add-on is made available.
- `service_name`: (name attribute) The name of the service to manage. Specify this like `product_name/service`, for example, `chef-server/rabbitmq`.

### ingredient_config

Makes it easy to create update configuration files of each Chef product. It uses the default locations for each product.

#### Actions

- `render` - (default) Creates the configuration file using the options passed in via `add` action or `config` attribute of `chef_ingredient` resource.
- `add` - Adds the `config` attribute contents to the data collection.  Must run `:render` action to generate the file.

#### Properties
- `product_name`: (name attribute) The product name. See the [PRODUCT_MATRIX.md](https://github.com/chef/mixlib-install/blob/master/PRODUCT_MATRIX.md). For example, `chef-server`, `analytics`, `delivery`, `manage`, etc.
- `sensitive`: (default `false`) Set to mask the config contents in logs. Use when you config contains information like passwords or secrets.
- `config`: String content that will be added to the configuration file of the given product.

#### Examples

We may need to restart the RabbitMQ service on the Chef Server, for example when adding configuration for Chef Analytics.

```ruby
template '/etc/opscode/chef-server.rb' do
  notifies :restart, 'omnibus_service[chef-server-core/rabbitmq]'
end

omnibus_service 'chef-server-core/rabbitmq' do
  action :nothing
end
```

To install Chef Server using some custom configuration options:

```ruby
chef_ingredient "chef-server" do
  config <<-EOS
api_fqdn "#{node["fqdn"]}"
ip_version "ipv6"
notification_email "#{node["chef_admin"]}"
nginx["ssl_protocols"] = "TLSv1 TLSv1.1 TLSv1.2"
EOS
  action :install
end

ingredient_config "chef-server" do
  notifies :reconfigure, "chef_ingredient[chef-server]"
end

```

To install or upgrade lastest version of Chef Client on your nodes:

```ruby
chef_ingredient "chef" do
  action :upgrade
  version :latest
end
```

To install an addon of Chef Server from `:current` channel:

```ruby
chef_ingredient 'chef-server' do
  channel :stable
  action :install
end

chef_ingredient 'analytics' do
  channel :current
  action :install
end

```

## License and Author

- Author: Joshua Timberman <joshua@chef.io>
- Author: Serdar Sutay <serdar@chef.io>
- Copyright (C) 2014-2015, Chef Software Inc. <legal@chef.io>

    Licensed under the Apache License, Version 2.0 (the "License");
    you may not use this file except in compliance with the License.
    You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

    Unless required by applicable law or agreed to in writing, software
    distributed under the License is distributed on an "AS IS" BASIS,
    WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
    See the License for the specific language governing permissions and
    limitations under the License.
# Windows SDK Cookbook

## Description
This cookbook installs the Windows 8.1 SDK. More information about the SDK
can be found at https://msdn.microsoft.com/en-us/windows/desktop/bg162891.aspx

## Usage

This cookbook provides a resource that can be used to install and uninstall
features provided with the Windows SDK.

### windows_sdk_feature Resource

#### Actions
- `:install`: Default. Install the given feature(s)
- `:uninstall`: Uninstall the given feature(s)

#### Attribute Parameters
- `:features`: Name Attribute. A feature(Symbol), an Array of features, or `:all`

  Valid features:
  - `:windows_software_development_kit`: The Microsoft Windows Software 
  Development Kit for Windows 8.1
  - `:windows_performance_kit`: Windows Performance Toolkit
  - `:debugging_tools`: Debugging Tools for Windows
  - `:application_verifier`: Application Verifier for Windows
  - `:windows_app_certification_kit`: Windows App Certification Kit
  - `:msi_tools`: MSI Tools
  - `:netfx_software_development_kit`: .Net Frame 4.5 Software Development Kit

- `:install_path`: Optional. The location where the SDK will be installed

#### Examples

Install all features:

```ruby
windows_sdk_feature :all
```

Install only the debugging tools and MSI tools

```ruby
windows_sdk_feature [:debugging_tools, :msi_tools]
```

Uninstall the MSI tools

```ruby
windows_sdk_feature :msi_tools do
  action :uninstall
end
```

## License

Copyright:: 2015, Chef Software

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.

# WIX Cookbook
[![Build Status](https://travis-ci.org/chef-cookbooks/wix.svg?branch=master)](http://travis-ci.org/chef-cookbooks/wix) [![Cookbook Version](https://img.shields.io/cookbook/v/wix.svg)](https://supermarket.chef.io/cookbooks/wix)

The [Windows Installer XML](http://wixtoolset.org/) (WiX) is a toolset that builds Windows installation packages from XML source code. The toolset supports a command line environment that developers may integrate into their build processes to build MSI and MSM setup packages. This cookbook installs the full WiX suite of tools.

## Requirements
### Platforms
- Windows Vista
- Windows 7
- Windows Server 2008 (R1, R2)
- Windows 8, 8.1
- Windows Server 2012 (R1, R2)

### Chef
- Chef 11+

### Cookbooks
- windows 1.38.2+

## Attributes
- `node['wix']['home']` - location to install WiX files to.  default is `%SYSTEMDRIVE%\wix`
- `node['wix']['download_id']` - CodePlex download id of the WiX binaries to install. default is `1540241` (WiX v3.10.2)
- `node['wix']['checksum']` - SHA256 of the WiX binaries zip file. default is `03b8f46cb3abf1465fe8f9975a94a4e0f75c77267ff4d1fcb6d5b6a97567f549`

## Usage
###default.rb

Downloads and installs WiX to the location specified by `node['wix']['home']`. Also ensures `node['wix']['home']` is in the system path.

## License & Authors
**Author:** Cookbook Engineering Team ([cookbooks@chef.io](mailto:cookbooks@chef.io))

**Copyright:** 2011-2015, Chef Software, Inc.

```text
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
# Rebar Fixtures

This directory is copied from the `src/oc_erchef/deps` directory of the Chef
Server source code, after running `./rebar get-deps` in that directory.

To reduce the amount of data, everything except for top-level files has
been removed via `find . -type d -depth 2 -exec rm -rf '{}' \;`

See also:

* https://github.com/chef/chef-server
MochiWeb is an Erlang library for building lightweight HTTP servers.

[![Build Status](https://secure.travis-ci.org/basho/mochiweb.png?branch=master)](http://travis-ci.org/basho/mochiweb)

The latest version of MochiWeb is available at http://github.com/mochi/mochiweb

The mailing list for MochiWeb is at http://groups.google.com/group/mochiweb/

R12B compatibility:
The master of MochiWeb is tested with R14A and later. A branch compatible
with R12B is maintained separately at http://github.com/lemenkov/mochiweb
The R12B branch of that repository is mirrored in the official repository
occasionally for convenience.

To create a new mochiweb using project:
   make app PROJECT=project_name

To create a new mochiweb using project in a specific directory:
   make app PROJECT=project_name PREFIX=$HOME/projects/
# Chef Authentication #

This is the authentication layer for chef.

Chef is a system integration framework written in erlang and ruby and designed to bring the benefits of configuration management to your entire infrastructure.

The Chef Wiki is the definitive source of user documentation.

    http://wiki.opscode.com/display/chef/Home

This README focuses on developers who want to modify Chef source code.  For users who just want to run the latest and greatest Chef development version in their environment, see:

   [TODO: add URL when available for erlang chef build process]

# DEVELOPMENT:

Before working on the code, if you plan to contribute your changes, you need to read the Opscode Contributing document.

    http://wiki.opscode.com/display/chef/How+to+Contribute

You will also need to set up the repository with the appropriate branches. We document the process on the Chef Wiki.

    http://wiki.opscode.com/display/chef/Working+with+git

Once your repository is set up, you can start working on the code.

# LINKS:

Source:

    https://github.com/opscode/chef_authn

Tickets/Issues:

    http://tickets.opscode.com/

Documentation:

    http://wiki.opscode.com/display/chef/Home/

# LICENSE:

Copyright 2011-2012 Opscode, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the License for the specific language governing permissions and limitations under the License.


# stats_hero your metrics and logging helper #

Copyright (c) 2012 Opscode, Inc.

__Authors:__ Seth Falcon ([`seth@opscode.com`](mailto:seth@opscode.com)).


### <a name="Overview">Overview</a> ###

The `stats_hero` application can help you instrument your Erlang
application with metrics that will be reported to `estatsd` and
browsable in Graphite.

### <a name="How_to_instrument_your_code_to_collect_metrics">How to instrument your code to collect metrics</a> ###

Include the `stats_hero.hrl` file. Wrap calls to upstream services
using the `?SH_TIME(ReqId, Mod, Fun, Args)` macro. Here's an example
from the `chef_db` module:

```
fetch_user(#context{reqid = ReqId, otto_connection = _Server} = _Context, UserName) ->
    case ?SH_TIME(ReqId, chef_sql, fetch_user, (UserName)) of
        {ok, not_found} ->
            not_found;
        {ok, #chef_user{}=User} ->
            User;
        {error, Error} ->
            {error, Error}
    end.
```

The `ReqId` argument is a request id generated by our front-end load
balancers (via nginx module). It is used to lookup a helper process
that aggregates metrics before sending them to estatsd. The macro
calls [`stats_hero:ctime/3`](http://github.com/opscode/stats_hero/blob/master/doc/stats_hero.md#ctime-3) and the `stats_hero` side of the computation is a
no-op if no worker process is found that matches the specified request
id. Note, however, that determining if there is a match requires the
`stats_hero` application to be running. So instrumented code will run
fine with a missing or crashed worker process, but will not function
if the `stats_hero` application is not running.

In order to generate consistent labels in graphite, `stats_hero`
maintains a mapping of module names to upstream names. The `Mod`
argument serves a double purpose: it is used as the module name for
the call to evaluate (and time) and it gets mapped to a generic
upstream name (e.g. `chef_sql` maps to `rdbms`). A future enhancement
would put this mapping in app config for `stats_hero`. If `Mod` is not
recognized, an error is raised.


### <a name="Sending_metrics_with_stats_hero">Sending metrics with stats_hero</a> ###

At the begining of your request, start a `stats_hero` worker process
using [`stats_hero_worker_sup:new_worker/1`](http://github.com/opscode/stats_hero/blob/master/doc/stats_hero_worker_sup.md#new_worker-1) like this:

```
    Config = [{estatsd_host, EstatsdServer},
              {estatsd_port, EstatsdPort},
              {request_id, ReqId},
              {my_app, "ChefAPI"},
              {request_label, RequestLabel},
              {request_action, atom_to_list(wrq:method(Req))},
              {upstream_prefixes, [<<"mysql">>, <<"couch">>, <<"authz">>, <<"solr">>]}],

stats_hero_worker_sup:new_worker(Config)
```

This will create the stats_hero worker and set the calling process as parent.
In the event the calling process terminates prior to cleaning up the worker,
then the stats_hero process will log and terminate gracefully.  It is
possible to change the monitored parent process using the reparent api.

```
stats_hero:reparent(ReqId),
```

You can also reparent using the two arity api where you supply a target process.

```
stats_hero:reparent(ReqId, Pid)
```

Then proceed to call code instrumented as described above. When your
request is complete, tell your worker process and it will send a total
time for the request to estatsd along with details on cummulative time
spent in the specified upstreams. Use [`stats_hero:report_metrics/2`](http://github.com/opscode/stats_hero/blob/master/doc/stats_hero.md#report_metrics-2)
for that. For example,

```
stats_hero:report_metrics(ReqId, Code),
```

Where `ReqId` is your request id as a binary and `Code` is an HTTP
response code (or similar integer).

Finally, you need to tell the `stats_hero` worker that you're done
with it. Use [`stats_her:stop_worker/1`](http://github.com/opscode/stats_hero/blob/master/doc/stats_her.md#stop_worker-1) for that.


### <a name="Obtaining_metrics_data_for_request_logging">Obtaining metrics data for request logging</a> ###

You can retrieve call timing and count data from your `stats_hero` worker using [`stats_hero:snapshot/2`](http://github.com/opscode/stats_hero/blob/master/doc/stats_hero.md#snapshot-2). This will return a proplist suitable for logging with the `fast_log` module tuple logger.

Here's the usage from `chef_rest_wm`:

```
log_request(Req, #base_state{reqid = ReqId, log_msg = Msg}) ->
    Status = wrq:response_code(Req),
    Tuples = [{req_id, ReqId},
              {status, Status},
              {method, wrq:method(Req)},
              {path, wrq:raw_path(Req)},
              {user, wrq:get_req_header("x-ops-userid", Req)},
              {msg, {raw, Msg}}],
    PerfTuples = stats_hero:snapshot(ReqId, agg),
    Level = log_level(Status),
    fast_log:Level(erchef, Tuples ++ PerfTuples).

log_level(Code) when Code >= 500 ->
    err;
log_level(_) ->
    info.
```


### <a name="Design_notes">Design notes</a> ###

The stats_hero workers are started using a `simple_one_for_one`
dynamic supervisor. Each worker updates a shared ETS table that
maintains a two-way mapping between worker pids and request ids.  The
workers also register with the `stats_hero_monitor` which monitors
each worker to ensure that the pid/reqid mapping is cleaned from the
ETS table when the worker exits. The top-level supervisor initializes
the ETS table.


#### <a name="Metrics_Reported_to_estatsd">Metrics Reported to estatsd</a> ####

Currently, the metrics sent to estatsd (UDP) are as follows and are
hard-coded into the stats_hero worker. At the start of a request, the
worker sends the following data:

```
1|167
test_hero.application.allRequests:1|m
test_hero.test-host.allRequests:1|m
test_hero.application.byRequestType.nodes.PUT:1|m
```
When [`stats_hero:report_metrics/2`](http://github.com/opscode/stats_hero/blob/master/doc/stats_hero.md#report_metrics-2) is called the worker sends:

```
1|640
test_hero.application.byStatusCode.200:1|m
test_hero.test-host.byStatusCode.200:1|m
test_hero.application.allRequests:108|h
test_hero.test-host.allRequests:108|h
test_hero.application.byRequestType.nodes.PUT:108|h
test_hero.upstreamRequests.rdbms:1200|h
test_hero.upstreamRequests.authz:100|h
test_hero.upstreamRequests.rdbms.nodes.put:200|h
test_hero.upstreamRequests.rdbms.nodes.fetch:1000|h
test_hero.upstreamRequests.authz.nodes.read:100|h
test_hero.application.byRequestType.nodes.PUT.upstreamRequests.rdbms:1200|h
test_hero.application.byRequestType.nodes.PUT.upstreamRequests.authz:100|h
```


#### <a name="Mapping_modules_to_upstream_labels">Mapping modules to upstream labels</a> ####

The current handling of upstream prefixes and module mappings is not
very flexible. You can specify a list of upstream prefixes when the
worker is initialized and any metrics (ctimer) with a label that
matches one of the prefixes will be appropriately aggregated in
reporting. However, the helper macro used to instrument code currently
relies on [`stats_hero:label/2`](http://github.com/opscode/stats_hero/blob/master/doc/stats_hero.md#label-2) which hard-codes a mapping of
module to upstream label. We'd like to make this configurable.


### <a name="LICENSE">LICENSE</a> ###

Copyright 2011-2012 Opscode, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you
may not use this file except in compliance with the License.  You may
obtain a copy of the License at [`http://www.apache.org/licenses/LICENSE-2.0`](http://www.apache.org/licenses/LICENSE-2.0)
Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied.  See the License for the specific language governing
permissions and limitations under the License.


## Modules ##


<table width="100%" border="0" summary="list of modules">
<tr><td><a href="http://github.com/opscode/stats_hero/blob/master/doc/stats_hero.md" class="module">stats_hero</a></td></tr>
<tr><td><a href="http://github.com/opscode/stats_hero/blob/master/doc/stats_hero_app.md" class="module">stats_hero_app</a></td></tr>
<tr><td><a href="http://github.com/opscode/stats_hero/blob/master/doc/stats_hero_monitor.md" class="module">stats_hero_monitor</a></td></tr>
<tr><td><a href="http://github.com/opscode/stats_hero/blob/master/doc/stats_hero_sender.md" class="module">stats_hero_sender</a></td></tr>
<tr><td><a href="http://github.com/opscode/stats_hero/blob/master/doc/stats_hero_sender_sup.md" class="module">stats_hero_sender_sup</a></td></tr>
<tr><td><a href="http://github.com/opscode/stats_hero/blob/master/doc/stats_hero_sup.md" class="module">stats_hero_sup</a></td></tr>
<tr><td><a href="http://github.com/opscode/stats_hero/blob/master/doc/stats_hero_worker_sup.md" class="module">stats_hero_worker_sup</a></td></tr></table>

[![Release](http://img.shields.io/github/release/eproxus/meck.svg?style=flat-square)](https://github.com/eproxus/meck/releases/latest)
[![Build Status](http://img.shields.io/travis/eproxus/meck.svg?style=flat-square)](http://travis-ci.org/eproxus/meck)
[![Code Climate](http://img.shields.io/badge/code_climate-Erlang_17.4-brightgreen.svg?style=flat-square)](https://travis-ci.org/eproxus/meck)

Meck
====

A mocking library for Erlang.

<a name='features'>

Features
--------

See what's new in [0.8 Release Notes][1].

  * Dynamic return values using sequences and loops of static values
  * Compact definition of mock arguments, clauses and return values
  * Pass through: call functions in the original module
  * Complete call history showing calls, return values and exceptions
  * Mock validation, will invalidate mocks that were not called correctly
  * Throwing of expected exceptions that keeps the module valid
  * Throws an error when mocking a module that doesn't exist or has been
    renamed (disable with option `non_strict`)
  * Support for [Hamcrest][2] matchers
  * Automatic backup and restore of cover data
  * Mock is linked to the creating process and will unload automatically
    when a crash occurs (disable with option `no_link`)
  * Mocking of sticky modules (using the option `unstick`)


<a name='examples'>

Examples
--------
Here's an example of using Meck in the Erlang shell:

```erl
Eshell V5.8.4  (abort with ^G)
1> meck:new(dog, [non_strict]). % non_strict is used to create modules that don't exist
ok
2> meck:expect(dog, bark, fun() -> "Woof!" end).
ok
3> dog:bark().
"Woof!"
4> meck:validate(dog).
true
5> meck:unload(dog).
ok
6> dog:bark().
** exception error: undefined function dog:bark/0
```

Exceptions can be anticipated by Meck (resulting in validation still
passing). This is intended to be used to test code that can and should
handle certain exceptions indeed does take care of them:

```erl
5> meck:expect(dog, meow, fun() -> meck:exception(error, not_a_cat) end).
ok
6> catch dog:meow().
{'EXIT',{not_a_cat,[{meck,exception,2},
                    {meck,exec,4},
                    {dog,meow,[]},
                    {erl_eval,do_apply,5},
                    {erl_eval,expr,5},
                    {shell,exprs,6},
                    {shell,eval_exprs,6},
                    {shell,eval_loop,3}]}}
7> meck:validate(dog).
true
```

Normal Erlang exceptions result in a failed validation. The following
example is just to demonstrate the behavior, in real test code the
exception would normally come from the code under test (which should,
if not expected, invalidate the mocked module):

```erl
8> meck:expect(dog, jump, fun(Height) when Height > 3 ->
                                  erlang:error(too_high);
                             (Height) ->
                                  ok
                          end).
ok
9> dog:jump(2).
ok
10> catch dog:jump(5).
{'EXIT',{too_high,[{meck,exec,4},
                   {dog,jump,[5]},
                   {erl_eval,do_apply,5},
                   {erl_eval,expr,5},
                   {shell,exprs,6},
                   {shell,eval_exprs,6},
                   {shell,eval_loop,3}]}}
11> meck:validate(dog).
false
```

Here's an example of using Meck inside an EUnit test case:

```erlang
my_test() ->
    meck:new(my_library_module),
    meck:expect(my_library_module, fib, fun(8) -> 21 end),
    ?assertEqual(21, code_under_test:run(fib, 8)), % Uses my_library_module
    ?assert(meck:validate(my_library_module)),
    meck:unload(my_library_module).
```

Pass-through is used when the original functionality of a module
should be kept. When the option `passthrough` is used when calling
`new/2` all functions in the original module will be kept in the
mock. These can later be overridden by calling `expect/3` or
`expect/4`.

```erl
Eshell V5.8.4  (abort with ^G)
1> meck:new(string, [unstick, passthrough]).
ok
2> string:strip("  test  ").
"test"
```

It's also possible to pass calls to the original function allowing us
to override only a certain behavior of a function (this usage is
compatible with the `passthrough` option). `passthrough/1` will always
call the original function with the same name as the expect is 
defined in):

```erl
Eshell V5.8.4  (abort with ^G)
1> meck:new(string, [unstick]).
ok
2> meck:expect(string, strip, fun(String) -> meck:passthrough([String]) end).
ok
3> string:strip("  test  ").
"test"
4> meck:unload(string).
ok
5> string:strip("  test  ").
"test"
```

<a name='build'>

Build
-----

Meck requires `make` and [rebar][1] to build. To build Meck go to the Meck directory
and simply type:

```sh
make
```

In order to run all tests for Meck type the following command from the same directory:

```sh
make test
```

Two things might seem alarming when running the tests:

  1. Warnings emitted by cover
  2. An exception printed by SASL

Both are expected due to the way Erlang currently prints errors. The
important line you should look for is `All XX tests passed`, if that
appears all is correct.

Documentation can be generated through the use of the following command:

```sh
make doc
```

<a name='install'>

Install
-------

Meck is best used via [rebar][3]. Add the following dependency t
your `rebar.config` in your project root:

```erlang
{deps, [
 {meck, ".*",
  {git, "https://github.com/eproxus/meck.git", {tag, "0.8.2"}}}
 ]}.
```

If you want to install your own built version of Meck add the ebin
directory to your Erlang code path or move the Meck folder into your
release folder and make sure that folder is in your `ERL_LIBS`
environment variable.


<a name='contribute'>

Caveats
-------

Meck will have trouble mocking certain modules since Meck works by
recompiling and reloading modules. Since Erlang have a flat module
namespace, replacing a module has to be done globally in the
Erlang VM. This means certain modules cannot be mocked. The
following is a non-exhaustive list of modules that can either be
problematic to mock or not possible at all:

* `erlang`
* `os`
* `crypto`
* `compile`

Contribute
----------

Patches are greatly appreciated! For a much nicer history, please
[write good commit messages][5]. Use a branch name prefixed by
`feature/` (e.g. `feature/my_example_branch`) for easier integration
when developing new features or fixes for meck.

Should you find yourself using Meck and have issues, comments or
feedback please [create an issue here on GitHub][4].

Contributors:

- Maxim Vladimirsky (@horkhe)
- Ryan Zezeski (@rzezeski)
- David Haglund (@daha)
- Magnus Henoch (@legoscia)
- Susan Potter (@mbbx6spp)
- Andreas Amsenius (@adbl)
- Anthony Molinaro (@djnym)
- Matt Campbell (@xenolinguist)
- Martynas Pumputis (@brb)
- Shunichi Shinohara (@shino)
- Miëtek Bak
- Henry Nystrom
- Ward Bekker (@wardbekker)
- Damon Richardson
- Christopher Meiklejohn
- Joseph Wayne Norton (@norton)
- Erkan Yilmaz (@Erkan-Yilmaz)
- Joe Williams (@joewilliams)
- Russell Brown
- Michael Klishin (@michaelklishin)
- Magnus Klaar


  [1]: https://github.com/eproxus/meck/wiki/0.8-Release-Notes
       "0.8 Release Notes"
  [2]: https://github.com/hyperthunk/hamcrest-erlang "Hamcrest for Erlang"
  [3]: https://github.com/basho/rebar "Rebar - A build tool for Erlang"
  [4]: http://github.com/eproxus/meck/issues "Meck issues"


# Edown - Markdown generated from Edoc #

Copyright (c) 2010 Erlang Solutions Ltd


__Authors:__ [`ulf.wiger@feuerlabs.com`](mailto:ulf.wiger@feuerlabs.com).


Status:
------
More-or-less readable Markdown can be generated.
A doclet needs to be written that also creates 
a markdown-based index and overview. Currently, the 
edoc_doclet creates an index.html and overview.html,
which do not point to the .md files.

To generate markdown edoc, run:

```

edoc:application(App, [{doclet, edown_doclet} | OtherOpts]).

```

The `edown_xmerl` module is used as an xmerl export module.
It converts xmerl's "simple xml" to Markdown syntax. Note that
GH-flavored Markdown allows HTML markup (at least common tags),
but doesn't expand markdown markup inside HTML markup, so the`edown_xmerl` module has to know the context in which it operates.

** Special edown option: **

Using the option `{top_level_readme, {File, BaseHref}}`, a github-friendly
`README.md` in the top directory can be generated from the `overview.edoc`.
This file is the same as the `doc/README.md` file already generated,
but with relative links corrected (using `BaseHref`) so that they actually
work. This step is needed since Github doesn't support relative paths in
Markdown links.

Example:

`{top_level_readme, {"./README.md", "http://github.com/esl/edown"}}`

The conversion function will fetch the current branch name from git,
and fail if it cannot do so.

Rebar customizations
====================
A set of escripts can be found under
[edown/priv/scripts/](http://github.com/esl/edown/blob/master/priv/scripts/), which
can be used to customize the `rebar` built process. The
[rebar.config.script](http://github.com/esl/edown/blob/master/priv/scripts/rebar.config.script)
file should be copied into your application, next to `rebar.config`.
It will sense if `doc` is a current target, and will then include
`edown` in the `deps`; otherwise, it removes it. This way, you will
not have to pull down `edown` unless you really want to build the
docs. It will also locate edown along your path, in which case
it doesn't need to pull it down again.

The script will also start the `inets` application, so that you
can include URLs as part of a `doc_path` option (see below).

Links to other EDown-generated docs
===================================
There is a way to configure Edoc/Edown to get URLs right even
when linking to other Edown-generated docs on Github.

First, you need to specify paths to the `edoc-info` files for
each repository as part of `edoc_opts` in your rebar.config, e.g.

```
   {doc_path, ["http://raw.github.com/uwiger/setup/master/doc",
               "http://raw.github.com/uwiger/gproc/master/doc"]}
```

Note (1) that we use "http:://...", not "https://...", since
Edoc doesn't recognize the latter. Also note that we use URLs
to the raw files. This is for Edoc as it fetches the `edoc-info`
files. Edown will detect and rewrite such links in the generated
output, since "raw" links wouldn't work for the markdown files.

The next issue is that Edoc uses httpd_client to fetch the
`edoc-info` files, which requires `inets` to be started. To
further complicate matters, `ssl` (and thus `crypto` and
`public_key`) must also be started, since Github will
redirect to https.

One way to solve this is to use the escripts found under
`edown/priv/scripts`.

NOTE
====
EDoc provides a plugin structure, so that one may specify own 
layout modules, export modules, and doclets. However, there is 
some overlap esp. between the layout and doclet modules, and 
several functions are expected to produce files on their own.
This causes a problem for EDown, since it cannot handle frames.
Instead, it would probably like to create one overview file with
different sections. It would have been better to have a framework
where some plugin functions identify the different files to be 
written, and the outline of each, other plugins convert to suitable
content representation (e.g. HTML or Markdown), and EDoc then 
writes the files necessary.

For now, EDown focuses on producing reasonable Markdown, rather
than complying fully with the plugin framework. That is, the 
edown_doclet module will not go out of its way to function together
with any other layout module than edown_layout, and vice versa.

markedoc
========

The sed script bin/markedoc works in the opposite direction and converts 
your `README.md` to an `EDoc` file. 

See [bin/MARKEDOC-README.md](http://github.com/esl/edown/blob/master/bin/MARKEDOC-README.md).

**FreeBSD, Mac OS X**`$ sed -E -f markedoc.sed <markdown file> > <edoc file>`

**Linux**`$ sed -r -f markedoc.sed <markdown file> > <edoc file>`


## Modules ##


<table width="100%" border="0" summary="list of modules">
<tr><td><a href="http://github.com/esl/edown/blob/master/doc/edown_doclet.md" class="module">edown_doclet</a></td></tr>
<tr><td><a href="http://github.com/esl/edown/blob/master/doc/edown_layout.md" class="module">edown_layout</a></td></tr>
<tr><td><a href="http://github.com/esl/edown/blob/master/doc/edown_lib.md" class="module">edown_lib</a></td></tr>
<tr><td><a href="http://github.com/esl/edown/blob/master/doc/edown_make.md" class="module">edown_make</a></td></tr>
<tr><td><a href="http://github.com/esl/edown/blob/master/doc/edown_xmerl.md" class="module">edown_xmerl</a></td></tr></table>

# Erlang PostgreSQL Database Client

Asynchronous fork of [wg/epgsql](https://github.com/wg/epgsql) originally here:
[mabrek/epgsql](https://github.com/mabrek/epgsql) and subsequently forked in order to
provide a common fork for community development.

## Motivation

When you need to execute several queries, it involves a number network
round-trips between the application and the database.
The PostgreSQL frontend/backend protocol supports request pipelining.
This means that you don't need to wait for the previous command to finish
before sending the next command. This version of the driver makes full use
of the protocol feature that allows faster execution.


## Difference highlights

- 3 API sets:
  - **epgsql** maintains backwards compatibility with the original driver API
  - **epgsqla** delivers complete results as regular erlang messages
  - **epgsqli** delivers results as messages incrementally (row by row)
- internal queue of client requests, so you don't need to wait for the response
  to send the next request
- single process to hold driver state and receive socket data
- execution of several parsed statements as a batch
- binding timestamps in `erlang:now()` format

see `CHANGES` for full list.

### Differences between current epgsql and mabrek's original async fork:

- Unnamed statements are used unless specified otherwise. This may
  cause problems for people attempting to use the same connection
  concurrently, which will no longer work.

## Known problems

- SSL performance can degrade if the driver process has a large inbox
  (thousands of messages).

## Usage
### Connect

```erlang
-type host() :: inet:ip_address() | inet:hostname().

-type connect_option() ::
    {database, DBName     :: string()}             |
    {port,     PortNum    :: inet:port_number()}   |
    {ssl,      IsEnabled  :: boolean() | required} |
    {ssl_opts, SslOptions :: [ssl:ssl_option()]}   | % @see OTP ssl app, ssl_api.hrl
    {timeout,  TimeoutMs  :: timeout()}            | % default: 5000 ms
    {async,    Receiver   :: pid()}. % process to receive LISTEN/NOTIFY msgs
    
-spec connect(host(), string(), string(), [connect_option()])
        -> {ok, Connection :: connection()} | {error, Reason :: connect_error()}.    
%% @doc connects to Postgres
%% where
%% `Host'     - host to connect to
%% `Username' - username to connect as, defaults to `$USER'
%% `Password' - optional password to authenticate with
%% `Opts'     - proplist of extra options
%% returns `{ok, Connection}' otherwise `{error, Reason}'
connect(Host, Username, Password, Opts) -> ...
```
example:
```erlang
{ok, C} = epgsql:connect("localhost", "username", "psss", [
    {database, "test_db"},
    {timeout, 4000}
]),
...
ok = epgsql:close(C).
```

The `{timeout, TimeoutMs}` parameter will trigger an `{error, timeout}` result when the
socket fails to connect within `TimeoutMs` milliseconds.

Asynchronous connect example (applies to **epgsqli** too):

```erlang
  {ok, C} = epgsqla:start_link(),
  Ref = epgsqla:connect(C, "localhost", "username", "psss", [{database, "test_db"}]),
  receive
    {C, Ref, connected} ->
        {ok, C};
    {C, Ref, Error = {error, _}} ->
        Error;
    {'EXIT', C, _Reason} ->
        {error, closed}
  end.
```

### Simple Query

```erlang
-type query() :: string() | iodata().
-type squery_row() :: {binary()}.

-record(column, {
    name :: binary(),
    type :: epgsql_type(),
    size :: -1 | pos_integer(),
    modifier :: -1 | pos_integer(),
    format :: integer()
}).

-type ok_reply(RowType) ::
    {ok, Count :: non_neg_integer()} |                                                            % select
    {ok, ColumnsDescription :: [#column{}], RowsValues :: [RowType]} |                            % update/insert
    {ok, Count :: non_neg_integer(), ColumnsDescription :: [#column{}], RowsValues :: [RowType]}. % update/insert + returning
-type error_reply() :: {error, query_error()}.
-type reply(RowType) :: ok_reply() | error_reply().

-spec squery(connection(), query()) -> reply(squery_row()) | [reply(squery_row())].
%% @doc runs simple `SqlQuery' via given `Connection'
squery(Connection, SqlQuery) -> ...
```
examples:
```erlang
InsertRes = epgsql:squery(C, "insert into account (name) values  ('alice'), ('bob')"),
io:format("~p~n", [InsertRes]),
```
> ```
{ok,2}
```

```erlang
SelectRes = epgsql:squery(C, "select * from account"),
io:format("~p~n", [SelectRes]).
```
> ```
{ok,
    [{column,<<"id">>,int4,4,-1,0},{column,<<"name">>,text,-1,-1,0}],
    [{<<"1">>,<<"alice">>},{<<"2">>,<<"bob">>}]
}
```

```erlang
InsertReturningRes = epgsql:squery(C, 
    "insert into account(name)"
    "    values ('joe'), (null)"
    "    returning *"),
io:format("~p~n", [InsertReturningRes]).
```
> ```
{ok,2,
    [{column,<<"id">>,int4,4,-1,0}, {column,<<"name">>,text,-1,-1,0}],
    [{<<"3">>,<<"joe">>},{<<"4">>,null}]
}
```

```erlang
{error, Reason} = epgsql:squery(C, "insert into account values (1, 'bad_pkey')"),
io:format("~p~n", [Reason]).
```
> ```
{error,
    error,
    <<"23505">>,
    <<"duplicate key value violates unique constraint \"account_pkey\"">>,
    [{detail,<<"Key (id)=(1) already exists.">>}]
}
```

The simple query protocol returns all columns as binary strings
and does not support parameters binding.

Several queries separated by semicolon can be executed by squery.

```erlang
  [{ok, _, [{<<"1">>}]}, {ok, _, [{<<"2">>}]}] = epgsql:squery(C, "select 1; select 2").
```

`epgsqla:squery/2` returns result as a single message:

```erlang
  Ref = epgsqla:squery(C, Sql),
  receive
    {C, Ref, Result} -> Result
  end.
```

Result has the same format as return value of `epgsql:squery/2`.

`epgsqli:squery/2` returns results incrementally for each query inside Sql and for each row:

```erlang
Ref = epgsqli:squery(C, Sql),
receive
  {C, Ref, {columns, Columns}} ->
      %% columns description
      Columns;
  {C, Ref, {data, Row}} ->
      %% single data row
      Row;
  {C, Ref, {error, _E} = Error} ->
      Error;
  {C, Ref, {complete, {_Type, Count}}} ->
      %% execution of one insert/update/delete has finished
      {ok, Count}; % affected rows count
  {C, Ref, {complete, _Type}} ->
      %% execution of one select has finished
      ok;
  {C, Ref, done} ->
      %% execution of all queries from Sql has been finished
      done;
end.
```

## Extended Query

```erlang
{ok, Columns, Rows}        = epgsql:equery(C, "select ...", [Parameters]).
{ok, Count}                = epgsql:equery(C, "update ...", [Parameters]).
{ok, Count, Columns, Rows} = epgsql:equery(C, "insert ... returning ...", [Parameters]).
{error, Error}             = epgsql:equery(C, "invalid SQL", [Parameters]).
```
`Parameters` - optional list of values to be bound to `$1`, `$2`, `$3`, etc.

The extended query protocol combines parse, bind, and execute using
the unnamed prepared statement and portal. A `select` statement returns
`{ok, Columns, Rows}`, `insert/update/delete` returns `{ok, Count}` or
`{ok, Count, Columns, Rows}` when a `returning` clause is present. When
an error occurs, all statements result in `{error, #error{}}`.

```erlang
SelectRes = epgsql:equery(C, "select id from account where name = $1", ["alice"]),
io:format("~p~n", [SelectRes]).
```
> ```
{ok,
    [{column,<<"id">>,int4,4,-1,1}],
    [{1}]
}
```

PostgreSQL's binary format is used to return integers as Erlang
integers, floats as floats, bytes/text/varchar columns as binaries,
bools as true/false, etc. For details see `pgsql_binary.erl` and the
Data Representation section below.

Asynchronous API `epgsqla:equery/3` requires you to parse statement beforehand

```erlang
Ref = epgsqla:equery(C, Statement, [Parameters]),
receive
  {C, Ref, Res} -> Res
end.
```

- `Statement` - parsed statement (see parse below)
- `Res` has same format as return value of `epgsql:equery/3`.

`epgsqli:equery(C, Statement, [Parameters])` sends same set of messages as
squery including final `{C, Ref, done}`.


## Parse/Bind/Execute

```erlang
{ok, Statement} = epgsql:parse(C, [StatementName], Sql, [ParameterTypes]).
```

- `StatementName`   - optional, reusable, name for the prepared statement.
- `ParameterTypes`  - optional list of PostgreSQL types for each parameter.

For valid type names see `pgsql_types.erl`.

`epgsqla:parse/2` sends `{C, Ref, {ok, Statement} | {error, Reason}}`.
`epgsqli:parse/2` sends:
 - `{C, Ref, {types, Types}}`
 - `{C, Ref, {columns, Columns}}`
 - `{C, Ref, no_data}` if statement will not return rows
 - `{C, Ref, {error, Reason}}`

```erlang
ok = epgsql:bind(C, Statement, [PortalName], ParameterValues).
```

- `PortalName`      - optional name for the result portal.

both `epgsqla:bind/3` and `epgsqli:bind/3` send `{C, Ref, ok | {error, Reason}}`

```erlang
{ok | partial, Rows} = epgsql:execute(C, Statement, [PortalName], [MaxRows]).
{ok, Count}          = epgsql:execute(C, Statement, [PortalName]).
{ok, Count, Rows}    = epgsql:execute(C, Statement, [PortalName]).
```

- `PortalName`      - optional portal name used in `epgsql:bind/4`.
- `MaxRows`         - maximum number of rows to return (0 for all rows).

`epgsql:execute/3` returns `{partial, Rows}` when more rows are available.

`epgsqla:execute/3` sends `{C, Ref, Result}` where `Result` has same format as
return value of `epgsql:execute/3`.

`epgsqli:execute/3` sends
- `{C, Ref, {data, Row}}`
- `{C, Ref, {error, Reason}}`
- `{C, Ref, suspended}` partial result was sent, more rows are available
- `{C, Ref, {complete, {_Type, Count}}}`
- `{C, Ref, {complete, _Type}}`

```erlang
ok = epgsql:close(C, Statement).
ok = epgsql:close(C, statement | portal, Name).
ok = epgsql:sync(C).
```

All epgsql functions return `{error, Error}` when an error occurs.

`epgsqla`/`epgsqli` modules' `close` and `sync` functions send `{C, Ref, ok}`.


## Batch execution

Batch execution is `bind` + `execute` for several prepared statements.
It uses unnamed portals and `MaxRows = 0`.

```erlang
Results = epgsql:execute_batch(C, Batch).
```

- `Batch`   - list of {Statement, ParameterValues}
- `Results` - list of {ok, Count} or {ok, Count, Rows}

example:

```erlang
{ok, S1} = epgsql:parse(C, "one", "select $1", [int4]),
{ok, S2} = epgsql:parse(C, "two", "select $1 + $2", [int4, int4]),
[{ok, [{1}]}, {ok, [{3}]}] = epgsql:execute_batch(C, [{S1, [1]}, {S2, [1, 2]}]).
```

`epgsqla:execute_batch/3` sends `{C, Ref, Results}`
`epgsqli:execute_batch/3` sends
- `{C, Ref, {data, Row}}`
- `{C, Ref, {error, Reason}}`
- `{C, Ref, {complete, {_Type, Count}}}`
- `{C, Ref, {complete, _Type}}`
- `{C, Ref, done}` - execution of all queries from Batch has finished


## Data Representation
PG type       | Representation
--------------|-------------------------------------
  null        | `null`
  bool        | `true` | `false`
  char        | `$A` | `binary`
  intX        | `1`
  floatX      | `1.0`
  date        | `{Year, Month, Day}`
  time        | `{Hour, Minute, Second.Microsecond}`
  timetz      | `{time, Timezone}`
  timestamp   | `{date, time}`
  timestamptz | `{date, time}`
  interval    | `{time, Days, Months}`
  text        | `<<"a">>`
  varchar     | `<<"a">>`
  bytea       | `<<1, 2>>`
  array       | `[1, 2, 3]`
  record      | `{int2, time, text, ...}` (decode only)
  point       |  `{10.2, 100.12}`
  int4range   | `[1,5)`

  `timestamp` and `timestamptz` parameters can take `erlang:now()` format: `{MegaSeconds, Seconds, MicroSeconds}`

  `int4range` is a range type for ints (bigint not supported yet) that obeys inclusive/exclusive semantics,
  bracket and parentheses respectively. Additionally, infinities are represented by the atoms `minus_infinity`
  and `plus_infinity`

## Errors

Errors originating from the PostgreSQL backend are returned as `{error, #error{}}`,
see `epgsql.hrl` for the record definition. `epgsql` functions may also return
`{error, What}` where `What` is one of the following:

- `{unsupported_auth_method, Method}`     - required auth method is unsupported
- `timeout`                               - request timed out
- `closed`                                - connection was closed
- `sync_required`                         - error occured and epgsql:sync must be called

## Server Notifications

PostgreSQL may deliver two types of asynchronous message: "notices" in response
to notice and warning messages generated by the server, and "notifications" which
are generated by the `LISTEN/NOTIFY` mechanism.

Passing the `{async, Pid}` option to `epgsql:connect/3` will result in these async
messages being sent to the specified process, otherwise they will be dropped.

Message formats:

```erlang
{epgsql, Connection, {notification, Channel, Pid, Payload}}
```
- `Connection`  - connection the notification occurred on
- `Channel`  - channel the notification occurred on
- `Pid`  - database session pid that sent notification
- `Payload`  - optional payload, only available from PostgreSQL >= 9.0

```erlang
{epgsql, Connection, {notice, Error}}
```
- `Connection`  - connection the notice occurred on
- `Error`       - an `#error{}` record, see `epgsql.hrl`


## Mailing list

  [Google groups](https://groups.google.com/forum/#!forum/epgsql)

## Contributing

epgsql is a community driven effort - we welcome contributions!
Here's how to create a patch that's easy to integrate:

* Create a new branch for the proposed fix.
* Make sure it includes a test and documentation, if appropriate.
* Open a pull request against the `devel` branch of epgsql.
* Passing build in travis

## Test Setup

In order to run the epgsql tests, you will need to set up a local
Postgres database that runs within its own, self-contained directory,
in order to avoid modifying the system installation of Postgres.

NOTE: you will need the postgis and hstore extensions to run these
tests!  On Ubuntu, you can install them with a command like this:

    apt-get install postgresql-9.3-postgis-2.1 postgresql-contrib

1. `./setup_test_db.sh` # This sets up an installation of Postgres in datadir/

2. `./start_test_db.sh` # Starts a Postgres instance on its own port (10432).

3. `make create_testdbs` # Creates the test database environment.

4. `make test` # Runs the tests

[![Build Status Master](https://travis-ci.org/chef/epgsql-1.svg?branch=master)](https://travis-ci.org/chef/epgsql-1)
# opscoderl_folsom #

Opscode helpers for instrumenting Erlang apps with folsom
metrics. Here you will find the module `oc_folsom` that will help you
standardize folsom metric labels and a convenience function for
instrumenting a bit of code such that you capture the run time in a
histogram and fire a meter metric all in one call
(`oc_folsom:time/2`).

# Guidelines for opscoderl helper repos #

This repository is the first in what we hope will be a useful pattern
for collecting reusable Erlang code. The idea is to balance the
extremes of a dumping ground "commons" repo that would force consumers
to pull in dependencies that they won't use with a proliferation of
single module repos (hi, that's what this is for now, sorry).

Helper repos should follow these guidelines:

1. Be named `opscoderl_$BLAH` where `$BLAH` names a dependency that
   is wrapped (e.g. this repo with folsom) OR a well defined bit of
   functionality. I think we will soon have an `opscoderl_json` repo
   that pulls in jiffy and ej.

2. Minimal focused set of dependencies. A dependency is reasonable if
   any user of the helper will want the dependency. Conversely, a
   dependency that covers a small or rare use case should be given
   extra scrutiny. As a consumer of a helper, it is unpleasant to have
   to pull in a dependency that you aren't going to use. A tag or git
   SHA should be used by the helper to peg the version of the
   dependency.

3. Modules should be prefixed with `oc_`. Care should be taken not to
   conflict with modules from other opscoderl helper applications.

4. Open source and not product specific. May contain some
   Opscode-isms, but the intention is that these helpers can be
   generally useful (like erlware_commons).

# Guidelines for using opscoderl helpers #

1. Contrary to normal practice, avoid specifying the dependencies
   provided by the helper even if you use them directly. For example,
   depend only on `opscoderl_folsom` and use `oc_folsom` and
   `folsom`. This allows the version of the wrapped dependencies to be
   controlled by the helper app. Care needs to be taken in managing
   OTP release when a non-helper app shares a dependency with a
   helper. We may need to add direct deps in some cases to get the
   right behavior out of rebar and lock deps.


## License ##

|                      |                                          |
|:---------------------|:-----------------------------------------|
| **Copyright:**       | Copyright (c) 2013 Opscode, Inc.
| **License:**         | Apache License, Version 2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


* webmachine
** Overview

[[http://travis-ci.org/basho/webmachine][Travis-CI]] :: [[https://secure.travis-ci.org/basho/webmachine.png]]

Webmachine is an application layer that adds HTTP semantic awareness
on top of the excellent bit-pushing and HTTP syntax-management
provided by mochiweb, and provides a simple and clean way to connect
that to your application's behavior.

More information is available [[http://webmachine.basho.com/][here]].

** Quick Start
A shell script is provided in the =webmachine= repository to help
users quickly and easily create a new =webmachine= application.

#+BEGIN_SRC shell
git clone git://github.com/basho/webmachine.git
cd webmachine
./scripts/new_webmachine.sh mydemo
#+END_SRC

A destination path can also be passed to the =new_webmachine.sh=
script.

#+BEGIN_SRC shell
./scripts/new_webmachine.sh mydemo ~/webmachine_applications
#+END_SRC

Once a new application has been created it can be built and started.

#+BEGIN_SRC shell
cd mydemo
make
./start.sh
#+END_SRC

The application will be available at [[http://localhost:8080]].

To learn more continue reading [[http://webmachine.basho.com/][here]].

** Contributing
   We encourage contributions to =webmachine= from the community.

   1) Fork the =webmachine= repository on [[https://github.com/basho/webmachine][Github]].
   2) Clone your fork or add the remote if you already have a clone of
      the repository.
#+BEGIN_SRC shell
git clone git@github.com:yourusername/webmachine.git
# or
git remote add mine git@github.com:yourusername/webmachine.git
#+END_SRC
   3) Create a topic branch for your change.
#+BEGIN_SRC shell
git checkout -b some-topic-branch
#+END_SRC
   4) Make your change and commit. Use a clear and descriptive commit
      message, spanning multiple lines if detailed explanation is
      needed.
   5) Push to your fork of the repository and then send a pull-request
      through Github.
#+BEGIN_SRC shell
git push mine some-topic-branch
#+END_SRC
   6) A Basho engineer or community maintainer will review your patch
      and merge it into the main repository or send you feedback.
rebar_vsn_plugin
================

NOTE
----

The rebar vsn plugin has a new feature where it can calculate a good
version for an Erlang app based solely on the *.app.src file. You
no longer need to place `semver` in your version field unless you
simply want to continue the old behaviour. The old behaviour is still
fully supported.

TLDR
----

This plugin will make accurate [semver](http://semver.org) compatible
version strings for your Erlang OTP Apps as long as you are doing
semver style versioning with tags 'v<version>'.

Use
---

Add the following dep specification to the deps tuple of your
`rebar.config`:

    {rebar_vsn_plugin, "",
         {git, "https://github.com/erlware/rebar_vsn_plugin.git",
          {branch, "master"}}},

Then inform rebar that you want this to be used as a plugin like so:

    {plugins, [rebar_vsn_plugin]}.

In Rebar, to make sure that the plugin is compiled and loaded before
the actual Rebar is started, you should add the following to your
Rebar config:

    {plugin_dir, "deps/rebar_vsn_plugin/src"}.

Then add the semver version to the `<app-name>.app.src` file. It
should go from something like:

    {application, rebar_vsn_plugin,
       [{description, "Correct version manipulation for rebar"},
        {vsn, git},
        {modules, []},
        {registered, []},
        {applications, [kernel, stdlib]}]}.

to this the actual version you are interested in using.

    {application, rebar_vsn_plugin,
       [{description, "Correct version manipulation for rebar"},
        {vsn, "0.0.5"},
        {modules, []},
        {registered, []},
        {applications, [kernel, stdlib]}]}.

The key change is having the version you wish to use `{vsn, "0.0.5"}`
in the version field.

If you wish to maintain the original 'tag oriented' behaviour you can
replace `{vsn, git}` with `{vsn, "semver"}`. This will give you the
same behaviour as the git approach, but with full semver versions.

So your app file would look as follows:

    {application, rebar_vsn_plugin,
       [{description, "Correct version manipulation for rebar"},
        {vsn, "semver"},
        {modules, []},
        {registered, []},
        {applications, [kernel, stdlib]}]}.


Explanation
-------------

This plugin is designed to take the latest semver
compatible tag and turn it into a semver compatible version for the
OTP Application. One of the key things it does (aside from making sure
that semver is respected) is insure that there is a unique
monotonically increasing version for each commit built. It does this
by creating a version from both the latest tag, the epoch timestamp and
the ref. The ref is actually only there to make the version human
readable.

So lets say you have a repository with the tag `v0.0.1` and the epoch
`1348518514` on the latest commit identified by `26ff3c6` then you
would end up with the version `0.0.1+build.1348518514.26ff3c6`. While
that version string is long, it is perfectly accurate, semver
compatible, and works well with OTP. This solves many of the current
versioning problems with rebar and erlang OTP Apps.
Quick Random Number Generation
==============================

Provides a simple interface to call efficient random number generation
functions based on the context.  Proper random number seeding is enforced.

Build
-----

    rebar compile

Author
------

Michael Truog (mjtruog [at] gmail (dot) com)

License
-------

BSD (`random_wh06_int.erl` is under the Erlang Public License)

Erlware Commons
===============

Current Status
--------------
[![Build Status](https://secure.travis-ci.org/erlware/erlware_commons.png)](http://travis-ci.org/erlware/erlware_commons)

Introduction
------------

Erlware commons can best be described as an extension to the stdlib
application that is distributed with Erlang. These are things that we
at Erlware have found useful for production applications but are not
included with the distribution. We hope that as things in this library
prove themselves useful, they will make their way into the main Erlang
distribution. However, whether they do or not, we hope that this
application will prove generally useful.

Goals for the project
---------------------

* Generally Useful Code
* High Quality
* Well Documented
* Well Tested

Currently Available Modules/Systems
------------------------------------

### [ec_date](https://github.com/erlware/erlware_commons/blob/master/src/ec_date.erl)

This module formats erlang dates in the form {{Year, Month, Day},
{Hour, Minute, Second}} to printable strings, using (almost)
equivalent formatting rules as http://uk.php.net/date, US vs European
dates are disambiguated in the same way as
http://uk.php.net/manual/en/function.strtotime.php That is, Dates in
the m/d/y or d-m-y formats are disambiguated by looking at the
separator between the various components: if the separator is a slash
(/), then the American m/d/y is assumed; whereas if the separator is a
dash (-) or a dot (.), then the European d-m-y format is assumed. To
avoid potential ambiguity, it's best to use ISO 8601 (YYYY-MM-DD)
dates.

erlang has no concept of timezone so the following formats are not
implemented: B e I O P T Z formats c and r will also differ slightly

### [ec_file](https://github.com/erlware/erlware_commons/blob/master/src/ec_file.erl)

A set of commonly defined helper functions for files that are not
included in stdlib.

### [ec_plists](https://github.com/erlware/erlware_commons/blob/master/src/ec_plists.erl)

plists is a drop-in replacement for module <a
href="http://www.erlang.org/doc/man/lists.html">lists</a>, making most
list operations parallel. It can operate on each element in parallel,
for IO-bound operations, on sublists in parallel, for taking advantage
of multi-core machines with CPU-bound operations, and across erlang
nodes, for parallizing inside a cluster. It handles errors and node
failures. It can be configured, tuned, and tweaked to get optimal
performance while minimizing overhead.

Almost all the functions are identical to equivalent functions in
lists, returning exactly the same result, and having both a form with
an identical syntax that operates on each element in parallel and a
form which takes an optional "malt", a specification for how to
parallize the operation.

fold is the one exception, parallel fold is different from linear
fold.  This module also include a simple mapreduce implementation, and
the function runmany. All the other functions are implemented with
runmany, which is as a generalization of parallel list operations.

### [ec_semver](https://github.com/erlware/erlware_commons/blob/master/src/ec_semver.erl)

A complete parser for the [semver](http://semver.org/)
standard. Including a complete set of conforming comparison functions.

### [ec_lists](https://github.com/ericbmerritt/erlware_commons/blob/master/src/ec_lists.erl)

A set of additional list manipulation functions designed to supliment
the `lists` module in stdlib.

### [ec_talk](https://github.com/erlware/erlware_commons/blob/master/src/ec_talk.erl)

A set of simple utility functions to falicitate command line
communication with a user.

Signatures
-----------

Other languages, have built in support for **Interface** or
**signature** functionality. Java has Interfaces, SML has
Signatures. Erlang, though, doesn't currently support this model, at
least not directly. There are a few ways you can approximate it. We
have defined a mechnism called *signatures* and several modules that
to serve as examples and provide a good set of *dictionary*
signatures. More information about signatures can be found at
[signature](https://github.com/erlware/erlware_commons/blob/master/doc/signatures.md).


### [ec_dictionary](https://github.com/erlware/erlware_commons/blob/master/src/ec_dictionary.erl)

A signature that supports association of keys to values. A map cannot
contain duplicate keys; each key can map to at most one value.

### [ec_dict](https://github.com/erlware/erlware_commons/blob/master/src/ec_dict.erl)

This provides an implementation of the ec_dictionary signature using
erlang's dicts as a base. The function documentation for ec_dictionary
applies here as well.

### [ec_gb_trees](https://github.com/ericbmerritt/erlware_commons/blob/master/src/ec_gb_trees.erl)

This provides an implementation of the ec_dictionary signature using
erlang's gb_trees as a base. The function documentation for
ec_dictionary applies here as well.

### [ec_orddict](https://github.com/ericbmerritt/erlware_commons/blob/master/src/ec_orddict.erl)

This provides an implementation of the ec_dictionary signature using
erlang's orddict as a base. The function documentation for
ec_dictionary applies here as well.

### [ec_rbdict](https://github.com/ericbmerritt/erlware_commons/blob/master/src/ec_rbdict.erl)

This provides an implementation of the ec_dictionary signature using
Robert Virding's rbdict module as a base. The function documentation
for ec_dictionary applies here as well.
# Stay in Sync

## What is Sync?

Sync is a developer utility. It recompiles and reloads your Erlang code
on-the-fly. With Sync, you can code without friction.

![Successful compilation image.](http://rusty.io.s3.amazonaws.com/sync/sync_01.png)

What does "code without friction" mean? It means that with Sync running, you no
longer need to worry about running `make`, or `c:l(Module)` again. Just write
code, save the file, and watch as Erlang automatically detects your changes,
recompiles the code, and reloads the module.

## How can I use Sync?

### Install via rebar dependency

```erlang
{deps, [
		{sync, ".*",
			{git, "git://github.com/rustyio/sync.git", {branch, "master"}}}
]}.
```

### Manual install

```bash
cd $ERL_LIBS
git clone git@github.com:rustyio/sync.git
(cd sync; make)
```

The recommended approach is to put sync in your $ERL_LIBS directory.

Then, go in the Erlang console of an application you are developing, run
`sync:go().`. You can also start sync using `application:start(sync).`

Starting up:

```
(rustyio@127.0.0.1)6> sync:go().

Starting Sync (Automatic Code Compiler / Reloader)
Scanning source files...
ok
08:34:18.609 [info] Application sync started on node 'rustyio@127.0.0.1'
```

Successfully recompiling a module:

```
08:34:43.255 [info] /Code/Webmachine/src/webmachine_dispatcher.erl:0: Recompiled.
08:34:43.265 [info] webmachine_dispatcher: Reloaded! (Beam changed.)
```

Warnings:

```
08:35:06.660 [info] /Code/Webmachine/src/webmachine_dispatcher.erl:33: Warning: function dispatch/3 is unused
```

Errors:

```
08:35:16.881 [info] /Code/Webmachine/src/webmachine_dispatcher.erl:196: Error: function reconstitute/1 undefined
/Code/Webmachine/src/webmachine_dispatcher.erl:250: Error: syntax error before: reconstitute
```

## Stopping and Pausing

You can stop the `sync` application entirely (wiping its internal state) with
`sync:stop()`. You can then restart the application with a new state using `sync:go()`

If, however, you just wish to pause `sync` so that it will not update anything
during some period, you can pause the scanner with `sync:pause()`.  You might
do this while upgrading you wish not to have immediately loaded until
everything is complete. Calling `sync:go()` once again will unpause the scanner.

Bear in mind that running `pause()` will not stop files that are currently
being compiled.

## Specifying folders to sync

To your erlang `config` add

```erlang
[
    {sync, [
        {src_dirs, {strategy(), [src_dir_descr()]}}
    ]}
].
```
```erlang
-type strategy() :: add | replace.
````
If `strategy()` is `replace`, sync will use ONLY specified dirs to sync. If `strategy()` is `add`, sync will add specific dirs to list of dirs to sync.

```erlang
-type src_dir_descr() :: { Dir :: file:filename(), [Options :: compile_option()]}.
```
You probably want to specify `outdir` compile option.

For example
```erlang
[
    {sync, [
        {src_dirs, {replace, [{"./priv/plugins", [{outdir,"./priv/plugins_bin"}]}]}}
    ]}
].
```

## Console Logging

By default, sync will print sucess / warning / failure notifications to the
erlang console.  You can control this behaviour with the `log` configuration options.

### Valid Values For `log`

* `all`: Print all console notifications
* `none`: Print no console notifications
* `[success | warnings | errors]`: A list of any combination of the atoms
  `success`, `warnings`, or `errors`.  Example: `[warnings, errors]` will only
  show warnings and errors, but suppress success messages.
* `true`: An alias to `all`, kept for backwards compatibility
* `false`: An alias to `none`, kept for backwards compatibility
* `skip_success`: An alias to `[errors, warnings]`, kept for backwards compatibility.

The `log` value can be specified in any of the following ways:

#### 1. Loaded from a .config file

	{log, all},	
	{log, [success, warnings]},

#### 2. As an environment variable called from the erlang command line:

	erl -sync log all
	erl -sync log none

#### 3. From within the Erlang shell:

	sync:log(all);
	sync:log(none);
	sync:log([errors, warnings]);

## Desktop Notifications

Sync can pop success / warning / failure notifications onto your desktop to
keep you informed of compliation results. All major operating systems are
supported: Mac via [Growl](http://growl.info), Linux via Libnotify, Windows via
[Notifu](http://www.paralint.com/projects/notifu/) and Emacs via lwarn /
message command. Below are Growl screenshots.


Success:

![Successful compilation image.](http://rusty.io.s3.amazonaws.com/sync/sync_01.png)

Warnings:

![Compilation warnings image.](http://rusty.io.s3.amazonaws.com/sync/sync_02.png)

Errors:

![Compilation errors image.](http://rusty.io.s3.amazonaws.com/sync/sync_03.png)

### Disabling Desktop Notifications

Desktop notifications follow the same conventions as the console logging above,
and can be selectively enabled or disabled with the `growl` configuration variable:

### Valid Values For `growl`

* `all`: Print all console notifications
* `none`: Print no console notifications
* `[success | warnings | errors]`: A list of any combination of the atoms
  `success`, `warnings`, or `errors`.  Example: `[warnings, errors]` will only
  show warnings and errors, but suppress success messages.
* `true`: An alias to `all`, kept for backwards compatibility
* `false`: An alias to `none`, kept for backwards compatibility
* `skip_success`: An alias to `[errors, warnings]`, kept for backwards compatibility.

The `growl` value can be specified in any of the following ways:

#### 1. Loaded from a .config file

	{growl, all},	
	{growl, [success, warnings]},

#### 2. As an environment variable called from the erlang command line:

	erl -sync growl all
	erl -sync growl none

#### 3. From within the Erlang shell:

	sync:growl(all);
	sync:growl(none);
	sync:growl([errors, warnings]);

### Troubleshooting Growl Notifications

Sync attempts to auto-detect the notification package to use via the
`os:type()` command.

If this isn't working for you, or you would like to override the default, use
the `executable` configuration parameter:

	{executable, TYPE}

Where `TYPE` is:
+ `'auto'` Autodetermine (default behaviour)
+ `'growlnotify'` for Mac / Growl.
+ `'notification_center'` for Mac OS X built-in Notification Center.
+ `'notify-send'` for Linux / libnotify.
+ `'notifu'` for Windows / Notifu.
+ `'emacsclient'` for Emacs notifications.

Like all configuration parameters, this can also be specified when launching
Erlang with:

    erl -sync executable TYPE

## Remote Server "Patching"

If you are developing an application that runs on an Erlang cluster, you may
need to recompile a module on one node, and then broadcast the changed module
to other nodes. Sync helps you do that with a feature called "patching."

To use the patching feature:

1. Connect to any machine in your cluster via distributed erlang. A simple
   `net_adm:ping(Node)` should suffice.

2. Run `sync:patch()`. This will start the Sync application if it's not already
   started, and enable "patch mode".

3. Start editing code.

Sync will detect changes to code, recompile your modules, and then sent the
updated modules to every Erlang node connected to your cluster. If the module
already exists on the node, then it will be overwritten on disk with the new
.beam file and reloaded. If the module doesn't exist on the new node, then it
is simply updated in memory.

## How does Sync work?

Upon startup, Sync gathers information about loaded modules, ebin directories,
source files, compilation options, etc.

Sync then periodically checks the last modified date of source files. If a file
has changed since the last scan, then Sync automatically recompiles the module
using the previous set of compilation options. If compilation was successful,
it loads the updated module. Otherwise, it prints compilation errors to the
console.

Sync also periodically checks the last modified date of any beam files, and
automatically reloads the file if it has changed.

The scanning process adds 1% to 2% CPU load on a running Erlang VM. Much care
has been taken to keep this low. Shouldn't have to say this, but this is for
development mode only, don't run it in production.

## Sync Post-hooks

You can register a post-hook to run after Sync reloads modules. This can allow
you to run tests on modules if you like, or anything else for that matter.

You can register a post-hook with:

```erlang
sync:onsync(fun(Mods) ->
				io:format("Reloaded Modules: ~p~n",[Mods]) 
			end).
```

This will simply print the list of modules that were successfully recompiled.

For example, if you wanted to automatically run a unit test on each reloaded
module that has a `test()` function exported, you could do the following:

```erlang
RunTests = fun(Mods) ->
	[Mod:test() || Mod <- Mods, erlang:function_exported(Mod, test, 0)]
end,
sync:onsync(RunTests).
```

A post-hook can also be specified as a `{Module,Function}` tuple, which assumes
`Module:Function/1`

*Note:* Currently, only one post-hook can be registered at a time.

### Unregistering a post-hook

To unregister a post-hook, just call

	sync:onsync(undefined).

## Whitelisting/Excluding modules from the scanning process

Sometimes you may want to focus only on a few modules, or prevent some modules
from being scanned by sync. To achive this just modify `whitelisted_modules` or
`excluded_modules` configuration parameter in the
[node's config file](http://www.erlang.org/doc/man/config.html).

Beyond specifying modules one by one, identified by atoms, you can also specify
them in bulk, identified by regular expressions, but with a slower sync.

## Moving Application Location

Previously, if an entire application (like a reltool-generated release) was
moved from one location to another, sync would fail to recompile files that
were changed until all the beams were remade.  While this is typically as
simple as typing `rebar compile`, it was still a hassle.

The solution to this was to enable the ability for sync to "heal" the paths
when it turned out they had been moved.

The way this works is by checking if the `source` path inside the beam is a
file that exists, and by checking if that path is a descendant of the root of
your application.  If sync has been set to fix the paths, and module's source
is pointing at a path that isn't a descendant of the current working directory,
it will attempt to find the correct file.

You can change how this will be handled with a `non_descendants` setting in the
config:

* `fix`: Fix any file that isn't a descendant

* `allow`: Use the original path in the module, regardless of its location,
  recompiling only if the original location changes.

* `ignore`: If a file is not a descendant, sync will completely ignore it.

## A note about Nitrogen

The `{sync_mode, nitrogen}` option is no longer necessary for users of the
[Nitrogen Web Framework](http://nitrogenproject.com) and will be ignored. Sync
works with Nitrogen without that option.

## Sample Configuration File

Please note that sync loads with the following defaults:

```erlang
[
	{sync, [
		{growl, all},
		{log, all},
		{non_descendants, fix},
		{executable, auto},
		{whitelisted_modules, []},
		{excluded_modules, []}
	]}
].
```

You can view a full sample configuration file
([sync.sample.config](https://github.com/rustyio/sync/blob/master/sync.sample.config))
that you're free to include in your application. Just be sure to use the
`-config` switch for the `erl` program:

	erl -config sync.config

## Sync with relx

If you use [relx](https://github.com/erlware/relx) and wish to use sync with a
relx created release, you'll need to run relx with -d option (symlink all
applications and configuration into the release instead of copying) add a
`syntax_tools` and `compiler` to `release` section to your relx.config file:

```erlang
{release, {your_app, "1.0.0"}, [
	syntax_tools,
	compiler
]}.
```
# Goldrush #

Goldrush is a small Erlang app that provides fast event stream processing

# Features #
* Event processing compiled to a query module
 - per module protected event processing statistics
 - query module logic can be combined for any/all filters
 - query module logic can be reduced to efficiently match event processing

* Complex event processing logic
 - match input events with greater than (gt) logic
 - match input events with less than (lt) logic
 - match input events with equal to (eq) logic
 - match input events with wildcard (wc) logic
 - match input events with notfound (nf) logic
 - match no input events (null blackhole) logic
 - match all input events (null passthrough) logic

* Handle output events
 - Once a query has been composed the output action can be overriden
   with an erlang function. The function will be applied to each
   output event from the query.

* Usage 
  To use goldrush in your application, you need to define it as a rebar dep or
  include it in erlang's path.


Before composing modules, you'll need to define a query. The query syntax 
matches any number of `{erlang, terms}' and is composed as follows:

* Simple Logic 
 - Simple logic is defined as any logic matching a single event filter

Select all events where 'a' exists and is greater than 0.
#+BEGIN_EXAMPLE
    glc:gt(a, 0).
#+END_EXAMPLE

Select all events where 'a' exists and is equal to 0.
#+BEGIN_EXAMPLE
    glc:eq(a, 0).
#+END_EXAMPLE

Select all events where 'a' exists and is less than 0.
#+BEGIN_EXAMPLE
    glc:lt(a, 0).
#+END_EXAMPLE

Select all events where 'a' exists.
#+BEGIN_EXAMPLE
    glc:wc(a).
#+END_EXAMPLE

Select all events where 'a' does not exist.
#+BEGIN_EXAMPLE
    glc:nf(a).
#+END_EXAMPLE

Select no input events. User as a black hole query.
#+BEGIN_EXAMPLE
    glc:null(false).
#+END_EXAMPLE

Select all input events. Used as a passthrough query.
#+BEGIN_EXAMPLE
    glc:null(true).
#+END_EXAMPLE


* Combined Logic
 - Combined logic is defined as logic matching multiple event filters

Select all events where both 'a' AND 'b' exists and are greater than 0.
#+BEGIN_EXAMPLE
    glc:all([glc:gt(a, 0), glc:gt(b, 0)]).
#+END_EXAMPLE

Select all events where 'a' OR 'b' exists and are greater than 0.
#+BEGIN_EXAMPLE
    glc:any([glc:gt(a, 0), glc:gt(b, 0)]).
#+END_EXAMPLE

Select all events where 'a' AND 'b' exists where 'a' is greater than 1 and 'b' is less than 2.
#+BEGIN_EXAMPLE
    glc:all([glc:gt(a, 1), glc:lt(b, 2)]).
#+END_EXAMPLE

Select all events where 'a' OR 'b' exists where 'a' is greater than 1 and 'b' is less than 2.
#+BEGIN_EXAMPLE
    glc:any([glc:gt(a, 1), glc:lt(b, 2)]).
#+END_EXAMPLE


* Reduced Logic
 - Reduced logic is defined as logic which can be simplified to improve efficiency.

Select all events where 'a' is equal to 1, 'b' is equal to 2 and 'c' is equal to 3 and collapse any duplicate logic.
#+BEGIN_EXAMPLE
        glc_lib:reduce(
            glc:all([
                glc:any([glc:eq(a, 1), glc:eq(b, 2)]),
                glc:any([glc:eq(a, 1), glc:eq(c, 3)])])).
#+END_EXAMPLE

The previous example will produce and is equivalent to:
#+BEGIN_EXAMPLE
    glc:all([glc:eq(a, 1), glc:eq(b, 2), glc:eq(c, 3)]).
#+END_EXAMPLE



# Composing Modules #

To compose a module you will take your Query defined above and compile it. 
#+BEGIN_EXAMPLE
    glc:compile(Module, Query).
#+END_EXAMPLE


- At this point you will be able to handle an event using a compiled query. 

Begin by constructing an event list.
#+BEGIN_EXAMPLE
    Event = gre:make([{'a', 2}], [list]).
#+END_EXAMPLE

Now pass it to your query module to be handled.
#+BEGIN_EXAMPLE
    glc:handle(Module, Event).
#+END_EXAMPLE

* Handling output events
  - You can override the output action with an erlang function.

Write all input events as info reports to the error logger.
#+BEGIN_EXAMPLE
    glc:with(glc:null(true), fun(E) ->
         error_logger:info_report(gre:pairs(E)) end).
#+END_EXAMPLE

Write all input events where `error_level' exists and is less than 5 as info reports to the error logger.
#+BEGIN_EXAMPLE
    glc:with(glc:lt(error_level, 5), fun(E) ->
         error_logger:info_report(gre:pairs(E)) end).
#+END_EXAMPLE


# Event Processing Statistics #

Return the number of input events for this query module.
#+BEGIN_EXAMPLE
glc:input(Module).
#+END_EXAMPLE

Return the number of output events for this query module.
#+BEGIN_EXAMPLE
glc:output(Module).
#+END_EXAMPLE

Return the number of filtered events for this query module.
#+BEGIN_EXAMPLE
glc:filter(Module).
#+END_EXAMPLE


* Build

#+BEGIN_EXAMPLE
 $ ./rebar compile
#+END_EXAMPLE

or

#+BEGIN_EXAMPLE
    $ make
#+END_EXAMPLE

* CHANGELOG 

0.1.6 
- Add notfound event matching

0.1.5 
- Rewrite to make highly crash resilient
  - per module supervision
  - statistics data recovery 
- Add wildcard event matching
- Add reset counters
# sqerl #

This is the repository for sqerl, a database layer originally written
for chef for interfacing with postgres.

## Getting Started

So, you want to model a Postgres database table with Sqerl. Let's get
to it.

## Postgres I'm going to assume you know very little about Postgres,
since that's what I knew when I started writing this. You can safely
skip this section if you know how to get that running.

You can get Postgres up and running on a Mac as easy as downloading
[Postgres.app](http://postgresapp.com). You should probably learn more
that the basics if you're going to run it anywhere more complex than
that.

Postgres.app starts Postgres on port 5432 of localhost. It'll also
create a user and database for your OS X user's shortname. We'll use
`tyktorp` for the examples below.

We should at least create a table so you have something to interact
with in the following examples.

```sql
CREATE TABLE things (
    id BIGSERIAL PRIMARY KEY,
    description TEXT
);
```

## Add It!

To add sqerl to your project (hereon known as `sample_app`), add it to
your deps proplist in `rebar.config`

```erlang
{sqerl, ".*",
 {git, "git://github.com/opscode/sqerl.git", {branch, "master"}}}
```

It's going to pull in these dependencies, just go with it:

```
Cloning into 'epgsql'...
Cloning into 'pooler'...
Cloning into 'envy'...
```

## Configuring Sqerl

You actually need two `sys.config` application blocks. If only there
were an application out there for abstracing configuration settings in
to logical groupings, instead of imposing erlang's application
behavior as a unit of scope.

```erlang
 {sqerl, [
          %% Database connection parameters
          {db_host, "localhost" },
          {db_port, 5432 },
          {db_user, "tyktorp" },
          {db_pass, "" },
          {db_name, "tyktorp" },
          {idle_check, 10000},
          {column_transforms, []},
          {prepared_statements,
            {sqerl_rec, statements, [[{app, sample_app}]]}}
         ]},

 {pooler, [
           {pools, [[{name, sqerl},
                     {max_count,  10 },
                     {init_count, 5 },
                     {start_mfa, {sqerl_client, start_link, []}}]]}
          ]},
```

## Model the table

`thing.erl`

```erlang
-module(thing).

-compile({parse_transform, sqerl_gobot}).

-export([
         '#insert_fields'/0,
         '#update_fields'/0,
         '#statements'/0,
         '#table_name'/0
        ]).

%% Must be the same as the module name
-record(thing, {
          id :: integer(),
          description :: binary()
         }).

'#insert_fields'() ->
    [description].

'#update_fields'() ->
    [description].

'#statements'() ->
    [default].

%% Only needed if table name is different than module name
%'#table_name'() ->
%    "things".

```

**NOTE:** module name and record name **MUST** be the same.

Hopefully the `sqerl_gobot` parse transform doesn't do too much magic
for you behind the scenes. Just the right amount of magic. They're not
tricks, they're illusions. Here's what it gives you:

### Behavior
`-behaviour(sqerl_rec)` - Basically defines the required callbacks.

### Callbacks

Some callbacks are generated by the parse transform, some you have to
do yourself. Either way, the ones that start with `#` are meant to be
called internally by `sqerl_rec`. The ones that don't are there for
developer use. I suppose you can use them if you want. It's more of a
guideline.

**Generated:**

`'#new'()` - returns a new record of this type

`'is'(Obj)` - is `Obj` an "object" of this type

`getval(Fieldname, Obj)` - returns `Fieldname` of `Object`

`setvals([{Fieldname, Value}|...]=Proplist, Obj)` - returns a copy of
`Obj` with each `Fieldname`'s `Value`' from `PropList` modified.

`fromlist([{Fieldname, Value}|...]=Proplist)` - works just like
`setvals/2`, but it's for new instances only.

`fields()` - returns a list of fields you provided in the `-record` of
your module.

**Write Yourself:**

`'#insert_fields'() -> [atom()]` - the list of record fields to be
inserted with generated insert statement.

`'#update_fields'() -> [atom()]` - the list of record fields to be
updated with generated update statement.

`'#statements'() -> [ default | {atom(), iolist()}]` - a list of named
statements. This is where your specific database code goes.

**Optional:**

`'#table_name'() -> atom`. If your table name isn't the name of your
module, set it here.

## Console

I skipped some steps here for now, but I'm assuming you can open up an
erlang console with this application started.

```erlang
%%% Make sure it's all configured right.
(sample_app@127.0.0.1)> sqerl_rec:statements([thing]).
[{thing_delete_by_id,<<"DELETE FROM things WHERE id = $1">>},
 {thing_fetch_by_id,<<"SELECT id, description FROM things WHERE id = $1">>},
 {thing_insert,<<"INSERT INTO things(description) VALUES ($1) RETURNING id, description">>},
 {thing_update,<<"UPDATE things SET description = $1 WHERE id = $2 RETURNING id, description">>}]

%% Add a thing?
(sample_app@127.0.0.1)> R = {thing, undefined, "Hi!"}.
{thing,undefined,"Hi!"}

(sample_app@127.0.0.1)> sqerl_rec:insert(R).
[{thing,1,<<"Hi!">>}]

(sample_app@127.0.0.1)> sqerl_rec:fetch(thing, id, 1).
[{thing,1,<<"Hi!">>}]

```

And look in the database!

```
tyktorp=# SELECT * FROM things;
 id | description
----+-------------
  1 | Hi!
(1 row)
```

## Here we are now, it's a statement
Let's get everything!

```erlang
(sample_app@127.0.0.1)> sqerl_rec:fetch_all(thing).
{error,{query_not_found,thing_fetch_all}}
%% OOPS!

```

You have to specify a `fetch_all` query for `thing`, fortunately
there's a convenience method for that. Change `thing:#statements/0` to

```
'#statements'() ->
    [default,
        {fetch_all, sqerl_rec:gen_fetch_all(thing, id)}
    ].
```

Yay!

```
(sample_app@127.0.0.1)1> sqerl_rec:fetch_all(thing).
[{thing,1,<<"Hi!">>}]
```

You can make lots of custom statements as your usecase requires. Ours
is pretty trivial though, I probably should have added more columns.


## tests

local postgres commands must be on `$PATH` to successfully `make all`

A set of integration and performance tests can be run via `make ct`

# LINKS:

Source:

    https://github.com/opscode/sqerl

Tickets/Issues:

    http://tickets.opscode.com/

Documentation:

    http://wiki.opscode.com/display/chef/Home/

# LICENSE:

Copyright 2011-2014 Opscode, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you
may not use this file except in compliance with the License.  You may
obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
implied.  See the License for the specific language governing
permissions and limitations under the License.
h1. Neotoma

h2. About

Neotoma is a packrat parser-generator for Erlang for Parsing Expression Grammars (PEGs).
It consists of a parsing-combinator library with memoization routines, a parser for PEGs,
and a utility to generate parsers from PEGs.  It is inspired by treetop, a Ruby library with
similar aims, and parsec, the parser-combinator library for Haskell.

Neotoma is licensed under the MIT License (see LICENSE).

h2. Features

# Simple, declarative parsers generated from even simpler grammars.
# Fully integrated, single-pass lexical and syntactic analysis (a feature of PEGs).
# Packrat-style memoization, boasting parse-time bound linearly to the input size (at the expense of memory usage).
# In-place semantic analysis/transformation, supporting single-pass end-to-end in some applications.
# Erlang code-generation for the lexical/syntactic analysis piece, with the option of semantic analysis/transformation inline, or in a separate module.
# Line/column number tracking for easy resolution of parsing errors.

h2. Installation

# Clone the repository from github: <notextile><pre><code>$ git clone git://github.com/seancribbs/neotoma.git</code></pre></notextile>
# Symlink or copy the cloned repository to somewhere in your Erlang code path. $ERLANG_HOME/lib is best.
# Build the source: <notextile><pre><code>$ make</code></pre></notextile>

h2. Usage

# After making sure the library is in your code path, fire up an Erlang shell.
# To generate a parser from a PEG, use @neotoma:file/1,2@ (more detailed documentation pending).  For PEG examples, see the @extra/@ directory in the repository.

  <notextile><pre><code>1&gt; neotoma:file("extra/arithmetic.peg").</code></pre></notextile>

  This will place @arithmetic.erl@ in the same directory as the @.peg@ file by default.

h2. Contributing

Please send pull-requests to 'seancribbs' on github.  When submitting a patch, eunit tests are strongly encouraged.
# mini_s3 #

This is the repository for mini_s3, a simple s3 client API.

Chef is a system integration framework written in erlang and ruby and designed to bring the benefits of configuration management to your entire infrastructure.

The Chef Wiki is the definitive source of user documentation.

    http://wiki.opscode.com/display/chef/Home

This README focuses on developers who want to modify Chef source code.  For users who just want to run the latest and greatest Chef development version in their environment, see:

   [TODO: add URL when available for erlang chef build process]

# DEVELOPMENT:

Before working on the code, if you plan to contribute your changes, you need to read the Opscode Contributing document.

    http://wiki.opscode.com/display/chef/How+to+Contribute

You will also need to set up the repository with the appropriate branches. We document the process on the Chef Wiki.

    http://wiki.opscode.com/display/chef/Working+with+git

Once your repository is set up, you can start working on the code.

# LINKS:

Source:

    https://github.com/opscode/mini_s3

Tickets/Issues:

    http://tickets.opscode.com/

Documentation:

    http://wiki.opscode.com/display/chef/Home/

# LICENSE:

Copyright 2011-2012 Opscode, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the License for the specific language governing permissions and limitations under the License.
folsom_graphite
===============

Send data from folsom automatically to graphite

## LICENSE:

Copyright 2011-2014 Opscode, Inc. All Rights Reserved.

Licensed under the Apache License, Version 2.0 (the "License"); you may not use this file except in compliance with the License.  You may obtain a copy of the License at

  http://www.apache.org/licenses/LICENSE-2.0

  Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.  See the License for the specific language governing permissions and limitations under the License.
gen_server2 - a copy of LSHIFT's gen_server modifications
=========================================================

_gen_server2_ is a modified version of OTP's gen_server behaviour. 
This repository is hosted so people don't have to keep copying the 
gen_server2 source file into their projects, which is pointless unless
you're planning on making modifications of your own. 

Installation
------------

Using [epm](http://github.com/JacobVorreuter/epm), you can install in the following manner: 

	t4@malachi:~ $ epm install hyperthunk/gen_server2
	epm v0.1.1, 2010

	===============================
	Install the following packages?
	===============================
	    + hyperthunk-gen_server2-master

	([y]/n) y

	+ downloading http://github.com/hyperthunk/gen_server2/tarball/master
	+ compiling with rebar...
	+ running gen_server2 build command
	+ running gen_server2 install command

	t4@malachi:~ $ erl
	Erlang R13B04 (erts-5.7.5) [source] [smp:2:2] [rq:2] [async-threads:0] [hipe] [kernel-poll:false]

	Eshell V5.7.5  (abort with ^G)
	1> code:which(gen_server2).
	"/Users/t4/Library/Erlang/Site/gen_server2-1.0.0/ebin/gen_server2.beam"
	2> 
	
If you're using [rebar](http://github.com/basho/rebar) as your build tool, then you can include this in your dependencies to have
it pulled down automatically: 

	%% file: rebar.config
	{deps, [
	  {gen_server2, "1.0.0", {git, "http://github.com/hyperthunk/gen_server2.git", "master"}}
	]}.

And pull it with get/check-deps:

	t4@malachi:plumber $ rebar get-deps
	==> plumber (get-deps)
	Pulling gen_server2 from {git,"http://github.com/hyperthunk/gen_server2.git",
	                              "master"}
	Initialized empty Git repository in /Users/t4/work/mine/plumber/deps/gen_server2/.git/
	Already on 'master'
	==> gen_server2 (get-deps)
	t4@malachi:plumber $ rebar check-deps
	==> gen_server2 (check-deps)
	==> plumber (check-deps)
	t4@malachi:plumber $


# A Rebar Plugin that Generates Locked Dependencies for Rebar Projects #

## tl;dr ##

Use this plugin to create reproducible builds for a rebar
project. Generate a `rebar.config.lock` file by running the command
from the top level directory of your project like this:

    rebar lock-deps

The generated `rebar.config.lock` file lists every dependency of the
project and locks it at the git revision found in the `deps` directory.

A clean build using the lock file (`rebar -C rebar.config.lock`) will
pull all dependencies as found at the time of generation. Suggestions
for integrating with Make are described below.

## Installation ##

Add the following to your top-level rebar.config:

    %% Plugin dependency
    {deps, [
    	{rebar_lock_deps_plugin, ".*",
         {git, "git://github.com/seth/rebar_lock_deps_plugin.git", {branch, "master"}}}
    ]}.

    %% Plugin usage
    {plugins, [rebar_lock_deps_plugin]}.

## How it works ##

The command must be run from a rebar project directory in which
`get-deps` has already been run. It generates a `rebar.config.lock`
file where the dependencies are locked to the versions available
locally (the current state of the project).

The lock-deps command goes through each directory in your deps dir and
calls `git rev-parse HEAD` to determine the currently checked out
version. It also extracts the dependency specs (the `deps` key) from
the rebar.config files inside each directory in deps (non-recursively)
along with the top-level rebar.config. Using this data, the script
creates a new rebar.config.lock file as a clone of the top-level
rebar.config file, but with the `deps` key replaced with the complete
list of dependencies set to SHA that is based on
what is currently checked out.

If something fails during the get-deps rebar stage, take care to run
`rebar get-deps skip_deps=true` to try to repair it. Otherwise, rebar
will pull deps based on specs of your dependencies rather than the
locked version at the top-level.

## Ignoring some dependencies ##

If there are dependencies which you do not wish to lock, you can list
them using the `ignore` option on the command line (comma separate
multiple values).  For example, `rebar lock-deps ignore=meck,eper`
would lock all dependencies except for `meck` and `eper` which would
retain the spec as found in one of the `rebar.config` files that
declared it. Note that if a dependency is declared more than once, the
script picks a spec "at random" to use.

## Updating locked dependencies ##

Sometimes, in case you already have your dependencies locked and
rebar.config.lock checked-in to your repository,
it is too expensive to run `rebar -C rebar.config.lock update-deps`
every time you checkout a specific commit of your project
as it is require updating the deps from remote repositories.
Since there are already certain SHAs for every dependency
in rebar.config.lock, in most cases you can use the local
deps repositories to checkout certain versions of the deps.
You can use `rebar -C rebar.config.lock update-deps-local` for this.
When there is no local commit needed to update a certain dependency,
this command will update it from the remote repository.

Particularly, it is helpful when using `git bisect` to find a 'bad' commit
in your repository (you go back in time and you usually have all needed commits
in local deps repositories).

Only git is supported for the moment.

## How you can integrate it into your build ##

Assuming you build your project with `make`, add the following to your
`Makefile`:

    # The release branch should have a file named USE_REBAR_LOCKED
    use_locked_config = $(wildcard USE_REBAR_LOCKED)
    ifeq ($(use_locked_config),USE_REBAR_LOCKED)
      rebar_config = rebar.config.locked
    else
      rebar_config = rebar.config
    endif
    REBAR = rebar -C $(rebar_config)

    update_locked_config:
    	@rebar lock-deps ignore=meck

To tag the release branch, you would create a clean build and verify
it works as desired. Then run `make update_locked_config` and check-in
the resulting `rebar.config.lock` file. For the release branch, `touch
USE_REBAR_LOCKED` and check that in as well. Now create a tag.

The idea is that a clean build from the tag will pull deps based on
rebar.config.lock and you will have reproduced what you tested.

On master, you don't have a `USE_REBAR_LOCKED` file checked in and will
use the standard `rebar.config` file. Of course, you can also use
`rebar.config.lock` in master, if you want to have stable reproduceble
builds in master as well.

This approach should keep merge conflicts to a minimum. It is also
nice that you can easily review which dependencies have changed by
comparing the `rebar.config.lock` file in version control.

### folsom

Folsom is an Erlang based metrics system inspired by Coda Hale's metrics (https://github.com/codahale/metrics/). The metrics API's purpose is to collect realtime metrics from your Erlang applications and publish them via Erlang APIs and output plugins. folsom is *not* a persistent store. There are 6 types of metrics: counters, gauges, histograms (and timers), histories, meter_readers and meters. Metrics can be created, read and updated via the `folsom_metrics` module.

#### Building and running

First, regarding using folsom and folsom_webmachine together. To make sure you have compatible versions of each, make sure you use code from the same version tags, ie 0.5 of folsom is known to work with 0.5 folsom_webmachine. HEAD on each repo may have broken API compatibility.

You need a (preferably recent) version of Erlang installed but that should be it.

       ./rebar get-deps compile

folsom can be run standalone or embedded in an Erlang application.

       $ erl -pa ebin deps/*/ebin

       > folsom:start(). % this creates the needed ETS tables and starts a gen_server

You can also start it as an application:

       $ erl -pa ebin deps/*/ebin
       > application:start(folsom).

       $ erl -pa ebin deps/*/ebin -s folsom

The application can be configured to create individual or lists of metrics at
startup on the command line or in an application config file:

       $ erl -pa ebin deps/*/ebin -s folsom \
          -folsom history '[hist1,hist2]' \
          -folsom gauge gauge1

       $ echo '[{folsom, [{history, [hist1, hist2]}, {gauge, gauge1}]}].' \
          > myapp.config
       $ erl -pa ebin deps/*/ebin -config myapp.config -s folsom

#### Metrics API

folsom_metrics.erl is the API module you will need to use most of the time.

Retrieve a list of current installed metrics:

      > folsom_metrics:get_metrics().

Query a specific metric:

      > folsom_metrics:get_metric_value(Name).

Generally names of metrics are atoms or binaries.

##### Counters

Counter metrics provide increment and decrement capabilities for a single scalar value.

      > folsom_metrics:new_counter(Name).
      > folsom_metrics:notify({Name, {inc, Value}}).
      > folsom_metrics:notify({Name, {dec, Value}}).

##### Gauges

Gauges are point-in-time single value metrics.

      > folsom_metrics:new_gauge(Name).
      > folsom_metrics:notify({Name, Value}).

##### Histograms (and Timers)

Histograms are collections of values that have statistical analysis done to them, such as mean, min, max, kurtosis and percentile. They can be used like "timers" as well with the timed update functions.

      > folsom_metrics:new_histogram(Name).
      > folsom_metrics:histogram_timed_update(Name, Mod, Fun, Args).
      > folsom_metrics:histogram_timed_update(Name, Fun, Args).
      > folsom_metrics:histogram_timed_update(Name, Fun).
      > folsom_metrics:notify({Name, Value}).

###### Histogram sample types

Each histogram draws its values from a `reservoir` of readings. You can select a `sample type` for a histogram by passing the name of the sample type as an atom when you create a new histogram.
Some sample types have further arguments. The purpose of a sample type is to control the size and charecteristics of the reservoir of readings the histogram performs analysis upon.

Folsom currently provides the following sample types:

######  `uniform`

This is a random uniform sample over the stream of readings. This is the default sample type, bounded in size to 1028 readings. When `size` readings have been taken, new readings replace older readings
in the reservoir at random. You can set the sample size at creation time:

      > folsom_metrics:new_histogram(Name, uniform, Size::integer()).

Be sure you understand _why_ before you do this.

###### `exdec`

This is a  sample that exponentially decays less significant readings over time so as to give greater significance to newer readings. Read more here -
[Forward Decay...](http://www.research.att.com/people/Cormode_Graham/library/publications/CormodeShkapenyukSrivastavaXu09.pdf).
Again you can change defaults at creation time, if you think you need to:

    > folsom_metrics:new_histogram(Name, exdec, Size::integer(), Alpha::float()).

###### `slide`

This is a sliding window in time over a stream of readings. The default window size is 60 seconds. Every reading that occurs in a sliding sixty second window is stored,
with older readings being discarded. If you have a lot of readings per
minute the `reservoir` may get pretty big and so it will take more time to calculate statistics. You can set the `window` size by providing a number of seconds.

    > folsom_metrics:new_histogram(Name, slide, Seconds::integer()).

###### `slide_uniform`

This is a sliding window in time over a stream of readings with a random uniform sample per second, to bound the size of the total number of readings. The maximum size of the reservoir will be
 `window size * sample size`. Default is a window of 60 seconds and a sample size of 1028. Again, you can change these at creation time:

    > folsom_metrics:new_histogram(Name, slide_uniform, {Secs::interger(), Size::integer()).

##### Histories

Histories are a collection of past events, such as errors or log messages.

      > folsom_metrics:new_history(Name).
      > folsom_metrics:get_history_values(Name, Count). % get more than the default number of history items back
      > folsom_metrics:notify({Name, Value}).

##### Meters

Meters are increment only counters with mean rates and exponentially weighted moving averages applied to them, similar to a unix load average.

      > folsom_metrics:new_meter(Name).
      > folsom_metrics:notify({Name, Value}).

###### `Spiral` meter

A `spiral` is a type of meter that has a one minute sliding window count. The meter tracks an increment only counter and a total for the last minute. This is a sliding count with older readings dropping off per second.

    > folsom_metrics:new_spiral(Name).
    > folsom_metrics:notify({Name, Count}).

##### Meter Reader

Meter readers are like a meter except that the values passed to it are monotonically increasing, e.g., reading from a water or gas meter, CPU jiffies, or I/O operation count.

      > folsom_metrics:new_meter_reader(Name).
      > folsom_metrics:notify({Name, Value}).

##### Metrics groups/tags

Certain users might want to group and query metrics monitoring a common task. In order to do so, they can
tag metrics:

    > folsom_metrics:tag_metric(Name, Tag).

and untag metrics:

    > folsom_metrics:untag_metric(Name, Tag).

Users can query a list of tuples `[{Name, Value}]` of all metrics with a given tag:

    > folsom_metrics:get_metrics_value(Tag).

If only a certain type of metrics from a given group is desired, one can specify so:

    > folsom_metrics:get_metrics_value(Tag, Type).

where Type is one of `counter`, `gauge`, `histogram`, `history`, `meter`, `meter_reader`, `duration` or `spiral`.

##### Erlang VM

folsom also produces Erlang VM statistics.

The result of `erlang:memory/0`:

       > folsom_vm_metrics:get_memory().

The result of `erlang:system_info/1`:

       > folsom_vm_metrics:get_system_info().

The result of `erlang:statistics/1`:

       > folsom_vm_metrics:get_statistics().

The result of `erlang:process_info/1`:

       > folsom_vm_metrics:get_process_info(). %% use with caution

The result of `inet:getstat/1`, `prim_inet:getstatus/1`, `erlang:port_info/1`, `prim_inet:gettype/1`, `inet:getopts/1`, `inet:sockname/1`:

       > folsom_vm_metrics:get_port_info(). %% use with caution

The result from `ets:info/1` and `dets:info/1` across all tables

       > folsom_vm_metrics:get_ets_info().
       > folsom_vm_metrics:get_dets_info().
This is a (somewhat) hacky attempt at making [meck](https://github.com/eproxus/meck) just a bit easier to use. My motivation to streamline and automate meck is based on two recent experiences: mocking out a complex database API to reduce testing dependencies and helping new Erlang programmers come up to speed with Eunit and meck.

## License

All files in the repository are licensed under the Apache 2.0 license. If any
file is missing the License header it should assume the following is attached;

```
Copyright 2014 Chef Software Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

_automeck_ has two main features. The first is a data driven format for generating simple mock functions which pattern match on their arguments to select the correct output. The file `priv/mocks.config` is an example of how to configure _automeck_ to generate a set of mocks.

The second feature allows _automeck_ to record function calls. _automeck_ records the module & function name, the call parameters, and the return value. The file `priv/record.config` is an example of how to configure _automeck_ to record function calls on a set of modules. After you've collected enough data you can tell _automeck_ to generate a set of mocks from the recorded data. The Erlang shell session listed below illustrates the API for this feature in more detail.

    1> {ok, Session} = automeck:record("priv/record.config").
    {ok,"/tmp/automeck_record.session"}
    %% Let's generate a bunch of function calls
    2> [{foo:test1(X), foo:test1(X, X + random:uniform(100)), bar:test(), bar:test(X, X)} || X <- lists:seq(1, 5)].
    [{2,-10,bar,2}|...]
    %% Let's look at the recorded data
    3> {ok, RawData} = file:read_file(Session).
    {ok, <<...>>}
    4> rp(RawData).
    <<"{foo, test1, [{[1,53], -52}]}.
       {bar, test, [{[], bar}]}.
       {bar, test, [{[1,1], 2}]}.
       {foo, test1, [{[2,56], -108}]}.
       {bar, test, [{[], bar}]}.
       {bar, test, [{[2,2], 4}]}.
       {foo, test1, [{[3,34], -93}]}...">>

----

    %% Finish the recording session and generate mock config file
    5> {ok, MockConfig} = automeck:finish_recording(Session).
    {ok,"/tmp/mocks.config"}
    6> MockedModules = automeck:mock(MockConfig).
    [bar, foo]
    %% Let's call a couple of mocked functions and an unmocked one
    7> foo:test1(1, 53).
    -52
    8> bar:test(2, 2).
    4
    %% The process tree crashes because this function wasn't mocked
    %% Same crash would occur if a mocked function was called with
    %% arguments not listed in mocks.config
    9> bar:test(1).
    =ERROR REPORT==== 27-Aug-2011::15:07:46 ===
    ** Generic server foo_meck terminating
    ** Last message in was {'EXIT',<0.31.0>,
                                   {undef,[{bar,test,[1]},
                                           {erl_eval,do_apply,5},
                                           {shell,exprs,7},
                                           {shell,eval_exprs,7},
                                           {shell,eval_loop,3}]}}


_automeck_ can also combine multiple recording sessions into a single mocks.config via `automeck:combine_recordings/2`. This should simplify the case where automeck is reconfigured multiple times during a test suite run, e.g. eunit's foreach and foreachx constructs. The merging process is smart enough to find conflicting function calls and abort the merge. A conflicting function call is one where the same function (same module name, function name and arity) is called in different sessions with the same inputs but returns differing results. There's no way for automeck to handle this cleanly so aborting the merge process is the only sane option.

_automeck_ started out as an experimental hack but I think these features are generally useful for testing and understanding non-trivial Erlang systems.

_automeck_'s lack of docs, specs, and tests will be addressed either as I have time or as I receive pull requests. Bug reports and/or suggestions also welcome :-)
Jiffy - JSON NIFs for Erlang
============================

A JSON parser as a NIF. This is a complete rewrite of the work I did
in EEP0018 that was based on Yajl. This new version is a hand crafted
state machine that does its best to be as quick and efficient as
possible while not placing any constraints on the parsed JSON.

[![Build Status](https://travis-ci.org/davisp/jiffy.svg?branch=master)](https://travis-ci.org/davisp/jiffy)

Usage
-----

Jiffy is a simple API. The only thing that might catch you off guard
is that the return type of `jiffy:encode/1` is an iolist even though
it returns a binary most of the time.

A quick note on unicode. Jiffy only understands UTF-8 in binaries. End
of story.

Errors are raised as exceptions.

    Eshell V5.8.2  (abort with ^G)
    1> jiffy:decode(<<"{\"foo\": \"bar\"}">>).
    {[{<<"foo">>,<<"bar">>}]}
    2> Doc = {[{foo, [<<"bing">>, 2.3, true]}]}.
    {[{foo,[<<"bing">>,2.3,true]}]}
    3> jiffy:encode(Doc).
    <<"{\"foo\":[\"bing\",2.3,true]}">>

`jiffy:decode/1,2`
------------------

* `jiffy:decode(IoData)`
* `jiffy:decode(IoData, Options)`

The options for decode are:

* `{bytes_per_iter, N}` where N &gt;= 0 - This controls the number of
  bytes that Jiffy will process before yielding back to the VM. The
  mechanics of this yield are completely hidden from the end user.
* `return_maps` - Tell Jiffy to return objects using the maps data type
  on VMs that support it. This raises an error on VMs that don't support
  maps.

`jiffy:encode/1,2`
------------------

* `jiffy:encode(EJSON)`
* `jiffy:encode(EJSON, Options)`

where EJSON is a valid representation of JSON in Erlang according to
the table below.

The options for encode are:

* `uescape` - Escapes UTF-8 sequences to produce a 7-bit clean output
* `pretty` - Produce JSON using two-space indentation
* `force_utf8` - Force strings to encode as UTF-8 by fixing broken
  surrogate pairs and/or using the replacement character to remove
  broken UTF-8 sequences in data.
* `{bytes_per_iter, N}` where N &gt;= 0 - This controls the number of
  bytes that Jiffy will generate before yielding back to the VM. The
  mechanics of this yield are completely hidden from the end user.

Data Format
-----------

    Erlang                          JSON            Erlang
    ==========================================================================

    null                       -> null           -> null
    true                       -> true           -> true
    false                      -> false          -> false
    "hi"                       -> [104, 105]     -> [104, 105]
    <<"hi">>                   -> "hi"           -> <<"hi">>
    hi                         -> "hi"           -> <<"hi">>
    1                          -> 1              -> 1
    1.25                       -> 1.25           -> 1.25
    []                         -> []             -> []
    [true, 1.0]                -> [true, 1.0]    -> [true, 1.0]
    {[]}                       -> {}             -> {[]}
    {[{foo, bar}]}             -> {"foo": "bar"} -> {[{<<"foo">>, <<"bar">>}]}
    {[{<<"foo">>, <<"bar">>}]} -> {"foo": "bar"} -> {[{<<"foo">>, <<"bar">>}]}
    #{<<"foo">> => <<"bar">>}  -> {"foo": "bar"} -> #{<<"foo">> -> <<"bar">>}

N.B. The last entry in this table is only valid for VM's that support
the `maps` data type (i.e., 17.0 and newer) and client code must pass
the `return_maps` option to `jiffy:decode/2`.

Improvements over EEP0018
-------------------------

Jiffy should be in all ways an improvemnt over EEP0018. It no longer
imposes limits on the nesting depth. It is capable of encoding and
decoding large numbers and it does quite a bit more validation of UTF-8 in strings.

erlang-bcrypt
=============

erlang-bcrypt is a wrapper around the OpenBSD Blowfish password hashing
algorithm, as described in `"A Future-Adaptable Password Scheme"`_ by Niels
Provos and David Mazieres.

.. _"A Future-Adaptable Password Scheme":
   http://www.openbsd.org/papers/bcrypt-paper.ps

Basic build instructions
------------------------

1. Build it (project uses rebar, but I've included a Makefile)::

        make

2. Run it (simple way, starting sasl, crypto and bcrypt)::

        erl -pa ebin -boot start_sasl -s crypto -s bcrypt

Basic usage instructions
------------------------

3. Hash a password using a salt with the default number of rounds::

        1> {ok, Salt} = bcrypt:gen_salt().
        {ok,"$2a$12$sSS8Eg.ovVzaHzi1nUHYK."}
        2> {ok, Hash} = bcrypt:hashpw("foo", Salt).
        {ok,"$2a$12$sSS8Eg.ovVzaHzi1nUHYK.HbUIOdlQI0iS22Q5rd5z.JVVYH6sfm6"}

3. Verify the password::

        3> {ok, Hash} =:= bcrypt:hashpw("foo", Hash).
        true
        4> {ok, Hash} =:= bcrypt:hashpw("bar", Hash).
        false

Configuration
-------------

The bcrypt application is configured by changing values in the
application's environment:

``default_log_rounds``
  Sets the default number of rounds which define the complexity of the
  hash function. Defaults to ``12``.

``mechanism``
  Specifies whether to use the NIF implementation (``'nif'``) or a
  pool of port programs (``'port'``). Defaults to ``'nif'``.

  `Note: the NIF implementation no longer blocks the Erlang VM
  scheduler threads`

``pool_size``
  Specifies the size of the port program pool. Defaults to ``4``.

Authors
-------

* `Hunter Morris`_
* `Mrinal Wadhwa`_

.. _Hunter Morris:
   http://github.com/skarab

.. _Mrinal Wadhwa:
   http://github.com/mrinalwadhwa
# ibrowse [![Build Status](https://secure.travis-ci.org/johannesh/ibrowse.png)](http://travis-ci.org/johannesh/ibrowse)

ibrowse is a HTTP client written in erlang.

**License:** ibrowse is available under two different licenses.
  LGPL or the BSD license.

**Comments to:** chandrashekhar.mullaparthi@gmail.com

**Current Version:** 4.0.1

**Latest Version:** git://github.com/cmullaparthi/ibrowse.git



## Features

*  [RFC2616](http://www.ietf.org/rfc/rfc2616.txt) compliant (AFAIK)
*  supports GET, POST, OPTIONS, HEAD, PUT, DELETE, TRACE,
   MKCOL, PROPFIND, PROPPATCH, LOCK, UNLOCK, MOVE and COPY
*  Understands HTTP/0.9, HTTP/1.0 and HTTP/1.1
*  Understands chunked encoding
*  Can generate requests using [Chunked Transfer-Encoding](http://en.wikipedia.org/wiki/Chunked_transfer_encoding)
*  Pools of connections to each webserver
*  Pipelining support
*  Download to file
*  Asynchronous requests. Responses are streamed to a process
*  Basic authentication
*  Supports proxy authentication
*  Can talk to secure webservers using SSL
*  *Any other features in the code not listed here :)*



## Usage Examples

Remember to start ibrowse first:

```erlang
5> ibrowse:start().
{ok,<0.94.0>}
```



### Synchronous Requests

A simple `GET` request:

```erlang
6> ibrowse:send_req("http://intranet/messenger/", [], get).
{ok,"200",
    [{"Server","Microsoft-IIS/5.0"},
     {"Content-Location","http://intranet/messenger/index.html"},
     {"Date","Fri, 17 Dec 2004 15:16:19 GMT"},
     {"Content-Type","text/html"},
     {"Accept-Ranges","bytes"},
     {"Last-Modified","Fri, 17 Dec 2004 08:38:21 GMT"},
     {"Etag","\"aa7c9dc313e4c41:d77\""},
     {"Content-Length","953"}],
    "<html>...</html>"}
```


A `GET` using a proxy:

```erlang
7> ibrowse:send_req("http://www.google.com/", [], get, [],
                 [{proxy_user, "XXXXX"},
                  {proxy_password, "XXXXX"},
                  {proxy_host, "proxy"},
                  {proxy_port, 8080}], 1000).
{ok,"302",
    [{"Date","Fri, 17 Dec 2004 15:22:56 GMT"},
     {"Content-Length","217"},
     {"Content-Type","text/html"},
     {"Set-Cookie",
      "PREF=ID=f58155c797f9..."},
     {"Server","GWS/2.1"},
     {"Location",
      "http://www.google.co.uk/cxfer?c=PREF%3D:TM%3D110329..."},
     {"Via","1.1 netapp01 (NetCache NetApp/5.5R2)"}],
    "<HTML>...</HTML>\r\n"}
```


A `GET` response saved to file. A temporary file is created and the
filename returned. The response will only be saved to file if the
status code is in the `200` range. The directory to download to can
be set using the application env var `download_dir` - the default
is the current working directory:

```erlang
8> ibrowse:send_req("http://www.erlang.se/", [], get, [],
                 [{proxy_user, "XXXXX"},
                  {proxy_password, "XXXXX"},
                  {proxy_host, "proxy"},
                  {proxy_port, 8080},
                  {save_response_to_file, true}], 1000).
{error,req_timedout}

9> ibrowse:send_req("http://www.erlang.se/", [], get, [],
                 [{proxy_user, "XXXXX"},
                  {proxy_password, "XXXXX"},
                  {proxy_host, "proxy"},
                  {proxy_port, 8080},
                  {save_response_to_file, true}], 5000).
{ok,"200",
    [{"Transfer-Encoding","chunked"},
     {"Date","Fri, 17 Dec 2004 15:24:36 GMT"},
     {"Content-Type","text/html"},
     {"Server","Apache/1.3.9 (Unix)"},
     {"Via","1.1 netapp01 (NetCache NetApp/5.5R2)"}],
    {file,"/Users/chandru/code/ibrowse/src/ibrowse_tmp_file_1103297041125854"}}
```


Setting the size of the connection pool and pipeline. This sets the
number of maximum connections to the specified server to `10` and the pipeline
size to `1`. Connections are assumed to be already setup.

```erlang
11> ibrowse:set_dest("www.hotmail.com", 80, [{max_sessions, 10},
                                             {max_pipeline_size, 1}]).
ok
```


Example using the `HEAD` method:

```erlang
56> ibrowse:send_req("http://www.erlang.org", [], head).
{ok,"200",
    [{"Date","Mon, 28 Feb 2005 04:40:53 GMT"},
     {"Server","Apache/1.3.9 (Unix)"},
     {"Last-Modified","Thu, 10 Feb 2005 09:31:23 GMT"},
     {"Etag","\"8d71d-1efa-420b29eb\""},
     {"Accept-ranges","bytes"},
     {"Content-Length","7930"},
     {"Content-Type","text/html"}],
    []}
```


Example using the `OPTIONS` method:

```erlang
62> ibrowse:send_req("http://www.sun.com", [], options).
{ok,"200",
    [{"Server","Sun Java System Web Server 6.1"},
     {"Date","Mon, 28 Feb 2005 04:44:39 GMT"},
     {"Content-Length","0"},
     {"P3p",
      "policyref=\"http://www.sun.com/p3p/Sun_P3P_Policy.xml\", CP=\"CAO DSP COR CUR ADMa DEVa TAIa PSAa PSDa CONi TELi OUR  SAMi PUBi IND PHY ONL PUR COM NAV INT DEM CNT STA POL PRE GOV\""},
     {"Set-Cookie",
      "SUN_ID=X.X.X.X:169191109565879; EXPIRES=Wednesday, 31-Dec-2025 23:59:59 GMT; DOMAIN=.sun.com; PATH=/"},
     {"Allow",
      "HEAD, GET, PUT, POST, DELETE, TRACE, OPTIONS, MOVE, INDEX, MKDIR, RMDIR"}],
    []}
```



### Asynchronous Requests

Example of an asynchronous `GET` request:

```erlang
18> ibrowse:send_req("http://www.google.com", [], get, [],
                     [{proxy_user, "XXXXX"},
                      {proxy_password, "XXXXX"},
                      {proxy_host, "proxy"},
                      {proxy_port, 8080},
                      {stream_to, self()}]).
{ibrowse_req_id,{1115,327256,389608}}

19> flush().
Shell got {ibrowse_async_headers,{1115,327256,389608},
           "302",
           [{"Date","Thu, 05 May 2005 21:06:41 GMT"},
            {"Content-Length","217"},
            {"Content-Type","text/html"},
            {"Set-Cookie",
             "PREF=ID=b601f16bfa32f071:CR=1:TM=1115327201:LM=1115327201:S=OX5hSB525AMjUUu7; expires=Sun, 17-Jan-2038 19:14:07 GMT; path=/; domain=.google.com"},
            {"Server","GWS/2.1"},
            {"Location",
             "http://www.google.co.uk/cxfer?c=PREF%3D:TM%3D1115327201:S%3DDS9pDJ4IHcAuZ_AS&prev=/"},
            {"Via",
             "1.1 hatproxy01 (NetCache NetApp/5.6.2)"}]}
Shell got {ibrowse_async_response,{1115,327256,389608},
           "<HTML>...</HTML>\r\n"}
Shell got {ibrowse_async_response_end,{1115,327256,389608}}
ok
```


Another asynchronous `GET` request:

```erlang
24> ibrowse:send_req("http://yaws.hyber.org/simple_ex2.yaws", [], get, [],
                     [{proxy_user, "XXXXX"},
                      {proxy_password, "XXXXX"},
                      {proxy_host, "proxy"},
                      {proxy_port, 8080},
                      {stream_to, self()}]).
{ibrowse_req_id,{1115,327430,512314}}

25> flush().
Shell got {ibrowse_async_headers,{1115,327430,512314},
           "200",
           [{"Date","Thu, 05 May 2005 20:58:08 GMT"},
            {"Content-Length","64"},
            {"Content-Type","text/html;charset="},
            {"Server",
             "Yaws/1.54 Yet Another Web Server"},
            {"Via",
             "1.1 hatproxy01 (NetCache NetApp/5.6.2)"}]}
Shell got {ibrowse_async_response,{1115,327430,512314},
           "<html>...</html>\n"}
Shell got {ibrowse_async_response_end,{1115,327430,512314}}
```


Example of request which fails when using the async option. Here
the `{ibrowse_req_id, ReqId}` is not returned. Instead the error code is
returned.

```erlang
68> ibrowse:send_req("http://www.earlyriser.org", [], get, [], [{stream_to, self()}]).
{error,conn_failed}
```



### Other Examples

Example of request using both Proxy-Authorization and authorization
by the final webserver:

```erlang
17> ibrowse:send_req("http://www.erlang.se/lic_area/protected/patches/erl_756_otp_beam.README",
                     [], get, [],
                     [{proxy_user, "XXXXX"},
                      {proxy_password, "XXXXX"},
                      {proxy_host, "proxy"},
                      {proxy_port, 8080},
                      {basic_auth, {"XXXXX", "XXXXXX"}}]).
{ok,"200",
    [{"Accept-Ranges","bytes"},
     {"Date","Thu, 05 May 2005 21:02:09 GMT"},
     {"Content-Length","2088"},
     {"Content-Type","text/plain"},
     {"Server","Apache/1.3.9 (Unix)"},
     {"Last-Modified","Tue, 03 May 2005 15:08:18 GMT"},
     {"ETag","\"1384c8-828-427793e2\""},
     {"Via","1.1 hatproxy01 (NetCache NetApp/5.6.2)"}],
    "Patch Id:\t\terl_756_otp_beam\n..."}
```


Example of a `TRACE` request. Very interesting! yaws.hyber.org didn't
support this. Nor did www.google.com. But good old BBC supports this:

```erlang
35> 37> ibrowse:send_req("http://www.bbc.co.uk/", [], trace, [],
                         [{proxy_user, "XXXXX"},
                          {proxy_password, "XXXXX"},
                          {proxy_host, "proxy"},
                          {proxy_port, 8080}]).
{ok,"200",
    [{"Transfer-Encoding","chunked"},
     {"Date","Thu, 05 May 2005 21:40:27 GMT"},
     {"Content-Type","message/http"},
     {"Server","Apache/2.0.51 (Unix)"},
     {"Set-Cookie",
      "BBC-UID=7452e72a..."},
     {"Set-Cookie",
      "BBC-UID=7452e72a..."},
     {"Via","1.1 hatproxy01 (NetCache NetApp/5.6.2)"}],
    "TRACE / HTTP/1.1\r\nHost: www.bbc.co.uk\r\nConnection: keep-alive\r\nX-Forwarded-For: 172.24.28.29\r\nVia: 1.1 hatproxy01 (NetCache NetApp/5.6.2)\r\nCookie: BBC-UID=7452e...\r\n\r\n"}
```
# opscoderl_httpc #

Http client library

## Author(s) ##

* Oliver Ferrigni <oliver@opscode.com>

## Copyright ##

Copyright (c) 2013 Opscode, Inc.  All rights reserved.


### opscoderl_httpc

 The goal of this library is to provide a drop-in replacement for ibrowse
that leverages pooler for process pooling and ibrowse for http client requests.

This is the README for darklaunch. darklaunch is an Erlang daemon
which manages a JSON file describing the feature flags available to
each org.

* License

All files in the repository are licensed under the Apache 2.0 license. If any
file is missing the License header it should assume the following is attached;


Copyright 2014 Chef Software Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


Building & Running darklaunch:
1) make rel
2) cd rel/darklaunch
3) bin/darklaunch console

Hacking on darklaunch:
1) make devrel(*)
2) Edit code
3) Compile and reload via 'make update'(**)

*The devrel target generates a standard OTP release and then
 symlinks the code for all dependencies and the application
 code into the resulting release tree. This allows a shorter
 edit/compile/debug cycle during development when devrel is
 coupled with 'make update'.

** The update target compiles any changed files and performs
   a warm restart of the Erlang VM. This triggers a global
   code reload. This is very handy when hacking on the code
   or trying to debug a problem. 'make update' only works when
   a release has been built via 'make devrel'.Overview
--------
Lager (as in the beer) is a logging framework for Erlang. Its purpose is
to provide a more traditional way to perform logging in an erlang application
that plays nicely with traditional UNIX logging tools like logrotate and
syslog.

  [Travis-CI](http://travis-ci.org/basho/lager) :: ![Travis-CI](https://secure.travis-ci.org/basho/lager.png)

Features
--------
* Finer grained log levels (debug, info, notice, warning, error, critical,
  alert, emergency)
* Logger calls are transformed using a parse transform to allow capturing
  Module/Function/Line/Pid information
* When no handler is consuming a log level (eg. debug) no event is sent
  to the log handler
* Supports multiple backends, including console and file.
* Rewrites common OTP error messages into more readable messages
* Support for pretty printing records encountered at compile time
* Tolerant in the face of large or many log messages, won't out of memory the node
* Supports internal time and date based rotation, as well as external rotation tools
* Syslog style log level comparison flags
* Colored terminal output (requires R16+)
* Map support (requires 17+)

Usage
-----
To use lager in your application, you need to define it as a rebar dep or have
some other way of including it in Erlang's path. You can then add the
following option to the erlang compiler flags:

```erlang
{parse_transform, lager_transform}
```

Alternately, you can add it to the module you wish to compile with logging
enabled:

```erlang
-compile([{parse_transform, lager_transform}]).
```

Before logging any messages, you'll need to start the lager application. The
lager module's `start` function takes care of loading and starting any dependencies
lager requires.

```erlang
lager:start().
```

You can also start lager on startup with a switch to `erl`:

```erlang
erl -pa path/to/lager/ebin -s lager
```

Once you have built your code with lager and started the lager application,
you can then generate log messages by doing the following:

```erlang
lager:error("Some message")
```

  Or:

```erlang
lager:warning("Some message with a term: ~p", [Term])
```

The general form is `lager:Severity()` where `Severity` is one of the log levels
mentioned above.

Configuration
-------------
To configure lager's backends, you use an application variable (probably in
your app.config):

```erlang
{lager, [
  {log_root, "/var/log/hello"},
  {handlers, [
    {lager_console_backend, info},
    {lager_file_backend, [{file, "error.log"}, {level, error}]},
    {lager_file_backend, [{file, "console.log"}, {level, info}]}
  ]}
]}.
```

```log_root``` variable is optional, by default file paths are relative to CWD.

The available configuration options for each backend are listed in their
module's documentation.

Custom Formatting
-----------------
All loggers have a default formatting that can be overriden.  A formatter is any module that
exports `format(#lager_log_message{},Config#any())`.  It is specified as part of the configuration
for the backend:

```erlang
{lager, [
  {handlers, [
    {lager_console_backend, [info, {lager_default_formatter, [time," [",severity,"] ", message, "\n"]}]},
    {lager_file_backend, [{file, "error.log"}, {level, error}, {formatter, lager_default_formatter},
      {formatter_config, [date, " ", time," [",severity,"] ",pid, " ", message, "\n"]}]},
    {lager_file_backend, [{file, "console.log"}, {level, info}]}
  ]}
]}.
```

Included is `lager_default_formatter`.  This provides a generic, default formatting for log messages using a structure similar to Erlang's [iolist](http://learnyousomeerlang.com/buckets-of-sockets#io-lists) which we call "semi-iolist":

* Any traditional iolist elements in the configuration are printed verbatim.
* Atoms in the configuration are treated as placeholders for lager metadata and extracted from the log message.
    * The placeholders `date`, `time`, `message`, and `severity` will always exist.
    * The placeholders `pid`, `file`, `line`, `module`, `function`, and `node` will always exist if the parse transform is used.
    * Applications can define their own metadata placeholder.
    * A tuple of `{atom(), semi-iolist()}` allows for a fallback for
      the atom placeholder. If the value represented by the atom
      cannot be found, the semi-iolist will be interpreted instead.
    * A tuple of `{atom(), semi-iolist(), semi-iolist()}` represents a
      conditional operator: if a value for the atom placeholder can be
      found, the first semi-iolist will be output; otherwise, the
      second will be used.

Examples:

```
["Foo"] -> "Foo", regardless of message content.
[message] -> The content of the logged message, alone.
[{pid,"Unknown Pid"}] -> "<?.?.?>" if pid is in the metadata, "Unknown Pid" if not.
[{pid, ["My pid is ", pid], ["Unknown Pid"]}] -> if pid is in the metadata print "My pid is <?.?.?>", otherwise print "Unknown Pid"
[{server,{pid, ["(", pid, ")"], ["(Unknown Server)"]}}] -> user provided server metadata, otherwise "(<?.?.?>)", otherwise "(Unknown Server)"
```

Error logger integration
------------------------
Lager is also supplied with a `error_logger` handler module that translates
traditional erlang error messages into a friendlier format and sends them into
lager itself to be treated like a regular lager log call. To disable this, set
the lager application variable `error_logger_redirect` to `false`.

The `error_logger` handler will also log more complete error messages (protected
with use of `trunc_io`) to a "crash log" which can be referred to for further
information. The location of the crash log can be specified by the crash_log
application variable. If set to `undefined` it is not written at all.

Messages in the crash log are subject to a maximum message size which can be
specified via the `crash_log_msg_size` application variable.

Overload Protection
-------------------

Prior to lager 2.0, the `gen_event` at the core of lager operated purely in
synchronous mode. Asynchronous mode is faster, but has no protection against
message queue overload. In lager 2.0, the `gen_event` takes a hybrid approach. it
polls its own mailbox size and toggles the messaging between synchronous and
asynchronous depending on mailbox size.

```erlang
{async_threshold, 20},
{async_threshold_window, 5}
```

This will use async messaging until the mailbox exceeds 20 messages, at which
point synchronous messaging will be used, and switch back to asynchronous, when
size reduces to `20 - 5 = 15`.

If you wish to disable this behaviour, simply set it to `undefined`. It defaults
to a low number to prevent the mailbox growing rapidly beyond the limit and causing
problems. In general, lager should process messages as fast as they come in, so getting
20 behind should be relatively exceptional anyway.

If you want to limit the number of messages per second allowed from `error_logger`,
which is a good idea if you want to weather a flood of messages when lots of
related processes crash, you can set a limit:

```erlang
{error_logger_hwm, 50}
```

It is probably best to keep this number small.

Runtime loglevel changes
------------------------
You can change the log level of any lager backend at runtime by doing the
following:

```erlang
lager:set_loglevel(lager_console_backend, debug).
```

  Or, for the backend with multiple handles (files, mainly):

```erlang
lager:set_loglevel(lager_file_backend, "console.log", debug).
```

Lager keeps track of the minimum log level being used by any backend and
suppresses generation of messages lower than that level. This means that debug
log messages, when no backend is consuming debug messages, are effectively
free. A simple benchmark of doing 1 million debug log messages while the
minimum threshold was above that takes less than half a second.

Syslog style loglevel comparison flags
--------------------------------------
In addition to the regular log level names, you can also do finer grained masking
of what you want to log:

```
info - info and higher (>= is implicit)
=debug - only the debug level
!=info - everything but the info level
<=notice - notice and below
<warning - anything less than warning
```

These can be used anywhere a loglevel is supplied, although they need to be either
a quoted atom or a string.

Internal log rotation
---------------------
Lager can rotate its own logs or have it done via an external process. To
use internal rotation, use the `size`, `date` and `count` values in the file
backend's config:

```erlang
[{file, "error.log"}, {level, error}, {size, 10485760}, {date, "$D0"}, {count, 5}]
```

This tells lager to log error and above messages to `error.log` and to
rotate the file at midnight or when it reaches 10mb, whichever comes first,
and to keep 5 rotated logs in addition to the current one. Setting the
count to 0 does not disable rotation, it instead rotates the file and keeps
no previous versions around. To disable rotation set the size to 0 and the
date to "".

The `$D0` syntax is taken from the syntax newsyslog uses in newsyslog.conf.
The relevant extract follows:

```
Day, week and month time format: The lead-in character
for day, week and month specification is a `$'-sign.
The particular format of day, week and month
specification is: [Dhh], [Ww[Dhh]] and [Mdd[Dhh]],
respectively.  Optional time fields default to
midnight.  The ranges for day and hour specifications
are:

  hh      hours, range 0 ... 23
  w       day of week, range 0 ... 6, 0 = Sunday
  dd      day of month, range 1 ... 31, or the
          letter L or l to specify the last day of
          the month.

Some examples:
  $D0     rotate every night at midnight
  $D23    rotate every day at 23:00 hr
  $W0D23  rotate every week on Sunday at 23:00 hr
  $W5D16  rotate every week on Friday at 16:00 hr
  $M1D0   rotate on the first day of every month at
          midnight (i.e., the start of the day)
  $M5D6   rotate on every 5th day of the month at
          6:00 hr
```

To configure the crash log rotation, the following application variables are
used:
* `crash_log_size`
* `crash_log_date`
* `crash_log_count`

See the `.app.src` file for further details.

Syslog Support
--------------
Lager syslog output is provided as a separate application:
[lager_syslog](https://github.com/basho/lager_syslog). It is packaged as a
separate application so lager itself doesn't have an indirect dependency on a
port driver. Please see the `lager_syslog` README for configuration information.

Older Backends
--------------
Lager 2.0 changed the backend API, there are various 3rd party backends for
lager available, but they may not have been updated to the new API. As they
are updated, links to them can be re-added here.

Record Pretty Printing
----------------------
Lager's parse transform will keep track of any record definitions it encounters
and store them in the module's attributes. You can then, at runtime, print any
record a module compiled with the lager parse transform knows about by using the
`lager:pr/2` function, which takes the record and the module that knows about the record:

```erlang
lager:info("My state is ~p", [lager:pr(State, ?MODULE)])
```

Often, `?MODULE` is sufficent, but you can obviously substitute that for a literal module name.
`lager:pr` also works from the shell.

Colored terminal output
-----------------------
If you have Erlang R16 or higher, you can tell lager's console backend to be colored. Simply
add to lager's application environment config:

```erlang
{colored, true}
```

If you don't like the default colors, they are also configurable; see
the `.app.src` file for more details.

The output will be colored from the first occurrence of the atom color
in the formatting configuration. For example:

```erlang
{lager_console_backend, [info, {lager_default_formatter, [time, color, " [",severity,"] ", message, "\e[0m\r\n"]}]}
```

This will make the entire log message, except time, colored. The
escape sequence before the line break is needed in order to reset the
color after each log message.

Tracing
-------
Lager supports basic support for redirecting log messages based on log message
attributes. Lager automatically captures the pid, module, function and line at the
log message callsite. However, you can add any additional attributes you wish:

```erlang
lager:warning([{request, RequestID},{vhost, Vhost}], "Permission denied to ~s", [User])
```

Then, in addition to the default trace attributes, you'll be able to trace
based on request or vhost:

```erlang
lager:trace_file("logs/example.com.error", [{vhost, "example.com"}], error)
```

To persist metadata for the life of a process, you can use `lager:md/1` to store metadata
in the process dictionary:

```erlang
lager:md([{zone, forbidden}])
```

Note that `lager:md` will *only* accept a list of key/value pairs keyed by atoms.

You can also omit the final argument, and the loglevel will default to
`debug`.

Tracing to the console is similar:

```erlang
lager:trace_console([{request, 117}])
```

In the above example, the loglevel is omitted, but it can be specified as the
second argument if desired.

You can also specify multiple expressions in a filter, or use the `*` atom as
a wildcard to match any message that has that attribute, regardless of its
value.

Tracing to an existing logfile is also supported, if you wanted to log
warnings from a particular function in a particular module to the default `error.log`:

```erlang
lager:trace_file("log/error.log", [{module, mymodule}, {function, myfunction}], warning)
```

To view the active log backends and traces, you can use the `lager:status()`
function. To clear all active traces, you can use `lager:clear_all_traces()`.

To delete a specific trace, store a handle for the trace when you create it,
that you later pass to `lager:stop_trace/1`:

```erlang
{ok, Trace} = lager:trace_file("log/error.log", [{module, mymodule}]),
...
lager:stop_trace(Trace)
```

Tracing to a pid is somewhat of a special case, since a pid is not a
data-type that serializes well. To trace by pid, use the pid as a string:

```erlang
lager:trace_console([{pid, "<0.410.0>"}])
```

As of lager 2.0, you can also use a 3 tuple while tracing, where the second
element is a comparison operator. The currently supported comparison operators
are:

* `<` - less than
* `=` - equal to
* `>` - greater than

```erlang
lager:trace_console([{request, '>', 117}, {request, '<', 120}])
```

Using `=` is equivalent to the 2-tuple form.

Setting the truncation limit at compile-time
--------------------------------------------
Lager defaults to truncating messages at 4096 bytes, you can alter this by
using the `{lager_truncation_size, X}` option. In rebar, you can add it to
`erl_opts`:

```erlang
{erl_opts, [{parse_transform, lager_transform}, {lager_truncation_size, 1024}]}.
```

You can also pass it to `erlc`, if you prefer:

```
erlc -pa lager/ebin +'{parse_transform, lager_transform}' +'{lager_truncation_size, 1024}' file.erl
```
envy
====

An enhancement for application:get_env to provide data validation and sensible error messages.Erlang UUID Implementation
==========================

http://www.ietf.org/rfc/rfc4122.txt is the reference for official UUIDs.
This implementation provides a version 1 UUID that includes both the Erlang pid
identifier (ID, Serial, Creation) and the distributed Erlang node name within
the 48 bit node ID.  To make room for the Erlang pid identifier, the 48 bits
from the MAC address (i.e., 3 OCI (Organizationally Unique Identifier) bytes and
3 NIC (Network Interface Controller) specific bytes) and the distributed Erlang
node name are bitwise-XORed down to 16 bits. The Erlang pid is 
bitwise-XORed from 72 bits down to 32 bits.
The version 3 (MD5), version 4 (random), and version 5 (SHA)
methods are provided as specified within the RFC.

Requires `Erlang >= R16B01`

Build
-----

    rebar get-deps
    rebar compile

Author
------

Michael Truog (mjtruog [at] gmail (dot) com)

License
-------

BSD

# opscoderl_wm #

Opscode helpers for Webmachine. Here you will find the following modules:

## License

All files in the repository are licensed under the Apache 2.0 license. If any
file is missing the License header it should assume the following is attached;

```
Copyright 2014 Chef Software Inc

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```

## oc_wm_request

Helper functions for use in a wm callback module.

Includes `make_req_id/0` for generating a random request id,
`read_req_id/2` for reading the req id out of a header and generating
one if none is found, and `add_notes/2` for annotating req data for
use in logging.

## oc_wm_request_logger

A request logger for use with Webmachine logging hooks. To use this
logger, add the following to your application's config:

```
  {webmachine, [
          {log_handlers, [
               {oc_wm_request_logger, [
                       {file, "requests.log"},
                       {file_size, 100},
                       {files, 10},
                       {annotations, [req_id, org_name, msg, darklaunch, perf_stats]}
                       ]
                      }]}]
      }
```

The `annotations` key is optional. If you specify annotation keys,
then values corresponding to those keys found in wm request's `notes`
field are extracted and integrated into the log entry.

### How webmachine starts a pluggable logger

The mechanism by which log handlers are added to wm's event logger is
a bit twisty. Here's an overview to help trace it down in the code if
you need it.

Webmachine starts your logger in `webmachine_app.erl` where a call to
`supervisor:start_child(webmachine_logger_watcher_sup, ...)` is made
for each handler found in app config. That call starts a new
`webmachine_logger_watcher` for each handler. In the init of
`webmachine_logger_watcher` you will find a call to
`gen_event:add_sup_handler` on the `webmachine_log_event` event logger
which is where your handler is actually installed.

# Guidelines for opscoderl helper repos #

This repository is the first in what we hope will be a useful pattern
for collecting reusable Erlang code. The idea is to balance the
extremes of a dumping ground "commons" repo that would force consumers
to pull in dependencies that they won't use with a proliferation of
single module repos (hi, that's what this is for now, sorry).

Helper repos should follow these guidelines:

1. Be named `opscoderl_$BLAH` where `$BLAH` names a dependency that
   is wrapped (e.g. this repo with folsom) OR a well defined bit of
   functionality. I think we will soon have an `opscoderl_json` repo
   that pulls in jiffy and ej.

2. Minimal focused set of dependencies. A dependency is reasonable if
   any user of the helper will want the dependency. Conversely, a
   dependency that covers a small or rare use case should be given
   extra scrutiny. As a consumer of a helper, it is unpleasant to have
   to pull in a dependency that you aren't going to use. A tag or git
   SHA should be used by the helper to peg the version of the
   dependency.

3. Modules should be prefixed with `oc_`. Care should be taken not to
   conflict with modules from other opscoderl helper applications.

4. Open source and not product specific. May contain some
   Opscode-isms, but the intention is that these helpers can be
   generally useful (like erlware_commons).

# Guidelines for using opscoderl helpers #

1. Contrary to normal practice, avoid specifying the dependencies
   provided by the helper even if you use them directly. For example,
   depend only on `opscoderl_folsom` and use `oc_folsom` and
   `folsom`. This allows the version of the wrapped dependencies to be
   controlled by the helper app. Care needs to be taken in managing
   OTP release when a non-helper app shares a dependency with a
   helper. We may need to add direct deps in some cases to get the
   right behavior out of rebar and lock deps.

## License ##

|                      |                                          |
|:---------------------|:-----------------------------------------|
| **Copyright:**       | Copyright (c) 2013 Opscode, Inc.
| **License:**         | Apache License, Version 2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.


  eper is a loose collection of Erlang Performance related tools.

  sherk - a profiler, similar to Linux oprofile or MacOs shark
  gperf - a graphical performance monitor; shows CPU, memory and network usage
  dtop  - similar to unix top
  ntop  - visualizes network traffic
  atop  - shows various aspects of the VM allocators
  redbug- similar to the OTP dbg application, but safer, better etc.* ej helps you work with Erlang terms representing JSON

The ej module makes it easier to work with Erlang terms representing
[[http://json.org][JSON]] in the format returned by [[https://github.com/davisp/jiffy][jiffy]], [[https://github.com/mochi/mochiweb][mochijson2]], or [[https://github.com/benoitc/ejson][ejson]].  You can use
=ej:get/2= to walk an object and return a particular value, =ej:set/3=
to update a value within an object, or =ej:delete/2= to remove a value
from an object.

In ej, paths into JSON objects are expressed using a tuple of keys
like so:

| Javascript              | ej                                         |
| =Obj.author.name.first= | =ej:get({"author", "name", "first"}, Obj)= |

To get started using ej, see [[ej by example]] below.

ej also provides a means of validating a JSON object according to a
specification you provide. This feature is useful if you need to
process JSON request bodies. As a brief example, here's a
specification for a JSON object describing a person and their favorite
foods:

#+BEGIN_SRC erlang
{[
  {<<"name">>, {string_match, regex_for(name)}},
  {{opt, <<"nick_name">>}, {string_match, regex_for(name)}},
  {<<"foods">>, {array_map, string}}
 ]}
#+END_SRC


ej is independent of the library used for JSON serialization and
has no dependencies.

** ej by example

ej is best explained by example.  Consider the following JSON data
(borrowed from http://www.json.org/example.html):

#+BEGIN_SRC js
  {"menu": {
    "id": "file",
    "value": "File",
    "popup": {
      "menuitem": [
        {"value": "New", "onclick": "CreateNewDoc()"},
        {"value": "Open", "onclick": "OpenDoc()"},
        {"value": "Close", "onclick": "CloseDoc()"}
      ]
    }
  }}
#+END_SRC

=mochijson2:decode/1= translates the JSON into Erlang terms like this:

#+BEGIN_SRC erlang
  {struct,
   [{<<"menu">>,
     {struct,
      [{<<"id">>,<<"file">>},
       {<<"value">>,<<"File">>},
       {<<"popup">>,
        {struct,
         [{<<"menuitem">>,
           [{struct,[{<<"value">>,<<"New">>},
                     {<<"onclick">>,<<"CreateNewDoc()">>}]},
            {struct,[{<<"value">>,<<"Open">>},
                     {<<"onclick">>,<<"OpenDoc()">>}]},
            {struct,[{<<"value">>,<<"Close">>},
                     {<<"onclick">>,<<"CloseDoc()">>}]}]}]}}]}}]}
#+END_SRC

And here's ej in action:

#+BEGIN_SRC txt
% specify the path you want to access as a tuple of keys (you can use
% strings or binaries)
4> ej:get({"menu", "value"}, Obj).
<<"File">>

% you can access list elements by index
> ej:get({"menu", "popup", "menuitem", 2, "onclick"}, Obj).
<<"OpenDoc()">>

% The atoms 'first' and 'last' can be used for lists as well
> ej:get({"menu", "popup", "menuitem", first, "value"}, Obj).  
<<"New">>

% you can filter a list of objects by specifying a property (key/value
% pair) to match on:
ej:get({"menu", "popup", "menuitem", {select, {"value", "New"}}}, Obj).

% set a value
Obj2 = ej:set({"menu", "id"}, Obj, <<"abc123">>).

% add a value
Obj3 = ej:set({"menu", "new_key"}, Obj, <<"something">>).

% add a value to a list
NewItem = {struct,[{<<"value">>,<<"Save">>}, {<<"onclick">>,<<"SaveDoc()">>}]}.
Obj4 = ej:set({"menu", "popup", "menuitem", new}, Obj, NewItem).

#+END_SRC

The idea for this helper module was inspired by [[http://groups.google.com/group/erlang-programming/browse_thread/thread/7af6f99e740df979/97c50c0df25502cd?lnk=gst&q=Javascript+parse+transform#97c50c0df25502cd][this thread on the
Erlang Questions]] mailing list and, in particular, by the reply from
Richard O'Keefe.  Additional motivation from the very similar helper
module =struct= included in the [[http://beebole.com/en/blog/erlang/tutorial-web-application-erlang/][sticky notes example application]] from
the folks at BeeBole.

** THANKS

- Christopher Brown
- Christopher Maier
- John Keiser
- Sebastian Probst Eide

** Build status

#+ATTR_HTML: alt="Build status images" title="Build status on Travis-CI"
[[https://travis-ci.org/seth/ej.png]]


** License

ej is available under the Apache License, Version 2.0.

#+BEGIN_EXAMPLE
Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
#+END_EXAMPLE
* pooler - An OTP Process Pool Application

The pooler application allows you to manage pools of OTP behaviors
such as gen_servers, gen_fsms, or supervisors, and provide consumers
with exclusive access to pool members using =pooler:take_member=.

#+ATTR_HTML: alt="Build status images" title="Build status on Travis-CI"
[[https://travis-ci.org/seth/pooler.png]]

** What pooler does

*** Protects the members of a pool from being used concurrently

The main pooler interface is =pooler:take_member/1= and
=pooler:return_member/3=.  The pooler server will keep track of which
members are *in use* and which are *free*.  There is no need to call
=pooler:return_member= if the consumer is a short-lived process; in
this case, pooler will detect the consumer's normal exit and reclaim
the member.  To achieve this, pooler tracks the calling process of
=take_member= as the consumer of the pool member.  Thus pooler assumes
that there is no middle-man process calling =take_member= and handing
out the member pid to another worker process.

*** Maintains the size of the pool

You specify an initial and a maximum number of members in the pool.
Pooler will create new members on demand until the maximum member
count is reached.  New pool members are added to replace members that
crash.  If a consumer crashes, the member it was using will be
destroyed and replaced.  You can configure Pooler to periodically
check for and remove members that have not been used recently to
reduce the member count back to its initial size.

*** Manage multiple pools

You can use pooler to manage multiple independent pools and multiple
grouped pools. Independent pools allow you to pool clients for
different backend services (e.g. postgresql and redis). Grouped pools
can optionally be accessed using =pooler:take_group_member/1= to
provide load balancing of the pools in the group. A typical use of
grouped pools is to have each pool contain clients connected to a
particular node in a cluster (think database read slaves).  Pooler's
=take_group_member= function will randomly select a pool in the group
to fetch a member from.  If the randomly selected pool has no free
members, pooler will attempt to obtain a member from each pool in the
group.  If there is no pool with available members, pooler will return
=error_no_members=.

** Motivation

The need for pooler arose while writing an Erlang-based application
that uses [[https://wiki.basho.com/display/RIAK/][Riak]] for data storage.  Riak's protocol buffer client is a
=gen_server= process that initiates a connection to a Riak node.  A
pool is needed to avoid spinning up a new client for each request in
the application.  Reusing clients also has the benefit of keeping the
vector clocks smaller since each client ID corresponds to an entry in
the vector clock.

When using the Erlang protocol buffer client for Riak, one should
avoid accessing a given client concurrently.  This is because each
client is associated with a unique client ID that corresponds to an
element in an object's vector clock.  Concurrent action from the same
client ID defeats the vector clock.  For some further explanation,
see [[http://lists.basho.com/pipermail/riak-users_lists.basho.com/2010-September/001900.html][post 1]] and [[http://lists.basho.com/pipermail/riak-users_lists.basho.com/2010-September/001904.html][post 2]].  Note that concurrent access to Riak's pb client is
actual ok as long as you avoid updating the same key at the same
time.  So the pool needs to have checkout/checkin semantics that give
consumers exclusive access to a client.

On top of that, in order to evenly load a Riak cluster and be able to
continue in the face of Riak node failures, consumers should spread
their requests across clients connected to each node.  The client pool
provides an easy way to load balance.

Since writing pooler, I've seen it used to pool database connections
for PostgreSQL, MySQL, and Redis. These uses led to a redesign to
better support multiple independent pools.

** Usage and API

*** Pool Configuration via application environment

Pool configuration is specified in the pooler application's
environment.  This can be provided in a config file using =-config= or
set at startup using =application:set_env(pooler, pools,
Pools)=. Here's an example config file that creates two pools of
Riak pb clients each talking to a different node in a local cluster
and one pool talking to a Postgresql database:

#+BEGIN_SRC erlang
  % pooler.config
  % Start Erlang as: erl -config pooler
  % -*- mode: erlang -*-
  % pooler app config
  [
   {pooler, [
           {pools, [
                    [{name, rc8081},
                     {group, riak},
                     {max_count, 5},
                     {init_count, 2},
                     {start_mfa,
                      {riakc_pb_socket, start_link, ["localhost", 8081]}}],

                    [{name, rc8082},
                     {group, riak},
                     {max_count, 5},
                     {init_count, 2},
                     {start_mfa,
                      {riakc_pb_socket, start_link, ["localhost", 8082]}}],

                    [{name, pg_db1},
                     {max_count, 10},
                     {init_count, 2},
                     {start_mfa,
                      {my_pg_sql_driver, start_link, ["db_host"]}}]
                   ]}
             %% if you want to enable metrics, set this to a module with
             %% an API conformant to the folsom_metrics module.
             %% If this config is missing, then no metrics are sent.
             %% {metrics_module, folsom_metrics}
          ]}
  ].
#+END_SRC

Each pool has a unique name, specified as an atom, an initial and maximum number of members,
and an ={M, F, A}= describing how to start members of the pool.  When
pooler starts, it will create members in each pool according to
=init_count=. Optionally, you can indicate that a pool is part of a
group. You can use pooler to load balance across pools labeled with
the same group tag.

**** Culling stale members

The =cull_interval= and =max_age= pool configuration parameters allow
you to control how (or if) the pool should be returned to its initial
size after a traffic burst. Both parameters specify a time value which
is specified as a tuple with the intended units. The following
examples are valid:

#+BEGIN_SRC erlang
%% two minutes, your way
{2, min}
{120, sec}
{1200, ms}
#+END_SRC

The =cull_interval= determines the schedule when a check will be made
for stale members. Checks are scheduled using =erlang:send_after/3=
which provides a light-weight timing mechanism. The next check is
scheduled after the prior check completes.

During a check, pool members that have not been used in more than
=max_age= minutes will be removed until the pool size reaches
=init_count=.

The default value for =cull_interval= is ={1, min}=. You can disable
culling by specifying a value os ={0, min}=. The =max_age= parameter
defaults to ={30, sec}=.

*** Pool Configuration via =pooler:new_pool=
You can create pools using =pooler:new_pool/1= when accepts a
proplist of pool configuration. Here's an example:
#+BEGIN_SRC erlang
PoolConfig = [{name, rc8081},
              {group, riak},
              {max_count, 5},
              {init_count, 2},
              {start_mfa,
               {riakc_pb_socket,
                start_link, ["localhost", 8081]}}],
pooler:new_pool(PoolConfig).
#+END_SRC
*** Using pooler

Here's an example session:

#+BEGIN_SRC erlang
application:start(pooler).
P = pooler:take_member(mysql),
% use P
pooler:return_member(mysql, P, ok).
#+END_SRC

Once started, the main interaction you will have with pooler is
through two functions, =take_member/1= and =return_member/3= (or
=return_member/2=).

Call =pooler:take_member(Pool)= to obtain the pid belonging to a
member of the pool =Pool=.  When you are done with it, return it to
the pool using =pooler:return_member(Pool, Pid, ok)=.  If you
encountered an error using the member, you can pass =fail= as the
second argument.  In this case, pooler will permanently remove that
member from the pool and start a new member to replace it.  If your
process is short lived, you can omit the call to =return_member=.  In
this case, pooler will detect the normal exit of the consumer and
reclaim the member.

If you would like to obtain a member from a randomly selected pool in
a group, call =pooler:take_group_member(Group)=. This will return a
=Pid= which must be returned using =pooler:return_group_member/2= or
=pooler:return_group_member/3=.

*** pooler as an included application

In order for pooler to start properly, all applications required to
start a pool member must be start before pooler starts. Since pooler
does not depend on members and since OTP may parallelize application
starts for applications with no detectable dependencies, this can
cause problems. One way to work around this is to specify pooler as an
included application in your app. This means you will call pooler's
top-level supervisor in your app's top-level supervisor and can regain
control over the application start order. To do this, you would remove
pooler from the list of applications in your_app.app and add
it to the included_application key:

#+BEGIN_SRC erlang
{application, your_app,
 [
  {description, "Your App"},
  {vsn, "0.1"},
  {registered, []},
  {applications, [kernel,
                  stdlib,
                  crypto,
                  mod_xyz]},
  {included_applications, [pooler]},
  {mod, {your_app, []}}
 ]}.
#+END_SRC

Then start pooler's top-level supervisor with something like the
following in your app's top-level supervisor:

#+BEGIN_SRC erlang
PoolerSup = {pooler_sup, {pooler_sup, start_link, []},
             permanent, infinity, supervisor, [pooler_sup]},
{ok, {{one_for_one, 5, 10}, [PoolerSup]}}.
#+END_SRC

*** Metrics
You can enable metrics collection by adding a =metrics_module= entry
to pooler's app config. Metrics are disabled by default. The module
specified must have an API matching that of the [[https://github.com/boundary/folsom/blob/master/src/folsom_metrics.erl][folsom_metrics]] module
in [[https://github.com/boundary/folsom][folsom]] (to use folsom, specify ={metrics_module, folsom_metrics}}=
and ensure that folsom is in your code path and has been started.

When enabled, the following metrics will be tracked:

| Metric Label                  | Description                                                                 |
| pooler.POOL_NAME.take_rate    | meter recording rate at which take_member is called                         |
| pooler.error_no_members_count | counter indicating how many times take_member has returned error_no_members |
| pooler.killed_free_count      | counter how many members have been killed when in the free state            |
| pooler.killed_in_use_count    | counter how many members have been killed when in the in_use state          |
| pooler.event                  | history various error conditions                                            |

*** Demo Quick Start

1. Clone the repo:
   #+BEGIN_EXAMPLE
   git clone https://github.com/seth/pooler.git
   #+END_EXAMPLE
2. Build and run tests:
   #+BEGIN_EXAMPLE
   cd pooler; make && make test
   #+END_EXAMPLE
3. Start a demo
   #+BEGIN_EXAMPLE
   erl -pa .eunit ebin -config demo

   Erlang R16B03 (erts-5.10.4) [source] [64-bit] [smp:8:8] [async-threads:10] [kernel-poll:false]

   Eshell V5.10.4  (abort with ^G)
   1> application:start(pooler).
   ok
   2> M = pooler:take_member(pool1).
   <0.44.0>
   3> pooled_gs:get_id(M).
   {"p1",#Ref<0.0.0.38>}
   4> M2 = pooler:take_member(pool1).
   <0.45.0>
   5> pooled_gs:get_id(M2).
   {"p1",#Ref<0.0.0.40>}
   6> pooler:return_member(pool1, M, ok).
   ok
   7> pooler:return_member(pool1, M2, ok).
   ok
   #+END_EXAMPLE

** Implementation Notes
*** Overview of supervision

[[./doc/pooler-sup-tree.png]]

The top-level supervisor is pooler_sup. It supervises one supervisor
for each pool configured in pooler's app config.

At startup, a pooler_NAME_pool_sup is started for each pool described in
pooler's app config with NAME matching the name attribute of the
config.

The pooler_NAME_pool_sup starts the gen_server that will register with
pooler_NAME_pool as well as a pooler_NAME_member_sup that will be used
to start and supervise the members of this pool. The
pooler_starter_sup is used to start temporary workers used for
managing async member start.

pooler_sup:                one_for_one
pooler_NAME_pool_sup:      all_for_one
pooler_NAME_member_sup:    simple_one_for_one
pooler_starter_sup:        simple_one_for_one

Groups of pools are managed using the pg2 application. This imposes a
requirement to set a configuration parameter on the kernel application
in an OTP release. Like this in sys.config:
#+begin_src erlang
{kernel, [{start_pg2, true}]}
#+end_src

** License
Pooler is licensed under the Apache License Version 2.0.  See the
[[file:LICENSE][LICENSE]] file for details.

#+OPTIONS: ^:{}
gen_bunny
---------

gen_bunny is a RabbitMQ_ client library for erlang whose primary goal is to be
easy to use.  Especially for simple publisher and consumer applications.

.. image:: https://secure.travis-ci.org/dreid/gen_bunny.png?branch=master
   :target: http://travis-ci.org/dreid/gen_bunny


Getting the code
================

One of gen_bunny's goals is to make it as easy to get all the required code
build it, and start using it as possible.  To achieve this goal we've used
rebar_ for dependency management, as our build tool, and as our test runner.

To get a local copy of gen_bunny only the following steps are needed.

::

  git clone http://github.com/dreid/gen_bunny.git
  cd gen_bunny
  make
  make test

Getting Started
===============

After cloning and compiling the code as above, start two terminal sessions
(in tabs, or with screen or tmux). Start RabbitMQ in the first session:

::

  rabbitmq-server

In the second terminal, start an erlang shell:

::

  erl -pa `find . -type d -name ebin`
  %% Load Records Used With Rabbit:
  > rr("deps/rabbit_common/include/rabbit_framing.hrl").

  %% Start gen_bunny as a producer using the default exchange:
  > bunnyc:start_link(mq_producer,
                      {network, "localhost", 5672, {<<"guest">>, <<"guest">>}, <<"/">>},
                      {#'exchange.declare'{exchange = <<"">>, durable=true}},
                      [] ).

  %% Start another gen_bunny as a producer/consumer using a named queue and exchange:
  > bunnyc:start_link(mq_consumer, {network, "localhost"}, {<<"myexchange">>, <<"myqueue">>, <<"">>}, []).

  %% Publish a message to "myqueue" via the default exchange:
  > bunnyc:publish(mq_producer, <<"myqueue">>, <<"hello, world">>).

  %% Fetch the message:
  > bunnyc:get(mq_consumer, true).

  {#'basic.get_ok'{delivery_tag = 1,redelivered = false,
                   exchange = <<>>,routing_key = <<"myqueue">>,
                   message_count = 0},
   {amqp_msg,#'P_basic'{content_type = undefined,
                        content_encoding = undefined,headers = undefined,
                        delivery_mode = undefined,priority = undefined,
                        correlation_id = undefined,reply_to = undefined,
                        expiration = undefined,message_id = undefined,
                        timestamp = undefined,type = undefined,user_id = undefined,
                        app_id = undefined,cluster_id = undefined},
             <<"hello, world">>}}

  %% Publish a message to "myqueue" via the "myexchange" exchange:
  > bunnyc:publish(mq_consumer, <<"">>, <<"hello again">>).

  %% Fetch the message:
  > bunnyc:get(mq_consumer, true).

  {#'basic.get_ok'{delivery_tag = 2,redelivered = false,
                   exchange = <<"myexchange">>,routing_key = <<>>,
                   message_count = 0},
   {amqp_msg,#'P_basic'{content_type = undefined,
                        content_encoding = undefined,headers = undefined,
                        delivery_mode = undefined,priority = undefined,
                        correlation_id = undefined,reply_to = undefined,
                        expiration = undefined,message_id = undefined,
                        timestamp = undefined,type = undefined,user_id = undefined,
                        app_id = undefined,cluster_id = undefined},
             <<"hello again">>}}

  %% Shut it down:
  > bunnyc:stop(mq_consumer).
  > bunnyc:stop(mq_producer).


Using rebar
===========

Using rebar_ for dependency management means that gen_bunny can also be used as
a rebar_ dependency.  This is the preferred way to get gen_bunny into your
application, and in fact at this time the only supported way.

To depend on gen_bunny in your application simply add the following line to
your project's ``rebar.config`` file.

::

  {deps, [{gen_bunny, ".*",
           {git, "http://github.com/dreid/gen_bunny.git", ""}}]}.



After that simply using ``rebar get-deps compile`` will fetch the necessary
amqp_client and rabbit_common dependencies and build them along with gen_bunny.

.. _RabbitMQ: http://rabbitmq.com/
.. _rebar: http://hg.basho.com/rebar/wiki/Home
### bear : a set of statistics functions for erlang

Currently bear is focused on use inside the Folsom Erlang metrics library but all of these functions are generic and useful in other situations.

Pull requests accepted!

#### Available under the Apache 2.0 License
`foo.erl`:

    -module(foo).

    -export([doit/0, doit/1, doit/2]).

    doit() ->
        doit.

    doit(A) ->
        [doit, A].

    doit(A, B) ->
        [doit, A, B].

Module `bar.erl` which 'mixes in' `foo`:

    -module(bar).
    -include_lib("mixer/include/mixer.hrl").
    -mixin([foo]).

or only specific functions from `foo`:

    -module(bar).
    -include_lib("mixer/include/mixer.hrl").
    -mixin([{foo, [doit/0, doit/2]}]).

Another version of `bar.erl` which mixes in all functions from `foo` and select functions from `baz`:

    -module(bar).
    -include_lib("mixer/include/mixer.hrl").
    -mixin([foo, {baz, [doit/0, doit/1]}]).

One more version of `bar.erl` which mixes in `foo:doit/0` and renames it to `do_it_now/0`:

    -module(bar).
    -include_lib("mixer/include/mixer.hrl").
    -mixin([{foo, doit/0, do_it_now}]).

The original motivation for this parse transform was to permit reuse of functions implementing common
logic for tasks such as signature verification and authorization across multiple webmachine resources.These fixtures represent a set from an omnibus build which looks pretty
different than the original rebar fixtures. The set of dependencies are reduced to these 4 specific things:

* bifrost => The project itself
* data_collector => An app inside the project
* edown => No license info
* eper => With license info
* mochiweb => Comes as a pkg
MochiWeb is an Erlang library for building lightweight HTTP servers.

The latest version of MochiWeb is available at http://github.com/mochi/mochiweb

The mailing list for MochiWeb is at http://groups.google.com/group/mochiweb/

R12B compatibility:
The master of MochiWeb is tested with R14A and later. A branch compatible
with R12B is maintained separately at http://github.com/lemenkov/mochiweb
The R12B branch of that repository is mirrored in the official repository
occasionally for convenience.

To create a new mochiweb using project:
   make app PROJECT=project_name

To create a new mochiweb using project in a specific directory:
   make app PROJECT=project_name PREFIX=$HOME/projects/


# Edown - Markdown generated from Edoc #

Copyright (c) 2010 Erlang Solutions Ltd


__Authors:__ [`ulf.wiger@feuerlabs.com`](mailto:ulf.wiger@feuerlabs.com).


Status:
------
More-or-less readable Markdown can be generated.
A doclet needs to be written that also creates 
a markdown-based index and overview. Currently, the 
edoc_doclet creates an index.html and overview.html,
which do not point to the .md files.

To generate markdown edoc, run:

```

edoc:application(App, [{doclet, edown_doclet} | OtherOpts]).

```

The `edown_xmerl` module is used as an xmerl export module.
It converts xmerl's "simple xml" to Markdown syntax. Note that
GH-flavored Markdown allows HTML markup (at least common tags),
but doesn't expand markdown markup inside HTML markup, so the`edown_xmerl` module has to know the context in which it operates.

** Special edown option: **

Using the option `{top_level_readme, {File, BaseHref}}`, a github-friendly
`README.md` in the top directory can be generated from the `overview.edoc`.
This file is the same as the `doc/README.md` file already generated,
but with relative links corrected (using `BaseHref`) so that they actually
work. This step is needed since Github doesn't support relative paths in
Markdown links.

Example:

`{top_level_readme, {"./README.md", "http://github.com/esl/edown"}}`

The conversion function will fetch the current branch name from git,
and fail if it cannot do so.

Rebar customizations
====================
A set of escripts can be found under
[edown/priv/scripts/](http://github.com/esl/edown/blob/master/priv/scripts/), which
can be used to customize the `rebar` built process. The
[rebar.config.script](http://github.com/esl/edown/blob/master/priv/scripts/rebar.config.script)
file should be copied into your application, next to `rebar.config`.
It will sense if `doc` is a current target, and will then include
`edown` in the `deps`; otherwise, it removes it. This way, you will
not have to pull down `edown` unless you really want to build the
docs. It will also locate edown along your path, in which case
it doesn't need to pull it down again.

The script will also start the `inets` application, so that you
can include URLs as part of a `doc_path` option (see below).

Links to other EDown-generated docs
===================================
There is a way to configure Edoc/Edown to get URLs right even
when linking to other Edown-generated docs on Github.

First, you need to specify paths to the `edoc-info` files for
each repository as part of `edoc_opts` in your rebar.config, e.g.

```
   {doc_path, ["http://raw.github.com/uwiger/setup/master/doc",
               "http://raw.github.com/uwiger/gproc/master/doc"]}
```

Note (1) that we use "http:://...", not "https://...", since
Edoc doesn't recognize the latter. Also note that we use URLs
to the raw files. This is for Edoc as it fetches the `edoc-info`
files. Edown will detect and rewrite such links in the generated
output, since "raw" links wouldn't work for the markdown files.

The next issue is that Edoc uses httpd_client to fetch the
`edoc-info` files, which requires `inets` to be started. To
further complicate matters, `ssl` (and thus `crypto` and
`public_key`) must also be started, since Github will
redirect to https.

One way to solve this is to use the escripts found under
`edown/priv/scripts`.

NOTE
====
EDoc provides a plugin structure, so that one may specify own 
layout modules, export modules, and doclets. However, there is 
some overlap esp. between the layout and doclet modules, and 
several functions are expected to produce files on their own.
This causes a problem for EDown, since it cannot handle frames.
Instead, it would probably like to create one overview file with
different sections. It would have been better to have a framework
where some plugin functions identify the different files to be 
written, and the outline of each, other plugins convert to suitable
content representation (e.g. HTML or Markdown), and EDoc then 
writes the files necessary.

For now, EDown focuses on producing reasonable Markdown, rather
than complying fully with the plugin framework. That is, the 
edown_doclet module will not go out of its way to function together
with any other layout module than edown_layout, and vice versa.

markedoc
========

The sed script bin/markedoc works in the opposite direction and converts 
your `README.md` to an `EDoc` file. 

See [bin/MARKEDOC-README.md](http://github.com/esl/edown/blob/master/bin/MARKEDOC-README.md).

**FreeBSD, Mac OS X**`$ sed -E -f markedoc.sed <markdown file> > <edoc file>`

**Linux**`$ sed -r -f markedoc.sed <markdown file> > <edoc file>`


## Modules ##


<table width="100%" border="0" summary="list of modules">
<tr><td><a href="http://github.com/esl/edown/blob/master/doc/edown_doclet.md" class="module">edown_doclet</a></td></tr>
<tr><td><a href="http://github.com/esl/edown/blob/master/doc/edown_layout.md" class="module">edown_layout</a></td></tr>
<tr><td><a href="http://github.com/esl/edown/blob/master/doc/edown_lib.md" class="module">edown_lib</a></td></tr>
<tr><td><a href="http://github.com/esl/edown/blob/master/doc/edown_make.md" class="module">edown_make</a></td></tr>
<tr><td><a href="http://github.com/esl/edown/blob/master/doc/edown_xmerl.md" class="module">edown_xmerl</a></td></tr></table>

[![Build Status](https://travis-ci.org/massemanet/eper.svg?branch=master)](https://travis-ci.org/massemanet/eper)

eper is a loose collection of Erlang Performance related tools.

* dtop   - similar to unix top
* ntop   - visualizes network traffic
* atop   - shows various aspects of the VM allocators
* redbug - similar to the OTP dbg application, but safer, better etc.# Mixlib::Versioning

[![Build Status](https://travis-ci.org/chef/mixlib-versioning.png?branch=master)](https://travis-ci.org/chef/mixlib-versioning)
[![Code Climate](https://codeclimate.com/github/chef/mixlib-versioning.png)](https://codeclimate.com/github/chef/mixlib-versioning)

This project is managed by the CHEF Release Engineering team. For more information on the Release Engineering team's contribution, triage, and release process, please consult the [CHEF Release Engineering OSS Management Guide](https://docs.google.com/a/chef.io/document/d/1oJB0vZb_3bl7_ZU2YMDBkMFdL-EWplW1BJv_FXTUOzg/edit).

Versioning is hard! `mixlib-versioning` is a general Ruby library that allows
you to parse, compare and manipulate version numbers in multiple formats.
Currently the following version string formats are supported:

### SemVer 2.0.0

**Specification:**

http://semver.org/

**Supported Formats:**

```text
MAJOR.MINOR.PATCH
MAJOR.MINOR.PATCH-PRERELEASE
MAJOR.MINOR.PATCH-PRERELEASE+BUILD
```

Not much to say here except: *YUNO USE SEMVER!* The specification is focused and
brief, do yourself a favor and go read it.

### Opscode SemVer

**Supported Formats:**

```text
MAJOR.MINOR.PATCH
MAJOR.MINOR.PATCH-alpha.INDEX
MAJOR.MINOR.PATCH-beta.INDEX
MAJOR.MINOR.PATCH-rc.INDEX
MAJOR.MINOR.PATCH-alpha.INDEX+YYYYMMDDHHMMSS
MAJOR.MINOR.PATCH-beta.INDEX+YYYYMMDDHHMMSS
MAJOR.MINOR.PATCH-rc.INDEX+YYYYMMDDHHMMSS
MAJOR.MINOR.PATCH-alpha.INDEX+YYYYMMDDHHMMSS.git.COMMITS_SINCE.SHA1
MAJOR.MINOR.PATCH-beta.INDEX+YYYYMMDDHHMMSS.git.COMMITS_SINCE.SHA1
MAJOR.MINOR.PATCH-rc.INDEX+YYYYMMDDHHMMSS.git.COMMITS_SINCE.SHA1
```

All the fun of regular SemVer with some extra limits around what constitutes a
valid pre-release or build version string.

Valid prerelease version strings use the format: `PRERELEASE_STAGE.INDEX`.
Valid prerelease stages include: `alpha`, `beta` and `rc`.

All of the following are acceptable Opscode SemVer pre-release versions:

```text
11.0.8-alpha.0
11.0.8-alpha.1
11.0.8-beta.7
11.0.8-beta.8
11.0.8-rc.1
11.0.8-rc.2
```

Build version strings are limited to timestamps (`YYYYMMDDHHMMSS`), git
describe strings (`git.COMMITS_SINCE.SHA1`) or a combination of the two
(`YYYYMMDDHHMMSS.git.COMMITS_SINCE.SHA1`).

All of the following are acceptable Opscode build versions:

```text
11.0.8+20130308110833
11.0.8+git.2.g94a1dde
11.0.8+20130308110833.git.2.94a1dde
```

And as is true with regular SemVer you can mix pre-release and build versions:

```text
11.0.8-rc.1+20130308110833
11.0.8-alpha.2+20130308110833.git.2.94a1dde
```

### Rubygems

**specification:**

http://docs.rubygems.org/read/chapter/7

http://guides.rubygems.org/patterns/

**Supported Formats:**

```text
MAJOR.MINOR.PATCH
MAJOR.MINOR.PATCH.PRERELEASE
```

Rubygems is *almost* SemVer compliant but it separates the main version from
the pre-release version using a "dot". It also does not have the notion of a
build version like SemVer.

Examples of valid Rubygems version strings:

```text
10.1.1
10.1.1
10.1.1.alpha.1
10.1.1.beta.1
10.1.1.rc.0
```

### Git Describe

**Specification:**

http://git-scm.com/docs/git-describe

**Supported Formats:**

```text
MAJOR.MINOR.PATCH-COMMITS_SINCE-gGIT_SHA1
MAJOR.MINOR.PATCH-COMMITS_SINCE-gGIT_SHA1-ITERATION
MAJOR.MINOR.PATCH-PRERELEASE-COMMITS_SINCE-gGIT_SHA1
MAJOR.MINOR.PATCH-PRERELEASE-COMMITS_SINCE-gGIT_SHA1-ITERATION
```

Examples of valid Git Describe version strings:

```text
10.16.2-49-g21353f0-1
10.16.2.rc.1-49-g21353f0-1
11.0.0-alpha-10-g642ffed
11.0.0-alpha.1-1-gcea071e
```

## Installation

Add this line to your application's Gemfile:

    gem 'mixlib-versioning'

And then execute:

    $ bundle

Or install it yourself as:

    $ gem install mixlib-semver

## Usage

### Basic Version String Parsing

```irb
>> require 'mixlib/versioning'
true
>> v1 = Mixlib::Versioning.parse("11.0.3")
#<Mixlib::Versioning::Format::OpscodeSemVer:0x3fecddccff4c @major=11, @minor=0, @patch=3, @prerelease=nil, @build=nil, @input="11.0.3">
>> v1.release?
true
>> v1.prerelease?
false
>> v1.build?
false
>> v1.prerelease_build?
false
>> v2 = Mixlib::Versioning.parse("11.0.0-beta.1")
#<Mixlib::Versioning::Format::OpscodeSemVer:0x3fecde44f420 @major=11, @minor=0, @patch=0, @prerelease="beta.1", @build=nil, @input="11.0.0-beta.1">
>> v2.release?
false
>> v2.prerelease?
true
>> v2.build?
false
>> v2.prerelease_build?
false
>> v3 = Mixlib::Versioning.parse("11.0.6+20130216075209")
#<Mixlib::Versioning::Format::OpscodeSemVer:0x3fecde49568c @major=11, @minor=0, @patch=6, @prerelease=nil, @build="20130216075209", @input="11.0.6+20130216075209">
>> v3.release?
false
>> v3.prerelease?
false
>> v3.build?
true
>> v3.prerelease_build?
false
>> v4 = Mixlib::Versioning.parse("11.0.8-rc.1+20130302083119")
#<Mixlib::Versioning::Format::OpscodeSemVer:0x3fecde4dad7c @major=11, @minor=0, @patch=8, @prerelease="rc.1", @build="20130302083119", @input="11.0.8-rc.1+20130302083119">
>> v4.release?
false
>> v4.prerelease?
false
>> v4.build?
true
>> v4.prerelease_build?
true
>> v5 = Mixlib::Versioning.parse("10.16.8.alpha.0")
#<Mixlib::Versioning::Format::Rubygems:0x3fecde532bd0 @major=10, @minor=16, @patch=8, @prerelease="alpha.0", @iteration=0, @input="10.16.8.alpha.0">
>> v5.major
10
>> v5.minor
16
>> v5.patch
8
>> v5.prerelease
"alpha.0"
>> v5.release?
false
>> v5.prerelease?
true
```

### Version Comparison and Sorting

```irb
>> require 'mixlib/versioning'
true
>> v1 = Mixlib::Versioning.parse("11.0.0-beta.1")
#<Mixlib::Versioning::Format::OpscodeSemVer:0x3ff009cd54e0 @major=11, @minor=0, @patch=0, @prerelease="beta.1", @build=nil, @input="11.0.0-beta.1">
>> v2 = Mixlib::Versioning.parse("11.0.0-rc.1")
#<Mixlib::Versioning::Format::OpscodeSemVer:0x3ff009d07260 @major=11, @minor=0, @patch=0, @prerelease="rc.1", @build=nil, @input="11.0.0-rc.1">
>> v3 = Mixlib::Versioning.parse("11.0.0")
#<Mixlib::Versioning::Format::OpscodeSemVer:0x3ff009d0d3cc @major=11, @minor=0, @patch=0, @prerelease=nil, @build=nil, @input="11.0.0">
>> v1 < v2
true
>> v3 < v1
false
>> v1 == v2
false
>> [v3, v1, v2].sort
[
  [0] #<Mixlib::Versioning::Format::OpscodeSemVer:0x3ff009cd54e0 @major=11, @minor=0, @patch=0, @prerelease="beta.1", @build=nil, @input="11.0.0-beta.1">,
  [1] #<Mixlib::Versioning::Format::OpscodeSemVer:0x3ff009d07260 @major=11, @minor=0, @patch=0, @prerelease="rc.1", @build=nil, @input="11.0.0-rc.1">,
  [2] #<Mixlib::Versioning::Format::OpscodeSemVer:0x3ff009d0d3cc @major=11, @minor=0, @patch=0, @prerelease=nil, @build=nil, @input="11.0.0">
]
>> [v3, v1, v2].map { |v| v.to_s}.sort
[
  [0] "11.0.0",
  [1] "11.0.0-beta.1",
  [2] "11.0.0-rc.1"
]
```

### Target Version Selection

Basic usage:

```ruby
>> require 'mixlib/versioning'
true
>> all_versions = %w{
  11.0.0-alpha.1
  11.0.0-alpha.1-1-gcea071e
  11.0.0-alpha.3+20130103213604.git.11.3fe70b5
  11.0.0-alpha.3+20130129075201.git.38.3332a80
  11.0.0-alpha.3+20130130075202.git.38.3332a80
  11.0.0-beta.0+20130131044557
  11.0.0-beta.1+20130201023059.git.5.c9d3320
  11.0.0-beta.2+20130201035911
  11.0.0-beta.2+20130201191308.git.4.9aa4cb2
  11.0.0-rc.1
  11.0.0+20130204053034.git.1.1802643
  11.0.4
  11.0.6-alpha.0+20130208045134.git.2.298c401
  11.0.6-alpha.0+20130214075209.git.11.5d72e1c
  11.0.6-alpha.0+20130215075208.git.11.5d72e1c
  11.0.6-rc.0
  11.0.6
  11.0.6+20130216075209
  11.0.6+20130221075213
  11.0.8-rc.1
  11.0.8-rc.1+20130302083119
  11.0.8-rc.1+20130304083118
  11.0.8-rc.1+20130305083118
  11.0.8-rc.1+20130305195925.git.2.94a1dde
  11.0.8-rc.1+20130306083036.git.2.94a1dde
  11.0.8-rc.1+20130319083111.git.6.dc8613e
};''
""
>> Mixlib::Versioning.find_target_version(all_versions, "11.0.6", false, false)
#<Mixlib::Versioning::Format::OpscodeSemVer:0x3ffdc91364a4 @major=11, @minor=0, @patch=6, @prerelease=nil, @build=nil, @input="11.0.6">
>> target = Mixlib::Versioning.find_target_version(all_versions, "11.0.6", false, false)
#<Mixlib::Versioning::Format::OpscodeSemVer:0x3ffdc91364a4 @major=11, @minor=0, @patch=6, @prerelease=nil, @build=nil, @input="11.0.6">
>> target.to_s
"11.0.6"
```

Select latest release version:

```irb
>> target = Mixlib::Versioning.find_target_version(all_versions, nil, false, false)
#<Mixlib::Versioning::Format::OpscodeSemVer:0x3ffdc91364a4 @major=11, @minor=0, @patch=6, @prerelease=nil, @build=nil, @input="11.0.6">
>> target.to_s
"11.0.6"
```

Select latest pre-release version:

```irb
>> target = Mixlib::Versioning.find_target_version(all_versions, nil, true, false)
#<Mixlib::Versioning::Format::OpscodeSemVer:0x3ffdc9139078 @major=11, @minor=0, @patch=8, @prerelease="rc.1", @build=nil, @input="11.0.8-rc.1">
>> target.to_s
"11.0.8-rc.1"
```

Select the latest release build version:

```irb
>> target = Mixlib::Versioning.find_target_version(all_versions, nil, false, true)
#<Mixlib::Versioning::Format::OpscodeSemVer:0x3ffdc91f0bb0 @major=11, @minor=0, @patch=6, @prerelease=nil, @build="20130221075213", @input="11.0.6+20130221075213">
>> target.to_s
"11.0.6+20130221075213"
```

Select the latest pre-release build version:

```irb
>> target = Mixlib::Versioning.find_target_version(all_versions, nil, true, true)
#<Mixlib::Versioning::Format::OpscodeSemVer:0x3ffdc91f154c @major=11, @minor=0, @patch=8, @prerelease="rc.1", @build="20130319083111.git.6.dc8613e", @input="11.0.8-rc.1+20130319083111.git.6.dc8613e">
>> target.to_s
"11.0.8-rc.1+20130319083111.git.6.dc8613e"
```

## How to Run the Tests

To run the unit tests, run

```
rake spec
```

## Documentation

All documentation is written using YARD. You can generate a by running:

```
rake yard
```

## License

|                      |                                          |
|:---------------------|:-----------------------------------------|
| **Author:**          | Seth Chisamore (schisamo@chef.io)
| **Author:**          | Christopher Maier (cm@chef.io)
| **Copyright:**       | Copyright (c) 2013 Opscode, Inc.
| **License:**         | Apache License, Version 2.0

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
= Net::SCP

<em><b>Please note: this project is in maintenance mode. It is not under active development but pull requests are very much welcome. Just be sure to include tests! -- delano</b></em>


* Docs: http://net-ssh.github.com/net-scp
* Issues: https://github.com/net-ssh/net-scp/issues
* Codes: https://github.com/net-ssh/net-scp
* Email: net-ssh@solutious.com

<em>As of v1.0.5, all gem releases are signed. See INSTALL.</em>


== DESCRIPTION:

Net::SCP is a pure-Ruby implementation of the SCP protocol. This operates over SSH (and requires the Net::SSH library), and allows files and directory trees to copied to and from a remote server.

== FEATURES/PROBLEMS:

* Transfer files or entire directory trees to or from a remote host via SCP
* Can preserve file attributes across transfers
* Can download files in-memory, or direct-to-disk
* Support for SCP URI's, and OpenURI

== SYNOPSIS:

In a nutshell:

  require 'net/scp'

  # upload a file to a remote server
  Net::SCP.upload!("remote.host.com", "username",
    "/local/path", "/remote/path",
    :ssh => { :password => "password" })

  # download a file from a remote server
  Net::SCP.download!("remote.host.com", "username",
    "/remote/path", "/local/path",
    :ssh => { :password => "password" })

  # download a file to an in-memory buffer
  data = Net::SCP::download!("remote.host.com", "username", "/remote/path")

  # use a persistent connection to transfer files
  Net::SCP.start("remote.host.com", "username", :ssh => { :password => "password" }) do |scp|
    # upload a file to a remote server
    scp.upload! "/local/path", "/remote/path"

    # upload from an in-memory buffer
    scp.upload! StringIO.new("some data to upload"), "/remote/path"

    # run multiple downloads in parallel
    d1 = scp.download("/remote/path", "/local/path")
    d2 = scp.download("/remote/path2", "/local/path2")
    [d1, d2].each { |d| d.wait }
  end

  # You can also use open-uri to grab data via scp:
  require 'uri/open-scp'
  data = open("scp://user@host/path/to/file.txt").read

For more information, see Net::SCP.

== REQUIREMENTS:

* Net::SSH 2

If you wish to run the tests, you'll also need:

* Echoe (for Rakefile use)
* Mocha (for tests)

== INSTALL:

* gem install net-scp (might need sudo privileges)

However, in order to be sure the code you're installing hasn't been tampered with, it's recommended that you verify the signiture[http://docs.rubygems.org/read/chapter/21]. To do this, you need to add my public key as a trusted certificate (you only need to do this once):

    # Add the public key as a trusted certificate
    # (You only need to do this once)
    $ curl -O https://raw.github.com/net-ssh/net-ssh/master/gem-public_cert.pem
    $ gem cert --add gem-public_cert.pem

Then, when install the gem, do so with high security:

    $ gem install net-scp -P HighSecurity

If you don't add the public key, you'll see an error like "Couldn't verify data signature". If you're still having trouble let me know and I'll give you a hand.


Or, you can do it the hard way (without Rubygems):

* tar xzf net-scp-*.tgz
* cd net-scp-*
* ruby setup.rb config
* ruby setup.rb install (might need sudo privileges)

== LICENSE:

(The MIT License)

Copyright (c) 2008 Jamis Buck <jamis@37signals.com>

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
Thor
====

[![Gem Version](http://img.shields.io/gem/v/thor.svg)][gem]
[![Build Status](http://img.shields.io/travis/erikhuda/thor.svg)][travis]
[![Dependency Status](http://img.shields.io/gemnasium/erikhuda/thor.svg)][gemnasium]
[![Code Climate](http://img.shields.io/codeclimate/github/erikhuda/thor.svg)][codeclimate]
[![Coverage Status](http://img.shields.io/coveralls/erikhuda/thor.svg)][coveralls]

[gem]: https://rubygems.org/gems/thor
[travis]: http://travis-ci.org/erikhuda/thor
[gemnasium]: https://gemnasium.com/erikhuda/thor
[codeclimate]: https://codeclimate.com/github/erikhuda/thor
[coveralls]: https://coveralls.io/r/erikhuda/thor

Description
-----------
Thor is a simple and efficient tool for building self-documenting command line
utilities.  It removes the pain of parsing command line options, writing
"USAGE:" banners, and can also be used as an alternative to the [Rake][rake]
build tool.  The syntax is Rake-like, so it should be familiar to most Rake
users.

[rake]: https://github.com/jimweirich/rake

Installation
------------
    gem install thor

Usage and documentation
-----------------------
Please see the [wiki][] for basic usage and other documentation on using Thor. You can also checkout the [official homepage][homepage].

[wiki]: https://github.com/erikhuda/thor/wiki
[homepage]: http://whatisthor.com/

License
-------
Released under the MIT License.  See the [LICENSE][] file for further details.

[license]: LICENSE.md
= Net::SSH 3.x

<em><b>Please note: this project is in maintenance mode. It is not under active development but pull requests are very much welcome. Just be sure to include tests! -- delano</b></em>


* Docs: http://net-ssh.github.com/net-ssh
* Issues: https://github.com/net-ssh/net-ssh/issues
* Codes: https://github.com/net-ssh/net-ssh
* Email: net-ssh@solutious.com


<em>As of v2.6.4, all gem releases are signed. See INSTALL.</em>


== DESCRIPTION:

Net::SSH is a pure-Ruby implementation of the SSH2 client protocol. It allows you to write programs that invoke and interact with processes on remote servers, via SSH2.

== FEATURES:

* Execute processes on remote servers and capture their output
* Run multiple processes in parallel over a single SSH connection
* Support for SSH subsystems
* Forward local and remote ports via an SSH connection

== SYNOPSIS:

In a nutshell:

  require 'net/ssh'

  Net::SSH.start('host', 'user', :password => "password") do |ssh|
    # capture all stderr and stdout output from a remote process
    output = ssh.exec!("hostname")
    puts output

    # capture only stdout matching a particular pattern
    stdout = ""
    ssh.exec!("ls -l /home/jamis") do |channel, stream, data|
      stdout << data if stream == :stdout
    end
    puts stdout

    # run multiple processes in parallel to completion
    ssh.exec "sed ..."
    ssh.exec "awk ..."
    ssh.exec "rm -rf ..."
    ssh.loop

    # open a new channel and configure a minimal set of callbacks, then run
    # the event loop until the channel finishes (closes)
    channel = ssh.open_channel do |ch|
      ch.exec "/usr/local/bin/ruby /path/to/file.rb" do |ch, success|
        raise "could not execute command" unless success

        # "on_data" is called when the process writes something to stdout
        ch.on_data do |c, data|
          $stdout.print data
        end

        # "on_extended_data" is called when the process writes something to stderr
        ch.on_extended_data do |c, type, data|
          $stderr.print data
        end

        ch.on_close { puts "done!" }
      end
    end

    channel.wait

    # forward connections on local port 1234 to port 80 of www.capify.org
    ssh.forward.local(1234, "www.capify.org", 80)
    ssh.loop { true }
  end

See Net::SSH for more documentation, and links to further information.

== REQUIREMENTS:

The only requirement you might be missing is the OpenSSL bindings for Ruby. These are built by default on most platforms, but you can verify that they're built and installed on your system by running the following command line:

  ruby -ropenssl -e 'puts OpenSSL::OPENSSL_VERSION'

If that spits out something like "OpenSSL 0.9.8g 19 Oct 2007", then you're set. If you get an error, then you'll need to see about rebuilding ruby with OpenSSL support, or (if your platform supports it) installing the OpenSSL bindings separately.

Additionally: if you are going to be having Net::SSH prompt you for things like passwords or certificate passphrases, you'll want to have either the Highline (recommended) or Termios (unix systems only) gem installed, so that the passwords don't echo in clear text.

Lastly, if you want to run the tests or use any of the Rake tasks, you'll need:

* Echoe (for the Rakefile)
* Mocha (for the tests)


== INSTALL:

* gem install net-ssh (might need sudo privileges)

NOTE: If you are running on jruby you need to install jruby-pageant manually (gemspec doesn't allow for platform specific dependencies).

However, in order to be sure the code you're installing hasn't been tampered with, it's recommended that you verify the signature[http://docs.rubygems.org/read/chapter/21]. To do this, you need to add my public key as a trusted certificate (you only need to do this once):

    # Add the public key as a trusted certificate
    # (You only need to do this once)
    $ curl -O https://raw.githubusercontent.com/net-ssh/net-ssh/master/net-ssh-public_cert.pem
    $ gem cert --add net-ssh-public_cert.pem

Then, when install the gem, do so with high security:

    $ gem install net-ssh -P HighSecurity

If you don't add the public key, you'll see an error like "Couldn't verify data signature". If you're still having trouble let me know and I'll give you a hand.

== RUBY 1.x SUPPORT

* Ruby 1.8.x is supported up until the net-ssh 2.5.1 release.
* Ruby 1.9.x is supported up until the net-ssh 2.9.x release.
* Current net-ssh releases require Ruby 2.0 or later.

== RUNNING TESTS

Run the test suite from the net-ssh directory with the following command:

     bash -c 'unset HOME && ruby -Ilib -Itest -rrubygems test/test_all.rb'

Run a single test file like this:

     ruby -Ilib -Itest -rrubygems test/transport/test_server_version.rb

To run integration tests see test/integration/README.txt

=== BUILDING GEM

Since building the gem requires the private key if you want to build a .gem locally please use the NET_SSH_NOKEY=1 envirnoment variable:

     rake build NET_SSH_NOKEY=1

=== PORT FORWARDING TESTS

     ruby -Ilib -Itest -rrubygems test/manual/test_forward.rb

test_forward.rb must be run separately from the test suite because
it requires authorizing your public SSH keys on you localhost.

If you already have keys you can do this:

     cat ~/.ssh/id_rsa.pub >> ~/.ssh/authorized_keys

If you don't have keys see:

     http://kimmo.suominen.com/docs/ssh/#ssh-keygen

You should now be able to login to your localhost with out
bring prompted for a password:

     ssh localhost


== LICENSE:

(The MIT License)

Copyright (c) 2008 Jamis Buck

Permission is hereby granted, free of charge, to any person obtaining
a copy of this software and associated documentation files (the
'Software'), to deal in the Software without restriction, including
without limitation the rights to use, copy, modify, merge, publish,
distribute, sublicense, and/or sell copies of the Software, and to
permit persons to whom the Software is furnished to do so, subject to
the following conditions:

The above copyright notice and this permission notice shall be
included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED 'AS IS', WITHOUT WARRANTY OF ANY KIND,
EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Mixlib::Install

## Usage

### Get URL for specific platform and package version
```ruby
options = {
  channel: :current,
  product_name: 'chef',
  product_version: :latest,
  platform: 'mac_os_x',
  platform_version: '10.9',
  architecture: 'x86_64'
}

artifact = Mixlib::Install.new(options).artifact_info
# => ArtifactInfo

artifact.url
# => "http://opscode-omnibus-packages-current.s3.amazonaws.com/mac_os_x/10.9/x86_64/chef-12.5.1%2B20151009083009-1.dmg"
```

### Get list of artifacts for all platforms given a package version
```ruby
options = {
  channel: :current,
  product_name: 'chef',
  product_version: :latest
}

artifacts = Mixlib::Install.new(options).artifact_info
# => Array<ArtifactInfo>

artifacts.first.url
# => "http://opscode-omnibus-packages-current.s3.amazonaws.com/mac_os_x/10.9/x86_64/chef-12.5.1%2B20151009083009-1.dmg"
```

### Detect platform information
```ruby
options = {
  channel: :current,
  product_name: 'chef',
  product_version: :latest
}

artifact = Mixlib::Install.new(options).detect_platform

artifact.platform # => "mac_os_x"
artifact.platform_version # => "10.10"
```

### Use an artifact released for an earlier version of the platform
```ruby
options = {
  channel: :current,
  product_name: 'chef',
  product_version: :latest,
  platform: 'ubuntu',
  platform_version: '15.04',
  architecture: 'x86_64',
  platform_version_compatibility_mode: true
}

artifact = Mixlib::Install.new(options).artifact_info

artifact.platform # => "ubuntu"
artifact.platform_version # => "14.04"
```

## Unstable channel
The `:unstable` channel is currently only available when connected to Chef's internal network.

## Development
Since mixlib-install needs to interact with Bintray and Artifactory and since Artifactory instances are only available in Chef's network, this project uses [vcr](https://github.com/vcr/vcr).

VCR is a tool that helps cache and replay http responses. When these responses change or when you add more tests you might need to update cached responses. Check out [spec_helper.rb](https://github.com/chef/mixlib-install/blob/master/spec/spec_helper.rb) for instructions on how to do this.

## Contributing

1. Fork it ( https://github.com/[my-github-username]/mixlib-install/fork )
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create a new Pull Request
Artifactory Client
==================
[![Build Status](https://secure.travis-ci.org/chef/artifactory-client.png?branch=master)](http://travis-ci.org/chef/artifactory-client)

A Ruby client and interface to the Artifactory API. **The majority of API endpoints are only exposed for Artifactory Pro customers!** As such, many of the resources and actions exposed by this gem also require Artifactory Pro.

The Artifactory gem offers a convienent interface for managing various parts of the Artifactory API. It is not a complete API implementation, and should still be considered a work in progress.

This project is managed by the CHEF Release Engineering team. For more information on the Release Engineering team's contribution, triage, and release process, please consult the [CHEF Release Engineering OSS Management Guide](https://docs.google.com/a/opscode.com/document/d/1oJB0vZb_3bl7_ZU2YMDBkMFdL-EWplW1BJv_FXTUOzg/edit).


Quick start
-----------
Install via Rubygems:

    $ gem install artifactory

or add it to your Gemfile if you're using Bundler:

```ruby
gem 'artifactory', '~> 1.0'
```

In your library or project, you wil likely want to include the `Artifactory::Resource` namespace:

```ruby
include Artifactory::Resource
```

This will given you "Rails-like" access to the top-level Artifactory resources like:

```ruby
System.info
Repository.all
```

If you choose not to include the module (for namespacing reasons), you will need to specify the full module path to access resources:

```ruby
Artifactory::Resource::System.info
Artifactory::Resource::Repository.all
```

### Create a connection
Before you can make a request, you must give Artifactory your connection information.

```ruby
Artifactory.configure do |config|
  # The endpoint for the Artifactory server. If you are running the "default"
  # Artifactory installation using tomcat, don't forget to include the
  # +/artifactoy+ part of the URL.
  config.endpoint = 'https://my.storage.server/artifactory'

  # The basic authentication information. Since this uses HTTP Basic Auth, it
  # is highly recommended that you run Artifactory over SSL.
  config.username = 'admin'
  config.password = 'password'

  # Speaking of SSL, you can specify the path to a pem file with your custom
  # certificates and the gem will wire it all up for you (NOTE: it must be a
  # valid PEM file).
  config.ssl_pem_file = '/path/to/my.pem'

  # Or if you are feelying frisky, you can always disable SSL verification
  config.ssl_verify = false

  # You can specify any proxy information, including any authentication
  # information in the URL.
  config.proxy_username = 'user'
  config.proxy_password = 'password'
  config.proxy_address  = 'my.proxy.server'
  config.proxy_port     = '8080'
end
```

All of these parameters are also configurable via the top-level `Artifactory` object. For example:

```ruby
Artifactory.endpoint = '...'
```

Or, if you want to be really Unixy, these parameters are all configurable via environment variables:

```bash
# Artifactory will use these values for the defaults
export ARTIFACTORY_ENDPOINT=http://my.storage.server/artifactory
export ARTIFACTORY_USERNAME=admin
export ARTIFACTORY_PASSWORD=password
export ARTIFACTORY_SSL_PEM_FILE=/path/to/my.pem
```

You can also create a full `Client` object with hash parameters:

```ruby
client = Artifactory::Client.new(endpoint: '...', username: '...')
```

### Making requests
The Artifactory gem attempts to make the Artifactory API as object-oriented and Ruby-like as possible. All of the methods and API calls are heavily documented with examples inline using YARD. In order to keep the examples versioned with the code, the README only lists a few examples for using the Artifactory gem. Please see the inline documentation for the full API documentation. The tests in the 'spec' directory are an additional source of examples.

#### Artifacts
```ruby
# Upload an artifact to a repository whose key is 'repo_key'
artifact.upload('/local/path/to/file', 'repo_key', param_1: 'foo')

# Search for an artifact by name
artifact = Artifact.search(name: 'package.deb').first
artifact #=> "#<Artifactory::Resource::Artifact md5: 'ABCD1234'>"

# Get the properties of an artifact
artifact.md5 #=> "ABCD1234"
artifact.properties #=> { ... }

# Download the artifact to disk
artifact.download #=> /tmp/folders-a38b0decf038201/package.deb
artifact.download('~/Desktop', filename: 'software.deb') #=> /Users/you/Desktop/software.deb

# Delete the artifact from the Artifactory server
artifact.delete #=> true
```

#### Builds
```ruby
# Show all components
BuildComponent.all #=> [#<BuildComponent ...>]

# Show all builds for a components
Build.all('wicket') #=> [#<Build ...>]

# Find a build component by name
component = BuildComponent.find('wicket')

# Delete some builds for a component
component.delete(build_numbers: %w( 51 52)) #=> true

# Delete all builds for a component
component.delete(delete_all: true) #=> true

# Delete a component and all of its associated data (including artifacts)
component.delete(artifacts: true, delete_all: true) #=> true

# Get a list of all buld records for a component
component.builds #=> #=> [#<Artifactory::Resource::Build ...>, ...]

# Create a new build record
build = Build.new(name: 'fricket', number: '51', properties: {...}, modules: [...])
build.save

# Find a build
build = Build.find('wicket', '51')

# Promote a build
build.promote('libs-release-local', status: 'staged', comment: 'Tested on all target platforms.')
```

#### Plugins
```ruby
# Show all plugins
Plugin.all #=> [#<Plugin ...>]
```

#### Repository
```ruby
# Find a repository by name
repo = Repository.find(name: 'libs-release-local')
repo #=> #<Artifactory::Resource::Repository ...>

# Get information about the repository
repo.description => "The default storage mechanism for..."

# Change the repository
repo.description = "This is a new description"
repo.save

# Upload an artifact to the repo
repo.upload('/local/path/to/file', param_1: 'foo', param_2: 'bar')

# Get a list of artifacts in this repository
repo.artifacts #=> [#<Artifactory::Resource::Artifact ...>, ...]
```

#### System
```ruby
# Get the system information
System.info #=> "..."

# See if artifactory is running
System.ping #=> true

# Get the Artifactory server version and other information
System.version #=> { ... }
```

#### Raw requests
If there's a specific endpoint or path you need to hit that is not implemented by this gem, you can execute a "raw" request:

```ruby
# Using the top-level Artifactory module
Artifactory.get('/some/special/path', param_1: 'foo', param_2: 'bar')

# Using an Artifactory::Client object
client.get('/some/special/path', param_1: 'foo', param_2: 'bar')
```

For more information on the methods available, please see the [`Artifactory::Client` class](https://github.com/opscode/artifactory-client/blob/master/lib/artifactory/client.rb).

### Threadsafety
If you plan to use the Artifactory gem in a library, you should be aware that _certain_ pathways for accessing resources are **not** threadsafe. In order to deliver a "Rails-like" experience, accessing a resource without a client object uses a global shared state. Other threads may modify this state, and therefore we do **not** recommend using the Rails-like approach if you are concerned about threadsafety. The following code snippet may better explain the differences:

```ruby
# In our current thread...
Artifactory.endpoint = 'http://foo.com/artifactory'

# Meanwhile, in another thread...
Thread.new do
  Artifactory.endpoint = 'http://bar.com/artifactory'
end

# You have a 50/50 chance of which endpoint is used, depending on the order in
# which the threads execute on the CPU.
Artifactory.endpoint #=> 'http://foo.com/artifactory'
Artifactory.endpoint #=> 'http://bar.com/artifactory'
```

To avoid this potential headache, the Artifactory gem offers a less Rails-like API in which the `Artifactory::Client` object becomes the pivot for all resources. First, you must create a client object (you cannot use the global namespace):

```ruby
client = Artifactory::Client.new(endpoint: 'http://foo.com/artifactory')
```

And then execute all requests using this client object, with the general pattern `resource_method`:

```ruby
# Search for artifacts
client.artifact_search(name: '...') #=> [...]

# Get all plugins
client.all_plugins #=> [...]
```

This pattern is slightly less eye-appealing, but it will ensure that your code is threadsafe.


Development
-----------
1. Clone the project on GitHub
2. Create a feature branch
3. Submit a Pull Request

Artifactory uses a built-in Sinatra server that "acts like" a real Artifactory Pro server. Since we cannot bundle a full Artifactory Pro server with the gem, we have re-implemented various pieces of their API. If you are writing a feature that accesses a new endpoint, you will likely need to add that endpoint to the vendored Sinatra app, using the [API documentation for Artifactory](http://www.jfrog.com/confluence/display/RTF/Artifactory+REST+API).

Important Notes:

- **All new features must include test coverage.** At a bare minimum, Unit tests are required. It is preferred if you include acceptance tests as well.
- **The tests must be be idempotent.** The HTTP calls made during a test should be able to be run over and over.
- **Tests are order independent.** The default RSpec configuration randomizes the test order, so this should not be a problem.


License & Authors
-----------------
- Author: Seth Vargo <sethvargo@gmail.com>

```text
Copyright 2013-2014 Chef Software, Inc.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
# Test Kitchen

[![Gem Version](https://badge.fury.io/rb/test-kitchen.svg)](http://badge.fury.io/rb/test-kitchen)
[![Build Status](https://secure.travis-ci.org/test-kitchen/test-kitchen.svg?branch=master)](https://travis-ci.org/test-kitchen/test-kitchen)
[![Code Climate](https://codeclimate.com/github/test-kitchen/test-kitchen.svg)](https://codeclimate.com/github/test-kitchen/test-kitchen)
[![Test Coverage](https://codeclimate.com/github/test-kitchen/test-kitchen/coverage.svg)](https://codeclimate.com/github/test-kitchen/test-kitchen)
[![Dependency Status](https://gemnasium.com/test-kitchen/test-kitchen.svg)](https://gemnasium.com/test-kitchen/test-kitchen)
[![Inline docs](http://inch-ci.org/github/test-kitchen/test-kitchen.svg?branch=master)](http://inch-ci.org/github/test-kitchen/test-kitchen)

|             |                                               |
|-------------|-----------------------------------------------|
| Website     | http://kitchen.ci                             |
| Source Code | http://kitchen.ci/docs/getting-started/       |
| IRC         | [#kitchenci][irc] channel on Freenode, [transcript][irc_log] thanks to [BotBot.me][botbotme] |
| Twitter     | [@kitchenci][twitter]                         |

> **Test Kitchen is an integration tool for developing and testing
> infrastructure code and software on isolated target platforms.**

## Getting Started Guide

To learn how to install and setup Test Kitchen for developing infrastructure
code, check out the [Getting Started Guide][guide].

If you want to get going super fast, then try the Quick Start next...

## Quick Start

Test Kitchen is a RubyGem and can be installed with:

```
$ gem install test-kitchen
```

If you use Bundler, you can add `gem "test-kitchen"` to your Gemfile and make
sure to run `bundle install`.

Next add support to your library, Chef cookbook, or empty project with `kitchen
init`:

```
$ kitchen init
```

A `.kitchen.yml` will be created in your project base directory. This file
describes your testing configuration; what you want to test and on which target
platforms. Each of these suite and platform combinations are called instances.
By default your instances will be converged with Chef Solo and run in Vagrant
virtual machines.

Get a listing of your instances with:

```
$ kitchen list
```

Run Chef on an instance, in this case `default-ubuntu-1204`, with:

```
$ kitchen converge default-ubuntu-1204
```

Destroy all instances with:

```
$ kitchen destroy
```

You can clone a Chef cookbook project that contains Test Kitchen support and
run through all the instances in serial by running:

```
$ kitchen test
```

## Usage

There is help included with the `kitchen help` subcommand which will list all
subcommands and their usage:

```
$ kitchen help test
```

More verbose logging for test-kitchen can be specified when running test-kitchen from the command line using:

```
$ kitchen test -l debug
```

For the provisioner (e.g. chef-solo or chef-zero) add a `log_level` item to the provisioner section of the `.kitchen.yml`
For more information see the Documentation.  This is a change since version 1.7.0

## Documentation

Documentation is being added on the Test Kitchen [website][website]. Please
read and contribute to improve them!

## Versioning

Test Kitchen aims to adhere to [Semantic Versioning 2.0.0][semver].

## Community and Ecosystem

If you would like to see a few of the plugins or ecosystem helpers, please look at [ECOSYSTEM.md][ecosystem].

## Development

* Source hosted at [GitHub][repo]
* Report issues/questions/feature requests on [GitHub Issues][issues]

Pull requests are very welcome! Make sure your patches are well tested.
Ideally create a topic branch for every separate change you make. For
example:

1. Fork the repo
2. Create your feature branch (`git checkout -b my-new-feature`)
3. Commit your changes (`git commit -am 'Added some feature'`)
4. Push to the branch (`git push origin my-new-feature`)
5. Create new Pull Request

## Authors

Created and maintained by [Fletcher Nichol][fnichol] (<fnichol@nichol.ca>) and
a growing community of [contributors][contributors].

## License

Apache License, Version 2.0 (see [LICENSE][license])

[botbotme]: https://botbot.me/
[contributors]: https://github.com/test-kitchen/test-kitchen/graphs/contributors
[fnichol]: https://github.com/fnichol
[guide]: http://kitchen.ci/docs/getting-started/
[irc]: http://webchat.freenode.net/?channels=kitchenci
[irc_log]: https://botbot.me/freenode/kitchenci/
[issues]: https://github.com/test-kitchen/test-kitchen/issues
[license]: https://github.com/test-kitchen/test-kitchen/blob/master/LICENSE
[repo]: https://github.com/test-kitchen/test-kitchen
[semver]: http://semver.org/
[twitter]: https://twitter.com/kitchenci
[website]: http://kitchen.ci
[ecosystem]: https://github.com/test-kitchen/test-kitchen/blob/master/ECOSYSTEM.md
SafeYAML
========

[![Build Status](https://travis-ci.org/dtao/safe_yaml.png)](http://travis-ci.org/dtao/safe_yaml)
[![Gem Version](https://badge.fury.io/rb/safe_yaml.png)](http://badge.fury.io/rb/safe_yaml)

The **SafeYAML** gem provides an alternative implementation of `YAML.load` suitable for accepting user input in Ruby applications. Unlike Ruby's built-in implementation of `YAML.load`, SafeYAML's version will not expose apps to arbitrary code execution exploits (such as [the ones discovered](http://www.reddit.com/r/netsec/comments/167c11/serious_vulnerability_in_ruby_on_rails_allowing/) [in Rails in early 2013](http://www.h-online.com/open/news/item/Rails-developers-close-another-extremely-critical-flaw-1793511.html)).

**If you encounter any issues with SafeYAML, check out the 'Common Issues' section below.** If you don't see anything that addresses the problem you're experiencing, by all means, [create an issue](https://github.com/dtao/safe_yaml/issues/new)!

Installation
------------

Add this line to your application's Gemfile:

```ruby
gem "safe_yaml"
```

Configuration
-------------

If *all you do* is add SafeYAML to your project, then `YAML.load` will operate in "safe" mode, which means it won't deserialize arbitrary objects. However, it will issue a warning the first time you call it because you haven't explicitly specified whether you want safe or unsafe behavior by default. To specify this behavior (e.g., in a Rails initializer):

```ruby
SafeYAML::OPTIONS[:default_mode] = :safe # or :unsafe
```

Another important option you might want to specify on startup is whether or not to allow *symbols* to be deserialized. The default setting is `false`, since symbols are not garbage collected in Ruby and so deserializing them from YAML may render your application vulnerable to a DOS (denial of service) attack. To allow symbol deserialization by default:

```ruby
SafeYAML::OPTIONS[:deserialize_symbols] = true
```

For more information on these and other options, see the "Usage" section down below.

What is this gem for, exactly?
------------------------------

Suppose your application were to use a popular open source library which contained code like this:

```ruby
class ClassBuilder
  def []=(key, value)
    @class ||= Class.new

    @class.class_eval <<-EOS
      def #{key}
        #{value}
      end
    EOS
  end

  def create
    @class.new
  end
end
```

Now, if you were to use `YAML.load` on user input anywhere in your application without the SafeYAML gem installed, an attacker who suspected you were using this library could send a request with a carefully-crafted YAML string to execute arbitrary code (yes, including `system("unix command")`) on your servers.

This simple example demonstrates the vulnerability:

```ruby
yaml = <<-EOYAML
--- !ruby/hash:ClassBuilder
"foo; end; puts %(I'm in yr system!); def bar": "baz"
EOYAML
```

    > YAML.load(yaml)
    I'm in yr system!
    => #<ClassBuilder:0x007fdbbe2e25d8 @class=#<Class:0x007fdbbe2e2510>>

With SafeYAML, the same attacker would be thwarted:

    > require "safe_yaml"
    => true
    > YAML.load(yaml, :safe => true)
    => {"foo; end; puts %(I'm in yr system!); def bar"=>"baz"}

Usage
-----

When you require the safe_yaml gem in your project, `YAML.load` is patched to accept one additional (optional) `options` parameter. This changes the method signature as follows:

- for Syck and Psych prior to Ruby 1.9.3: `YAML.load(yaml, options={})`
- for Psych in 1.9.3 and later: `YAML.load(yaml, filename=nil, options={})`

The most important option is the `:safe` option (default: `true`), which controls whether or not to deserialize arbitrary objects when parsing a YAML document. The other options, along with explanations, are as follows.

- `:deserialize_symbols` (default: `false`): Controls whether or not YAML will deserialize symbols. It is probably best to only enable this option where necessary, e.g. to make trusted libraries work. Symbols receive special treatment in Ruby and are not garbage collected, which means deserializing them indiscriminately may render your site vulnerable to a DOS attack.

- `:whitelisted_tags`: Accepts an array of YAML tags that designate trusted types, e.g., ones that can be deserialized without worrying about any resulting security vulnerabilities. When any of the given tags are encountered in a YAML document, the associated data will be parsed by the underlying YAML engine (Syck or Psych) for the version of Ruby you are using. See the "Whitelisting Trusted Types" section below for more information.

- `:custom_initializers`: Similar to the `:whitelisted_tags` option, but allows you to provide your own initializers for specified tags rather than using Syck or Psyck. Accepts a hash with string tags for keys and lambdas for values.

- `:raise_on_unknown_tag` (default: `false`): Represents the highest possible level of paranoia. If the YAML engine encounters any tag other than ones that are automatically trusted by SafeYAML or that you've explicitly whitelisted, it will raise an exception. This may be a good choice if you expect to always be dealing with perfectly safe YAML and want your application to fail loudly upon encountering questionable data.

All of the above options can be set at the global level via `SafeYAML::OPTIONS`. You can also set each one individually per call to `YAML.load`; an option explicitly passed to `load` will take precedence over an option specified globally.

What if I don't *want* to patch `YAML`?
---------------------------------------

[Excellent question](https://github.com/dtao/safe_yaml/issues/47)! You can also get the methods `SafeYAML.load` and `SafeYAML.load_file` without touching the `YAML` module at all like this:

```ruby
require "safe_yaml/load" # instead of require "safe_yaml"
```

This way, you can use `SafeYAML.load` to parse YAML that *you* don't trust, without affecting the rest of an application (if you're developing a library, for example).

Supported Types
---------------

The way that SafeYAML works is by restricting the kinds of objects that can be deserialized via `YAML.load`. More specifically, only the following types of objects can be deserialized by default:

- Hashes
- Arrays
- Strings
- Numbers
- Dates
- Times
- Booleans
- Nils

Again, deserialization of symbols can be enabled globally by setting `SafeYAML::OPTIONS[:deserialize_symbols] = true`, or in a specific call to `YAML.load([some yaml], :deserialize_symbols => true)`.

Whitelisting Trusted Types
--------------------------

SafeYAML supports whitelisting certain YAML tags for trusted types. This is handy when your application uses YAML to serialize and deserialize certain types not listed above, which you know to be free of any deserialization-related vulnerabilities.

The easiest way to whitelist types is by calling `SafeYAML.whitelist!`, which can accept a variable number of safe types, e.g.:

```ruby
SafeYAML.whitelist!(Foo, Bar)
```

You can also whitelist YAML *tags* via the `:whitelisted_tags` option:

```ruby
# Using Syck
SafeYAML::OPTIONS[:whitelisted_tags] = ["tag:ruby.yaml.org,2002:object:OpenStruct"]

# Using Psych
SafeYAML::OPTIONS[:whitelisted_tags] = ["!ruby/object:OpenStruct"]
```

And in case you were wondering: no, this feature will *not* allow would-be attackers to embed untrusted types within trusted types:

```ruby
yaml = <<-EOYAML
--- !ruby/object:OpenStruct 
table: 
  :backdoor: !ruby/hash:ClassBuilder 
    "foo; end; puts %(I'm in yr system!); def bar": "baz"
EOYAML
```

    > YAML.safe_load(yaml)
    => #<OpenStruct :backdoor={"foo; end; puts %(I'm in yr system!); def bar"=>"baz"}>

Known Issues
------------

If you add SafeYAML to your project and start seeing any errors about missing keys, or you notice mysterious strings that look like `":foo"` (i.e., start with a colon), it's likely you're seeing errors from symbols being saved in YAML format. If you are able to modify the offending code, you might want to consider changing your YAML content to use plain vanilla strings instead of symbols. If not, you may need to set the `:deserialize_symbols` option to `true`, either in calls to `YAML.load` or---as a last resort---globally, with `SafeYAML::OPTIONS[:deserialize_symbols]`.

Also be aware that some Ruby libraries, particularly those requiring inter-process communication, leverage YAML's object deserialization functionality and therefore may break or otherwise be impacted by SafeYAML. The following list includes known instances of SafeYAML's interaction with other Ruby gems:

- [**ActiveRecord**](https://github.com/rails/rails/tree/master/activerecord): uses YAML to control serialization of model objects using the `serialize` class method. If you find that accessing serialized properties on your ActiveRecord models is causing errors, chances are you may need to:
  1. set the `:deserialize_symbols` option to `true`,
  2. whitelist some of the types in your serialized data via `SafeYAML.whitelist!` or the `:whitelisted_tags` option, or
  3. both
- [**delayed_job**](https://github.com/collectiveidea/delayed_job): Uses YAML to serialize the objects on which delayed methods are invoked (with `delay`). The safest solution in this case is to use `SafeYAML.whitelist!` to whitelist the types you need to serialize.
- [**Guard**](https://github.com/guard/guard): Uses YAML as a serialization format for notifications. The data serialized uses symbolic keys, so setting `SafeYAML::OPTIONS[:deserialize_symbols] = true` is necessary to allow Guard to work.
- [**sidekiq**](https://github.com/mperham/sidekiq): Uses a YAML configiuration file with symbolic keys, so setting `SafeYAML::OPTIONS[:deserialize_symbols] = true` should allow it to work.

The above list will grow over time, as more issues are discovered.

Versioning
----------

SafeYAML will follow [semantic versioning](http://semver.org/) so any updates to the first major version will maintain backwards compatability. So expect primarily bug fixes and feature enhancements (if anything!) from here on out... unless it makes sense to break the interface at some point and introduce a version 2.0, which I honestly think is unlikely.

Requirements
------------

SafeYAML requires Ruby 1.8.7 or newer and works with both [Syck](http://www.ruby-doc.org/stdlib-1.8.7/libdoc/yaml/rdoc/YAML.html) and [Psych](http://github.com/tenderlove/psych).

If you are using a version of Ruby where Psych is the default YAML engine (e.g., 1.9.3) but you want to use Syck, be sure to set `YAML::ENGINE.yamler = "syck"` **before** requiring the safe_yaml gem.
# Mixlib::ShellOut
Provides a simplified interface to shelling out yet still collecting both
standard out and standard error and providing full control over environment,
working directory, uid, gid, etc.

No means for passing input to the subprocess is provided.

## Example
Invoke find(1) to search for .rb files:

      find = Mixlib::ShellOut.new("find . -name '*.rb'")
      find.run_command

If all went well, the results are on `stdout`

      puts find.stdout

`find(1)` prints diagnostic info to STDERR:

      puts "error messages" + find.stderr

Raise an exception if it didn't exit with 0

      find.error!

Run a command as the `www` user with no extra ENV settings from `/tmp`

      cmd = Mixlib::ShellOut.new("apachectl", "start", :user => 'www', :env => nil, :cwd => '/tmp')
      cmd.run_command # etc.

## STDIN Example
Invoke crontab to edit user cron:

      # :input only supports simple strings
      crontab_lines = [ "* * * * * /bin/true", "* * * * * touch /tmp/here" ]
      crontab = Mixlib::ShellOut.new("crontab -l -u #{@new_resource.user}", :input => crontab_lines.join("\n"))
      crontab.run_command

## Windows Impersonation Example
Invoke "whoami.exe" to demonstrate running a command as another user:

      whoami = Mixlib::ShellOut.new("whoami.exe", :user => "username", :domain => "DOMAIN", :password => "password")
      whoami.run_command      

## Platform Support
Mixlib::ShellOut does a standard fork/exec on Unix, and uses the Win32
API on Windows. There is not currently support for JRuby.

## License
Apache 2 Licensed. See LICENSE for full details.

## See Also
* `Process.spawn` in Ruby 1.9
* [https://github.com/rtomayko/posix-spawn](https://github.com/rtomayko/posix-spawn)
rebar_lock_json
===============

A minimal escript converting a rebar.lock file to json output.

Should work with any version of rebar (2 or 3)'s rebar.lock file.

Build
-----

    $ rebar3 escriptize # this also copies the escript file to bin/

Run
---

    $ bin/rebar_lock_json path/to/rebar.lock
    {"amqp_client":{"type":"git","git_url":"git:\/\/github.com\/seth\/amqp_client.git","git_ref":"7622ad8093a41b7288a1aa44dd16d3e92ce8f833"}}
# MixLockJson

**TODO: Add description**

## Installation

If [available in Hex](https://hex.pm/docs/publish), the package can be installed
by adding `mix_lock_json` to your list of dependencies in `mix.exs`:

```elixir
def deps do
  [
    {:mix_lock_json, "~> 0.1.0"}
  ]
end
```

Documentation can be generated with [ExDoc](https://github.com/elixir-lang/ex_doc)
and published on [HexDocs](https://hexdocs.pm). Once published, the docs can
be found at [https://hexdocs.pm/mix_lock_json](https://hexdocs.pm/mix_lock_json).

