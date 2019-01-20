iOS アプリ開発入門

# 今日やること

簡単なアプリの実装を進めながら、iOSアプリ開発の基本を学ぶ。
Firebase というサービスを利用し、端末外のデータを取得して表示したりデータを保存・更新したりするアプリを実装できるようになる。

## 開発環境

- macOS Sierra 10.12.5
- iOS 10.3.2
- Xcode 8.3.3
- Swift 3.1

## 身に付けること

- iOS アプリ開発の基本
- iOS SDK の UIコンポーネントを使った画面の構築と画面間の遷移の実装

# 基礎知識

## iOS アプリとは

iOS が動く端末(iPhone、iPad など)で動作するアプリケーションのこと。

macOS 上で動作する Xcode というアプリケーションを使って Objective-C または Swift というプログラミング言語を用いて開発することができる。

## Swift とは

Apple が開発し 2014年に公開されたプログラミング言語である。 https://swift.org/

Swift が登場するまでは Objective-C, C, C++ などでアプリケーションが開発されていた。 今後はこの Swift を使って iOS アプリケーションを開発するのが主流となる。

- The Swift Programming Language - https://developer.apple.com/library/ios/documentation/Swift/Conceptual/Swift_Programming_Language/
- [ざっくり Swift 入門](./swift.md)

## Firebase とは

Google が提供しているモバイルアプリのための BaaS (Backend as a Service) である。
Firebase はモバイルアプリに必要な機能を実現する複数のサービスから成り立っている。ユーザ認証やデータベース、クラッシュレポート、ユーザイベント分析基盤など様々なものを自由に組み合わせてアプリに組み込むことができる。
講義では Realtime Database を利用してアプリのデータを保存する。

- Firebase - https://firebase.google.com/

# この講義で作成するアプリ

- [Cookpatodon](./cookpatodon_app.md)

# 講義の進め方

- アプリを完成させるまでの過程を複数のパートに分けています
- アプリ開発のやり方を説明しながら一緒に進める講義パートと自分のペースでアプリの機能追加を進める課題パートがあります
- 課題パートでは具体的な実装方法の説明をしないので、iOS SDKやライブラリのドキュメントを自分で読んで取り組んでください。どうしてもわからなければ講師やTAに質問すること。
- 各課題パートの項目では画面の実装例を出していますが、全くその通りに実装する必要はありません
- 課題をひと通り終えてしまった場合はアプリに必要だと思う機能を自分で考えて実装してみてください。機能や見た目、操作感など、こだわろうとするとたくさんやることを見つけられるはずです。

## 講義・実習過程

### iOSアプリ開発の基本編

- [講義1 プロジェクトの作成](./01-create_project.md)
- [講義2 Storyboard を用いた画面の設定](./02-storyboard_basics.md)
- [講義3 画面要素の配置](./03-set_up_tableviewcell.md)
- [講義4 TableView によるリストの表示](./04-show_list_with_tableview.md)

### Firebase Realtime Database を用いたデータ読み書きの基本編

- [講義5 Firebase SDK の導入](./05-introduce_firebase_sdk.md)
- [課題6 投稿一覧画面を実装する](./06-implement_post_list_view.md)
- [講義7 Storyboard を用いた画面遷移](./07-transition_screens.md)
- [課題1 メッセージ投稿画面を実装する](./08-implement_compose_view.md)
- [課題2 ユーザ情報登録画面を実装する](./09-implement_user_settings_view.md)

### 発展課題

- [発展課題1 自分のユーザ名を含む投稿に色を付ける](./10-advanced_colorize_mentioned_message.md)
- [発展課題2 文字数カウンタを実装する](./11-advanced_characters_counter.md)
- [発展課題3 共有したいURLを含めた投稿に対応する](./12-advanced_share_url.md)
# 機械学習

