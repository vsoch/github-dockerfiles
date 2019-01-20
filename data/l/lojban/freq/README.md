Introduction
------------

This code takes the data from:

http://www.lojban.org/corpus/ (specifically the "compressed" link in "Corpus (compressed)" )

and

http://jbovlaste.lojban.org/ (specifically the XML Export -> English link)

and uses them with a template to generate a list of words in usage
order in whatever format you specify.

There are two modes: in blob mode, the template is run exactly once,
with all words.  In normal mode, the template is run once for each
word and the results are concatenated.  Which mode you want to use
depends on how the template was written, but normally you want
normal mode.

Example Run
-----------

    ./run_docker.sh -t templates/anki_gismu.erb -o test.out

gives you test.out with the lines generated by the anki_gismu
template.

To get a shell in the docker environment for testing/debugging:

    ./run_docker.sh shell

Template Details
----------------

The following, in YAML format, is what the "words" variable looks
like if you use the -b option.  The normal mode is the same
except that you get each of these words one at a time, and all of
the per-word items are variables, i.e. "type" is a variable, "word"
is a variable, etc.

In normal mode, all the parts of the current word are available as a
hash at the variable "word_all", and all the words are available as
an array at the variable "words_all".

There's also an artificial variable, rafsi_or_selmaho, which is all
the rafsi joined with spaces, if any, or the selmaho, or the empty
string.

The Ruby "||=" idiom is very useful here.  For example, this:

    <%= notes %>

will fail if any word has no notes field, but this:

    <%= notes ||= '' %>

works fine, and the auto-vivification of the variable does us no
harm.

    - definition: 'descriptor: the one, which (is / does) ... / those, which (are / do)
        ...'
      selmaho: LE
      notes: Terminated with {ku}. Under the xorlo reform, {lo} converts a selbri to a
        sumti in a generic way. In particular, lo broda = {zo'e} noi broda.
      glosswords:
      - word: that, which
      type: cmavo
      word: lo
      frequency: 374663
      rank_up: 1
      rank_down: 9720
    - definition: "$x_{1}$ is happy/merry/glad/gleeful about $x_{2}$ (event/state)."
      notes: Adversity (= {kamnalgei}).  See also {badri}, {cinmo}.
      rafsi:
      - gek
      - gei
      glosswords:
      - word: happy
      type: gismu
      word: gleki
      frequency: 54166
      rank_up: 13
      rank_down: 9708
    - definition: "$x_{1}$ (agent) expresses/says $x_{2}$ (sedu'u/text/lu'e concept) for
        audience $x_{3}$ via expressive medium $x_{4}$."
      notes: Also says.  See also {bacru}, {tavla}, {casnu}, {spuda}, cmavo list {cu'u},
        {bangu}, {dapma}, {jufra}, {pinka}.
      rafsi:
      - cus
      - sku
      glosswords:
      - word: say
      - word: express
      - word: mention
      keywords:
      - word: expresser
        place: '1'
      - word: expression
        sense: expressed information
        place: '2'
      - word: audience
        sense: receiver of expression
        place: '3'
      - word: medium
        sense: communication format
        place: '4'
      type: gismu
      word: cusku
      frequency: 19373
      rank_up: 47
      rank_down: 9674