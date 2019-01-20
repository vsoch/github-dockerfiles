"Moono-lisa" Skin
=================

This skin has been made a **default skin** starting from CKEditor 4.6.0 and is maintained by the core developers.

For more information about skins, please check the [CKEditor Skin SDK](http://docs.cksource.com/CKEditor_4.x/Skin_SDK)
documentation.

Features
-------------------
"Moono-lisa" is a monochromatic skin, which offers a modern, flat and minimalistic look which blends very well in modern design.
It comes with the following features:

- Chameleon feature with brightness.
- High-contrast compatibility.
- Graphics source provided in SVG.

Directory Structure
-------------------

CSS parts:
- **editor.css**: the main CSS file. It's simply loading several other files, for easier maintenance,
- **mainui.css**: the file contains styles of entire editor outline structures,
- **toolbar.css**: the file contains styles of the editor toolbar space (top),
- **richcombo.css**: the file contains styles of the rich combo ui elements on toolbar,
- **panel.css**: the file contains styles of the rich combo drop-down, it's not loaded
until the first panel open up,
- **elementspath.css**: the file contains styles of the editor elements path bar (bottom),
- **menu.css**: the file contains styles of all editor menus including context menu and button drop-down,
it's not loaded until the first menu open up,
- **dialog.css**: the CSS files for the dialog UI, it's not loaded until the first dialog open,
- **reset.css**: the file defines the basis of style resets among all editor UI spaces,
- **preset.css**: the file defines the default styles of some UI elements reflecting the skin preference,
- **editor_XYZ.css** and **dialog_XYZ.css**: browser specific CSS hacks.

Other parts:
- **skin.js**: the only JavaScript part of the skin that registers the skin, its browser specific files and its icons and defines the Chameleon feature,
- **images/**: contains a fill general used images,
- **dev/**: contains SVG and PNG source of the skin icons.

License
-------

Copyright (c) 2003-2016, CKSource - Frederico Knabben. All rights reserved.

For licensing, see LICENSE.md or [http://ckeditor.com/license](http://ckeditor.com/license)
"Moono" Skin
====================

This skin has been chosen for the **default skin** of CKEditor 4.x, elected from the CKEditor
[skin contest](http://ckeditor.com/blog/new_ckeditor_4_skin) and further shaped by
the CKEditor team. "Moono" is maintained by the core developers.

For more information about skins, please check the [CKEditor Skin SDK](http://docs.cksource.com/CKEditor_4.x/Skin_SDK)
documentation.

Features
-------------------
"Moono" is a monochromatic skin, which offers a modern look coupled with gradients and transparency.
It comes with the following features:

- Chameleon feature with brightness,
- high-contrast compatibility,
- graphics source provided in SVG.

Directory Structure
-------------------

CSS parts:
- **editor.css**: the main CSS file. It's simply loading several other files, for easier maintenance,
- **mainui.css**: the file contains styles of entire editor outline structures,
- **toolbar.css**: the file contains styles of the editor toolbar space (top),
- **richcombo.css**: the file contains styles of the rich combo ui elements on toolbar,
- **panel.css**: the file contains styles of the rich combo drop-down, it's not loaded
until the first panel open up,
- **elementspath.css**: the file contains styles of the editor elements path bar (bottom),
- **menu.css**: the file contains styles of all editor menus including context menu and button drop-down,
it's not loaded until the first menu open up,
- **dialog.css**: the CSS files for the dialog UI, it's not loaded until the first dialog open,
- **reset.css**: the file defines the basis of style resets among all editor UI spaces,
- **preset.css**: the file defines the default styles of some UI elements reflecting the skin preference,
- **editor_XYZ.css** and **dialog_XYZ.css**: browser specific CSS hacks.

Other parts:
- **skin.js**: the only JavaScript part of the skin that registers the skin, its browser specific files and its icons and defines the Chameleon feature,
- **icons/**: contains all skin defined icons,
- **images/**: contains a fill general used images,
- **dev/**: contains SVG source of the skin icons.

License
-------

Copyright (c) 2003-2016, CKSource - Frederico Knabben. All rights reserved.

For licensing, see LICENSE.md or [http://ckeditor.com/license](http://ckeditor.com/license)
CKEditor 4
==========

Copyright (c) 2003-2016, CKSource - Frederico Knabben. All rights reserved.
http://ckeditor.com - See LICENSE.md for license information.

CKEditor is a text editor to be used inside web pages. It's not a replacement
for desktop text editors like Word or OpenOffice, but a component to be used as
part of web applications and websites.

## Documentation

The full editor documentation is available online at the following address:
http://docs.ckeditor.com

## Installation

Installing CKEditor is an easy task. Just follow these simple steps:

 1. **Download** the latest version from the CKEditor website:
    http://ckeditor.com. You should have already completed this step, but be
    sure you have the very latest version.
 2. **Extract** (decompress) the downloaded file into the root of your website.

**Note:** CKEditor is by default installed in the `ckeditor` folder. You can
place the files in whichever you want though.

## Checking Your Installation

The editor comes with a few sample pages that can be used to verify that
installation proceeded properly. Take a look at the `samples` directory.

To test your installation, just call the following page at your website:

	http://<your site>/<CKEditor installation path>/samples/index.html

For example:

	http://www.example.com/ckeditor/samples/index.html
CKEditor SCAYT Plugin
=====================

This plugin brings Spell Check As You Type (SCAYT) into up to CKEditor 4+.

SCAYT is a "installation-less", using the web-services of [WebSpellChecker.net](http://www.webspellchecker.net/). It's an out of the box solution.

Installation
------------

1. Clone/copy this repository contents in a new "plugins/scayt" folder in your CKEditor installation.
2. Enable the "scayt" plugin in the CKEditor configuration file (config.js):

        config.extraPlugins = 'scayt';

That's all. SCAYT will appear on the editor toolbar and will be ready to use.

License
-------

Licensed under the terms of any of the following licenses at your choice: [GPL](http://www.gnu.org/licenses/gpl.html), [LGPL](http://www.gnu.org/licenses/lgpl.html) and [MPL](http://www.mozilla.org/MPL/MPL-1.1.html).

See LICENSE.md for more information.

Developed in cooperation with [WebSpellChecker.net](http://www.webspellchecker.net/).
CKEditor WebSpellChecker Plugin
===============================

This plugin brings Web Spell Checker (WSC) into CKEditor.

WSC is "installation-less", using the web-services of [WebSpellChecker.net](http://www.webspellchecker.net/). It's an out of the box solution.

Installation
------------

1. Clone/copy this repository contents in a new "plugins/wsc" folder in your CKEditor installation.
2. Enable the "wsc" plugin in the CKEditor configuration file (config.js):

        config.extraPlugins = 'wsc';

That's all. WSC will appear on the editor toolbar and will be ready to use.

License
-------

Licensed under the terms of any of the following licenses at your choice: [GPL](http://www.gnu.org/licenses/gpl.html), [LGPL](http://www.gnu.org/licenses/lgpl.html) and [MPL](http://www.mozilla.org/MPL/MPL-1.1.html).

See LICENSE.md for more information.

Developed in cooperation with [WebSpellChecker.net](http://www.webspellchecker.net/).
# Highlight.js

Highlight.js нужен для подсветки синтаксиса в примерах кода в блогах,
форумах и вообще на любых веб-страницах. Пользоваться им очень просто,
потому что работает он автоматически: сам находит блоки кода, сам
определяет язык, сам подсвечивает.

Автоопределением языка можно управлять, когда оно не справляется само (см.
дальше "Эвристика").


## Простое использование

Подключите библиотеку и стиль на страницу и повесть вызов подсветки на
загрузку страницы:

```html
<link rel="stylesheet" href="styles/default.css">
<script src="highlight.pack.js"></script>
<script>hljs.initHighlightingOnLoad();</script>
```

Весь код на странице, обрамлённый в теги `<pre><code> .. </code></pre>`
будет автоматически подсвечен. Если вы используете другие теги или хотите
подсвечивать блоки кода динамически, читайте "Инициализацию вручную" ниже.

- Вы можете скачать собственную версию "highlight.pack.js" или сослаться
  на захостенный файл, как описано на странице загрузки:
  <http://highlightjs.org/download/>

- Стилевые темы можно найти в загруженном архиве или также использовать
  захостенные. Чтобы сделать собственный стиль для своего сайта, вам
  будет полезен [CSS classes reference][cr], который тоже есть в архиве.

[cr]: http://highlightjs.readthedocs.org/en/latest/css-classes-reference.html


## node.js

Highlight.js можно использовать в node.js. Библиотеку со всеми возможными языками можно
установить с NPM:

    npm install highlight.js

Также её можно собрать из исходников с только теми языками, которые нужны:

    python3 tools/build.py -tnode lang1 lang2 ..

Использование библиотеки:

```javascript
var hljs = require('highlight.js');

// Если вы знаете язык
hljs.highlight(lang, code).value;

// Автоопределение языка
hljs.highlightAuto(code).value;
```


## AMD

Highlight.js можно использовать с загрузчиком AMD-модулей.  Для этого его
нужно собрать из исходников следующей командой:

```bash
$ python3 tools/build.py -tamd lang1 lang2 ..
```

Она создаст файл `build/highlight.pack.js`, который является загружаемым
AMD-модулем и содержит все выбранные при сборке языки. Используется он так:

```javascript
require(["highlight.js/build/highlight.pack"], function(hljs){

  // Если вы знаете язык
  hljs.highlight(lang, code).value;

  // Автоопределение языка
  hljs.highlightAuto(code).value;
});
```


## Замена TABов

Также вы можете заменить символы TAB ('\x09'), используемые для отступов, на
фиксированное количество пробелов или на отдельный `<span>`, чтобы задать ему
какой-нибудь специальный стиль:

```html
<script type="text/javascript">
  hljs.configure({tabReplace: '    '}); // 4 spaces
  // ... or
  hljs.configure({tabReplace: '<span class="indent">\t</span>'});

  hljs.initHighlightingOnLoad();
</script>
```


## Инициализация вручную

Если вы используете другие теги для блоков кода, вы можете инициализировать их
явно с помощью функции `highlightBlock(code)`. Она принимает DOM-элемент с
текстом расцвечиваемого кода и опционально - строчку для замены символов TAB.

Например с использованием jQuery код инициализации может выглядеть так:

```javascript
$(document).ready(function() {
  $('pre code').each(function(i, e) {hljs.highlightBlock(e)});
});
```

`highlightBlock` можно также использовать, чтобы подсветить блоки кода,
добавленные на страницу динамически. Только убедитесь, что вы не делаете этого
повторно для уже раскрашенных блоков.

Если ваш блок кода использует `<br>` вместо переводов строки (т.е. если это не
`<pre>`), включите опцию `useBR`:

```javascript
hljs.configure({useBR: true});
$('div.code').each(function(i, e) {hljs.highlightBlock(e)});
```


## Эвристика

Определение языка, на котором написан фрагмент, делается с помощью
довольно простой эвристики: программа пытается расцветить фрагмент всеми
языками подряд, и для каждого языка считает количество подошедших
синтаксически конструкций и ключевых слов. Для какого языка нашлось больше,
тот и выбирается.

Это означает, что в коротких фрагментах высока вероятность ошибки, что
периодически и случается. Чтобы указать язык фрагмента явно, надо написать
его название в виде класса к элементу `<code>`:

```html
<pre><code class="html">...</code></pre>
```

Можно использовать рекомендованные в HTML5 названия классов:
"language-html", "language-php". Также можно назначать классы на элемент
`<pre>`.

Чтобы запретить расцветку фрагмента вообще, используется класс "no-highlight":

```html
<pre><code class="no-highlight">...</code></pre>
```


## Экспорт

В файле export.html находится небольшая программка, которая показывает и дает
скопировать непосредственно HTML-код подсветки для любого заданного фрагмента кода.
Это может понадобится например на сайте, на котором нельзя подключить сам скрипт
highlight.js.


## Координаты

- Версия: 8.0
- URL:    http://highlightjs.org/

Лицензионное соглашение читайте в файле LICENSE.
Список авторов и соавторов читайте в файле AUTHORS.ru.txt
All icons are taken from Font Awesome (http://fontawesome.io/) project.
The Font Awesome font is licensed under the SIL OFL 1.1:
- http://scripts.sil.org/OFL

SVG icons source: https://github.com/encharm/Font-Awesome-SVG-PNG
Font-Awesome-SVG-PNG is licensed under the MIT license (see file license
in current folder).
Roboto webfont source: https://www.google.com/fonts/specimen/Roboto
Weights used in this project: Light (300), Regular (400), Bold (700)