## データに関する注意
インターンではクックパッドの実データを使って分析をしましたが、このRepositoryにはデータは含まれていませんのでためご自身でご準備下さい。
- ./notebooks/basic.ipynb : データの準備なく動かせます
- ./notebooks/recipe_classification_text.ipynb : 少量のサンプルデータがあるのでデータの準備がなくても動かせますが、学習などは意味を成さない結果を返します
- ./notebooks/deeplearning_in_45minutes.ipynb : データの準備なく動かせます
- ./notebooks/recipe_classification_image.ipynb : データを準備しないと動かせません
- ./notebooks/object_detection/object_detection.ipynb : データの準備なく動かせます

## 講義資料
https://speakerdeck.com/diracdiego/cookpad-summer-internship-2017-ml <br>
分析用の環境構築の手順もこの講義資料内で説明されています。

## 目的
- 機械学習の一端を知り、サービスを創るときに機械学習を使ってより良いものとできないかを検討できるようになる

## ゴール
- 機械学習一般に関して
  - 機械学習とは何かを自分の言葉で説明できるようになる
  - 機械学習がどのような用途で使えるかを理解し、pythonを用いたモデル構築を経験する
  - 機械学習をどのように学んでいけばよいかを理解する
- ディープラーニングに関して
  - ディープラーニングとは何かを自分の言葉で説明できるようになる
  - 画像分析でよく用いられるCNNの基礎を理解し、pythonを用いたモデル構築を経験する
  - 画像分析における最近の話題について幾許かの知識を得る

## 時間割

| 時間        | 内容        |
|:---------------:|:---------------|
| 9:30-10:30 | 【講義】機械学習とは何か？ |
| 10:30-10:40 | 休憩 |
| 10:40-12:00 | 【実習】機械学習初歩 |
| 12:00-13:00 | 昼食 |
| 13:00-14:30 | 【講義】ディープラーニング（画像分析） |
| 14:30-14:40 | 休憩 |
| 14:40-16:20 | 【実習】画像分析 |
| 16:20-16:30 | 休憩 |
| 16:30-17:50 | 発展的課題への挑戦 |
| 17:50-18:00 | 本日のまとめ |
| 18:00-18:30 | 日報・質問 |
# 概要

## 開発環境/ツール
- Android Studio 2.3.3
- Android 7.1 (API level 25) をターゲット
- Java7 相当

## 前準備
[Prerequisites](prerequisites.md) の内容がすべて終わっている


## 講義の目的
- Android のアプリ構成要素について理解する
- 一般的なView要素による画面レイアウト、画面遷移などの実装方法を理解する
- すべての課題をこなすことで入門レベルのAndroid開発ができるようになる

## タイムスケジュール

- 09:30 - 10:00 自己紹介、セットアップ
- 10:00 - 12:00 基本編
- 12:00 - 13:00 ランチ
- 13:00 - 15:30 基本編
- 15:30 - 18:00 発展課題(適宜質問)
- 18:00 - 18:30 まとめ

## この講義で得られる知識

- Androidプロジェクトの基本構成
- Activity のライフサイクルに関する理解
- xmlを使ったレイアウトの組み方
- RecyclerView によるリスト表示
- Activityによる画面遷移の実装
- Firebase Auth の使い方(一部)
- Firebase Realtime Database の使い方
- アプリのデバッグ方法

# 基本編

- [講義1 : HelloWorld](01-hello_world.md)
- [講義2 : Firebase #とは](02-firebase.md)
- [講義3 : 認証処理の実装](03-implement_anonymous_auth.md)
- [講義4 : 投稿一覧の取得](04-get_post_list.md)
- [講義5 : 投稿一覧の表示](05-show_post_list.md)
- [講義6 : 投稿機能の実装](06-implement_post_message.md)
- [講義7 : ユーザー情報の更新](07-implement_user_setting.md)

# 発展課題

- [課題1 : 自分のユーザー名を含む投稿に色を付ける](08-advanced_colorize_mentioned_message.md)
- [課題2 : 投稿時の文字数チェックを実装する](09-advanced_characters_counter.md)
- [課題3 : 共有したいURLを含めた投稿に対応する](10-advanced_share_url.md)
- [課題4 : ユーザー一覧を表示する](11-advanced_user_list.md)
- [課題5 : 特定のユーザーの投稿一覧を表示する](12-advanced_post_list_by_user.md)
