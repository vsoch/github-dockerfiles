This directory is for libraries:

* for compatibility with ruby 1.8 and 1.9.
* for patching about charctor encoding.
# Docker image for tdiary development

## how to build

```
% docker build -t tdiary-devel misc/docker-devel
```

## how to run

```
% docker run -v $(pwd):/usr/src/app -p 9292:9292 -it --rm tdiary-devel
```

or debugging `contrib` in the parent directory:

```
% docker run -v $(pwd):/usr/src/app -v $(pwd)/../contrib:/usr/src/contrib -p 9292:9292 -it --rm tdiary-devel
```
!機能

blogger API/metaWeblog API/MovableType APIでのtDiaryの更新ができます。

!インストール方法
xmlrpc.rb,ja/xmlrpc.rb,en/xmlrpc.rb,zh/xmlrpc.rbをpluginディレクトリにコピーします。
xmlrpc/xmlrpc.rbをtDiaryのインストールされているディレクトリ(index.rbなどと同じディレクトリ)にコピーします。xmlrpc.rbのパーミッションは、755などに変更する必要があります。
index.rbを設置したディレクトリにrsd.xmlというファイルを作成し、CGIから書き換えられるように書き込み権限を設定します。

!使用方法

設定画面から'XML-RPC API'を選択してXML-RPC APIの設定を行いOKボタンをクリックします。

あとはblogger API/metaWeblog API/MovableType APIに対応したツールからアクセスします。
たとえばubicast BloggerだとXMl-RPCエンドポイントという設定にはxmlrpc.rbのURLを指定します。

  (MovableTypeの場合) http://<youdomain>/<path>/mt-xmlrpc.cgi
  (xmlrpc.rbの場合)   http://<youdomain>/<path>/xmlrpc.rb

rsd.xmlに対応したクライアントならサイトのトップページのURLを指定すればOKです。
tDiary -- a TSUKKOMI-able Web-log
=================================

tDiary is so called Weblog. tDiary has these features.

features
--------

### You can change your configuration with browser.

You can not only read diary, but also write diary. Also, it is possible to change your configuration with browser. With tDiary, you can easily use and maintain Web-log system. So, you continue to write diary for a long time.

### TSUKKOMI

'TSUKKOMI' means a short, smart and heartfelt comment in Japanese. It is possible for diary readers to add a TSUKKOMI to your diary. In other words, tDiary is equipped with BBS. With this BBS, you can communicate with your diary readers. tDiary can inform the author of a new TSUKKOMI by e-mail.

### Today's Link (Referer)

When people links their diary to your diary, tDiary shows their URL by analysis of the referer header. This feature is supported in many Japanese web-log systems. In tDiary, this feature is more user-friendly.

### small devices -- PDA or mobile phone

You can read your diary with PDA or mobile phone, for example, i-mode, Palm, Zaurus(SHARP's PDA) and so on. When you access the same URL as usual, tDiary creates a page for PDA or mobile phone. The page for small devices are small and suitable for reading with them.

### theme -- CSS

You can change the look of the diary by CSS. In tDiary, this feature is called 'theme'. tDiary package has some themes. Of course, you can create a new theme. You can change your theme with browser.

### Plugin

By plugins, you can add new features to tDiary, and change the existing feature of tDiary.

### Selectable Style and IO

You can choice a grammar of writing your diary by 'Style' feature. Some style files are in misc/style. And you can choice data saving format (IO) also. Seee HOWTO-make-io.html for more information about Style or IO.

### Written in Ruby

Important :-). tDiary requires Ruby 2.1.0 or later.

### Others

tDiary also supports these features.

  - Section anchor
  - Read past diaries

Installation and Configuration
------------------------------

In this manual, we presume this environment as one example.

  - WWW server: Apache 1.3.x
  - User: foo
  - Diary URL: http://www.bar.example.org/~foo/diary/
  - Diary Path: /home/foo/public\_html/diary/

### CGI script configuration

Unpack archive, and copy all the files to "/home/foo/public\_html/diary/". You must change permission of two files, which are executed as CGI script.

  - index.rb
  - update.rb

If you use tDiary in an environment where the command "/usr/bin/env" can't be used, you need to edit these files and change their front line so that it stands for the Ruby executable. Except the case when you install Ruby under your home directory, you may be not careful about this thing.

### .htaccess

Next, you arrange CGI environment. You copy "dot.htaccess" as ".htaccess". And, edit it. The file, "dot.htaccess", is like this;

```
Options ExecCGI AddHandler cgi-script .rb DirectoryIndex index.rb  deny from all  deny from all  AuthName tDiary AuthType Basic AuthUserFile /home/foo/.htpasswd Require user foo
```
"dot.htaccess" configures these things.

  - makes it possible to use CGI.
  - makes files whose suffix is ".rb" recognized as CGI script.
  - sets "index.rb" to the default file.
  - prohibits accesses to "*.rhtml" and "tdiary.*"
  - When you access "update.rb", authentification is needed.

At least, you must change the "AuthUserFile" and "Require User" items. In Addition to it, you must create the the file named as "AuthUserFile" by "htpasswd" command before you access your diary. If you don't know "AuthUserFile" and "Require users", please examine these words.

