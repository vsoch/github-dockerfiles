# Iris Web Framework <a href="README.md"> <img width="20px" src="https://iris-go.com/images/flag-unitedkingdom.svg?v=10" /></a> <a href="README_ZH.md"> <img width="20px" src="https://iris-go.com/images/flag-china.svg?v=10" /></a> <a href="README_RU.md"><img width="20px" src="https://iris-go.com/images/flag-russia.svg?v=10" /></a> <a href="README_ID.md"> <img width="20px" src="https://iris-go.com/images/flag-indonesia.svg?v=10" /></a> <a href="README_PT_BR.md"><img width="20px" src="https://iris-go.com/images/flag-pt-br.svg?v=10" /></a> <a href="README_JPN.md"><img width="20px" src="https://iris-go.com/images/flag-japan.svg?v=10" /></a>

<a href="https://iris-go.com"> <img align="right" width="169px" src="https://iris-go.com/images/icon.svg?v=a" title="logo created by @merry.dii" /> </a>

[![build status](https://img.shields.io/travis/kataras/iris/master.svg?style=flat-square)](https://travis-ci.org/kataras/iris)<!-- [![release](https://img.shields.io/github/release/kataras/iris.svg?style=flat-square)](https://github.com/kataras/iris/releases)--> [![report card](https://img.shields.io/badge/report%20card-a%2B-ff3333.svg?style=flat-square)](http://goreportcard.com/report/kataras/iris) [![vscode-iris](https://img.shields.io/badge/ext%20-vscode-0c77e3.svg?style=flat-square)](https://marketplace.visualstudio.com/items?itemName=kataras2006.iris)<!--[![github closed issues](https://img.shields.io/github/issues-closed-raw/kataras/iris.svg?style=flat-square)](https://github.com/kataras/iris/issues?q=is%3Aissue+is%3Aclosed)--> [![chat](https://img.shields.io/badge/community-%20chat-00BCD4.svg?style=flat-square)](https://kataras.rocket.chat/channel/iris) [![view examples](https://img.shields.io/badge/learn%20by-examples-0077b3.svg?style=flat-square)](https://iris-go.com/v10/recipe) [![release](https://img.shields.io/badge/release%20-v10.6-0077b3.svg?style=flat-square)](https://github.com/kataras/iris/releases)

Το Iris είναι ένα γρήγορο, απλό αλλά και πλήρως λειτουργικό και πολύ αποδοτικό web framework για τη Go.

Το Iris παρέχει ένα όμορφα εκφραστικό και εύχρηστο υπόβαθρο για την επόμενη σας ιστοσελίδα ή API.

Επιτέλους, ένα πραγματικά ισάξιο (και με το παραπάνω) expressjs web framework για τη γλώσσα προγραμματισμού Go.

Μάθετε τι [λένε οι άλλοι για το Iris](#%CE%A5%CF%80%CE%BF%CF%83%CF%84%CE%AE%CF%81%CE%B9%CE%BE%CE%B7) και [δώστε ένα αστέρι](https://github.com/kataras/iris/stargazers) στο github repository για να μένετε [πάντα ενημερωμένοι](https://facebook.com/iris.framework).

## Yποστηρικτές

Eυχαριστούμε όλους τους υποστηρικτές μας! 🙏 [Γίνετε ένας από αυτούς](https://iris-go.com/donate)

<a href="https://iris-go.com/donate" target="_blank"><img src="https://iris-go.com/backers.svg?v=2"/></a>

```sh
$ cat example.go
```

```go
package main

import "github.com/kataras/iris"

func main() {
    app := iris.New()
    // Εδώ φορτώνουμε όλα τα templates από τον
    // φάκελο "./views"
    // όπου το extension είναι ".html" και αναλύουμε
    // τα αρχεία αυτά βάση του `html/template` πακέτου.
    app.RegisterView(iris.HTML("./views", ".html"))

    // Method:    GET
    // Resource:  http://localhost:8080
    app.Get("/", func(ctx iris.Context) {
        // Όπου {{.message}} εμφάνισε "Hello world!"
        ctx.ViewData("message", "Hello world!")
        // Εμφάνισε το σχετικό αρχείο "./views/hello.html"
        ctx.View("hello.html")
    })

    // Method:    GET
    // Resource:  http://localhost:8080/user/42
    //
    // Θέλετε να χρησημοποιήσετε regex expressions;
    // Εύκολο,
    // απλά δηλώστε τον τύπο της παραμέτρου ως 'string'
    // ο οποίος δέχετε κάθε τιμή και κάντε χρήση
    // της `regexp` macro function, για παράδειγμα:
    // app.Get("/user/{id:string regexp(^[0-9]+$)}")
    app.Get("/user/{id:long}", func(ctx iris.Context) {
        userID, _ := ctx.Params().GetInt64("id")
        ctx.Writef("User ID: %d", userID)
    })

    // Εδώ αρχίζουμε τον server χρησιμοποιώντας την
    // τοπική διεύθυνση δικτύου με πόρτα την 8080.
    app.Run(iris.Addr(":8080"))
}
```

> Μάθετε περισσότερα για τους τύπους παραμέτρων διαδρομής(routing) πατώντας [εδώ](_examples/routing/dynamic-path/main.go#L31)

```html
<!-- αρχείο: ./views/hello.html -->
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>{{.message}}</h1>
</body>
</html>
```

```sh
$ go run example.go
Now listening on: http://localhost:8080
Application Started. Press CTRL+C to shut down.
_
```

## Εγκατάσταση

Η μόνη απαίτηση είναι η [Go Γλώσσα Προγραμματισμού](https://golang.org/dl/)

```sh
$ go get -u github.com/kataras/iris
```

Το Iris εκμεταλλεύεται τη λεγόμενη λειτουργία [vendor directory](https://docs.google.com/document/d/1Bz5-UB7g2uPBdOx-rw5t9MxJwkfpx90cqG9AFL0JAYo). Παίρνετε πλήρως αναπαραγωγίσιμα builds, καθώς αυτή η μέθοδος προστατεύει από τις upstream μετονομασίες και διαγραφές.

[![Iris vs .NET Core(C#) vs Node.js (Express)](https://iris-go.com/images/benchmark-new-gray.png)](_benchmarks/README_UNIX.md)

_Η τελευταία ενημέρωση έγινε την [Τρίτη, 21 Νοεμβρίου του 2017](_benchmarks/README_UNIX.md)_

<details>
<summary>Στοιχεία αναφοράς από τρίτες πηγές σε σχέση με τα υπόλοιπα web frameworks</summary>

![Comparison with other frameworks](https://raw.githubusercontent.com/smallnest/go-web-framework-benchmark/4db507a22c964c9bc9774c5b31afdc199a0fe8b7/benchmark.png)

</details>

## Υποστήριξη

- To [HISTORY](HISTORY_GR.md#tu-05-june-2018--v1066) αρχείο είναι ο καλύτερος σας φίλος, περιέχει πληροφορίες σχετικά με τις τελευταίες λειτουργίες(features) και αλλαγές
- Μήπως τυχαίνει να βρήκατε κάποιο bug; Δημοσιεύστε το στα [github issues](https://github.com/kataras/iris/issues)
- Έχετε οποιεσδήποτε ερωτήσεις ή πρέπει να μιλήσετε με κάποιον έμπειρο για την επίλυση ενός προβλήματος σε πραγματικό χρόνο; Ελάτε μαζί μας στην [συνομιλία κοινότητας](https://chat.iris-go.com)
- Συμπληρώστε την αναφορά εμπειρίας χρήστη κάνοντας κλικ [εδώ](https://docs.google.com/forms/d/e/1FAIpQLSdCxZXPANg_xHWil4kVAdhmh7EBBHQZ_4_xSZVDL-oCC_z5pA/viewform?usp=sf_link)
- Σας αρέσει το Iris; Τιτιβίστε κάτι για αυτό! Άνθρωποι από ολόκληρο τον πλανήτη έχουνε μιλήσει για αυτό ακριβώς:

<a href="https://twitter.com/gelnior/status/769100480706379776"> 
    <img src="https://comments.iris-go.com/comment27_mini.png" width="350px">
</a>

<a href="https://twitter.com/MeAlex07/status/822799954188075008"> 
    <img src="https://comments.iris-go.com/comment28_mini.png" width="350px">
</a>

<a href="https://twitter.com/_mgale/status/818591490305761280"> 
    <img src="https://comments.iris-go.com/comment29_mini.png" width="350px">
</a>
<a href="https://twitter.com/VeayoX/status/813273328550973440"> 
    <img src="https://comments.iris-go.com/comment30_mini.png" width="350px">
</a>

<a href="https://twitter.com/pvsukale/status/745328224876408832"> 
    <img src="https://comments.iris-go.com/comment31_mini.png" width="350px">
</a>

<a href="https://twitter.com/blainsmith/status/745338092211560453"> 
    <img src="https://comments.iris-go.com/comment32_mini.png" width="350px">
</a>

<a href="https://twitter.com/tjbyte/status/758287014210867200"> 
    <img src="https://comments.iris-go.com/comment33_mini.png" width="350px">
</a>

<a href="https://twitter.com/tangzero/status/751050577220698112"> 
    <img src="https://comments.iris-go.com/comment34_mini.png" width="350px">
</a>

<a href="https://twitter.com/tjbyte/status/758287244947972096"> 
    <img src="https://comments.iris-go.com/comment33_2_mini.png" width="350px">
</a>

<a href="https://twitter.com/ferarias/status/902468752364773376"> 
    <img src="https://comments.iris-go.com/comment41.png" width="350px">
</a>

<br/><br/>

Για περισσότερες πληροφορίες σχετικά με τη συμβολή στο Iris, διαβάστε το [CONTRIBUTING.md](CONTRIBUTING.md) αρχείο.

[Κατάλογος όλων των Συνεργατών](https://github.com/kataras/iris/graphs/contributors)

## Μάθηση

Πρώτα απ 'όλα, ο πιο σωστός τρόπος για να ξεκινήσετε με ένα web framework είναι να μάθετε τα βασικά της γλώσσας προγραμματισμού και των τυπικών της δυνατοτήτων `http`, αν η εφαρμογή σας είναι ένα πολύ απλό προσωπικό έργο χωρίς απαιτήσεις επιδόσεων και συντηρησιμότητας, ίσως να θέλετε να προχωρήσετε μόνο με τα τυπικά πακέτα, εαν οχι τότε ακολουθήστε τις παρακάτω οδηγίες:

- Πλοηγηθείτε μέσω των **100+1** **[παραδειγμάτων](_examples)** και μερικές [απλές εφαρμογές για αρχάριους](#iris-starter-kits) που δημιουργήσαμε για εσάς
- Διαβάστε τα [godocs](https://godoc.org/github.com/kataras/iris) για οποιαδήποτε λεπτομέρεια
- Ετοιμάστε ένα φλιτζάνι καφέ ή τσάι, ό,τι σας ευχαριστεί περισσότερο και διαβάστε κάποια [άρθρα](#articles) που βρήκαμε για εσάς

### Iris starter kits

<!-- table form 
| Description | Link |
| -----------|-------------|
| Hasura hub starter project with a ready to deploy golang helloworld webapp with IRIS! | https://hasura.io/hub/project/hasura/hello-golang-iris |
| A basic web app built in Iris for Go |https://github.com/gauravtiwari/go_iris_app |
| A mini social-network created with the awesome Iris💖💖 | https://github.com/iris-contrib/Iris-Mini-Social-Network |
| Iris isomorphic react/hot reloadable/redux/css-modules starter kit | https://github.com/iris-contrib/iris-starter-kit |
| Demo project with react using typescript and Iris | https://github.com/ionutvilie/react-ts |
| Self-hosted Localization Management Platform built with Iris and Angular | https://github.com/iris-contrib/parrot |
| Iris + Docker and Kubernetes | https://github.com/iris-contrib/cloud-native-go |
| Quickstart for Iris with Nanobox | https://guides.nanobox.io/golang/iris/from-scratch |
-->

1. [A basic web app built in Iris for Go](https://github.com/gauravtiwari/go_iris_app)
2. [A mini social-network created with the awesome Iris💖💖](https://github.com/iris-contrib/Iris-Mini-Social-Network)
3. [Iris isomorphic react/hot reloadable/redux/css-modules starter kit](https://github.com/iris-contrib/iris-starter-kit)
4. [Demo project with react using typescript and Iris](https://github.com/ionutvilie/react-ts)
5. [Self-hosted Localization Management Platform built with Iris and Angular](https://github.com/iris-contrib/parrot)
6. [Iris + Docker and Kubernetes](https://github.com/iris-contrib/cloud-native-go)
7. [Quickstart for Iris with Nanobox](https://guides.nanobox.io/golang/iris/from-scratch)
8. [A Hasura starter project with a ready to deploy Golang hello-world web app with IRIS](https://hasura.io/hub/project/hasura/hello-golang-iris)

> Έχετε χτίσει κάτι παρόμοιο; [Ενημέρωσέ μας](https://github.com/kataras/iris/pulls)!

### Middleware

Το Iris έχει μια μεγάλη συλλογή Handlers[[1]](middleware/)[[2]](https://github.com/iris-contrib/middleware) που μπορείτε να χρησιμοποιήσετε μέσα στις εφαρμογές σας. Ωστόσο, δεν περιορίζεστε σε αυτά - είστε ελεύθεροι να χρησιμοποιήσετε οποιοδήποτε μεσαίο λογισμικό τρίτου μέρους που είναι συμβατό με το [net/http](https://golang.org/pkg/net/http/) πακέτο, [_examples/convert-handlers](_examples/convert-handlers) θα σας δείξουν τον δρόμο.

Το Iris, σε αντίθεση με τα άλλα, είναι 100% συμβατό με τα πρότυπα και γι 'αυτό η πλειοψηφία των μεγάλων εταιρειών που προσαρμόζονται στην Go, όπως ένα πολύ γνωστό τηλεοπτικό δίκτυο των ΗΠΑ, εμπιστεύονται το Iris, και αυτό γιατί είναι πάντα ενημερωμένο και ευθυγραμμισμένο με το πακέτο `net/http` το οποίο εκσυγχρονίζεται από τους συγγραφέες(authors) της Go σε κάθε νέα έκδοση της, για πάντα.

### Articles

* [A Todo MVC Application using Iris and Vue.js](https://hackernoon.com/a-todo-mvc-application-using-iris-and-vue-js-5019ff870064)
* [A Hasura starter project with a ready to deploy Golang hello-world web app with IRIS](bit.ly/2lmKaAZ)
* [Top 6 web frameworks for Go as of 2017](https://blog.usejournal.com/top-6-web-frameworks-for-go-as-of-2017-23270e059c4b)
* [Iris Go Framework + MongoDB](https://medium.com/go-language/iris-go-framework-mongodb-552e349eab9c)
* [How to build a file upload form using DropzoneJS and Go](https://hackernoon.com/how-to-build-a-file-upload-form-using-dropzonejs-and-go-8fb9f258a991)
* [How to display existing files on server using DropzoneJS and Go](https://hackernoon.com/how-to-display-existing-files-on-server-using-dropzonejs-and-go-53e24b57ba19)
* [Iris, a modular web framework](https://medium.com/@corebreaker/iris-web-cd684b4685c7)
* [Go vs .NET Core in terms of HTTP performance](https://medium.com/@kataras/go-vs-net-core-in-terms-of-http-performance-7535a61b67b8)
* [Iris Go vs .NET Core Kestrel in terms of HTTP performance](https://hackernoon.com/iris-go-vs-net-core-kestrel-in-terms-of-http-performance-806195dc93d5)
* [How to Turn an Android Device into a Web Server](https://twitter.com/ThePracticalDev/status/892022594031017988)
* [Deploying a Iris Golang app in hasura](https://medium.com/@HasuraHQ/deploy-an-iris-golang-app-with-backend-apis-in-minutes-25a559bf530b)
* [A URL Shortener Service using Go, Iris and Bolt](https://medium.com/@kataras/a-url-shortener-service-using-go-iris-and-bolt-4182f0b00ae7)

### Εκμάθηση μέσω video

* [Daily Coding - Web Framework Golang: Iris Framework]( https://www.youtube.com/watch?v=BmOLFQ29J3s) από WarnabiruTV, πηγή: youtube, κόστος: **ΔΩΡΕΑΝ**
* [Tutorial Golang MVC dengan Iris Framework & Mongo DB](https://www.youtube.com/watch?v=uXiNYhJqh2I&list=PLMrwI6jIZn-1tzskocnh1pptKhVmWdcbS) (19 videos ως τωρα) από Musobar Media, πηγή: youtube, κόστος: **ΔΩΡΕΑΝ**
* [Go/Golang 27 - Iris framework : Routage de base](https://www.youtube.com/watch?v=rQxRoN6ub78) από stephgdesign, πηγή: youtube, κόστος: **ΔΩΡΕΑΝ**
* [Go/Golang 28 - Iris framework : Templating](https://www.youtube.com/watch?v=nOKYV073S2Y) από stephgdesignn, πηγή: youtube, κόστος: **ΔΩΡΕΑΝ**
* [Go/Golang 29 - Iris framework : Paramètres](https://www.youtube.com/watch?v=K2FsprfXs1E) από stephgdesign, πηγή: youtube, κόστος: **ΔΩΡΕΑΝ**
* [Go/Golang 30 - Iris framework : Les middelwares](https://www.youtube.com/watch?v=BLPy1So6bhE) από stephgdesign, πηγή: youtube, κόστος: **ΔΩΡΕΑΝ**
* [Go/Golang 31 - Iris framework : Les sessions](https://www.youtube.com/watch?v=RnBwUrwgEZ8) από stephgdesign, πηγή: youtube, κόστος: **ΔΩΡΕΑΝ**

### Προσληφθείτε

Υπάρχουν πολλές νεοσύστατες εταιρείες που αναζητούν Go web developers με εμπειρία Iris ως απαίτηση, ψάχνουμε καθημερινά και δημοσιεύουμε αυτές τις πληροφορίες μέσω της [σελίδας μας στο facebook](https://www.facebook.com/iris.framework), κάντε like για να λαμβάνετε ειδοποιήσεις, έχουμε ήδη δημοσιεύσει ορισμένες από αυτές(τις θέσεις εργασίας).

## License

Το Iris διαθέτει άδεια βάσει του [3-Clause BSD License](LICENSE). Το Iris είναι 100% δωρεάν και  ανοιχτού κώδικα λογισμικό.

Για τυχόν ερωτήσεις σχετικά με την άδεια παρακαλώ στείλτε [e-mail](mailto:kataras2006@hotmail.com?subject=Iris%20License).
# Iris ウェブフレームワーク <a href="README.md"> <img width="20px" src="https://iris-go.com/images/flag-unitedkingdom.svg?v=10" /></a> <a href="README_ZH.md"> <img width="20px" src="https://iris-go.com/images/flag-china.svg?v=10" /></a> <a href="README_RU.md"><img width="20px" src="https://iris-go.com/images/flag-russia.svg?v=10" /></a> <a href="README_ID.md"> <img width="20px" src="https://iris-go.com/images/flag-indonesia.svg?v=10" /></a> <a href="README_GR.md"><img width="20px" src="https://iris-go.com/images/flag-greece.svg?v=10" /></a> <a href="README_PT_BR.md"><img width="20px" src="https://iris-go.com/images/flag-pt-br.svg?v=10" /></a>

<a href="https://iris-go.com"> <img align="right" width="169px" src="https://iris-go.com/images/icon.svg?v=a" title="logo created by @merry.dii" /> </a>

[![build status](https://img.shields.io/travis/kataras/iris/master.svg?style=flat-square)](https://travis-ci.org/kataras/iris)<!-- [![release](https://img.shields.io/github/release/kataras/iris.svg?style=flat-square)](https://github.com/kataras/iris/releases)--> [![report card](https://img.shields.io/badge/report%20card-a%2B-ff3333.svg?style=flat-square)](http://goreportcard.com/report/kataras/iris) [![vscode-iris](https://img.shields.io/badge/ext%20-vscode-0c77e3.svg?style=flat-square)](https://marketplace.visualstudio.com/items?itemName=kataras2006.iris)<!--[![github closed issues](https://img.shields.io/github/issues-closed-raw/kataras/iris.svg?style=flat-square)](https://github.com/kataras/iris/issues?q=is%3Aissue+is%3Aclosed)--> [![chat](https://img.shields.io/badge/community-%20chat-00BCD4.svg?style=flat-square)](https://kataras.rocket.chat/channel/iris) [![view examples](https://img.shields.io/badge/learn%20by-examples-0077b3.svg?style=flat-square)](https://iris-go.com/v10/recipe) [![release](https://img.shields.io/badge/release%20-v10.6-0077b3.svg?style=flat-square)](https://github.com/kataras/iris/releases)

Irisはシンプルで高速、それにも関わらず充実した機能を有する効率的なGo言語のウェブフレームワークです。

Irisは表現力豊かなウェブサイトやAPIの基礎構造をいとも簡単に提供します。

Go言語におけるExpressjsと言っても過言ではないでしょう。

[皆様の声](#支援)をご覧ください。このレポジトリを[Star](https://github.com/kataras/iris/stargazers)し、[最新情報](https://facebook.com/iris.framework)を受け取りましょう。

## 支援者

支援者の方々、ありがとうございます! 🙏 [支援者になる](https://iris-go.com/donate)

<a href="https://iris-go.com/donate" target="_blank"><img src="https://iris-go.com/backers.svg?v=2"/></a>

```sh
$ cat example.go
```

```go
package main

import "github.com/kataras/iris"

func main() {
    app := iris.New()
    // Load all templates from the "./views" folder
    // where extension is ".html" and parse them
    // using the standard `html/template` package.
    app.RegisterView(iris.HTML("./views", ".html"))

    // Method:    GET
    // Resource:  http://localhost:8080
    app.Get("/", func(ctx iris.Context) {
        // Bind: {{.message}} with "Hello world!"
        ctx.ViewData("message", "Hello world!")
        // Render template file: ./views/hello.html
        ctx.View("hello.html")
    })

    // Method:    GET
    // Resource:  http://localhost:8080/user/42
    //
    // Need to use a custom regexp instead?
    // Easy,
    // just mark the parameter's type to 'string'
    // which accepts anything and make use of
    // its `regexp` macro function, i.e:
    // app.Get("/user/{id:string regexp(^[0-9]+$)}")
    app.Get("/user/{id:long}", func(ctx iris.Context) {
        userID, _ := ctx.Params().GetInt64("id")
        ctx.Writef("User ID: %d", userID)
    })

    // Start the server using a network address.
    app.Run(iris.Addr(":8080"))
}
```

> [here](_examples/routing/dynamic-path/main.go#L31)をクリックしてパスパラメータについて学ぶ

```html
<!-- file: ./views/hello.html -->
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>{{.message}}</h1>
</body>
</html>
```

```sh
$ go run example.go
Now listening on: http://localhost:8080
Application Started. Press CTRL+C to shut down.
_
```

## インストール

[Go Programming Language](https://golang.org/dl/)をインストールしていることが唯一の前提条件です。

```sh
$ go get -u github.com/kataras/iris
```

Irisは[vendor directory](https://docs.google.com/document/d/1Bz5-UB7g2uPBdOx-rw5t9MxJwkfpx90cqG9AFL0JAYo)機能の利点を活かしています。これが上流レポジトリの変更や削除を防ぐため、再現可能なビルドを実現します。

[![Iris vs .NET Core(C#) vs Node.js (Express)](https://iris-go.com/images/benchmark-new-gray.png)](_benchmarks/README_UNIX.md)

_Updated at: [Tuesday, 21 November 2017](_benchmarks/README_UNIX.md)_

<details>
<summary>他のウェブフレームワークとの比較</summary>

![Comparison with other frameworks](https://raw.githubusercontent.com/smallnest/go-web-framework-benchmark/4db507a22c964c9bc9774c5b31afdc199a0fe8b7/benchmark.png)

</details>

## 支援

- [HISTORY](HISTORY.md#tu-05-june-2018--v1066)ファイルはあなたの友人です。このファイルには、機能に関する最新の情報や変更点が記載されています。
- バグを発見しましたか？[github issues](https://github.com/kataras/iris/issues)に投稿をお願い致します。
- 質問がありますか？または問題を即時に解決するため、熟練者に相談する必要がありますか？[community chat](https://chat.iris-go.com)に参加しましょう。
- [here](https://docs.google.com/forms/d/e/1FAIpQLSdCxZXPANg_xHWil4kVAdhmh7EBBHQZ_4_xSZVDL-oCC_z5pA/viewform?usp=sf_link)をクリックしてユーザーとしての体験を報告しましょう。
- フレームワークを愛していますか?それならばツイートしましょう!他の人はこのようにツイートしています:

<a href="https://twitter.com/gelnior/status/769100480706379776"> 
    <img src="https://comments.iris-go.com/comment27_mini.png" width="350px">
</a>

<a href="https://twitter.com/MeAlex07/status/822799954188075008"> 
    <img src="https://comments.iris-go.com/comment28_mini.png" width="350px">
</a>

<a href="https://twitter.com/_mgale/status/818591490305761280"> 
    <img src="https://comments.iris-go.com/comment29_mini.png" width="350px">
</a>
<a href="https://twitter.com/VeayoX/status/813273328550973440"> 
    <img src="https://comments.iris-go.com/comment30_mini.png" width="350px">
</a>

<a href="https://twitter.com/pvsukale/status/745328224876408832"> 
    <img src="https://comments.iris-go.com/comment31_mini.png" width="350px">
</a>

<a href="https://twitter.com/blainsmith/status/745338092211560453"> 
    <img src="https://comments.iris-go.com/comment32_mini.png" width="350px">
</a>

<a href="https://twitter.com/tjbyte/status/758287014210867200"> 
    <img src="https://comments.iris-go.com/comment33_mini.png" width="350px">
</a>

<a href="https://twitter.com/tangzero/status/751050577220698112"> 
    <img src="https://comments.iris-go.com/comment34_mini.png" width="350px">
</a>

<a href="https://twitter.com/tjbyte/status/758287244947972096"> 
    <img src="https://comments.iris-go.com/comment33_2_mini.png" width="350px">
</a>

<a href="https://twitter.com/ferarias/status/902468752364773376"> 
    <img src="https://comments.iris-go.com/comment41.png" width="350px">
</a>

<br/><br/>

Irisプロジェクトに貢献して頂ける方は、[CONTRIBUTING.md](CONTRIBUTING.md) をお読みください.

[全貢献者リスト](https://github.com/kataras/iris/graphs/contributors)

## 学習する

ウェブフレームワークで開発を行う時には、まず言語の基本を学ぶこと、標準的なhttpで何ができるのか知ることが重要です。あなたのアプリケーションが個人的なもので、とてもシンプル、パフォーマンスとメンテナンス性にそこまで拘らない場合、標準パッケージでの開発が推奨されます。以下のガイドラインを参照してください。

- **100+1** **[examples](_examples)** や[Irisスターターキット](#Irisスターターキット)を学習する
- より詳しく知るために[godocs](https://godoc.org/github.com/kataras/iris)を読む
- 一息ついて、私たちが発見した[記事](#記事)を読む

### Irisスターターキット

<!-- table form
| Description | Link |
| -----------|-------------|
| Hasura hub starter project with a ready to deploy golang helloworld webapp with IRIS! | https://hasura.io/hub/project/hasura/hello-golang-iris |
| A basic web app built in Iris for Go |https://github.com/gauravtiwari/go_iris_app |
| A mini social-network created with the awesome Iris💖💖 | https://github.com/iris-contrib/Iris-Mini-Social-Network |
| Iris isomorphic react/hot reloadable/redux/css-modules starter kit | https://github.com/iris-contrib/iris-starter-kit |
| Demo project with react using typescript and Iris | https://github.com/ionutvilie/react-ts |
| Self-hosted Localization Management Platform built with Iris and Angular | https://github.com/iris-contrib/parrot |
| Iris + Docker and Kubernetes | https://github.com/iris-contrib/cloud-native-go |
| Quickstart for Iris with Nanobox | https://guides.nanobox.io/golang/iris/from-scratch |
-->

1. [A basic web app built in Iris for Go](https://github.com/gauravtiwari/go_iris_app)
2. [A mini social-network created with the awesome Iris💖💖](https://github.com/iris-contrib/Iris-Mini-Social-Network)
3. [Iris isomorphic react/hot reloadable/redux/css-modules starter kit](https://github.com/iris-contrib/iris-starter-kit)
4. [Demo project with react using typescript and Iris](https://github.com/ionutvilie/react-ts)
5. [Self-hosted Localization Management Platform built with Iris and Angular](https://github.com/iris-contrib/parrot)
6. [Iris + Docker and Kubernetes](https://github.com/iris-contrib/cloud-native-go)
7. [Quickstart for Iris with Nanobox](https://guides.nanobox.io/golang/iris/from-scratch)
8. [A Hasura starter project with a ready to deploy Golang hello-world web app with IRIS](https://hasura.io/hub/project/hasura/hello-golang-iris)

> 似たようなものを開発しましたか？ [私たちにも教えてください！](https://github.com/kataras/iris/pulls)

### ミドルウェア

Irisはあなたのウェブアプリケーションにご使用いただけるハンドラー[[1]](middleware/)[[2]](https://github.com/iris-contrib/middleware)を多く有しています。さらに、[net/http](https://golang.org/pkg/net/http/)と互換性のある外部のミドルウェアもご使用いただけます。[examples/convert-handlers](_examples/convert-handlers)を参照してください。

Irisは他のフレームワークと異なり、標準パッケージと１００％互換性があります。故に、米国の有名なテレビ局を含め、大企業のの大半がGoをワークフローに取り入れています。Irisは常にGo言語の最新版リリースに対応し、Goの作成者によって開発されている標準的な`net/http`パッケージに沿っています。 

### 記事

* [A Todo MVC Application using Iris and Vue.js](https://hackernoon.com/a-todo-mvc-application-using-iris-and-vue-js-5019ff870064)
* [A Hasura starter project with a ready to deploy Golang hello-world web app with IRIS](https://bit.ly/2lmKaAZ)
* [Top 6 web frameworks for Go as of 2017](https://blog.usejournal.com/top-6-web-frameworks-for-go-as-of-2017-23270e059c4b)
* [Iris Go Framework + MongoDB](https://medium.com/go-language/iris-go-framework-mongodb-552e349eab9c)
* [How to build a file upload form using DropzoneJS and Go](https://hackernoon.com/how-to-build-a-file-upload-form-using-dropzonejs-and-go-8fb9f258a991)
* [How to display existing files on server using DropzoneJS and Go](https://hackernoon.com/how-to-display-existing-files-on-server-using-dropzonejs-and-go-53e24b57ba19)
* [Iris, a modular web framework](https://medium.com/@corebreaker/iris-web-cd684b4685c7)
* [Go vs .NET Core in terms of HTTP performance](https://medium.com/@kataras/go-vs-net-core-in-terms-of-http-performance-7535a61b67b8)
* [Iris Go vs .NET Core Kestrel in terms of HTTP performance](https://hackernoon.com/iris-go-vs-net-core-kestrel-in-terms-of-http-performance-806195dc93d5)
* [How to Turn an Android Device into a Web Server](https://twitter.com/ThePracticalDev/status/892022594031017988)
* [Deploying a Iris Golang app in hasura](https://medium.com/@HasuraHQ/deploy-an-iris-golang-app-with-backend-apis-in-minutes-25a559bf530b)
* [A URL Shortener Service using Go, Iris and Bolt](https://medium.com/@kataras/a-url-shortener-service-using-go-iris-and-bolt-4182f0b00ae7)

### 動画

* [Daily Coding - Web Framework Golang: Iris Framework]( https://www.youtube.com/watch?v=BmOLFQ29J3s) by WarnabiruTV, source: youtube, cost: **FREE**
* [Tutorial Golang MVC dengan Iris Framework & Mongo DB](https://www.youtube.com/watch?v=uXiNYhJqh2I&list=PLMrwI6jIZn-1tzskocnh1pptKhVmWdcbS) (19 parts so far) by Musobar Media, source: youtube, cost: **FREE**
* [Go/Golang 27 - Iris framework : Routage de base](https://www.youtube.com/watch?v=rQxRoN6ub78) by stephgdesign, source: youtube, cost: **FREE**
* [Go/Golang 28 - Iris framework : Templating](https://www.youtube.com/watch?v=nOKYV073S2Y) by stephgdesignn, source: youtube, cost: **FREE**
* [Go/Golang 29 - Iris framework : Paramètres](https://www.youtube.com/watch?v=K2FsprfXs1E) by stephgdesign, source: youtube, cost: **FREE**
* [Go/Golang 30 - Iris framework : Les middelwares](https://www.youtube.com/watch?v=BLPy1So6bhE) by stephgdesign, source: youtube, cost: **FREE**
* [Go/Golang 31 - Iris framework : Les sessions](https://www.youtube.com/watch?v=RnBwUrwgEZ8) by stephgdesign, source: youtube, cost: **FREE**

### 雇用

多くの企業やスタートアップがIrisの使用経験を有するGo言語開発者を探しています。私たちは募集情報を毎日検索し、[facebook page](https://www.facebook.com/iris.framework)に投稿しています。既に投稿されている情報をご覧ください。Likeを押して通知を受け取りましょう。

## ライセンス

Iris[3-Clause BSD License](LICENSE)に基いています。Irisは完全無料のオープンソースソフトウェアです。

ライセンスに関するご質問は[e-mail](mailto:kataras2006@hotmail.com?subject=Iris%20License)までご連絡ください。
# Iris Web Framework <a href="README.md"> <img width="20px" src="https://iris-go.com/images/flag-unitedkingdom.svg?v=10" /></a> <a href="README_ZH.md"> <img width="20px" src="https://iris-go.com/images/flag-china.svg?v=10" /></a> <a href="README_RU.md"><img width="20px" src="https://iris-go.com/images/flag-russia.svg?v=10" /></a> <a href="README_ID.md"> <img width="20px" src="https://iris-go.com/images/flag-indonesia.svg?v=10" /></a> <a href="README_GR.md"><img width="20px" src="https://iris-go.com/images/flag-greece.svg?v=10" /></a> <a href="README_JPN.md"><img width="20px" src="https://iris-go.com/images/flag-japan.svg?v=10" /></a>

<a href="https://iris-go.com"> <img align="right" width="169px" src="https://iris-go.com/images/icon.svg?v=a" title="logo created by @merry.dii" /> </a>

[![build status](https://img.shields.io/travis/kataras/iris/master.svg?style=flat-square)](https://travis-ci.org/kataras/iris)<!-- [![release](https://img.shields.io/github/release/kataras/iris.svg?style=flat-square)](https://github.com/kataras/iris/releases)--> [![report card](https://img.shields.io/badge/report%20card-a%2B-ff3333.svg?style=flat-square)](http://goreportcard.com/report/kataras/iris) [![vscode-iris](https://img.shields.io/badge/ext%20-vscode-0c77e3.svg?style=flat-square)](https://marketplace.visualstudio.com/items?itemName=kataras2006.iris)<!--[![github closed issues](https://img.shields.io/github/issues-closed-raw/kataras/iris.svg?style=flat-square)](https://github.com/kataras/iris/issues?q=is%3Aissue+is%3Aclosed)--> [![chat](https://img.shields.io/badge/community-%20chat-00BCD4.svg?style=flat-square)](https://kataras.rocket.chat/channel/iris) [![view examples](https://img.shields.io/badge/learn%20by-examples-0077b3.svg?style=flat-square)](https://iris-go.com/v10/recipe) [![release](https://img.shields.io/badge/release%20-v10.6-0077b3.svg?style=flat-square)](https://github.com/kataras/iris/releases)

Iris é um framework rápido, simples porém completo e muito eficiente para a linguagem Go.

Além disso, Iris proporciona uma base sólida que capricha na expressividade e facilidade de uso para seu próximo site ou API.

Por último, Iris é um framework equivalente ao expressjs no ecossistema da linguagem de programação Go.

Veja o que [as pessoas estão dizendo sobre o Iris](#support) e [deixe uma estrela](https://github.com/kataras/iris/stargazers) nesse repositório do github para se [manter atualizado](https://facebook.com/iris.framework).

## Apoiadores

Muito obrigado a todos que nos apoiam! 🙏 [Apoie a gente!](https://iris-go.com/donate)


<a href="https://iris-go.com/donate" target="_blank"><img src="https://iris-go.com/backers.svg?v=2"/></a>

```sh
$ cat example.go
```

```go
package main

import "github.com/kataras/iris"

func main() {
    app := iris.New()
    // Carrega todos os templates da pasta "./views"
    // cuja extensão é ".html" e parseie-os utilizando
    // a biblioteca `html/template`.
    app.RegisterView(iris.HTML("./views", ".html"))

    // Method:    GET
    // Resource:  http://localhost:8080
    app.Get("/", func(ctx iris.Context) {
        // Associa {{.message}} a "Hello world!"
        ctx.ViewData("message", "Hello world!")
        // Renderiza o template: ./views/hello.html
        ctx.View("hello.html")
    })

    // Method:    GET
    // Resource:  http://localhost:8080/user/42
    //
    // Deseja utilizar uma expressão regular ?
    // É fácil,
    // é só marcar o type to parametro como 'string'
    // e utilizar sua macro `regexp`, i.e:
    // app.Get("/user/{id:string regexp(^[0-9]+$)}")
    app.Get("/user/{id:long}", func(ctx iris.Context) {
        userID, _ := ctx.Params().GetInt64("id")
        ctx.Writef("User ID: %d", userID)
    })

    // Inicializa o servidor utilizando um endereço de rede.
    app.Run(iris.Addr(":8080"))
}
```

> Aprenda mais sobre tipos dos parametros da URI clicando [aqui](_examples/routing/dynamic-path/main.go#L31)

```html
<!-- arquivo: ./views/hello.html -->
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>{{.message}}</h1>
</body>
</html>
```

```sh
$ go run example.go
Now listening on: http://localhost:8080
Application Started. Press CTRL+C to shut down.
_
```

## Instalação

O único pré requisito é a [Linguagem de Programação GO](https://golang.org/dl/)

```sh
$ go get -u github.com/kataras/iris
```

Iris lança mão da [pasta vendor](https://docs.google.com/document/d/1Bz5-UB7g2uPBdOx-rw5t9MxJwkfpx90cqG9AFL0JAYo). Dessa forma você conseguirá obter builds reprodutíveis já que esse método impede que nomes no branch upstream sejam renomeados ou deletados.

[![Iris vs .NET Core(C#) vs Node.js (Express)](https://iris-go.com/images/benchmark-new-gray.png)](_benchmarks/README_UNIX.md)

_Atualizado em : [Terça, 21 de Novembro de 2017](_benchmarks/README_UNIX.md)_

<details>
<summary>Benchmarks de fonte third-party acerca dos frameworks web</summary>

![Comparison with other frameworks](https://raw.githubusercontent.com/smallnest/go-web-framework-benchmark/4db507a22c964c9bc9774c5b31afdc199a0fe8b7/benchmark.png)

</details>

## Apoie

- [HISTORY](HISTORY.md#tu-05-june-2018--v1066) o arquivo HISTORY é o seu melhor amigo, ele contém informações sobre as últimas features e mudanças.
- Econtrou algum bug ? Poste-o nas [issues](https://github.com/kataras/iris/issues)
- Possui alguma dúvida ou gostaria de falar com alguém experiente para resolver seu problema em tempo real ? Junte-se ao [chat da nossa comunidade](https://chat.iris-go.com).
- Complete nosso formulário de experiência do usuário clicando [aqui](https://docs.google.com/forms/d/e/1FAIpQLSdCxZXPANg_xHWil4kVAdhmh7EBBHQZ_4_xSZVDL-oCC_z5pA/viewform?usp=sf_link)
- Gostou do framework ? Deixe um Tweet sobre ele! Veja o que os outros já disseram:

<a href="https://twitter.com/gelnior/status/769100480706379776"> 
    <img src="https://comments.iris-go.com/comment27_mini.png" width="350px">
</a>

<a href="https://twitter.com/MeAlex07/status/822799954188075008"> 
    <img src="https://comments.iris-go.com/comment28_mini.png" width="350px">
</a>

<a href="https://twitter.com/_mgale/status/818591490305761280"> 
    <img src="https://comments.iris-go.com/comment29_mini.png" width="350px">
</a>
<a href="https://twitter.com/VeayoX/status/813273328550973440"> 
    <img src="https://comments.iris-go.com/comment30_mini.png" width="350px">
</a>

<a href="https://twitter.com/pvsukale/status/745328224876408832"> 
    <img src="https://comments.iris-go.com/comment31_mini.png" width="350px">
</a>

<a href="https://twitter.com/blainsmith/status/745338092211560453"> 
    <img src="https://comments.iris-go.com/comment32_mini.png" width="350px">
</a>

<a href="https://twitter.com/tjbyte/status/758287014210867200"> 
    <img src="https://comments.iris-go.com/comment33_mini.png" width="350px">
</a>

<a href="https://twitter.com/tangzero/status/751050577220698112"> 
    <img src="https://comments.iris-go.com/comment34_mini.png" width="350px">
</a>

<a href="https://twitter.com/tjbyte/status/758287244947972096"> 
    <img src="https://comments.iris-go.com/comment33_2_mini.png" width="350px">
</a>

<a href="https://twitter.com/ferarias/status/902468752364773376"> 
    <img src="https://comments.iris-go.com/comment41.png" width="350px">
</a>

<br/><br/>

Para mais informações sobre como contribuir para o projeto Iris leia por favor o arquivo [CONTRIBUTING.md](CONTRIBUTING.md).

[Lista de todos os Contribuintes](https://github.com/kataras/iris/graphs/contributors)

## Aprenda

Primeiramente, a melhor maneira de começar a aprender um framework é
aprender os fundamentos da linguagem de programação em questão e
as funções principais da biblioteca `http`, se seu app é um projeto
pessoal muito simples que exija performance e manutenção contínua
é provável que você consiga seguir adiante apenas com a biblioteca
padrão. Feito isso, você pode seguir as seguintes diretrizes:

- Navegue por **100+1** **[exemplos](_examples)** e os [iris starter kits](#iris-starter-kits) que criamos para você
- Leia os [godocs](https://godoc.org/github.com/kataras/iris) para mais detalhes
- Prepare um chá ou cafezinho, ou o que lhe for mais conveniente, e leia alguns [artigos](#articles) que achamos para você

### Iris starter kits

<!-- table form 
| Description | Link |
| -----------|-------------|
| Hasura hub starter project with a ready to deploy golang helloworld webapp with IRIS! | https://hasura.io/hub/project/hasura/hello-golang-iris |
| Web app básico utilizando o Iris |https://github.com/gauravtiwari/go_iris_app |
| Uma mini rede social criada com o incrível Iris💖💖 | https://github.com/iris-contrib/Iris-Mini-Social-Network |
| Iris isomorphic react/hot reloadable/redux/css-modules starter kit | https://github.com/iris-contrib/iris-starter-kit |
| Projeto demo usando react com typescript e Iris | https://github.com/ionutvilie/react-ts |
| Plataforma de Gerenciamento de Localização auto hospedada criada com Iris e Angular | https://github.com/iris-contrib/parrot |
| Iris + Docker e Kubernetes | https://github.com/iris-contrib/cloud-native-go |
| Quickstart do Iris com Nanobox | https://guides.nanobox.io/golang/iris/from-scratch |
-->

1. [Web app básico utilizando o Iris](https://github.com/gauravtiwari/go_iris_app)
2. [Uma mini rede social criada com o incrível Iris💖💖] (https://github.com/iris-contrib/Iris-Mini-Social-Network)
3. [Iris isomorphic react/hot reloadable/redux/css-modules starter kit](https://github.com/iris-contrib/iris-starter-kit)
4. [Projeto demo usando react com typescript e Iris](https://github.com/ionutvilie/react-ts)
5. [Plataforma de Gerenciamento de Localização auto hospedada criada com Iris e Angular](https://github.com/iris-contrib/parrot)
6. [Iris + Docker e Kubernetes](https://github.com/iris-contrib/cloud-native-go)
7. [Quickstart do Iris com Nanobox](https://guides.nanobox.io/golang/iris/from-scratch)
8. [Um projeto Hasura para iniciantes pronto para o deply com um app Golang hello-world utilizando o IRIS](https://hasura.io/hub/project/hasura/hello-golang-iris)

> Voce criou algo parecido ? [Informe-nos](https://github.com/kataras/iris/pulls)!

### Middleware

Iris tem uma ótima coleção de handlers[[1]](middleware/)[[2]](https://github.com/iris-contrib/middleware) os quais você pode utilizar lado a lado com seus web apps. Entretanto, você não esta limitado a eles - você pode utilizar qualquer middleware de terceiros desde que seja compatível com a biblioteca [net/http](https://golang.org/pkg/net/http/), [_examples/convert-handlers](_examples/convert-handlers) é um exemplo que pode ser tomado como base para tal.

Iris, ao contrário dos demais, é 100% compatível com os padrões e esse é o motivo pelo qual a maioria das grandes empresas que inserem Go em seu fluxo operacional, tal qual a famosa US Television Network, usam e confiam no Iris; Ele é atualizado com frequencia e sempre estará alinhado com o padrão da biblioteca `net/http` que é periodicamente modernizada pelos autores da linguagem Go a cada novo release.

### Artigos

* [Um aplicação Todo utilizando Iris e Vue.js](https://hackernoon.com/a-todo-mvc-application-using-iris-and-vue-js-5019ff870064)
* [Um projeto Hasura para iniciantes pronto para o deply com um app Golang hello-world utilizando o IRIS](https://bit.ly/2lmKaAZ)
* [Top 6 frameworks web do Go em 2017](https://blog.usejournal.com/top-6-web-frameworks-for-go-as-of-2017-23270e059c4b)
* [Framework Iris + MongoDB](https://medium.com/go-language/iris-go-framework-mongodb-552e349eab9c)
* [Como criar um formulário de upload de arquivos com DropzoneJS e Go](https://hackernoon.com/how-to-build-a-file-upload-form-using-dropzonejs-and-go-8fb9f258a991)
* [Como mostrar arquivos existentes no servidor utilizando DropzoneJS e Go](https://hackernoon.com/how-to-display-existing-files-on-server-using-dropzonejs-and-go-53e24b57ba19)
* [Iris,um web framework modular](https://medium.com/@corebreaker/iris-web-cd684b4685c7)
* [Go vs .NET Core em termos de performance HTTP](https://medium.com/@kataras/go-vs-net-core-in-terms-of-http-performance-7535a61b67b8)
* [Iris Go vs .NET Core Kestrel em termos de performance HTTP](https://hackernoon.com/iris-go-vs-net-core-kestrel-in-terms-of-http-performance-806195dc93d5)
* [Como transformar um aparelho Android em um servidor web](https://twitter.com/ThePracticalDev/status/892022594031017988)
* [Fazendo Deploy de um app Iris na hasura](https://medium.com/@HasuraHQ/deploy-an-iris-golang-app-with-backend-apis-in-minutes-25a559bf530b)
* [Um serviço encurtador de URL utilizando Go, Iris e Bolt](https://medium.com/@kataras/a-url-shortener-service-using-go-iris-and-bolt-4182f0b00ae7)

### Video Aulas

* [Daily Coding - Web Framework Golang: Iris Framework]( https://www.youtube.com/watch?v=BmOLFQ29J3s) por WarnabiruTV, fonte: youtube, custo: **GRATUITO**
* [Tutorial Golang MVC dengan Iris Framework & Mongo DB](https://www.youtube.com/watch?v=uXiNYhJqh2I&list=PLMrwI6jIZn-1tzskocnh1pptKhVmWdcbS) (19 ate o momento) por Musobar Media, fonte: youtube, custo: **GRATUITO**
* [Go/Golang 27 - Iris framework : Routage de base](https://www.youtube.com/watch?v=rQxRoN6ub78) por stephgdesign, fonte: youtube, custo: **GRATUITO**
* [Go/Golang 28 - Iris framework : Templating](https://www.youtube.com/watch?v=nOKYV073S2Y) por stephgdesignn, fonte: youtube, custo: **GRATUITO**
* [Go/Golang 29 - Iris framework : Paramètres](https://www.youtube.com/watch?v=K2FsprfXs1E) por stephgdesign, fonte: youtube, custo: **GRATUITO**
* [Go/Golang 30 - Iris framework : Les middelwares](https://www.youtube.com/watch?v=BLPy1So6bhE) por stephgdesign, fonte: youtube, custo: **GRATUITO**
* [Go/Golang 31 - Iris framework : Les sessions](https://www.youtube.com/watch?v=RnBwUrwgEZ8) por stephgdesign, fonte: youtube, custo: **GRATUITO**

### Seja contratado

Várias empresas e start-ups estão procurando por desenvolvedores web que sabem Go e possuam experiência com Iris como pré requisito, todos os dias estamos procurando informações sobre empregos e postando na nossa [página do facebook](https://www.facebook.com/iris.framework), de um like na página para ser notificado.

## Licença

Iris é licenciado sob a [Licença 3-Clause BSD](LICENSE). Iris é um software 100% gratuito e open-source.

Caso haja quaisquer dúvidas em relação a licença favor enviar um [e-mail](mailto:kataras2006@hotmail.com?subject=Iris%20License).
# Iris Web Framework <a href="README.md"> <img width="20px" src="https://iris-go.com/images/flag-unitedkingdom.svg?v=10" /></a> <a href="README_ZH.md"><img width="20px" src="https://iris-go.com/images/flag-china.svg?v=10" /></a> <a href="README_ID.md"> <img width="20px" src="https://iris-go.com/images/flag-indonesia.svg?v=10" /></a> <a href="README_GR.md"><img width="20px" src="https://iris-go.com/images/flag-greece.svg?v=10" /></a> <a href="README_PT_BR.md"><img width="20px" src="https://iris-go.com/images/flag-pt-br.svg?v=10" /></a> <a href="README_JPN.md"><img width="20px" src="https://iris-go.com/images/flag-japan.svg?v=10" /></a>

<a href="https://iris-go.com"> <img align="right" width="169px" src="https://iris-go.com/images/icon.svg?v=a" title="logo created by @merry.dii" /> </a>

[![build status](https://img.shields.io/travis/kataras/iris/master.svg?style=flat-square)](https://travis-ci.org/kataras/iris)<!-- [![release](https://img.shields.io/github/release/kataras/iris.svg?style=flat-square)](https://github.com/kataras/iris/releases)--> [![report card](https://img.shields.io/badge/report%20card-a%2B-ff3333.svg?style=flat-square)](http://goreportcard.com/report/kataras/iris) [![vscode-iris](https://img.shields.io/badge/ext%20-vscode-0c77e3.svg?style=flat-square)](https://marketplace.visualstudio.com/items?itemName=kataras2006.iris)<!--[![github closed issues](https://img.shields.io/github/issues-closed-raw/kataras/iris.svg?style=flat-square)](https://github.com/kataras/iris/issues?q=is%3Aissue+is%3Aclosed)--> [![chat](https://img.shields.io/badge/community-%20chat-00BCD4.svg?style=flat-square)](https://kataras.rocket.chat/channel/iris) [![view examples](https://img.shields.io/badge/learn%20by-examples-0077b3.svg?style=flat-square)](https://iris-go.com/v10/recipe) [![release](https://img.shields.io/badge/release%20-v10.6-0077b3.svg?style=flat-square)](https://github.com/kataras/iris/releases)

Iris - это быстрая, простая, но полнофункциональная и очень эффективная веб-платформа для Go.

Iris предоставляет красиво выразительную и удобную основу для вашего следующего веб-сайта или API.

Наконец, настоящий эквивалент expressjs для языка программирования Go.

Узнайте, что [другие говорят об Iris](#support), и [запустите](https://github.com/kataras/iris/stargazers) этот github-хранилище, чтобы оставаться в курсе последних событий [актуальными](https://facebook.com/iris.framework).

## Сторонники

Спасибо всем, кто поддерживал нас! 🙏 [Поддержать нас](https://iris-go.com/donate)

<a href="https://iris-go.com/donate" target="_blank"><img src="https://iris-go.com/backers.svg?v=2"/></a>

```sh
$ cat example.go
```

```go
package main

import "github.com/kataras/iris"

func main() {
    app := iris.New()
    // Load all templates from the "./views" folder
    // where extension is ".html" and parse them
    // using the standard `html/template` package.
    app.RegisterView(iris.HTML("./views", ".html"))

    // Method:    GET
    // Resource:  http://localhost:8080
    app.Get("/", func(ctx iris.Context) {
        // Bind: {{.message}} with "Hello world!"
        ctx.ViewData("message", "Hello world!")
        // Render template file: ./views/hello.html
        ctx.View("hello.html")
    })

    // Method:    GET
    // Resource:  http://localhost:8080/user/42
    //
    // Need to use a custom regexp instead?
    // Easy,
    // just mark the parameter's type to 'string'
    // which accepts anything and make use of
    // its `regexp` macro function, i.e:
    // app.Get("/user/{id:string regexp(^[0-9]+$)}")
    app.Get("/user/{id:long}", func(ctx iris.Context) {
        userID, _ := ctx.Params().GetInt64("id")
        ctx.Writef("User ID: %d", userID)
    })

    // Start the server using a network address.
    app.Run(iris.Addr(":8080"))
}
```

> Чтобы узнать подробнее о типах пути параметров нажмите [здесь](_examples/routing/dynamic-path/main.go#L31)

```html
<!-- file: ./views/hello.html -->
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>{{.message}}</h1>
</body>
</html>
```

```sh
$ go run example.go
Now listening on: http://localhost:8080
Application Started. Press CTRL+C to shut down.
_
```

## Установка

Единственное требование [язык программирования Go.](https://golang.org/dl/)

```sh
$ go get -u github.com/kataras/iris
```

Iris использует преимущества функции  [из каталога поставщика](https://docs.google.com/document/d/1Bz5-UB7g2uPBdOx-rw5t9MxJwkfpx90cqG9AFL0JAYo). Вы получаете действительно воспроизводимые конструкции, так как этот метод защищает от восходящего потока переименований и удалений.

[![Iris vs .NET Core(C#) vs Node.js (Express)](https://iris-go.com/images/benchmark-new-gray.png)](_benchmarks/README_UNIX.md)

_Обновлено: [Вторник, 21 ноября 2017 г.](_benchmarks/README_UNIX.md)_

<details>
<summary>Сравнительные тесты сторонних источников по остальным веб-фреймворкам</summary>

![Comparison with other frameworks](https://raw.githubusercontent.com/smallnest/go-web-framework-benchmark/4db507a22c964c9bc9774c5b31afdc199a0fe8b7/benchmark.png)

</details>

## Поддержка

- Файл [HISTORY](HISTORY.md#tu-05-june-2018--v1066) - ваш лучший друг, он содержит информацию о последних особенностях и всех изменениях
- Вы случайно обнаружили ошибку? Опубликуйте ее на [Github вопросы](https://github.com/kataras/iris/issues)
- У Вас есть какие-либо вопросы или Вам нужно поговорить с кем-то, кто бы смог решить Вашу проблему в режиме реального времени? Присоединяйтесь к нам в [чате сообщества](https://chat.iris-go.com)
- Заполните наш отчет о пользовательском опыте на основе формы, нажав [здесь](https://docs.google.com/forms/d/e/1FAIpQLSdCxZXPANg_xHWil4kVAdhmh7EBBHQZ_4_xSZVDL-oCC_z5pA/viewform?usp=sf_link) 
- Вам нравится фреймворк? Поделись об этом в Twitter! Люди говорят:

<a href="https://twitter.com/gelnior/status/769100480706379776"> 
    <img src="https://comments.iris-go.com/comment27_mini.png" width="350px">
</a>

<a href="https://twitter.com/MeAlex07/status/822799954188075008"> 
    <img src="https://comments.iris-go.com/comment28_mini.png" width="350px">
</a>

<a href="https://twitter.com/_mgale/status/818591490305761280"> 
    <img src="https://comments.iris-go.com/comment29_mini.png" width="350px">
</a>
<a href="https://twitter.com/VeayoX/status/813273328550973440"> 
    <img src="https://comments.iris-go.com/comment30_mini.png" width="350px">
</a>

<a href="https://twitter.com/pvsukale/status/745328224876408832"> 
    <img src="https://comments.iris-go.com/comment31_mini.png" width="350px">
</a>

<a href="https://twitter.com/blainsmith/status/745338092211560453"> 
    <img src="https://comments.iris-go.com/comment32_mini.png" width="350px">
</a>

<a href="https://twitter.com/tjbyte/status/758287014210867200"> 
    <img src="https://comments.iris-go.com/comment33_mini.png" width="350px">
</a>

<a href="https://twitter.com/tangzero/status/751050577220698112"> 
    <img src="https://comments.iris-go.com/comment34_mini.png" width="350px">
</a>

<a href="https://twitter.com/tjbyte/status/758287244947972096"> 
    <img src="https://comments.iris-go.com/comment33_2_mini.png" width="350px">
</a>

<a href="https://twitter.com/ferarias/status/902468752364773376"> 
    <img src="https://comments.iris-go.com/comment41.png" width="350px">
</a>

<br/><br/>

Для получения дополнительной информации о внесении вклада в проект Iris, пожалуйста, проверьте файл  [CONTRIBUTING.md](CONTRIBUTING.md).

[Список всех участников](https://github.com/kataras/iris/graphs/contributors)

## Учить

Прежде всего, самый правильный способ начать работу с веб-фрэймворк - изучить основы языка программирования и стандартные возможности `http`. Если Ваше веб-приложение представляет собой очень простой персональный проект без производительности и требований к техническому обслуживанию, тогда Вы возможно захотите развиваться просто со стандартным пакетом. После этого следуйте рекомендациям:

- Пройдитесь по **100+1** **[примерам](_examples)** и по некоторым [ стартовым Iris наборам](#iris-starter-kits), которые мы создали для вас
- Прочтите [godocs](https://godoc.org/github.com/kataras/iris) для любых подробностей
- Приготовьте чашечку кофе или чая, что вам больше нравится, и ознакомьтесь с некоторыми  [статьями](#articles), которые мы нашли для вас 

### Стартовые наборы IRIS:

<!-- table form 
| Description | Link |
| -----------|-------------|
| Hasura hub starter project with a ready to deploy golang helloworld webapp with IRIS! | https://hasura.io/hub/project/hasura/hello-golang-iris |
| A basic web app built in Iris for Go |https://github.com/gauravtiwari/go_iris_app |
| A mini social-network created with the awesome Iris💖💖 | https://github.com/iris-contrib/Iris-Mini-Social-Network |
| Iris isomorphic react/hot reloadable/redux/css-modules starter kit | https://github.com/iris-contrib/iris-starter-kit |
| Demo project with react using typescript and Iris | https://github.com/ionutvilie/react-ts |
| Self-hosted Localization Management Platform built with Iris and Angular | https://github.com/iris-contrib/parrot |
| Iris + Docker and Kubernetes | https://github.com/iris-contrib/cloud-native-go |
| Quickstart for Iris with Nanobox | https://guides.nanobox.io/golang/iris/from-scratch |
-->

1. [Основное веб-приложение, созданное в Iris for Go](https://github.com/gauravtiwari/go_iris_app)
2. [Мини-социальная сеть, созданная с удивительным Iris💖💖](https://github.com/iris-contrib/Iris-Mini-Social-Network)
3. [Iris isomorphic react/hot reloadable/redux/css-modules starter kit](https://github.com/iris-contrib/iris-starter-kit)
4. [Демо-проект с реакцией на использованием машинописного текста и Iris](https://github.com/ionutvilie/react-ts)
5. [Самостоятельная платформа управления локализацией, построенная с помощью Iris и Angular](https://github.com/iris-contrib/parrot)
6. [Iris + Docker and Kubernetes](https://github.com/iris-contrib/cloud-native-go)
7. [Быстрый запуск для Iris с Nanobox](https://guides.nanobox.io/golang/iris/from-scratch)
8. [Cтартовый проект Hasura с готовностью применять веб-приложение Golang hello-world с IRIS](https://hasura.io/hub/project/hasura/hello-golang-iris)

> Вы построили что-то подобное? Дайте нам [знать](https://github.com/kataras/iris/pulls)!

### Связующее программное обеспечение

У Iris есть отличный сбор обработчиков[[1]](middleware/)[[2]](https://github.com/iris-contrib/middleware) которые вы можете использовать бок о бок с вашими веб-приложениями. Однако вы не ограничены ими - вы можете использовать стороннее программное обеспечение, совместимое с [net/http](https://golang.org/pkg/net/http/) пакетом, [_examples/convert-handlers](_examples/convert-handlers) покажут вам путь.

Iris, в отличие от других, на 100% совместим со стандартами, и именно поэтому большинство крупных компаний, которые адаптируют Go к своему рабочему процессу, как и очень известная телевизионная сеть США, доверяют Iris; это всегда актуально, и он будет приведен в соответствии с пакетом - `net/http`, который будет модернизирован Автором Go при каждом новом выпуске языка программирования Go навсегда.

### Статьи

* [Приложение Todo MVC с использованием Iris и Vue.js](https://hackernoon.com/a-todo-mvc-application-using-iris-and-vue-js-5019ff870064)
* [Стартовый проект Hasura с готовностью применять веб-приложение Golang hello-world с IRIS](bit.ly/2lmKaAZ)
* [Топ-6 веб-фреймворков для Go на 2017 год
](https://blog.usejournal.com/top-6-web-frameworks-for-go-as-of-2017-23270e059c4b)
* [Iris Go Framework + MongoDB](https://medium.com/go-language/iris-go-framework-mongodb-552e349eab9c)
* [Как создать форму загрузки файла с помощью DropzoneJS и Go](https://hackernoon.com/how-to-build-a-file-upload-form-using-dropzonejs-and-go-8fb9f258a991)
* [Как отображать существующие файлы на сервере с помощью DropzoneJS и Go](https://hackernoon.com/how-to-display-existing-files-on-server-using-dropzonejs-and-go-53e24b57ba19)
* [ Iris, модульная структура сети](https://medium.com/@corebreaker/iris-web-cd684b4685c7)
* [ Go vs .NET Core с точки зрения производительности HTTP](https://medium.com/@kataras/go-vs-net-core-in-terms-of-http-performance-7535a61b67b8)
* [ Iris Go vs .NET Core Kestrel с точки зрения производительности HTTP
](https://hackernoon.com/iris-go-vs-net-core-kestrel-in-terms-of-http-performance-806195dc93d5)
* [Как превратить Android-устройство в веб-сервер](https://twitter.com/ThePracticalDev/status/892022594031017988)
* [Применение приложения Iris Golang на Hasura](https://medium.com/@HasuraHQ/deploy-an-iris-golang-app-with-backend-apis-in-minutes-25a559bf530b)
* [URL-адрес Shortener Service с помощью Go, Iris и Bolt](https://medium.com/@kataras/a-url-shortener-service-using-go-iris-and-bolt-4182f0b00ae7)

### Video Courses

* [Daily Coding - Web Framework Golang: Iris Framework]( https://www.youtube.com/watch?v=BmOLFQ29J3s) by WarnabiruTV, source: youtube, cost: **FREE**
* [Tutorial Golang MVC dengan Iris Framework & Mongo DB](https://www.youtube.com/watch?v=uXiNYhJqh2I&list=PLMrwI6jIZn-1tzskocnh1pptKhVmWdcbS) (19 parts so far) by Musobar Media, source: youtube, cost: **FREE**
* [Go/Golang 27 - Iris framework : Routage de base](https://www.youtube.com/watch?v=rQxRoN6ub78) by stephgdesign, source: youtube, cost: **FREE**
* [Go/Golang 28 - Iris framework : Templating](https://www.youtube.com/watch?v=nOKYV073S2Y) by stephgdesignn, source: youtube, cost: **FREE**
* [Go/Golang 29 - Iris framework : Paramètres](https://www.youtube.com/watch?v=K2FsprfXs1E) by stephgdesign, source: youtube, cost: **FREE**
* [Go/Golang 30 - Iris framework : Les middelwares](https://www.youtube.com/watch?v=BLPy1So6bhE) by stephgdesign, source: youtube, cost: **FREE**
* [Go/Golang 31 - Iris framework : Les sessions](https://www.youtube.com/watch?v=RnBwUrwgEZ8) by stephgdesign, source: youtube, cost: **FREE**

### Получить работу

Есть много компаний и стартапов, находящиеся в поисках Go веб-разработчиков с опытом работы с Iris как в качестве требования, которые мы подыскиваем для вас каждый день. Мы публикуем эту информацию на нашей [странице в Facebook](https://www.facebook.com/iris.framework). Ставьте Like, чтобы получите уведомления. Мы уже опубликовали некоторые из них.

## Лицензия

Iris лицензируется в соответствии с  [BSD 3-Clause лицензией](LICENSE). Iris - это бесплатное программное обеспечение с открытым исходным кодом на 100%.

По любым вопросам, касающимся лицензии, отправьте письмо на [почту](mailto:kataras2006@hotmail.com?subject=Iris%20License).
# Iris Web Framework <a href="README_ZH.md"> <img width="20px" src="https://iris-go.com/images/flag-china.svg?v=10" /></a> <a href="README_RU.md"><img width="20px" src="https://iris-go.com/images/flag-russia.svg?v=10" /></a> <a href="README_ID.md"> <img width="20px" src="https://iris-go.com/images/flag-indonesia.svg?v=10" /></a> <a href="README_GR.md"><img width="20px" src="https://iris-go.com/images/flag-greece.svg?v=10" /></a> <a href="README_PT_BR.md"><img width="20px" src="https://iris-go.com/images/flag-pt-br.svg?v=10" /></a> <a href="README_JPN.md"><img width="20px" src="https://iris-go.com/images/flag-japan.svg?v=10" /></a>

<a href="https://iris-go.com"> <img align="right" width="169px" src="https://iris-go.com/images/icon.svg?v=a" title="logo created by @merry.dii" /> </a>

[![build status](https://img.shields.io/travis/kataras/iris/master.svg?style=flat-square)](https://travis-ci.org/kataras/iris)<!-- [![release](https://img.shields.io/github/release/kataras/iris.svg?style=flat-square)](https://github.com/kataras/iris/releases)--> [![report card](https://img.shields.io/badge/report%20card-a%2B-ff3333.svg?style=flat-square)](http://goreportcard.com/report/kataras/iris) [![vscode-iris](https://img.shields.io/badge/ext%20-vscode-0c77e3.svg?style=flat-square)](https://marketplace.visualstudio.com/items?itemName=kataras2006.iris)<!--[![github closed issues](https://img.shields.io/github/issues-closed-raw/kataras/iris.svg?style=flat-square)](https://github.com/kataras/iris/issues?q=is%3Aissue+is%3Aclosed)--> [![chat](https://img.shields.io/badge/community-%20chat-00BCD4.svg?style=flat-square)](https://kataras.rocket.chat/channel/iris) [![view examples](https://img.shields.io/badge/learn%20by-examples-0077b3.svg?style=flat-square)](https://iris-go.com/v10/recipe) [![release](https://img.shields.io/badge/release%20-v10.6-0077b3.svg?style=flat-square)](https://github.com/kataras/iris/releases)

Iris is a fast, simple yet fully featured and very efficient web framework for Go.

Iris provides a beautifully expressive and easy to use foundation for your next website or API.

Finally, a real expressjs equivalent for the Go Programming Language.

Learn what [others say about Iris](#support) and [star](https://github.com/kataras/iris/stargazers) this github repository to stay [up to date](https://facebook.com/iris.framework).

## Backers

Thank you to all our backers! 🙏 [Become a backer](https://iris-go.com/donate)

<a href="https://iris-go.com/donate" target="_blank"><img src="https://iris-go.com/backers.svg?v=2"/></a>

```sh
$ cat example.go
```

```go
package main

import "github.com/kataras/iris"

func main() {
    app := iris.New()
    // Load all templates from the "./views" folder
    // where extension is ".html" and parse them
    // using the standard `html/template` package.
    app.RegisterView(iris.HTML("./views", ".html"))

    // Method:    GET
    // Resource:  http://localhost:8080
    app.Get("/", func(ctx iris.Context) {
        // Bind: {{.message}} with "Hello world!"
        ctx.ViewData("message", "Hello world!")
        // Render template file: ./views/hello.html
        ctx.View("hello.html")
    })

    // Method:    GET
    // Resource:  http://localhost:8080/user/42
    //
    // Need to use a custom regexp instead?
    // Easy,
    // just mark the parameter's type to 'string'
    // which accepts anything and make use of
    // its `regexp` macro function, i.e:
    // app.Get("/user/{id:string regexp(^[0-9]+$)}")
    app.Get("/user/{id:long}", func(ctx iris.Context) {
        userID, _ := ctx.Params().GetInt64("id")
        ctx.Writef("User ID: %d", userID)
    })

    // Start the server using a network address.
    app.Run(iris.Addr(":8080"))
}
```

> Learn more about path parameter's types by clicking [here](_examples/routing/dynamic-path/main.go#L31)

```html
<!-- file: ./views/hello.html -->
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>{{.message}}</h1>
</body>
</html>
```

```sh
$ go run example.go
Now listening on: http://localhost:8080
Application Started. Press CTRL+C to shut down.
_
```

## Installation

The only requirement is the [Go Programming Language](https://golang.org/dl/)

```sh
$ go get -u github.com/kataras/iris
```

Iris takes advantage of the [vendor directory](https://docs.google.com/document/d/1Bz5-UB7g2uPBdOx-rw5t9MxJwkfpx90cqG9AFL0JAYo) feature. You get truly reproducible builds, as this method guards against upstream renames and deletes.

[![Iris vs .NET Core(C#) vs Node.js (Express)](https://iris-go.com/images/benchmark-new-gray.png)](_benchmarks/README_UNIX.md)

_Updated at: [Tuesday, 21 November 2017](_benchmarks/README_UNIX.md)_

<details>
<summary>Benchmarks from third-party source over the rest web frameworks</summary>

![Comparison with other frameworks](https://raw.githubusercontent.com/smallnest/go-web-framework-benchmark/4db507a22c964c9bc9774c5b31afdc199a0fe8b7/benchmark.png)

</details>

## Support

- [HISTORY](HISTORY.md#tu-05-june-2018--v1066) file is your best friend, it contains information about the latest features and changes
- Did you happen to find a bug? Post it at [github issues](https://github.com/kataras/iris/issues)
- Do you have any questions or need to speak with someone experienced to solve a problem at real-time? Join us to the [community chat](https://chat.iris-go.com)
- Complete our form-based user experience report by clicking [here](https://docs.google.com/forms/d/e/1FAIpQLSdCxZXPANg_xHWil4kVAdhmh7EBBHQZ_4_xSZVDL-oCC_z5pA/viewform?usp=sf_link)
- Do you like the framework? Tweet something about it! The People have spoken:

<a href="https://twitter.com/gelnior/status/769100480706379776"> 
    <img src="https://comments.iris-go.com/comment27_mini.png" width="350px">
</a>

<a href="https://twitter.com/MeAlex07/status/822799954188075008"> 
    <img src="https://comments.iris-go.com/comment28_mini.png" width="350px">
</a>

<a href="https://twitter.com/_mgale/status/818591490305761280"> 
    <img src="https://comments.iris-go.com/comment29_mini.png" width="350px">
</a>
<a href="https://twitter.com/VeayoX/status/813273328550973440"> 
    <img src="https://comments.iris-go.com/comment30_mini.png" width="350px">
</a>

<a href="https://twitter.com/pvsukale/status/745328224876408832"> 
    <img src="https://comments.iris-go.com/comment31_mini.png" width="350px">
</a>

<a href="https://twitter.com/blainsmith/status/745338092211560453"> 
    <img src="https://comments.iris-go.com/comment32_mini.png" width="350px">
</a>

<a href="https://twitter.com/tjbyte/status/758287014210867200"> 
    <img src="https://comments.iris-go.com/comment33_mini.png" width="350px">
</a>

<a href="https://twitter.com/tangzero/status/751050577220698112"> 
    <img src="https://comments.iris-go.com/comment34_mini.png" width="350px">
</a>

<a href="https://twitter.com/tjbyte/status/758287244947972096"> 
    <img src="https://comments.iris-go.com/comment33_2_mini.png" width="350px">
</a>

<a href="https://twitter.com/ferarias/status/902468752364773376"> 
    <img src="https://comments.iris-go.com/comment41.png" width="350px">
</a>

<br/><br/>

For more information about contributing to the Iris project please check the [CONTRIBUTING.md](CONTRIBUTING.md) file.

[List of all Contributors](https://github.com/kataras/iris/graphs/contributors)

## Learn

First of all, the most correct way to begin with a web framework is to learn the basics of the programming language and the standard `http` capabilities, if your web application is a very simple personal project without performance and maintainability requirements you may want to proceed just with the standard packages. After that follow the guidelines:

- Navigate through **100+1** **[examples](_examples)** and some [iris starter kits](#iris-starter-kits) we crafted for you
- Read the [godocs](https://godoc.org/github.com/kataras/iris) for any details
- Prepare a cup of coffee or tea, whatever pleases you the most, and read some [articles](#articles) we found for you

### Iris starter kits

<!-- table form
| Description | Link |
| -----------|-------------|
| Hasura hub starter project with a ready to deploy golang helloworld webapp with IRIS! | https://hasura.io/hub/project/hasura/hello-golang-iris |
| A basic web app built in Iris for Go |https://github.com/gauravtiwari/go_iris_app |
| A mini social-network created with the awesome Iris💖💖 | https://github.com/iris-contrib/Iris-Mini-Social-Network |
| Iris isomorphic react/hot reloadable/redux/css-modules starter kit | https://github.com/iris-contrib/iris-starter-kit |
| Demo project with react using typescript and Iris | https://github.com/ionutvilie/react-ts |
| Self-hosted Localization Management Platform built with Iris and Angular | https://github.com/iris-contrib/parrot |
| Iris + Docker and Kubernetes | https://github.com/iris-contrib/cloud-native-go |
| Quickstart for Iris with Nanobox | https://guides.nanobox.io/golang/iris/from-scratch |
-->

1. [A basic web app built in Iris for Go](https://github.com/gauravtiwari/go_iris_app)
2. [A mini social-network created with the awesome Iris💖💖](https://github.com/iris-contrib/Iris-Mini-Social-Network)
3. [Iris isomorphic react/hot reloadable/redux/css-modules starter kit](https://github.com/iris-contrib/iris-starter-kit)
4. [Demo project with react using typescript and Iris](https://github.com/ionutvilie/react-ts)
5. [Self-hosted Localization Management Platform built with Iris and Angular](https://github.com/iris-contrib/parrot)
6. [Iris + Docker and Kubernetes](https://github.com/iris-contrib/cloud-native-go)
7. [Quickstart for Iris with Nanobox](https://guides.nanobox.io/golang/iris/from-scratch)
8. [A Hasura starter project with a ready to deploy Golang hello-world web app with IRIS](https://hasura.io/hub/project/hasura/hello-golang-iris)

> Did you build something similar? Let us [know](https://github.com/kataras/iris/pulls)!

### Middleware

Iris has a great collection of handlers[[1]](middleware/)[[2]](https://github.com/iris-contrib/middleware) that you can use side by side with your web apps. However you are not limited to them - you are free to use any third-party middleware that is compatible with the [net/http](https://golang.org/pkg/net/http/) package, [_examples/convert-handlers](_examples/convert-handlers) will show you the way.

Iris, unlike others, is 100% compatible with the standards and that's why the majority of the big companies that adapt Go to their workflow, like a very famous US Television Network, trust Iris; it's up-to-date and it will be always aligned with the std `net/http` package which is modernized by the Go Authors on each new release of the Go Programming Language.

### Articles

* [A Todo MVC Application using Iris and Vue.js](https://hackernoon.com/a-todo-mvc-application-using-iris-and-vue-js-5019ff870064)
* [A Hasura starter project with a ready to deploy Golang hello-world web app with IRIS](https://bit.ly/2lmKaAZ)
* [Top 6 web frameworks for Go as of 2017](https://blog.usejournal.com/top-6-web-frameworks-for-go-as-of-2017-23270e059c4b)
* [Iris Go Framework + MongoDB](https://medium.com/go-language/iris-go-framework-mongodb-552e349eab9c)
* [How to build a file upload form using DropzoneJS and Go](https://hackernoon.com/how-to-build-a-file-upload-form-using-dropzonejs-and-go-8fb9f258a991)
* [How to display existing files on server using DropzoneJS and Go](https://hackernoon.com/how-to-display-existing-files-on-server-using-dropzonejs-and-go-53e24b57ba19)
* [Iris, a modular web framework](https://medium.com/@corebreaker/iris-web-cd684b4685c7)
* [Go vs .NET Core in terms of HTTP performance](https://medium.com/@kataras/go-vs-net-core-in-terms-of-http-performance-7535a61b67b8)
* [Iris Go vs .NET Core Kestrel in terms of HTTP performance](https://hackernoon.com/iris-go-vs-net-core-kestrel-in-terms-of-http-performance-806195dc93d5)
* [How to Turn an Android Device into a Web Server](https://twitter.com/ThePracticalDev/status/892022594031017988)
* [Deploying a Iris Golang app in hasura](https://medium.com/@HasuraHQ/deploy-an-iris-golang-app-with-backend-apis-in-minutes-25a559bf530b)
* [A URL Shortener Service using Go, Iris and Bolt](https://medium.com/@kataras/a-url-shortener-service-using-go-iris-and-bolt-4182f0b00ae7)

### Video Courses

* [Daily Coding - Web Framework Golang: Iris Framework]( https://www.youtube.com/watch?v=BmOLFQ29J3s) by WarnabiruTV, source: youtube, cost: **FREE**
* [Tutorial Golang MVC dengan Iris Framework & Mongo DB](https://www.youtube.com/watch?v=uXiNYhJqh2I&list=PLMrwI6jIZn-1tzskocnh1pptKhVmWdcbS) (19 parts so far) by Musobar Media, source: youtube, cost: **FREE**
* [Go/Golang 27 - Iris framework : Routage de base](https://www.youtube.com/watch?v=rQxRoN6ub78) by stephgdesign, source: youtube, cost: **FREE**
* [Go/Golang 28 - Iris framework : Templating](https://www.youtube.com/watch?v=nOKYV073S2Y) by stephgdesignn, source: youtube, cost: **FREE**
* [Go/Golang 29 - Iris framework : Paramètres](https://www.youtube.com/watch?v=K2FsprfXs1E) by stephgdesign, source: youtube, cost: **FREE**
* [Go/Golang 30 - Iris framework : Les middelwares](https://www.youtube.com/watch?v=BLPy1So6bhE) by stephgdesign, source: youtube, cost: **FREE**
* [Go/Golang 31 - Iris framework : Les sessions](https://www.youtube.com/watch?v=RnBwUrwgEZ8) by stephgdesign, source: youtube, cost: **FREE**

### Get hired

There are many companies and start-ups looking for Go web developers with Iris experience as requirement, we are searching for you every day and we post those information via our [facebook page](https://www.facebook.com/iris.framework), like the page to get notified, we have already posted some of them.

## License

Iris is licensed under the [3-Clause BSD License](LICENSE). Iris is 100% free and open-source software.

For any questions regarding the license please send [e-mail](mailto:kataras2006@hotmail.com?subject=Iris%20License).
# Iris Web Framework <a href="README.md"> <img width="20px" src="https://iris-go.com/images/flag-unitedkingdom.svg?v=10" /></a> <a href="README_RU.md"><img width="20px" src="https://iris-go.com/images/flag-russia.svg?v=10" /></a> <a href="README_ID.md"> <img width="20px" src="https://iris-go.com/images/flag-indonesia.svg?v=10" /></a> <a href="README_GR.md"><img width="20px" src="https://iris-go.com/images/flag-greece.svg?v=10" /></a> <a href="README_PT_BR.md"><img width="20px" src="https://iris-go.com/images/flag-pt-br.svg?v=10" /></a> <a href="README_JPN.md"><img width="20px" src="https://iris-go.com/images/flag-japan.svg?v=10" /></a>

<a href="https://iris-go.com"> <img align="right" width="169px" src="https://iris-go.com/images/icon.svg?v=a" title="logo created by @merry.dii" /> </a>

[![build status](https://img.shields.io/travis/kataras/iris/master.svg?style=flat-square)](https://travis-ci.org/kataras/iris)<!-- [![release](https://img.shields.io/github/release/kataras/iris.svg?style=flat-square)](https://github.com/kataras/iris/releases)--> [![report card](https://img.shields.io/badge/report%20card-a%2B-ff3333.svg?style=flat-square)](http://goreportcard.com/report/kataras/iris) [![vscode-iris](https://img.shields.io/badge/ext%20-vscode-0c77e3.svg?style=flat-square)](https://marketplace.visualstudio.com/items?itemName=kataras2006.iris)<!--[![github closed issues](https://img.shields.io/github/issues-closed-raw/kataras/iris.svg?style=flat-square)](https://github.com/kataras/iris/issues?q=is%3Aissue+is%3Aclosed)--> [![chat](https://img.shields.io/badge/community-%20chat-00BCD4.svg?style=flat-square)](https://kataras.rocket.chat/channel/iris) [![view examples](https://img.shields.io/badge/learn%20by-examples-0077b3.svg?style=flat-square)](https://iris-go.com/v10/recipe) [![release](https://img.shields.io/badge/release%20-v10.6-0077b3.svg?style=flat-square)](https://github.com/kataras/iris/releases)

Iris 是一款超快、简洁高效的 Go 语言 Web开发框架。

Iris 功能强大、使用简单，它将会是你下一个网站、API 服务或者分布式应用基础框架的不二之选。

总之，是一款与 express.js 旗鼓相当的 Go 语言框架。

看看[别人是如何评价 Iris](#support)，同时欢迎各位点亮 Iris [Star](https://github.com/kataras/iris/stargazers)，或者关注 [Iris facebook 主页](https://facebook.com/iris.framework)。

## 支持者

感谢所有的支持者! 🙏 [支持我们](https://iris-go.com/donate)

<a href="https://iris-go.com/donate" target="_blank"><img src="https://iris-go.com/backers.svg?v=2"/></a>

```sh
$ cat example.go
```

```go
package main

import "github.com/kataras/iris"

func main() {
    app := iris.New()
    // 从 "./views" 目录加载HTML模板
    // 模板解析 html 后缀文件
    // 此方式使用 `html/template` 标准包 (Iris 的模板引擎)
    app.RegisterView(iris.HTML("./views", ".html"))

    // 方法：GET
    // 路径：http://localhost:8080
    app.Get("/", func(ctx iris.Context) {
        // {{.message}} 和 "Hello world!" 字符串变量绑定
        ctx.ViewData("message", "Hello world!")
        // 映射 HTML 模板文件路径 ./views/hello.html
        ctx.View("hello.html")
    })

    //方法：GET
    //路径：http://localhost:8080/user/42
    //
    // 使用正则表达式必须设置参数类型为 string
    // app.Get("/user/{id:string regexp(^[0-9]+$)}")
    app.Get("/user/{id:long}", func(ctx iris.Context) {
        userID, _ := ctx.Params().GetInt64("id")
        ctx.Writef("User ID: %d", userID)
    })

    // 绑定端口并启动服务.
    app.Run(iris.Addr(":8080"))
}
```

> 想要了解更多关于路径参数配置，戳[这里](_examples/routing/dynamic-path/main.go#L31)。

```html
<!-- file: ./views/hello.html -->
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>{{.message}}</h1>
</body>
</html>
```

```sh
$ go run example.go
Now listening on: http://localhost:8080
Application Started. Press CTRL+C to shut down.
_
```

## 安装

请确保安装 [Go Programming Language](https://golang.org/dl/)

```sh
$ go get -u github.com/kataras/iris
```

Iris 使用 [vendor](https://docs.google.com/document/d/1Bz5-UB7g2uPBdOx-rw5t9MxJwkfpx90cqG9AFL0JAYo) 包依赖管理方式。vendor 包管理的方式可以有效处理包依赖更新问题

[![Iris vs .NET Core(C#) vs Node.js (Express)](https://iris-go.com/images/benchmark-new-gray.png)](_benchmarks/README_UNIX.md)

_更新于: [2017年11月21日星期二](_benchmarks/README_UNIX.md)_

<details>
<summary>来自第三方的其他网络框架的基准测试</summary>

![Comparison with other frameworks](https://raw.githubusercontent.com/smallnest/go-web-framework-benchmark/4db507a22c964c9bc9774c5b31afdc199a0fe8b7/benchmark.png)

</details>

## 支持

- [更新记录](HISTORY_ZH.md#tu-05-june-2018--v1066) 是您最好的朋友，它包含有关最新功能和更改的信息
- 你碰巧找到了一个错误？ 请提交 [github issues](https://github.com/kataras/iris/issues)
- 您是否有任何疑问或需要与有经验的人士交谈以实时解决问题？ [加入我们的聊天](https://chat.iris-go.com)
- [点击这里完成我们基于表单的用户体验报告](https://docs.google.com/forms/d/e/1FAIpQLSdCxZXPANg_xHWil4kVAdhmh7EBBHQZ_4_xSZVDL-oCC_z5pA/viewform?usp=sf_link) 
- 你喜欢这个框架吗？ Twitter 上关于 Iris 的评价:

<a href="https://twitter.com/gelnior/status/769100480706379776"> 
    <img src="https://comments.iris-go.com/comment27_mini.png" width="350px">
</a>

<a href="https://twitter.com/MeAlex07/status/822799954188075008"> 
    <img src="https://comments.iris-go.com/comment28_mini.png" width="350px">
</a>

<a href="https://twitter.com/_mgale/status/818591490305761280"> 
    <img src="https://comments.iris-go.com/comment29_mini.png" width="350px">
</a>
<a href="https://twitter.com/VeayoX/status/813273328550973440"> 
    <img src="https://comments.iris-go.com/comment30_mini.png" width="350px">
</a>

<a href="https://twitter.com/pvsukale/status/745328224876408832"> 
    <img src="https://comments.iris-go.com/comment31_mini.png" width="350px">
</a>

<a href="https://twitter.com/blainsmith/status/745338092211560453"> 
    <img src="https://comments.iris-go.com/comment32_mini.png" width="350px">
</a>

<a href="https://twitter.com/tjbyte/status/758287014210867200"> 
    <img src="https://comments.iris-go.com/comment33_mini.png" width="350px">
</a>

<a href="https://twitter.com/tangzero/status/751050577220698112"> 
    <img src="https://comments.iris-go.com/comment34_mini.png" width="350px">
</a>

<a href="https://twitter.com/tjbyte/status/758287244947972096"> 
    <img src="https://comments.iris-go.com/comment33_2_mini.png" width="350px">
</a>

<a href="https://twitter.com/ferarias/status/902468752364773376"> 
    <img src="https://comments.iris-go.com/comment41.png" width="350px">
</a>


[如何贡献代码](CONTRIBUTING.md)

[贡献者列表](https://github.com/kataras/iris/graphs/contributors)

## 学习

首先，从 Web 框架开始的最正确的方法是学习 Golang 标准库 [net/http](https://golang.org/pkg/net/http/ "net/http") 的基础知识，如果您的 web 应用程序是一个非常简单的个人项目，没有性能和可维护性要求，您可能只需使用标准库即可。 之后，遵循以下指导原则：

- 浏览 **100+** **[例子](_examples)** 和 我们提供的 [一些入门经验](#iris-starter-kits)
- 通过 [godocs](https://godoc.org/github.com/kataras/iris) 阅读细节
- 准备一杯咖啡或茶，无论你喜欢什么，并阅读我们为你推荐的 [一些文章](#articles)

### Iris 入门

<!-- table form
| Description | Link |
| -----------|-------------|
| Hasura hub starter project with a ready to deploy golang helloworld webapp with IRIS! | https://hasura.io/hub/project/hasura/hello-golang-iris |
| A basic web app built in Iris for Go |https://github.com/gauravtiwari/go_iris_app |
| A mini social-network created with the awesome Iris💖💖 | https://github.com/iris-contrib/Iris-Mini-Social-Network |
| Iris isomorphic react/hot reloadable/redux/css-modules starter kit | https://github.com/iris-contrib/iris-starter-kit |
| Demo project with react using typescript and Iris | https://github.com/ionutvilie/react-ts |
| Self-hosted Localization Management Platform built with Iris and Angular | https://github.com/iris-contrib/parrot |
| Iris + Docker and Kubernetes | https://github.com/iris-contrib/cloud-native-go |
| Quickstart for Iris with Nanobox | https://guides.nanobox.io/golang/iris/from-scratch |
-->

1. [A basic web app built in Iris for Go](https://github.com/gauravtiwari/go_iris_app)
2. [A mini social-network created with the awesome Iris💖💖](https://github.com/iris-contrib/Iris-Mini-Social-Network)
3. [Iris isomorphic react/hot reloadable/redux/css-modules starter kit](https://github.com/iris-contrib/iris-starter-kit)
4. [Demo project with react using typescript and Iris](https://github.com/ionutvilie/react-ts)
5. [Self-hosted Localization Management Platform built with Iris and Angular](https://github.com/iris-contrib/parrot)
6. [Iris + Docker and Kubernetes](https://github.com/iris-contrib/cloud-native-go)
7. [Quickstart for Iris with Nanobox](https://guides.nanobox.io/golang/iris/from-scratch)
8. [A Hasura starter project with a ready to deploy Golang hello-world web app with IRIS](https://hasura.io/hub/project/hasura/hello-golang-iris)

> 如果你有类似的使用经验吗 [请提交给我们](https://github.com/kataras/iris/pulls)!

### 中间件

Iris 拥有大量的中间件 [[1]](middleware/)[[2]](https://github.com/iris-contrib/middleware) 供您的 Web 应用程序使用。 不过，您并不局限于此，您可以自由使用与 [net/http](https://golang.org/pkg/net/http/) 包兼容的任何第三方中间件，相关示例 [_examples/convert-handlers](_examples/convert-handlers) 。

### 相关文章（英文）

* [A Todo MVC Application using Iris and Vue.js](https://hackernoon.com/a-todo-mvc-application-using-iris-and-vue-js-5019ff870064)
* [A Hasura starter project with a ready to deploy Golang hello-world web app with IRIS](bit.ly/2lmKaAZ)
* [Top 6 web frameworks for Go as of 2017](https://blog.usejournal.com/top-6-web-frameworks-for-go-as-of-2017-23270e059c4b)
* [Iris Go Framework + MongoDB](https://medium.com/go-language/iris-go-framework-mongodb-552e349eab9c)
* [How to build a file upload form using DropzoneJS and Go](https://hackernoon.com/how-to-build-a-file-upload-form-using-dropzonejs-and-go-8fb9f258a991)
* [How to display existing files on server using DropzoneJS and Go](https://hackernoon.com/how-to-display-existing-files-on-server-using-dropzonejs-and-go-53e24b57ba19)
* [Iris, a modular web framework](https://medium.com/@corebreaker/iris-web-cd684b4685c7)
* [Go vs .NET Core in terms of HTTP performance](https://medium.com/@kataras/go-vs-net-core-in-terms-of-http-performance-7535a61b67b8)
* [Iris Go vs .NET Core Kestrel in terms of HTTP performance](https://hackernoon.com/iris-go-vs-net-core-kestrel-in-terms-of-http-performance-806195dc93d5)
* [How to Turn an Android Device into a Web Server](https://twitter.com/ThePracticalDev/status/892022594031017988)
* [Deploying a Iris Golang app in hasura](https://medium.com/@HasuraHQ/deploy-an-iris-golang-app-with-backend-apis-in-minutes-25a559bf530b)
* [A URL Shortener Service using Go, Iris and Bolt](https://medium.com/@kataras/a-url-shortener-service-using-go-iris-and-bolt-4182f0b00ae7)

### 视频教程（英文） - Youtube

* [Daily Coding - Web Framework Golang: Iris Framework]( https://www.youtube.com/watch?v=BmOLFQ29J3s) by WarnabiruTV
* [Tutorial Golang MVC dengan Iris Framework & Mongo DB](https://www.youtube.com/watch?v=uXiNYhJqh2I&list=PLMrwI6jIZn-1tzskocnh1pptKhVmWdcbS) (19 parts so far) by Musobar Media
* [Go/Golang 27 - Iris framework : Routage de base](https://www.youtube.com/watch?v=rQxRoN6ub78) by stephgdesign
* [Go/Golang 28 - Iris framework : Templating](https://www.youtube.com/watch?v=nOKYV073S2Y) by stephgdesignn
* [Go/Golang 29 - Iris framework : Paramètres](https://www.youtube.com/watch?v=K2FsprfXs1E) by stephgdesign
* [Go/Golang 30 - Iris framework : Les middelwares](https://www.youtube.com/watch?v=BLPy1So6bhE) by stephgdesign
* [Go/Golang 31 - Iris framework : Les sessions](https://www.youtube.com/watch?v=RnBwUrwgEZ8) by stephgdesign

### 工作机会

有很多公司都在寻找具有 Iris 经验的 Go 网站开发者，我们通过 [facebook page](https://www.facebook.com/iris.framework) 发布这些招聘信息。

## 授权协议

Iris 授权基于 [3-Clause BSD License](LICENSE). Iris 是 100％ 免费和开源软件。

有关授权的任何问题，[请发送电子邮件](mailto:kataras2006@hotmail.com?subject=Iris%20License)。
# Iris Web Framework <a href="README.md"> <img width="20px" src="https://iris-go.com/images/flag-unitedkingdom.svg?v=10" /> </a> <a href="README_ZH.md"> <img width="20px" src="https://iris-go.com/images/flag-china.svg?v=10" /> </a> <a href="README_RU.md"><img width="20px" src="https://iris-go.com/images/flag-russia.svg?v=10" /></a> <a href="README_GR.md"><img width="20px" src="https://iris-go.com/images/flag-greece.svg?v=10" /></a> <a href="README_PT_BR.md"><img width="20px" src="https://iris-go.com/images/flag-pt-br.svg?v=10" /></a> <a href="README_JPN.md"><img width="20px" src="https://iris-go.com/images/flag-japan.svg?v=10" /></a>

<a href="https://iris-go.com"> <img align="right" width="169px" src="https://iris-go.com/images/icon.svg?v=a" title="logo created by @merry.dii" /> </a>

[![build status](https://img.shields.io/travis/kataras/iris/master.svg?style=flat-square)](https://travis-ci.org/kataras/iris)<!-- [![release](https://img.shields.io/github/release/kataras/iris.svg?style=flat-square)](https://github.com/kataras/iris/releases)--> [![report card](https://img.shields.io/badge/report%20card-a%2B-ff3333.svg?style=flat-square)](http://goreportcard.com/report/kataras/iris) [![vscode-iris](https://img.shields.io/badge/ext%20-vscode-0c77e3.svg?style=flat-square)](https://marketplace.visualstudio.com/items?itemName=kataras2006.iris)<!--[![github closed issues](https://img.shields.io/github/issues-closed-raw/kataras/iris.svg?style=flat-square)](https://github.com/kataras/iris/issues?q=is%3Aissue+is%3Aclosed)--> [![chat](https://img.shields.io/badge/community-%20chat-00BCD4.svg?style=flat-square)](https://kataras.rocket.chat/channel/iris) [![view examples](https://img.shields.io/badge/learn%20by-examples-0077b3.svg?style=flat-square)](https://iris-go.com/v10/recipe) [![release](https://img.shields.io/badge/release%20-v10.6-0077b3.svg?style=flat-square)](https://github.com/kataras/iris/releases)

Iris adalah web framework yang cepat, sederhana namun berfitur lengkap dan sangat efisien untuk Go.

Iris menyediakan fondasi yang indah expresif dan mudah digunakan untuk website atau API anda selanjutnya.

Akhirnya, framework nyata yang setara dengan expressjs untuk Go Programming Language.

Pelajari apa yang [orang lain katakan tentang Iris](#support) dan [star](https://github.com/kataras/iris/stargazers) github repository ini untuk [mendapatkan informasi terbaru](https://facebook.com/iris.framework).

## Donatur

Terima kasih kepada seluruh donatur kami! 🙏 [Menjadi donatur](https://iris-go.com/donate)

<a href="https://iris-go.com/donate" target="_blank"><img src="https://iris-go.com/backers.svg?v=2"/></a>

```sh
$ cat example.go
```

```go
package main

import "github.com/kataras/iris"

func main() {
    app := iris.New()
    // Memuat semua template dari folder "./views"
    // yang memiliki ekstensi ".html" dan menguraikannya
    // menggunakan package standard `html/template`.
    app.RegisterView(iris.HTML("./views", ".html"))

    // Method:    GET
    // Resource:  http://localhost:8080
    app.Get("/", func(ctx iris.Context) {
        // Bind: {{.message}} with "Hello world!"
        ctx.ViewData("message", "Hello world!")
        // Render template file: ./views/hello.html
        ctx.View("hello.html")
    })

    // Method:    GET
    // Resource:  http://localhost:8080/user/42
    //
    // Butuh menggunakan custom regexp sebagai gantinya?
    // Mudah,
    // cukup tandai tipe parameter menjadi 'string'
    // yang akan menerima semua dan akan menggunakan
    // fungsi macro `regexp`, Contoh:
    // app.Get("/user/{id:string regexp(^[0-9]+$)}")
    app.Get("/user/{id:long}", func(ctx iris.Context) {
        userID, _ := ctx.Params().GetInt64("id")
        ctx.Writef("User ID: %d", userID)
    })

    // Menyalakan server menggunakan network address.
    app.Run(iris.Addr(":8080"))
}
```

> Pelajari lebih lanjut tentang tipe parameter di path dengan klik [disini](_examples/routing/dynamic-path/main.go#L31)

```html
<!-- file: ./views/hello.html -->
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>{{.message}}</h1>
</body>
</html>
```

```sh
$ go run example.go
Now listening on: http://localhost:8080
Application Started. Press CTRL+C to shut down.
_
```

## Instalasi

Satu - satunya persyaratan adalah [Go Programming Language](https://golang.org/dl/)

```sh
$ go get -u github.com/kataras/iris
```

Iris mengambil keuntungan dari fitur [vendor directory](https://docs.google.com/document/d/1Bz5-UB7g2uPBdOx-rw5t9MxJwkfpx90cqG9AFL0JAYo). Anda mendapatkan build yang benar - benar dapat direproduksi, karena metode ini menjaga terhadap penggantian nama dan penghapusan di upstream.

[![Iris vs .NET Core(C#) vs Node.js (Express)](https://iris-go.com/images/benchmark-new-gray.png)](_benchmarks/README_UNIX.md)

_Diperbarui pada: [Tuesday, 21 November 2017](_benchmarks/README_UNIX.md)_

<details>
<summary>Benchmarks dari sumber pihak ketiga terhadap rest web frameworks</summary>

![Perbandingan dengan framework lain](https://raw.githubusercontent.com/smallnest/go-web-framework-benchmark/4db507a22c964c9bc9774c5b31afdc199a0fe8b7/benchmark.png)

</details>

## Dukungan

- File [HISTORY](HISTORY_ID.md#tu-05-june-2018--v1066) adalah sahabat anda, file tersebut memiliki informasi terkait fitur dan perubahan terbaru
- Apakah anda menemukan bug? Laporkan itu melalui [github issues](https://github.com/kataras/iris/issues)
- Apakah anda memiliki pertanyaan atau butuh untuk bicara kepada seseorang yang sudah berpengalaman untuk menyelesaikan masalah secara langsung? Gabung bersama kami di [community chat](https://chat.iris-go.com)
- Lengkapi laporan user-experience berbasis formulir kami dengan tekan [disini](https://docs.google.com/forms/d/e/1FAIpQLSdCxZXPANg_xHWil4kVAdhmh7EBBHQZ_4_xSZVDL-oCC_z5pA/viewform?usp=sf_link)
- Apakah anda menyukai framework ini? Tweet sesuatu tentang ini! Orang - orang yang sudah berbicara:

<a href="https://twitter.com/gelnior/status/769100480706379776"> 
    <img src="https://comments.iris-go.com/comment27_mini.png" width="350px">
</a>

<a href="https://twitter.com/MeAlex07/status/822799954188075008"> 
    <img src="https://comments.iris-go.com/comment28_mini.png" width="350px">
</a>

<a href="https://twitter.com/_mgale/status/818591490305761280"> 
    <img src="https://comments.iris-go.com/comment29_mini.png" width="350px">
</a>
<a href="https://twitter.com/VeayoX/status/813273328550973440"> 
    <img src="https://comments.iris-go.com/comment30_mini.png" width="350px">
</a>

<a href="https://twitter.com/pvsukale/status/745328224876408832"> 
    <img src="https://comments.iris-go.com/comment31_mini.png" width="350px">
</a>

<a href="https://twitter.com/blainsmith/status/745338092211560453"> 
    <img src="https://comments.iris-go.com/comment32_mini.png" width="350px">
</a>

<a href="https://twitter.com/tjbyte/status/758287014210867200"> 
    <img src="https://comments.iris-go.com/comment33_mini.png" width="350px">
</a>

<a href="https://twitter.com/tangzero/status/751050577220698112"> 
    <img src="https://comments.iris-go.com/comment34_mini.png" width="350px">
</a>

<a href="https://twitter.com/tjbyte/status/758287244947972096"> 
    <img src="https://comments.iris-go.com/comment33_2_mini.png" width="350px">
</a>

<a href="https://twitter.com/ferarias/status/902468752364773376"> 
    <img src="https://comments.iris-go.com/comment41.png" width="350px">
</a>

<br/><br/>

Untuk informasi lebih lanjut mengenai kontribusi terhadap project Iris, mohon untuk mengecek file [CONTRIBUTING.md](CONTRIBUTING.md).

[Daftar seluruh Kontributor](https://github.com/kataras/iris/graphs/contributors)

## Belajar

Pertama - tama, cara yang paling tepat untuk memulai dengan web framework adalah dengan mempelajari dasar dari bahasa pemrograman dan kemampuan dasar `http`, apabila aplikasi web anda adalah proyek pribadi yang sangat sederhana tanpa kebutuhan kinerja dan pemeliharaan, anda dapat melanjutkan hanya dengan standard packages. Setelah itu, ikut petunjuknya:

- Kunjungi **100+1** **[contoh](_examples)** dan beberapa [iris starter kits](#iris-starter-kits) yang kami buat untuk anda
- Baca [godocs](https://godoc.org/github.com/kataras/iris) untuk penjelasan yang lebih detail
- Siapkan secangkir kopi atau teh, apapun yang paling menyenangkan anda, dan baca beberapa [artikel](#articles) yang kami temukan untuk anda

### Iris starter kits

<!-- table form 
| Description | Link |
| -----------|-------------|
| Hasura hub starter project with a ready to deploy golang helloworld webapp with IRIS! | https://hasura.io/hub/project/hasura/hello-golang-iris |
| A basic web app built in Iris for Go |https://github.com/gauravtiwari/go_iris_app |
| A mini social-network created with the awesome Iris💖💖 | https://github.com/iris-contrib/Iris-Mini-Social-Network |
| Iris isomorphic react/hot reloadable/redux/css-modules starter kit | https://github.com/iris-contrib/iris-starter-kit |
| Demo project with react using typescript and Iris | https://github.com/ionutvilie/react-ts |
| Self-hosted Localization Management Platform built with Iris and Angular | https://github.com/iris-contrib/parrot |
| Iris + Docker and Kubernetes | https://github.com/iris-contrib/cloud-native-go |
| Quickstart for Iris with Nanobox | https://guides.nanobox.io/golang/iris/from-scratch |
-->

1. [A basic web app built in Iris for Go](https://github.com/gauravtiwari/go_iris_app)
2. [A mini social-network created with the awesome Iris💖💖](https://github.com/iris-contrib/Iris-Mini-Social-Network)
3. [Iris isomorphic react/hot reloadable/redux/css-modules starter kit](https://github.com/iris-contrib/iris-starter-kit)
4. [Demo project with react using typescript and Iris](https://github.com/ionutvilie/react-ts)
5. [Self-hosted Localization Management Platform built with Iris and Angular](https://github.com/iris-contrib/parrot)
6. [Iris + Docker and Kubernetes](https://github.com/iris-contrib/cloud-native-go)
7. [Quickstart for Iris with Nanobox](https://guides.nanobox.io/golang/iris/from-scratch)
8. [A Hasura starter project with a ready to deploy Golang hello-world web app with IRIS](https://hasura.io/hub/project/hasura/hello-golang-iris)

> Apakah anda membuat hal yang serupa? [Beritahu kami](https://github.com/kataras/iris/pulls)!

### Middleware

Iris memiliki koleksi handler yang hebat[[1]](middleware/)[[2]](https://github.com/iris-contrib/middleware) yang dapat anda gunakan berdampingan dengan aplikasi web anda. Namun, anda tidak terbatas oleh itu saja - anda bebas menggunakan third-party middleware yang compatible dengan package [net/http](https://golang.org/pkg/net/http/), [_examples/convert-handlers](_examples/convert-handlers) akan menunjukkan caranya.

Iris, tidak seperti yang lain, 100% compatible dengan standards dan maka dari itu mayoritas dari perusahaan besar yang mengadaptasi Go kepada alur kerja mereka, seperti Jaringan Telivisi yang sangat terkenal di US, mempercayai Iris; framework yang up-to-date dan ini akan selalu selaras dengan package std `net/http` yang dimodernisasi oleh Pencipta Go di setiap release dari Go Programming Language.

### Articles

* [A Todo MVC Application using Iris and Vue.js](https://hackernoon.com/a-todo-mvc-application-using-iris-and-vue-js-5019ff870064)
* [A Hasura starter project with a ready to deploy Golang hello-world web app with IRIS](https://bit.ly/2lmKaAZ)
* [Top 6 web frameworks for Go as of 2017](https://blog.usejournal.com/top-6-web-frameworks-for-go-as-of-2017-23270e059c4b)
* [Iris Go Framework + MongoDB](https://medium.com/go-language/iris-go-framework-mongodb-552e349eab9c)
* [How to build a file upload form using DropzoneJS and Go](https://hackernoon.com/how-to-build-a-file-upload-form-using-dropzonejs-and-go-8fb9f258a991)
* [How to display existing files on server using DropzoneJS and Go](https://hackernoon.com/how-to-display-existing-files-on-server-using-dropzonejs-and-go-53e24b57ba19)
* [Iris, a modular web framework](https://medium.com/@corebreaker/iris-web-cd684b4685c7)
* [Go vs .NET Core in terms of HTTP performance](https://medium.com/@kataras/go-vs-net-core-in-terms-of-http-performance-7535a61b67b8)
* [Iris Go vs .NET Core Kestrel in terms of HTTP performance](https://hackernoon.com/iris-go-vs-net-core-kestrel-in-terms-of-http-performance-806195dc93d5)
* [How to Turn an Android Device into a Web Server](https://twitter.com/ThePracticalDev/status/892022594031017988)
* [Deploying a Iris Golang app in hasura](https://medium.com/@HasuraHQ/deploy-an-iris-golang-app-with-backend-apis-in-minutes-25a559bf530b)
* [A URL Shortener Service using Go, Iris and Bolt](https://medium.com/@kataras/a-url-shortener-service-using-go-iris-and-bolt-4182f0b00ae7)

### Video Courses

* [Daily Coding - Web Framework Golang: Iris Framework]( https://www.youtube.com/watch?v=BmOLFQ29J3s) by WarnabiruTV, sumber: youtube, biaya: **GRATIS**
* [Tutorial Golang MVC dengan Iris Framework & Mongo DB](https://www.youtube.com/watch?v=uXiNYhJqh2I&list=PLMrwI6jIZn-1tzskocnh1pptKhVmWdcbS) (19 parts so far) by Musobar Media, sumber: youtube, biaya: **GRATIS**
* [Go/Golang 27 - Iris framework : Routage de base](https://www.youtube.com/watch?v=rQxRoN6ub78) by stephgdesign, sumber: youtube, biaya: **GRATIS**
* [Go/Golang 28 - Iris framework : Templating](https://www.youtube.com/watch?v=nOKYV073S2Y) by stephgdesignn, sumber: youtube, biaya: **GRATIS**
* [Go/Golang 29 - Iris framework : Paramètres](https://www.youtube.com/watch?v=K2FsprfXs1E) by stephgdesign, sumber: youtube, biaya: **GRATIS**
* [Go/Golang 30 - Iris framework : Les middelwares](https://www.youtube.com/watch?v=BLPy1So6bhE) by stephgdesign, sumber: youtube, biaya: **GRATIS**
* [Go/Golang 31 - Iris framework : Les sessions](https://www.youtube.com/watch?v=RnBwUrwgEZ8) by stephgdesign, sumber: youtube, biaya: **GRATIS**

### Get hired

Ada beberapa perusahaan dan start-up yang mencari web developer Go yang memiliki pengalaman menggunakn Iris, kami mencarikan untuk anda setiap hari dan kami post informasi tersebut melalui [facebook page](https://www.facebook.com/iris.framework) kami, like page kami untuk mendapatkan notifikasi, kami sudah mempost beberapa dari mereka.

## License

Iris dilisensikan di bawah [3-Clause BSD License](LICENSE). Iris 100% gratis dan software open-source.

Apabila ada pertanyaan mengenai lisensi, anda dapat mengirimkan [e-mail](mailto:kataras2006@hotmail.com?subject=Iris%20License).
# Examples

Please do learn how [net/http](https://golang.org/pkg/net/http/) std package works, first.

This folder provides easy to understand code snippets on how to get started with [iris](https://github.com/kataras/iris) micro web framework.

It doesn't always contain the "best ways" but it does cover each important feature that will make you so excited to GO with iris!

### Overview

- [Hello world!](hello-world/main.go)
- [Glimpse](overview/main.go)
- [Tutorial: Online Visitors](tutorial/online-visitors/main.go)
- [Tutorial: A Todo MVC Application using Iris and Vue.js](https://hackernoon.com/a-todo-mvc-application-using-iris-and-vue-js-5019ff870064)
- [Tutorial: URL Shortener using BoltDB](https://medium.com/@kataras/a-url-shortener-service-using-go-iris-and-bolt-4182f0b00ae7)
- [Tutorial: How to turn your Android Device into a fully featured Web Server (**MUST**)](https://twitter.com/ThePracticalDev/status/892022594031017988)
- [POC: Convert the medium-sized project "Parrot" from native to Iris](https://github.com/iris-contrib/parrot)
- [POC: Isomorphic react/hot reloadable/redux/css-modules starter kit](https://github.com/kataras/iris-starter-kit)
- [Tutorial: DropzoneJS Uploader](tutorial/dropzonejs)
- [Tutorial: Caddy](tutorial/caddy)
- [Tutorial:Iris Go Framework + MongoDB](https://medium.com/go-language/iris-go-framework-mongodb-552e349eab9c)

### Structuring

Nothing stops you from using your favorite folder structure. Iris is a low level web framework, it has got MVC first-class support but it doesn't limit your folder structure, this is your choice.

Structuring depends on your own needs. We can't tell you how to design your own application for sure but you're free to take a closer look to the examples below; you may find something useful that you can borrow for your app;

- [Bootstrapper](structuring/bootstrap)
- [MVC with Repository and Service layer Overview](structuring/mvc-plus-repository-and-service-layers)
- [Login (MVC with Single Responsibility package)](structuring/login-mvc-single-responsibility-package)
- [Login (MVC with Datamodels, Datasource, Repository and Service layer)](structuring/login-mvc)

### HTTP Listening

- [Common, with address](http-listening/listen-addr/main.go)
    * [omit server errors](http-listening/listen-addr/omit-server-errors/main.go)
- [UNIX socket file](http-listening/listen-unix/main.go)
- [TLS](http-listening/listen-tls/main.go)
- [Letsencrypt (Automatic Certifications)](http-listening/listen-letsencrypt/main.go)
- [Notify on shutdown](http-listening/notify-on-shutdown/main.go)
- Custom TCP Listener
    * [common net.Listener](http-listening/custom-listener/main.go)
    * [SO_REUSEPORT for unix systems](http-listening/custom-listener/unix-reuseport/main.go)
- Custom HTTP Server
    * [easy way](http-listening/custom-httpserver/easy-way/main.go)
    * [std way](http-listening/custom-httpserver/std-way/main.go)
    * [multi server instances](http-listening/custom-httpserver/multi/main.go)
- Graceful Shutdown
    * [using the `RegisterOnInterrupt`](http-listening/graceful-shutdown/default-notifier/main.go)
    * [using a custom notifier](http-listening/graceful-shutdown/custom-notifier/main.go)

### Configuration

- [Functional](configuration/functional/main.go)
- [From Configuration Struct](configuration/from-configuration-structure/main.go)
- [Import from YAML file](configuration/from-yaml-file/main.go)
    * [Share Configuration between multiple instances](configuration/from-yaml-file/shared-configuration/main.go)
- [Import from TOML file](configuration/from-toml-file/main.go)

### Routing, Grouping, Dynamic Path Parameters, "Macros" and Custom Context

* `app.Get("{userid:int min(1)}", myHandler)`
* `app.Post("{asset:path}", myHandler)`
* `app.Put("{custom:string regexp([a-z]+)}", myHandler)`

Note: unlike other routers you'd seen, iris' router can handle things like these:
```go
// Matches all GET requests prefixed with "/assets/"
app.Get("/assets/{asset:path}", assetsWildcardHandler)

// Matches only GET "/"
app.Get("/", indexHandler)
// Matches only GET "/about"
app.Get("/about", aboutHandler)

// Matches all GET requests prefixed with "/profile/"
// and followed by a single path part
app.Get("/profile/{username:string}", userHandler)
// Matches only GET "/profile/me" because 
// it does not conflict with /profile/{username:string}
// or the root wildcard {root:path}
app.Get("/profile/me", userHandler)

// Matches all GET requests prefixed with /users/
// and followed by a number which should be equal or bigger than 1
app.Get("/user/{userid:int min(1)}", getUserHandler)
// Matches all requests DELETE prefixed with /users/
// and following by a number which should be equal or bigger than 1
app.Delete("/user/{userid:int min(1)}", deleteUserHandler)

// Matches all GET requests except "/", "/about", anything starts with "/assets/" etc...
// because it does not conflict with the rest of the routes.
app.Get("{root:path}", rootWildcardHandler)
```

Navigate through examples for a better understanding.

- [Overview](routing/overview/main.go)
- [Basic](routing/basic/main.go)
- [Controllers](mvc)
- [Custom HTTP Errors](routing/http-errors/main.go)
- [Dynamic Path](routing/dynamic-path/main.go)
    * [root level wildcard path](routing/dynamic-path/root-wildcard/main.go)
- [Reverse routing](routing/reverse/main.go)
- [Custom wrapper](routing/custom-wrapper/main.go)
- Custom Context
    * [method overriding](routing/custom-context/method-overriding/main.go)
    * [new implementation](routing/custom-context/new-implementation/main.go)
- [Route State](routing/route-state/main.go)
- [Writing a middleware](routing/writing-a-middleware)
    * [per-route](routing/writing-a-middleware/per-route/main.go)
    * [globally](routing/writing-a-middleware/globally/main.go)

### hero

- [Basic](hero/basic/main.go)
- [Overview](hero/overview)

### MVC

![](mvc/web_mvc_diagram.png)

Iris has **first-class support for the MVC (Model View Controller) pattern**, you'll not find
these stuff anywhere else in the Go world.

Iris web framework supports Request data, Models, Persistence Data and Binding
with the fastest possible execution.

**Characteristics**

All HTTP Methods are supported, for example if want to serve `GET`
then the controller should have a function named `Get()`,
you can define more than one method function to serve in the same Controller.

Serve custom controller's struct's methods as handlers with custom paths(even with regex parametermized path) via the `BeforeActivation` custom event callback, per-controller. Example:

```go
import (
    "github.com/kataras/iris"
    "github.com/kataras/iris/mvc"
)

func main() {
    app := iris.New()
    mvc.Configure(app.Party("/root"), myMVC)
    app.Run(iris.Addr(":8080"))
}

func myMVC(app *mvc.Application) {
    // app.Register(...)
    // app.Router.Use/UseGlobal/Done(...)
    app.Handle(new(MyController))
}

type MyController struct {}

func (m *MyController) BeforeActivation(b mvc.BeforeActivation) {
    // b.Dependencies().Add/Remove
    // b.Router().Use/UseGlobal/Done // and any standard API call you already know

    // 1-> Method
    // 2-> Path
    // 3-> The controller's function name to be parsed as handler
    // 4-> Any handlers that should run before the MyCustomHandler
    b.Handle("GET", "/something/{id:long}", "MyCustomHandler", anyMiddleware...)
}

// GET: http://localhost:8080/root
func (m *MyController) Get() string { return "Hey" }

// GET: http://localhost:8080/root/something/{id:long}
func (m *MyController) MyCustomHandler(id int64) string { return "MyCustomHandler says Hey" }
```

Persistence data inside your Controller struct (share data between requests)
by defining services to the Dependencies or have a `Singleton` controller scope.

Share the dependencies between controllers or register them on a parent MVC Application, and ability
to modify dependencies per-controller on the `BeforeActivation` optional event callback inside a Controller,
i.e `func(c *MyController) BeforeActivation(b mvc.BeforeActivation) { b.Dependencies().Add/Remove(...) }`.

Access to the `Context` as a controller's field(no manual binding is neede) i.e `Ctx iris.Context` or via a method's input argument, i.e `func(ctx iris.Context, otherArguments...)`.

Models inside your Controller struct (set-ed at the Method function and rendered by the View).
You can return models from a controller's method or set a field in the request lifecycle
and return that field to another method, in the same request lifecycle.

Flow as you used to, mvc application has its own `Router` which is a type of `iris/router.Party`, the standard iris api.
`Controllers` can be registered to any `Party`, including Subdomains, the Party's begin and done handlers work as expected.

Optional `BeginRequest(ctx)` function to perform any initialization before the method execution,
useful to call middlewares or when many methods use the same collection of data.

Optional `EndRequest(ctx)` function to perform any finalization after any method executed.

Inheritance, recursively, see for example our `mvc.SessionController`, it has the `Session *sessions.Session` and `Manager *sessions.Sessions` as embedded fields
which are filled by its `BeginRequest`, [here](https://github.com/kataras/iris/blob/master/mvc/session_controller.go).
This is just an example, you could use the `sessions.Session` which returned from the manager's `Start` as a dynamic dependency to the MVC Application, i.e
`mvcApp.Register(sessions.New(sessions.Config{Cookie: "iris_session_id"}).Start)`.

Access to the dynamic path parameters via the controller's methods' input arguments, no binding is needed.
When you use the Iris' default syntax to parse handlers from a controller, you need to suffix the methods
with the `By` word, uppercase is a new sub path. Example:

If `mvc.New(app.Party("/user")).Handle(new(user.Controller))`

- `func(*Controller) Get()` - `GET:/user`.
- `func(*Controller) Post()` - `POST:/user`.
- `func(*Controller) GetLogin()` - `GET:/user/login`
- `func(*Controller) PostLogin()` - `POST:/user/login`
- `func(*Controller) GetProfileFollowers()` - `GET:/user/profile/followers`
- `func(*Controller) PostProfileFollowers()` - `POST:/user/profile/followers`
- `func(*Controller) GetBy(id int64)` - `GET:/user/{param:long}`
- `func(*Controller) PostBy(id int64)` - `POST:/user/{param:long}`

If `mvc.New(app.Party("/profile")).Handle(new(profile.Controller))`

- `func(*Controller) GetBy(username string)` - `GET:/profile/{param:string}`

If `mvc.New(app.Party("/assets")).Handle(new(file.Controller))`

- `func(*Controller) GetByWildard(path string)` - `GET:/assets/{param:path}`

    Supported types for method functions receivers: int, int64, bool and string.

Response via output arguments, optionally, i.e

```go
func(c *ExampleController) Get() string |
                                (string, string) |
                                (string, int) |
                                int |
                                (int, string) |
                                (string, error) |
                                error |
                                (int, error) |
                                (any, bool) |
                                (customStruct, error) |
                                customStruct |
                                (customStruct, int) |
                                (customStruct, string) |
                                mvc.Result or (mvc.Result, error)
```

where [mvc.Result](https://github.com/kataras/iris/blob/master/mvc/go19.go#L10) is an [interface](https://github.com/kataras/iris/blob/master/hero/func_result.go#L18) which contains only that function: `Dispatch(ctx iris.Context)`.

## Using Iris MVC for code reuse

By creating components that are independent of one another, developers are able to reuse components quickly and easily in other applications. The same (or similar) view for one application can be refactored for another application with different data because the view is simply handling how the data is being displayed to the user.

If you're new to back-end web development read about the MVC architectural pattern first, a good start is that [wikipedia article](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller).

Follow the examples below,

- [Hello world](mvc/hello-world/main.go) **UPDATED**
- [Session Controller](mvc/session-controller/main.go) **UPDATED**
- [Overview - Plus Repository and Service layers](mvc/overview) **UPDATED**
- [Login showcase - Plus Repository and Service layers](mvc/login) **UPDATED**
- [Singleton](mvc/singleton) **NEW**
- [Websocket Controller](mvc/websocket) **NEW**
- [Register Middleware](mvc/middleware) **NEW**
- [Vue.js Todo MVC](tutorial/vuejs-todo-mvc) **NEW**

### Subdomains

- [Single](subdomains/single/main.go)
- [Multi](subdomains/multi/main.go)
- [Wildcard](subdomains/wildcard/main.go)
- [WWW](subdomains/www/main.go)
- [Redirect fast](subdomains/redirect/main.go)

### Convert `http.Handler/HandlerFunc`

- [From func(w http.ResponseWriter, r *http.Request, next http.HandlerFunc)](convert-handlers/negroni-like/main.go)
- [From http.Handler or http.HandlerFunc](convert-handlers/nethttp/main.go)
- [From func(http.HandlerFunc) http.HandlerFunc](convert-handlers/real-usecase-raven/writing-middleware/main.go)

### View

| Engine | Declaration |
| -----------|-------------|
| template/html | `iris.HTML(...)`       |
| django        | `iris.Django(...)`     |
| handlebars    | `iris.Handlebars(...)` |
| amber         | `iris.Amber(...)`      |
| pug(jade)     | `iris.Pug(...)`        |

- [Overview](view/overview/main.go)
- [Hi](view/template_html_0/main.go)
- [A simple Layout](view/template_html_1/main.go)
- [Layouts: `yield` and `render` tmpl funcs](view/template_html_2/main.go)
- [The `urlpath` tmpl func](view/template_html_3/main.go)
- [The `url` tmpl func](view/template_html_4/main.go)
- [Inject Data Between Handlers](view/context-view-data/main.go)
- [Embedding Templates Into App Executable File](view/embedding-templates-into-app/main.go)
- [Write to a custom `io.Writer`](view/write-to)
- [Greeting with Pug (Jade)`](view/template_pug_0)
- [Pug (Jade) Actions`](view/template_pug_1)
- [Pug (Jade) Includes`](view/template_pug_2)
- [Pug (Jade) Extends`](view/template_pug_3)

You can serve [quicktemplate](https://github.com/valyala/quicktemplate) and [hero templates](https://github.com/shiyanhui/hero/hero) files too, simply by using the `context#ResponseWriter`, take a look at the [http_responsewriter/quicktemplate](http_responsewriter/quicktemplate) and [http_responsewriter/herotemplate](http_responsewriter/herotemplate) examples.

### Authentication

- [Basic Authentication](authentication/basicauth/main.go)
- [OAUth2](authentication/oauth2/main.go)
- [JWT](experimental-handlers/jwt/main.go)
- [Sessions](#sessions)

### File Server

- [Favicon](file-server/favicon/main.go)
- [Basic](file-server/basic/main.go)
- [Embedding Files Into App Executable File](file-server/embedding-files-into-app/main.go)
- [Embedding Gziped Files Into App Executable File](file-server/embedding-gziped-files-into-app/main.go) **NEW**
- [Send/Force-Download Files](file-server/send-files/main.go)
- Single Page Applications
    * [single Page Application](file-server/single-page-application/basic/main.go)
    * [embedded Single Page Application](file-server/single-page-application/embedded-single-page-application/main.go)
    * [embedded Single Page Application with other routes](file-server/single-page-application/embedded-single-page-application-with-other-routes/main.go)

### How to Read from `context.Request() *http.Request`

- [Read JSON](http_request/read-json/main.go)
- [Read XML](http_request/read-xml/main.go)
- [Read Form](http_request/read-form/main.go)
- [Read Custom per type](http_request/read-custom-per-type/main.go)
- [Read Custom via Unmarshaler](http_request/read-custom-via-unmarshaler/main.go)
- [Upload/Read File](http_request/upload-file/main.go)
- [Upload multiple files with an easy way](http_request/upload-files/main.go)

> The `context.Request()` returns the same *http.Request you already know, these examples show some places where the  Context uses this object. Besides that you can use it as you did before iris.

### How to Write to `context.ResponseWriter() http.ResponseWriter`

- [Write `valyala/quicktemplate` templates](http_responsewriter/quicktemplate)
- [Write `shiyanhui/hero` templates](http_responsewriter/herotemplate)
- [Text, Markdown, HTML, JSON, JSONP, XML, Binary](http_responsewriter/write-rest/main.go)
- [Write Gzip](http_responsewriter/write-gzip/main.go)
- [Stream Writer](http_responsewriter/stream-writer/main.go)
- [Transactions](http_responsewriter/transactions/main.go)
- [SSE (third-party package usage for server-side events)](http_responsewriter/sse-third-party/main.go)

> The `context/context#ResponseWriter()` returns an enchament version of a http.ResponseWriter, these examples show some places where the Context uses this object. Besides that you can use it as you did before iris.

### ORM

- [Using xorm(Mysql, MyMysql, Postgres, Tidb, **SQLite**, MsSql, MsSql, Oracle)](orm/xorm/main.go)

### Miscellaneous

- [Request Logger](http_request/request-logger/main.go)
    * [log requests to a file](http_request/request-logger/request-logger-file/main.go)
- [Localization and Internationalization](miscellaneous/i18n/main.go)
- [Recovery](miscellaneous/recover/main.go)
- [Profiling (pprof)](miscellaneous/pprof/main.go)
- [Internal Application File Logger](miscellaneous/file-logger/main.go)
- [Google reCAPTCHA](miscellaneous/recaptcha/main.go) 

### Experimental Handlers

- [Casbin wrapper](experimental-handlers/casbin/wrapper/main.go)
- [Casbin middleware](experimental-handlers/casbin/middleware/main.go)
- [Cloudwatch](experimental-handlers/cloudwatch/simple/main.go)
- [CORS](experimental-handlers/cors/simple/main.go)
- [JWT](experimental-handlers/jwt/main.go)
- [Newrelic](experimental-handlers/newrelic/simple/main.go)
- [Prometheus](experimental-handlers/prometheus/simple/main.go)
- [Secure](experimental-handlers/secure/simple/main.go)
- [Tollboothic](experimental-handlers/tollboothic/limit-handler/main.go)
- [Cross-Site Request Forgery Protection](experimental-handlers/csrf/main.go)

#### More

https://github.com/kataras/iris/tree/master/middleware#third-party-handlers

### Automated API Documentation

- [yaag](apidoc/yaag/main.go)

### Testing

The `httptest` package is your way for end-to-end HTTP testing, it uses the httpexpect library created by our friend, [gavv](https://github.com/gavv).

[Example](testing/httptest/main_test.go)

### Caching

iris cache library lives on its own [package](https://github.com/kataras/iris/tree/master/cache).

- [Simple](cache/simple/main.go)
- [Client-Side (304)](cache/client-side/main.go) - part of the iris context core

> You're free to use your own favourite caching package if you'd like so.

### Cookies

- [Basic](cookies/basic/main.go)
- [Encode/Decode (securecookie)](cookies/securecookie/main.go)

### Sessions

iris session manager lives on its own [package](https://github.com/kataras/iris/tree/master/sessions).

- [Overview](sessions/overview/main.go)
- [Standalone](sessions/standalone/main.go)
- [Secure Cookie](sessions/securecookie/main.go)
- [Flash Messages](sessions/flash-messages/main.go)
- [Databases](sessions/database)
    * [Badger](sessions/database/badger/main.go)
    * [BoltDB](sessions/database/boltdb/main.go)
    * [Redis](sessions/database/redis/main.go)

> You're free to use your own favourite sessions package if you'd like so.

### Websockets

iris websocket library lives on its own [package](https://github.com/kataras/iris/tree/master/websocket).

The package is designed to work with raw websockets although its API is similar to the famous [socket.io](https://socket.io). I have read an article recently and I felt very contented about my decision to design a **fast** websocket-**only** package for Iris and not a backwards socket.io-like package. You can read that article by following this link: https://medium.com/@ivanderbyl/why-you-don-t-need-socket-io-6848f1c871cd.

- [Chat](websocket/chat/main.go)
- [Native Messages](websocket/native-messages/main.go)
- [Connection List](websocket/connectionlist/main.go)
- [TLS Enabled](websocket/secure/main.go)
- [Custom Raw Go Client](websocket/custom-go-client/main.go)
- [Third-Party socket.io](websocket/third-party-socketio/main.go)

> You're free to use your own favourite websockets package if you'd like so.

### Typescript Automation Tools

typescript automation tools have their own repository: [https://github.com/kataras/iris/tree/master/typescript](https://github.com/kataras/iris/tree/master/typescript) **it contains examples**

> I'd like to tell you that you can use your favourite but I don't think you will find such a thing anywhere else.

### Hey, You

Developers should read the [godocs](https://godoc.org/github.com/kataras/iris) and https://docs.iris-go.com for a better understanding.

Psst, I almost forgot; do not forget to [star or watch](https://github.com/kataras/iris/stargazers) the project in order to stay updated with the latest tech trends, it never takes more than a second!

# 示例

请先学习如何使用 [net/http](https://golang.org/pkg/net/http/) 

这里包含大部分 [iris](https://github.com/kataras/iris) 网络微框架的简单使用示例

这些示例不一定是最优解，但涵盖了 Iris 的大部分重要功能。

### 概览

- [Hello world!](hello-world/main.go)
- [基础](overview/main.go)
- [教程: 在线人数](tutorial/online-visitors/main.go)
- [教程: A Todo MVC Application using Iris and Vue.js](https://hackernoon.com/a-todo-mvc-application-using-iris-and-vue-js-5019ff870064)
- [教程: 结合 BoltDB 生成短网址](https://medium.com/@kataras/a-url-shortener-service-using-go-iris-and-bolt-4182f0b00ae7)
- [教程: 用安卓设备搭建服务器 (**MUST**)](https://twitter.com/ThePracticalDev/status/892022594031017988)
- [POC: Convert the medium-sized project "Parrot" from native to Iris](https://github.com/iris-contrib/parrot)
- [POC: Isomorphic react/hot reloadable/redux/css-modules starter kit](https://github.com/kataras/iris-starter-kit)
- [教程: DropzoneJS 上传](tutorial/dropzonejs)
- [教程: Caddy 服务器使用](tutorial/caddy)
- [教程: Iris + MongoDB](https://medium.com/go-language/iris-go-framework-mongodb-552e349eab9c)

### 目录结构

Iris 是个底层框架, 对 MVC 模式有很好的支持，但不限制文件夹结构，你可以随意组织你的代码。

如何组织代码取决于你的需求. 我们无法告诉你如何设计程序，但你可以仔细查看下面的示例，也许有些片段可以直接放到你的程序里。

- [引导模式架构](structuring/bootstrap)
- [MVC 存储层与服务层](structuring/mvc-plus-repository-and-service-layers)
- [登录演示 (MVC 使用独立包组织)](structuring/login-mvc-single-responsibility-package)
- [登录演示 (MVC 数据模型, 数据源, 存储 和 服务层)](structuring/login-mvc)

### HTTP 监听

- [基础用法](http-listening/listen-addr/main.go)
    * [忽略错误信息](http-listening/listen-addr/omit-server-errors/main.go)
- [UNIX socket file](http-listening/listen-unix/main.go)
- [TLS](http-listening/listen-tls/main.go)
- [Letsencrypt (自动认证)](http-listening/listen-letsencrypt/main.go)
- [进程关闭通知](http-listening/notify-on-shutdown/main.go)
- 自定义 TCP 监听器
    * [通用 net.Listener](http-listening/custom-listener/main.go)
    * [SO_REUSEPORT for unix systems](http-listening/custom-listener/unix-reuseport/main.go)
- 自定义 HTTP 服务
    * [easy way](http-listening/custom-httpserver/easy-way/main.go)
    * [std way](http-listening/custom-httpserver/std-way/main.go)
    * [多个服务示例](http-listening/custom-httpserver/multi/main.go)
- 优雅关闭
    * [使用 `RegisterOnInterrupt`](http-listening/graceful-shutdown/default-notifier/main.go)
    * [自定义通知](http-listening/graceful-shutdown/custom-notifier/main.go)

### 配置

- [基本配置方式](configuration/functional/main.go)
- [Struct 方式配置](configuration/from-configuration-structure/main.go)
- [导入 YAML 配置文件](configuration/from-yaml-file/main.go)
    * [多实例共享配置](configuration/from-yaml-file/shared-configuration/main.go)
- [导入 TOML 配置文件](configuration/from-toml-file/main.go)

### 路由、路由分组、路径动态参数、路由参数处理宏 、 自定义上下文

* `app.Get("{userid:int min(1)}", myHandler)`
* `app.Post("{asset:path}", myHandler)`
* `app.Put("{custom:string regexp([a-z]+)}", myHandler)`

提示: 不同于其他路由处理, iris 路由可以处理以下各种情况:
```go
// 匹配静态前缀 "/assets/" 的各种请求
app.Get("/assets/{asset:path}", assetsWildcardHandler)

// 只匹配 GET "/"
app.Get("/", indexHandler)
// 只匹配 GET "/about"
app.Get("/about", aboutHandler)

// 匹配前缀为 "/profile/" 的所有 GET 请求
// 接着是其余部分的匹配
app.Get("/profile/{username:string}", userHandler)
// 只匹配 "/profile/me" GET 请求，
// 这和 /profile/{username:string} 
// 或跟通配符 {root:path} 不冲突
app.Get("/profile/me", userHandler)

// 匹配所有前缀为 /users/ 的 GET 请求
// 参数为数字，且 >= 1
app.Get("/user/{userid:int min(1)}", getUserHandler)
// 匹配所有前缀为 /users/ 的 DELETE 请求
// 参数为数字，且 >= 1
app.Delete("/user/{userid:int min(1)}", deleteUserHandler)

// 匹配所有 GET 请求，除了 "/", "/about", 或其他以 "/assets/" 开头
// 因为它不会与其他路线冲突。
app.Get("{root:path}", rootWildcardHandler)
```

可以浏览以下示例，以便更好理解

- [概览](routing/overview/main.go)
- [基本使用](routing/basic/main.go)
- [控制器](mvc)
- [自定义 HTTP 错误](routing/http-errors/main.go)
- [动态路径](routing/dynamic-path/main.go)
    * [根级通配符路径](routing/dynamic-path/root-wildcard/main.go)
- [反向路由](routing/reverse/main.go)
- [自定义包装](routing/custom-wrapper/main.go)
- 自定义上下文
    * [方法重写](routing/custom-context/method-overriding/main.go)
    * [新实现方式](routing/custom-context/new-implementation/main.go)
- [路由状态](routing/route-state/main.go)
- [中间件定义](routing/writing-a-middleware)
    * [路由前](routing/writing-a-middleware/per-route/main.go)
    * [全局](routing/writing-a-middleware/globally/main.go)

### hero (输出的一种高效包装模式)

- [基础](hero/basic/main.go)
- [概览](hero/overview)

### MVC 模式

![](mvc/web_mvc_diagram.png)

Iris **对 MVC (Model View Controller) 有一流的支持**, 在 Go 社区里是独一无二的。

Iris 支持快速的请求数据，模型，持久性数据和绑定。

**特点**

All HTTP Methods are supported, for example if want to serve `GET`
then the controller should have a function named `Get()`,
you can define more than one method function to serve in the same Controller.

Serve custom controller's struct's methods as handlers with custom paths(even with regex parametermized path) via the `BeforeActivation` custom event callback, per-controller. Example:

```go
import (
    "github.com/kataras/iris"
    "github.com/kataras/iris/mvc"
)

func main() {
    app := iris.New()
    mvc.Configure(app.Party("/root"), myMVC)
    app.Run(iris.Addr(":8080"))
}

func myMVC(app *mvc.Application) {
    // app.Register(...)
    // app.Router.Use/UseGlobal/Done(...)
    app.Handle(new(MyController))
}

type MyController struct {}

func (m *MyController) BeforeActivation(b mvc.BeforeActivation) {
    // b.Dependencies().Add/Remove
    // b.Router().Use/UseGlobal/Done // and any standard API call you already know

    // 1-> Method
    // 2-> Path
    // 3-> The controller's function name to be parsed as handler
    // 4-> Any handlers that should run before the MyCustomHandler
    b.Handle("GET", "/something/{id:long}", "MyCustomHandler", anyMiddleware...)
}

// GET: http://localhost:8080/root
func (m *MyController) Get() string { return "Hey" }

// GET: http://localhost:8080/root/something/{id:long}
func (m *MyController) MyCustomHandler(id int64) string { return "MyCustomHandler says Hey" }
```

Persistence data inside your Controller struct (share data between requests)
by defining services to the Dependencies or have a `Singleton` controller scope.

Share the dependencies between controllers or register them on a parent MVC Application, and ability
to modify dependencies per-controller on the `BeforeActivation` optional event callback inside a Controller,
i.e `func(c *MyController) BeforeActivation(b mvc.BeforeActivation) { b.Dependencies().Add/Remove(...) }`.

Access to the `Context` as a controller's field(no manual binding is neede) i.e `Ctx iris.Context` or via a method's input argument, i.e `func(ctx iris.Context, otherArguments...)`.

Models inside your Controller struct (set-ed at the Method function and rendered by the View).
You can return models from a controller's method or set a field in the request lifecycle
and return that field to another method, in the same request lifecycle.

Flow as you used to, mvc application has its own `Router` which is a type of `iris/router.Party`, the standard iris api.
`Controllers` can be registered to any `Party`, including Subdomains, the Party's begin and done handlers work as expected.

Optional `BeginRequest(ctx)` function to perform any initialization before the method execution,
useful to call middlewares or when many methods use the same collection of data.

Optional `EndRequest(ctx)` function to perform any finalization after any method executed.

Inheritance, recursively, see for example our `mvc.SessionController`, it has the `Session *sessions.Session` and `Manager *sessions.Sessions` as embedded fields
which are filled by its `BeginRequest`, [here](https://github.com/kataras/iris/blob/master/mvc/session_controller.go).
This is just an example, you could use the `sessions.Session` which returned from the manager's `Start` as a dynamic dependency to the MVC Application, i.e
`mvcApp.Register(sessions.New(sessions.Config{Cookie: "iris_session_id"}).Start)`.

Access to the dynamic path parameters via the controller's methods' input arguments, no binding is needed.
When you use the Iris' default syntax to parse handlers from a controller, you need to suffix the methods
with the `By` word, uppercase is a new sub path. Example:

If `mvc.New(app.Party("/user")).Handle(new(user.Controller))`

- `func(*Controller) Get()` - `GET:/user`.
- `func(*Controller) Post()` - `POST:/user`.
- `func(*Controller) GetLogin()` - `GET:/user/login`
- `func(*Controller) PostLogin()` - `POST:/user/login`
- `func(*Controller) GetProfileFollowers()` - `GET:/user/profile/followers`
- `func(*Controller) PostProfileFollowers()` - `POST:/user/profile/followers`
- `func(*Controller) GetBy(id int64)` - `GET:/user/{param:long}`
- `func(*Controller) PostBy(id int64)` - `POST:/user/{param:long}`

If `mvc.New(app.Party("/profile")).Handle(new(profile.Controller))`

- `func(*Controller) GetBy(username string)` - `GET:/profile/{param:string}`

If `mvc.New(app.Party("/assets")).Handle(new(file.Controller))`

- `func(*Controller) GetByWildard(path string)` - `GET:/assets/{param:path}`

    Supported types for method functions receivers: int, int64, bool and string.

Response via output arguments, optionally, i.e

```go
func(c *ExampleController) Get() string |
                                (string, string) |
                                (string, int) |
                                int |
                                (int, string) |
                                (string, error) |
                                error |
                                (int, error) |
                                (any, bool) |
                                (customStruct, error) |
                                customStruct |
                                (customStruct, int) |
                                (customStruct, string) |
                                mvc.Result or (mvc.Result, error)
```

where [mvc.Result](https://github.com/kataras/iris/blob/master/mvc/func_result.go) is an interface which contains only that function: `Dispatch(ctx iris.Context)`.

## Iris MVC 模式代码复用

By creating components that are independent of one another, developers are able to reuse components quickly and easily in other applications. The same (or similar) view for one application can be refactored for another application with different data because the view is simply handling how the data is being displayed to the user.

If you're new to back-end web development read about the MVC architectural pattern first, a good start is that [wikipedia article](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller).

参考下面的示例

- [Hello world](mvc/hello-world/main.go) **UPDATED**
- [Session Controller](mvc/session-controller/main.go) **UPDATED**
- [Overview - Plus Repository and Service layers](mvc/overview) **UPDATED**
- [Login showcase - Plus Repository and Service layers](mvc/login) **UPDATED**
- [Singleton](mvc/singleton) **NEW**
- [Websocket Controller](mvc/websocket) **NEW**
- [Register Middleware](mvc/middleware) **NEW**
- [Vue.js Todo MVC](tutorial/vuejs-todo-mvc) **NEW**

### 子域名

- [单域名](subdomains/single/main.go)
- [多域名](subdomains/multi/main.go)
- [通配符](subdomains/wildcard/main.go)
- [WWW](subdomains/www/main.go)
- [快速跳转](subdomains/redirect/main.go)

### 改造 `http.Handler/HandlerFunc`

- [From func(w http.ResponseWriter, r *http.Request, next http.HandlerFunc)](convert-handlers/negroni-like/main.go)
- [From http.Handler or http.HandlerFunc](convert-handlers/nethttp/main.go)
- [From func(http.HandlerFunc) http.HandlerFunc](convert-handlers/real-usecase-raven/writing-middleware/main.go)

### 视图

| 模板引擎 | 调用声明 |
| -----------|-------------|
| template/html | `iris.HTML(...)`       |
| django        | `iris.Django(...)`     |
| handlebars    | `iris.Handlebars(...)` |
| amber         | `iris.Amber(...)`      |
| pug(jade)     | `iris.Pug(...)`        |

- [Overview](view/overview/main.go)
- [Hi](view/template_html_0/main.go)
- [A simple Layout](view/template_html_1/main.go)
- [Layouts: `yield` and `render` tmpl funcs](view/template_html_2/main.go)
- [The `urlpath` tmpl func](view/template_html_3/main.go)
- [The `url` tmpl func](view/template_html_4/main.go)
- [Inject Data Between Handlers](view/context-view-data/main.go)
- [Embedding Templates Into App Executable File](view/embedding-templates-into-app/main.go)
- [Write to a custom `io.Writer`](view/write-to)
- [Greeting with Pug (Jade)`](view/template_pug_0)
- [Pug (Jade) Actions`](view/template_pug_1)
- [Pug (Jade) Includes`](view/template_pug_2)
- [Pug (Jade) Extends`](view/template_pug_3)

You can serve [quicktemplate](https://github.com/valyala/quicktemplate) and [hero templates](https://github.com/shiyanhui/hero/hero) files too, simply by using the `context#ResponseWriter`, take a look at the [http_responsewriter/quicktemplate](http_responsewriter/quicktemplate) and [http_responsewriter/herotemplate](http_responsewriter/herotemplate) examples.

### 认证

- [Basic Authentication](authentication/basicauth/main.go)
- [OAUth2](authentication/oauth2/main.go)
- [JWT](experimental-handlers/jwt/main.go)
- [Sessions](#sessions)

### 文件服务器

- [Favicon](file-server/favicon/main.go)
- [Basic](file-server/basic/main.go)
- [Embedding Files Into App Executable File](file-server/embedding-files-into-app/main.go)
- [Embedding Gziped Files Into App Executable File](file-server/embedding-gziped-files-into-app/main.go) **NEW**
- [Send/Force-Download Files](file-server/send-files/main.go)
- Single Page Applications
    * [single Page Application](file-server/single-page-application/basic/main.go)
    * [embedded Single Page Application](file-server/single-page-application/embedded-single-page-application/main.go)
    * [embedded Single Page Application with other routes](file-server/single-page-application/embedded-single-page-application-with-other-routes/main.go)

### How to Read from `context.Request() *http.Request`

- [Read JSON](http_request/read-json/main.go)
- [Read XML](http_request/read-xml/main.go)
- [Read Form](http_request/read-form/main.go)
- [Read Custom per type](http_request/read-custom-per-type/main.go)
- [Read Custom via Unmarshaler](http_request/read-custom-via-unmarshaler/main.go)
- [Upload/Read File](http_request/upload-file/main.go)
- [Upload multiple files with an easy way](http_request/upload-files/main.go)

> The `context.Request()` returns the same *http.Request you already know, these examples show some places where the  Context uses this object. Besides that you can use it as you did before iris.

### How to Write to `context.ResponseWriter() http.ResponseWriter`

- [Write `valyala/quicktemplate` templates](http_responsewriter/quicktemplate)
- [Write `shiyanhui/hero` templates](http_responsewriter/herotemplate)
- [Text, Markdown, HTML, JSON, JSONP, XML, Binary](http_responsewriter/write-rest/main.go)
- [Write Gzip](http_responsewriter/write-gzip/main.go)
- [Stream Writer](http_responsewriter/stream-writer/main.go)
- [Transactions](http_responsewriter/transactions/main.go)
- [SSE (third-party package usage for server-side events)](http_responsewriter/sse-third-party/main.go)

> The `context/context#ResponseWriter()` returns an enchament version of a http.ResponseWriter, these examples show some places where the Context uses this object. Besides that you can use it as you did before iris.

### ORM

- [Using xorm(Mysql, MyMysql, Postgres, Tidb, **SQLite**, MsSql, MsSql, Oracle)](orm/xorm/main.go)

### 其他

- [Request Logger](http_request/request-logger/main.go)
    * [log requests to a file](http_request/request-logger/request-logger-file/main.go)
- [Localization and Internationalization](miscellaneous/i18n/main.go)
- [Recovery](miscellaneous/recover/main.go)
- [Profiling (pprof)](miscellaneous/pprof/main.go)
- [Internal Application File Logger](miscellaneous/file-logger/main.go)
- [Google reCAPTCHA](miscellaneous/recaptcha/main.go) 

### 试验性质处理器

- [Casbin wrapper](experimental-handlers/casbin/wrapper/main.go)
- [Casbin middleware](experimental-handlers/casbin/middleware/main.go)
- [Cloudwatch](experimental-handlers/cloudwatch/simple/main.go)
- [CORS](experimental-handlers/cors/simple/main.go)
- [JWT](experimental-handlers/jwt/main.go)
- [Newrelic](experimental-handlers/newrelic/simple/main.go)
- [Prometheus](experimental-handlers/prometheus/simple/main.go)
- [Secure](experimental-handlers/secure/simple/main.go)
- [Tollboothic](experimental-handlers/tollboothic/limit-handler/main.go)
- [Cross-Site Request Forgery Protection](experimental-handlers/csrf/main.go)

#### 更多

https://github.com/kataras/iris/tree/master/middleware#third-party-handlers

### 自动 API 文档

- [yaag](apidoc/yaag/main.go)

### 测试

The `httptest` package is your way for end-to-end HTTP testing, it uses the httpexpect library created by our friend, [gavv](https://github.com/gavv).

[Example](testing/httptest/main_test.go)

### 缓存

Iris 独立缓存包 [package](https://github.com/kataras/iris/tree/master/cache).

- [简单示例](cache/simple/main.go)
- [客户端 (304)](cache/client-side/main.go) - context 方法

> 可以随意使用自定义的缓存包。

### Cookies

- [Basic](cookies/basic/main.go)
- [Encode/Decode (securecookie)](cookies/securecookie/main.go)

### Sessions

Iris session 管理独立包 [package](https://github.com/kataras/iris/tree/master/sessions).

- [Overview](sessions/overview/main.go)
- [Standalone](sessions/standalone/main.go)
- [Secure Cookie](sessions/securecookie/main.go)
- [Flash Messages](sessions/flash-messages/main.go)
- [Databases](sessions/database)
    * [Badger](sessions/database/badger/main.go)
    * [Redis](sessions/database/redis/main.go)

> 可以随意使用自定义的 Session 管理包。

### Websockets

iris websocket library lives on its own [package](https://github.com/kataras/iris/tree/master/websocket).

The package is designed to work with raw websockets although its API is similar to the famous [socket.io](https://socket.io). I have read an article recently and I felt very contented about my decision to design a **fast** websocket-**only** package for Iris and not a backwards socket.io-like package. You can read that article by following this link: https://medium.com/@ivanderbyl/why-you-don-t-need-socket-io-6848f1c871cd.

- [Chat](websocket/chat/main.go)
- [Native Messages](websocket/native-messages/main.go)
- [Connection List](websocket/connectionlist/main.go)
- [TLS Enabled](websocket/secure/main.go)
- [Custom Raw Go Client](websocket/custom-go-client/main.go)
- [Third-Party socket.io](websocket/third-party-socketio/main.go)

> 如果你愿意，你可以自由使用你自己喜欢的websockets包。

### Typescript 自动化工具

Typescript 自动化工具独立库： [https://github.com/kataras/iris/tree/master/typescript](https://github.com/kataras/iris/tree/master/typescript) **包含相关示例**

### 大兄弟

进一步学习可通过 [godocs](https://godoc.org/github.com/kataras/iris) 和 https://docs.iris-go.com

不要忘记点赞 [star or watch](https://github.com/kataras/iris/stargazers) 这个项目会一直跟进最新趋势。
# Caddy loves Iris

The `Caddyfile` shows how you can use caddy to listen on ports 80 & 443 and sit in front of iris webserver(s) that serving on a different port (9091 and 9092 in this case; see Caddyfile).

## Running our two web servers

1. Go to `$GOPATH/src/github.com/kataras/iris/_examples/tutorial/caddy/server1`
2. Open a terminal window and execute `go run main.go`
3. Go to `$GOPATH/src/github.com/kataras/iris/_examples/tutorial/caddy/server2`
4. Open a new terminal window and execute `go run main.go`

## Caddy installation

1. Download caddy: https://caddyserver.com/download
2. Extract its contents where the `Caddyfile` is located, the `$GOPATH/src/github.com/kataras/iris/_examples/tutorial/caddy` in this case
3. Open, read and modify the `Caddyfile` to see by yourself how easy it is to configure the servers
4. Run `caddy` directly or open a terminal window and execute `caddy`
5. Go to `https://example.com` and `https://api.example.com/user/42`


## Notes

Iris has the `app.Run(iris.AutoTLS(":443", "example.com", "mail@example.com"))` which does
the exactly same thing but caddy is a great tool that helps you when you run multiple web servers from one host machine, i.e iris, apache, tomcat.# A Todo MVC Application using Iris and Vue.js

Vue.js is a front-end framework for building web applications using javascript. It has a blazing fast Virtual DOM renderer.

Iris is a back-end framework for building web applications using The Go Programming Language (disclaimer: author here). It's one of the fastest and featured web frameworks out there. We wanna use this to serve our "todo service".

## The Tools

Programming Languages are just tools for us, but we need a safe, fast and “cross-platform” programming language to power our service.

[Go](https://golang.org) is a [rapidly growing](https://www.tiobe.com/tiobe-index/) open source programming language designed for building simple, fast, and reliable software. Take a look [here](https://github.com/golang/go/wiki/GoUsers) which great companies use Go to power their services.

### Install the Go Programming Language

Extensive information about downloading & installing Go can be found [here](https://golang.org/dl/).

[![](https://i3.ytimg.com/vi/9x-pG3lvLi0/hqdefault.jpg)](https://youtu.be/9x-pG3lvLi0)

> Maybe [Windows](https://www.youtube.com/watch?v=WT5mTznJBS0) or [Mac OS X](https://www.youtube.com/watch?v=5qI8z_lB5Lw) user?

> The article does not contain an introduction to the language itself, if you’re a newcomer I recommend you to bookmark this article, [learn](https://github.com/golang/go/wiki/Learn) the language’s fundamentals and come back later on.

## The Dependencies

Many articles have been written, in the past, that lead developers not to use a web framework because they are useless and "bad". I have to tell you that there is no such thing, it always depends on the (web) framework that you’re going to use. At production environment,  we don’t have the time or the experience to code everything that we wanna use in the applications, and if we could are we sure that we can do better and safely than others? In short term: **Good frameworks are helpful tools for any developer, company or startup and "bad" frameworks are waste of time, crystal clear.**

You’ll need two dependencies:

1. Vue.js, for our client-side requirements. Download it from [here](https://vuejs.org/), latest v2.
2. The Iris Web Framework, for our server-side requirements. Can be found [here](https://github.com/kataras/iris), latest v10.

> If you have Go already installed then just execute `go get -u github.com/kataras/iris` to install the Iris Web Framework.

## Start

If we are all in the same page, it’s time to learn how we can create a live todo application that will be easy to deploy and extend even more!

We're going to use a vue.js todo application which uses browser'
s local storage and doesn't have any user-specified features like live sync between browser's tabs, you can find the original version inside the vue's [docs](https://vuejs.org/v2/examples/todomvc.html).

Assuming that you know how %GOPATH% works, create an empty folder, i.e "vuejs-todo-mvc" in the %GOPATH%/src directory, there you will create those files:

- web/public/js/app.js
- web/public/index.html
- todo/item.go
- todo/service.go
- web/controllers/todo_controller.go
- web/main.go

_Read the comments in the source code, they may be very helpful_

### The client-side (vue.js)

```js
/* file: vuejs-todo-mvc/web/public/js/app.js */
// Full spec-compliant TodoMVC with Iris
// and hash-based routing in ~200 effective lines of JavaScript.

var socket = new Ws("ws://localhost:8080/todos/sync");

socket.On("saved", function () {
  // console.log("receive: on saved");
  fetchTodos(function (items) {
    app.todos = items
  });
});


function fetchTodos(onComplete) {
  axios.get("/todos").then(response => {
    if (response.data === null) {
      return;
    }

    onComplete(response.data);
  });
}

var todoStorage = {
  fetch: function () {
    var todos = [];
    fetchTodos(function (items) {
      for (var i = 0; i < items.length; i++) {
        todos.push(items[i]);
      }
    });
    return todos;
  },
  save: function (todos) {
    axios.post("/todos", JSON.stringify(todos)).then(response => {
      if (!response.data.success) {
        window.alert("saving had a failure");
        return;
      }
      // console.log("send: save");
      socket.Emit("save")
    });
  }
}

// visibility filters
var filters = {
  all: function (todos) {
    return todos
  },
  active: function (todos) {
    return todos.filter(function (todo) {
      return !todo.completed
    })
  },
  completed: function (todos) {
    return todos.filter(function (todo) {
      return todo.completed
    })
  }
}

// app Vue instance
var app = new Vue({
  // app initial state
  data: {
    todos: todoStorage.fetch(),
    newTodo: '',
    editedTodo: null,
    visibility: 'all'
  },

  // we will not use the "watch" as it works with the fields like "hasChanges"
  // and callbacks to make it true but let's keep things very simple as it's just a small getting started. 
  // // watch todos change for persistence
  // watch: {
  //   todos: {
  //     handler: function (todos) {
  //       if (app.hasChanges) {
  //         todoStorage.save(todos);
  //         app.hasChanges = false;
  //       }

  //     },
  //     deep: true
  //   }
  // },

  // computed properties
  // http://vuejs.org/guide/computed.html
  computed: {
    filteredTodos: function () {
      return filters[this.visibility](this.todos)
    },
    remaining: function () {
      return filters.active(this.todos).length
    },
    allDone: {
      get: function () {
        return this.remaining === 0
      },
      set: function (value) {
        this.todos.forEach(function (todo) {
          todo.completed = value
        })
        this.notifyChange();
      }
    }
  },

  filters: {
    pluralize: function (n) {
      return n === 1 ? 'item' : 'items'
    }
  },

  // methods that implement data logic.
  // note there's no DOM manipulation here at all.
  methods: {
    notifyChange: function () {
      todoStorage.save(this.todos)
    },
    addTodo: function () {
      var value = this.newTodo && this.newTodo.trim()
      if (!value) {
        return
      }
      this.todos.push({
        id: this.todos.length + 1, // just for the client-side.
        title: value,
        completed: false
      })
      this.newTodo = ''
      this.notifyChange();
    },

    completeTodo: function (todo) {
      if (todo.completed) {
        todo.completed = false;
      } else {
        todo.completed = true;
      }
      this.notifyChange();
    },
    removeTodo: function (todo) {
      this.todos.splice(this.todos.indexOf(todo), 1)
      this.notifyChange();
    },

    editTodo: function (todo) {
      this.beforeEditCache = todo.title
      this.editedTodo = todo
    },

    doneEdit: function (todo) {
      if (!this.editedTodo) {
        return
      }
      this.editedTodo = null
      todo.title = todo.title.trim();
      if (!todo.title) {
        this.removeTodo(todo);
      }
      this.notifyChange();
    },

    cancelEdit: function (todo) {
      this.editedTodo = null
      todo.title = this.beforeEditCache
    },

    removeCompleted: function () {
      this.todos = filters.active(this.todos);
      this.notifyChange();
    }
  },

  // a custom directive to wait for the DOM to be updated
  // before focusing on the input field.
  // http://vuejs.org/guide/custom-directive.html
  directives: {
    'todo-focus': function (el, binding) {
      if (binding.value) {
        el.focus()
      }
    }
  }
})

// handle routing
function onHashChange() {
  var visibility = window.location.hash.replace(/#\/?/, '')
  if (filters[visibility]) {
    app.visibility = visibility
  } else {
    window.location.hash = ''
    app.visibility = 'all'
  }
}

window.addEventListener('hashchange', onHashChange)
onHashChange()

// mount
app.$mount('.todoapp')
```

Let's add our view, the static html.

```html
<!-- file: vuejs-todo-mvc/web/public/index.html -->
<!doctype html>
<html data-framework="vue">

<head>
  <meta charset="utf-8">
  <title>Iris + Vue.js • TodoMVC</title>
  <link rel="stylesheet" href="https://unpkg.com/todomvc-app-css@2.0.4/index.css">
  <!-- this needs to be loaded before guide's inline scripts -->
  <script src="https://vuejs.org/js/vue.js"></script>
  <!-- $http -->
  <script src="https://unpkg.com/axios/dist/axios.min.js"></script>
  <!-- -->
  <script src="https://unpkg.com/director@1.2.8/build/director.js"></script>
  <!-- websocket sync between multiple tabs -->
  <script src="/todos/iris-ws.js"></script>
  <!-- -->
  <style>
    [v-cloak] {
      display: none;
    }
  </style>
</head>

<body>
  <section class="todoapp">
    <header class="header">
      <h1>todos</h1>
      <input class="new-todo" autofocus autocomplete="off" placeholder="What needs to be done?" v-model="newTodo" @keyup.enter="addTodo">
    </header>
    <section class="main" v-show="todos.length" v-cloak>
      <input class="toggle-all" type="checkbox" v-model="allDone">
      <ul class="todo-list">
        <li v-for="todo in filteredTodos" class="todo" :key="todo.id" :class="{ completed: todo.completed, editing: todo == editedTodo }">
          <div class="view">
             <!-- v-model="todo.completed" -->
            <input class="toggle" type="checkbox" @click="completeTodo(todo)">
            <label @dblclick="editTodo(todo)">{{ todo.title }}</label>
            <button class="destroy" @click="removeTodo(todo)"></button>
          </div>
          <input class="edit" type="text" v-model="todo.title" v-todo-focus="todo == editedTodo" @blur="doneEdit(todo)" @keyup.enter="doneEdit(todo)"
            @keyup.esc="cancelEdit(todo)">
        </li>
      </ul>
    </section>
    <footer class="footer" v-show="todos.length" v-cloak>
      <span class="todo-count">
        <strong>{{ remaining }}</strong> {{ remaining | pluralize }} left
      </span>
      <ul class="filters">
        <li>
          <a href="#/all" :class="{ selected: visibility == 'all' }">All</a>
        </li>
        <li>
          <a href="#/active" :class="{ selected: visibility == 'active' }">Active</a>
        </li>
        <li>
          <a href="#/completed" :class="{ selected: visibility == 'completed' }">Completed</a>
        </li>
      </ul>
      <button class="clear-completed" @click="removeCompleted" v-show="todos.length > remaining">
        Clear completed
      </button>
    </footer>
  </section>
  <footer class="info">
    <p>Double-click to edit a todo</p>
  </footer>

  <script src="/js/app.js"></script>
</body>

</html>
```

### The server-side (iris)

Our view model.

```go
// file: vuejs-todo-mvc/todo/item.go
package todo

type Item struct {
    SessionID string `json:"-"`
    ID        int64  `json:"id,omitempty"`
    Title     string `json:"title"`
    Completed bool   `json:"completed"`
}
```

Our service.

```go
// file: vuejs-todo-mvc/todo/service.go
package todo

import (
    "sync"
)

type Service interface {
    Get(owner string) []Item
    Save(owner string, newItems []Item) error
}

type MemoryService struct {
    // key = session id, value the list of todo items that this session id has.
    items map[string][]Item
    // protected by locker for concurrent access.
    mu sync.RWMutex
}

func NewMemoryService() *MemoryService {
    return &MemoryService{
        items: make(map[string][]Item, 0),
    }
}

func (s *MemoryService) Get(sessionOwner string) []Item {
    s.mu.RLock()
    items := s.items[sessionOwner]
    s.mu.RUnlock()

    return items
}

func (s *MemoryService) Save(sessionOwner string, newItems []Item) error {
    var prevID int64
    for i := range newItems {
        if newItems[i].ID == 0 {
            newItems[i].ID = prevID
            prevID++
        }
    }

    s.mu.Lock()
    s.items[sessionOwner] = newItems
    s.mu.Unlock()
    return nil
}
```

We are going to use some of the MVC functionalities of the iris web framework here but you can do the same with the standard API as well.

```go
// file: vuejs-todo-mvc/controllers/todo_controller.go
package controllers

import (
    "vuejs-todo-mvc/todo"

    "github.com/kataras/iris"
    "github.com/kataras/iris/mvc"
    "github.com/kataras/iris/sessions"
    "github.com/kataras/iris/websocket"
)

// TodoController is our TODO app's web controller.
type TodoController struct {
    Service todo.Service

    Session *sessions.Session
}

// BeforeActivation called once before the server ran, and before
// the routes and dependencies binded.
// You can bind custom things to the controller, add new methods, add middleware,
// add dependencies to the struct or the method(s) and more.
func (c *TodoController) BeforeActivation(b mvc.BeforeActivation) {
    // this could be binded to a controller's function input argument
    // if any, or struct field if any:
    b.Dependencies().Add(func(ctx iris.Context) (items []todo.Item) {
        ctx.ReadJSON(&items)
        return
    })
}

// Get handles the GET: /todos route.
func (c *TodoController) Get() []todo.Item {
    return c.Service.Get(c.Session.ID())
}

// PostItemResponse the response data that will be returned as json
// after a post save action of all todo items.
type PostItemResponse struct {
    Success bool `json:"success"`
}

var emptyResponse = PostItemResponse{Success: false}

// Post handles the POST: /todos route.
func (c *TodoController) Post(newItems []todo.Item) PostItemResponse {
    if err := c.Service.Save(c.Session.ID(), newItems); err != nil {
        return emptyResponse
    }

    return PostItemResponse{Success: true}
}

func (c *TodoController) GetSync(conn websocket.Connection) {
    conn.Join(c.Session.ID())
    conn.On("save", func() { // "save" event from client.
        conn.To(c.Session.ID()).Emit("saved", nil) // fire a "saved" event to the rest of the clients w.
    })

    conn.Wait()
}
```

And finally our main application's endpoint.

```go
// file: web/main.go
package main

import (
    "vuejs-todo-mvc/todo"
    "vuejs-todo-mvc/web/controllers"

    "github.com/kataras/iris"
    "github.com/kataras/iris/sessions"
    "github.com/kataras/iris/websocket"

    "github.com/kataras/iris/mvc"
)

func main() {
    app := iris.New()

    // serve our app in public, public folder
    // contains the client-side vue.js application,
    // no need for any server-side template here,
    // actually if you're going to just use vue without any
    // back-end services, you can just stop afer this line and start the server.
    app.StaticWeb("/", "./public")

    // configure the http sessions.
    sess := sessions.New(sessions.Config{
        Cookie: "iris_session",
    })

    // configure the websocket server.
    ws := websocket.New(websocket.Config{})

    // create a sub router and register the client-side library for the iris websockets,
    // you could skip it but iris websockets supports socket.io-like API.
    todosRouter := app.Party("/todos")
    // http://localhost:8080/todos/iris-ws.js
    // serve the javascript client library to communicate with
    // the iris high level websocket event system.
    todosRouter.Any("/iris-ws.js", websocket.ClientHandler())

    // create our mvc application targeted to /todos relative sub path.
    todosApp := mvc.New(todosRouter)

    // any dependencies bindings here...
    todosApp.Register(
        todo.NewMemoryService(),
        sess.Start,
        ws.Upgrade,
    )

    // controllers registration here...
    todosApp.Handle(new(controllers.TodoController))

    // start the web server at http://localhost:8080
    app.Run(iris.Addr(":8080"), iris.WithoutVersionChecker)
}
```

Run the Iris web server you've just created by executing `go run main.go` from your current path (%GOPATH%/src/%your_folder%/web/).

```sh
$ go run main.go
Now listening on: http://localhost:8080
Application Started. Press CTRL+C to shut down.
_
```

Open one or more browser tabs at: http://localhost:8080 and have fun!

![](screen.png)

### Download the Source Code

The whole project, all the files you saw in this article are located at: https://github.com/kataras/iris/tree/master/_examples/tutorial/vuejs-todo-mvc

## References

https://vuejs.org/v2/examples/todomvc.html (using browser's local storage)

https://github.com/kataras/iris/tree/master/_examples/mvc (mvc examples and features overview repository)

## Thank you, once again

Happy new year and thank you for your pattience, once again:) Don't hesitate to post any questions and provide feedback(I'm very active dev therefore you will be heard here!)

Don't forget to check out my medium profile and twitter as well, I'm posting some (useful) stuff there too:)

- https://medium.com/@kataras 
- https://twitter.com/MakisMaropoulos
# Articles

* [How to build a file upload form using DropzoneJS and Go](https://hackernoon.com/how-to-build-a-file-upload-form-using-dropzonejs-and-go-8fb9f258a991)
* [How to display existing files on server using DropzoneJS and Go](https://hackernoon.com/how-to-display-existing-files-on-server-using-dropzonejs-and-go-53e24b57ba19)

# Content

This is the part 2 of 2 in DropzoneJS + Go series.

- [Part 1: How to build a file upload form](README.md)
- [Part 2: How to display existing files on server](README_PART2.md)

# DropzoneJS + Go: How to display existing files on server

In this tutorial, we will show you how to display existing files on the server when using DropzoneJS and Go. This tutorial is based on [How to build a file upload form using DropzoneJS and Go](README.md). Make sure you have read it before proceeding to content in this tutorial.

## Table Of Content

- [Preparation](#preparation)
- [Modify the Server side](#modify-the-server-side)
- [Modify the Client side](#modify-the-client-side)
- [References](#references)
- [The End](#the-end)

## Preparation

Install the go package "github.com/nfnt/resize" with `go get github.com/nfnt/resize`, we need it to create thumbnails.

In previous [tutorial](README.md). We have already set up a proper working DropzoneJs upload form. There is no additional file needed for this tutorial. What we need to do is to make some modifications to file below:

1. main.go
2. views/upload.html

Let us get started!

## Modify the Server side

In previous tutorial. All "/upload" does is to store uploaded files to the server directory "./public/uploads". So we need to add a piece of code to retrieve stored files' information (name and size), and return it in JSON format.

Copy the content below to "main.go". Read comments for details.

```go
// main.go

package main

import (
    "image/jpeg"
    "image/png"
    "io"
    "os"
    "path"
    "path/filepath"
    "strings"
    "sync"

    "github.com/kataras/iris"

    "github.com/nfnt/resize" // $ go get -u github.com/nfnt/resize
)

const uploadsDir = "./public/uploads/"

type uploadedFile struct {
    // {name: "", size: } are the dropzone's only requirements.
    Name string `json:"name"`
    Size int64  `json:"size"`
}

type uploadedFiles struct {
    dir   string
    items []uploadedFile
    mu    sync.RWMutex // slices are safe but RWMutex is a good practise for you.
}

// scan the ./public/uploads folder for any files
// add them to a new  uploadedFiles list.
func scanUploads(dir string) *uploadedFiles {
    f := new(uploadedFiles)

    lindex := dir[len(dir)-1]
    if lindex != os.PathSeparator && lindex != '/' {
        dir += string(os.PathSeparator)
    }

    // create directories if necessary
    // and if, then return empty uploaded files; skipping the scan.
    if err := os.MkdirAll(dir, os.FileMode(0666)); err != nil {
        return f
    }

    // otherwise scan the given "dir" for files.
    f.scan(dir)
    return f
}

func (f *uploadedFiles) scan(dir string) {
    f.dir = dir
    filepath.Walk(dir, func(path string, info os.FileInfo, err error) error {

        // if it's directory or a thumbnail we saved earlier, skip it.
        if info.IsDir() || strings.HasPrefix(info.Name(), "thumbnail_") {
            return nil
        }

        f.add(info.Name(), info.Size())
        return nil
    })
}

// add the file's Name and Size to the uploadedFiles memory list
func (f *uploadedFiles) add(name string, size int64) uploadedFile {
    uf := uploadedFile{
        Name: name,
        Size: size,
    }
    f.mu.Lock()
    f.items = append(f.items, uf)
    f.mu.Unlock()

    return uf
}

// create thumbnail 100x100
// and save that to the ./public/uploads/thumbnail_$FILENAME
func (f *uploadedFiles) createThumbnail(uf uploadedFile) {
    file, err := os.Open(path.Join(f.dir, uf.Name))
    if err != nil {
        return
    }
    defer file.Close()

    name := strings.ToLower(uf.Name)

    out, err := os.OpenFile(f.dir+"thumbnail_"+uf.Name,
        os.O_WRONLY|os.O_CREATE, 0666)
    if err != nil {
        return
    }
    defer out.Close()

    if strings.HasSuffix(name, ".jpg") {
        // decode jpeg into image.Image
        img, err := jpeg.Decode(file)
        if err != nil {
            return
        }

        // write new image to file
        resized := resize.Thumbnail(180, 180, img, resize.Lanczos3)
        jpeg.Encode(out, resized,
            &jpeg.Options{Quality: jpeg.DefaultQuality})

    } else if strings.HasSuffix(name, ".png") {
        img, err := png.Decode(file)
        if err != nil {
            return
        }

        // write new image to file
        resized := resize.Thumbnail(180, 180, img, resize.Lanczos3) // slower but better res
        png.Encode(out, resized)
    }
    // and so on... you got the point, this code can be simplify, as a practise.
}

func main() {
    app := iris.New()
    app.RegisterView(iris.HTML("./views", ".html"))

    app.StaticWeb("/public", "./public")

    app.Get("/", func(ctx iris.Context) {
        ctx.View("upload.html")
    })

    files := scanUploads(uploadsDir)

    app.Get("/uploads", func(ctx iris.Context) {
        ctx.JSON(files.items)
    })

    app.Post("/upload", iris.LimitRequestBodySize(10<<20), func(ctx iris.Context) {
        // Get the file from the dropzone request
        file, info, err := ctx.FormFile("file")
        if err != nil {
            ctx.StatusCode(iris.StatusInternalServerError)
            ctx.Application().Logger().Warnf("Error while uploading: %v", err.Error())
            return
        }

        defer file.Close()
        fname := info.Filename

        // Create a file with the same name
        // assuming that you have a folder named 'uploads'
        out, err := os.OpenFile(uploadsDir+fname,
            os.O_WRONLY|os.O_CREATE, 0666)

        if err != nil {
            ctx.StatusCode(iris.StatusInternalServerError)
            ctx.Application().Logger().Warnf("Error while preparing the new file: %v", err.Error())
            return
        }
        defer out.Close()

        io.Copy(out, file)

        // optionally, add that file to the list in order to be visible when refresh.
        uploadedFile := files.add(fname, info.Size)
        go files.createThumbnail(uploadedFile)
    })

    // start the server at http://localhost:8080
    app.Run(iris.Addr(":8080"))
}
```

## Modify the Client side

Copy content below to "./views/upload.html". We will go through modifications individually.

```html
<!-- /views/upload.html -->
<html>

<head>
    <title>DropzoneJS Uploader</title>

    <!-- 1 -->
    <link href="/public/css/dropzone.css" type="text/css" rel="stylesheet" />

    <!-- 2 -->
    <script src="/public/js/dropzone.js"></script>
    <!-- 4 -->
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.10.2/jquery.min.js"></script>
    <!-- 5 -->
    <script>
        Dropzone.options.myDropzone = {
            paramName: "file", // The name that will be used to transfer the file
            init: function () {
                thisDropzone = this;
                // 6
                $.get('/uploads', function (data) {

                    if (data == null) {
                        return;
                    }
                    // 7
                    $.each(data, function (key, value) {
                        var mockFile = { name: value.name, size: value.size };

                        thisDropzone.emit("addedfile", mockFile);
                        thisDropzone.options.thumbnail.call(thisDropzone, mockFile, '/public/uploads/thumbnail_' + value.name);

                        // Make sure that there is no progress bar, etc...
                        thisDropzone.emit("complete", mockFile);
                    });

                });
            }
        };
    </script>
</head>

<body>

    <!-- 3 -->
    <form action="/upload" method="POST" class="dropzone" id="my-dropzone">
        <div class="fallback">
            <input name="file" type="file" multiple />
            <input type="submit" value="Upload" />
        </div>
    </form>
</body>

</html>
```

1. We added Jquery library into our page. This actually not for DropzoneJs directly. We are using Jquery's ajax function **$.get** only. You will see below
2. We added an ID element (my-dropzone) to the form. This is needed because we need to pass configuration values to Dropzone. And to do it, we must have an ID reference of it. So that we can configure it by assigning values to Dropzone.options.myDropzone. A lot of people face confusion when configuring Dropzone. To put it in a simple way. Do not take Dropzone as a Jquery plugin, it has its own syntax and you need to follow it.
3. This starts the main part of modification. What we did here is to pass a function to listen to Dropzone's init event. This event is called when Dropzone is initialized.
4. Retrieve files details from the new "/uploads" via ajax.
5. Create mockFile using values from server. mockFile is simply JavaScript objects with properties of name and size. Then we call Dropzone's **addedfile** and **thumbnail** functions explicitly to put existing files to Dropzone upload area and generate its thumbnail.

### Running the server

Open the terminal at the current project's folder and execute:

```bash
$ go run main.go
Now listening on: http://localhost:8080
Application started. Press CTRL+C to shut down.
```

If you have done it successfully. Now go and upload some images and reload the upload page. Already uploaded files should auto display in Dropzone area.

![with uploaded files screenshot](with_files.png)

## References

- http://www.dropzonejs.com/#server-side-implementation
- https://www.startutorial.com/articles/view/how-to-build-a-file-upload-form-using-dropzonejs-and-php
- https://docs.iris-go.com
- https://github.com/kataras/iris/tree/master/_examples/tutorial/dropzonejs

## The end

Hopefully this simple tutorial helped you with your development.
If you like my post, please follow me on [Twitter](https://twitter.com/makismaropoulos) and help spread the word. I need your support to continue.# Articles

* [How to build a file upload form using DropzoneJS and Go](https://hackernoon.com/how-to-build-a-file-upload-form-using-dropzonejs-and-go-8fb9f258a991)
* [How to display existing files on server using DropzoneJS and Go](https://hackernoon.com/how-to-display-existing-files-on-server-using-dropzonejs-and-go-53e24b57ba19)

# Content

This is the part 1 of 2 in DropzoneJS + Go series.

- [Part 1: How to build a file upload form](README.md)
- [Part 2: How to display existing files on server](README_PART2.md)

# DropzoneJS + Go: How to build a file upload form

[DropzoneJS](https://github.com/enyo/dropzone) is an open source library that provides drag'n'drop file uploads with image previews. It is a great JavaScript library which actually does not even rely on JQuery. 
In this tutorial, we are building a multiple file upload form using DropzoneJS, and the backend will be handled by Go and [Iris](https://iris-go.com).

## Table Of Content

- [Preparation](#preparation)
- [Work with DropzoneJS](#work-with-dropzonejs)
- [Work with Go](#work-with-go)

## Preparation

1. Download [Go(Golang)](https://golang.org/dl), setup your computer as shown there and continue to 2.
2. Install [Iris](https://github.com/kataras/iris); open a terminal and execute `go get -u github.com/kataras/iris`
3. Download DropzoneJS from [this URL](https://raw.githubusercontent.com/enyo/dropzone/master/dist/dropzone.js). DropzoneJS does not rely on JQuery, you will not have to worry that, upgrading JQuery version breaks your application.
4. Download dropzone.css from [this URL](https://raw.githubusercontent.com/enyo/dropzone/master/dist/dropzone.css), if you want some already made css.
5. Create a folder "./public/uploads", this is for storing uploaded files.
6. Create a file "./views/upload.html", this is for the front form page.
7. Create a file "./main.go", this is for handling backend file upload process.

Your folder&file structure should look like this after the preparation:

![folder&file structure](folder_structure.png)

## Work with DropzoneJS

Open file "./views/upload.html" and let us create a DropzoneJs form.

Copy the content below to "./views/upload.html" and we will go through each line of code individually.

```html
<!-- /views/upload.html -->
<html>

<head>
    <title>DropzoneJS Uploader</title>

    <!-- 1 -->
    <link href="/public/css/dropzone.css" type="text/css" rel="stylesheet" />

    <!-- 2 -->
    <script src="/public/js/dropzone.js"></script>
</head>

<body>

    <!-- 3 -->
    <form action="/upload" method="POST" class="dropzone" id="my-dropzone">
        <div class="fallback">
            <input name="file" type="file" multiple />
            <input type="submit" value="Upload" />
        </div>
    </form>
</body>

</html>
```

1. Include the CSS Stylesheet.
2. Include DropzoneJS JavaScript library.
3. Create an upload form with css class "dropzone" and "action" is the route path "/upload". Note that we did create an input filed for fallback mode. This is all handled by DropzoneJS library itself. All we need to do is assign css class "dropzone" to the form. By default, DropzoneJS will find all forms with class "dropzone" and automatically attach itself to it.

## Work with Go

Now you have come to Last part of the tutorial. In this section, we will store files sent from DropzoneJS to the "./public/uploads" folder.

Open "main.go" and copy the code below:

```go
// main.go

package main

import (
    "os"
    "io"
    "strings"

    "github.com/kataras/iris"
)

const uploadsDir = "./public/uploads/"

func main() {
    app := iris.New()

    // Register templates
    app.RegisterView(iris.HTML("./views", ".html"))

    // Make the /public route path to statically serve the ./public/... contents
    app.StaticWeb("/public", "./public")

    // Render the actual form
    // GET: http://localhost:8080
    app.Get("/", func(ctx iris.Context) {
        ctx.View("upload.html")
    })

    // Upload the file to the server
    // POST: http://localhost:8080/upload
    app.Post("/upload", iris.LimitRequestBodySize(10<<20), func(ctx iris.Context) {
        // Get the file from the dropzone request
        file, info, err := ctx.FormFile("file")
        if err != nil {
            ctx.StatusCode(iris.StatusInternalServerError)
            ctx.Application().Logger().Warnf("Error while uploading: %v", err.Error())
            return
        }

        defer file.Close()
        fname := info.Filename

        // Create a file with the same name
        // assuming that you have a folder named 'uploads'
        out, err := os.OpenFile(uploadsDir+fname,
            os.O_WRONLY|os.O_CREATE, 0666)

        if err != nil {
            ctx.StatusCode(iris.StatusInternalServerError)
            ctx.Application().Logger().Warnf("Error while preparing the new file: %v", err.Error())
            return
        }
        defer out.Close()

        io.Copy(out, file)
    })

    // Start the server at http://localhost:8080
    app.Run(iris.Addr(":8080"))
}
```

1. Create a new Iris app.
2. Register and load templates from the "views" folder.
3. Make the "/public" route path to statically serve the ./public/... folder's contents
4. Create a route to serve the upload form.
5. Create a route to handle the POST form data from the DropzoneJS' form 
6. Declare a variable for destination folder.
7. If file is sent to the page, store the file object to a temporary "file" variable.
8. Move uploaded file to destination based on the uploadsDir+uploaded file's name.

### Running the server

Open the terminal at the current project's folder and execute:

```bash
$ go run main.go
Now listening on: http://localhost:8080
Application started. Press CTRL+C to shut down.
```

Now go to browser, and navigate to http://localhost:8080, you should be able to see a page as below:

![no files screenshot](no_files.png)
![with uploaded files screenshot](with_files.png)# Install iris-contrib/middleware

```sh
$ go get -u github.com/iris-contrib/middleware/...
```# Please navigate to the [_examples/mvc/login](https://github.com/kataras/iris/tree/master/_examples/mvc/login)# Please navigate to the [_examples/mvc/overview](https://github.com/kataras/iris/tree/master/_examples/mvc/overview)# Hosts

## Listen and Serve

You can start the server(s) listening to any type of `net.Listener` or even `http.Server` instance.
The method for initialization of the server should be passed at the end, via `Run` function.

The most common method that Go developers use to serve their servers are
by passing a network address with form of "hostname:ip". With Iris
we use the `iris.Addr` which is an `iris.Runner` type

```go
// Listening on tcp with network address 0.0.0.0:8080
app.Run(iris.Addr(":8080"))
```

Sometimes you have created a standard net/http server somewhere else in your app and want to use that to serve the Iris web app

```go
// Same as before but using a custom http.Server which may being used somewhere else too
app.Run(iris.Server(&http.Server{Addr:":8080"}))
```

The most advanced usage is to create a custom or a standard `net.Listener` and pass that to `app.Run`

```go
// Using a custom net.Listener
l, err := net.Listen("tcp4", ":8080")
if err != nil {
    panic(err)
}
app.Run(iris.Listener(l))
```

A more complete example, using the unix-only socket files feature 

```go
package main

import (
    "os"
    "net"

    "github.com/kataras/iris"
)

func main() {
    app := iris.New()

    // UNIX socket
    if errOs := os.Remove(socketFile); errOs != nil && !os.IsNotExist(errOs) {
        app.Logger().Fatal(errOs)
    }

    l, err := net.Listen("unix", socketFile)

    if err != nil {
        app.Logger().Fatal(err)
    }

    if err = os.Chmod(socketFile, mode); err != nil {
        app.Logger().Fatal(err)
    }

    app.Run(iris.Listener(l))
}
```

UNIX and BSD hosts can take advantage of the reuse port feature

```go
package main

import (
    // Package tcplisten provides customizable TCP net.Listener with various
    // performance-related options:
    //
    //   - SO_REUSEPORT. This option allows linear scaling server performance
    //     on multi-CPU servers.
    //     See https://www.nginx.com/blog/socket-sharding-nginx-release-1-9-1/ for details.
    //
    //   - TCP_DEFER_ACCEPT. This option expects the server reads from the accepted
    //     connection before writing to them.
    //
    //   - TCP_FASTOPEN. See https://lwn.net/Articles/508865/ for details.
    "github.com/valyala/tcplisten"

    "github.com/kataras/iris"
)

// go get github.com/valyala/tcplisten
// go run main.go

func main() {
    app := iris.New()

    app.Get("/", func(ctx iris.Context) {
        ctx.HTML("<h1>Hello World!</h1>")
    })

    listenerCfg := tcplisten.Config{
        ReusePort:   true,
        DeferAccept: true,
        FastOpen:    true,
    }

    l, err := listenerCfg.NewListener("tcp", ":8080")
    if err != nil {
        app.Logger().Fatal(err)
    }

    app.Run(iris.Listener(l))
}
```

### HTTP/2 and Secure

If you have signed file keys you can use the `iris.TLS` to serve `https` based on those certification keys

```go
// TLS using files
app.Run(iris.TLS("127.0.0.1:443", "mycert.cert", "mykey.key"))
```

The method you should use when your app is ready for **production** is the `iris.AutoTLS` which starts a secure server with automated certifications provided by https://letsencrypt.org for **free**

```go
// Automatic TLS
app.Run(iris.AutoTLS(":443", "example.com", "admin@example.com"))
```

### Any `iris.Runner`

There may be times that you want something very special to listen on, which is not a type of `net.Listener`. You are able to do that by `iris.Raw`, but you're responsible of that method

```go
// Using any func() error,
// the responsibility of starting up a listener is up to you with this way,
// for the sake of simplicity we will use the
// ListenAndServe function of the `net/http` package.
app.Run(iris.Raw(&http.Server{Addr:":8080"}).ListenAndServe)
```

## Host configurators

All the above forms of listening are accepting a last, variadic argument of `func(*iris.Supervisor)`. This is used to add configurators for that specific host you passed via those functions.

For example let's say that we want to add a callback which is fired when
the server is shutdown

```go
app.Run(iris.Addr(":8080", func(h *iris.Supervisor) {
    h.RegisterOnShutdown(func() {
        println("server terminated")
    })
}))
```

You can even do that before `app.Run` method, but the difference is that
these host configurators will be executed to all hosts that you may use to serve your web app (via `app.NewHost` we'll see that in a minute)

```go
app := iris.New()
app.ConfigureHost(func(h *iris.Supervisor) {
    h.RegisterOnShutdown(func() {
        println("server terminated")
    })
})
app.Run(iris.Addr(":8080"))
```

Access to all hosts that serve your application can be provided by
the `Application#Hosts` field, after the `Run` method.

But the most common scenario is that you may need access to the host before the `app.Run` method,
there are two ways of gain access to the host supervisor, read below.

We have already saw how to configure all application's hosts by second argument of `app.Run` or `app.ConfigureHost`. There is one more way which suits better for simple scenarios and that is to use the `app.NewHost` to create a new host
and use one of its `Serve` or `Listen` functions
to start the application via the `iris#Raw` Runner.

Note that this way needs an extra import of the `net/http` package.

Example Code:

```go
h := app.NewHost(&http.Server{Addr:":8080"})
h.RegisterOnShutdown(func(){
    println("server terminated")
})

app.Run(iris.Raw(h.ListenAndServe))
```

## Multi hosts

You can serve your Iris web app using more than one server, the `iris.Router` is compatible with the `net/http/Handler` function therefore, as you can understand, it can be used to be adapted at any `net/http` server, however there is an easier way, by using the `app.NewHost` which is also copying all the host configurators and it closes all the hosts attached to the particular web app on `app.Shutdown`.

```go
app := iris.New()
app.Get("/", indexHandler)

// run in different goroutine in order to not block the main "goroutine".
go app.Run(iris.Addr(":8080"))
// start a second server which is listening on tcp 0.0.0.0:9090,
// without "go" keyword because we want to block at the last server-run.
app.NewHost(&http.Server{Addr:":9090"}).ListenAndServe()
```

## Shutdown (Gracefully)

Let's continue by learning how to catch CONTROL+C/COMMAND+C or unix kill command and shutdown the server gracefully.

> Gracefully Shutdown on CONTROL+C/COMMAND+C or when kill command sent is ENABLED BY-DEFAULT.

In order to manually manage what to do when app is interrupted,
we have to disable the default behavior with the option `WithoutInterruptHandler`
and register a new interrupt handler (globally, across all possible hosts).


Example code:

```go
package main

import (
    "context"
    "time"

    "github.com/kataras/iris"
)


func main() {
    app := iris.New()

    iris.RegisterOnInterrupt(func() {
        timeout := 5 * time.Second
        ctx, cancel := context.WithTimeout(context.Background(), timeout)
        defer cancel()
        // close all hosts
        app.Shutdown(ctx)
    })

    app.Get("/", func(ctx iris.Context) {
        ctx.HTML(" <h1>hi, I just exist in order to see if the server is closed</h1>")
    })

    app.Run(iris.Addr(":8080"), iris.WithoutInterruptHandler)
}
```
A silly example for this issue: https://github.com/kataras/iris/issues/688#issuecomment-318828259.
However it seems useful and therefore is being included in the examples for everyone else.# MVC

![](https://github.com/kataras/iris/raw/master/_examples/mvc/web_mvc_diagram.png)

Iris has **first-class support for the MVC pattern**, you'll not find
these stuff anywhere else in the Go world.

Iris supports Request data, Models, Persistence Data and Binding
with the fastest possible execution.

## Characteristics

All HTTP Methods are supported, for example if want to serve `GET`
then the controller should have a function named `Get()`,
you can define more than one method function to serve in the same Controller.

Serve custom controller's struct's methods as handlers with custom paths(even with regex parametermized path) 
via the `BeforeActivation` custom event callback, per-controller. Example:

```go
import (
    "github.com/kataras/iris"
    "github.com/kataras/iris/mvc"
)

func main() {
    app := iris.New()
    mvc.Configure(app.Party("/root"), myMVC)
    app.Run(iris.Addr(":8080"))
}

func myMVC(app *mvc.Application) {
    // app.Register(...)
    // app.Router.Use/UseGlobal/Done(...)
    app.Handle(new(MyController))
}

type MyController struct {}

func (m *MyController) BeforeActivation(b mvc.BeforeActivation) {
    // b.Dependencies().Add/Remove
    // b.Router().Use/UseGlobal/Done // and any standard API call you already know

    // 1-> Method
    // 2-> Path
    // 3-> The controller's function name to be parsed as handler
    // 4-> Any handlers that should run before the MyCustomHandler
    b.Handle("GET", "/something/{id:long}", "MyCustomHandler", anyMiddleware...)
}

// GET: http://localhost:8080/root
func (m *MyController) Get() string { return "Hey" }

// GET: http://localhost:8080/root/something/{id:long}
func (m *MyController) MyCustomHandler(id int64) string { return "MyCustomHandler says Hey" }
```

Persistence data inside your Controller struct (share data between requests)
by defining services to the Dependencies or have a `Singleton` controller scope.

Share the dependencies between controllers or register them on a parent MVC Application, and ability
to modify dependencies per-controller on the `BeforeActivation` optional event callback inside a Controller,
i.e `func(c *MyController) BeforeActivation(b mvc.BeforeActivation) { b.Dependencies().Add/Remove(...) }`.

Access to the `Context` as a controller's field(no manual binding is neede) i.e `Ctx iris.Context` or via a method's input argument, i.e `func(ctx iris.Context, otherArguments...)`.

Models inside your Controller struct (set-ed at the Method function and rendered by the View).
You can return models from a controller's method or set a field in the request lifecycle
and return that field to another method, in the same request lifecycle.

Flow as you used to, mvc application has its own `Router` which is a type of `iris/router.Party`, the standard iris api.
`Controllers` can be registered to any `Party`, including Subdomains, the Party's begin and done handlers work as expected.

Optional `BeginRequest(ctx)` function to perform any initialization before the method execution,
useful to call middlewares or when many methods use the same collection of data.

Optional `EndRequest(ctx)` function to perform any finalization after any method executed.

Inheritance, recursively, see for example our `mvc.SessionController`, it has the `Session *sessions.Session` and `Manager *sessions.Sessions` as embedded fields
which are filled by its `BeginRequest`, [here](https://github.com/kataras/iris/blob/master/mvc/session_controller.go).
This is just an example, you could use the `sessions.Session` as a dependency to the MVC Application, i.e
`mvcApp.Register(sessions.New(sessions.Config{Cookie: "iris_session_id"}).Start)`.

Access to the dynamic path parameters via the controller's methods' input arguments, no binding is needed.
When you use the Iris' default syntax to parse handlers from a controller, you need to suffix the methods
with the `By` word, uppercase is a new sub path. Example:

If `mvc.New(app.Party("/user")).Handle(new(user.Controller))`

- `func(*Controller) Get()` - `GET:/user`.
- `func(*Controller) Post()` - `POST:/user`.
- `func(*Controller) GetLogin()` - `GET:/user/login`
- `func(*Controller) PostLogin()` - `POST:/user/login`
- `func(*Controller) GetProfileFollowers()` - `GET:/user/profile/followers`
- `func(*Controller) PostProfileFollowers()` - `POST:/user/profile/followers`
- `func(*Controller) GetBy(id int64)` - `GET:/user/{param:long}`
- `func(*Controller) PostBy(id int64)` - `POST:/user/{param:long}`

If `mvc.New(app.Party("/profile")).Handle(new(profile.Controller))`

- `func(*Controller) GetBy(username string)` - `GET:/profile/{param:string}`

If `mvc.New(app.Party("/assets")).Handle(new(file.Controller))`

- `func(*Controller) GetByWildard(path string)` - `GET:/assets/{param:path}`

    Supported types for method functions receivers: int, int64, bool and string.

Response via output arguments, optionally, i.e

```go
func(c *ExampleController) Get() string |
                                (string, string) |
                                (string, int) |
                                int |
                                (int, string) |
                                (string, error) |
                                error |
                                (int, error) |
                                (any, bool) |
                                (customStruct, error) |
                                customStruct |
                                (customStruct, int) |
                                (customStruct, string) |
                                mvc.Result or (mvc.Result, error)
```

where [mvc.Result](https://github.com/kataras/iris/blob/master/mvc/func_result.go) is an interface which contains only that function: `Dispatch(ctx iris.Context)`.

## Using Iris MVC for code reuse

By creating components that are independent of one another, developers are able to reuse components quickly and easily in other applications. The same (or similar) view for one application can be refactored for another application with different data because the view is simply handling how the data is being displayed to the user.

If you're new to back-end web development read about the MVC architectural pattern first, a good start is that [wikipedia article](https://en.wikipedia.org/wiki/Model%E2%80%93view%E2%80%93controller).

## Examples

- [Hello world](hello-world/main.go) **UPDATED**
- [Session Controller](session-controller/main.go) **UPDATED**
- [Overview - Plus Repository and Service layers](overview) **UPDATED**
- [Login showcase - Plus Repository and Service layers](login) **UPDATED**
- [Singleton](singleton) **NEW**
- [Websocket Controller](websocket) **NEW**
- [Register Middleware](middleware) **NEW**

Folder structure guidelines can be found at the [_examples/#structuring](https://github.com/kataras/iris/tree/master/_examples/#structuring) section.# View Models

There should be the view models, the structure that the client will be able to see.

Example:

```go
import (
    "github.com/kataras/iris/_examples/mvc/login/datamodels"

    "github.com/kataras/iris/context"
)

type User struct {
    datamodels.User
}

func (m User) IsValid() bool {
    /* do some checks and return true if it's valid... */
    return m.ID > 0
}
```

Iris is able to convert any custom data Structure into an HTTP Response Dispatcher,
so theoretically, something like the following is permitted if it's really necessary;

```go
// Dispatch completes the `kataras/iris/mvc#Result` interface.
// Sends a `User` as a controlled http response.
// If its ID is zero or less then it returns a 404 not found error
// else it returns its json representation,
// (just like the controller's functions do for custom types by default).
//
// Don't overdo it, the application's logic should not be here.
// It's just one more step of validation before the response,
// simple checks can be added here.
//
// It's just a showcase,
// imagine the potentials this feature gives when designing a bigger application.
//
// This is called where the return value from a controller's method functions
// is type of `User`.
// For example the `controllers/user_controller.go#GetBy`.
func (m User) Dispatch(ctx context.Context) {
    if !m.IsValid() {
        ctx.NotFound()
        return
    }
    ctx.JSON(m, context.JSON{Indent: " "})
}
```

However, we will use the "datamodels" as the only one models package because
User structure doesn't contain any sensitive data, clients are able to see all of its fields
and we don't need any extra functionality or validation inside it.# Data Source / Data Store Layer# View Models

There should be the view models, the structure that the client will be able to see.

Example:

```go
import (
    "github.com/kataras/iris/_examples/mvc/overview/datamodels"

    "github.com/kataras/iris/context"
)

type Movie struct {
    datamodels.Movie
}

func (m Movie) IsValid() bool {
    /* do some checks and return true if it's valid... */
    return m.ID > 0
}
```

Iris is able to convert any custom data Structure into an HTTP Response Dispatcher,
so theoretically, something like the following is permitted if it's really necessary;

```go
// Dispatch completes the `kataras/iris/mvc#Result` interface.
// Sends a `Movie` as a controlled http response.
// If its ID is zero or less then it returns a 404 not found error
// else it returns its json representation,
// (just like the controller's functions do for custom types by default).
//
// Don't overdo it, the application's logic should not be here.
// It's just one more step of validation before the response,
// simple checks can be added here.
//
// It's just a showcase,
// imagine the potentials this feature gives when designing a bigger application.
//
// This is called where the return value from a controller's method functions
// is type of `Movie`.
// For example the `controllers/movie_controller.go#GetBy`.
func (m Movie) Dispatch(ctx context.Context) {
    if !m.IsValid() {
        ctx.NotFound()
        return
    }
    ctx.JSON(m, context.JSON{Indent: " "})
}
```

However, we will use the "datamodels" as the only one models package because
Movie structure doesn't contain any sensitive data, clients are able to see all of its fields
and we don't need any extra functionality or validation inside it.# Domain Models

There should be the domain/business-level models.

Example:

```go
import "github.com/kataras/iris/_examples/mvc/overview/datamodels"

type Movie struct {
    datamodels.Movie
}

func (m Movie) Validate() (Movie, error) {
    /* do some checks and return an error if that Movie is not valid */
}
```

However, we will use the "datamodels" as the only one models package because
Movie structure we don't need any extra functionality or validation inside it.# Service Layer

The package which has access to call functions from the "repositories" and "models" ("datamodels" only in that simple example). It should contain the domain logic.# Repositories

The package which has direct access to the "datasource" and can manipulate data directly.# Data Model LayerThe `context.ResponseWriter()` returns an enchament version of a http.ResponseWriter, the examples show some places where the Context uses this object. Besides that you can use it as you did before iris.# Hero Template Example

This folder contains the iris version of the original hero's example: https://github.com/shiyanhui/hero/tree/master/examples/app.

Iris is 100% compatible with `net/http` so you don't have to change anything else
except the handler input from the original example.

The only inline handler's changes were:

From:

```go
if _, err := w.Write(buffer.Bytes()); err != nil {
// and
template.UserListToWriter(userList, w)
```
To: 
```go
if _, err := ctx.Write(buffer.Bytes()); err != nil {
// and
template.UserListToWriter(userList, ctx)
```

So easy.

Read more at: https://github.com/shiyanhui/heroFirst of all, install [quicktemplate](https://github.com/valyala/quicktemplate) package and [quicktemplate compiler](https://github.com/valyala/quicktemplate/tree/master/qtc)

```sh
go get -u github.com/valyala/quicktemplate
go get -u github.com/valyala/quicktemplate/qtc
```

The example has the Go code compiled already for you, therefore:
```sh
go run main.go # http://localhost:8080
```

However there is an instruction below, full documentation can be found at https://github.com/valyala/quicktemplate.

Save your template files into `templates` folder under the extension *.qtpl, open your terminal and run `qtc` inside this folder.

If all went ok, `*.qtpl.go` files must appear in the `templates` folder. These files contain the Go code for  all `*.qtpl` files.

> Remember, each time you change a  a `/templates/*.qtpl` file you have to run the `qtc` command and re-build your application.The `context.Request()` returns the same *http.Request you already know, the examples show some places where the  Context uses this object. Besides that you can use it as you did before iris.# Configuration

All configuration's values have default values, things will work as you expected with `iris.New()`.

Configuration is useless before listen functions, so it should be passed on `Application#Run/2` (second argument(s)).

Iris has a type named `Configurator` which is a `func(*iris.Application)`, any function
which completes this can be passed at `Application#Configure` and/or `Application#Run/2`.

`Application#ConfigurationReadOnly()` returns the configuration values.

`.Run` **by `Configuration` struct**

```go
package main

import (
    "github.com/kataras/iris"
)

func main() {
    app := iris.New()
    app.Get("/", func(ctx iris.Context) {
        ctx.HTML("<b>Hello!</b>")
    })
    // [...]

    // Good when you want to modify the whole configuration.
    app.Run(iris.Addr(":8080"), iris.WithConfiguration(iris.Configuration{
        DisableStartupLog:                 false,
        DisableInterruptHandler:           false,
        DisablePathCorrection:             false,
        EnablePathEscape:                  false,
        FireMethodNotAllowed:              false,
        DisableBodyConsumptionOnUnmarshal: false,
        DisableAutoFireStatusCode:         false,
        TimeFormat:                        "Mon, 02 Jan 2006 15:04:05 GMT",
        Charset:                           "UTF-8",
    }))
}
```

`.Run` **by options**

```go
package main

import (
    "github.com/kataras/iris"
)

func main() {
    app := iris.New()
    app.Get("/", func(ctx iris.Context) {
        ctx.HTML("<b>Hello!</b>")
    })
    // [...]

    // Good when you want to change some of the configuration's field.
    // Prefix: "With", code editors will help you navigate through all
    // configuration options without even a glitch to the documentation.

    app.Run(iris.Addr(":8080"), iris.WithoutStartupLog, iris.WithCharset("UTF-8"))

    // or before run:
    // app.Configure(iris.WithoutStartupLog, iris.WithCharset("UTF-8"))
    // app.Run(iris.Addr(":8080"))
}
```

`.Run` **by TOML config file**

```tml
DisablePathCorrection = false
EnablePathEscape = false
FireMethodNotAllowed = true
DisableBodyConsumptionOnUnmarshal = false
TimeFormat = "Mon, 01 Jan 2006 15:04:05 GMT"
Charset = "UTF-8"

[Other]
	MyServerName = "iris"

```

```go
package main

import (
    "github.com/kataras/iris"
)

func main() {
    app := iris.New()

    app.Get("/", func(ctx iris.Context) {
        ctx.HTML("<b>Hello!</b>")
    })
    // [...]

    // Good when you have two configurations, one for development and a different one for production use.
    app.Run(iris.Addr(":8080"), iris.WithConfiguration(iris.TOML("./configs/iris.tml")))
}
```


`.Run` **by YAML config file**

```yml
DisablePathCorrection: false
EnablePathEscape: false
FireMethodNotAllowed: true
DisableBodyConsumptionOnUnmarshal: true
TimeFormat: Mon, 01 Jan 2006 15:04:05 GMT
Charset: UTF-8
```

```go
package main

import (
    "github.com/kataras/iris"
)

func main() {
    app := iris.New()
    app.Get("/", func(ctx iris.Context) {
        ctx.HTML("<b>Hello!</b>")
    })
    // [...]

    app.Run(iris.Addr(":8080"), iris.WithConfiguration(iris.YAML("./configs/iris.yml")))
}

```

## Built'n Configurators

```go
// WithoutServerError will cause to ignore the matched "errors"
// from the main application's `Run` function.
//
// Usage:
// err := app.Run(iris.Addr(":8080"), iris.WithoutServerError(iris.ErrServerClosed))
// will return `nil` if the server's error was `http/iris#ErrServerClosed`.
//
// See `Configuration#IgnoreServerErrors []string` too.
//
// Example: https://github.com/kataras/iris/tree/master/_examples/http-listening/listen-addr/omit-server-errors
func WithoutServerError(errors ...error) Configurator

// WithoutStartupLog turns off the information send, once, to the terminal when the main server is open.
var WithoutStartupLog

// WithoutInterruptHandler disables the automatic graceful server shutdown
// when control/cmd+C pressed.
var WithoutInterruptHandler

// WithoutPathCorrection disables the PathCorrection setting.
//
// See `Configuration`.
var WithoutPathCorrection

// WithoutBodyConsumptionOnUnmarshal disables BodyConsumptionOnUnmarshal setting.
//
// See `Configuration`.
var WithoutBodyConsumptionOnUnmarshal

// WithoutAutoFireStatusCode disables the AutoFireStatusCode setting.
//
// See `Configuration`.
var WithoutAutoFireStatusCode

// WithPathEscape enanbles the PathEscape setting.
//
// See `Configuration`.
var WithPathEscape

// WithOptimizations can force the application to optimize for the best performance where is possible.
//
// See `Configuration`.
var WithOptimizations

// WithFireMethodNotAllowed enanbles the FireMethodNotAllowed setting.
//
// See `Configuration`.
var WithFireMethodNotAllowed

// WithTimeFormat sets the TimeFormat setting.
//
// See `Configuration`.
func WithTimeFormat(timeformat string) Configurator

// WithCharset sets the Charset setting.
//
// See `Configuration`.
func WithCharset(charset string) Configurator

// WithRemoteAddrHeader enables or adds a new or existing request header name
// that can be used to validate the client's real IP.
//
// Existing values are:
// "X-Real-Ip":             false,
// "X-Forwarded-For":       false,
// "CF-Connecting-IP": false
//
// Look `context.RemoteAddr()` for more.
func WithRemoteAddrHeader(headerName string) Configurator

// WithoutRemoteAddrHeader disables an existing request header name
// that can be used to validate the client's real IP.
//
// Existing values are:
// "X-Real-Ip":             false,
// "X-Forwarded-For":       false,
// "CF-Connecting-IP": false
//
// Look `context.RemoteAddr()` for more.
func WithoutRemoteAddrHeader(headerName string) Configurator

// WithOtherValue adds a value based on a key to the Other setting.
//
// See `Configuration`.
func WithOtherValue(key string, val interface{}) Configurator
```

## Custom Configurator

With the `Configurator` developers can modularize their applications with ease.

Example Code:

```go
// file counter/counter.go
package counter

import (
    "time"

    "github.com/kataras/iris"
    "github.com/kataras/iris/core/host"
)

func Configurator(app *iris.Application) {
    counterValue := 0

    go func() {
        ticker := time.NewTicker(time.Second)

        for range ticker.C {
            counterValue++
        }

        app.ConfigureHost(func(h *host.Supervisor) { // <- HERE: IMPORTANT
            h.RegisterOnShutdown(func() {
                ticker.Stop()
            })
        })
    }()

    app.Get("/counter", func(ctx iris.Context) {
        ctx.Writef("Counter value = %d", counterValue)
    })
}
```

```go
// file: main.go
package main

import (
    "counter"

    "github.com/kataras/iris"
)

func main() {
    app := iris.New()
    app.Configure(counter.Configurator)

    app.Run(iris.Addr(":8080"))
}
```# Sessions

Iris provides a fast, fully featured and easy to use sessions manager.

Iris sessions manager lives on its own [kataras/iris/sessions](https://github.com/kataras/iris/tree/master/sessions) package.

Some trivial examples,

- [Overview](https://github.com/kataras/iris/blob/master/_examples/sessions/overview/main.go)
- [Standalone](https://github.com/kataras/iris/blob/master/_examples/sessions/standalone/main.go)
- [Secure Cookie](https://github.com/kataras/iris/blob/master/_examples/sessions/securecookie/main.go)
- [Flash Messages](https://github.com/kataras/iris/blob/master/_examples/sessions/flash-messages/main.go)
- [Databases](https://github.com/kataras/iris/tree/master/_examples/sessions/database)
    * [Badger](https://github.com/kataras/iris/blob/master/_examples/sessions/database/badger/main.go) **fastest**
    * [BoltDB](https://github.com/kataras/iris/blob/master/_examples/sessions/database/boltdb/main.go)
    * [Redis](https://github.com/kataras/iris/blob/master/_examples/sessions/database/redis/main.go)

## Overview

```go
import "github.com/kataras/iris/sessions"

manager := sessions.Start(iris.Context)
manager.
  ID() string
  Get(string) interface{}
  HasFlash() bool
  GetFlash(string) interface{}
  GetFlashString(string) string
  GetString(key string) string
  GetInt(key string) (int, error)
  GetInt64(key string) (int64, error)
  GetFloat32(key string) (float32, error)
  GetFloat64(key string) (float64, error)
  GetBoolean(key string) (bool, error)
  GetAll() map[string]interface{}
  GetFlashes() map[string]interface{}
  VisitAll(cb func(k string, v interface{}))
  Set(string, interface{})
  SetImmutable(key string, value interface{})
  SetFlash(string, interface{})
  Delete(string)
  Clear()
  ClearFlashes()
```

This example will show how to store data from a session.

You don't need any third-party library except Iris, but if you want you can use anything, remember Iris is fully compatible with the standard library. You can find a more detailed examples by pressing [here](https://github.com/kataras/iris/tree/master/_examples/sessions).

In this example we will only allow authenticated users to view our secret message on the `/secret` age. To get access to it, the will first have to visit `/login` to get a valid session cookie, hich logs him in. Additionally he can visit `/logout` to revoke his access to our secret message.

```go
// sessions.go
package main

import (
    "github.com/kataras/iris"

    "github.com/kataras/iris/sessions"
)

var (
    cookieNameForSessionID = "mycookiesessionnameid"
    sess                   = sessions.New(sessions.Config{Cookie: cookieNameForSessionID, AllowReclaim: true})
)

func secret(ctx iris.Context) {
    // Check if user is authenticated
    if auth, _ := sess.Start(ctx).GetBoolean("authenticated"); !auth {
        ctx.StatusCode(iris.StatusForbidden)
        return
    }

    // Print secret message
    ctx.WriteString("The cake is a lie!")
}

func login(ctx iris.Context) {
    session := sess.Start(ctx)

    // Authentication goes here
    // ...

    // Set user as authenticated
    session.Set("authenticated", true)
}

func logout(ctx iris.Context) {
    session := sess.Start(ctx)

    // Revoke users authentication
    session.Set("authenticated", false)
}

func main() {
    app := iris.New()

    app.Get("/secret", secret)
    app.Get("/login", login)
    app.Get("/logout", logout)

    app.Run(iris.Addr(":8080"))
}

```

```bash
$ go run sessions.go

$ curl -s http://localhost:8080/secret
Forbidden

$ curl -s -I http://localhost:8080/login
Set-Cookie: mysessionid=MTQ4NzE5Mz...

$ curl -s --cookie "mysessionid=MTQ4NzE5Mz..." http://localhost:8080/secret
The cake is a lie!
```# Authentication

- [Basic Authentication](basicauth/main.go)
- [OAUth2](oauth2/main.go)
- [JWT](https://github.com/kataras/iris/blob/master/_examples/experimental-handlers/jwt/main.go)
- [Sessions](https://github.com/kataras/iris/tree/master/_examples/#sessions)# hero: basic

## 1. Path Parameters - Built'n Dependencies

![](https://github.com/kataras/explore/raw/master/iris/hero/hero-1-monokai.png)

## 2. Services - Static Dependencies

![](https://github.com/kataras/explore/raw/master/iris/hero/hero-2-monokai.png)

## 3. Per-Request - Dynamic Dependencies

![](https://github.com/kataras/explore/raw/master/iris/hero/hero-3-monokai.png)## Info

This folder examines the {{render "dir/templatefilename"}} functionality to manually render any template inside any template
# Routing

## Handlers

A Handler, as the name implies, handle requests.

```go
// A Handler responds to an HTTP request.
// It writes reply headers and data to the
// Context.ResponseWriter() and then return.
// Returning signals that the request is finished;
// it is not valid to use the Context after or
// concurrently with the completion of the Handler call.
//
// Depending on the HTTP client software, HTTP protocol version,
// and any intermediaries between the client and the iris server,
// it may not be possible to read from the
// Context.Request().Body after writing to the context.ResponseWriter().
// Cautious handlers should read the Context.Request().Body first, and then reply.
//
// Except for reading the body, handlers should not modify the provided Context.
//
// If Handler panics, the server (the caller of Handler) assumes that
// the effect of the panic was isolated to the active request.
// It recovers the panic, logs a stack trace to the server error log
// and hangs up the connection.
type Handler func(Context)
```

Once the handler is registered, we can use the returned [`Route`](https://godoc.org/github.com/kataras/iris/core/router#Route) instance to give a name to the handler registration for easier lookup in code or in templates.

For more information, checkout the [Routing and reverse lookups](routing_reverse.md) section.

## API

All HTTP methods are supported, developers can also register handlers for same paths for different methods.

The first parameter is the HTTP Method,
second parameter is the request path of the route,
third variadic parameter should contains one or more iris.Handler executed
by the registered order when a user requests for that specific resouce path from the server.

Example code:

```go
app := iris.New()

app.Handle("GET", "/contact", func(ctx iris.Context) {
    ctx.HTML("<h1> Hello from /contact </h1>")
})
```

In order to make things easier for the end-developer, iris provides functions for all HTTP Methods.
The first parameter is the request path of the route,
second variadic parameter should contains one or more iris.Handler executed
by the registered order when a user requests for that specific resouce path from the server.

Example code:

```go
app := iris.New()

// Method: "GET"
app.Get("/", handler)

// Method: "POST"
app.Post("/", handler)

// Method: "PUT"
app.Put("/", handler)

// Method: "DELETE"
app.Delete("/", handler)

// Method: "OPTIONS"
app.Options("/", handler)

// Method: "TRACE"
app.Trace("/", handler)

// Method: "CONNECT"
app.Connect("/", handler)

// Method: "HEAD"
app.Head("/", handler)

// Method: "PATCH"
app.Patch("/", handler)

// register the route for all HTTP Methods
app.Any("/", handler)

func handler(ctx iris.Context){
    ctx.Writef("Hello from method: %s and path: %s", ctx.Method(), ctx.Path())
}
```

## Grouping Routes

A set of routes that are being groupped by path prefix can (optionally) share the same middleware handlers and template layout.
A group can have a nested group too.

`.Party` is being used to group routes, developers can declare an unlimited number of (nested) groups.

Example code:

```go
app := iris.New()

users := app.Party("/users", myAuthMiddlewareHandler)

// http://localhost:8080/users/42/profile
users.Get("/{id:int}/profile", userProfileHandler)
// http://localhost:8080/users/messages/1
users.Get("/inbox/{id:int}", userMessageHandler)
```

The same could be also written using a function which accepts the child router(the Party).

```go
app := iris.New()

app.PartyFunc("/users", func(users iris.Party) {
    users.Use(myAuthMiddlewareHandler)

    // http://localhost:8080/users/42/profile
    users.Get("/{id:int}/profile", userProfileHandler)
    // http://localhost:8080/users/messages/1
    users.Get("/inbox/{id:int}", userMessageHandler)
})
```

> `id:int` is a (typed) dynamic path parameter, learn more by scrolling down.

# Dynamic Path Parameters

Iris has the easiest and the most powerful routing process you have ever meet.

At the same time,
Iris has its own interpeter(yes like a programming language)
for route's path syntax and their dynamic path parameters parsing and evaluation.
We call them "macros" for shortcut.

How? It calculates its needs and if not any special regexp needed then it just
registers the route with the low-level path syntax,
otherwise it pre-compiles the regexp and adds the necessary middleware(s). That means that you have zero performance cost compared to other routers or web frameworks.

Standard macro types for route path parameters

```sh
+------------------------+
| {param:string}         |
+------------------------+
string type
anything

+------------------------+
| {param:int}            |
+------------------------+
int type
only numbers (0-9)

+------------------------+
| {param:long}           |
+------------------------+
int64 type
only numbers (0-9)

+------------------------+
| {param:boolean}        |
+------------------------+
bool type
only "1" or "t" or "T" or "TRUE" or "true" or "True"
or "0" or "f" or "F" or "FALSE" or "false" or "False"

+------------------------+
| {param:alphabetical}   |
+------------------------+
alphabetical/letter type
letters only (upper or lowercase)

+------------------------+
| {param:file}           |
+------------------------+
file type
letters (upper or lowercase)
numbers (0-9)
underscore (_)
dash (-)
point (.)
no spaces ! or other character

+------------------------+
| {param:path}           |
+------------------------+
path type
anything, should be the last part, more than one path segment,
i.e: /path1/path2/path3 , ctx.Params().Get("param") == "/path1/path2/path3"
```

If type is missing then parameter's type is defaulted to string, so
`{param} == {param:string}`.

If a function not found on that type then the `string` macro type's functions are being used.

Besides the fact that iris provides the basic types and some default "macro funcs"
you are able to register your own too!.

Register a named path parameter function

```go
app.Macros().Int.RegisterFunc("min", func(argument int) func(paramValue string) bool {
    // [...]
    return true 
    // -> true means valid, false means invalid fire 404 or if "else 500" is appended to the macro syntax then internal server error.
})
```

At the `func(argument ...)` you can have any standard type, it will be validated before the server starts so don't care about any performance cost there, the only thing it runs at serve time is the returning `func(paramValue string) bool`.

```go
{param:string equal(iris)} , "iris" will be the argument here:
app.Macros().String.RegisterFunc("equal", func(argument string) func(paramValue string) bool {
    return func(paramValue string){ return argument == paramValue }
})
```

Example Code:

```go
app := iris.New()
// you can use the "string" type which is valid for a single path parameter that can be anything.
app.Get("/username/{name}", func(ctx iris.Context) {
    ctx.Writef("Hello %s", ctx.Params().Get("name"))
}) // type is missing = {name:string}

// Let's register our first macro attached to int macro type.
// "min" = the function
// "minValue" = the argument of the function
// func(string) bool = the macro's path parameter evaluator, this executes in serve time when
// a user requests a path which contains the :int macro type with the min(...) macro parameter function.
app.Macros().Int.RegisterFunc("min", func(minValue int) func(string) bool {
    // do anything before serve here [...]
    // at this case we don't need to do anything
    return func(paramValue string) bool {
        n, err := strconv.Atoi(paramValue)
        if err != nil {
            return false
        }
        return n >= minValue
    }
})

// http://localhost:8080/profile/id>=1
// this will throw 404 even if it's found as route on : /profile/0, /profile/blabla, /profile/-1
// macro parameter functions are optional of course.
app.Get("/profile/{id:int min(1)}", func(ctx iris.Context) {
    // second parameter is the error but it will always nil because we use macros,
    // the validaton already happened.
    id, _ := ctx.Params().GetInt("id")
    ctx.Writef("Hello id: %d", id)
})

// to change the error code per route's macro evaluator:
app.Get("/profile/{id:int min(1)}/friends/{friendid:int min(1) else 504}", func(ctx iris.Context) {
    id, _ := ctx.Params().GetInt("id")
    friendid, _ := ctx.Params().GetInt("friendid")
    ctx.Writef("Hello id: %d looking for friend id: ", id, friendid)
}) // this will throw e 504 error code instead of 404 if all route's macros not passed.

// http://localhost:8080/game/a-zA-Z/level/0-9
// remember, alphabetical is lowercase or uppercase letters only.
app.Get("/game/{name:alphabetical}/level/{level:int}", func(ctx iris.Context) {
    ctx.Writef("name: %s | level: %s", ctx.Params().Get("name"), ctx.Params().Get("level"))
})

// let's use a trivial custom regexp that validates a single path parameter
// which its value is only lowercase letters.

// http://localhost:8080/lowercase/anylowercase
app.Get("/lowercase/{name:string regexp(^[a-z]+)}", func(ctx iris.Context) {
    ctx.Writef("name should be only lowercase, otherwise this handler will never executed: %s", ctx.Params().Get("name"))
})

// http://localhost:8080/single_file/app.js
app.Get("/single_file/{myfile:file}", func(ctx iris.Context) {
    ctx.Writef("file type validates if the parameter value has a form of a file name, got: %s", ctx.Params().Get("myfile"))
})

// http://localhost:8080/myfiles/any/directory/here/
// this is the only macro type that accepts any number of path segments.
app.Get("/myfiles/{directory:path}", func(ctx iris.Context) {
    ctx.Writef("path type accepts any number of path segments, path after /myfiles/ is: %s", ctx.Params().Get("directory"))
})

app.Run(iris.Addr(":8080"))
}
```

A **path parameter name should contain only alphabetical letters. Symbols like  '_' and numbers are NOT allowed**.

Last, do not confuse `ctx.Params()` with `ctx.Values()`.
Path parameter's values goes to `ctx.Params()` and context's local storage
that can be used to communicate between handlers and middleware(s) goes to
`ctx.Values()`.

# Routing and reverse lookups

As mentioned in the [Handlers](handlers.md) chapter, Iris provides several handler registration methods, each of which returns a [`Route`](https://godoc.org/github.com/kataras/iris/core/router#Route) instance.

## Route naming

Route naming is easy, since we just call the returned `*Route` with a `Name` field to define a name:

```go
package main

import (
    "github.com/kataras/iris"
)

func main() {
    app := iris.New()
    // define a function
    h := func(ctx iris.Context) {
        ctx.HTML("<b>Hi</b1>")
    }

    // handler registration and naming
    home := app.Get("/", h)
    home.Name = "home"
    // or
    app.Get("/about", h).Name = "about"
    app.Get("/page/{id}", h).Name = "page"

    app.Run(iris.Addr(":8080"))
}
```

## Route reversing AKA generating URLs from the route name

When we register the handlers for a specific path, we get the ability to create URLs based on the structured data we pass to Iris. In the example above, we've named three routers, one of which even takes parameters. If we're using the default `html/template` view engine, we can use a simple action to reverse the routes (and generae actual URLs):

```sh
Home: {{ urlpath "home" }}
About: {{ urlpath "about" }}
Page 17: {{ urlpath "page" "17" }}
```

Above code would generate the following output:

```sh
Home: http://localhost:8080/ 
About: http://localhost:8080/about
Page 17: http://localhost:8080/page/17
```

## Using route names in code

We can use the following methods/functions to work with named routes (and their parameters):

* [`GetRoutes`](https://godoc.org/github.com/kataras/iris/core/router#APIBuilder.GetRoutes) function to get all registered routes
* [`GetRoute(routeName string)`](https://godoc.org/github.com/kataras/iris/core/router#APIBuilder.GetRoute) method to retrieve a route by name
* [`URL(routeName string, paramValues ...interface{})`](https://godoc.org/github.com/kataras/iris/core/router#RoutePathReverser.URL) method to generate url string based on supplied parameters
* [`Path(routeName string, paramValues ...interface{}`](https://godoc.org/github.com/kataras/iris/core/router#RoutePathReverser.Path) method to generate just the path (without host and protocol) portion of the URL based on provided values

## Examples

Check out the [https://github.com/kataras/iris/tree/master/_examples/view/template_html_4](https://github.com/kataras/iris/tree/master/_examples/view/template_html_4) example for more details.

# Middleware

When we talk about Middleware in Iris we're talking about running code before and/or after our main handler code in a HTTP request lifecycle. For example, logging middleware might write the incoming request details to a log, then call the handler code, before writing details about the response to the log. One of the cool things about middleware is that these units are extremely flexible and reusable.

A middleware is just a **Handler** form of `func(ctx iris.Context)`, the middleware is being executed when the previous middleware calls the `ctx.Next()`, this can be used for authentication, i.e: if logged in then `ctx.Next()` otherwise fire an error response. 

## Writing a middleware

```go
package main

import "github.com/kataras/iris"

func main() {
    app := iris.New()
    // or app.Use(before) and app.Done(after).
    app.Get("/", before, mainHandler, after)
    app.Run(iris.Addr(":8080"))
}

func before(ctx iris.Context) {
    shareInformation := "this is a sharable information between handlers"

    requestPath := ctx.Path()
    println("Before the mainHandler: " + requestPath)

    ctx.Values().Set("info", shareInformation)
    ctx.Next() // execute the next handler, in this case the main one.
}

func after(ctx iris.Context) {
    println("After the mainHandler")
}

func mainHandler(ctx iris.Context) {
    println("Inside mainHandler")

    // take the info from the "before" handler.
    info := ctx.Values().GetString("info")

    // write something to the client as a response.
    ctx.HTML("<h1>Response</h1>")
    ctx.HTML("<br/> Info: " + info)

    ctx.Next() // execute the "after".
}
```

```bash
$ go run main.go # and navigate to the http://localhost:8080
Now listening on: http://localhost:8080
Application started. Press CTRL+C to shut down.
Before the mainHandler: /
Inside mainHandler
After the mainHandler
```

### Globally

```go
package main

import "github.com/kataras/iris"

func main() {
    app := iris.New()

    // register our routes.
    app.Get("/", indexHandler)
    app.Get("/contact", contactHandler)

    // Order of those calls doesn't matter, `UseGlobal` and `DoneGlobal`
    // are applied to existing routes and future routes.
    //
    // Remember: the `Use` and `Done` are applied to the current party's and its children,
    // so if we used the `app.Use/Don`e before the routes registration
    // it would work like UseGlobal/DoneGlobal in this case, because the `app` is the root party.
    //
    // See `app.Party/PartyFunc` for more.
    app.UseGlobal(before)
    app.DoneGlobal(after)

    app.Run(iris.Addr(":8080"))
}

func before(ctx iris.Context) {
     // [...]
}

func after(ctx iris.Context) {
    // [...]
}

func indexHandler(ctx iris.Context) {
    // write something to the client as a response.
    ctx.HTML("<h1>Index</h1>")

    ctx.Next() // execute the "after" handler registered via `Done`.
}

func contactHandler(ctx iris.Context) {
    // write something to the client as a response.
    ctx.HTML("<h1>Contact</h1>")

    ctx.Next() // execute the "after" handler registered via `Done`.
}
```

## [Explore](https://github.com/kataras/iris/tree/master/middleware)

# Wrapping the Router

**Very rare**, you may never need that but it's here in any case you need it.

There are times you need to override or decide whether the Router will be executed on an incoming request. If you've any previous experience with the `net/http` and other web frameworks this function will be familiar with you (it has the form of a net/http middleware, but instead of accepting the next handler it accepts the Router as a function to be executed or not).

```go
// WrapperFunc is used as an expected input parameter signature
// for the WrapRouter. It's a "low-level" signature which is compatible
// with the net/http.
// It's being used to run or no run the router based on a custom logic.
type WrapperFunc func(w http.ResponseWriter, r *http.Request, firstNextIsTheRouter http.HandlerFunc)

// WrapRouter adds a wrapper on the top of the main router.
// Usually it's useful for third-party middleware
// when need to wrap the entire application with a middleware like CORS.
//
// Developers can add more than one wrappers,
// those wrappers' execution comes from last to first.
// That means that the second wrapper will wrap the first, and so on.
//
// Before build.
func WrapRouter(wrapperFunc WrapperFunc)
```

Iris' router searches for its routes based on the `HTTP Method` a Router Wrapper can override that behavior and execute custom code.

Example Code:

```go
package main

import (
    "net/http"
    "strings"

    "github.com/kataras/iris"
)

// In this example you'll just see one use case of .WrapRouter.
// You can use the .WrapRouter to add custom logic when or when not the router should
// be executed in order to execute the registered routes' handlers.
//
// To see how you can serve files on root "/" without a custom wrapper
// just navigate to the "file-server/single-page-application" example.
//
// This is just for the proof of concept, you can skip this tutorial if it's too much for you.


func main() {
    app := iris.New()

    app.OnErrorCode(iris.StatusNotFound, func(ctx iris.Context) {
        ctx.HTML("<b>Resource Not found</b>")
    })

    app.Get("/", func(ctx iris.Context) {
        ctx.ServeFile("./public/index.html", false)
    })

    app.Get("/profile/{username}", func(ctx iris.Context) {
        ctx.Writef("Hello %s", ctx.Params().Get("username"))
    })

    // serve files from the root "/", if we used .StaticWeb it could override
    // all the routes because of the underline need of wildcard.
    // Here we will see how you can by-pass this behavior
    // by creating a new file server handler and
    // setting up a wrapper for the router(like a "low-level" middleware)
    // in order to manually check if we want to process with the router as normally
    // or execute the file server handler instead.

    // use of the .StaticHandler
    // which is the same as StaticWeb but it doesn't
    // registers the route, it just returns the handler.
    fileServer := app.StaticHandler("./public", false, false)

    // wrap the router with a native net/http handler.
    // if url does not contain any "." (i.e: .css, .js...)
    // (depends on the app , you may need to add more file-server exceptions),
    // then the handler will execute the router that is responsible for the
    // registered routes (look "/" and "/profile/{username}")
    // if not then it will serve the files based on the root "/" path.
    app.WrapRouter(func(w http.ResponseWriter, r *http.Request, router http.HandlerFunc) {
        path := r.URL.Path
        // Note that if path has suffix of "index.html" it will auto-permant redirect to the "/",
        // so our first handler will be executed instead.

        if !strings.Contains(path, ".") { 
            // if it's not a resource then continue to the router as normally. <-- IMPORTANT
            router(w, r)
            return
        }
        // acquire and release a context in order to use it to execute
        // our file server
        // remember: we use net/http.Handler because here we are in the "low-level", before the router itself.
        ctx := app.ContextPool.Acquire(w, r)
        fileServer(ctx)
        app.ContextPool.Release(ctx)
    })

    // http://localhost:8080
    // http://localhost:8080/index.html
    // http://localhost:8080/app.js
    // http://localhost:8080/css/main.css
    // http://localhost:8080/profile/anyusername
    app.Run(iris.Addr(":8080"))

    // Note: In this example we just saw one use case,
    // you may want to .WrapRouter or .Downgrade in order to bypass the iris' default router, i.e:
    // you can use that method to setup custom proxies too.
    //
    // If you just want to serve static files on other path than root
    // you can just use the StaticWeb, i.e:
    // 					     .StaticWeb("/static", "./public")
    // ________________________________requestPath, systemPath
}
```

There is not much to say here, it's just a function wrapper which accepts the native response writer and request and the next handler which is the Iris' Router itself, it's being or not executed whether is called or not, **it's a middleware for the whole Router**.

# Error handlers

You can define your own handlers when a specific http error code occurs.

> Error codes are the http status codes that are bigger or equal to 400, like 404 not found and 500 internal server.

Example code:

```go
package main

import "github.com/kataras/iris"

func main(){
    app := iris.New()
    app.OnErrorCode(iris.StatusNotFound, notFound)
    app.OnErrorCode(iris.StatusInternalServerError, internalServerError)
    // to register a handler for all "error" status codes(context.StatusCodeNotSuccessful)
    // defaults to < 200 || >= 400:
    // app.OnAnyErrorCode(handler)
    app.Get("/", index)
    app.Run(iris.Addr(":8080"))
}

func notFound(ctx iris.Context) {
    // when 404 then render the template $views_dir/errors/404.html
    ctx.View("errors/404.html")
}

func internalServerError(ctx iris.Context) {
    ctx.WriteString("Oups something went wrong, try again")
}

func index(ctx context.Context) {
    ctx.View("index.html")
}
```

# Context Outline

The `iris.Context` source code can be found [here](https://github.com/kataras/iris/blob/master/context/context.go). Keep note using an IDE/Editors with `auto-complete` feature will help you a lot.

```go
// Context is the midle-man server's "object" for the clients.
//
// A New context is being acquired from a sync.Pool on each connection.
// The Context is the most important thing on the iris's http flow.
//
// Developers send responses to the client's request through a Context.
// Developers get request information from the client's request a Context.
//
// This context is an implementation of the context.Context sub-package.
// context.Context is very extensible and developers can override
// its methods if that is actually needed.
type Context interface {
    // ResponseWriter returns an http.ResponseWriter compatible response writer, as expected.
    ResponseWriter() ResponseWriter
    // ResetResponseWriter should change or upgrade the Context's ResponseWriter.
    ResetResponseWriter(ResponseWriter)

    // Request returns the original *http.Request, as expected.
    Request() *http.Request

    // SetCurrentRouteName sets the route's name internally,
    // in order to be able to find the correct current "read-only" Route when
    // end-developer calls the `GetCurrentRoute()` function.
    // It's being initialized by the Router, if you change that name
    // manually nothing really happens except that you'll get other
    // route via `GetCurrentRoute()`.
    // Instead, to execute a different path
    // from this context you should use the `Exec` function
    // or change the handlers via `SetHandlers/AddHandler` functions.
    SetCurrentRouteName(currentRouteName string)
    // GetCurrentRoute returns the current registered "read-only" route that
    // was being registered to this request's path.
    GetCurrentRoute() RouteReadOnly

    // Do calls the SetHandlers(handlers)
    // and executes the first handler,
    // handlers should not be empty.
    //
    // It's used by the router, developers may use that
    // to replace and execute handlers immediately.
    Do(Handlers)

    // AddHandler can add handler(s)
    // to the current request in serve-time,
    // these handlers are not persistenced to the router.
    //
    // Router is calling this function to add the route's handler.
    // If AddHandler called then the handlers will be inserted
    // to the end of the already-defined route's handler.
    //
    AddHandler(...Handler)
    // SetHandlers replaces all handlers with the new.
    SetHandlers(Handlers)
    // Handlers keeps tracking of the current handlers.
    Handlers() Handlers

    // HandlerIndex sets the current index of the
    // current context's handlers chain.
    // If -1 passed then it just returns the
    // current handler index without change the current index.rns that index, useless return value.
    //
    // Look Handlers(), Next() and StopExecution() too.
    HandlerIndex(n int) (currentIndex int)
    // Proceed is an alternative way to check if a particular handler
    // has been executed and called the `ctx.Next` function inside it.
    // This is useful only when you run a handler inside
    // another handler. It justs checks for before index and the after index.
    //
    // A usecase example is when you want to execute a middleware
    // inside controller's `BeginRequest` that calls the `ctx.Next` inside it.
    // The Controller looks the whole flow (BeginRequest, method handler, EndRequest)
    // as one handler, so `ctx.Next` will not be reflected to the method handler
    // if called from the `BeginRequest`.
    //
    // Although `BeginRequest` should NOT be used to call other handlers,
    // the `BeginRequest` has been introduced to be able to set
    // common data to all method handlers before their execution.
    // Controllers can accept middleware(s) from the MVC's Application's Router as normally.
    //
    // That said let's see an example of `ctx.Proceed`:
    //
    // var authMiddleware = basicauth.New(basicauth.Config{
    // 	Users: map[string]string{
    // 		"admin": "password",
    // 	},
    // })
    //
    // func (c *UsersController) BeginRequest(ctx iris.Context) {
    // 	if !ctx.Proceed(authMiddleware) {
    // 		ctx.StopExecution()
    // 	}
    // }
    // This Get() will be executed in the same handler as `BeginRequest`,
    // internally controller checks for `ctx.StopExecution`.
    // So it will not be fired if BeginRequest called the `StopExecution`.
    // func(c *UsersController) Get() []models.User {
    //	  return c.Service.GetAll()
    //}
    // Alternative way is `!ctx.IsStopped()` if middleware make use of the `ctx.StopExecution()` on failure.
    Proceed(Handler) bool
    // HandlerName returns the current handler's name, helpful for debugging.
    HandlerName() string
    // Next calls all the next handler from the handlers chain,
    // it should be used inside a middleware.
    //
    // Note: Custom context should override this method in order to be able to pass its own context.Context implementation.
    Next()
    // NextOr checks if chain has a next handler, if so then it executes it
    // otherwise it sets a new chain assigned to this Context based on the given handler(s)
    // and executes its first handler.
    //
    // Returns true if next handler exists and executed, otherwise false.
    //
    // Note that if no next handler found and handlers are missing then
    // it sends a Status Not Found (404) to the client and it stops the execution.
    NextOr(handlers ...Handler) bool
    // NextOrNotFound checks if chain has a next handler, if so then it executes it
    // otherwise it sends a Status Not Found (404) to the client and stops the execution.
    //
    // Returns true if next handler exists and executed, otherwise false.
    NextOrNotFound() bool
    // NextHandler returns (it doesn't execute) the next handler from the handlers chain.
    //
    // Use .Skip() to skip this handler if needed to execute the next of this returning handler.
    NextHandler() Handler
    // Skip skips/ignores the next handler from the handlers chain,
    // it should be used inside a middleware.
    Skip()
    // StopExecution if called then the following .Next calls are ignored,
    // as a result the next handlers in the chain will not be fire.
    StopExecution()
    // IsStopped checks and returns true if the current position of the Context is 255,
    // means that the StopExecution() was called.
    IsStopped() bool

    //  +------------------------------------------------------------+
    //  | Current "user/request" storage                             |
    //  | and share information between the handlers - Values().     |
    //  | Save and get named path parameters - Params()              |
    //  +------------------------------------------------------------+

    // Params returns the current url's named parameters key-value storage.
    // Named path parameters are being saved here.
    // This storage, as the whole Context, is per-request lifetime.
    Params() *RequestParams

    // Values returns the current "user" storage.
    // Named path parameters and any optional data can be saved here.
    // This storage, as the whole Context, is per-request lifetime.
    //
    // You can use this function to Set and Get local values
    // that can be used to share information between handlers and middleware.
    Values() *memstore.Store
    // Translate is the i18n (localization) middleware's function,
    // it calls the Get("translate") to return the translated value.
    //
    // Example: https://github.com/kataras/iris/tree/master/_examples/miscellaneous/i18n
    Translate(format string, args ...interface{}) string

    //  +------------------------------------------------------------+
    //  | Path, Host, Subdomain, IP, Headers etc...                  |
    //  +------------------------------------------------------------+

    // Method returns the request.Method, the client's http method to the server.
    Method() string
    // Path returns the full request path,
    // escaped if EnablePathEscape config field is true.
    Path() string
    // RequestPath returns the full request path,
    // based on the 'escape'.
    RequestPath(escape bool) string

    // Host returns the host part of the current url.
    Host() string
    // Subdomain returns the subdomain of this request, if any.
    // Note that this is a fast method which does not cover all cases.
    Subdomain() (subdomain string)
    // IsWWW returns true if the current subdomain (if any) is www.
    IsWWW() bool
    // RemoteAddr tries to parse and return the real client's request IP.
    //
    // Based on allowed headers names that can be modified from Configuration.RemoteAddrHeaders.
    //
    // If parse based on these headers fail then it will return the Request's `RemoteAddr` field
    // which is filled by the server before the HTTP handler.
    //
    // Look `Configuration.RemoteAddrHeaders`,
    //      `Configuration.WithRemoteAddrHeader(...)`,
    //      `Configuration.WithoutRemoteAddrHeader(...)` for more.
    RemoteAddr() string
    // GetHeader returns the request header's value based on its name.
    GetHeader(name string) string
    // IsAjax returns true if this request is an 'ajax request'( XMLHttpRequest)
    //
    // There is no a 100% way of knowing that a request was made via Ajax.
    // You should never trust data coming from the client, they can be easily overcome by spoofing.
    //
    // Note that "X-Requested-With" Header can be modified by any client(because of "X-"),
    // so don't rely on IsAjax for really serious stuff,
    // try to find another way of detecting the type(i.e, content type),
    // there are many blogs that describe these problems and provide different kind of solutions,
    // it's always depending on the application you're building,
    // this is the reason why this `IsAjax`` is simple enough for general purpose use.
    //
    // Read more at: https://developer.mozilla.org/en-US/docs/AJAX
    // and https://xhr.spec.whatwg.org/
    IsAjax() bool
    // IsMobile checks if client is using a mobile device(phone or tablet) to communicate with this server.
    // If the return value is true that means that the http client using a mobile
    // device to communicate with the server, otherwise false.
    //
    // Keep note that this checks the "User-Agent" request header.
    IsMobile() bool
    //  +------------------------------------------------------------+
    //  | Response Headers helpers                                   |
    //  +------------------------------------------------------------+

    // Header adds a header to the response writer.
    Header(name string, value string)

    // ContentType sets the response writer's header key "Content-Type" to the 'cType'.
    ContentType(cType string)
    // GetContentType returns the response writer's header value of "Content-Type"
    // which may, setted before with the 'ContentType'.
    GetContentType() string

    // GetContentLength returns the request's header value of "Content-Length".
    // Returns 0 if header was unable to be found or its value was not a valid number.
    GetContentLength() int64

    // StatusCode sets the status code header to the response.
    // Look .GetStatusCode too.
    StatusCode(statusCode int)
    // GetStatusCode returns the current status code of the response.
    // Look StatusCode too.
    GetStatusCode() int

    // Redirect sends a redirect response to the client
    // to a specific url or relative path.
    // accepts 2 parameters string and an optional int
    // first parameter is the url to redirect
    // second parameter is the http status should send,
    // default is 302 (StatusFound),
    // you can set it to 301 (Permant redirect)
    // or 303 (StatusSeeOther) if POST method,
    // or StatusTemporaryRedirect(307) if that's nessecery.
    Redirect(urlToRedirect string, statusHeader ...int)

    //  +------------------------------------------------------------+
    //  | Various Request and Post Data                              |
    //  +------------------------------------------------------------+

    // URLParam returns true if the url parameter exists, otherwise false.
    URLParamExists(name string) bool
    // URLParamDefault returns the get parameter from a request,
    // if not found then "def" is returned.
    URLParamDefault(name string, def string) string
    // URLParam returns the get parameter from a request, if any.
    URLParam(name string) string
    // URLParamTrim returns the url query parameter with trailing white spaces removed from a request.
    URLParamTrim(name string) string
    // URLParamTrim returns the escaped url query parameter from a request.
    URLParamEscape(name string) string
    // URLParamInt returns the url query parameter as int value from a request,
    // returns -1 and an error if parse failed.
    URLParamInt(name string) (int, error)
    // URLParamIntDefault returns the url query parameter as int value from a request,
    // if not found or parse failed then "def" is returned.
    URLParamIntDefault(name string, def int) int
    // URLParamInt64 returns the url query parameter as int64 value from a request,
    // returns -1 and an error if parse failed.
    URLParamInt64(name string) (int64, error)
    // URLParamInt64Default returns the url query parameter as int64 value from a request,
    // if not found or parse failed then "def" is returned.
    URLParamInt64Default(name string, def int64) int64
    // URLParamFloat64 returns the url query parameter as float64 value from a request,
    // returns -1 and an error if parse failed.
    URLParamFloat64(name string) (float64, error)
    // URLParamFloat64Default returns the url query parameter as float64 value from a request,
    // if not found or parse failed then "def" is returned.
    URLParamFloat64Default(name string, def float64) float64
    // URLParamBool returns the url query parameter as boolean value from a request,
    // returns an error if parse failed or not found.
    URLParamBool(name string) (bool, error)
    // URLParams returns a map of GET query parameters separated by comma if more than one
    // it returns an empty map if nothing found.
    URLParams() map[string]string

    // FormValueDefault returns a single parsed form value by its "name",
    // including both the URL field's query parameters and the POST or PUT form data.
    //
    // Returns the "def" if not found.
    FormValueDefault(name string, def string) string
    // FormValue returns a single parsed form value by its "name",
    // including both the URL field's query parameters and the POST or PUT form data.
    FormValue(name string) string
    // FormValues returns the parsed form data, including both the URL
    // field's query parameters and the POST or PUT form data.
    //
    // The default form's memory maximum size is 32MB, it can be changed by the
    // `iris#WithPostMaxMemory` configurator at main configuration passed on `app.Run`'s second argument.
    //
    // NOTE: A check for nil is necessary.
    FormValues() map[string][]string

    // PostValueDefault returns the parsed form data from POST, PATCH,
    // or PUT body parameters based on a "name".
    //
    // If not found then "def" is returned instead.
    PostValueDefault(name string, def string) string
    // PostValue returns the parsed form data from POST, PATCH,
    // or PUT body parameters based on a "name"
    PostValue(name string) string
    // PostValueTrim returns the parsed form data from POST, PATCH,
    // or PUT body parameters based on a "name",  without trailing spaces.
    PostValueTrim(name string) string
    // PostValueInt returns the parsed form data from POST, PATCH,
    // or PUT body parameters based on a "name", as int.
    //
    // If not found returns -1 and a non-nil error.
    PostValueInt(name string) (int, error)
    // PostValueIntDefault returns the parsed form data from POST, PATCH,
    // or PUT body parameters based on a "name", as int.
    //
    // If not found returns or parse errors the "def".
    PostValueIntDefault(name string, def int) int
    // PostValueInt64 returns the parsed form data from POST, PATCH,
    // or PUT body parameters based on a "name", as float64.
    //
    // If not found returns -1 and a no-nil error.
    PostValueInt64(name string) (int64, error)
    // PostValueInt64Default returns the parsed form data from POST, PATCH,
    // or PUT body parameters based on a "name", as int64.
    //
    // If not found or parse errors returns the "def".
    PostValueInt64Default(name string, def int64) int64
    // PostValueInt64Default returns the parsed form data from POST, PATCH,
    // or PUT body parameters based on a "name", as float64.
    //
    // If not found returns -1 and a non-nil error.
    PostValueFloat64(name string) (float64, error)
    // PostValueInt64Default returns the parsed form data from POST, PATCH,
    // or PUT body parameters based on a "name", as float64.
    //
    // If not found or parse errors returns the "def".
    PostValueFloat64Default(name string, def float64) float64
    // PostValueInt64Default returns the parsed form data from POST, PATCH,
    // or PUT body parameters based on a "name", as bool.
    //
    // If not found or value is false, then it returns false, otherwise true.
    PostValueBool(name string) (bool, error)
    // PostValues returns all the parsed form data from POST, PATCH,
    // or PUT body parameters based on a "name" as a string slice.
    //
    // The default form's memory maximum size is 32MB, it can be changed by the
    // `iris#WithPostMaxMemory` configurator at main configuration passed on `app.Run`'s second argument.
    PostValues(name string) []string
    // FormFile returns the first uploaded file that received from the client.
    //
    // The default form's memory maximum size is 32MB, it can be changed by the
    //  `iris#WithPostMaxMemory` configurator at main configuration passed on `app.Run`'s second argument.
    //
    // Example: https://github.com/kataras/iris/tree/master/_examples/http_request/upload-file
    FormFile(key string) (multipart.File, *multipart.FileHeader, error)
    // UploadFormFiles uploads any received file(s) from the client
    // to the system physical location "destDirectory".
    //
    // The second optional argument "before" gives caller the chance to
    // modify the *miltipart.FileHeader before saving to the disk,
    // it can be used to change a file's name based on the current request,
    // all FileHeader's options can be changed. You can ignore it if
    // you don't need to use this capability before saving a file to the disk.
    //
    // Note that it doesn't check if request body streamed.
    //
    // Returns the copied length as int64 and
    // a not nil error if at least one new file
    // can't be created due to the operating system's permissions or
    // http.ErrMissingFile if no file received.
    //
    // If you want to receive & accept files and manage them manually you can use the `context#FormFile`
    // instead and create a copy function that suits your needs, the below is for generic usage.
    //
    // The default form's memory maximum size is 32MB, it can be changed by the
    //  `iris#WithPostMaxMemory` configurator at main configuration passed on `app.Run`'s second argument.
    //
    // See `FormFile` to a more controlled to receive a file.
    //
    //
    // Example: https://github.com/kataras/iris/tree/master/_examples/http_request/upload-files
    UploadFormFiles(destDirectory string, before ...func(Context, *multipart.FileHeader)) (n int64, err error)

    //  +------------------------------------------------------------+
    //  | Custom HTTP Errors                                         |
    //  +------------------------------------------------------------+

    // NotFound emits an error 404 to the client, using the specific custom error error handler.
    // Note that you may need to call ctx.StopExecution() if you don't want the next handlers
    // to be executed. Next handlers are being executed on iris because you can alt the
    // error code and change it to a more specific one, i.e
    // users := app.Party("/users")
    // users.Done(func(ctx context.Context){ if ctx.StatusCode() == 400 { /*  custom error code for /users */ }})
    NotFound()

    //  +------------------------------------------------------------+
    //  | Body Readers                                               |
    //  +------------------------------------------------------------+

    // SetMaxRequestBodySize sets a limit to the request body size
    // should be called before reading the request body from the client.
    SetMaxRequestBodySize(limitOverBytes int64)

    // UnmarshalBody reads the request's body and binds it to a value or pointer of any type.
    // Examples of usage: context.ReadJSON, context.ReadXML.
    //
    // Example: https://github.com/kataras/iris/blob/master/_examples/http_request/read-custom-via-unmarshaler/main.go
    UnmarshalBody(outPtr interface{}, unmarshaler Unmarshaler) error
    // ReadJSON reads JSON from request's body and binds it to a pointer of a value of any json-valid type.
    //
    // Example: https://github.com/kataras/iris/blob/master/_examples/http_request/read-json/main.go
    ReadJSON(jsonObjectPtr interface{}) error
    // ReadXML reads XML from request's body and binds it to a pointer of a value of any xml-valid type.
    //
    // Example: https://github.com/kataras/iris/blob/master/_examples/http_request/read-xml/main.go
    ReadXML(xmlObjectPtr interface{}) error
    // ReadForm binds the formObject  with the form data
    // it supports any kind of struct.
    //
    // Example: https://github.com/kataras/iris/blob/master/_examples/http_request/read-form/main.go
    ReadForm(formObjectPtr interface{}) error

    //  +------------------------------------------------------------+
    //  | Body (raw) Writers                                         |
    //  +------------------------------------------------------------+

    // Write writes the data to the connection as part of an HTTP reply.
    //
    // If WriteHeader has not yet been called, Write calls
    // WriteHeader(http.StatusOK) before writing the data. If the Header
    // does not contain a Content-Type line, Write adds a Content-Type set
    // to the result of passing the initial 512 bytes of written data to
    // DetectContentType.
    //
    // Depending on the HTTP protocol version and the client, calling
    // Write or WriteHeader may prevent future reads on the
    // Request.Body. For HTTP/1.x requests, handlers should read any
    // needed request body data before writing the response. Once the
    // headers have been flushed (due to either an explicit Flusher.Flush
    // call or writing enough data to trigger a flush), the request body
    // may be unavailable. For HTTP/2 requests, the Go HTTP server permits
    // handlers to continue to read the request body while concurrently
    // writing the response. However, such behavior may not be supported
    // by all HTTP/2 clients. Handlers should read before writing if
    // possible to maximize compatibility.
    Write(body []byte) (int, error)
    // Writef formats according to a format specifier and writes to the response.
    //
    // Returns the number of bytes written and any write error encountered.
    Writef(format string, args ...interface{}) (int, error)
    // WriteString writes a simple string to the response.
    //
    // Returns the number of bytes written and any write error encountered.
    WriteString(body string) (int, error)

    // SetLastModified sets the "Last-Modified" based on the "modtime" input.
    // If "modtime" is zero then it does nothing.
    //
    // It's mostly internally on core/router and context packages.
    //
    // Note that modtime.UTC() is being used instead of just modtime, so
    // you don't have to know the internals in order to make that works.
    SetLastModified(modtime time.Time)
    // CheckIfModifiedSince checks if the response is modified since the "modtime".
    // Note that it has nothing to do with server-side caching.
    // It does those checks by checking if the "If-Modified-Since" request header
    // sent by client or a previous server response header
    // (e.g with WriteWithExpiration or StaticEmbedded or Favicon etc.)
    // is a valid one and it's before the "modtime".
    //
    // A check for !modtime && err == nil is necessary to make sure that
    // it's not modified since, because it may return false but without even
    // had the chance to check the client-side (request) header due to some errors,
    // like the HTTP Method is not "GET" or "HEAD" or if the "modtime" is zero
    // or if parsing time from the header failed.
    //
    // It's mostly used internally, e.g. `context#WriteWithExpiration`.
    //
    // Note that modtime.UTC() is being used instead of just modtime, so
    // you don't have to know the internals in order to make that works.
    CheckIfModifiedSince(modtime time.Time) (bool, error)
    // WriteNotModified sends a 304 "Not Modified" status code to the client,
    // it makes sure that the content type, the content length headers
    // and any "ETag" are removed before the response sent.
    //
    // It's mostly used internally on core/router/fs.go and context methods.
    WriteNotModified()
    // WriteWithExpiration like Write but it sends with an expiration datetime
    // which is refreshed every package-level `StaticCacheDuration` field.
    WriteWithExpiration(body []byte, modtime time.Time) (int, error)
    // StreamWriter registers the given stream writer for populating
    // response body.
    //
    // Access to context's and/or its' members is forbidden from writer.
    //
    // This function may be used in the following cases:
    //
    //     * if response body is too big (more than iris.LimitRequestBodySize(if setted)).
    //     * if response body is streamed from slow external sources.
    //     * if response body must be streamed to the client in chunks.
    //     (aka `http server push`).
    //
    // receives a function which receives the response writer
    // and returns false when it should stop writing, otherwise true in order to continue
    StreamWriter(writer func(w io.Writer) bool)

    //  +------------------------------------------------------------+
    //  | Body Writers with compression                              |
    //  +------------------------------------------------------------+
    // ClientSupportsGzip retruns true if the client supports gzip compression.
    ClientSupportsGzip() bool
    // WriteGzip accepts bytes, which are compressed to gzip format and sent to the client.
    // returns the number of bytes written and an error ( if the client doesn' supports gzip compression)
    // You may re-use this function in the same handler
    // to write more data many times without any troubles.
    WriteGzip(b []byte) (int, error)
    // TryWriteGzip accepts bytes, which are compressed to gzip format and sent to the client.
    // If client does not supprots gzip then the contents are written as they are, uncompressed.
    TryWriteGzip(b []byte) (int, error)
    // GzipResponseWriter converts the current response writer into a response writer
    // which when its .Write called it compress the data to gzip and writes them to the client.
    //
    // Can be also disabled with its .Disable and .ResetBody to rollback to the usual response writer.
    GzipResponseWriter() *GzipResponseWriter
    // Gzip enables or disables (if enabled before) the gzip response writer,if the client
    // supports gzip compression, so the following response data will
    // be sent as compressed gzip data to the client.
    Gzip(enable bool)

    //  +------------------------------------------------------------+
    //  | Rich Body Content Writers/Renderers                        |
    //  +------------------------------------------------------------+

    // ViewLayout sets the "layout" option if and when .View
    // is being called afterwards, in the same request.
    // Useful when need to set or/and change a layout based on the previous handlers in the chain.
    //
    // Note that the 'layoutTmplFile' argument can be setted to iris.NoLayout || view.NoLayout
    // to disable the layout for a specific view render action,
    // it disables the engine's configuration's layout property.
    //
    // Look .ViewData and .View too.
    //
    // Example: https://github.com/kataras/iris/tree/master/_examples/view/context-view-data/
    ViewLayout(layoutTmplFile string)
    // ViewData saves one or more key-value pair in order to be passed if and when .View
    // is being called afterwards, in the same request.
    // Useful when need to set or/and change template data from previous hanadlers in the chain.
    //
    // If .View's "binding" argument is not nil and it's not a type of map
    // then these data are being ignored, binding has the priority, so the main route's handler can still decide.
    // If binding is a map or context.Map then these data are being added to the view data
    // and passed to the template.
    //
    // After .View, the data are not destroyed, in order to be re-used if needed (again, in the same request as everything else),
    // to clear the view data, developers can call:
    // ctx.Set(ctx.Application().ConfigurationReadOnly().GetViewDataContextKey(), nil)
    //
    // If 'key' is empty then the value is added as it's (struct or map) and developer is unable to add other value.
    //
    // Look .ViewLayout and .View too.
    //
    // Example: https://github.com/kataras/iris/tree/master/_examples/view/context-view-data/
    ViewData(key string, value interface{})
    // GetViewData returns the values registered by `context#ViewData`.
    // The return value is `map[string]interface{}`, this means that
    // if a custom struct registered to ViewData then this function
    // will try to parse it to map, if failed then the return value is nil
    // A check for nil is always a good practise if different
    // kind of values or no data are registered via `ViewData`.
    //
    // Similarly to `viewData := ctx.Values().Get("iris.viewData")` or
    // `viewData := ctx.Values().Get(ctx.Application().ConfigurationReadOnly().GetViewDataContextKey())`.
    GetViewData() map[string]interface{}
    // View renders a template based on the registered view engine(s).
    // First argument accepts the filename, relative to the view engine's Directory and Extension,
    // i.e: if directory is "./templates" and want to render the "./templates/users/index.html"
    // then you pass the "users/index.html" as the filename argument.
    //
    // The second optional argument can receive a single "view model"
    // that will be binded to the view template if it's not nil,
    // otherwise it will check for previous view data stored by the `ViewData`
    // even if stored at any previous handler(middleware) for the same request.
    //
    // Look .ViewData` and .ViewLayout too.
    //
    // Examples: https://github.com/kataras/iris/tree/master/_examples/view
    View(filename string, optionalViewModel ...interface{}) error

    // Binary writes out the raw bytes as binary data.
    Binary(data []byte) (int, error)
    // Text writes out a string as plain text.
    Text(text string) (int, error)
    // HTML writes out a string as text/html.
    HTML(htmlContents string) (int, error)
    // JSON marshals the given interface object and writes the JSON response.
    JSON(v interface{}, options ...JSON) (int, error)
    // JSONP marshals the given interface object and writes the JSON response.
    JSONP(v interface{}, options ...JSONP) (int, error)
    // XML marshals the given interface object and writes the XML response.
    XML(v interface{}, options ...XML) (int, error)
    // Markdown parses the markdown to html and renders its result to the client.
    Markdown(markdownB []byte, options ...Markdown) (int, error)
    // YAML parses the "v" using the yaml parser and renders its result to the client.
    YAML(v interface{}) (int, error)
    //  +------------------------------------------------------------+
    //  | Serve files                                                |
    //  +------------------------------------------------------------+

    // ServeContent serves content, headers are autoset
    // receives three parameters, it's low-level function, instead you can use .ServeFile(string,bool)/SendFile(string,string)
    //
    //
    // You can define your own "Content-Type" with `context#ContentType`, before this function call.
    //
    // This function doesn't support resuming (by range),
    // use ctx.SendFile or router's `StaticWeb` instead.
    ServeContent(content io.ReadSeeker, filename string, modtime time.Time, gzipCompression bool) error
    // ServeFile serves a file (to send a file, a zip for example to the client you should use the `SendFile` instead)
    // receives two parameters
    // filename/path (string)
    // gzipCompression (bool)
    //
    // You can define your own "Content-Type" with `context#ContentType`, before this function call.
    //
    // This function doesn't support resuming (by range),
    // use ctx.SendFile or router's `StaticWeb` instead.
    //
    // Use it when you want to serve dynamic files to the client.
    ServeFile(filename string, gzipCompression bool) error
    // SendFile sends file for force-download to the client
    //
    // Use this instead of ServeFile to 'force-download' bigger files to the client.
    SendFile(filename string, destinationName string) error

    //  +------------------------------------------------------------+
    //  | Cookies                                                    |
    //  +------------------------------------------------------------+

    // SetCookie adds a cookie.
    // Use of the "options" is not required, they can be used to amend the "cookie".
    //
    // Example: https://github.com/kataras/iris/tree/master/_examples/cookies/basic
    SetCookie(cookie *http.Cookie, options ...CookieOption)
    // SetCookieKV adds a cookie, requires the name(string) and the value(string).
    //
    // By default it expires at 2 hours and it's added to the root path,
    // use the `CookieExpires` and `CookiePath` to modify them.
    // Alternatively: ctx.SetCookie(&http.Cookie{...})
    //
    // If you want to set custom the path:
    // ctx.SetCookieKV(name, value, iris.CookiePath("/custom/path/cookie/will/be/stored"))
    //
    // If you want to be visible only to current request path:
    // ctx.SetCookieKV(name, value, iris.CookieCleanPath/iris.CookiePath(""))
    // More:
    //                              iris.CookieExpires(time.Duration)
    //                              iris.CookieHTTPOnly(false)
    //
    // Example: https://github.com/kataras/iris/tree/master/_examples/cookies/basic
    SetCookieKV(name, value string, options ...CookieOption)
    // GetCookie returns cookie's value by it's name
    // returns empty string if nothing was found.
    //
    // If you want more than the value then:
    // cookie, err := ctx.Request().Cookie("name")
    //
    // Example: https://github.com/kataras/iris/tree/master/_examples/cookies/basic
    GetCookie(name string, options ...CookieOption) string
    // RemoveCookie deletes a cookie by it's name and path = "/".
    // Tip: change the cookie's path to the current one by: RemoveCookie("name", iris.CookieCleanPath)
    //
    // Example: https://github.com/kataras/iris/tree/master/_examples/cookies/basic
    RemoveCookie(name string, options ...CookieOption)
    // VisitAllCookies takes a visitor which loops
    // on each (request's) cookies' name and value.
    VisitAllCookies(visitor func(name string, value string))

    // MaxAge returns the "cache-control" request header's value
    // seconds as int64
    // if header not found or parse failed then it returns -1.
    MaxAge() int64

    //  +------------------------------------------------------------+
    //  | Advanced: Response Recorder and Transactions               |
    //  +------------------------------------------------------------+

    // Record transforms the context's basic and direct responseWriter to a ResponseRecorder
    // which can be used to reset the body, reset headers, get the body,
    // get & set the status code at any time and more.
    Record()
    // Recorder returns the context's ResponseRecorder
    // if not recording then it starts recording and returns the new context's ResponseRecorder
    Recorder() *ResponseRecorder
    // IsRecording returns the response recorder and a true value
    // when the response writer is recording the status code, body, headers and so on,
    // else returns nil and false.
    IsRecording() (*ResponseRecorder, bool)

    // BeginTransaction starts a scoped transaction.
    //
    // You can search third-party articles or books on how Business Transaction works (it's quite simple, especially here).
    //
    // Note that this is unique and new
    // (=I haver never seen any other examples or code in Golang on this subject, so far, as with the most of iris features...)
    // it's not covers all paths,
    // such as databases, this should be managed by the libraries you use to make your database connection,
    // this transaction scope is only for context's response.
    // Transactions have their own middleware ecosystem also, look iris.go:UseTransaction.
    //
    // See https://github.com/kataras/iris/tree/master/_examples/ for more
    BeginTransaction(pipe func(t *Transaction))
    // SkipTransactions if called then skip the rest of the transactions
    // or all of them if called before the first transaction
    SkipTransactions()
    // TransactionsSkipped returns true if the transactions skipped or canceled at all.
    TransactionsSkipped() bool

    // Exec calls the `context/Application#ServeCtx`
    // based on this context but with a changed method and path
    // like it was requested by the user, but it is not.
    //
    // Offline means that the route is registered to the iris and have all features that a normal route has
    // BUT it isn't available by browsing, its handlers executed only when other handler's context call them
    // it can validate paths, has sessions, path parameters and all.
    //
    // You can find the Route by app.GetRoute("theRouteName")
    // you can set a route name as: myRoute := app.Get("/mypath", handler)("theRouteName")
    // that will set a name to the route and returns its RouteInfo instance for further usage.
    //
    // It doesn't changes the global state, if a route was "offline" it remains offline.
    //
    // app.None(...) and app.GetRoutes().Offline(route)/.Online(route, method)
    //
    // Example: https://github.com/kataras/iris/tree/master/_examples/routing/route-state
    //
    // User can get the response by simple using rec := ctx.Recorder(); rec.Body()/rec.StatusCode()/rec.Header().
    //
    // Context's Values and the Session are kept in order to be able to communicate via the result route.
    //
    // It's for extreme use cases, 99% of the times will never be useful for you.
    Exec(method, path string)

    // RouteExists reports whether a particular route exists
    // It will search from the current subdomain of context's host, if not inside the root domain.
    RouteExists(method, path string) bool

    // Application returns the iris app instance which belongs to this context.
    // Worth to notice that this function returns an interface
    // of the Application, which contains methods that are safe
    // to be executed at serve-time. The full app's fields
    // and methods are not available here for the developer's safety.
    Application() Application

    // String returns the string representation of this request.
    // Each context has a unique string representation.
    // It can be used for simple debugging scenarios, i.e print context as string.
    //
    // What it returns? A number which declares the length of the
    // total `String` calls per executable application, followed
    // by the remote IP (the client) and finally the method:url.
    String() string
}
```# Websocket

[WebSocket](https://wikipedia.org/wiki/WebSocket) is a protocol that enables two-way persistent communication channels over TCP connections. It is used for applications such as chat, stock tickers, games, anywhere you want real-time functionality in a web application.

[View or download sample code](https://github.com/kataras/iris/tree/master/_examples/websocket).

## When to use it

Use WebSockets when you need to work directly with a socket connection. For example, you might need the best possible performance for a real-time game.

## How to use it

* import the `"github.com/kataras/iris/websocket"`
* Configure the websocket package.
* Accept WebSocket requests.
* Send and receive messages.

### Import the websocket package

```go
import "github.com/kataras/iris/websocket"
```

### Configure the websocket package

```go
import "github.com/kataras/iris/websocket"

func main() {
    ws := websocket.New(websocket.Config{
        ReadBufferSize:  1024,
        WriteBufferSize: 1024,
    })
}
```

#### Complete configuration

```go
// Config the websocket server configuration
// all of these are optional.
type Config struct {
    // IDGenerator used to create (and later on, set)
    // an ID for each incoming websocket connections (clients).
    // The request is an argument which you can use to generate the ID (from headers for example).
    // If empty then the ID is generated by DefaultIDGenerator: randomString(64)
    IDGenerator func(ctx context.Context) string
    // Error is the function that will be fired if any client couldn't upgrade the HTTP connection
    // to a websocket connection, a handshake error.
    Error func(w http.ResponseWriter, r *http.Request, status int, reason error)
    // CheckOrigin a function that is called right before the handshake,
    // if returns false then that client is not allowed to connect with the websocket server.
    CheckOrigin func(r *http.Request) bool
    // HandshakeTimeout specifies the duration for the handshake to complete.
    HandshakeTimeout time.Duration
    // WriteTimeout time allowed to write a message to the connection.
    // 0 means no timeout.
    // Default value is 0
    WriteTimeout time.Duration
    // ReadTimeout time allowed to read a message from the connection.
    // 0 means no timeout.
    // Default value is 0
    ReadTimeout time.Duration
    // PongTimeout allowed to read the next pong message from the connection.
    // Default value is 60 * time.Second
    PongTimeout time.Duration
    // PingPeriod send ping messages to the connection with this period. Must be less than PongTimeout.
    // Default value is 60 *time.Second
    PingPeriod time.Duration
    // MaxMessageSize max message size allowed from connection.
    // Default value is 1024
    MaxMessageSize int64
    // BinaryMessages set it to true in order to denotes binary data messages instead of utf-8 text
    // compatible if you wanna use the Connection's EmitMessage to send a custom binary data to the client, like a native server-client communication.
    // defaults to false
    BinaryMessages bool
    // ReadBufferSize is the buffer size for the underline reader
    // Default value is 4096
    ReadBufferSize int
    // WriteBufferSize is the buffer size for the underline writer
    // Default value is 4096
    WriteBufferSize int
    // EnableCompression specify if the server should attempt to negotiate per
    // message compression (RFC 7692). Setting this value to true does not
    // guarantee that compression will be supported. Currently only "no context
    // takeover" modes are supported.
    EnableCompression bool

    // Subprotocols specifies the server's supported protocols in order of
    // preference. If this field is set, then the Upgrade method negotiates a
    // subprotocol by selecting the first match in this list with a protocol
    // requested by the client.
    Subprotocols []string
}
```

### Accept WebSocket requests & send & receive messages

```go
import (
    "github.com/kataras/iris"
    "github.com/kataras/iris/websocket"
)

func main() {
    ws := websocket.New(websocket.Config{
        ReadBufferSize:  1024,
        WriteBufferSize: 1024,
    })

    ws.OnConnection(handleConnection)

    app := iris.New()
    // register the server on an endpoint.
    // see the inline javascript code in the websockets.html, this endpoint is used to connect to the server.
    app.Get("/echo", ws.Handler())

    // serve the javascript built'n client-side library,
    // see websockets.html script tags, this path is used.
    app.Any("/iris-ws.js", func(ctx iris.Context) {
        ctx.Write(websocket.ClientSource)
    })
}

func handleConnection(c websocket.Connection) {
    // Read events from browser
    c.On("chat", func(msg string) {
        // Print the message to the console, c.Context() is the iris's http context.
        fmt.Printf("%s sent: %s\n", c.Context().RemoteAddr(), msg)
        // Write message back to the client message owner:
        // c.Emit("chat", msg)
        c.To(websocket.Broadcast).Emit("chat", msg)
    })
}
```Built'n Handlers
------------

| Middleware | Example |
| -----------|-------------|
| [basic authentication](basicauth) | [iris/_examples/authentication/basicauth](https://github.com/kataras/iris/tree/master/_examples/authentication/basicauth) |
| [Google reCAPTCHA](recaptcha) | [iris/_examples/miscellaneous/recaptcha](https://github.com/kataras/iris/tree/master/_examples/miscellaneous/recaptcha) |
| [localization and internationalization](i18n) | [iris/_examples/miscellaneous/i81n](https://github.com/kataras/iris/tree/master/_examples/miscellaneous/i18n) |
| [request logger](logger) | [iris/_examples/http_request/request-logger](https://github.com/kataras/iris/tree/master/_examples/http_request/request-logger) |
| [profiling (pprof)](pprof) | [iris/_examples/miscellaneous/pprof](https://github.com/kataras/iris/tree/master/_examples/miscellaneous/pprof) |
| [recovery](recover) | [iris/_examples/miscellaneous/recover](https://github.com/kataras/iris/tree/master/_examples/miscellaneous/recover) |

Experimental Handlers
------------

Most of the experimental handlers are ported to work with _iris_'s handler form, from third-party sources.

| Middleware | Description | Example |
| -----------|--------|-------------|
| [jwt](https://github.com/iris-contrib/middleware/tree/master/jwt) | Middleware checks for a JWT on the `Authorization` header on incoming requests and decodes it. | [iris-contrib/middleware/jwt/_example](https://github.com/iris-contrib/middleware/tree/master/jwt/_example) |
| [cors](https://github.com/iris-contrib/middleware/tree/master/cors) | HTTP Access Control. | [iris-contrib/middleware/cors/_example](https://github.com/iris-contrib/middleware/tree/master/cors/_example) |
| [secure](https://github.com/iris-contrib/middleware/tree/master/secure) | Middleware that implements a few quick security wins. | [iris-contrib/middleware/secure/_example](https://github.com/iris-contrib/middleware/tree/master/secure/_example/main.go) |
| [tollbooth](https://github.com/iris-contrib/middleware/tree/master/tollboothic) | Generic middleware to rate-limit HTTP requests. | [iris-contrib/middleware/tollbooth/_examples/limit-handler](https://github.com/iris-contrib/middleware/tree/master/tollbooth/_examples/limit-handler) |
| [cloudwatch](https://github.com/iris-contrib/middleware/tree/master/cloudwatch) |  AWS cloudwatch metrics middleware. |[iris-contrib/middleware/cloudwatch/_example](https://github.com/iris-contrib/middleware/tree/master/cloudwatch/_example) |
| [new relic](https://github.com/iris-contrib/middleware/tree/master/newrelic) | Official [New Relic Go Agent](https://github.com/newrelic/go-agent). | [iris-contrib/middleware/newrelic/_example](https://github.com/iris-contrib/middleware/tree/master/newrelic/_example) |
| [prometheus](https://github.com/iris-contrib/middleware/tree/master/prometheus)| Easily create metrics endpoint for the [prometheus](http://prometheus.io) instrumentation tool | [iris-contrib/middleware/prometheus/_example](https://github.com/iris-contrib/middleware/tree/master/prometheus/_example) |
| [casbin](https://github.com/iris-contrib/middleware/tree/master/casbin)| An authorization library that supports access control models like ACL, RBAC, ABAC | [iris-contrib/middleware/casbin/_examples](https://github.com/iris-contrib/middleware/tree/master/casbin/_examples) |
| [raven](https://github.com/iris-contrib/middleware/tree/master/raven)| Sentry client in Go | [raven/_example](https://github.com/iris-contrib/middleware/blob/master/raven/_example/main.go) |
| [csrf](https://github.com/iris-contrib/middleware/tree/master/csrf)| Cross-Site Request Forgery Protection | [csrf/_example](https://github.com/iris-contrib/middleware/blob/master/csrf/_example/main.go) (hard-tested for Iris) **NEW** |
Third-Party Handlers
------------

iris has its own middleware form of `func(ctx context.Context)` but it's also compatible with all `net/http` middleware forms. See [here](https://github.com/kataras/iris/tree/master/_examples/convert-handlers).

Here's a small list of useful third-party handlers:

| Middleware | Description |
| -----------|-------------|
| [goth](https://github.com/markbates/goth) | OAuth, OAuth2 authentication. [Example](https://github.com/kataras/iris/tree/master/_examples/authentication/oauth2) |
| [binding](https://github.com/mholt/binding) | Data binding from HTTP requests into structs |
| [csp](https://github.com/awakenetworks/csp) | [Content Security Policy](https://www.w3.org/TR/CSP2/) (CSP) support |
| [delay](https://github.com/jeffbmartinez/delay) | Add delays/latency to endpoints. Useful when testing effects of high latency |
| [onthefly](https://github.com/xyproto/onthefly) | Generate TinySVG, HTML and CSS on the fly |
| [permissions2](https://github.com/xyproto/permissions2) | Cookies, users and permissions |
| [RestGate](https://github.com/pjebs/restgate) | Secure authentication for REST API endpoints |
| [stats](https://github.com/thoas/stats) | Store information about your web application (response time, etc.) |
| [VanGoH](https://github.com/auroratechnologies/vangoh) | Configurable [AWS-Style](http://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html) HMAC authentication middleware |
| [xrequestid](https://github.com/pilu/xrequestid) | Middleware that assigns a random X-Request-Id header to each request |
| [digits](https://github.com/bamarni/digits) | Middleware that handles [Twitter Digits](https://get.digits.com/) authentication |

> Feel free to put up your own middleware in this list!# Typescript

[Typescript](http://www.typescriptlang.org/) and [alm-tools cloud editor](http://alm.tools/) automation tools for the [iris](https://github.com/kataras/iris) web framework.


## Table of contents

* [Typescript compiler](_examples/typescript/main.go)
* [Alm-tools cloud editor](_examples/editor/main.go)![Iris vs .NET Core(C#) vs Node.js (Express)](https://iris-go.com/images/benchmark-new.png)]

## Hardware

* [Processor](screens/unix/system_info_cpu.png): Intel(R) Core(TM) **i7-4710HQ** CPU @ 2.50GHz
* [RAM](screens/unix/system_info_ram.png): **8.00 GB**

## Software

* OS: Linux **Ubuntu** [Version **17.10**] with latest kernel version **4.14.0-041400-generic x86_64 GNU/Linux**
* HTTP Benchmark Tool: https://github.com/codesenberg/bombardier, latest version **1.1**
* **Iris [Go]**: https://github.com/kataras/iris, latest version **8.5.7** built with [go1.9.2](https://golang.org)
* **.NET Core [C#]**: https://www.microsoft.com/net/core, latest version **2.0.2**
* **Node.js (express + throng) [Javascript]**: https://nodejs.org/, latest version **9.2.0**, express: https://github.com/expressjs/express latest version **4.16.0** and [throng](https://www.npmjs.com/package/throng) latest version **4.0.0**

Go ahead to the [README.md](README.md) and read how you can reproduce the benchmarks. Don't be scary it's actually very easy, you can do these things as well!

## Results

* Throughput - `bigger is better`.
* Reqs/sec (Requests Per Second in Average) - `bigger is better`.
* Latency - `smaller is better`.
* Time To Complete - `smaller is better`.
* Total Requests in this fortune are all 1 million, in order to be easier to do the graph later on.

### Native

| Name | Throughput | Reqs/sec | Latency | Time To Complete | Total Requests |
|-------|:-----------|:--------|:-------------|---------|------|
| Iris | **29.31MB/s** | 157628 | 791.58us | 6s | 1000000 |
| Kestrel | **25.28MB/s** | 139642 | 0.89ms | 7s | 1000000 |
| Node.js | **13.69MB/s** | 50907 | 2.45ms | 19s | 1000000 |
| Iris with Sessions | **22.37MB/s** | 71922 | 1.74ms | 14s | 1000000 |
| Kestrel with Sessions | **14.51MB/s** | 31102 | 4.02ms | 32s | 1000000 |
| Node.js with Sessions | **5.08MB/s** | 19358 | 6.48ms | 51s | 1000000 |

> each test has its own screenshot, click [here](screens/unix) to explore

### MVC (Model View Controller)

| Name | Throughput | Reqs/sec | Latency | Time To Complete | Total Requests |
|-------|:-----------|:--------|:-------------|---------|------|
| Iris MVC | **26.39MB/s** | 141868 | 0.88ms | 7s | 1000000 |
| .Net Core MVC | **11.99MB/s** | 54418 | 2.30ms | 18s | 1000000 |
| - | - | - | - | - | - |
| Iris MVC with Templates | **136.58MB/s** | 18933 | 6.60ms | 52s | 1000000 |
| .Net Core MVC with Templates | **88.95MB/s** | 12347 | 10.12ms | 1m21s | 1000000 |
| - | - | - | - | - | - |

> nodejs express does not contain any MVC features

### Updates

- 21 November 2017: initial run and publish

## Articles (ms windows OS)

- https://hackernoon.com/go-vs-net-core-in-terms-of-http-performance-7535a61b67b8
- https://hackernoon.com/iris-go-vs-net-core-kestrel-in-terms-of-http-performance-806195dc93d5

**Thank you all** for the 100% green feedback, have fun!## Hardware

* Processor: Intel(R) Core(TM) **i7-4710HQ** CPU @ 2.50GHz 2.50GHz
* RAM: **8.00 GB**

## Software

* OS: Microsoft **Windows** [Version **10**.0.15063], power plan is "High performance"
* HTTP Benchmark Tool: https://github.com/codesenberg/bombardier, latest version **1.1**
* **.NET Core**: https://www.microsoft.com/net/core, latest version **2.0**
* **Iris**: https://github.com/kataras/iris, latest version **8.3** built with [go1.8.3](https://golang.org)

# .NET Core MVC vs Iris MVC

The first test will contain a simple application with a text response and the second will render templates + a layout.

## Simple

We will compare two identical things here, in terms of application, the expected response and the stability of their run times, so we will not try to put more things in the game like `JSON` or `XML` encoders and decoders, just a simple text message. To achieve a fair comparison we will use the MVC architecture pattern on both sides, Go and .NET Core.

### .NET Core MVC

```bash
$ cd netcore-mvc
$ dotnet run -c Release
Hosting environment: Production
Content root path: C:\mygopath\src\github.com\kataras\iris\_benchmarks\netcore-mvc
Now listening on: http://localhost:5000
Application started. Press Ctrl+C to shut down.
```

```bash
$ bombardier -c 125 -n 5000000 http://localhost:5000/api/values/5
Bombarding http://localhost:5000/api/values/5 with 5000000 requests using 125 connections
 5000000 / 5000000 [=====================================================================================] 100.00% 2m3s
Done!
Statistics        Avg      Stdev        Max
  Reqs/sec     40226.03    8724.30     161919
  Latency        3.09ms     1.40ms   169.12ms
  HTTP codes:
    1xx - 0, 2xx - 5000000, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:     8.91MB/s
```

### Iris MVC

```bash
$ cd iris-mvc
$ go run main.go
Now listening on: http://localhost:5000
Application started. Press CTRL+C to shut down.
```

```bash
$ bombardier -c 125 -n 5000000 http://localhost:5000/api/values/5
Bombarding http://localhost:5000/api/values/5 with 5000000 requests using 125 connections
 5000000 / 5000000 [======================================================================================] 100.00% 47s
Done!
Statistics        Avg      Stdev        Max
  Reqs/sec    105643.81    7687.79     122564
  Latency        1.18ms   366.55us    22.01ms
  HTTP codes:
    1xx - 0, 2xx - 5000000, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    19.65MB/s
```

Click [here](screens) to navigate to the screenshots.

### Summary

* Time to complete the `5000000 requests` - smaller is better.
* Reqs/sec - bigger is better.
* Latency - smaller is better
* Throughput - bigger is better.
* Memory usage - smaller is better.
* LOC (Lines Of Code) - smaller is better.

.NET Core MVC Application, written using 86 lines of code, ran for **2 minutes and 3 seconds** serving **40226.03** requests per second within **3.09ms** latency in average and **169.12ms** max, the memory usage of all these was ~123MB (without the dotnet host).

Iris MVC Application, written using 27 lines of code, ran for **47 seconds** serving **105643.71** requests per second within **1.18ms** latency in average and **22.01ms** max, the memory usage of all these was ~12MB.

#### Update: 20 August 2017

As [Josh Clark](https://twitter.com/clarkis117) and [Scott Hanselman‏](https://twitter.com/shanselman)‏ pointed out [on this status](https://twitter.com/shanselman/status/899005786826788865), on .NET Core MVC `Startup.cs` file the line with `services.AddMvc();` can be replaced with `services.AddMvcCore();`. I followed their helpful instructions and re-run the benchmarks. The article now contains the latest benchmark output for the .NET Core application with the change both Josh and Scott noted.

The twitter conversion: https://twitter.com/MakisMaropoulos/status/899113215895982080

For those who want to compare with the standard services.AddMvc(); you can see the old output by pressing [here](screens/5m_requests_netcore-mvc.png).

## MVC + Templates

Let’s run one more benchmark, spawn `1000000 requests` but this time we expect HTML generated by templates via the view engine.

### .NET Core MVC with Templates

```bash
$ cd netcore-mvc-templates
$ dotnet run -c Release
Hosting environment: Production
Content root path: C:\mygopath\src\github.com\kataras\iris\_benchmarks\netcore-mvc-templates
Now listening on: http://localhost:5000
Application started. Press Ctrl+C to shut down.
```

```bash
$ bombardier -c 125 -n 1000000 http://localhost:5000
Bombarding http://localhost:5000 with 1000000 requests using 125 connections
 1000000 / 1000000 [=====================================================================================] 100.00% 1m20s
Done!
Statistics        Avg      Stdev        Max
  Reqs/sec     11738.60    7741.36     125887
  Latency       10.10ms    22.10ms      1.97s
  HTTP codes:
    1xx - 0, 2xx - 1000000, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    89.03MB/s
```

### Iris MVC with Templates

```bash
$ cd iris-mvc-templates
$ go run main.go
Now listening on: http://localhost:5000
Application started. Press CTRL+C to shut down.
```

```bash
$ bombardier -c 125 -n 1000000 http://localhost:5000
Bombarding http://localhost:5000 with 1000000 requests using 125 connections
 1000000 / 1000000 [======================================================================================] 100.00% 37s
Done!
Statistics        Avg      Stdev        Max
  Reqs/sec     26656.76    1944.73      31188
  Latency        4.69ms     1.20ms    22.52ms
  HTTP codes:
    1xx - 0, 2xx - 1000000, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:   192.51MB/s
```

### Summary

* Time to complete the `1000000 requests` - smaller is better.
* Reqs/sec - bigger is better.
* Latency - smaller is better
* Memory usage - smaller is better.
* Throughput - bigger is better.

.NET Core MVC with Templates Application ran for **1 minute and 20 seconds** serving **11738.60** requests per second with **89.03MB/s** within **10.10ms** latency in average and **1.97s** max, the memory usage of all these was ~193MB (without the dotnet host).

Iris MVC with Templates Application ran for **37 seconds** serving **26656.76** requests per second with **192.51MB/s** within **1.18ms** latency in average and **22.52ms** max, the memory usage of all these was ~17MB.

# .NET Core (Kestrel) vs Iris

_Monday, 21 August 2017_

This time we will compare the speed of the “low-level” .NET Core’s server implementation named Kestrel and Iris’ “low-level” handlers, we will test two simple applications, the first will be the same as our previous application but written using handlers and the second test will contain a single route which sets and gets a session value(string) based on a key(string).

## Simple

Spawn `1000000 requests` with 125 different "threads", targeting to a dynamic registered route path, responds with a simple "value" text.

### .NET Core (Kestrel)

```bash
$ cd netcore
$ dotnet run -c Release
Hosting environment: Production
Content root path: C:\mygopath\src\github.com\kataras\iris\_benchmarks\netcore
Now listening on: http://localhost:5000
Application started. Press Ctrl+C to shut down.
```

```bash
$ bombardier -c 125 -n 1000000 http://localhost:5000/api/values/5
Bombarding http://localhost:5000/api/values/5 with 1000000 requests using 125 connections
 1000000 / 1000000 [======================================================================================] 100.00% 10s
Done!
Statistics        Avg      Stdev        Max
  Reqs/sec     97884.57    8699.94     110509
  Latency        1.28ms   682.63us    61.04ms
  HTTP codes:
    1xx - 0, 2xx - 1000000, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    17.73MB/s
```

### Iris

```bash
$ cd iris
$ go run main.go
Now listening on: http://localhost:5000
Application started. Press CTRL+C to shut down.
```

```bash
$ bombardier -c 125 -n 1000000 http://localhost:5000/api/values/5
Bombarding http://localhost:5000/api/values/5 with 1000000 requests using 125 connections
 1000000 / 1000000 [=======================================================================================] 100.00% 8s
Done!
Statistics        Avg      Stdev        Max
  Reqs/sec    117917.79    4437.04     125614
  Latency        1.06ms   278.12us    19.03ms
  HTTP codes:
    1xx - 0, 2xx - 1000000, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    21.93MB/s
```

### Node.js (Express)

```bash
$ cd expressjs
$ npm install
$ node app.js
Now listening on: http://localhost:5000
Application started. Press CTRL+C to shut down.
```

```bash
$ bombardier -c 125 -n 1000000 http://localhost:5000/api/values/5
Bombarding http://localhost:5000/api/values/5 with 1000000 requests using 125 connections
 1000000 / 1000000 [=======================================================================================] 100.00% 1m25s
Done!
Statistics        Avg      Stdev        Max
  Reqs/sec      11665.30   628.41       21978
  Latency        10.72ms   1.45ms    112.10ms
  HTTP codes:
    1xx - 0, 2xx - 1000000, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    3.14MB/s
```

### Summary

* Time to complete the `1000000 requests` - smaller is better.
* Reqs/sec - bigger is better.
* Latency - smaller is better
* Throughput - bigger is better.
* LOC (Lines Of Code) - smaller is better.

.NET Core (Kestrel) Application written using **63 code of lines** ran for **10 seconds** serving **97884.57** requests per second with **17.73MB/s** within **1.28ms** latency in average and **61.04ms** max.

Iris Application written using **14 code of lines** ran for **8 seconds** serving **117917.79** requests per second with **21.93MB/s** within **1.06ms** latency in average and **19.03ms** max.

Node.js (Express) Application written using **12 code of lines** ran for **1 minute and 25 seconds** serving **11665.30** requests per second with **3.14MB/s** within **10.72ms** latency in average and **112.10ms** max.

## Sessions

Spawn `5000000 requests` with 125 different "threads" targeting a static request path, sets and gets a session based on the name `"key"` and string value `"value"` and write that session value to the response stream.

### .NET Core (Kestrel) with Sessions

```bash
$ cd netcore-sessions
$ dotnet run -c Release
Hosting environment: Production
Content root path: C:\mygopath\src\github.com\kataras\iris\_benchmarks\netcore-sessions
Now listening on: http://localhost:5000
Application started. Press Ctrl+C to shut down.
```

```bash
$ bombardier -c 125 -n 5000000 http://localhost:5000/setget
Bombarding http://localhost:5000/setget with 5000000 requests using 125 connections
 5000000 / 5000000 [====================================================================================] 100.00% 2m40s
Done!
Statistics        Avg      Stdev        Max
  Reqs/sec     31844.77   13856.19     253746
  Latency        4.02ms    15.57ms      0.96s
  HTTP codes:
    1xx - 0, 2xx - 5000000, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    14.51MB/s
```

### Iris with Sessions

```bash
$ cd iris-sessions
$ go run main.go
Now listening on: http://localhost:5000
Application started. Press CTRL+C to shut down.
```

```bash
$ bombardier -c 125 -n 5000000 http://localhost:5000/setget
Bombarding http://localhost:5000/setget with 5000000 requests using 125 connections
 5000000 / 5000000 [====================================================================================] 100.00% 1m15s
Done!
Statistics        Avg      Stdev        Max
  Reqs/sec     66749.70   32110.67     110445
  Latency        1.88ms     9.13ms      1.94s
  HTTP codes:
    1xx - 0, 2xx - 5000000, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    20.65MB/s
```

### Node.js (Express) with Sessions

```bash
$ cd expressjs-sessions
$ npm install
$ node app.js
Now listening on: http://localhost:5000
Application started. Press CTRL+C to shut down.
```

```bash
$ bombardier -c 125 -n 5000000 http://localhost:5000/setget
Bombarding http://localhost:5000/setget with 5000000 requests using 125 connections
 5000000 / 5000000 [====================================================================================] 100.00% 15m47s
Done!
Statistics        Avg      Stdev        Max
  Reqs/sec      5634.27   2317.30         9945
  Latency       22.17ms    8.19ms     119.08ms
  HTTP codes:
    1xx - 0, 2xx - 5000000, 3xx - 0, 4xx - 0, 5xx - 0
    others - 0
  Throughput:    1.48MB/s
```

### Summary

* Time to complete the `5000000 requests` - smaller is better.
* Reqs/sec - bigger is better.
* Latency - smaller is better
* Throughput - bigger is better.

.NET Core with Sessions Application ran for **2 minutes and 40 seconds** serving **31844.77** requests per second with **14.51MB/s** within **4.02ms** latency in average and **0.96s** max.

Iris with Sessions Application ran for **1 minute and 15 seconds** serving **66749.70** requests per second with **20.65MB/s** within **1.88ms** latency in average and **1.94s** max.

Node.js (Express) with Sessions Application ran for **15 minutes and 47 seconds** serving **5634.27** requests per second with **1.48MB/s** within **22.17ms** latency in average and **119.08ms** max.

> Click [here](screens) to navigate to the screenshots.

### Articles

 **Go vs .NET Core in terms of HTTP performance (Sa, 19 August 2017)**

- https://medium.com/@kataras/go-vs-net-core-in-terms-of-http-performance-7535a61b67b8
- https://dev.to/kataras/go-vsnet-core-in-terms-of-http-performance

**Iris Go vs .NET Core Kestrel in terms of HTTP performance (Mo, 21 August 2017)** 

- https://medium.com/@kataras/iris-go-vs-net-core-kestrel-in-terms-of-http-performance-806195dc93d5

**Thank you all** for the 100% green feedback, have fun!# View

Iris supports 5 template engines out-of-the-box, developers can still use any external golang template engine,
as `context/context#ResponseWriter()` is an `io.Writer`.

All of these five template engines have common features with common API,
like Layout, Template Funcs, Party-specific layout, partial rendering and more.

- The standard html, its template parser is the [golang.org/pkg/html/template/](https://golang.org/pkg/html/template/)
- Django, its template parser is the [github.com/flosch/pongo2](https://github.com/flosch/pongo2)
- Pug(Jade), its template parser is the [github.com/Joker/jade](https://github.com/Joker/jade)
- Handlebars, its template parser is the [github.com/aymerick/raymond](https://github.com/aymerick/raymond)
- Amber, its template parser is the [github.com/eknkc/amber](https://github.com/eknkc/amber)

## Overview

```go
// file: main.go
package main

import "github.com/kataras/iris"

func main() {
    app := iris.New()
    // Load all templates from the "./views" folder
    // where extension is ".html" and parse them
    // using the standard `html/template` package.
    app.RegisterView(iris.HTML("./views", ".html"))

    // Method:    GET
    // Resource:  http://localhost:8080
    app.Get("/", func(ctx iris.Context) {
        // Bind: {{.message}} with "Hello world!"
        ctx.ViewData("message", "Hello world!")
        // Render template file: ./views/hello.html
        ctx.View("hello.html")
    })

    // Method:    GET
    // Resource:  http://localhost:8080/user/42
    app.Get("/user/{id:long}", func(ctx iris.Context) {
        userID, _ := ctx.Params().GetInt64("id")
        ctx.Writef("User ID: %d", userID)
    })

    // Start the server using a network address.
    app.Run(iris.Addr(":8080"))
}
```

```html
<!-- file: ./views/hello.html -->
<html>
<head>
    <title>Hello Page</title>
</head>
<body>
    <h1>{{.message}}</h1>
</body>
</html>
```

## Template functions

```go
package main

import "github.com/kataras/iris"

func main() {
    app := iris.New()

    // - standard html  | iris.HTML(...)
    // - django         | iris.Django(...)
    // - pug(jade)      | iris.Pug(...)
    // - handlebars     | iris.Handlebars(...)
    // - amber          | iris.Amber(...)
    tmpl := iris.HTML("./templates", ".html")

    // built'n template funcs are:
    //
    // - {{ urlpath "mynamedroute" "pathParameter_ifneeded" }}
    // - {{ render "header.html" }}
    // - {{ render_r "header.html" }} // partial relative path to current page
    // - {{ yield }}
    // - {{ current }}

    // register a custom template func.
    tmpl.AddFunc("greet", func(s string) string {
        return "Greetings " + s + "!"
    })

    // register the view engine to the views, this will load the templates.
    app.RegisterView(tmpl)

    app.Get("/", hi)

    // http://localhost:8080
    app.Run(iris.Addr(":8080"))
}

func hi(ctx iris.Context) {
    // render the template file "./templates/hi.html"
    ctx.View("hi.html")
}
```

```html
<!-- file: ./templates/hi.html -->
<b>{{greet "kataras"}}</b> <!-- will be rendered as: <b>Greetings kataras!</b> -->
```

## Embedded

View engine supports bundled(https://github.com/shuLhan/go-bindata) template files too.
`go-bindata` gives you two functions, `Assset` and `AssetNames`,
these can be setted to each of the template engines using the `.Binary` function.

Example code:

```go
package main

import "github.com/kataras/iris"

func main() {
    app := iris.New()
    // $ go get -u github.com/shuLhan/go-bindata/...
    // $ go-bindata ./templates/...
    // $ go build
    // $ ./embedding-templates-into-app
    // html files are not used, you can delete the folder and run the example
    app.RegisterView(iris.HTML("./templates", ".html").Binary(Asset, AssetNames))
    app.Get("/", hi)

    // http://localhost:8080
    app.Run(iris.Addr(":8080"))
}

type page struct {
    Title, Name string
}

func hi(ctx iris.Context) {
    //                      {{.Page.Title}} and {{Page.Name}}
    ctx.ViewData("Page", page{Title: "Hi Page", Name: "iris"})
    ctx.View("hi.html")
}
```

A real example can be found here: https://github.com/kataras/iris/tree/master/_examples/view/embedding-templates-into-app.

## Reload

Enable auto-reloading of templates on each request. Useful while developers are in dev mode
as they no neeed to restart their app on every template edit.

Example code:

```go
pugEngine := iris.Pug("./templates", ".jade")
pugEngine.Reload(true) // <--- set to true to re-build the templates on each request.
app.RegisterView(pugEngine)
```

## Examples

- [Overview](https://github.com/kataras/iris/blob/master/_examples/view/overview/main.go)
- [Hi](https://github.com/kataras/iris/blob/master/_examples/view/template_html_0/main.go)
- [A simple Layout](https://github.com/kataras/iris/blob/master/_examples/view/template_html_1/main.go)
- [Layouts: `yield` and `render` tmpl funcs](https://github.com/kataras/iris/blob/master/_examples/view/template_html_2/main.go)
- [The `urlpath` tmpl func](https://github.com/kataras/iris/blob/master/_examples/view/template_html_3/main.go)
- [The `url` tmpl func](https://github.com/kataras/iris/blob/master/_examples/view/template_html_4/main.go)
- [Inject Data Between Handlers](https://github.com/kataras/iris/blob/master/_examples/view/context-view-data/main.go)
- [Embedding Templates Into App Executable File](https://github.com/kataras/iris/blob/master/_examples/view/embedding-templates-into-app/main.go)

You can serve [quicktemplate](https://github.com/valyala/quicktemplate) files too, simply by using the `context#ResponseWriter`, take a look at the [iris/_examples/http_responsewriter/quicktemplate](https://github.com/kataras/iris/tree/master/_examples/http_responsewriter/quicktemplate) example.