If your WWW server doesn't allow you to change the suffix of CGI scripts, you need to change the "AddHandeler" or "DirectoryIndex" items. In this case, you may need to change the filenames of "index.rb" and "update.rb".

### creation of tdiary.conf

You copy "misc/i18n/tdiary.conf.sample-en" as "tdiary.conf" and edit "tdiary.conf". _Notice! "tdiary.conf.sample" in INSTALLDIR is Japanese version_. "tdiary.conf.sample" only supports Japanese.

"tdiary.conf" is loaded as Ruby script by the CGI scripts, for example, "index.rb" and "update.rb". With tDiary, you can do configuration with browser. If necessary, you may change "@data\_path" parameter at first. "@data\_path" is appeared at the beginning of "tdiary.conf".

```
@data_path = "data"
```
In "@data\_path", you specify the directory where your diary data are stored. This item is usually set to the directory which can not be accessed through WWW. In addition to it, you must set permission of this directory so that the WWW server can access it.

In "tdiary.conf", you can configure many items. They are divided into three categories.

The items which you can't set with browserLike "@data\_path", these are the items which you can't change with browser. These items are configured only by editing "tdiary.conf" directly.

The items which you can set with browserWhen you click the menu, "preferences", you can change your configuration with browser. Almost all the items are changed with browser. You don't have to edit "tdiary.conf" directly.

The items to which you can add values with browser"tdiary.conf" has some items to which values are added with browser, for example, the ignored links and the rules which convert a URL. By editing these items of "tdiary.conf", you can set the default values(This is meaningful if you use multi-user mode).

### Configuration

The meaning of each item is explained in "tdiary.conf.sample". Generally speaking, you can change your configuration with browser after you configure @data\_path. If you want to receive a new TSUKKOMI by e-mail, you configure the @smtp\_host and @smtp\_port.

If you run tDiary in the environment where you can't use the suffix, ".rb", as CGI script, you change the filenames of "index.rb" and "update.rb". In this case, you must configure @index and @update.

After you finish configuration, access "http://www.hoge.example.org/~foo/diary/". If you can see an empty page, tDiary works well. Unfortunately, if you encounter "Internal Server Error", you must change configuration. The error-log of Apache is useful in order to investigate the cause.

run tDiary
----------

### update the diary

At the beginning of the diary page, there are two links, "Top" and "Update". When you click "Top", you move to the page which is specified by "@index\_page". When you click "Update", you move to the page which has the form to update your diary. If the authentification dialog doesn't appear in clicking "Update", there is possibility that your ".htaccess" is wrong.

The "Update" page also has the menu in its beginning. In "Update" page, "Preferences" is added in the right of the menu. When you click it, the "Preferences" page is opened. The detail about the "Preferences" page is explained in the below.

The "Update" page has the form where you can input the date, title, and body of diary. Write your diary and put the "Add" button. By this procedure, the diary is added. Because this procedure is "Add", you don't have to show all the diary data if you write diary many times a day. Once you set the title of the diary, tDiary uses it.

If you set date and click the "Edit this day" button, the title and body of the date are loaded(If the data is empty, these data are not loaded). In this case, the last button of the form is "Register"(Be careful. It is not "Add").

In tDiary, You use a bit specialized HTML in order to describe your diary. It is a little characteristic and it takes considerable time for some people to get accustomed to writing diary in this format. Please read HOWTO-write-diary.

### Configuration with browser

When you click the "Preferences" button in the "Update" page, the "Preferences" page is shown. Here, you can configure many items with browser. In the "Preferences" page, each item has explanation. When you change a item, it is good to refer to explanation. Though the "Preferences" page has many "OK" buttons, their role is the same. When any "OK" button is clicked, all the items are stored to the configuration file. These buttons are located for the purpose of convenience.

The configuration which is done with browser is stored as "tdiary.conf", which is located in the "@data\_path" directory. This "tdiary.conf" is not the "tdiary.conf" which you edit manually. This file is normally loaded after the original "tdiary.conf" is loaded, so the values of the CGI "tdiary.conf" has priority over the values of the original "tdiary.conf". (If you edit the original "tdiary.conf", you can change the timing of loading the cgi "tdiary.conf")

### Read Diary

When you read your diary, tDiary provides the three kind of the pages, "Latest", "Monthly", and "Daily". In default, tDiary shows "Latest" page. You can read the "Monthly" page if you click the link of the calendar located at the beginning of the page. And you can read the "Daily" page if you click the date.

There is difference between "Latest"/"Monthly" and "Daily" page. In "Latest"/"Monthly" page, today's TSUKKOMIs and today's links are partly omitted. On the other hand, "Daily" page shows all the TSUKKOMIs and links. And, "Daily" page has the form for TSUKKOMI.

Every month, day, section, and TSUKKOMI has an anchor, and diary readers can link other place to it. Because each anchor is also a link, you can know the URL of it if you move pointer to it.

With small devices, for instance, mobile phone, Zaurus and Palm, you can't use some of the features above because of restriction on data amount. When you access the diary with small devices, the "Latest" page shows the page which contains only one latest diary. You can move from this page to previous day page or next day page.

### And ...

Now, All you have to do is that you write diary ( But, it is the most difficult to continue to write diary:-) ). Have fun.!!

License
-------

tDiary is free software created by TADA Tadashi(sho@spc.gr.jp). tDiary is licensed under the terms of GPL2 or any later version. You can distribute and modify it under the terms of GPL2.

But, all the files that are in "erb/" directory is ERb library created by Seki-san. You can know the detail about the license of these files at http://www2a.biglobe.ne.jp/~seki/ruby/.

And, authors of all the plugins and themes have its copyright. All the plugins can be distributed and modified under the terms of GPL2. Most themes are also under GPL2, but some have original license. See each theme file.

tDiary is developed on https://sourceforge.net/projects/tdiary/.

ツッコミのできるWeb日記システム
=================

tDiaryでできること
------------

tDiaryは、いわゆるWeb日記を支援するシステムです。tDiaryには以下の特徴があります。

### 更新や設定までブラウザからできる

日記の参照だけでなく、日記の更新、設定までもWebブラウザから実行できます。ブラウザさえあれば面倒なメンテナンスは不要。手軽に使えて、長く続けられます。

### 「ツッコミ」が入れられる

日記の読者が、日記に「ツッコミ」を入れられます。ようするに、日付ごとに掲示板がついています。これを通じて、読者とのコミュニケーションが生まれます。 ツッコミがあったことを著者にメールで知らせる機能もあります。

### 「本日のリンク元」(Referer)機能

他の日記等からリンクされると、Refererヘッダを見てそのURLを表示します。どこかで自分の日記が話題にされていることがすぐにわかるように、従来のWeb日記コミュニケーションで使われている手法をわかりやすくサポートしています。

### 携帯端末対応

iモードに限らず、ほとんどの携帯電話やPalm・ザウルスなどの携帯端末からも日記を参照できます。専用の特別なURLは必要なく、自動認識して最適なページを生成します。通信料金のシビアな端末向けには無駄を省いた小さなページを送るようになっています。

### CSSを使ったテーマ機能

スタイルシートを使って見た目をがらりを変えることができます。これは「テーマ」と呼ばれ、別パッケージとして配布されているテーマ集には、100を越えるテーマが収録されています。もちろん自分で作ることも可能です。テーマは設定画面で簡単に切り替えることができます。

### プラグインによる機能追加

プラグインというモジュールを追加することで、日記の機能を増やしたり変更したりすることが可能です。詳しくは[HOWTO-use-plugin.html](HOWTO-use-plugin.html)(使い方)・[HOWTO-make-plugin.html](HOWTO-make-plugin.html)(作り方)を参照してください。

### 記述形式や保存形式を変更できる

日記を記述する形式(スタイル機能)や、データの保存形式(IO機能)が選択可能です。スタイルはmisc/styleの下に複数収められています。IOは現在、1.4系までの旧tDiary互換のPStoreIOと、2.0系以降の新しいテキスト形式であるDefaultIOがあります。詳しくは[HOWTO-make-io.html](HOWTO-make-io.html)を参照してください。

### Rubyで書かれている

重要なポイントでしょう:-) ruby 2.1.0以上が必要です。

セクション(段落)アンカーや過去の日記の参照など、一般的なWeb日記システムの持つ機能は基本的にサポートしています。

tDiaryのインストールと設定
----------------

[INSTALL.html](INSTALL.html)を参照してください。

著作権、サポートなど
----------

tDiary本体は、原作者であるただただし(t@tdtds.jp)が、GPL2ないしその後継ライセンスの元で配布、改変を許可するフリーソフトウェアです。

また、tDiaryフルセットに付属するテーマ、プラグインはすべて、それぞれの原作者が著作権を有します。ライセンス等に関しては個々のファイルを参照してください。

tDiaryは[http://www.tdiary.org/](http://www.tdiary.org/)でサポートを行っています。ご意見・ご要望はこちらへどうぞ。パッチ歓迎です。

Title: tDiary2デフォルト
Revision: $Revision: 2.0 $
Author: ただただし
Access: t@tdtds.jp
License: GPL2 or any later version
Comment: tDiary 2.0に付属するデフォルトテーマ

ChangeLog
2011-07-16 TADA Tadashi <t@tdtds.jp>
	* renamed from default.

2003-04-17 TADA Tadashi <sho@spc.gr.jp>
	* add table settings.

2003-03-12 TADA Tadashi <sho@spc.gr.jp>
	* little modified.

2003-02-03 TADA Tadashi <sho@spc.gr.jp>
	* add h4.
Title: tDiary3デフォルト
Revision: $Revision: 1.0 $
Author: ただただし
Access: t@tdtds.jp
License: GPL2 or any later version
Comment: tDiary 3.1に付属するデフォルトテーマ

ChangeLog
2011-07-18 TADA Tadashi <t@tdtds.jp>
	* ported from gustav.

Title: tDiary1デフォルト
Revision: $Revision: 1.2 $
Author: ただただし
Access: sho@spc.gr.jp
License: GPL2 or any later version
Comment: tDiary 1.4までのデフォルトテーマ
