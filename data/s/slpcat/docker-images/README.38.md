Gogs [![Build Status](https://travis-ci.org/gogits/gogs.svg?branch=master)](https://travis-ci.org/gogits/gogs) [![Build status](https://ci.appveyor.com/api/projects/status/b9uu5ejl933e2wlt/branch/master?svg=true)](https://ci.appveyor.com/project/Unknwon/gogs/branch/master) [![Crowdin](https://d322cqt584bo4o.cloudfront.net/gogs/localized.svg)](https://crowdin.com/project/gogs) [![Discord](https://img.shields.io/discord/382595433060499458.svg)](https://discord.gg/9aqdHU7)
=====================

![](https://github.com/gogits/gogs/blob/master/public/img/gogs-large-resize.png?raw=true)

##### Current tip version: [`.VERSION`](templates/.VERSION) (see [Releases](https://github.com/gogits/gogs/releases) for binary versions)

| Web | UI  | Preview  |
|:-------------:|:-------:|:-------:|
|![Dashboard](https://gogs.io/img/screenshots/1.png)|![Repository](https://gogs.io/img/screenshots/2.png)|![Editor](https://gogs.io/img/screenshots/3.png)|
|![Profile](https://gogs.io/img/screenshots/4.png)|![Diff](https://gogs.io/img/screenshots/5.png)|![Repository Settings](https://gogs.io/img/screenshots/6.png?ts=20170322)|
|![Webhook](https://gogs.io/img/screenshots/7.png)|![Organization](https://gogs.io/img/screenshots/8.png)|![Admin Dashboard](https://gogs.io/img/screenshots/9.png)|

### Important Notes

1. **YOU MUST READ [Contributing Code](https://github.com/gogits/gogs/wiki/Contributing-Code) BEFORE STARTING TO WORK ON A PULL REQUEST**.
2. Due to testing purpose, data of [try.gogs.io](https://try.gogs.io) was reset in **Jan 28, 2015** and will reset multiple times after. Please do **NOT** put your important data on the site.
3. The demo site [try.gogs.io](https://try.gogs.io) is running under `develop` branch.
4. If you think there are vulnerabilities in the project, please talk privately to **u@gogs.io**, and the name you want to be credited as. Thanks!
5. If you're interested in using APIs, we have experimental support with [documentation](https://github.com/gogits/go-gogs-client/wiki).
6. If your team/company is using Gogs and would like to put your logo on [our website](https://gogs.io), contact us by any means.

[简体中文](README_ZH.md)

## Purpose

The goal of this project is to make the easiest, fastest, and most painless way of setting up a self-hosted Git service. With Go, this can be done with an independent binary distribution across **ALL platforms** that Go supports, including Linux, macOS, Windows and ARM.

## Overview

- Please see the [Documentation](https://gogs.io/docs/intro) for common usages and change log.
- Want to try it before doing anything else? Do it [online](https://try.gogs.io/gogs/gogs)!
- Having trouble? Get help with [Troubleshooting](https://gogs.io/docs/intro/troubleshooting.html) or [User Forum](https://discuss.gogs.io/).
- Want to help with localization? Check out the [guide](https://gogs.io/docs/features/i18n.html)!

## Features

- Activity timeline
- SSH and HTTP/HTTPS protocols
- SMTP/LDAP/Reverse proxy authentication
- Reverse proxy with sub-path
- Account/Organization/Repository management
- Add/Remove repository collaborators
- Repository/Organization webhooks (including Slack and Discord)
- Repository Git hooks/deploy keys
- Repository issues, pull requests, wiki and protected branches
- Migrate and mirror repository and its wiki
- Web editor for repository files and wiki
- Jupyter Notebook
- Two-factor authentication
- Gravatar and Federated avatar with custom source
- Mail service
- Administration panel
- Supports MySQL, PostgreSQL, SQLite3, MSSQL and [TiDB](https://github.com/pingcap/tidb) (via MySQL protocol)
- Multi-language support ([29 languages](https://crowdin.com/project/gogs))

## Hardware Requirements

- A Raspberry Pi or $5 Digital Ocean Droplet is more than enough to get you started. Some even use 64MB RAM Docker [CaaS](https://blog.docker.com/2016/02/containers-as-a-service-caas/).
- 2 CPU cores and 512MB RAM would be the baseline for teamwork.
- Increase CPU cores when your team size gets significantly larger, memory footprint remains low.

## Browser Support

- Please see [Semantic UI](https://github.com/Semantic-Org/Semantic-UI#browser-support) for specific versions of supported browsers.
- The smallest resolution officially supported is **1024*768**, however the UI may still look right in smaller resolutions, but no promises or fixes.

## Installation

Make sure you install the [prerequisites](https://gogs.io/docs/installation) first.

There are 5 ways to install Gogs:

- [Install from binary](https://gogs.io/docs/installation/install_from_binary.html)
- [Install from source](https://gogs.io/docs/installation/install_from_source.html)
- [Install from packages](https://gogs.io/docs/installation/install_from_packages.html)
- [Ship with Docker](https://github.com/gogits/gogs/tree/master/docker)
- [Install with Vagrant](https://github.com/geerlingguy/ansible-vagrant-examples/tree/master/gogs)

### Tutorials

- [How To Set Up Gogs on Ubuntu 14.04](https://www.digitalocean.com/community/tutorials/how-to-set-up-gogs-on-ubuntu-14-04)
- [Run your own GitHub-like service with the help of Docker](http://blog.hypriot.com/post/run-your-own-github-like-service-with-docker/)
- [Dockerized Gogs git server and alpine postgres in 20 minutes or less](http://garthwaite.org/docker-gogs.html)
- [Host Your Own Private GitHub with Gogs](https://eladnava.com/host-your-own-private-github-with-gogs-io/)
- [使用 Gogs 搭建自己的 Git 服务器](https://mynook.info/blog/post/host-your-own-git-server-using-gogs) (Chinese)
- [阿里云上 Ubuntu 14.04 64 位安装 Gogs](http://my.oschina.net/luyao/blog/375654) (Chinese)
- [Installing Gogs on FreeBSD](https://www.codejam.info/2015/03/installing-gogs-on-freebsd.html)
- [Gogs on Raspberry Pi](http://blog.meinside.pe.kr/Gogs-on-Raspberry-Pi/)
- [Cloudflare Full SSL with Gogs using NGINX](http://www.listekconsulting.com/articles/cloudflare-full-ssl-with-gogs-go-git-service-using-nginx/)

### Screencasts

- [How to install Gogs on a Linux Server (DigitalOcean)](https://www.youtube.com/watch?v=deSfX0gqefE)
- [Instalando Gogs no Ubuntu](https://www.youtube.com/watch?v=4UkHAR1F7ZA) (Português)

### Deploy to Cloud

- [OpenShift](https://github.com/tkisme/gogs-openshift)
- [Cloudron](https://cloudron.io/appstore.html#io.gogs.cloudronapp)
- [Scaleway](https://www.scaleway.com/imagehub/gogs/)
- [Sandstorm](https://github.com/cem/gogs-sandstorm)
- [sloppy.io](https://github.com/sloppyio/quickstarters/tree/master/gogs)
- [YunoHost](https://github.com/YunoHost-Apps/gogs_ynh)
- [DPlatform](https://github.com/j8r/DPlatform)

## Software and Service Support

- [Drone](https://github.com/drone/drone) (CI)
- [Jenkins](https://wiki.jenkins-ci.org/display/JENKINS/Gogs+Webhook+Plugin) (CI)
- [Fabric8](http://fabric8.io/) (DevOps)
- [Taiga](https://taiga.io/) (Project Management)
- [Puppet](https://forge.puppetlabs.com/Siteminds/gogs) (IT)
- [Kanboard](http://kanboard.net/plugin/gogs-webhook) (Project Management)
- [BearyChat](https://bearychat.com/) (Team Communication)
- [HiWork](http://www.hiwork.cc/) (Team Communication)
- [GitPitch](https://gitpitch.com/) (Markdown Presentations)

### Product Support

- [Synology](https://www.synology.com) (Docker)
- [One Space](http://www.onespace.cc) (App Store)

## Acknowledgments

- Thanks [Egon Elbre](https://twitter.com/egonelbre) for designing logo.
- Thanks [Crowdin](https://crowdin.com/project/gogs) for sponsoring open source translation plan.
- Thanks [DigitalOcean](https://www.digitalocean.com) for sponsoring VPS service.
- Thanks [KeyCDN](https://www.keycdn.com/) for sponsoring CDN service.

## Contributors

- See [contributors page](https://github.com/gogits/gogs/graphs/contributors) for top 100 contributors.
- See [TRANSLATORS](conf/locale/TRANSLATORS) for public list of translators.

## License

This project is under the MIT License. See the [LICENSE](https://github.com/gogits/gogs/blob/master/LICENSE) file for the full license text.
Gogs [![Build Status](https://travis-ci.org/gogits/gogs.svg?branch=master)](https://travis-ci.org/gogits/gogs) [![Build status](https://ci.appveyor.com/api/projects/status/b9uu5ejl933e2wlt/branch/master?svg=true)](https://ci.appveyor.com/project/Unknwon/gogs/branch/master)
=====================

Gogs 是一款极易搭建的自助 Git 服务。

## 开发目的

Gogs 的目标是打造一个最简单、最快速和最轻松的方式搭建自助 Git 服务。使用 Go 语言开发使得 Gogs 能够通过独立的二进制分发，并且支持 Go 语言支持的 **所有平台**，包括 Linux、macOS、Windows 以及 ARM 平台。

## 项目概览

- 有关基本用法和变更日志，请通过 [使用手册](https://gogs.io/docs/intro) 查看。
- 想要先睹为快？直接去 [在线体验](https://try.gogs.io/gogs/gogs) 。
- 使用过程中遇到问题？尝试从 [故障排查](https://gogs.io/docs/intro/troubleshooting.html) 页面或 [用户论坛](https://discuss.gogs.io/) 获取帮助。
- 希望帮助多国语言界面的翻译吗？请立即访问 [详情页面](https://gogs.io/docs/features/i18n.html)！

## 功能特性

- 支持活动时间线
- 支持 SSH 以及 HTTP/HTTPS 协议
- 支持 SMTP、LDAP 和反向代理的用户认证
- 支持反向代理子路径
- 支持用户、组织和仓库管理系统
- 支持添加和删除仓库协作者
- 支持仓库和组织级别 Web 钩子（包括 Slack 和 Discord 集成）
- 支持仓库 Git 钩子和部署密钥
- 支持仓库工单（Issue）、合并请求（Pull Request）、Wiki 和保护分支
- 支持迁移和镜像仓库以及它的 Wiki
- 支持在线编辑仓库文件和 Wiki
- 支持自定义源的 Gravatar 和 Federated Avatar
- 支持 Jupyter Notebook
- 支持两步验证登录
- 支持邮件服务
- 支持后台管理面板
- 支持 MySQL、PostgreSQL、SQLite3、MSSQL 和 [TiDB](https://github.com/pingcap/tidb)（通过 MySQL 协议）数据库
- 支持多语言本地化（[29 种语言]([more](https://crowdin.com/project/gogs))）

## 硬件要求

- 最低的系统硬件要求为一个廉价的树莓派
- 如果用于团队项目管理，建议使用 2 核 CPU 及 512MB 内存
- 当团队成员大量增加时，可以考虑添加 CPU 核数，内存占用保持不变

## 浏览器支持

- 请根据 [Semantic UI](https://github.com/Semantic-Org/Semantic-UI#browser-support) 查看具体支持的浏览器版本。
- 官方支持的最小 UI 尺寸为 **1024*768**，UI 不一定会在更小尺寸的设备上被破坏，但我们无法保证且不会修复。

## 安装部署

在安装 Gogs 之前，您需要先安装 [基本环境](https://gogs.io/docs/installation)。

然后，您可以通过以下 5 种方式来安装 Gogs：

- [二进制安装](https://gogs.io/docs/installation/install_from_binary.html)
- [源码安装](https://gogs.io/docs/installation/install_from_source.html)
- [包管理安装](https://gogs.io/docs/installation/install_from_packages.html)
- [采用 Docker 部署](https://github.com/gogits/gogs/tree/master/docker)
- [通过 Vagrant 安装](https://github.com/geerlingguy/ansible-vagrant-examples/tree/master/gogs)

### 使用教程

- [使用 Gogs 搭建自己的 Git 服务器](https://mynook.info/blog/post/host-your-own-git-server-using-gogs)
- [阿里云上 Ubuntu 14.04 64 位安装 Gogs](http://my.oschina.net/luyao/blog/375654)

### 云端部署

- [OpenShift](https://github.com/tkisme/gogs-openshift)
- [Cloudron](https://cloudron.io/appstore.html#io.gogs.cloudronapp)
- [Scaleway](https://www.scaleway.com/imagehub/gogs/)
- [Sandstorm](https://github.com/cem/gogs-sandstorm)
- [sloppy.io](https://github.com/sloppyio/quickstarters/tree/master/gogs)
- [YunoHost](https://github.com/mbugeia/gogs_ynh)
- [DPlatform](https://github.com/j8r/DPlatform)

## 软件及服务支持

- [Drone](https://github.com/drone/drone)（CI）
- [Jenkins](https://wiki.jenkins-ci.org/display/JENKINS/Gogs+Webhook+Plugin)（CI）
- [Fabric8](http://fabric8.io/)（DevOps）
- [Taiga](https://taiga.io/)（项目管理）
- [Puppet](https://forge.puppetlabs.com/Siteminds/gogs)（IT）
- [Kanboard](http://kanboard.net/plugin/gogs-webhook)（项目管理）
- [BearyChat](https://bearychat.com/)（团队交流）
- [HiWork](http://www.hiwork.cc/)（团队交流）
- [GitPitch](https://gitpitch.com/)（Markdown 演示）

### 产品支持

- [Synology](https://www.synology.com)（Docker）
- [One Space](http://www.onespace.cc)（应用商店）

## 特别鸣谢

- 感谢 [Egon Elbre](https://twitter.com/egonelbre) 设计的 Logo。
- 感谢 [Crowdin](https://crowdin.com/project/gogs) 提供免费的开源项目本地化支持。
- 感谢 [DigitalOcean](https://www.digitalocean.com) 提供主站和体验站点的服务器赞助。
- 感谢 [KeyCDN](https://www.keycdn.com/) 提供 CDN 服务赞助。

## 贡献成员

- 您可以通过查看 [贡献者页面](https://github.com/gogits/gogs/graphs/contributors) 获取 TOP 100 的贡献者列表。
- 您可以通过查看 [TRANSLATORS](conf/locale/TRANSLATORS) 文件获取公开的翻译人员列表。

## 授权许可

本项目采用 MIT 开源授权许可证，完整的授权说明已放置在 [LICENSE](https://github.com/gogits/gogs/blob/master/LICENSE) 文件中。
1. Delete package directory from vendor when developing new code of dependency.
2. After commit on dependency, run:
	govendor update <import path>
3. Introduce a new dependency, run:
	govendor add +vendor <import path>
4. To update all deependencies, delete all packages from vendor, and run:
	govendor add +vendor +external
5. Too hard.# Clog [![Build Status](https://travis-ci.org/go-clog/clog.svg?branch=master)](https://travis-ci.org/go-clog/clog) [![GoDoc](https://godoc.org/gopkg.in/clog.v1?status.svg)](https://godoc.org/gopkg.in/clog.v1) [![Sourcegraph](https://sourcegraph.com/github.com/go-clog/clog/-/badge.svg)](https://sourcegraph.com/github.com/go-clog/clog?badge)

![](https://avatars1.githubusercontent.com/u/25576866?v=3&s=200)

Clog is a channel-based logging package for Go.

This package supports multiple logger adapters across different levels of logging. It uses Go's native channel feature to provide goroutine-safe mechanism on large concurrency.

## Installation

To use a tagged revision:

	go get gopkg.in/clog.v1

To use with latest changes:

	go get github.com/go-clog/clog
    
Please apply `-u` flag to update in the future.

### Testing

If you want to test on your machine, please apply `-t` flag:

	go get -t gopkg.in/clog.v1

Please apply `-u` flag to update in the future.

## Getting Started

Clog currently has three builtin logger adapters: `console`, `file`, `slack` and `discord`.

It is extremely easy to create one with all default settings. Generally, you would want to create new logger inside `init` or `main` function.

```go
...

import (
	"fmt"
	"os"

	log "gopkg.in/clog.v1"
)

func init() {
	err := log.New(log.CONSOLE, log.ConsoleConfig{})
	if err != nil {
		fmt.Printf("Fail to create new logger: %v\n", err)
		os.Exit(1)
	}

	log.Trace("Hello %s!", "Clog")
	// Output: Hello Clog!

	log.Info("Hello %s!", "Clog")
	log.Warn("Hello %s!", "Clog")
	...
}

...
```

The above code is equivalent to the follow settings:

```go
...
	err := log.New(log.CONSOLE, log.ConsoleConfig{
		Level:      log.TRACE, // Record all logs
		BufferSize: 0,         // 0 means logging synchronously
	})
...
```

In production, you may want to make log less verbose and asynchronous:

```go
...
	err := log.New(log.CONSOLE, log.ConsoleConfig{
		// Logs under INFO level (in this case TRACE) will be discarded
		Level:      log.INFO, 
		// Number mainly depends on how many logs will be produced by program, 100 is good enough
		BufferSize: 100,      
	})
...
```

Console logger comes with color output, but for non-colorable destination, the color output will be disabled automatically.

### Error Location

When using `log.Error` and `log.Fatal` functions, the first argument allows you to indicate whether to print the code location or not. 

```go
...
	// 0 means disable printing code location
	log.Error(0, "So bad... %v", err)

	// To print appropriate code location mainly depends on how deep your call stack is, 
	// you need to try and verify
	log.Error(2, "So bad... %v", err)
	// Output: 2017/02/09 01:06:16 [ERROR] [...uban-builder/main.go:64 main()] ...
	log.Fatal(2, "Boom! %v", err)
	// Output: 2017/02/09 01:06:16 [FATAL] [...uban-builder/main.go:64 main()] ...
...
```

Calling `log.Fatal` will exit the program.

## File

File logger is more complex than console, and it has ability to rotate:

```go
...
	err := log.New(log.FILE, log.FileConfig{
		Level:              log.INFO, 
		BufferSize:         100,  
		Filename:           "clog.log",  
		FileRotationConfig: log.FileRotationConfig {
			Rotate: true,
			Daily:  true,
		},
	})
...
```

## Slack

Slack logger is also supported in a simple way:

```go
...
	err := log.New(log.SLACK, log.SlackConfig{
		Level:              log.INFO, 
		BufferSize:         100,  
		URL:                "https://url-to-slack-webhook",  
	})
...
```

This logger also works for [Discord Slack](https://discordapp.com/developers/docs/resources/webhook#execute-slackcompatible-webhook) endpoint.

## Discord

Discord logger is supported in rich format via [Embed Object](https://discordapp.com/developers/docs/resources/channel#embed-object):

```go
...
	err := log.New(log.DISCORD, log.DiscordConfig{
		Level:              log.INFO, 
		BufferSize:         100,  
		URL:                "https://url-to-discord-webhook",  
	})
...
```

This logger also retries automatically if hits rate limit after `retry_after`.

## Credits

- Avatar is a modified version based on [egonelbre/gophers' scientist](https://github.com/egonelbre/gophers/blob/master/vector/science/scientist.svg).

## License

This project is under Apache v2 License. See the [LICENSE](LICENSE) file for the full license text.[![GoDoc](https://godoc.org/gopkg.in/ldap.v2?status.svg)](https://godoc.org/gopkg.in/ldap.v2)
[![Build Status](https://travis-ci.org/go-ldap/ldap.svg)](https://travis-ci.org/go-ldap/ldap)

# Basic LDAP v3 functionality for the GO programming language.

## Install

For the latest version use:

    go get gopkg.in/ldap.v2

Import the latest version with:

    import "gopkg.in/ldap.v2"

## Required Libraries:

 - gopkg.in/asn1-ber.v1

## Features:

 - Connecting to LDAP server (non-TLS, TLS, STARTTLS)
 - Binding to LDAP server
 - Searching for entries
 - Filter Compile / Decompile
 - Paging Search Results
 - Modify Requests / Responses
 - Add Requests / Responses
 - Delete Requests / Responses

## Examples:

 - search
 - modify

## Contributing:

Bug reports and pull requests are welcome!

Before submitting a pull request, please make sure tests and verification scripts pass:
```
make all
```

To set up a pre-push hook to run the tests and verify scripts before pushing:
```
ln -s ../../.githooks/pre-push .git/hooks/pre-push
```

---
The Go gopher was designed by Renee French. (http://reneefrench.blogspot.com/)
The design is licensed under the Creative Commons 3.0 Attributions license.
Read this article for more details: http://blog.golang.org/gopher
# Gomail
[![Build Status](https://travis-ci.org/go-gomail/gomail.svg?branch=v2)](https://travis-ci.org/go-gomail/gomail) [![Code Coverage](http://gocover.io/_badge/gopkg.in/gomail.v2)](http://gocover.io/gopkg.in/gomail.v2) [![Documentation](https://godoc.org/gopkg.in/gomail.v2?status.svg)](https://godoc.org/gopkg.in/gomail.v2)

## Introduction

Gomail is a simple and efficient package to send emails. It is well tested and
documented.

Gomail can only send emails using an SMTP server. But the API is flexible and it
is easy to implement other methods for sending emails using a local Postfix, an
API, etc.

It is versioned using [gopkg.in](https://gopkg.in) so I promise
there will never be backward incompatible changes within each version.

It requires Go 1.2 or newer. With Go 1.5, no external dependencies are used.


## Features

Gomail supports:
- Attachments
- Embedded images
- HTML and text templates
- Automatic encoding of special characters
- SSL and TLS
- Sending multiple emails with the same SMTP connection


## Documentation

https://godoc.org/gopkg.in/gomail.v2


## Download

    go get gopkg.in/gomail.v2


## Examples

See the [examples in the documentation](https://godoc.org/gopkg.in/gomail.v2#example-package).


## FAQ

### x509: certificate signed by unknown authority

If you get this error it means the certificate used by the SMTP server is not
considered valid by the client running Gomail. As a quick workaround you can
bypass the verification of the server's certificate chain and host name by using
`SetTLSConfig`:

    package main

    import (
    	"crypto/tls"

    	"gopkg.in/gomail.v2"
    )

    func main() {
    	d := gomail.NewDialer("smtp.example.com", 587, "user", "123456")
    	d.TLSConfig = &tls.Config{InsecureSkipVerify: true}

        // Send emails using d.
    }

Note, however, that this is insecure and should not be used in production.


## Contribute

Contributions are more than welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for
more info.


## Change log

See [CHANGELOG.md](CHANGELOG.md).


## License

[MIT](LICENSE)


## Contact

You can ask questions on the [Gomail
thread](https://groups.google.com/d/topic/golang-nuts/jMxZHzvvEVg/discussion)
in the Go mailing-list.
Macaron [![Build Status](https://travis-ci.org/go-macaron/macaron.svg?branch=v1)](https://travis-ci.org/go-macaron/macaron)
=======================

![Macaron Logo](https://raw.githubusercontent.com/go-macaron/macaron/v1/macaronlogo.png)

Package macaron is a high productive and modular web framework in Go.

## Getting Started

The minimum requirement of Go is **1.3**.

To install Macaron:

	go get gopkg.in/macaron.v1

The very basic usage of Macaron:

```go
package main

import "gopkg.in/macaron.v1"

func main() {
	m := macaron.Classic()
	m.Get("/", func() string {
		return "Hello world!"
	})
	m.Run()
}
```

## Features

- Powerful routing with suburl.
- Flexible routes combinations.
- Unlimited nested group routers.
- Directly integrate with existing services.
- Dynamically change template files at runtime.
- Allow to use in-memory template and static files.
- Easy to plugin/unplugin features with modular design.
- Handy dependency injection powered by [inject](https://github.com/codegangsta/inject).
- Better router layer and less reflection make faster speed.

## Middlewares

Middlewares allow you easily plugin/unplugin features for your Macaron applications.

There are already many [middlewares](https://github.com/go-macaron) to simplify your work:

- render - Go template engine
- static - Serves static files
- [gzip](https://github.com/go-macaron/gzip) - Gzip compression to all responses
- [binding](https://github.com/go-macaron/binding) - Request data binding and validation
- [i18n](https://github.com/go-macaron/i18n) - Internationalization and Localization
- [cache](https://github.com/go-macaron/cache) - Cache manager
- [session](https://github.com/go-macaron/session) - Session manager
- [csrf](https://github.com/go-macaron/csrf) - Generates and validates csrf tokens
- [captcha](https://github.com/go-macaron/captcha) - Captcha service
- [pongo2](https://github.com/go-macaron/pongo2) - Pongo2 template engine support
- [sockets](https://github.com/go-macaron/sockets) - WebSockets channels binding
- [bindata](https://github.com/go-macaron/bindata) - Embed binary data as static and template files
- [toolbox](https://github.com/go-macaron/toolbox) - Health check, pprof, profile and statistic services
- [oauth2](https://github.com/go-macaron/oauth2) - OAuth 2.0 backend
- [authz](https://github.com/go-macaron/authz) - ACL/RBAC/ABAC authorization based on Casbin
- [switcher](https://github.com/go-macaron/switcher) - Multiple-site support
- [method](https://github.com/go-macaron/method) - HTTP method override
- [permissions2](https://github.com/xyproto/permissions2) - Cookies, users and permissions
- [renders](https://github.com/go-macaron/renders) - Beego-like render engine(Macaron has built-in template engine, this is another option)
- [piwik](https://github.com/veecue/piwik-middleware) - Server-side piwik analytics

## Use Cases

- [Gogs](https://gogs.io): A painless self-hosted Git Service
- [Grafana](http://grafana.org/): The open platform for beautiful analytics and monitoring
- [Peach](https://peachdocs.org): A modern web documentation server
- [Go Walker](https://gowalker.org): Go online API documentation
- [Switch](https://gopm.io): Gopm registry
- [Critical Stack Intel](https://intel.criticalstack.com/): A 100% free intel marketplace from Critical Stack, Inc.

## Getting Help

- [API Reference](https://gowalker.org/gopkg.in/macaron.v1)
- [Documentation](https://go-macaron.com)
- [FAQs](https://go-macaron.com/docs/faqs)

## Credits

- Basic design of [Martini](https://github.com/go-martini/martini).
- Logo is modified by [@insionng](https://github.com/insionng) based on [Tribal Dragon](http://xtremeyamazaki.deviantart.com/art/Tribal-Dragon-27005087).

## License

This project is under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for the full license text.
# quotedprintable

## Introduction

Package quotedprintable implements quoted-printable and message header encoding
as specified by RFC 2045 and RFC 2047.

It is a copy of the Go 1.5 package `mime/quotedprintable`. It also includes
the new functions of package `mime` concerning RFC 2047.

This code has minor changes with the standard library code in order to work
with Go 1.0 and newer. 

## Documentation

https://godoc.org/gopkg.in/alexcesaro/quotedprintable.v3
bufio
=====

This is a fork of the http://golang.org/pkg/bufio/ package. It adds `ReadN` method that allows reading next `n` bytes from the internal buffer without allocating intermediate buffer. This method works just like the [Buffer.Next](http://golang.org/pkg/bytes/#Buffer.Next) method, but has slightly different signature.
[![GoDoc](https://godoc.org/gopkg.in/editorconfig/editorconfig-core-go.v1?status.svg)](https://godoc.org/gopkg.in/editorconfig/editorconfig-core-go.v1)
[![Go Report Card](https://goreportcard.com/badge/gopkg.in/editorconfig/editorconfig-core-go.v1)](https://goreportcard.com/report/gopkg.in/editorconfig/editorconfig-core-go.v1)

# Editorconfig Core Go

A [Editorconfig][editorconfig] file parser and manipulator for Go.

> This package is already working, but still under testing.

## Installing

We recommend the use of [gopkg.in][gopkg] for this package:

```bash
go get -u gopkg.in/editorconfig/editorconfig-core-go.v1
```

Import by the same path. Tha package name you will use to access it is
`editorconfig`.

```go
import (
    "gopkg.in/editorconfig/editorconfig-core-go.v1"
)
```

## Usage

### Parse from file

```go
editorConfig, err := editorconfig.ParseFile("path/to/.editorconfig")
if err != nil {
    log.Fatal(err)
}
```

### Parse from slice of bytes

```go
data := []byte("...")
editorConfig, err := editorconfig.ParseBytes(data)
if err != nil {
    log.Fatal(err)
}
```

### Get definition to a given filename

This method builds a definition to a given filename.
This definition is a merge of the properties with selectors that matched the
given filename.
The lasts sections of the file have preference over the priors.

```go
def := editorConfig.GetDefinitionForFilename("my/file.go")
```

This definition have the following properties:

```go
type Definition struct {
	Selector string

	Charset                string
	IndentStyle            string
	IndentSize             string
	TabWidth               int
	EndOfLine              string
	TrimTrailingWhitespace bool
	InsertFinalNewline     bool
}
```

#### Automatic search for `.editorconfig` files

If you want a definition of a file without having to manually
parse the `.editorconfig` files, you can then use the static version
of `GetDefinitionForFilename`:

```go
def, err := editorconfig.GetDefinitionForFilename("foo/bar/baz/my-file.go")
```

In the example above, the package will automatically search for
`.editorconfig` files on:

- `foo/bar/baz/.editorconfig`
- `foo/baz/.editorconfig`
- `foo/.editorconfig`

Until it reaches a file with `root = true` or the root of the filesystem.

### Generating a .editorconfig file

You can easily convert a Editorconfig struct to a compatible INI file:

```go
// serialize to slice of bytes
data, err := editorConfig.Serialize()
if err != nil {
    log.Fatal(err)
}

// save directly to file
err := editorConfig.Save("path/to/.editorconfig")
if err != nil {
    log.Fatal(err)
}
```

## Contributing

To run the tests:

```bash
go test -v
```

[editorconfig]: http://editorconfig.org/
[gopkg]: https://gopkg.in
Redis client for Golang [![Build Status](https://travis-ci.org/go-redis/redis.png?branch=master)](https://travis-ci.org/go-redis/redis)
=======================

Supports:

- Redis 2.8 commands except QUIT, MONITOR, SLOWLOG and SYNC.
- Pub/sub.
- Transactions.
- Pipelining.
- Connection pool.
- TLS connections.
- Thread safety.
- Timeouts.
- Redis Sentinel.

API docs: http://godoc.org/gopkg.in/redis.v2.
Examples: http://godoc.org/gopkg.in/redis.v2#pkg-examples.

Installation
------------

Install:

    go get gopkg.in/redis.v2

Look and feel
-------------

Some corner cases:

    SORT list LIMIT 0 2 ASC
    vals, err := client.Sort("list", redis.Sort{Offset: 0, Count: 2, Order: "ASC"}).Result()

    ZRANGEBYSCORE zset -inf +inf WITHSCORES LIMIT 0 2
    vals, err := client.ZRangeByScoreWithScores("zset", redis.ZRangeByScore{
        Min: "-inf",
        Max: "+inf",
        Offset: 0,
        Count: 2,
    }).Result()

    ZINTERSTORE out 2 zset1 zset2 WEIGHTS 2 3 AGGREGATE SUM
    vals, err := client.ZInterStore("out", redis.ZStore{Weights: []int64{2, 3}}, "zset1", "zset2").Result()

    EVAL "return {KEYS[1],ARGV[1]}" 1 "key" "hello"
    vals, err := client.Eval("return {KEYS[1],ARGV[1]}", []string{"key"}, []string{"hello"}).Result()
INI [![Build Status](https://travis-ci.org/go-ini/ini.svg?branch=master)](https://travis-ci.org/go-ini/ini) [![Sourcegraph](https://sourcegraph.com/github.com/go-ini/ini/-/badge.svg)](https://sourcegraph.com/github.com/go-ini/ini?badge)
===

![](https://avatars0.githubusercontent.com/u/10216035?v=3&s=200)

Package ini provides INI file read and write functionality in Go.

[简体中文](README_ZH.md)

## Feature

- Load multiple data sources(`[]byte`, file and `io.ReadCloser`) with overwrites.
- Read with recursion values.
- Read with parent-child sections.
- Read with auto-increment key names.
- Read with multiple-line values.
- Read with tons of helper methods.
- Read and convert values to Go types.
- Read and **WRITE** comments of sections and keys.
- Manipulate sections, keys and comments with ease.
- Keep sections and keys in order as you parse and save.

## Installation

To use a tagged revision:

	go get gopkg.in/ini.v1

To use with latest changes:

	go get github.com/go-ini/ini

Please add `-u` flag to update in the future.

### Testing

If you want to test on your machine, please apply `-t` flag:

	go get -t gopkg.in/ini.v1

Please add `-u` flag to update in the future.

## Getting Started

### Loading from data sources

A **Data Source** is either raw data in type `[]byte`, a file name with type `string` or `io.ReadCloser`. You can load **as many data sources as you want**. Passing other types will simply return an error.

```go
cfg, err := ini.Load([]byte("raw data"), "filename", ioutil.NopCloser(bytes.NewReader([]byte("some other data"))))
```

Or start with an empty object:

```go
cfg := ini.Empty()
```

When you cannot decide how many data sources to load at the beginning, you will still be able to **Append()** them later.

```go
err := cfg.Append("other file", []byte("other raw data"))
```

If you have a list of files with possibilities that some of them may not available at the time, and you don't know exactly which ones, you can use `LooseLoad` to ignore nonexistent files without returning error.

```go
cfg, err := ini.LooseLoad("filename", "filename_404")
```

The cool thing is, whenever the file is available to load while you're calling `Reload` method, it will be counted as usual.

#### Ignore cases of key name

When you do not care about cases of section and key names, you can use `InsensitiveLoad` to force all names to be lowercased while parsing.

```go
cfg, err := ini.InsensitiveLoad("filename")
//...

// sec1 and sec2 are the exactly same section object
sec1, err := cfg.GetSection("Section")
sec2, err := cfg.GetSection("SecTIOn")

// key1 and key2 are the exactly same key object
key1, err := cfg.GetKey("Key")
key2, err := cfg.GetKey("KeY")
```

#### MySQL-like boolean key 

MySQL's configuration allows a key without value as follows:

```ini
[mysqld]
...
skip-host-cache
skip-name-resolve
```

By default, this is considered as missing value. But if you know you're going to deal with those cases, you can assign advanced load options:

```go
cfg, err := LoadSources(LoadOptions{AllowBooleanKeys: true}, "my.cnf"))
```

The value of those keys are always `true`, and when you save to a file, it will keep in the same foramt as you read.

To generate such keys in your program, you could use `NewBooleanKey`:

```go
key, err := sec.NewBooleanKey("skip-host-cache")
```

#### Comment

Take care that following format will be treated as comment:

1. Line begins with `#` or `;`
2. Words after `#` or `;`
3. Words after section name (i.e words after `[some section name]`)

If you want to save a value with `#` or `;`, please quote them with ``` ` ``` or ``` """ ```.

### Working with sections

To get a section, you would need to:

```go
section, err := cfg.GetSection("section name")
```

For a shortcut for default section, just give an empty string as name:

```go
section, err := cfg.GetSection("")
```

When you're pretty sure the section exists, following code could make your life easier:

```go
section := cfg.Section("section name")
```

What happens when the section somehow does not exist? Don't panic, it automatically creates and returns a new section to you.

To create a new section:

```go
err := cfg.NewSection("new section")
```

To get a list of sections or section names:

```go
sections := cfg.Sections()
names := cfg.SectionStrings()
```

### Working with keys

To get a key under a section:

```go
key, err := cfg.Section("").GetKey("key name")
```

Same rule applies to key operations:

```go
key := cfg.Section("").Key("key name")
```

To check if a key exists:

```go
yes := cfg.Section("").HasKey("key name")
```

To create a new key:

```go
err := cfg.Section("").NewKey("name", "value")
```

To get a list of keys or key names:

```go
keys := cfg.Section("").Keys()
names := cfg.Section("").KeyStrings()
```

To get a clone hash of keys and corresponding values:

```go
hash := cfg.Section("").KeysHash()
```

### Working with values

To get a string value:

```go
val := cfg.Section("").Key("key name").String()
```

To validate key value on the fly:

```go
val := cfg.Section("").Key("key name").Validate(func(in string) string {
	if len(in) == 0 {
		return "default"
	}
	return in
})
```

If you do not want any auto-transformation (such as recursive read) for the values, you can get raw value directly (this way you get much better performance):

```go
val := cfg.Section("").Key("key name").Value()
```

To check if raw value exists:

```go
yes := cfg.Section("").HasValue("test value")
```

To get value with types:

```go
// For boolean values:
// true when value is: 1, t, T, TRUE, true, True, YES, yes, Yes, y, ON, on, On
// false when value is: 0, f, F, FALSE, false, False, NO, no, No, n, OFF, off, Off
v, err = cfg.Section("").Key("BOOL").Bool()
v, err = cfg.Section("").Key("FLOAT64").Float64()
v, err = cfg.Section("").Key("INT").Int()
v, err = cfg.Section("").Key("INT64").Int64()
v, err = cfg.Section("").Key("UINT").Uint()
v, err = cfg.Section("").Key("UINT64").Uint64()
v, err = cfg.Section("").Key("TIME").TimeFormat(time.RFC3339)
v, err = cfg.Section("").Key("TIME").Time() // RFC3339

v = cfg.Section("").Key("BOOL").MustBool()
v = cfg.Section("").Key("FLOAT64").MustFloat64()
v = cfg.Section("").Key("INT").MustInt()
v = cfg.Section("").Key("INT64").MustInt64()
v = cfg.Section("").Key("UINT").MustUint()
v = cfg.Section("").Key("UINT64").MustUint64()
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339)
v = cfg.Section("").Key("TIME").MustTime() // RFC3339

// Methods start with Must also accept one argument for default value
// when key not found or fail to parse value to given type.
// Except method MustString, which you have to pass a default value.

v = cfg.Section("").Key("String").MustString("default")
v = cfg.Section("").Key("BOOL").MustBool(true)
v = cfg.Section("").Key("FLOAT64").MustFloat64(1.25)
v = cfg.Section("").Key("INT").MustInt(10)
v = cfg.Section("").Key("INT64").MustInt64(99)
v = cfg.Section("").Key("UINT").MustUint(3)
v = cfg.Section("").Key("UINT64").MustUint64(6)
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339, time.Now())
v = cfg.Section("").Key("TIME").MustTime(time.Now()) // RFC3339
```

What if my value is three-line long?

```ini
[advance]
ADDRESS = """404 road,
NotFound, State, 5000
Earth"""
```

Not a problem!

```go
cfg.Section("advance").Key("ADDRESS").String()

/* --- start ---
404 road,
NotFound, State, 5000
Earth
------  end  --- */
```

That's cool, how about continuation lines?

```ini
[advance]
two_lines = how about \
	continuation lines?
lots_of_lines = 1 \
	2 \
	3 \
	4
```

Piece of cake!

```go
cfg.Section("advance").Key("two_lines").String() // how about continuation lines?
cfg.Section("advance").Key("lots_of_lines").String() // 1 2 3 4
```

Well, I hate continuation lines, how do I disable that?

```go
cfg, err := ini.LoadSources(ini.LoadOptions{
	IgnoreContinuation: true,
}, "filename")
```

Holy crap! 

Note that single quotes around values will be stripped:

```ini
foo = "some value" // foo: some value
bar = 'some value' // bar: some value
```

That's all? Hmm, no.

#### Helper methods of working with values

To get value with given candidates:

```go
v = cfg.Section("").Key("STRING").In("default", []string{"str", "arr", "types"})
v = cfg.Section("").Key("FLOAT64").InFloat64(1.1, []float64{1.25, 2.5, 3.75})
v = cfg.Section("").Key("INT").InInt(5, []int{10, 20, 30})
v = cfg.Section("").Key("INT64").InInt64(10, []int64{10, 20, 30})
v = cfg.Section("").Key("UINT").InUint(4, []int{3, 6, 9})
v = cfg.Section("").Key("UINT64").InUint64(8, []int64{3, 6, 9})
v = cfg.Section("").Key("TIME").InTimeFormat(time.RFC3339, time.Now(), []time.Time{time1, time2, time3})
v = cfg.Section("").Key("TIME").InTime(time.Now(), []time.Time{time1, time2, time3}) // RFC3339
```

Default value will be presented if value of key is not in candidates you given, and default value does not need be one of candidates.

To validate value in a given range:

```go
vals = cfg.Section("").Key("FLOAT64").RangeFloat64(0.0, 1.1, 2.2)
vals = cfg.Section("").Key("INT").RangeInt(0, 10, 20)
vals = cfg.Section("").Key("INT64").RangeInt64(0, 10, 20)
vals = cfg.Section("").Key("UINT").RangeUint(0, 3, 9)
vals = cfg.Section("").Key("UINT64").RangeUint64(0, 3, 9)
vals = cfg.Section("").Key("TIME").RangeTimeFormat(time.RFC3339, time.Now(), minTime, maxTime)
vals = cfg.Section("").Key("TIME").RangeTime(time.Now(), minTime, maxTime) // RFC3339
```

##### Auto-split values into a slice

To use zero value of type for invalid inputs:

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> [0.0 2.2 0.0 0.0]
vals = cfg.Section("").Key("STRINGS").Strings(",")
vals = cfg.Section("").Key("FLOAT64S").Float64s(",")
vals = cfg.Section("").Key("INTS").Ints(",")
vals = cfg.Section("").Key("INT64S").Int64s(",")
vals = cfg.Section("").Key("UINTS").Uints(",")
vals = cfg.Section("").Key("UINT64S").Uint64s(",")
vals = cfg.Section("").Key("TIMES").Times(",")
```

To exclude invalid values out of result slice:

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> [2.2]
vals = cfg.Section("").Key("FLOAT64S").ValidFloat64s(",")
vals = cfg.Section("").Key("INTS").ValidInts(",")
vals = cfg.Section("").Key("INT64S").ValidInt64s(",")
vals = cfg.Section("").Key("UINTS").ValidUints(",")
vals = cfg.Section("").Key("UINT64S").ValidUint64s(",")
vals = cfg.Section("").Key("TIMES").ValidTimes(",")
```

Or to return nothing but error when have invalid inputs:

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> error
vals = cfg.Section("").Key("FLOAT64S").StrictFloat64s(",")
vals = cfg.Section("").Key("INTS").StrictInts(",")
vals = cfg.Section("").Key("INT64S").StrictInt64s(",")
vals = cfg.Section("").Key("UINTS").StrictUints(",")
vals = cfg.Section("").Key("UINT64S").StrictUint64s(",")
vals = cfg.Section("").Key("TIMES").StrictTimes(",")
```

### Save your configuration

Finally, it's time to save your configuration to somewhere.

A typical way to save configuration is writing it to a file:

```go
// ...
err = cfg.SaveTo("my.ini")
err = cfg.SaveToIndent("my.ini", "\t")
```

Another way to save is writing to a `io.Writer` interface:

```go
// ...
cfg.WriteTo(writer)
cfg.WriteToIndent(writer, "\t")
```

By default, spaces are used to align "=" sign between key and values, to disable that:

```go
ini.PrettyFormat = false
``` 

## Advanced Usage

### Recursive Values

For all value of keys, there is a special syntax `%(<name>)s`, where `<name>` is the key name in same section or default section, and `%(<name>)s` will be replaced by corresponding value(empty string if key not found). You can use this syntax at most 99 level of recursions.

```ini
NAME = ini

[author]
NAME = Unknwon
GITHUB = https://github.com/%(NAME)s

[package]
FULL_NAME = github.com/go-ini/%(NAME)s
```

```go
cfg.Section("author").Key("GITHUB").String()		// https://github.com/Unknwon
cfg.Section("package").Key("FULL_NAME").String()	// github.com/go-ini/ini
```

### Parent-child Sections

You can use `.` in section name to indicate parent-child relationship between two or more sections. If the key not found in the child section, library will try again on its parent section until there is no parent section.

```ini
NAME = ini
VERSION = v1
IMPORT_PATH = gopkg.in/%(NAME)s.%(VERSION)s

[package]
CLONE_URL = https://%(IMPORT_PATH)s

[package.sub]
```

```go
cfg.Section("package.sub").Key("CLONE_URL").String()	// https://gopkg.in/ini.v1
```

#### Retrieve parent keys available to a child section

```go
cfg.Section("package.sub").ParentKeys() // ["CLONE_URL"]
```

### Unparseable Sections

Sometimes, you have sections that do not contain key-value pairs but raw content, to handle such case, you can use `LoadOptions.UnparsableSections`:

```go
cfg, err := LoadSources(LoadOptions{UnparseableSections: []string{"COMMENTS"}}, `[COMMENTS]
<1><L.Slide#2> This slide has the fuel listed in the wrong units <e.1>`))

body := cfg.Section("COMMENTS").Body()

/* --- start ---
<1><L.Slide#2> This slide has the fuel listed in the wrong units <e.1>
------  end  --- */
```

### Auto-increment Key Names

If key name is `-` in data source, then it would be seen as special syntax for auto-increment key name start from 1, and every section is independent on counter.

```ini
[features]
-: Support read/write comments of keys and sections
-: Support auto-increment of key names
-: Support load multiple files to overwrite key values
```

```go
cfg.Section("features").KeyStrings()	// []{"#1", "#2", "#3"}
```

### Map To Struct

Want more objective way to play with INI? Cool.

```ini
Name = Unknwon
age = 21
Male = true
Born = 1993-01-01T20:17:05Z

[Note]
Content = Hi is a good man!
Cities = HangZhou, Boston
```

```go
type Note struct {
	Content string
	Cities  []string
}

type Person struct {
	Name string
	Age  int `ini:"age"`
	Male bool
	Born time.Time
	Note
	Created time.Time `ini:"-"`
}

func main() {
	cfg, err := ini.Load("path/to/ini")
	// ...
	p := new(Person)
	err = cfg.MapTo(p)
	// ...

	// Things can be simpler.
	err = ini.MapTo(p, "path/to/ini")
	// ...

	// Just map a section? Fine.
	n := new(Note)
	err = cfg.Section("Note").MapTo(n)
	// ...
}
```

Can I have default value for field? Absolutely.

Assign it before you map to struct. It will keep the value as it is if the key is not presented or got wrong type.

```go
// ...
p := &Person{
	Name: "Joe",
}
// ...
```

It's really cool, but what's the point if you can't give me my file back from struct?

### Reflect From Struct

Why not?

```go
type Embeded struct {
	Dates  []time.Time `delim:"|"`
	Places []string    `ini:"places,omitempty"`
	None   []int       `ini:",omitempty"`
}

type Author struct {
	Name      string `ini:"NAME"`
	Male      bool
	Age       int
	GPA       float64
	NeverMind string `ini:"-"`
	*Embeded
}

func main() {
	a := &Author{"Unknwon", true, 21, 2.8, "",
		&Embeded{
			[]time.Time{time.Now(), time.Now()},
			[]string{"HangZhou", "Boston"},
			[]int{},
		}}
	cfg := ini.Empty()
	err = ini.ReflectFrom(cfg, a)
	// ...
}
```

So, what do I get?

```ini
NAME = Unknwon
Male = true
Age = 21
GPA = 2.8

[Embeded]
Dates = 2015-08-07T22:14:22+08:00|2015-08-07T22:14:22+08:00
places = HangZhou,Boston
```

#### Name Mapper

To save your time and make your code cleaner, this library supports [`NameMapper`](https://gowalker.org/gopkg.in/ini.v1#NameMapper) between struct field and actual section and key name.

There are 2 built-in name mappers:

- `AllCapsUnderscore`: it converts to format `ALL_CAPS_UNDERSCORE` then match section or key.
- `TitleUnderscore`: it converts to format `title_underscore` then match section or key.

To use them:

```go
type Info struct {
	PackageName string
}

func main() {
	err = ini.MapToWithMapper(&Info{}, ini.TitleUnderscore, []byte("package_name=ini"))
	// ...

	cfg, err := ini.Load([]byte("PACKAGE_NAME=ini"))
	// ...
	info := new(Info)
	cfg.NameMapper = ini.AllCapsUnderscore
	err = cfg.MapTo(info)
	// ...
}
```

Same rules of name mapper apply to `ini.ReflectFromWithMapper` function.

#### Value Mapper

To expand values (e.g. from environment variables), you can use the `ValueMapper` to transform values:

```go
type Env struct {
	Foo string `ini:"foo"`
}

func main() {
	cfg, err := ini.Load([]byte("[env]\nfoo = ${MY_VAR}\n")
	cfg.ValueMapper = os.ExpandEnv
	// ...
	env := &Env{}
	err = cfg.Section("env").MapTo(env)
}
```

This would set the value of `env.Foo` to the value of the environment variable `MY_VAR`.

#### Other Notes On Map/Reflect

Any embedded struct is treated as a section by default, and there is no automatic parent-child relations in map/reflect feature:

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child
}

type Config struct {
	City string
	Parent
}
```

Example configuration:

```ini
City = Boston

[Parent]
Name = Unknwon

[Child]
Age = 21
```

What if, yes, I'm paranoid, I want embedded struct to be in the same section. Well, all roads lead to Rome.

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child `ini:"Parent"`
}

type Config struct {
	City string
	Parent
}
```

Example configuration:

```ini
City = Boston

[Parent]
Name = Unknwon
Age = 21
```

## Getting Help

- [API Documentation](https://gowalker.org/gopkg.in/ini.v1)
- [File An Issue](https://github.com/go-ini/ini/issues/new)

## FAQs

### What does `BlockMode` field do?

By default, library lets you read and write values so we need a locker to make sure your data is safe. But in cases that you are very sure about only reading data through the library, you can set `cfg.BlockMode = false` to speed up read operations about **50-70%** faster.

### Why another INI library?

Many people are using my another INI library [goconfig](https://github.com/Unknwon/goconfig), so the reason for this one is I would like to make more Go style code. Also when you set `cfg.BlockMode = false`, this one is about **10-30%** faster.

To make those changes I have to confirm API broken, so it's safer to keep it in another place and start using `gopkg.in` to version my package at this time.(PS: shorter import path)

## License

This project is under Apache v2 License. See the [LICENSE](LICENSE) file for the full license text.
本包提供了 Go 语言中读写 INI 文件的功能。

## 功能特性

- 支持覆盖加载多个数据源（`[]byte`、文件和 `io.ReadCloser`）
- 支持递归读取键值
- 支持读取父子分区
- 支持读取自增键名
- 支持读取多行的键值
- 支持大量辅助方法
- 支持在读取时直接转换为 Go 语言类型
- 支持读取和 **写入** 分区和键的注释
- 轻松操作分区、键值和注释
- 在保存文件时分区和键值会保持原有的顺序

## 下载安装

使用一个特定版本：

    go get gopkg.in/ini.v1

使用最新版：

	go get github.com/go-ini/ini

如需更新请添加 `-u` 选项。

### 测试安装

如果您想要在自己的机器上运行测试，请使用 `-t` 标记：

	go get -t gopkg.in/ini.v1

如需更新请添加 `-u` 选项。

## 开始使用

### 从数据源加载

一个 **数据源** 可以是 `[]byte` 类型的原始数据，`string` 类型的文件路径或 `io.ReadCloser`。您可以加载 **任意多个** 数据源。如果您传递其它类型的数据源，则会直接返回错误。

```go
cfg, err := ini.Load([]byte("raw data"), "filename", ioutil.NopCloser(bytes.NewReader([]byte("some other data"))))
```

或者从一个空白的文件开始：

```go
cfg := ini.Empty()
```

当您在一开始无法决定需要加载哪些数据源时，仍可以使用 **Append()** 在需要的时候加载它们。

```go
err := cfg.Append("other file", []byte("other raw data"))
```

当您想要加载一系列文件，但是不能够确定其中哪些文件是不存在的，可以通过调用函数 `LooseLoad` 来忽略它们（`Load` 会因为文件不存在而返回错误）：

```go
cfg, err := ini.LooseLoad("filename", "filename_404")
```

更牛逼的是，当那些之前不存在的文件在重新调用 `Reload` 方法的时候突然出现了，那么它们会被正常加载。

#### 忽略键名的大小写

有时候分区和键的名称大小写混合非常烦人，这个时候就可以通过 `InsensitiveLoad` 将所有分区和键名在读取里强制转换为小写：

```go
cfg, err := ini.InsensitiveLoad("filename")
//...

// sec1 和 sec2 指向同一个分区对象
sec1, err := cfg.GetSection("Section")
sec2, err := cfg.GetSection("SecTIOn")

// key1 和 key2 指向同一个键对象
key1, err := cfg.GetKey("Key")
key2, err := cfg.GetKey("KeY")
```

#### 类似 MySQL 配置中的布尔值键

MySQL 的配置文件中会出现没有具体值的布尔类型的键：

```ini
[mysqld]
...
skip-host-cache
skip-name-resolve
```

默认情况下这被认为是缺失值而无法完成解析，但可以通过高级的加载选项对它们进行处理：

```go
cfg, err := LoadSources(LoadOptions{AllowBooleanKeys: true}, "my.cnf"))
```

这些键的值永远为 `true`，且在保存到文件时也只会输出键名。

如果您想要通过程序来生成此类键，则可以使用 `NewBooleanKey`：

```go
key, err := sec.NewBooleanKey("skip-host-cache")
```

#### 关于注释

下述几种情况的内容将被视为注释：

1. 所有以 `#` 或 `;` 开头的行
2. 所有在 `#` 或 `;` 之后的内容
3. 分区标签后的文字 (即 `[分区名]` 之后的内容)

如果你希望使用包含 `#` 或 `;` 的值，请使用 ``` ` ``` 或 ``` """ ``` 进行包覆。

### 操作分区（Section）

获取指定分区：

```go
section, err := cfg.GetSection("section name")
```

如果您想要获取默认分区，则可以用空字符串代替分区名：

```go
section, err := cfg.GetSection("")
```

当您非常确定某个分区是存在的，可以使用以下简便方法：

```go
section := cfg.Section("section name")
```

如果不小心判断错了，要获取的分区其实是不存在的，那会发生什么呢？没事的，它会自动创建并返回一个对应的分区对象给您。

创建一个分区：

```go
err := cfg.NewSection("new section")
```

获取所有分区对象或名称：

```go
sections := cfg.Sections()
names := cfg.SectionStrings()
```

### 操作键（Key）

获取某个分区下的键：

```go
key, err := cfg.Section("").GetKey("key name")
```

和分区一样，您也可以直接获取键而忽略错误处理：

```go
key := cfg.Section("").Key("key name")
```

判断某个键是否存在：

```go
yes := cfg.Section("").HasKey("key name")
```

创建一个新的键：

```go
err := cfg.Section("").NewKey("name", "value")
```

获取分区下的所有键或键名：

```go
keys := cfg.Section("").Keys()
names := cfg.Section("").KeyStrings()
```

获取分区下的所有键值对的克隆：

```go
hash := cfg.Section("").KeysHash()
```

### 操作键值（Value）

获取一个类型为字符串（string）的值：

```go
val := cfg.Section("").Key("key name").String()
```

获取值的同时通过自定义函数进行处理验证：

```go
val := cfg.Section("").Key("key name").Validate(func(in string) string {
	if len(in) == 0 {
		return "default"
	}
	return in
})
```

如果您不需要任何对值的自动转变功能（例如递归读取），可以直接获取原值（这种方式性能最佳）：

```go
val := cfg.Section("").Key("key name").Value()
```

判断某个原值是否存在：

```go
yes := cfg.Section("").HasValue("test value")
```

获取其它类型的值：

```go
// 布尔值的规则：
// true 当值为：1, t, T, TRUE, true, True, YES, yes, Yes, y, ON, on, On
// false 当值为：0, f, F, FALSE, false, False, NO, no, No, n, OFF, off, Off
v, err = cfg.Section("").Key("BOOL").Bool()
v, err = cfg.Section("").Key("FLOAT64").Float64()
v, err = cfg.Section("").Key("INT").Int()
v, err = cfg.Section("").Key("INT64").Int64()
v, err = cfg.Section("").Key("UINT").Uint()
v, err = cfg.Section("").Key("UINT64").Uint64()
v, err = cfg.Section("").Key("TIME").TimeFormat(time.RFC3339)
v, err = cfg.Section("").Key("TIME").Time() // RFC3339

v = cfg.Section("").Key("BOOL").MustBool()
v = cfg.Section("").Key("FLOAT64").MustFloat64()
v = cfg.Section("").Key("INT").MustInt()
v = cfg.Section("").Key("INT64").MustInt64()
v = cfg.Section("").Key("UINT").MustUint()
v = cfg.Section("").Key("UINT64").MustUint64()
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339)
v = cfg.Section("").Key("TIME").MustTime() // RFC3339

// 由 Must 开头的方法名允许接收一个相同类型的参数来作为默认值，
// 当键不存在或者转换失败时，则会直接返回该默认值。
// 但是，MustString 方法必须传递一个默认值。

v = cfg.Seciont("").Key("String").MustString("default")
v = cfg.Section("").Key("BOOL").MustBool(true)
v = cfg.Section("").Key("FLOAT64").MustFloat64(1.25)
v = cfg.Section("").Key("INT").MustInt(10)
v = cfg.Section("").Key("INT64").MustInt64(99)
v = cfg.Section("").Key("UINT").MustUint(3)
v = cfg.Section("").Key("UINT64").MustUint64(6)
v = cfg.Section("").Key("TIME").MustTimeFormat(time.RFC3339, time.Now())
v = cfg.Section("").Key("TIME").MustTime(time.Now()) // RFC3339
```

如果我的值有好多行怎么办？

```ini
[advance]
ADDRESS = """404 road,
NotFound, State, 5000
Earth"""
```

嗯哼？小 case！

```go
cfg.Section("advance").Key("ADDRESS").String()

/* --- start ---
404 road,
NotFound, State, 5000
Earth
------  end  --- */
```

赞爆了！那要是我属于一行的内容写不下想要写到第二行怎么办？

```ini
[advance]
two_lines = how about \
	continuation lines?
lots_of_lines = 1 \
	2 \
	3 \
	4
```

简直是小菜一碟！

```go
cfg.Section("advance").Key("two_lines").String() // how about continuation lines?
cfg.Section("advance").Key("lots_of_lines").String() // 1 2 3 4
```

可是我有时候觉得两行连在一起特别没劲，怎么才能不自动连接两行呢？

```go
cfg, err := ini.LoadSources(ini.LoadOptions{
	IgnoreContinuation: true,
}, "filename")
```

哇靠给力啊！

需要注意的是，值两侧的单引号会被自动剔除：

```ini
foo = "some value" // foo: some value
bar = 'some value' // bar: some value
```

这就是全部了？哈哈，当然不是。

#### 操作键值的辅助方法

获取键值时设定候选值：

```go
v = cfg.Section("").Key("STRING").In("default", []string{"str", "arr", "types"})
v = cfg.Section("").Key("FLOAT64").InFloat64(1.1, []float64{1.25, 2.5, 3.75})
v = cfg.Section("").Key("INT").InInt(5, []int{10, 20, 30})
v = cfg.Section("").Key("INT64").InInt64(10, []int64{10, 20, 30})
v = cfg.Section("").Key("UINT").InUint(4, []int{3, 6, 9})
v = cfg.Section("").Key("UINT64").InUint64(8, []int64{3, 6, 9})
v = cfg.Section("").Key("TIME").InTimeFormat(time.RFC3339, time.Now(), []time.Time{time1, time2, time3})
v = cfg.Section("").Key("TIME").InTime(time.Now(), []time.Time{time1, time2, time3}) // RFC3339
```

如果获取到的值不是候选值的任意一个，则会返回默认值，而默认值不需要是候选值中的一员。

验证获取的值是否在指定范围内：

```go
vals = cfg.Section("").Key("FLOAT64").RangeFloat64(0.0, 1.1, 2.2)
vals = cfg.Section("").Key("INT").RangeInt(0, 10, 20)
vals = cfg.Section("").Key("INT64").RangeInt64(0, 10, 20)
vals = cfg.Section("").Key("UINT").RangeUint(0, 3, 9)
vals = cfg.Section("").Key("UINT64").RangeUint64(0, 3, 9)
vals = cfg.Section("").Key("TIME").RangeTimeFormat(time.RFC3339, time.Now(), minTime, maxTime)
vals = cfg.Section("").Key("TIME").RangeTime(time.Now(), minTime, maxTime) // RFC3339
```

##### 自动分割键值到切片（slice）

当存在无效输入时，使用零值代替：

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> [0.0 2.2 0.0 0.0]
vals = cfg.Section("").Key("STRINGS").Strings(",")
vals = cfg.Section("").Key("FLOAT64S").Float64s(",")
vals = cfg.Section("").Key("INTS").Ints(",")
vals = cfg.Section("").Key("INT64S").Int64s(",")
vals = cfg.Section("").Key("UINTS").Uints(",")
vals = cfg.Section("").Key("UINT64S").Uint64s(",")
vals = cfg.Section("").Key("TIMES").Times(",")
```

从结果切片中剔除无效输入：

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> [2.2]
vals = cfg.Section("").Key("FLOAT64S").ValidFloat64s(",")
vals = cfg.Section("").Key("INTS").ValidInts(",")
vals = cfg.Section("").Key("INT64S").ValidInt64s(",")
vals = cfg.Section("").Key("UINTS").ValidUints(",")
vals = cfg.Section("").Key("UINT64S").ValidUint64s(",")
vals = cfg.Section("").Key("TIMES").ValidTimes(",")
```

当存在无效输入时，直接返回错误：

```go
// Input: 1.1, 2.2, 3.3, 4.4 -> [1.1 2.2 3.3 4.4]
// Input: how, 2.2, are, you -> error
vals = cfg.Section("").Key("FLOAT64S").StrictFloat64s(",")
vals = cfg.Section("").Key("INTS").StrictInts(",")
vals = cfg.Section("").Key("INT64S").StrictInt64s(",")
vals = cfg.Section("").Key("UINTS").StrictUints(",")
vals = cfg.Section("").Key("UINT64S").StrictUint64s(",")
vals = cfg.Section("").Key("TIMES").StrictTimes(",")
```

### 保存配置

终于到了这个时刻，是时候保存一下配置了。

比较原始的做法是输出配置到某个文件：

```go
// ...
err = cfg.SaveTo("my.ini")
err = cfg.SaveToIndent("my.ini", "\t")
```

另一个比较高级的做法是写入到任何实现 `io.Writer` 接口的对象中：

```go
// ...
cfg.WriteTo(writer)
cfg.WriteToIndent(writer, "\t")
```

默认情况下，空格将被用于对齐键值之间的等号以美化输出结果，以下代码可以禁用该功能：

```go
ini.PrettyFormat = false
``` 

## 高级用法

### 递归读取键值

在获取所有键值的过程中，特殊语法 `%(<name>)s` 会被应用，其中 `<name>` 可以是相同分区或者默认分区下的键名。字符串 `%(<name>)s` 会被相应的键值所替代，如果指定的键不存在，则会用空字符串替代。您可以最多使用 99 层的递归嵌套。

```ini
NAME = ini

[author]
NAME = Unknwon
GITHUB = https://github.com/%(NAME)s

[package]
FULL_NAME = github.com/go-ini/%(NAME)s
```

```go
cfg.Section("author").Key("GITHUB").String()		// https://github.com/Unknwon
cfg.Section("package").Key("FULL_NAME").String()	// github.com/go-ini/ini
```

### 读取父子分区

您可以在分区名称中使用 `.` 来表示两个或多个分区之间的父子关系。如果某个键在子分区中不存在，则会去它的父分区中再次寻找，直到没有父分区为止。

```ini
NAME = ini
VERSION = v1
IMPORT_PATH = gopkg.in/%(NAME)s.%(VERSION)s

[package]
CLONE_URL = https://%(IMPORT_PATH)s

[package.sub]
```

```go
cfg.Section("package.sub").Key("CLONE_URL").String()	// https://gopkg.in/ini.v1
```

#### 获取上级父分区下的所有键名

```go
cfg.Section("package.sub").ParentKeys() // ["CLONE_URL"]
```

### 无法解析的分区

如果遇到一些比较特殊的分区，它们不包含常见的键值对，而是没有固定格式的纯文本，则可以使用 `LoadOptions.UnparsableSections` 进行处理：

```go
cfg, err := LoadSources(LoadOptions{UnparseableSections: []string{"COMMENTS"}}, `[COMMENTS]
<1><L.Slide#2> This slide has the fuel listed in the wrong units <e.1>`))

body := cfg.Section("COMMENTS").Body()

/* --- start ---
<1><L.Slide#2> This slide has the fuel listed in the wrong units <e.1>
------  end  --- */
```

### 读取自增键名

如果数据源中的键名为 `-`，则认为该键使用了自增键名的特殊语法。计数器从 1 开始，并且分区之间是相互独立的。

```ini
[features]
-: Support read/write comments of keys and sections
-: Support auto-increment of key names
-: Support load multiple files to overwrite key values
```

```go
cfg.Section("features").KeyStrings()	// []{"#1", "#2", "#3"}
```

### 映射到结构

想要使用更加面向对象的方式玩转 INI 吗？好主意。

```ini
Name = Unknwon
age = 21
Male = true
Born = 1993-01-01T20:17:05Z

[Note]
Content = Hi is a good man!
Cities = HangZhou, Boston
```

```go
type Note struct {
	Content string
	Cities  []string
}

type Person struct {
	Name string
	Age  int `ini:"age"`
	Male bool
	Born time.Time
	Note
	Created time.Time `ini:"-"`
}

func main() {
	cfg, err := ini.Load("path/to/ini")
	// ...
	p := new(Person)
	err = cfg.MapTo(p)
	// ...

	// 一切竟可以如此的简单。
	err = ini.MapTo(p, "path/to/ini")
	// ...

	// 嗯哼？只需要映射一个分区吗？
	n := new(Note)
	err = cfg.Section("Note").MapTo(n)
	// ...
}
```

结构的字段怎么设置默认值呢？很简单，只要在映射之前对指定字段进行赋值就可以了。如果键未找到或者类型错误，该值不会发生改变。

```go
// ...
p := &Person{
	Name: "Joe",
}
// ...
```

这样玩 INI 真的好酷啊！然而，如果不能还给我原来的配置文件，有什么卵用？

### 从结构反射

可是，我有说不能吗？

```go
type Embeded struct {
	Dates  []time.Time `delim:"|"`
	Places []string    `ini:"places,omitempty"`
	None   []int       `ini:",omitempty"`
}

type Author struct {
	Name      string `ini:"NAME"`
	Male      bool
	Age       int
	GPA       float64
	NeverMind string `ini:"-"`
	*Embeded
}

func main() {
	a := &Author{"Unknwon", true, 21, 2.8, "",
		&Embeded{
			[]time.Time{time.Now(), time.Now()},
			[]string{"HangZhou", "Boston"},
			[]int{},
		}}
	cfg := ini.Empty()
	err = ini.ReflectFrom(cfg, a)
	// ...
}
```

瞧瞧，奇迹发生了。

```ini
NAME = Unknwon
Male = true
Age = 21
GPA = 2.8

[Embeded]
Dates = 2015-08-07T22:14:22+08:00|2015-08-07T22:14:22+08:00
places = HangZhou,Boston
```

#### 名称映射器（Name Mapper）

为了节省您的时间并简化代码，本库支持类型为 [`NameMapper`](https://gowalker.org/gopkg.in/ini.v1#NameMapper) 的名称映射器，该映射器负责结构字段名与分区名和键名之间的映射。

目前有 2 款内置的映射器：

- `AllCapsUnderscore`：该映射器将字段名转换至格式 `ALL_CAPS_UNDERSCORE` 后再去匹配分区名和键名。
- `TitleUnderscore`：该映射器将字段名转换至格式 `title_underscore` 后再去匹配分区名和键名。

使用方法：

```go
type Info struct{
	PackageName string
}

func main() {
	err = ini.MapToWithMapper(&Info{}, ini.TitleUnderscore, []byte("package_name=ini"))
	// ...

	cfg, err := ini.Load([]byte("PACKAGE_NAME=ini"))
	// ...
	info := new(Info)
	cfg.NameMapper = ini.AllCapsUnderscore
	err = cfg.MapTo(info)
	// ...
}
```

使用函数 `ini.ReflectFromWithMapper` 时也可应用相同的规则。

#### 值映射器（Value Mapper）

值映射器允许使用一个自定义函数自动展开值的具体内容，例如：运行时获取环境变量：

```go
type Env struct {
	Foo string `ini:"foo"`
}

func main() {
	cfg, err := ini.Load([]byte("[env]\nfoo = ${MY_VAR}\n")
	cfg.ValueMapper = os.ExpandEnv
	// ...
	env := &Env{}
	err = cfg.Section("env").MapTo(env)
}
```

本例中，`env.Foo` 将会是运行时所获取到环境变量 `MY_VAR` 的值。

#### 映射/反射的其它说明

任何嵌入的结构都会被默认认作一个不同的分区，并且不会自动产生所谓的父子分区关联：

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child
}

type Config struct {
	City string
	Parent
}
```

示例配置文件：

```ini
City = Boston

[Parent]
Name = Unknwon

[Child]
Age = 21
```

很好，但是，我就是要嵌入结构也在同一个分区。好吧，你爹是李刚！

```go
type Child struct {
	Age string
}

type Parent struct {
	Name string
	Child `ini:"Parent"`
}

type Config struct {
	City string
	Parent
}
```

示例配置文件：

```ini
City = Boston

[Parent]
Name = Unknwon
Age = 21
```

## 获取帮助

- [API 文档](https://gowalker.org/gopkg.in/ini.v1)
- [创建工单](https://github.com/go-ini/ini/issues/new)

## 常见问题

### 字段 `BlockMode` 是什么？

默认情况下，本库会在您进行读写操作时采用锁机制来确保数据时间。但在某些情况下，您非常确定只进行读操作。此时，您可以通过设置 `cfg.BlockMode = false` 来将读操作提升大约 **50-70%** 的性能。

### 为什么要写另一个 INI 解析库？

许多人都在使用我的 [goconfig](https://github.com/Unknwon/goconfig) 来完成对 INI 文件的操作，但我希望使用更加 Go 风格的代码。并且当您设置 `cfg.BlockMode = false` 时，会有大约 **10-30%** 的性能提升。

为了做出这些改变，我必须对 API 进行破坏，所以新开一个仓库是最安全的做法。除此之外，本库直接使用 `gopkg.in` 来进行版本化发布。（其实真相是导入路径更短了）
[![GoDoc](https://godoc.org/gopkg.in/asn1-ber.v1?status.svg)](https://godoc.org/gopkg.in/asn1-ber.v1) [![Build Status](https://travis-ci.org/go-asn1-ber/asn1-ber.svg)](https://travis-ci.org/go-asn1-ber/asn1-ber)


ASN1 BER Encoding / Decoding Library for the GO programming language.
---------------------------------------------------------------------

Required libraries: 
   None

Working:
   Very basic encoding / decoding needed for LDAP protocol

Tests Implemented:
   A few

TODO:
   Fix all encoding / decoding to conform to ASN1 BER spec
   Implement Tests / Benchmarks

---

The Go gopher was designed by Renee French. (http://reneefrench.blogspot.com/)
The design is licensed under the Creative Commons 3.0 Attributions license.
Read this article for more details: http://blog.golang.org/gopher
identicon [![Build Status](https://travis-ci.org/issue9/identicon.svg?branch=master)](https://travis-ci.org/issue9/identicon)
======

根据用户的IP、邮箱名等任意数据为用户产生漂亮的随机头像。

![screenhost.1](https://raw.github.com/issue9/identicon/master/screenshot/1.png)
![screenhost.4](https://raw.github.com/issue9/identicon/master/screenshot/4.png)
![screenhost.5](https://raw.github.com/issue9/identicon/master/screenshot/5.png)
![screenhost.6](https://raw.github.com/issue9/identicon/master/screenshot/6.png)
![screenhost.7](https://raw.github.com/issue9/identicon/master/screenshot/7.png)

```go
// 根据用户访问的IP，为其生成一张头像
img, _ := identicon.Make(128, color.NRGBA{},color.NRGBA{}, []byte("192.168.1.1"))
fi, _ := os.Create("/tmp/u1.png")
png.Encode(fi, img)
fi.Close()

// 或者
ii, _ := identicon.New(128, color.NRGBA{}, color.NRGBA{}, color.NRGBA{}, color.NRGBA{})
img := ii.Make([]byte("192.168.1.1"))
img = ii.Make([]byte("192.168.1.2"))
```

### 安装

```shell
go get github.com/issue9/identicon
```


### 文档

[![Go Walker](http://gowalker.org/api/v1/badge)](http://gowalker.org/github.com/issue9/identicon)
[![GoDoc](https://godoc.org/github.com/issue9/identicon?status.svg)](https://godoc.org/github.com/issue9/identicon)


### 版权

本项目采用[MIT](http://opensource.org/licenses/MIT)开源授权许可证，完整的授权说明可在[LICENSE](LICENSE)文件中找到。
# go-colorable

Colorable writer for windows.

For example, most of logger packages doesn't show colors on windows. (I know we can do it with ansicon. But I don't want.)
This package is possible to handle escape sequence for ansi color on windows.

## Too Bad!

![](https://raw.githubusercontent.com/mattn/go-colorable/gh-pages/bad.png)


## So Good!

![](https://raw.githubusercontent.com/mattn/go-colorable/gh-pages/good.png)

## Usage

```go
logrus.SetFormatter(&logrus.TextFormatter{ForceColors: true})
logrus.SetOutput(colorable.NewColorableStdout())

logrus.Info("succeeded")
logrus.Warn("not correct")
logrus.Error("something error")
logrus.Fatal("panic")
```

You can compile above code on non-windows OSs.

## Installation

```
$ go get github.com/mattn/go-colorable
```

# License

MIT

# Author

Yasuhiro Matsumoto (a.k.a mattn)
# go-isatty

isatty for golang

## Usage

```go
package main

import (
	"fmt"
	"github.com/mattn/go-isatty"
	"os"
)

func main() {
	if isatty.IsTerminal(os.Stdout.Fd()) {
		fmt.Println("Is Terminal")
	} else {
		fmt.Println("Is Not Terminal")
	}
}
```

## Installation

```
$ go get github.com/mattn/go-isatty
```

# License

MIT

# Author

Yasuhiro Matsumoto (a.k.a mattn)
go-sqlite3
==========

[![Build Status](https://travis-ci.org/mattn/go-sqlite3.svg?branch=master)](https://travis-ci.org/mattn/go-sqlite3)
[![Coverage Status](https://coveralls.io/repos/mattn/go-sqlite3/badge.svg?branch=master)](https://coveralls.io/r/mattn/go-sqlite3?branch=master)
[![GoDoc](https://godoc.org/github.com/mattn/go-sqlite3?status.svg)](http://godoc.org/github.com/mattn/go-sqlite3)

Description
-----------

sqlite3 driver conforming to the built-in database/sql interface

Installation
------------

This package can be installed with the go get command:

    go get github.com/mattn/go-sqlite3
    
_go-sqlite3_ is *cgo* package.
If you want to build your app using go-sqlite3, you need gcc.
However, if you install _go-sqlite3_ with `go install github.com/mattn/go-sqlite3`, you don't need gcc to build your app anymore.
    
Documentation
-------------

API documentation can be found here: http://godoc.org/github.com/mattn/go-sqlite3

Examples can be found under the `./_example` directory

FAQ
---

* Want to build go-sqlite3 with libsqlite3 on my linux.

    Use `go build --tags "libsqlite3 linux"`

* Want to build go-sqlite3 with libsqlite3 on OS X.

    Install sqlite3 from homebrew: `brew install sqlite3`

    Use `go build --tags "libsqlite3 darwin"`

* Want to build go-sqlite3 with icu extension.

   Use `go build --tags "icu"`

* Can't build go-sqlite3 on windows 64bit.

    > Probably, you are using go 1.0, go1.0 has a problem when it comes to compiling/linking on windows 64bit. 
    > See: https://github.com/mattn/go-sqlite3/issues/27

* Getting insert error while query is opened.

    > You can pass some arguments into the connection string, for example, a URI.
    > See: https://github.com/mattn/go-sqlite3/issues/39

* Do you want to cross compile? mingw on Linux or Mac?

    > See: https://github.com/mattn/go-sqlite3/issues/106
    > See also: http://www.limitlessfx.com/cross-compile-golang-app-for-windows-from-linux.html

* Want to get time.Time with current locale

    Use `loc=auto` in SQLite3 filename schema like `file:foo.db?loc=auto`.

* Can use this in multiple routines concurrently?

    Yes for readonly. But, No for writable. See #50, #51, #209.

License
-------

MIT: http://mattn.mit-license.org/2012

sqlite3-binding.c, sqlite3-binding.h, sqlite3ext.h

The -binding suffix was added to avoid build failures under gccgo.

In this repository, those files are an amalgamation of code that was copied from SQLite3. The license of that code is the same as the license of SQLite3.

Author
------

Yasuhiro Matsumoto (a.k.a mattn)
Blackfriday [![Build Status](https://travis-ci.org/russross/blackfriday.svg?branch=master)](https://travis-ci.org/russross/blackfriday) [![GoDoc](https://godoc.org/github.com/russross/blackfriday?status.svg)](https://godoc.org/github.com/russross/blackfriday)
===========

Blackfriday is a [Markdown][1] processor implemented in [Go][2]. It
is paranoid about its input (so you can safely feed it user-supplied
data), it is fast, it supports common extensions (tables, smart
punctuation substitutions, etc.), and it is safe for all utf-8
(unicode) input.

HTML output is currently supported, along with Smartypants
extensions. An experimental LaTeX output engine is also included.

It started as a translation from C of [Sundown][3].


Installation
------------

Blackfriday is compatible with Go 1. If you are using an older
release of Go, consider using v1.1 of blackfriday, which was based
on the last stable release of Go prior to Go 1. You can find it as a
tagged commit on github.

With Go 1 and git installed:

    go get github.com/russross/blackfriday

will download, compile, and install the package into your `$GOPATH`
directory hierarchy. Alternatively, you can achieve the same if you
import it into a project:

    import "github.com/russross/blackfriday"

and `go get` without parameters.

Usage
-----

For basic usage, it is as simple as getting your input into a byte
slice and calling:

    output := blackfriday.MarkdownBasic(input)

This renders it with no extensions enabled. To get a more useful
feature set, use this instead:

    output := blackfriday.MarkdownCommon(input)

### Sanitize untrusted content

Blackfriday itself does nothing to protect against malicious content. If you are
dealing with user-supplied markdown, we recommend running blackfriday's output
through HTML sanitizer such as
[Bluemonday](https://github.com/microcosm-cc/bluemonday).

Here's an example of simple usage of blackfriday together with bluemonday:

``` go
import (
    "github.com/microcosm-cc/bluemonday"
    "github.com/russross/blackfriday"
)

// ...
unsafe := blackfriday.MarkdownCommon(input)
html := bluemonday.UGCPolicy().SanitizeBytes(unsafe)
```

### Custom options

If you want to customize the set of options, first get a renderer
(currently either the HTML or LaTeX output engines), then use it to
call the more general `Markdown` function. For examples, see the
implementations of `MarkdownBasic` and `MarkdownCommon` in
`markdown.go`.

You can also check out `blackfriday-tool` for a more complete example
of how to use it. Download and install it using:

    go get github.com/russross/blackfriday-tool

This is a simple command-line tool that allows you to process a
markdown file using a standalone program.  You can also browse the
source directly on github if you are just looking for some example
code:

* <http://github.com/russross/blackfriday-tool>

Note that if you have not already done so, installing
`blackfriday-tool` will be sufficient to download and install
blackfriday in addition to the tool itself. The tool binary will be
installed in `$GOPATH/bin`.  This is a statically-linked binary that
can be copied to wherever you need it without worrying about
dependencies and library versions.


Features
--------

All features of Sundown are supported, including:

*   **Compatibility**. The Markdown v1.0.3 test suite passes with
    the `--tidy` option.  Without `--tidy`, the differences are
    mostly in whitespace and entity escaping, where blackfriday is
    more consistent and cleaner.

*   **Common extensions**, including table support, fenced code
    blocks, autolinks, strikethroughs, non-strict emphasis, etc.

*   **Safety**. Blackfriday is paranoid when parsing, making it safe
    to feed untrusted user input without fear of bad things
    happening. The test suite stress tests this and there are no
    known inputs that make it crash.  If you find one, please let me
    know and send me the input that does it.

    NOTE: "safety" in this context means *runtime safety only*. In order to
    protect yourself against JavaScript injection in untrusted content, see
    [this example](https://github.com/russross/blackfriday#sanitize-untrusted-content).

*   **Fast processing**. It is fast enough to render on-demand in
    most web applications without having to cache the output.

*   **Thread safety**. You can run multiple parsers in different
    goroutines without ill effect. There is no dependence on global
    shared state.

*   **Minimal dependencies**. Blackfriday only depends on standard
    library packages in Go. The source code is pretty
    self-contained, so it is easy to add to any project, including
    Google App Engine projects.

*   **Standards compliant**. Output successfully validates using the
    W3C validation tool for HTML 4.01 and XHTML 1.0 Transitional.


Extensions
----------

In addition to the standard markdown syntax, this package
implements the following extensions:

*   **Intra-word emphasis supression**. The `_` character is
    commonly used inside words when discussing code, so having
    markdown interpret it as an emphasis command is usually the
    wrong thing. Blackfriday lets you treat all emphasis markers as
    normal characters when they occur inside a word.

*   **Tables**. Tables can be created by drawing them in the input
    using a simple syntax:

    ```
    Name    | Age
    --------|------
    Bob     | 27
    Alice   | 23
    ```

*   **Fenced code blocks**. In addition to the normal 4-space
    indentation to mark code blocks, you can explicitly mark them
    and supply a language (to make syntax highlighting simple). Just
    mark it like this:

        ``` go
        func getTrue() bool {
            return true
        }
        ```

    You can use 3 or more backticks to mark the beginning of the
    block, and the same number to mark the end of the block.

    To preserve classes of fenced code blocks while using the bluemonday
    HTML sanitizer, use the following policy:

    ``` go
    p := bluemonday.UGCPolicy()
    p.AllowAttrs("class").Matching(regexp.MustCompile("^language-[a-zA-Z0-9]+$")).OnElements("code")
    html := p.SanitizeBytes(unsafe)
    ```

*   **Definition lists**. A simple definition list is made of a single-line
    term followed by a colon and the definition for that term.

        Cat
        : Fluffy animal everyone likes
        
        Internet
        : Vector of transmission for pictures of cats

    Terms must be separated from the previous definition by a blank line.

*   **Footnotes**. A marker in the text that will become a superscript number;
    a footnote definition that will be placed in a list of footnotes at the
    end of the document. A footnote looks like this:

        This is a footnote.[^1]
        
        [^1]: the footnote text.

*   **Autolinking**. Blackfriday can find URLs that have not been
    explicitly marked as links and turn them into links.

*   **Strikethrough**. Use two tildes (`~~`) to mark text that
    should be crossed out.

*   **Hard line breaks**. With this extension enabled (it is off by
    default in the `MarkdownBasic` and `MarkdownCommon` convenience
    functions), newlines in the input translate into line breaks in
    the output.

*   **Smart quotes**. Smartypants-style punctuation substitution is
    supported, turning normal double- and single-quote marks into
    curly quotes, etc.

*   **LaTeX-style dash parsing** is an additional option, where `--`
    is translated into `&ndash;`, and `---` is translated into
    `&mdash;`. This differs from most smartypants processors, which
    turn a single hyphen into an ndash and a double hyphen into an
    mdash.

*   **Smart fractions**, where anything that looks like a fraction
    is translated into suitable HTML (instead of just a few special
    cases like most smartypant processors). For example, `4/5`
    becomes `<sup>4</sup>&frasl;<sub>5</sub>`, which renders as
    <sup>4</sup>&frasl;<sub>5</sub>.


Other renderers
---------------

Blackfriday is structured to allow alternative rendering engines. Here
are a few of note:

*   [github_flavored_markdown](https://godoc.org/github.com/shurcooL/github_flavored_markdown):
    provides a GitHub Flavored Markdown renderer with fenced code block
    highlighting, clickable header anchor links.

    It's not customizable, and its goal is to produce HTML output
    equivalent to the [GitHub Markdown API endpoint](https://developer.github.com/v3/markdown/#render-a-markdown-document-in-raw-mode),
    except the rendering is performed locally.

*   [markdownfmt](https://github.com/shurcooL/markdownfmt): like gofmt,
    but for markdown.

*   LaTeX output: renders output as LaTeX. This is currently part of the
    main Blackfriday repository, but may be split into its own project
    in the future. If you are interested in owning and maintaining the
    LaTeX output component, please be in touch.

    It renders some basic documents, but is only experimental at this
    point. In particular, it does not do any inline escaping, so input
    that happens to look like LaTeX code will be passed through without
    modification.
    
*   [Md2Vim](https://github.com/FooSoft/md2vim): transforms markdown files into vimdoc format.


Todo
----

*   More unit testing
*   Improve unicode support. It does not understand all unicode
    rules (about what constitutes a letter, a punctuation symbol,
    etc.), so it may fail to detect word boundaries correctly in
    some instances. It is safe on all utf-8 input.


License
-------

[Blackfriday is distributed under the Simplified BSD License](LICENSE.txt)


   [1]: http://daringfireball.net/projects/markdown/ "Markdown"
   [2]: http://golang.org/ "Go Language"
   [3]: https://github.com/vmg/sundown "Sundown"
#+TITLE: chaseadamsio/goorgeous

[[https://travis-ci.org/chaseadamsio/goorgeous.svg?branch=master]]
[[https://coveralls.io/repos/github/chaseadamsio/goorgeous/badge.svg?branch=master]]

/goorgeous is a Go Org to HTML Parser./

[[file:gopher_small.gif]] 

*Pronounced: Go? Org? Yes!*

#+BEGIN_QUOTE
"Org mode is for keeping notes, maintaining TODO lists, planning projects, and authoring documents with a fast and effective plain-text system."

- [[orgmode.org]]
#+END_QUOTE

The purpose of this package is to come as close as possible as parsing an =*.org= document into HTML, the same way one might publish [[http://orgmode.org/worg/org-tutorials/org-publish-html-tutorial.html][with org-publish-html from Emacs]]. 

* Installation

#+BEGIN_SRC sh
  go get -u github.com/chaseadamsio/goorgeous
#+END_SRC

* Usage

** Org Headers

To retreive the headers from a =[]byte=, call =OrgHeaders= and it will return a =map[string]interface{}=: 

#+BEGIN_SRC go
  input := "#+title: goorgeous\n* Some Headline\n"
  out := goorgeous.OrgHeaders(input) 
#+END_SRC

#+BEGIN_SRC go
  map[string]interface{}{ 
          "title": "goorgeous"
  }
#+END_SRC

** Org Content

After importing =github.com/chaseadamsio/goorgeous=, you can call =Org= with a =[]byte= and it will return an =html= version of the content as a =[]byte=

#+BEGIN_SRC go
  input := "#+TITLE: goorgeous\n* Some Headline\n"
  out := goorgeous.Org(input) 
#+END_SRC

=out= will be:

#+BEGIN_SRC html
  <h1>Some Headline</h1>/n
#+END_SRC

* Why? 

First off, I've become an unapologetic user of Emacs & ever since finding =org-mode= I use it for anything having to do with writing content, organizing my life and keeping documentation of my days/weeks/months.

Although I like Emacs & =emacs-lisp=, I publish all of my html sites with [[https://gohugo.io][Hugo Static Site Generator]] and wanted to be able to write my content in =org-mode= in Emacs rather than markdown.

Hugo's implementation of templating and speed are unmatched, so the only way I knew for sure I could continue to use Hugo and write in =org-mode= seamlessly was to write a golang parser for org content and submit a PR for Hugo to use it.
* Acknowledgements
I leaned heavily on russross' [[https://github.com/russross/blackfriday][blackfriday markdown renderer]] as both an example of how to write a parser (with some updates to leverage the go we know today) and reusing the blackfriday HTML Renderer so I didn't have to write my own!
gls
===

Goroutine local storage

### IMPORTANT NOTE ###

It is my duty to point you to https://blog.golang.org/context, which is how 
Google solves all of the problems you'd perhaps consider using this package
for at scale. 

One downside to Google's approach is that *all* of your functions must have
a new first argument, but after clearing that hurdle everything else is much
better.

If you aren't interested in this warning, read on.

### Huhwaht? Why? ###

Every so often, a thread shows up on the
[golang-nuts](https://groups.google.com/d/forum/golang-nuts) asking for some
form of goroutine-local-storage, or some kind of goroutine id, or some kind of
context. There are a few valid use cases for goroutine-local-storage, one of
the most prominent being log line context. One poster was interested in being
able to log an HTTP request context id in every log line in the same goroutine
as the incoming HTTP request, without having to change every library and
function call he was interested in logging.

This would be pretty useful. Provided that you could get some kind of
goroutine-local-storage, you could call
[log.SetOutput](http://golang.org/pkg/log/#SetOutput) with your own logging
writer that checks goroutine-local-storage for some context information and
adds that context to your log lines.

But alas, Andrew Gerrand's typically diplomatic answer to the question of
goroutine-local variables was:

> We wouldn't even be having this discussion if thread local storage wasn't
> useful. But every feature comes at a cost, and in my opinion the cost of
> threadlocals far outweighs their benefits. They're just not a good fit for
> Go.

So, yeah, that makes sense. That's a pretty good reason for why the language
won't support a specific and (relatively) unuseful feature that requires some
runtime changes, just for the sake of a little bit of log improvement.

But does Go require runtime changes?

### How it works ###

Go has pretty fantastic introspective and reflective features, but one thing Go
doesn't give you is any kind of access to the stack pointer, or frame pointer,
or goroutine id, or anything contextual about your current stack. It gives you
access to your list of callers, but only along with program counters, which are
fixed at compile time.

But it does give you the stack.

So, we define 16 special functions and embed base-16 tags into the stack using
the call order of those 16 functions. Then, we can read our tags back out of
the stack looking at the callers list.

We then use these tags as an index into a traditional map for implementing
this library.

### What are people saying? ###

"Wow, that's horrifying."

"This is the most terrible thing I have seen in a very long time."

"Where is it getting a context from? Is this serializing all the requests? 
What the heck is the client being bound to? What are these tags? Why does he 
need callers? Oh god no. No no no."

### Docs ###

Please see the docs at http://godoc.org/github.com/jtolds/gls

### Related ###

If you're okay relying on the string format of the current runtime stacktrace 
including a unique goroutine id (not guaranteed by the spec or anything, but 
very unlikely to change within a Go release), you might be able to squeeze 
out a bit more performance by using this similar library, inspired by some 
code Brad Fitzpatrick wrote for debugging his HTTP/2 library: 
https://github.com/tylerb/gls (in contrast, jtolds/gls doesn't require 
any knowledge of the string format of the runtime stacktrace, which 
probably adds unnecessary overhead).
# html2text

[![Documentation](https://godoc.org/github.com/jaytaylor/html2text?status.svg)](https://godoc.org/github.com/jaytaylor/html2text)
[![Build Status](https://travis-ci.org/jaytaylor/html2text.svg?branch=master)](https://travis-ci.org/jaytaylor/html2text)
[![Report Card](https://goreportcard.com/badge/github.com/jaytaylor/html2text)](https://goreportcard.com/report/github.com/jaytaylor/html2text)

### Converts HTML into text


## Introduction

html2text is a simple golang package for rendering HTML into plaintext.

There are still lots of improvements to be had, but FWIW this has worked fine for my [basic] HTML-2-text needs.

It requires go 1.x or newer ;)


## Download the package

```bash
go get github.com/jaytaylor/html2text
```

## Example usage

```go
package main

import (
	"fmt"

	"github.com/jaytaylor/html2text"
)

func main() {
	inputHtml := `
          <html>
            <head>
              <title>My Mega Service</title>
              <link rel=\"stylesheet\" href=\"main.css\">
              <style type=\"text/css\">body { color: #fff; }</style>
            </head>
        
            <body>
              <div class="logo">
                <a href="http://mymegaservice.com/"><img src="/logo-image.jpg" alt="Mega Service"/></a>
              </div>
        
              <h1>Welcome to your new account on my service!</h1>
        
              <p>
                  Here is some more information:
        
                  <ul>
                      <li>Link 1: <a href="https://example.com">Example.com</a></li>
                      <li>Link 2: <a href="https://example2.com">Example2.com</a></li>
                      <li>Something else</li>
                  </ul>
              </p>
            </body>
          </html>
	`

	text, err := html2text.FromString(inputHtml)
	if err != nil {
		panic(err)
	}
	fmt.Println(text)
}
```

Output:
```
Mega Service ( http://mymegaservice.com/ )

******************************************
Welcome to your new account on my service!
******************************************

Here is some more information:

* Link 1: Example.com ( https://example.com )
* Link 2: Example2.com ( https://example2.com )
* Something else
```


## Unit-tests

Running the unit-tests is straightforward and standard:

```bash
go test
```


# License

Permissive MIT license.


## Contact

You are more than welcome to open issues and send pull requests if you find a bug or want a new feature.

If you appreciate this library please feel free to drop me a line and tell me!  It's always nice to hear from people who have benefitted from my work.

Email: jay at (my github username).com

Twitter: [@jtaylor](https://twitter.com/jtaylor)

# pq - A pure Go postgres driver for Go's database/sql package

[![Build Status](https://travis-ci.org/lib/pq.png?branch=master)](https://travis-ci.org/lib/pq)

## Install

	go get github.com/lib/pq

## Docs

For detailed documentation and basic usage examples, please see the package
documentation at <http://godoc.org/github.com/lib/pq>.

## Tests

`go test` is used for testing.  A running PostgreSQL server is
required, with the ability to log in.  The default database to connect
to test with is "pqgotest," but it can be overridden using environment
variables.

Example:

	PGHOST=/run/postgresql go test github.com/lib/pq

Optionally, a benchmark suite can be run as part of the tests:

	PGHOST=/run/postgresql go test -bench .

## Features

* SSL
* Handles bad connections for `database/sql`
* Scan `time.Time` correctly (i.e. `timestamp[tz]`, `time[tz]`, `date`)
* Scan binary blobs correctly (i.e. `bytea`)
* Package for `hstore` support
* COPY FROM support
* pq.ParseURL for converting urls to connection strings for sql.Open.
* Many libpq compatible environment variables
* Unix socket support
* Notifications: `LISTEN`/`NOTIFY`
* pgpass support

## Future / Things you can help with

* Better COPY FROM / COPY TO (see discussion in #181)

## Thank you (alphabetical)

Some of these contributors are from the original library `bmizerany/pq.go` whose
code still exists in here.

* Andy Balholm (andybalholm)
* Ben Berkert (benburkert)
* Benjamin Heatwole (bheatwole)
* Bill Mill (llimllib)
* Bjørn Madsen (aeons)
* Blake Gentry (bgentry)
* Brad Fitzpatrick (bradfitz)
* Charlie Melbye (cmelbye)
* Chris Bandy (cbandy)
* Chris Gilling (cgilling)
* Chris Walsh (cwds)
* Dan Sosedoff (sosedoff)
* Daniel Farina (fdr)
* Eric Chlebek (echlebek)
* Eric Garrido (minusnine)
* Eric Urban (hydrogen18)
* Everyone at The Go Team
* Evan Shaw (edsrzf)
* Ewan Chou (coocood)
* Fazal Majid (fazalmajid)
* Federico Romero (federomero)
* Fumin (fumin)
* Gary Burd (garyburd)
* Heroku (heroku)
* James Pozdena (jpoz)
* Jason McVetta (jmcvetta)
* Jeremy Jay (pbnjay)
* Joakim Sernbrant (serbaut)
* John Gallagher (jgallagher)
* Jonathan Rudenberg (titanous)
* Joël Stemmer (jstemmer)
* Kamil Kisiel (kisielk)
* Kelly Dunn (kellydunn)
* Keith Rarick (kr)
* Kir Shatrov (kirs)
* Lann Martin (lann)
* Maciek Sakrejda (uhoh-itsmaciek)
* Marc Brinkmann (mbr)
* Marko Tiikkaja (johto)
* Matt Newberry (MattNewberry)
* Matt Robenolt (mattrobenolt)
* Martin Olsen (martinolsen)
* Mike Lewis (mikelikespie)
* Nicolas Patry (Narsil)
* Oliver Tonnhofer (olt)
* Patrick Hayes (phayes)
* Paul Hammond (paulhammond)
* Ryan Smith (ryandotsmith)
* Samuel Stauffer (samuel)
* Timothée Peignier (cyberdelia)
* Travis Cline (tmc)
* TruongSinh Tran-Nguyen (truongsinh)
* Yaismel Miranda (ympons)
* notedit (notedit)
# A pure Go MSSQL driver for Go's database/sql package

## Install

    go get github.com/denisenkom/go-mssqldb

## Connection Parameters and DSN

* "server" - host or host\instance (default localhost)
* "port" - used only when there is no instance in server (default 1433)
* "failoverpartner" - host or host\instance (default is no partner). 
* "failoverport" - used only when there is no instance in failoverpartner (default 1433)
* "user id" - enter the SQL Server Authentication user id or the Windows Authentication user id in the DOMAIN\User format. On Windows, if user id is empty or missing Single-Sign-On is used.
* "password"
* "database"
* "connection timeout" - in seconds (default is 30)
* "dial timeout" - in seconds (default is 5)
* "keepAlive" - in seconds; 0 to disable (default is 0)
* "log" - logging flags (default 0/no logging, 63 for full logging)
  *  1 log errors
  *  2 log messages
  *  4 log rows affected
  *  8 trace sql statements
  * 16 log statement parameters
  * 32 log transaction begin/end
* "encrypt"
  * disable - Data send between client and server is not encrypted.
  * false - Data sent between client and server is not encrypted beyond the login packet. (Default)
  * true - Data sent between client and server is encrypted.
* "TrustServerCertificate"
  * false - Server certificate is checked. Default is false if encypt is specified.
  * true - Server certificate is not checked. Default is true if encrypt is not specified. If trust server certificate is true, driver accepts any certificate presented by the server and any host name in that certificate. In this mode, TLS is susceptible to man-in-the-middle attacks. This should be used only for testing.
* "certificate" - The file that contains the public key certificate of the CA that signed the SQL Server certificate. The specified certificate overrides the go platform specific CA certificates.
* "hostNameInCertificate" - Specifies the Common Name (CN) in the server certificate. Default value is the server host.
* "ServerSPN" - The kerberos SPN (Service Principal Name) for the server. Default is MSSQLSvc/host:port.
* "Workstation ID" - The workstation name (default is the host name)
* "app name" - The application name (default is go-mssqldb)
* "ApplicationIntent" - Can be given the value "ReadOnly" to initiate a read-only connection to an Availability Group listener.

The connection string can be specified in one of three formats:

1. ADO: `key=value` pairs separated by `;`. Values may not contain `;`, leading and trailing whitespace is ignored.
     Examples:
	
  * `server=localhost\\SQLExpress;user id=sa;database=master;connection timeout=30`
  * `server=localhost;user id=sa;database=master;connection timeout=30`

2. ODBC: Prefix with `odbc`, `key=value` pairs separated by `;`. Allow `;` by wrapping
    values in `{}`. Examples:
	
  * `odbc:server=localhost\\SQLExpress;user id=sa;database=master;connection timeout=30`
  * `odbc:server=localhost;user id=sa;database=master;connection timeout=30`
  * `odbc:server=localhost;user id=sa;password={foo;bar}` // Value marked with `{}`, password is "foo;bar"
  * `odbc:server=localhost;user id=sa;password={foo{bar}` // Value marked with `{}`, password is "foo{bar"
  * `odbc:server=localhost;user id=sa;password={foobar }` // Value marked with `{}`, password is "foobar "
  * `odbc:server=localhost;user id=sa;password=foo{bar`   // Literal `{`, password is "foo{bar"
  * `odbc:server=localhost;user id=sa;password=foo}bar`   // Literal `}`, password is "foo}bar"
  * `odbc:server=localhost;user id=sa;password={foo{bar}` // Literal `{`, password is "foo{bar"
  * `odbc:server=localhost;user id=sa;password={foo}}bar}` // Escaped `} with `}}`, password is "foo}bar"

3. URL: with `sqlserver` scheme. username and password appears before the host. Any instance appears as
    the first segment in the path. All other options are query parameters. Examples:

  * `sqlserver://username:password@host/instance?param1=value&param2=value`
  * `sqlserver://username:password@host:port?param1=value&param2=value`
  * `sqlserver://sa@localhost/SQLExpress?database=master&connection+timeout=30` // `SQLExpress instance.
  * `sqlserver://sa:mypass@localhost?database=master&connection+timeout=30`     // username=sa, password=mypass.
  * `sqlserver://sa:mypass@localhost:1234?database=master&connection+timeout=30"` // port 1234 on localhost.
  * `sqlserver://sa:my%7Bpass@somehost?connection+timeout=30` // password is "my{pass"

  A string of this format can be constructed using the `URL` type in the `net/url` package.

  ```go
  query := url.Values{}
  query.Add("connection timeout", fmt.Sprintf("%d", connectionTimeout))

  u := &url.URL{
      Scheme:   "sqlserver",
      User:     url.UserPassword(username, password),
      Host:     fmt.Sprintf("%s:%d", hostname, port),
      // Path:  instance, // if connecting to an instance instead of a port
      RawQuery: query.Encode(),
  }

  connectionString := u.String()

  db, err := sql.Open("sqlserver", connectionString)
  // or
  db, err := sql.Open("mssql", connectionString)
  ```

## Statement Parameters

The `sqlserver` driver uses normal MS SQL Server syntax and expects parameters in
the sql query to be in the form of either `@Name` or `@p1` to `@pN` (ordinal position).

```go
db.QueryContext(ctx, `select * from t where ID = @ID;`, sql.Named("ID", 6))
```


For the `mssql` driver, the SQL statement text will be processed and literals will
be replaced by a parameter that matches one of the following:

* ?
* ?nnn
* :nnn
* $nnn

where nnn represents an integer that specifies a 1-indexed positional parameter. Ex:

```go
db.Query("SELECT * FROM t WHERE a = ?3, b = ?2, c = ?1", "x", "y", "z")
```

will expand to roughly

```sql
SELECT * FROM t WHERE a = 'z', b = 'y', c = 'x'
```

## Features

* Can be used with SQL Server 2005 or newer
* Can be used with Microsoft Azure SQL Database
* Can be used on all go supported platforms (e.g. Linux, Mac OS X and Windows)
* Supports new date/time types: date, time, datetime2, datetimeoffset
* Supports string parameters longer than 8000 characters
* Supports encryption using SSL/TLS
* Supports SQL Server and Windows Authentication
* Supports Single-Sign-On on Windows
* Supports connections to AlwaysOn Availability Group listeners, including re-direction to read-only replicas.
* Supports query notifications

## Tests

`go test` is used for testing. A running instance of MSSQL server is required.
Environment variables are used to pass login information.

Example:

    env HOST=localhost SQLUSER=sa SQLPASSWORD=sa DATABASE=test go test

## Known Issues

* SQL Server 2008 and 2008 R2 engine cannot handle login records when SSL encryption is not disabled.
To fix SQL Server 2008 R2 issue, install SQL Server 2008 R2 Service Pack 2.
To fix SQL Server 2008 issue, install Microsoft SQL Server 2008 Service Pack 3 and Cumulative update package 3 for SQL Server 2008 SP3.
More information: http://support.microsoft.com/kb/2653857
# assertions
--
    import "github.com/smartystreets/assertions"

Package assertions contains the implementations for all assertions which are
referenced in goconvey's `convey` package
(github.com/smartystreets/goconvey/convey) and gunit
(github.com/smartystreets/gunit) for use with the So(...) method. They can also
be used in traditional Go test functions and even in applications.

Many of the assertions lean heavily on work done by Aaron Jacobs in his
excellent oglematchers library. (https://github.com/jacobsa/oglematchers) The
ShouldResemble assertion leans heavily on work done by Daniel Jacques in his
very helpful go-render library. (https://github.com/luci/go-render)

## Usage

#### func  GoConveyMode

```go
func GoConveyMode(yes bool)
```
GoConveyMode provides control over JSON serialization of failures. When using
the assertions in this package from the convey package JSON results are very
helpful and can be rendered in a DIFF view. In that case, this function will be
called with a true value to enable the JSON serialization. By default, the
assertions in this package will not serializer a JSON result, making standalone
ussage more convenient.

#### func  ShouldAlmostEqual

```go
func ShouldAlmostEqual(actual interface{}, expected ...interface{}) string
```
ShouldAlmostEqual makes sure that two parameters are close enough to being
equal. The acceptable delta may be specified with a third argument, or a very
small default delta will be used.

#### func  ShouldBeBetween

```go
func ShouldBeBetween(actual interface{}, expected ...interface{}) string
```
ShouldBeBetween receives exactly three parameters: an actual value, a lower
bound, and an upper bound. It ensures that the actual value is between both
bounds (but not equal to either of them).

#### func  ShouldBeBetweenOrEqual

```go
func ShouldBeBetweenOrEqual(actual interface{}, expected ...interface{}) string
```
ShouldBeBetweenOrEqual receives exactly three parameters: an actual value, a
lower bound, and an upper bound. It ensures that the actual value is between
both bounds or equal to one of them.

#### func  ShouldBeBlank

```go
func ShouldBeBlank(actual interface{}, expected ...interface{}) string
```
ShouldBeBlank receives exactly 1 string parameter and ensures that it is equal
to "".

#### func  ShouldBeChronological

```go
func ShouldBeChronological(actual interface{}, expected ...interface{}) string
```
ShouldBeChronological receives a []time.Time slice and asserts that the are in
chronological order starting with the first time.Time as the earliest.

#### func  ShouldBeEmpty

```go
func ShouldBeEmpty(actual interface{}, expected ...interface{}) string
```
ShouldBeEmpty receives a single parameter (actual) and determines whether or not
calling len(actual) would return `0`. It obeys the rules specified by the len
function for determining length: http://golang.org/pkg/builtin/#len

#### func  ShouldBeFalse

```go
func ShouldBeFalse(actual interface{}, expected ...interface{}) string
```
ShouldBeFalse receives a single parameter and ensures that it is false.

#### func  ShouldBeGreaterThan

```go
func ShouldBeGreaterThan(actual interface{}, expected ...interface{}) string
```
ShouldBeGreaterThan receives exactly two parameters and ensures that the first
is greater than the second.

#### func  ShouldBeGreaterThanOrEqualTo

```go
func ShouldBeGreaterThanOrEqualTo(actual interface{}, expected ...interface{}) string
```
ShouldBeGreaterThanOrEqualTo receives exactly two parameters and ensures that
the first is greater than or equal to the second.

#### func  ShouldBeIn

```go
func ShouldBeIn(actual interface{}, expected ...interface{}) string
```
ShouldBeIn receives at least 2 parameters. The first is a proposed member of the
collection that is passed in either as the second parameter, or of the
collection that is comprised of all the remaining parameters. This assertion
ensures that the proposed member is in the collection (using ShouldEqual).

#### func  ShouldBeLessThan

```go
func ShouldBeLessThan(actual interface{}, expected ...interface{}) string
```
ShouldBeLessThan receives exactly two parameters and ensures that the first is
less than the second.

#### func  ShouldBeLessThanOrEqualTo

```go
func ShouldBeLessThanOrEqualTo(actual interface{}, expected ...interface{}) string
```
ShouldBeLessThan receives exactly two parameters and ensures that the first is
less than or equal to the second.

#### func  ShouldBeNil

```go
func ShouldBeNil(actual interface{}, expected ...interface{}) string
```
ShouldBeNil receives a single parameter and ensures that it is nil.

#### func  ShouldBeTrue

```go
func ShouldBeTrue(actual interface{}, expected ...interface{}) string
```
ShouldBeTrue receives a single parameter and ensures that it is true.

#### func  ShouldBeZeroValue

```go
func ShouldBeZeroValue(actual interface{}, expected ...interface{}) string
```
ShouldBeZeroValue receives a single parameter and ensures that it is the Go
equivalent of the default value, or "zero" value.

#### func  ShouldContain

```go
func ShouldContain(actual interface{}, expected ...interface{}) string
```
ShouldContain receives exactly two parameters. The first is a slice and the
second is a proposed member. Membership is determined using ShouldEqual.

#### func  ShouldContainKey

```go
func ShouldContainKey(actual interface{}, expected ...interface{}) string
```
ShouldContainKey receives exactly two parameters. The first is a map and the
second is a proposed key. Keys are compared with a simple '=='.

#### func  ShouldContainSubstring

```go
func ShouldContainSubstring(actual interface{}, expected ...interface{}) string
```
ShouldContainSubstring receives exactly 2 string parameters and ensures that the
first contains the second as a substring.

#### func  ShouldEndWith

```go
func ShouldEndWith(actual interface{}, expected ...interface{}) string
```
ShouldEndWith receives exactly 2 string parameters and ensures that the first
ends with the second.

#### func  ShouldEqual

```go
func ShouldEqual(actual interface{}, expected ...interface{}) string
```
ShouldEqual receives exactly two parameters and does an equality check.

#### func  ShouldEqualTrimSpace

```go
func ShouldEqualTrimSpace(actual interface{}, expected ...interface{}) string
```
ShouldEqualTrimSpace receives exactly 2 string parameters and ensures that the
first is equal to the second after removing all leading and trailing whitespace
using strings.TrimSpace(first).

#### func  ShouldEqualWithout

```go
func ShouldEqualWithout(actual interface{}, expected ...interface{}) string
```
ShouldEqualWithout receives exactly 3 string parameters and ensures that the
first is equal to the second after removing all instances of the third from the
first using strings.Replace(first, third, "", -1).

#### func  ShouldHappenAfter

```go
func ShouldHappenAfter(actual interface{}, expected ...interface{}) string
```
ShouldHappenAfter receives exactly 2 time.Time arguments and asserts that the
first happens after the second.

#### func  ShouldHappenBefore

```go
func ShouldHappenBefore(actual interface{}, expected ...interface{}) string
```
ShouldHappenBefore receives exactly 2 time.Time arguments and asserts that the
first happens before the second.

#### func  ShouldHappenBetween

```go
func ShouldHappenBetween(actual interface{}, expected ...interface{}) string
```
ShouldHappenBetween receives exactly 3 time.Time arguments and asserts that the
first happens between (not on) the second and third.

#### func  ShouldHappenOnOrAfter

```go
func ShouldHappenOnOrAfter(actual interface{}, expected ...interface{}) string
```
ShouldHappenOnOrAfter receives exactly 2 time.Time arguments and asserts that
the first happens on or after the second.

#### func  ShouldHappenOnOrBefore

```go
func ShouldHappenOnOrBefore(actual interface{}, expected ...interface{}) string
```
ShouldHappenOnOrBefore receives exactly 2 time.Time arguments and asserts that
the first happens on or before the second.

#### func  ShouldHappenOnOrBetween

```go
func ShouldHappenOnOrBetween(actual interface{}, expected ...interface{}) string
```
ShouldHappenOnOrBetween receives exactly 3 time.Time arguments and asserts that
the first happens between or on the second and third.

#### func  ShouldHappenWithin

```go
func ShouldHappenWithin(actual interface{}, expected ...interface{}) string
```
ShouldHappenWithin receives a time.Time, a time.Duration, and a time.Time (3
arguments) and asserts that the first time.Time happens within or on the
duration specified relative to the other time.Time.

#### func  ShouldHaveLength

```go
func ShouldHaveLength(actual interface{}, expected ...interface{}) string
```
ShouldHaveLength receives 2 parameters. The first is a collection to check the
length of, the second being the expected length. It obeys the rules specified by
the len function for determining length: http://golang.org/pkg/builtin/#len

#### func  ShouldHaveSameTypeAs

```go
func ShouldHaveSameTypeAs(actual interface{}, expected ...interface{}) string
```
ShouldHaveSameTypeAs receives exactly two parameters and compares their
underlying types for equality.

#### func  ShouldImplement

```go
func ShouldImplement(actual interface{}, expectedList ...interface{}) string
```
ShouldImplement receives exactly two parameters and ensures that the first
implements the interface type of the second.

#### func  ShouldNotAlmostEqual

```go
func ShouldNotAlmostEqual(actual interface{}, expected ...interface{}) string
```
ShouldNotAlmostEqual is the inverse of ShouldAlmostEqual

#### func  ShouldNotBeBetween

```go
func ShouldNotBeBetween(actual interface{}, expected ...interface{}) string
```
ShouldNotBeBetween receives exactly three parameters: an actual value, a lower
bound, and an upper bound. It ensures that the actual value is NOT between both
bounds.

#### func  ShouldNotBeBetweenOrEqual

```go
func ShouldNotBeBetweenOrEqual(actual interface{}, expected ...interface{}) string
```
ShouldNotBeBetweenOrEqual receives exactly three parameters: an actual value, a
lower bound, and an upper bound. It ensures that the actual value is nopt
between the bounds nor equal to either of them.

#### func  ShouldNotBeBlank

```go
func ShouldNotBeBlank(actual interface{}, expected ...interface{}) string
```
ShouldNotBeBlank receives exactly 1 string parameter and ensures that it is
equal to "".

#### func  ShouldNotBeEmpty

```go
func ShouldNotBeEmpty(actual interface{}, expected ...interface{}) string
```
ShouldNotBeEmpty receives a single parameter (actual) and determines whether or
not calling len(actual) would return a value greater than zero. It obeys the
rules specified by the `len` function for determining length:
http://golang.org/pkg/builtin/#len

#### func  ShouldNotBeIn

```go
func ShouldNotBeIn(actual interface{}, expected ...interface{}) string
```
ShouldNotBeIn receives at least 2 parameters. The first is a proposed member of
the collection that is passed in either as the second parameter, or of the
collection that is comprised of all the remaining parameters. This assertion
ensures that the proposed member is NOT in the collection (using ShouldEqual).

#### func  ShouldNotBeNil

```go
func ShouldNotBeNil(actual interface{}, expected ...interface{}) string
```
ShouldNotBeNil receives a single parameter and ensures that it is not nil.

#### func  ShouldNotContain

```go
func ShouldNotContain(actual interface{}, expected ...interface{}) string
```
ShouldNotContain receives exactly two parameters. The first is a slice and the
second is a proposed member. Membership is determinied using ShouldEqual.

#### func  ShouldNotContainKey

```go
func ShouldNotContainKey(actual interface{}, expected ...interface{}) string
```
ShouldNotContainKey receives exactly two parameters. The first is a map and the
second is a proposed absent key. Keys are compared with a simple '=='.

#### func  ShouldNotContainSubstring

```go
func ShouldNotContainSubstring(actual interface{}, expected ...interface{}) string
```
ShouldNotContainSubstring receives exactly 2 string parameters and ensures that
the first does NOT contain the second as a substring.

#### func  ShouldNotEndWith

```go
func ShouldNotEndWith(actual interface{}, expected ...interface{}) string
```
ShouldEndWith receives exactly 2 string parameters and ensures that the first
does not end with the second.

#### func  ShouldNotEqual

```go
func ShouldNotEqual(actual interface{}, expected ...interface{}) string
```
ShouldNotEqual receives exactly two parameters and does an inequality check.

#### func  ShouldNotHappenOnOrBetween

```go
func ShouldNotHappenOnOrBetween(actual interface{}, expected ...interface{}) string
```
ShouldNotHappenOnOrBetween receives exactly 3 time.Time arguments and asserts
that the first does NOT happen between or on the second or third.

#### func  ShouldNotHappenWithin

```go
func ShouldNotHappenWithin(actual interface{}, expected ...interface{}) string
```
ShouldNotHappenWithin receives a time.Time, a time.Duration, and a time.Time (3
arguments) and asserts that the first time.Time does NOT happen within or on the
duration specified relative to the other time.Time.

#### func  ShouldNotHaveSameTypeAs

```go
func ShouldNotHaveSameTypeAs(actual interface{}, expected ...interface{}) string
```
ShouldNotHaveSameTypeAs receives exactly two parameters and compares their
underlying types for inequality.

#### func  ShouldNotImplement

```go
func ShouldNotImplement(actual interface{}, expectedList ...interface{}) string
```
ShouldNotImplement receives exactly two parameters and ensures that the first
does NOT implement the interface type of the second.

#### func  ShouldNotPanic

```go
func ShouldNotPanic(actual interface{}, expected ...interface{}) (message string)
```
ShouldNotPanic receives a void, niladic function and expects to execute the
function without any panic.

#### func  ShouldNotPanicWith

```go
func ShouldNotPanicWith(actual interface{}, expected ...interface{}) (message string)
```
ShouldNotPanicWith receives a void, niladic function and expects to recover a
panic whose content differs from the second argument.

#### func  ShouldNotPointTo

```go
func ShouldNotPointTo(actual interface{}, expected ...interface{}) string
```
ShouldNotPointTo receives exactly two parameters and checks to see that they
point to different addresess.

#### func  ShouldNotResemble

```go
func ShouldNotResemble(actual interface{}, expected ...interface{}) string
```
ShouldNotResemble receives exactly two parameters and does an inverse deep equal
check (see reflect.DeepEqual)

#### func  ShouldNotStartWith

```go
func ShouldNotStartWith(actual interface{}, expected ...interface{}) string
```
ShouldNotStartWith receives exactly 2 string parameters and ensures that the
first does not start with the second.

#### func  ShouldPanic

```go
func ShouldPanic(actual interface{}, expected ...interface{}) (message string)
```
ShouldPanic receives a void, niladic function and expects to recover a panic.

#### func  ShouldPanicWith

```go
func ShouldPanicWith(actual interface{}, expected ...interface{}) (message string)
```
ShouldPanicWith receives a void, niladic function and expects to recover a panic
with the second argument as the content.

#### func  ShouldPointTo

```go
func ShouldPointTo(actual interface{}, expected ...interface{}) string
```
ShouldPointTo receives exactly two parameters and checks to see that they point
to the same address.

#### func  ShouldResemble

```go
func ShouldResemble(actual interface{}, expected ...interface{}) string
```
ShouldResemble receives exactly two parameters and does a deep equal check (see
reflect.DeepEqual)

#### func  ShouldStartWith

```go
func ShouldStartWith(actual interface{}, expected ...interface{}) string
```
ShouldStartWith receives exactly 2 string parameters and ensures that the first
starts with the second.

#### func  So

```go
func So(actual interface{}, assert assertion, expected ...interface{}) (bool, string)
```
So is a convenience function (as opposed to an inconvenience function?) for
running assertions on arbitrary arguments in any context, be it for testing or
even application logging. It allows you to perform assertion-like behavior (and
get nicely formatted messages detailing discrepancies) but without the program
blowing up or panicking. All that is required is to import this package and call
`So` with one of the assertions exported by this package as the second
parameter. The first return parameter is a boolean indicating if the assertion
was true. The second return parameter is the well-formatted message showing why
an assertion was incorrect, or blank if the assertion was correct.

Example:

    if ok, message := So(x, ShouldBeGreaterThan, y); !ok {
         log.Println(message)
    }

#### type Assertion

```go
type Assertion struct {
}
```


#### func  New

```go
func New(t testingT) *Assertion
```
New swallows the *testing.T struct and prints failed assertions using t.Error.
Example: assertions.New(t).So(1, should.Equal, 1)

#### func (*Assertion) Failed

```go
func (this *Assertion) Failed() bool
```
Failed reports whether any calls to So (on this Assertion instance) have failed.

#### func (*Assertion) So

```go
func (this *Assertion) So(actual interface{}, assert assertion, expected ...interface{}) bool
```
So calls the standalone So function and additionally, calls t.Error in failure
scenarios.

#### type FailureView

```go
type FailureView struct {
	Message  string `json:"Message"`
	Expected string `json:"Expected"`
	Actual   string `json:"Actual"`
}
```

This struct is also declared in
github.com/smartystreets/goconvey/convey/reporting. The json struct tags should
be equal in both declarations.

#### type Serializer

```go
type Serializer interface {
	// contains filtered or unexported methods
}
```
[![GoDoc](https://godoc.org/github.com/smartystreets/assertions/internal/oglematchers?status.svg)](https://godoc.org/github.com/smartystreets/assertions/internal/oglematchers)

`oglematchers` is a package for the Go programming language containing a set of
matchers, useful in a testing or mocking framework, inspired by and mostly
compatible with [Google Test][googletest] for C++ and
[Google JS Test][google-js-test]. The package is used by the
[ogletest][ogletest] testing framework and [oglemock][oglemock] mocking
framework, which may be more directly useful to you, but can be generically used
elsewhere as well.

A "matcher" is simply an object with a `Matches` method defining a set of golang
values matched by the matcher, and a `Description` method describing that set.
For example, here are some matchers:

```go
// Numbers
Equals(17.13)
LessThan(19)

// Strings
Equals("taco")
HasSubstr("burrito")
MatchesRegex("t.*o")

// Combining matchers
AnyOf(LessThan(17), GreaterThan(19))
```

There are lots more; see [here][reference] for a reference. You can also add
your own simply by implementing the `oglematchers.Matcher` interface.


Installation
------------

First, make sure you have installed Go 1.0.2 or newer. See
[here][golang-install] for instructions.

Use the following command to install `oglematchers` and keep it up to date:

    go get -u github.com/smartystreets/assertions/internal/oglematchers


Documentation
-------------

See [here][reference] for documentation. Alternatively, you can install the
package and then use `godoc`:

    godoc github.com/smartystreets/assertions/internal/oglematchers


[reference]: http://godoc.org/github.com/smartystreets/assertions/internal/oglematchers
[golang-install]: http://golang.org/doc/install.html
[googletest]: http://code.google.com/p/googletest/
[google-js-test]: http://code.google.com/p/google-js-test/
[ogletest]: http://github.com/smartystreets/assertions/internal/ogletest
[oglemock]: http://github.com/smartystreets/assertions/internal/oglemock
# otp: One Time Password utilities Go / Golang

[![GoDoc](https://godoc.org/github.com/pquerna/otp?status.svg)](https://godoc.org/github.com/pquerna/otp) [![Build Status](https://travis-ci.org/pquerna/otp.svg?branch=master)](https://travis-ci.org/pquerna/otp)

# Why One Time Passwords?

One Time Passwords (OTPs) are an mechanism to  improve security over passwords alone. When a Time-based OTP (TOTP) is stored on a user's phone, and combined with something the user knows (Password), you have an easy on-ramp to [Multi-factor authentication](http://en.wikipedia.org/wiki/Multi-factor_authentication) without adding a dependency on a SMS provider.  This Password and TOTP combination is used by many popular websites including Google, Github, Facebook, Salesforce and many others.

The `otp` library enables you to easily add TOTPs to your own application, increasing your user's security against mass-password breaches and malware.

Because TOTP is standardized and widely deployed, there are many [mobile clients and software implementations](http://en.wikipedia.org/wiki/Time-based_One-time_Password_Algorithm#Client_implementations).

## `otp` Supports:

* Generating QR Code images for easy user enrollment.
* Time-based One-time Password Algorithm (TOTP) (RFC 6238): Time based OTP, the most commonly used method.
* HMAC-based One-time Password Algorithm (HOTP) (RFC 4226): Counter based OTP, which TOTP is based upon.
* Generation and Validation of codes for either algorithm.

## Implementing TOTP in your application:

### User Enrollment

For an example of a working enrollment work flow, [Github has documented theirs](https://help.github.com/articles/configuring-two-factor-authentication-via-a-totp-mobile-app/
),  but the basics are:

1. Generate new TOTP Key for a User. `key,_ := totp.Generate(...)`.
1. Display the Key's Secret and QR-Code for the User. `key.Secret()` and `key.Image(...)`.
1. Test that the user can successfully use their TOTP. `totp.Validate(...)`.
1. Store TOTP Secret for the User in your backend. `key.Secret()`
1. Provide the user with "recovery codes". (See Recovery Codes bellow)

### Code Generation

* In either TOTP or HOTP cases, use the `GenerateCode` function and a counter or
  `time.Time` struct to generate a valid code compatible with most implementations.
* For uncommon or custom settings, or to catch unlikely errors, use `GenerateCodeCustom`
  in either module.

### Validation

1. Prompt and validate User's password as normal.
1. If the user has TOTP enabled, prompt for TOTP passcode.
1. Retrieve the User's TOTP Secret from your backend.
1. Validate the user's passcode. `totp.Validate(...)`


### Recovery Codes

When a user loses access to their TOTP device, they would no longer have access to their account.  Because TOTPs are often configured on mobile devices that can be lost, stolen or damaged, this is a common problem. For this reason many providers give their users "backup codes" or "recovery codes".  These are a set of one time use codes that can be used instead of the TOTP.  These can simply be randomly generated strings that you store in your backend.  [Github's documentation provides an overview of the user experience](
https://help.github.com/articles/downloading-your-two-factor-authentication-recovery-codes/).


## Improvements, bugs, adding feature, etc:

Please [open issues in Github](https://github.com/pquerna/otp/issues) for ideas, bugs, and general thoughts.  Pull requests are of course preferred :)

## License

`otp` is licensed under the [Apache License, Version 2.0](./LICENSE)
Paginater [![Build Status](https://travis-ci.org/Unknwon/paginater.svg?branch=master)](https://travis-ci.org/Unknwon/paginater)
=========

Package paginater is a helper module for custom pagination calculation.

## Installation

	go get github.com/Unknwon/paginater

## Getting Started

The following code shows an example of how to use paginater:

```go
package main

import "github.com/Unknwon/paginater"

func main() {
	// Arguments:
	// - Total number of rows
	// - Number of rows in one page
	// - Current page number 
	// - Number of page links to be displayed
	p := paginater.New(45, 10, 3, 3)
	
	// Then use p as a template object named "Page" in "demo.html"
	// ...
}
```

`demo.html`

```html
{{if not .Page.IsFirst}}[First](1){{end}}
{{if .Page.HasPrevious}}[Previous]({{.Page.Previous}}){{end}}

{{range .Page.Pages}}
	{{if eq .Num -1}}
	...
	{{else}}
	{{.Num}}{{if .IsCurrent}}(current){{end}}
	{{end}}
{{end}}

{{if .Page.HasNext}}[Next]({{.Page.Next}}){{end}}
{{if not .Page.IsLast}}[Last]({{.Page.TotalPages}}){{end}}
```

Possible output:

```
[First](1) [Previous](2) ... 2 3(current) 4 ... [Next](4) [Last](5)
```

As you may guess, if the `Page` value is `-1`, you should print `...` in the HTML as common practice.

## Getting Help

- [API Documentation](https://gowalker.org/github.com/Unknwon/paginater)
- [File An Issue](https://github.com/Unknwon/paginater/issues/new)

## License

This project is under Apache v2 License. See the [LICENSE](LICENSE) file for the full license text.i18n
====

Package i18n is for app Internationalization and Localization.

## Introduction

This package provides multiple-language options to improve user experience. Sites like [Go Walker](http://gowalker.org) and [gogs.io](http://gogs.io) are using this module to implement Chinese and English user interfaces.

You can use following command to install this module:

    go get github.com/Unknwon/i18n

## Usage

First of all, you have to import this package:

```go
import "github.com/Unknwon/i18n"
```

The format of locale files is very like INI format configuration file, which is basically key-value pairs. But this module has some improvements. Every language corresponding to a locale file, for example, under `conf/locale` folder of [gogsweb](https://github.com/gogits/gogsweb/tree/master/conf/locale), there are two files called `locale_en-US.ini` and `locale_zh-CN.ini`.

The name and extensions of locale files can be anything, but we strongly recommend you to follow the style of gogsweb.

## Minimal example

Here are two simplest locale file examples:

File `locale_en-US.ini`:

```ini
hi = hello, %s
bye = goodbye
```

File `locale_zh-CN.ini`:

```ini
hi = 您好，%s
bye = 再见
```

### Do Translation

There are two ways to do translation depends on which way is the best fit for your application or framework.

Directly use package function to translate:

```go
i18n.Tr("en-US", "hi", "Unknwon")
i18n.Tr("en-US", "bye")
```

Or create a struct and embed it:

```go
type MyController struct{
    // ...other fields
    i18n.Locale
}

//...

func ... {
    c := &MyController{
        Locale: i18n.Locale{"en-US"},
    }
    _ = c.Tr("hi", "Unknwon")
    _ = c.Tr("bye")
}
```

Code above will produce correspondingly:

- English `en-US`：`hello, Unknwon`, `goodbye`
- Chinese `zh-CN`：`您好，Unknwon`, `再见`

## Section

For different pages, one key may map to different values. Therefore, i18n module also uses the section feature of INI format configuration to achieve section.

For example, the key name is `about`, and we want to show `About` in the home page and `About Us` in about page. Then you can do following:

Content in locale file:

```ini
about = About

[about]
about = About Us
```

Get `about` in home page:

```go
i18n.Tr("en-US", "about")
```

Get `about` in about page:

```go
i18n.Tr("en-US", "about.about")
```

### Ambiguity

Because dot `.` is sign of section in both [INI parser](https://github.com/go-ini/ini) and locale files, so when your key name contains `.` will cause ambiguity. At this point, you just need to add one more `.` in front of the key.

For example, the key name is `about.`, then we can use:

```go
i18n.Tr("en-US", ".about.")
```

to get expect result.

## Helper tool

Module i18n provides a command line helper tool beei18n for simplify steps of your development. You can install it as follows:

	go get github.com/Unknwon/i18n/ui18n

### Sync locale files

Command `sync` allows you use a exist local file as the template to create or sync other locale files:

	ui18n sync srouce_file.ini other1.ini other2.ini

This command can operate 1 or more files in one command.

## More information

If the key does not exist, then i18n will return the key string to caller. For instance, when key name is `hi` and it does not exist in locale file, simply return `hi` as output.
Compression and Archive Extensions
==================================

[![Go Walker](http://gowalker.org/api/v1/badge)](http://gowalker.org/github.com/Unknwon/cae)

[中文文档](README_ZH.md)

Package cae implements PHP-like Compression and Archive Extensions.

But this package has some modifications depends on Go-style.

Reference: [PHP:Compression and Archive Extensions](http://www.php.net/manual/en/refs.compression.php).

Code Convention: based on [Go Code Convention](https://github.com/Unknwon/go-code-convention).

### Implementations

Package `zip`([Go Walker](http://gowalker.org/github.com/Unknwon/cae/zip)) and `tz`([Go Walker](http://gowalker.org/github.com/Unknwon/cae/tz)) both enable you to transparently read or write ZIP/TAR.GZ compressed archives and the files inside them.

- Features:
	- Add file or directory from everywhere to archive, no one-to-one limitation.
	- Extract part of entries, not all at once. 
	- Stream data directly into `io.Writer` without any file system storage.

### Test cases and Coverage

All subpackages use [GoConvey](http://goconvey.co/) to write test cases, and coverage is more than 80 percent.

### Use cases

- [Gogs](https://github.com/gogits/gogs): self hosted Git service in the Go Programming Language.
- [GoBlog](https://github.com/fuxiaohei/GoBlog): personal blogging application.
- [GoBuild](https://github.com/shxsun/gobuild/): online Go cross-platform compilation and download service.

## License

This project is under Apache v2 License. See the [LICENSE](LICENSE) file for the full license text.压缩与打包扩展
=============

[![Go Walker](http://gowalker.org/api/v1/badge)](http://gowalker.org/github.com/Unknwon/cae)

包 cae 实现了 PHP 风格的压缩与打包扩展。

但本包依据 Go 语言的风格进行了一些修改。

引用：[PHP:Compression and Archive Extensions](http://www.php.net/manual/en/refs.compression.php)

编码规范：基于 [Go 编码规范](https://github.com/Unknwon/go-code-convention)

### 实现

包 `zip`([Go Walker](http://gowalker.org/github.com/Unknwon/cae/zip)) 和 `tz`([Go Walker](http://gowalker.org/github.com/Unknwon/cae/tz)) 都允许你轻易的读取或写入 ZIP/TAR.GZ 压缩档案和其内部文件。

- 特性：
	- 将任意位置的文件或目录加入档案，没有一对一的操作限制。
	- 只解压部分文件，而非一次性解压全部。 
	- 将数据以流的形式直接写入 `io.Writer` 而不需经过文件系统的存储。

### 测试用例与覆盖率

所有子包均采用 [GoConvey](http://goconvey.co/) 来书写测试用例，覆盖率均超过 80%。

## 授权许可

本项目采用 Apache v2 开源授权许可证，完整的授权说明已放置在 [LICENSE](LICENSE) 文件中。Common Functions
================

[![Build Status](https://travis-ci.org/Unknwon/com.svg)](https://travis-ci.org/Unknwon/com) [![Go Walker](http://gowalker.org/api/v1/badge)](http://gowalker.org/github.com/Unknwon/com)

This is an open source project for commonly used functions for the Go programming language.

This package need >= **go 1.2**

Code Convention: based on [Go Code Convention](https://github.com/Unknwon/go-code-convention).

## Contribute

Your contribute is welcome, but you have to check following steps after you added some functions and commit them:

1. Make sure you wrote user-friendly comments for **all functions** .
2. Make sure you wrote test cases with any possible condition for **all functions** in file `*_test.go`.
3. Make sure you wrote benchmarks for **all functions** in file `*_test.go`.
4. Make sure you wrote useful examples for **all functions** in file `example_test.go`.
5. Make sure you ran `go test` and got **PASS** .
sanitized_anchor_name
=====================

[![Build Status](https://travis-ci.org/shurcooL/sanitized_anchor_name.svg?branch=master)](https://travis-ci.org/shurcooL/sanitized_anchor_name) [![GoDoc](https://godoc.org/github.com/shurcooL/sanitized_anchor_name?status.svg)](https://godoc.org/github.com/shurcooL/sanitized_anchor_name)

Package sanitized_anchor_name provides a func to create sanitized anchor names.

Its logic can be reused by multiple packages to create interoperable anchor names and links to those anchors.

At this time, it does not try to ensure that generated anchor names are unique, that responsibility falls on the caller.

Installation
------------

```bash
go get -u github.com/shurcooL/sanitized_anchor_name
```

Example
-------

```Go
anchorName := sanitized_anchor_name.Create("This is a header")

fmt.Println(anchorName)

// Output:
// this-is-a-header
```

License
-------

-	[MIT License](LICENSE)
# session [![Build Status](https://travis-ci.org/go-macaron/session.svg?branch=master)](https://travis-ci.org/go-macaron/session)

Middleware session provides session management for [Macaron](https://github.com/go-macaron/macaron). It can use many session providers, including memory, file, Redis, Memcache, PostgreSQL, MySQL, Couchbase, Ledis and Nodb.

### Installation

	go get github.com/go-macaron/session
	
## Getting Help

- [API Reference](https://gowalker.org/github.com/go-macaron/session)
- [Documentation](https://go-macaron.com/docs/middlewares/session)

## Credits

This package is a modified version of [beego/session](https://github.com/astaxie/beego/tree/master/session).

## License

This project is under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for the full license text.# i18n [![Build Status](https://travis-ci.org/go-macaron/i18n.svg?branch=master)](https://travis-ci.org/go-macaron/i18n) [![](http://gocover.io/_badge/github.com/go-macaron/i18n)](http://gocover.io/github.com/go-macaron/i18n)

Middleware i18n provides app Internationalization and Localization for [Macaron](https://github.com/go-macaron/macaron).

### Installation

	go get github.com/go-macaron/i18n
	
## Getting Help

- [API Reference](https://gowalker.org/github.com/go-macaron/i18n)
- [Documentation](http://go-macaron.com/docs/middlewares/i18n)

## License

This project is under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for the full license text.# inject [![Build Status](https://travis-ci.org/go-macaron/inject.svg?branch=master)](https://travis-ci.org/go-macaron/inject) [![](http://gocover.io/_badge/github.com/go-macaron/inject)](http://gocover.io/github.com/go-macaron/inject)

Package inject provides utilities for mapping and injecting dependencies in various ways.

**This a modified version of [codegangsta/inject](https://github.com/codegangsta/inject) for special purpose of Macaron**

**Please use the original version if you need dependency injection feature**

## License

This project is under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for the full license text.# cache [![Build Status](https://travis-ci.org/go-macaron/cache.svg?branch=master)](https://travis-ci.org/go-macaron/cache) [![](http://gocover.io/_badge/github.com/go-macaron/cache)](http://gocover.io/github.com/go-macaron/cache)

Middleware cache provides cache management for [Macaron](https://github.com/go-macaron/macaron). It can use many cache adapters, including memory, file, Redis, Memcache, PostgreSQL, MySQL, Ledis and Nodb.

### Installation

	go get github.com/go-macaron/cache

## Getting Help

- [API Reference](https://gowalker.org/github.com/go-macaron/cache)
- [Documentation](http://go-macaron.com/docs/middlewares/cache)

## Credits

This package is a modified version of [beego/cache](https://github.com/astaxie/beego/tree/master/cache).

## License

This project is under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for the full license text.# gzip [![Build Status](https://travis-ci.org/go-macaron/gzip.svg?branch=master)](https://travis-ci.org/go-macaron/gzip) [![](http://gocover.io/_badge/github.com/go-macaron/gzip)](http://gocover.io/github.com/go-macaron/gzip)

Middleware gzip provides compress to responses for [Macaron](https://github.com/go-macaron/macaron).

### Installation

	go get github.com/go-macaron/gzip

## Getting Help

- [API Reference](https://gowalker.org/github.com/go-macaron/gzip)
- [Documentation](http://go-macaron.com/docs/middlewares/gzip)

## Credits

This package is a modified version of [martini-contrib/gzip](https://github.com/martini-contrib/gzip).

## License

This project is under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for the full license text.# binding [![Build Status](https://travis-ci.org/go-macaron/binding.svg?branch=master)](https://travis-ci.org/go-macaron/binding) [![Sourcegraph](https://sourcegraph.com/github.com/go-macaron/binding/-/badge.svg)](https://sourcegraph.com/github.com/go-macaron/binding?badge)

Middleware binding provides request data binding and validation for [Macaron](https://github.com/go-macaron/macaron).

### Installation

	go get github.com/go-macaron/binding
	
## Getting Help

- [API Reference](https://gowalker.org/github.com/go-macaron/binding)
- [Documentation](http://go-macaron.com/docs/middlewares/binding)

## Credits

This package is a modified version of [martini-contrib/binding](https://github.com/martini-contrib/binding).

## License

This project is under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for the full license text.# csrf [![Build Status](https://travis-ci.org/go-macaron/csrf.svg?branch=master)](https://travis-ci.org/go-macaron/csrf) [![](http://gocover.io/_badge/github.com/go-macaron/csrf)](http://gocover.io/github.com/go-macaron/csrf)

Middleware csrf generates and validates CSRF tokens for [Macaron](https://github.com/go-macaron/macaron).

[API Reference](https://gowalker.org/github.com/go-macaron/csrf)

### Installation

	go get github.com/go-macaron/csrf
	
## Getting Help

- [API Reference](https://gowalker.org/github.com/go-macaron/csrf)
- [Documentation](http://go-macaron.com/docs/middlewares/csrf)

## License

This project is under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for the full license text.toolbox
=======

Middleware toolbox provides health chcek, pprof, profile and statistic services for [Macaron](https://github.com/go-macaron/macaron).

[API Reference](https://gowalker.org/github.com/go-macaron/toolbox)

### Installation

	go get github.com/go-macaron/toolbox
	
## Usage

```go
// main.go
import (
	"gopkg.in/macaron.v1"
	"github.com/go-macaron/toolbox"
)

func main() {
  	m := macaron.Classic()
  	m.Use(toolbox.Toolboxer(m))
	m.Run()
}
```

Open your browser and visit `http://localhost:4000/debug` to see the effects.

## Options

`toolbox.Toolboxer` comes with a variety of configuration options:

```go
type dummyChecker struct {
}

func (dc *dummyChecker) Desc() string {
	return "Dummy checker"
}

func (dc *dummyChecker) Check() error {
	return nil
}

// ...
m.Use(toolbox.Toolboxer(m, toolbox.Options{
	URLPrefix:			"/debug",			// URL prefix for toolbox dashboard.
	HealthCheckURL:		"/healthcheck", 	// URL for health check request.
	HealthCheckers: []HealthChecker{
		new(dummyChecker),
	},										// Health checkers.
	HealthCheckFuncs: []*toolbox.HealthCheckFuncDesc{
		&toolbox.HealthCheckFuncDesc{
			Desc: "Database connection",
			Func: func() error { return "OK" },
		},
	},										// Health check functions.
	PprofURLPrefix:		"/debug/pprof/", 	// URL prefix of pprof.
	ProfileURLPrefix:	"/debug/profile/", 	// URL prefix of profile.
	ProfilePath:		"profile", 			// Path store profile files.
}))
// ...
```

## Route Statistic

Toolbox also comes with a route call statistic functionality:

```go
import (
	"os"
	"time"
	//...
	"github.com/go-macaron/toolbox"
)

func main() {
	//...
	m.Get("/", func(t toolbox.Toolbox) {
		start := time.Now()
		
		// Other operations.
		
		t.AddStatistics("GET", "/", time.Since(start))
	})
	
	m.Get("/dump", func(t toolbox.Toolbox) {
		t.GetMap(os.Stdout)
	})
}
```

Output take from test:

```
+---------------------------------------------------+------------+------------------+------------------+------------------+------------------+------------------+
| Request URL                                       | Method     | Times            | Total Used(s)    | Max Used(μs)     | Min Used(μs)     | Avg Used(μs)     |
+---------------------------------------------------+------------+------------------+------------------+------------------+------------------+------------------+
| /api/user                                         | POST       |                2 |         0.000122 |       120.000000 |         2.000000 |        61.000000 |
| /api/user                                         | GET        |                1 |         0.000013 |        13.000000 |        13.000000 |        13.000000 |
| /api/user                                         | DELETE     |                1 |         0.000001 |         1.400000 |         1.400000 |         1.400000 |
| /api/admin                                        | POST       |                1 |         0.000014 |        14.000000 |        14.000000 |        14.000000 |
| /api/user/unknwon                                 | POST       |                1 |         0.000012 |        12.000000 |        12.000000 |        12.000000 |
+---------------------------------------------------+------------+------------------+------------------+------------------+------------------+------------------+
```

## License

This project is under Apache v2 License. See the [LICENSE](LICENSE) file for the full license text.# captcha [![Build Status](https://travis-ci.org/go-macaron/captcha.svg?branch=master)](https://travis-ci.org/go-macaron/captcha)

Middleware captcha provides captcha service for [Macaron](https://github.com/go-macaron/macaron).

### Installation

	go get github.com/go-macaron/captcha

## Getting Help

- [API Reference](https://gowalker.org/github.com/go-macaron/captcha)
- [Documentation](http://go-macaron.com/docs/middlewares/captcha)

## License

This project is under the Apache License, Version 2.0. See the [LICENSE](LICENSE) file for the full license text.##Introduction##
This is a package for GO which can be used to create different types of barcodes.

##Supported Barcode Types##
* Aztec Code
* Codabar
* Code 128
* Code 39
* EAN 8
* EAN 13
* Datamatrix
* QR Codes
* 2 of 5

##Documentation##
See [GoDoc](https://godoc.org/github.com/boombuler/barcode)

To create a barcode use the Encode function from one of the subpackages.
# Git Module [![Build Status](https://travis-ci.org/gogits/git-module.svg?branch=master)](https://travis-ci.org/gogits/git-module)

Package git-module is a Go module for Git access through shell commands.

## Limitations

- Go version must be at least **1.4**.
- Git version must be no less than **1.7.1**, and greater than or equal to **1.8.3** is recommended.
- For Windows users, try use as new a version as possible.

## License

This project is under the MIT License. See the [LICENSE](LICENSE) file for the full license text.
# chardet

chardet is library to automatically detect
[charset](http://en.wikipedia.org/wiki/Character_encoding) of texts for [Go
programming language](http://golang.org/). It's based on the algorithm and data
in [ICU](http://icu-project.org/)'s implementation.

The project was created by [saintfish](http://github.com/saintfish/chardet). In January 2015 it was forked by the gogits project in order to incorporate bugfixes and new features.

## Documentation and Usage

See [pkgdoc](http://godoc.org/github.com/gogits/chardet)
### Minimal windows service stub

Programs designed to run from most *nix style operating systems
can import this package to enable running programs as services without modifying
them.

```
import _ "github.com/kardianos/minwinsvc"
```

If you need more control over the exit behavior, set
```
minwinsvc.SetOnExit(func() {
	// Do something.
	// Within 10 seconds call:
	os.Exit(0)
})
```
Gogs API client in Go
=====================

This package is still in experiment, see [Wiki](https://github.com/gogits/go-gogs-client/wiki) for documentation.

## License

This project is under the MIT License. See the [LICENSE](https://github.com/gogits/gogs/blob/master/LICENSE) file for the full license text.Simple [golang](https://www.golang.org) library for serving
[federated avatars](https://www.libravatar.org)

[![trunk](https://goreportcard.com/badge/strk.kbt.io/projects/go/libravatar)]
(https://goreportcard.com/report/strk.kbt.io/projects/go/libravatar)

# Use

```sh
go get strk.kbt.io/projects/go/libravatar
cd $GOPATH/src/strk.kbt.io/projects/go/libravatar
go doc
```

# Contribute

A clone of the code repository would be downloaded by `go get`.
You can send patches or pull requests to strk@kbt.io.

If you need a place to publish your contribution branches,
you could start from a fork of the gitlab mirror:
https://gitlab.com/strk/go-libravatar
  
# Contacts

 * Project homepage: http://strk.kbt.io/projects/go/libravatar
 * Maintainer: Sandro Santilli <strk@kbt.io>

[![GoDoc](http://godoc.org/github.com/robfig/cron?status.png)](http://godoc.org/github.com/robfig/cron) 
[![Build Status](https://travis-ci.org/robfig/cron.svg?branch=master)](https://travis-ci.org/robfig/cron)
# Go-MySQL-Driver

A MySQL-Driver for Go's [database/sql](http://golang.org/pkg/database/sql) package

![Go-MySQL-Driver logo](https://raw.github.com/wiki/go-sql-driver/mysql/gomysql_m.png "Golang Gopher holding the MySQL Dolphin")

**Latest stable Release:** [Version 1.2 (June 03, 2014)](https://github.com/go-sql-driver/mysql/releases)

[![Build Status](https://travis-ci.org/go-sql-driver/mysql.png?branch=master)](https://travis-ci.org/go-sql-driver/mysql)

---------------------------------------
  * [Features](#features)
  * [Requirements](#requirements)
  * [Installation](#installation)
  * [Usage](#usage)
    * [DSN (Data Source Name)](#dsn-data-source-name)
      * [Password](#password)
      * [Protocol](#protocol)
      * [Address](#address)
      * [Parameters](#parameters)
      * [Examples](#examples)
    * [LOAD DATA LOCAL INFILE support](#load-data-local-infile-support)
    * [time.Time support](#timetime-support)
    * [Unicode support](#unicode-support)
  * [Testing / Development](#testing--development)
  * [License](#license)

---------------------------------------

## Features
  * Lightweight and [fast](https://github.com/go-sql-driver/sql-benchmark "golang MySQL-Driver performance")
  * Native Go implementation. No C-bindings, just pure Go
  * Connections over TCP/IPv4, TCP/IPv6, Unix domain sockets or [custom protocols](http://godoc.org/github.com/go-sql-driver/mysql#DialFunc)
  * Automatic handling of broken connections
  * Automatic Connection Pooling *(by database/sql package)*
  * Supports queries larger than 16MB
  * Full [`sql.RawBytes`](http://golang.org/pkg/database/sql/#RawBytes) support.
  * Intelligent `LONG DATA` handling in prepared statements
  * Secure `LOAD DATA LOCAL INFILE` support with file Whitelisting and `io.Reader` support
  * Optional `time.Time` parsing
  * Optional placeholder interpolation

## Requirements
  * Go 1.2 or higher
  * MySQL (4.1+), MariaDB, Percona Server, Google CloudSQL or Sphinx (2.2.3+)

---------------------------------------

## Installation
Simple install the package to your [$GOPATH](http://code.google.com/p/go-wiki/wiki/GOPATH "GOPATH") with the [go tool](http://golang.org/cmd/go/ "go command") from shell:
```bash
$ go get github.com/go-sql-driver/mysql
```
Make sure [Git is installed](http://git-scm.com/downloads) on your machine and in your system's `PATH`.

## Usage
_Go MySQL Driver_ is an implementation of Go's `database/sql/driver` interface. You only need to import the driver and can use the full [`database/sql`](http://golang.org/pkg/database/sql) API then.

Use `mysql` as `driverName` and a valid [DSN](#dsn-data-source-name)  as `dataSourceName`:
```go
import "database/sql"
import _ "github.com/go-sql-driver/mysql"

db, err := sql.Open("mysql", "user:password@/dbname")
```

[Examples are available in our Wiki](https://github.com/go-sql-driver/mysql/wiki/Examples "Go-MySQL-Driver Examples").


### DSN (Data Source Name)

The Data Source Name has a common format, like e.g. [PEAR DB](http://pear.php.net/manual/en/package.database.db.intro-dsn.php) uses it, but without type-prefix (optional parts marked by squared brackets):
```
[username[:password]@][protocol[(address)]]/dbname[?param1=value1&...&paramN=valueN]
```

A DSN in its fullest form:
```
username:password@protocol(address)/dbname?param=value
```

Except for the databasename, all values are optional. So the minimal DSN is:
```
/dbname
```

If you do not want to preselect a database, leave `dbname` empty:
```
/
```
This has the same effect as an empty DSN string:
```

```

Alternatively, [Config.FormatDSN](https://godoc.org/github.com/go-sql-driver/mysql#Config.FormatDSN) can be used to create a DSN string by filling a struct.

#### Password
Passwords can consist of any character. Escaping is **not** necessary.

#### Protocol
See [net.Dial](http://golang.org/pkg/net/#Dial) for more information which networks are available.
In general you should use an Unix domain socket if available and TCP otherwise for best performance.

#### Address
For TCP and UDP networks, addresses have the form `host:port`.
If `host` is a literal IPv6 address, it must be enclosed in square brackets.
The functions [net.JoinHostPort](http://golang.org/pkg/net/#JoinHostPort) and [net.SplitHostPort](http://golang.org/pkg/net/#SplitHostPort) manipulate addresses in this form.

For Unix domain sockets the address is the absolute path to the MySQL-Server-socket, e.g. `/var/run/mysqld/mysqld.sock` or `/tmp/mysql.sock`.

#### Parameters
*Parameters are case-sensitive!*

Notice that any of `true`, `TRUE`, `True` or `1` is accepted to stand for a true boolean value. Not surprisingly, false can be specified as any of: `false`, `FALSE`, `False` or `0`.

##### `allowAllFiles`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

`allowAllFiles=true` disables the file Whitelist for `LOAD DATA LOCAL INFILE` and allows *all* files.
[*Might be insecure!*](http://dev.mysql.com/doc/refman/5.7/en/load-data-local.html)

##### `allowCleartextPasswords`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

`allowCleartextPasswords=true` allows using the [cleartext client side plugin](http://dev.mysql.com/doc/en/cleartext-authentication-plugin.html) if required by an account, such as one defined with the [PAM authentication plugin](http://dev.mysql.com/doc/en/pam-authentication-plugin.html). Sending passwords in clear text may be a security problem in some configurations. To avoid problems if there is any possibility that the password would be intercepted, clients should connect to MySQL Server using a method that protects the password. Possibilities include [TLS / SSL](#tls), IPsec, or a private network.

##### `allowOldPasswords`

```
Type:           bool
Valid Values:   true, false
Default:        false
```
`allowOldPasswords=true` allows the usage of the insecure old password method. This should be avoided, but is necessary in some cases. See also [the old_passwords wiki page](https://github.com/go-sql-driver/mysql/wiki/old_passwords).

##### `charset`

```
Type:           string
Valid Values:   <name>
Default:        none
```

Sets the charset used for client-server interaction (`"SET NAMES <value>"`). If multiple charsets are set (separated by a comma), the following charset is used if setting the charset failes. This enables for example support for `utf8mb4` ([introduced in MySQL 5.5.3](http://dev.mysql.com/doc/refman/5.5/en/charset-unicode-utf8mb4.html)) with fallback to `utf8` for older servers (`charset=utf8mb4,utf8`).

Usage of the `charset` parameter is discouraged because it issues additional queries to the server.
Unless you need the fallback behavior, please use `collation` instead.

##### `collation`

```
Type:           string
Valid Values:   <name>
Default:        utf8_general_ci
```

Sets the collation used for client-server interaction on connection. In contrast to `charset`, `collation` does not issue additional queries. If the specified collation is unavailable on the target server, the connection will fail.

A list of valid charsets for a server is retrievable with `SHOW COLLATION`.

##### `clientFoundRows`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

`clientFoundRows=true` causes an UPDATE to return the number of matching rows instead of the number of rows changed.

##### `columnsWithAlias`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

When `columnsWithAlias` is true, calls to `sql.Rows.Columns()` will return the table alias and the column name separated by a dot. For example:

```
SELECT u.id FROM users as u
```

will return `u.id` instead of just `id` if `columnsWithAlias=true`.

##### `interpolateParams`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

If `interpolateParams` is true, placeholders (`?`) in calls to `db.Query()` and `db.Exec()` are interpolated into a single query string with given parameters. This reduces the number of roundtrips, since the driver has to prepare a statement, execute it with given parameters and close the statement again with `interpolateParams=false`.

*This can not be used together with the multibyte encodings BIG5, CP932, GB2312, GBK or SJIS. These are blacklisted as they may [introduce a SQL injection vulnerability](http://stackoverflow.com/a/12118602/3430118)!*

##### `loc`

```
Type:           string
Valid Values:   <escaped name>
Default:        UTC
```

Sets the location for time.Time values (when using `parseTime=true`). *"Local"* sets the system's location. See [time.LoadLocation](http://golang.org/pkg/time/#LoadLocation) for details.

Note that this sets the location for time.Time values but does not change MySQL's [time_zone setting](https://dev.mysql.com/doc/refman/5.5/en/time-zone-support.html). For that see the [time_zone system variable](#system-variables), which can also be set as a DSN parameter.

Please keep in mind, that param values must be [url.QueryEscape](http://golang.org/pkg/net/url/#QueryEscape)'ed. Alternatively you can manually replace the `/` with `%2F`. For example `US/Pacific` would be `loc=US%2FPacific`.

##### `multiStatements`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

Allow multiple statements in one query. While this allows batch queries, it also greatly increases the risk of SQL injections. Only the result of the first query is returned, all other results are silently discarded.

When `multiStatements` is used, `?` parameters must only be used in the first statement.


##### `parseTime`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

`parseTime=true` changes the output type of `DATE` and `DATETIME` values to `time.Time` instead of `[]byte` / `string`


##### `readTimeout`

```
Type:           decimal number
Default:        0
```

I/O read timeout. The value must be a decimal number with an unit suffix ( *"ms"*, *"s"*, *"m"*, *"h"* ), such as *"30s"*, *"0.5m"* or *"1m30s"*.


##### `strict`

```
Type:           bool
Valid Values:   true, false
Default:        false
```

`strict=true` enables the strict mode in which MySQL warnings are treated as errors.

By default MySQL also treats notes as warnings. Use [`sql_notes=false`](http://dev.mysql.com/doc/refman/5.7/en/server-system-variables.html#sysvar_sql_notes) to ignore notes. See the [examples](#examples) for an DSN example.


##### `timeout`

```
Type:           decimal number
Default:        OS default
```

*Driver* side connection timeout. The value must be a decimal number with an unit suffix ( *"ms"*, *"s"*, *"m"*, *"h"* ), such as *"30s"*, *"0.5m"* or *"1m30s"*. To set a server side timeout, use the parameter [`wait_timeout`](http://dev.mysql.com/doc/refman/5.6/en/server-system-variables.html#sysvar_wait_timeout).


##### `tls`

```
Type:           bool / string
Valid Values:   true, false, skip-verify, <name>
Default:        false
```

`tls=true` enables TLS / SSL encrypted connection to the server. Use `skip-verify` if you want to use a self-signed or invalid certificate (server side). Use a custom value registered with [`mysql.RegisterTLSConfig`](http://godoc.org/github.com/go-sql-driver/mysql#RegisterTLSConfig).


##### `writeTimeout`

```
Type:           decimal number
Default:        0
```

I/O write timeout. The value must be a decimal number with an unit suffix ( *"ms"*, *"s"*, *"m"*, *"h"* ), such as *"30s"*, *"0.5m"* or *"1m30s"*.


##### System Variables

All other parameters are interpreted as system variables:
  * `autocommit`: `"SET autocommit=<value>"`
  * [`time_zone`](https://dev.mysql.com/doc/refman/5.5/en/time-zone-support.html): `"SET time_zone=<value>"`
  * [`tx_isolation`](https://dev.mysql.com/doc/refman/5.5/en/server-system-variables.html#sysvar_tx_isolation): `"SET tx_isolation=<value>"`
  * `param`: `"SET <param>=<value>"`

*The values must be [url.QueryEscape](http://golang.org/pkg/net/url/#QueryEscape)'ed!*

#### Examples
```
user@unix(/path/to/socket)/dbname
```

```
root:pw@unix(/tmp/mysql.sock)/myDatabase?loc=Local
```

```
user:password@tcp(localhost:5555)/dbname?tls=skip-verify&autocommit=true
```

Use the [strict mode](#strict) but ignore notes:
```
user:password@/dbname?strict=true&sql_notes=false
```

TCP via IPv6:
```
user:password@tcp([de:ad:be:ef::ca:fe]:80)/dbname?timeout=90s&collation=utf8mb4_unicode_ci
```

TCP on a remote host, e.g. Amazon RDS:
```
id:password@tcp(your-amazonaws-uri.com:3306)/dbname
```

Google Cloud SQL on App Engine:
```
user@cloudsql(project-id:instance-name)/dbname
```

TCP using default port (3306) on localhost:
```
user:password@tcp/dbname?charset=utf8mb4,utf8&sys_var=esc%40ped
```

Use the default protocol (tcp) and host (localhost:3306):
```
user:password@/dbname
```

No Database preselected:
```
user:password@/
```

### `LOAD DATA LOCAL INFILE` support
For this feature you need direct access to the package. Therefore you must change the import path (no `_`):
```go
import "github.com/go-sql-driver/mysql"
```

Files must be whitelisted by registering them with `mysql.RegisterLocalFile(filepath)` (recommended) or the Whitelist check must be deactivated by using the DSN parameter `allowAllFiles=true` ([*Might be insecure!*](http://dev.mysql.com/doc/refman/5.7/en/load-data-local.html)).

To use a `io.Reader` a handler function must be registered with `mysql.RegisterReaderHandler(name, handler)` which returns a `io.Reader` or `io.ReadCloser`. The Reader is available with the filepath `Reader::<name>` then. Choose different names for different handlers and `DeregisterReaderHandler` when you don't need it anymore.

See the [godoc of Go-MySQL-Driver](http://godoc.org/github.com/go-sql-driver/mysql "golang mysql driver documentation") for details.


### `time.Time` support
The default internal output type of MySQL `DATE` and `DATETIME` values is `[]byte` which allows you to scan the value into a `[]byte`, `string` or `sql.RawBytes` variable in your programm.

However, many want to scan MySQL `DATE` and `DATETIME` values into `time.Time` variables, which is the logical opposite in Go to `DATE` and `DATETIME` in MySQL. You can do that by changing the internal output type from `[]byte` to `time.Time` with the DSN parameter `parseTime=true`. You can set the default [`time.Time` location](http://golang.org/pkg/time/#Location) with the `loc` DSN parameter.

**Caution:** As of Go 1.1, this makes `time.Time` the only variable type you can scan `DATE` and `DATETIME` values into. This breaks for example [`sql.RawBytes` support](https://github.com/go-sql-driver/mysql/wiki/Examples#rawbytes).

Alternatively you can use the [`NullTime`](http://godoc.org/github.com/go-sql-driver/mysql#NullTime) type as the scan destination, which works with both `time.Time` and `string` / `[]byte`.


### Unicode support
Since version 1.1 Go-MySQL-Driver automatically uses the collation `utf8_general_ci` by default.

Other collations / charsets can be set using the [`collation`](#collation) DSN parameter.

Version 1.0 of the driver recommended adding `&charset=utf8` (alias for `SET NAMES utf8`) to the DSN to enable proper UTF-8 support. This is not necessary anymore. The [`collation`](#collation) parameter should be preferred to set another collation / charset than the default.

See http://dev.mysql.com/doc/refman/5.7/en/charset-unicode.html for more details on MySQL's Unicode support.


## Testing / Development
To run the driver tests you may need to adjust the configuration. See the [Testing Wiki-Page](https://github.com/go-sql-driver/mysql/wiki/Testing "Testing") for details.

Go-MySQL-Driver is not feature-complete yet. Your help is very appreciated.
If you want to contribute, you can work on an [open issue](https://github.com/go-sql-driver/mysql/issues?state=open) or review a [pull request](https://github.com/go-sql-driver/mysql/pulls).

See the [Contribution Guidelines](https://github.com/go-sql-driver/mysql/blob/master/CONTRIBUTING.md) for details.

---------------------------------------

## License
Go-MySQL-Driver is licensed under the [Mozilla Public License Version 2.0](https://raw.github.com/go-sql-driver/mysql/master/LICENSE)

Mozilla summarizes the license scope as follows:
> MPL: The copyleft applies to any files containing MPLed code.


That means:
  * You can **use** the **unchanged** source code both in private and commercially
  * When distributing, you **must publish** the source code of any **changed files** licensed under the MPL 2.0 under a) the MPL 2.0 itself or b) a compatible license (e.g. GPL 3.0 or Apache License 2.0)
  * You **needn't publish** the source code of your library as long as the files licensed under the MPL 2.0 are **unchanged**

Please read the [MPL 2.0 FAQ](http://www.mozilla.org/MPL/2.0/FAQ.html) if you have further questions regarding the license.

You can read the full terms here: [LICENSE](https://raw.github.com/go-sql-driver/mysql/master/LICENSE)

![Go Gopher and MySQL Dolphin](https://raw.github.com/wiki/go-sql-driver/mysql/go-mysql-driver_m.jpg "Golang Gopher transporting the MySQL Dolphin in a wheelbarrow")

go-version [![Build Status](https://travis-ci.org/mcuadros/go-version.svg?branch=master)](https://travis-ci.org/mcuadros/go-version) [![GoDoc](https://godoc.org/github.com/mcuadros/go-version?status.svg)](http://godoc.org/github.com/mcuadros/go-version)
==============================

Version normalizer and comparison library for go, heavy based on PHP version_compare function and Version comparsion libs from [Composer](https://github.com/composer/composer) PHP project

Installation
------------

The recommended way to install go-version

```
go get github.com/mcuadros/go-version
```

Examples
--------

How import the package

```go
import (
    "github.com/mcuadros/go-version"
)
```

`version.Normalize()`: Normalizes a version string to be able to perform comparisons on it

```go
version.Normalize("10.4.13-b")
//Returns: 10.4.13.0-beta
```


`version.CompareSimple()`: Compares two normalizated version number strings

```go
version.CompareSimple("1.2", "1.0.1")
//Returns: 1

version.CompareSimple("1.0rc1", "1.0")
//Returns: -1
```


`version.Compare()`: Compares two normalizated version number strings, for a particular relationship

```go
version.Compare("1.0-dev", "1.0", "<")
//Returns: true

version.Compare("1.0rc1", "1.0", ">=")
//Returns: false

version.Compare("2.3.4", "v3.1.2", "<")
//Returns: true
```

`version.ConstrainGroup.Match()`: Match a given version againts a group of constrains, read about constraint string format at [Composer documentation](http://getcomposer.org/doc/01-basic-usage.md#package-versions)  

```go
c := version.NewConstrainGroupFromString(">2.0,<=3.0")
c.Match("2.5.0beta")
//Returns: true

c := version.NewConstrainGroupFromString("~1.2.3")
c.Match("1.2.3.5")
//Returns: true
```

`version.Sort()`: Sorts a string slice of version number strings using version.CompareSimple()

```go
version.Sort([]string{"1.10-dev", "1.0rc1", "1.0", "1.0-dev"})
//Returns []string{"1.0-dev", "1.0rc1", "1.0", "1.10-dev"}
```

License
-------

MIT, see [LICENSE](LICENSE)
[![Build Status](https://travis-ci.org/msteinert/pam.svg?branch=master)](https://travis-ci.org/msteinert/pam)
[![GoDoc](https://godoc.org/github.com/msteinert/pam?status.svg)](http://godoc.org/github.com/msteinert/pam)
[![Coverage Status](https://coveralls.io/repos/msteinert/pam/badge.svg?branch=master)](https://coveralls.io/r/msteinert/pam?branch=master)
[![Go Report Card](http://goreportcard.com/badge/msteinert/pam)](http://goreportcard.com/report/msteinert/pam)

# Go PAM

This is a Go wrapper for the PAM application API.

## Testing

To run the full suite, the tests must be run as the root user. To setup your
system for testing, create a user named "test" with the password "secret". For
example:

```
$ sudo useradd test \
    -d /tmp/test \
    -p '$1$Qd8H95T5$RYSZQeoFbEB.gS19zS99A0' \
    -s /bin/false
```

Then execute the tests:

```
$ sudo GOPATH=$GOPATH $(which go) test -v
```

[1]: http://godoc.org/github.com/msteinert/pam
[2]: http://www.linux-pam.org/Linux-PAM-html/Linux-PAM_ADG.html
cli
===

[![Build Status](https://travis-ci.org/urfave/cli.svg?branch=master)](https://travis-ci.org/urfave/cli)
[![Windows Build Status](https://ci.appveyor.com/api/projects/status/rtgk5xufi932pb2v?svg=true)](https://ci.appveyor.com/project/urfave/cli)
[![GoDoc](https://godoc.org/github.com/urfave/cli?status.svg)](https://godoc.org/github.com/urfave/cli)
[![codebeat](https://codebeat.co/badges/0a8f30aa-f975-404b-b878-5fab3ae1cc5f)](https://codebeat.co/projects/github-com-urfave-cli)
[![Go Report Card](https://goreportcard.com/badge/urfave/cli)](https://goreportcard.com/report/urfave/cli)
[![top level coverage](https://gocover.io/_badge/github.com/urfave/cli?0 "top level coverage")](http://gocover.io/github.com/urfave/cli) /
[![altsrc coverage](https://gocover.io/_badge/github.com/urfave/cli/altsrc?0 "altsrc coverage")](http://gocover.io/github.com/urfave/cli/altsrc)

**Notice:** This is the library formerly known as
`github.com/codegangsta/cli` -- Github will automatically redirect requests
to this repository, but we recommend updating your references for clarity.

cli is a simple, fast, and fun package for building command line apps in Go. The
goal is to enable developers to write fast and distributable command line
applications in an expressive way.

<!-- toc -->

- [Overview](#overview)
- [Installation](#installation)
  * [Supported platforms](#supported-platforms)
  * [Using the `v2` branch](#using-the-v2-branch)
  * [Pinning to the `v1` releases](#pinning-to-the-v1-releases)
- [Getting Started](#getting-started)
- [Examples](#examples)
  * [Arguments](#arguments)
  * [Flags](#flags)
    + [Placeholder Values](#placeholder-values)
    + [Alternate Names](#alternate-names)
    + [Ordering](#ordering)
    + [Values from the Environment](#values-from-the-environment)
    + [Values from alternate input sources (YAML, TOML, and others)](#values-from-alternate-input-sources-yaml-toml-and-others)
  * [Subcommands](#subcommands)
  * [Subcommands categories](#subcommands-categories)
  * [Exit code](#exit-code)
  * [Bash Completion](#bash-completion)
    + [Enabling](#enabling)
    + [Distribution](#distribution)
    + [Customization](#customization)
  * [Generated Help Text](#generated-help-text)
    + [Customization](#customization-1)
  * [Version Flag](#version-flag)
    + [Customization](#customization-2)
    + [Full API Example](#full-api-example)
- [Contribution Guidelines](#contribution-guidelines)

<!-- tocstop -->

## Overview

Command line apps are usually so tiny that there is absolutely no reason why
your code should *not* be self-documenting. Things like generating help text and
parsing command flags/options should not hinder productivity when writing a
command line app.

**This is where cli comes into play.** cli makes command line programming fun,
organized, and expressive!

## Installation

Make sure you have a working Go environment.  Go version 1.2+ is supported.  [See
the install instructions for Go](http://golang.org/doc/install.html).

To install cli, simply run:
```
$ go get github.com/urfave/cli
```

Make sure your `PATH` includes the `$GOPATH/bin` directory so your commands can
be easily used:
```
export PATH=$PATH:$GOPATH/bin
```

### Supported platforms

cli is tested against multiple versions of Go on Linux, and against the latest
released version of Go on OS X and Windows.  For full details, see
[`./.travis.yml`](./.travis.yml) and [`./appveyor.yml`](./appveyor.yml).

### Using the `v2` branch

**Warning**: The `v2` branch is currently unreleased and considered unstable.

There is currently a long-lived branch named `v2` that is intended to land as
the new `master` branch once development there has settled down.  The current
`master` branch (mirrored as `v1`) is being manually merged into `v2` on
an irregular human-based schedule, but generally if one wants to "upgrade" to
`v2` *now* and accept the volatility (read: "awesomeness") that comes along with
that, please use whatever version pinning of your preference, such as via
`gopkg.in`:

```
$ go get gopkg.in/urfave/cli.v2
```

``` go
...
import (
  "gopkg.in/urfave/cli.v2" // imports as package "cli"
)
...
```

### Pinning to the `v1` releases

Similarly to the section above describing use of the `v2` branch, if one wants
to avoid any unexpected compatibility pains once `v2` becomes `master`, then
pinning to `v1` is an acceptable option, e.g.:

```
$ go get gopkg.in/urfave/cli.v1
```

``` go
...
import (
  "gopkg.in/urfave/cli.v1" // imports as package "cli"
)
...
```

This will pull the latest tagged `v1` release (e.g. `v1.18.1` at the time of writing).

## Getting Started

One of the philosophies behind cli is that an API should be playful and full of
discovery. So a cli app can be as little as one line of code in `main()`.

<!-- {
  "args": ["&#45;&#45;help"],
  "output": "A new cli application"
} -->
``` go
package main

import (
  "os"

  "github.com/urfave/cli"
)

func main() {
  cli.NewApp().Run(os.Args)
}
```

This app will run and show help text, but is not very useful. Let's give an
action to execute and some help documentation:

<!-- {
  "output": "boom! I say!"
} -->
``` go
package main

import (
  "fmt"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()
  app.Name = "boom"
  app.Usage = "make an explosive entrance"
  app.Action = func(c *cli.Context) error {
    fmt.Println("boom! I say!")
    return nil
  }

  app.Run(os.Args)
}
```

Running this already gives you a ton of functionality, plus support for things
like subcommands and flags, which are covered below.

## Examples

Being a programmer can be a lonely job. Thankfully by the power of automation
that is not the case! Let's create a greeter app to fend off our demons of
loneliness!

Start by creating a directory named `greet`, and within it, add a file,
`greet.go` with the following code in it:

<!-- {
  "output": "Hello friend!"
} -->
``` go
package main

import (
  "fmt"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()
  app.Name = "greet"
  app.Usage = "fight the loneliness!"
  app.Action = func(c *cli.Context) error {
    fmt.Println("Hello friend!")
    return nil
  }

  app.Run(os.Args)
}
```

Install our command to the `$GOPATH/bin` directory:

```
$ go install
```

Finally run our new command:

```
$ greet
Hello friend!
```

cli also generates neat help text:

```
$ greet help
NAME:
    greet - fight the loneliness!

USAGE:
    greet [global options] command [command options] [arguments...]

VERSION:
    0.0.0

COMMANDS:
    help, h  Shows a list of commands or help for one command

GLOBAL OPTIONS
    --version Shows version information
```

### Arguments

You can lookup arguments by calling the `Args` function on `cli.Context`, e.g.:

<!-- {
  "output": "Hello \""
} -->
``` go
package main

import (
  "fmt"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Action = func(c *cli.Context) error {
    fmt.Printf("Hello %q", c.Args().Get(0))
    return nil
  }

  app.Run(os.Args)
}
```

### Flags

Setting and querying flags is simple.

<!-- {
  "output": "Hello Nefertiti"
} -->
``` go
package main

import (
  "fmt"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Flags = []cli.Flag {
    cli.StringFlag{
      Name: "lang",
      Value: "english",
      Usage: "language for the greeting",
    },
  }

  app.Action = func(c *cli.Context) error {
    name := "Nefertiti"
    if c.NArg() > 0 {
      name = c.Args().Get(0)
    }
    if c.String("lang") == "spanish" {
      fmt.Println("Hola", name)
    } else {
      fmt.Println("Hello", name)
    }
    return nil
  }

  app.Run(os.Args)
}
```

You can also set a destination variable for a flag, to which the content will be
scanned.

<!-- {
  "output": "Hello someone"
} -->
``` go
package main

import (
  "os"
  "fmt"

  "github.com/urfave/cli"
)

func main() {
  var language string

  app := cli.NewApp()

  app.Flags = []cli.Flag {
    cli.StringFlag{
      Name:        "lang",
      Value:       "english",
      Usage:       "language for the greeting",
      Destination: &language,
    },
  }

  app.Action = func(c *cli.Context) error {
    name := "someone"
    if c.NArg() > 0 {
      name = c.Args()[0]
    }
    if language == "spanish" {
      fmt.Println("Hola", name)
    } else {
      fmt.Println("Hello", name)
    }
    return nil
  }

  app.Run(os.Args)
}
```

See full list of flags at http://godoc.org/github.com/urfave/cli

#### Placeholder Values

Sometimes it's useful to specify a flag's value within the usage string itself.
Such placeholders are indicated with back quotes.

For example this:

<!-- {
  "args": ["&#45;&#45;help"],
  "output": "&#45;&#45;config FILE, &#45;c FILE"
} -->
```go
package main

import (
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Flags = []cli.Flag{
    cli.StringFlag{
      Name:  "config, c",
      Usage: "Load configuration from `FILE`",
    },
  }

  app.Run(os.Args)
}
```

Will result in help output like:

```
--config FILE, -c FILE   Load configuration from FILE
```

Note that only the first placeholder is used. Subsequent back-quoted words will
be left as-is.

#### Alternate Names

You can set alternate (or short) names for flags by providing a comma-delimited
list for the `Name`. e.g.

<!-- {
  "args": ["&#45;&#45;help"],
  "output": "&#45;&#45;lang value, &#45;l value.*language for the greeting.*default: \"english\""
} -->
``` go
package main

import (
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Flags = []cli.Flag {
    cli.StringFlag{
      Name: "lang, l",
      Value: "english",
      Usage: "language for the greeting",
    },
  }

  app.Run(os.Args)
}
```

That flag can then be set with `--lang spanish` or `-l spanish`. Note that
giving two different forms of the same flag in the same command invocation is an
error.

#### Ordering

Flags for the application and commands are shown in the order they are defined.
However, it's possible to sort them from outside this library by using `FlagsByName`
with `sort`.

For example this:

<!-- {
  "args": ["&#45;&#45;help"],
  "output": "Load configuration from FILE\n.*Language for the greeting.*"
} -->
``` go
package main

import (
  "os"
  "sort"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Flags = []cli.Flag {
    cli.StringFlag{
      Name: "lang, l",
      Value: "english",
      Usage: "Language for the greeting",
    },
    cli.StringFlag{
      Name: "config, c",
      Usage: "Load configuration from `FILE`",
    },
  }

  sort.Sort(cli.FlagsByName(app.Flags))

  app.Run(os.Args)
}
```

Will result in help output like:

```
--config FILE, -c FILE  Load configuration from FILE
--lang value, -l value  Language for the greeting (default: "english")
```

#### Values from the Environment

You can also have the default value set from the environment via `EnvVar`.  e.g.

<!-- {
  "args": ["&#45;&#45;help"],
  "output": "language for the greeting.*APP_LANG"
} -->
``` go
package main

import (
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Flags = []cli.Flag {
    cli.StringFlag{
      Name: "lang, l",
      Value: "english",
      Usage: "language for the greeting",
      EnvVar: "APP_LANG",
    },
  }

  app.Run(os.Args)
}
```

The `EnvVar` may also be given as a comma-delimited "cascade", where the first
environment variable that resolves is used as the default.

<!-- {
  "args": ["&#45;&#45;help"],
  "output": "language for the greeting.*LEGACY_COMPAT_LANG.*APP_LANG.*LANG"
} -->
``` go
package main

import (
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Flags = []cli.Flag {
    cli.StringFlag{
      Name: "lang, l",
      Value: "english",
      Usage: "language for the greeting",
      EnvVar: "LEGACY_COMPAT_LANG,APP_LANG,LANG",
    },
  }

  app.Run(os.Args)
}
```

#### Values from alternate input sources (YAML, TOML, and others)

There is a separate package altsrc that adds support for getting flag values
from other file input sources.

Currently supported input source formats:
* YAML
* TOML

In order to get values for a flag from an alternate input source the following
code would be added to wrap an existing cli.Flag like below:

``` go
  altsrc.NewIntFlag(cli.IntFlag{Name: "test"})
```

Initialization must also occur for these flags. Below is an example initializing
getting data from a yaml file below.

``` go
  command.Before = altsrc.InitInputSourceWithContext(command.Flags, NewYamlSourceFromFlagFunc("load"))
```

The code above will use the "load" string as a flag name to get the file name of
a yaml file from the cli.Context.  It will then use that file name to initialize
the yaml input source for any flags that are defined on that command.  As a note
the "load" flag used would also have to be defined on the command flags in order
for this code snipped to work.

Currently only the aboved specified formats are supported but developers can
add support for other input sources by implementing the
altsrc.InputSourceContext for their given sources.

Here is a more complete sample of a command using YAML support:

<!-- {
  "args": ["test-cmd", "&#45;&#45;help"],
  "output": "&#45&#45;test value.*default: 0"
} -->
``` go
package notmain

import (
  "fmt"
  "os"

  "github.com/urfave/cli"
  "github.com/urfave/cli/altsrc"
)

func main() {
  app := cli.NewApp()

  flags := []cli.Flag{
    altsrc.NewIntFlag(cli.IntFlag{Name: "test"}),
    cli.StringFlag{Name: "load"},
  }

  app.Action = func(c *cli.Context) error {
    fmt.Println("yaml ist rad")
    return nil
  }

  app.Before = altsrc.InitInputSourceWithContext(flags, altsrc.NewYamlSourceFromFlagFunc("load"))
  app.Flags = flags

  app.Run(os.Args)
}
```

### Subcommands

Subcommands can be defined for a more git-like command line app.

<!-- {
  "args": ["template", "add"],
  "output": "new task template: .+"
} -->
```go
package main

import (
  "fmt"
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Commands = []cli.Command{
    {
      Name:    "add",
      Aliases: []string{"a"},
      Usage:   "add a task to the list",
      Action:  func(c *cli.Context) error {
        fmt.Println("added task: ", c.Args().First())
        return nil
      },
    },
    {
      Name:    "complete",
      Aliases: []string{"c"},
      Usage:   "complete a task on the list",
      Action:  func(c *cli.Context) error {
        fmt.Println("completed task: ", c.Args().First())
        return nil
      },
    },
    {
      Name:        "template",
      Aliases:     []string{"t"},
      Usage:       "options for task templates",
      Subcommands: []cli.Command{
        {
          Name:  "add",
          Usage: "add a new template",
          Action: func(c *cli.Context) error {
            fmt.Println("new task template: ", c.Args().First())
            return nil
          },
        },
        {
          Name:  "remove",
          Usage: "remove an existing template",
          Action: func(c *cli.Context) error {
            fmt.Println("removed task template: ", c.Args().First())
            return nil
          },
        },
      },
    },
  }

  app.Run(os.Args)
}
```

### Subcommands categories

For additional organization in apps that have many subcommands, you can
associate a category for each command to group them together in the help
output.

E.g.

```go
package main

import (
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()

  app.Commands = []cli.Command{
    {
      Name: "noop",
    },
    {
      Name:     "add",
      Category: "template",
    },
    {
      Name:     "remove",
      Category: "template",
    },
  }

  app.Run(os.Args)
}
```

Will include:

```
COMMANDS:
    noop

  Template actions:
    add
    remove
```

### Exit code

Calling `App.Run` will not automatically call `os.Exit`, which means that by
default the exit code will "fall through" to being `0`.  An explicit exit code
may be set by returning a non-nil error that fulfills `cli.ExitCoder`, *or* a
`cli.MultiError` that includes an error that fulfills `cli.ExitCoder`, e.g.:

``` go
package main

import (
  "os"

  "github.com/urfave/cli"
)

func main() {
  app := cli.NewApp()
  app.Flags = []cli.Flag{
    cli.BoolTFlag{
      Name:  "ginger-crouton",
      Usage: "is it in the soup?",
    },
  }
  app.Action = func(ctx *cli.Context) error {
    if !ctx.Bool("ginger-crouton") {
      return cli.NewExitError("it is not in the soup", 86)
    }
    return nil
  }

  app.Run(os.Args)
}
```

### Bash Completion

You can enable completion commands by setting the `EnableBashCompletion`
flag on the `App` object.  By default, this setting will only auto-complete to
show an app's subcommands, but you can write your own completion methods for
the App or its subcommands.

<!-- {
  "args": ["complete", "&#45;&#45;generate&#45;bash&#45;completion"],
  "output": "laundry"
} -->
``` go
package main

import (
  "fmt"
  "os"

  "github.com/urfave/cli"
)

func main() {
  tasks := []string{"cook", "clean", "laundry", "eat", "sleep", "code"}

  app := cli.NewApp()
  app.EnableBashCompletion = true
  app.Commands = []cli.Command{
    {
      Name:  "complete",
      Aliases: []string{"c"},
      Usage: "complete a task on the list",
      Action: func(c *cli.Context) error {
         fmt.Println("completed task: ", c.Args().First())
         return nil
      },
      BashComplete: func(c *cli.Context) {
        // This will complete if no args are passed
        if c.NArg() > 0 {
          return
        }
        for _, t := range tasks {
          fmt.Println(t)
        }
      },
    },
  }

  app.Run(os.Args)
}
```

#### Enabling

Source the `autocomplete/bash_autocomplete` file in your `.bashrc` file while
setting the `PROG` variable to the name of your program:

`PROG=myprogram source /.../cli/autocomplete/bash_autocomplete`

#### Distribution

Copy `autocomplete/bash_autocomplete` into `/etc/bash_completion.d/` and rename
it to the name of the program you wish to add autocomplete support for (or
automatically install it there if you are distributing a package). Don't forget
to source the file to make it active in the current shell.

```
sudo cp src/bash_autocomplete /etc/bash_completion.d/<myprogram>
source /etc/bash_completion.d/<myprogram>
```

Alternatively, you can just document that users should source the generic
`autocomplete/bash_autocomplete` in their bash configuration with `$PROG` set
to the name of their program (as above).

#### Customization

The default bash completion flag (`--generate-bash-completion`) is defined as
`cli.BashCompletionFlag`, and may be redefined if desired, e.g.:

<!-- {
  "args": ["&#45;&#45;compgen"],
  "output": "wat\nhelp\nh"
} -->
``` go
package main

import (
  "os"

  "github.com/urfave/cli"
)

func main() {
  cli.BashCompletionFlag = cli.BoolFlag{
    Name:   "compgen",
    Hidden: true,
  }

  app := cli.NewApp()
  app.EnableBashCompletion = true
  app.Commands = []cli.Command{
    {
      Name: "wat",
    },
  }
  app.Run(os.Args)
}
```

### Generated Help Text

The default help flag (`-h/--help`) is defined as `cli.HelpFlag` and is checked
by the cli internals in order to print generated help text for the app, command,
or subcommand, and break execution.

#### Customization

All of the help text generation may be customized, and at multiple levels.  The
templates are exposed as variables `AppHelpTemplate`, `CommandHelpTemplate`, and
`SubcommandHelpTemplate` which may be reassigned or augmented, and full override
is possible by assigning a compatible func to the `cli.HelpPrinter` variable,
e.g.:

<!-- {
  "output": "Ha HA.  I pwnd the help!!1"
} -->
``` go
package main

import (
  "fmt"
  "io"
  "os"

  "github.com/urfave/cli"
)

func main() {
  // EXAMPLE: Append to an existing template
  cli.AppHelpTemplate = fmt.Sprintf(`%s

WEBSITE: http://awesometown.example.com

SUPPORT: support@awesometown.example.com

`, cli.AppHelpTemplate)

  // EXAMPLE: Override a template
  cli.AppHelpTemplate = `NAME:
   {{.Name}} - {{.Usage}}
USAGE:
   {{.HelpName}} {{if .VisibleFlags}}[global options]{{end}}{{if .Commands}} command
[command options]{{end}} {{if
.ArgsUsage}}{{.ArgsUsage}}{{else}}[arguments...]{{end}}
   {{if len .Authors}}
AUTHOR(S):
   {{range .Authors}}{{ . }}{{end}}
   {{end}}{{if .Commands}}
COMMANDS:
{{range .Commands}}{{if not .HideHelp}}   {{join .Names ", "}}{{ "\t"
}}{{.Usage}}{{ "\n" }}{{end}}{{end}}{{end}}{{if .VisibleFlags}}
GLOBAL OPTIONS:
   {{range .VisibleFlags}}{{.}}
   {{end}}{{end}}{{if .Copyright }}
COPYRIGHT:
   {{.Copyright}}
   {{end}}{{if .Version}}
VERSION:
   {{.Version}}
   {{end}}
`

  // EXAMPLE: Replace the `HelpPrinter` func
  cli.HelpPrinter = func(w io.Writer, templ string, data interface{}) {
    fmt.Println("Ha HA.  I pwnd the help!!1")
  }

  cli.NewApp().Run(os.Args)
}
```

The default flag may be customized to something other than `-h/--help` by
setting `cli.HelpFlag`, e.g.:

<!-- {
  "args": ["&#45;&#45halp"],
  "output": "haaaaalp.*HALP"
} -->
``` go
package main

import (
  "os"

  "github.com/urfave/cli"
)

func main() {
  cli.HelpFlag = cli.BoolFlag{
    Name: "halp, haaaaalp",
    Usage: "HALP",
    EnvVar: "SHOW_HALP,HALPPLZ",
  }

  cli.NewApp().Run(os.Args)
}
```

### Version Flag

The default version flag (`-v/--version`) is defined as `cli.VersionFlag`, which
is checked by the cli internals in order to print the `App.Version` via
`cli.VersionPrinter` and break execution.

#### Customization

The default flag may be customized to something other than `-v/--version` by
setting `cli.VersionFlag`, e.g.:

<!-- {
  "args": ["&#45;&#45print-version"],
  "output": "partay version 19\\.99\\.0"
} -->
``` go
package main

import (
  "os"

  "github.com/urfave/cli"
)

func main() {
  cli.VersionFlag = cli.BoolFlag{
    Name: "print-version, V",
    Usage: "print only the version",
  }

  app := cli.NewApp()
  app.Name = "partay"
  app.Version = "19.99.0"
  app.Run(os.Args)
}
```

Alternatively, the version printer at `cli.VersionPrinter` may be overridden, e.g.:

<!-- {
  "args": ["&#45;&#45version"],
  "output": "version=19\\.99\\.0 revision=fafafaf"
} -->
``` go
package main

import (
  "fmt"
  "os"

  "github.com/urfave/cli"
)

var (
  Revision = "fafafaf"
)

func main() {
  cli.VersionPrinter = func(c *cli.Context) {
    fmt.Printf("version=%s revision=%s\n", c.App.Version, Revision)
  }

  app := cli.NewApp()
  app.Name = "partay"
  app.Version = "19.99.0"
  app.Run(os.Args)
}
```

#### Full API Example

**Notice**: This is a contrived (functioning) example meant strictly for API
demonstration purposes.  Use of one's imagination is encouraged.

<!-- {
  "output": "made it!\nPhew!"
} -->
``` go
package main

import (
  "errors"
  "flag"
  "fmt"
  "io"
  "io/ioutil"
  "os"
  "time"

  "github.com/urfave/cli"
)

func init() {
  cli.AppHelpTemplate += "\nCUSTOMIZED: you bet ur muffins\n"
  cli.CommandHelpTemplate += "\nYMMV\n"
  cli.SubcommandHelpTemplate += "\nor something\n"

  cli.HelpFlag = cli.BoolFlag{Name: "halp"}
  cli.BashCompletionFlag = cli.BoolFlag{Name: "compgen", Hidden: true}
  cli.VersionFlag = cli.BoolFlag{Name: "print-version, V"}

  cli.HelpPrinter = func(w io.Writer, templ string, data interface{}) {
    fmt.Fprintf(w, "best of luck to you\n")
  }
  cli.VersionPrinter = func(c *cli.Context) {
    fmt.Fprintf(c.App.Writer, "version=%s\n", c.App.Version)
  }
  cli.OsExiter = func(c int) {
    fmt.Fprintf(cli.ErrWriter, "refusing to exit %d\n", c)
  }
  cli.ErrWriter = ioutil.Discard
  cli.FlagStringer = func(fl cli.Flag) string {
    return fmt.Sprintf("\t\t%s", fl.GetName())
  }
}

type hexWriter struct{}

func (w *hexWriter) Write(p []byte) (int, error) {
  for _, b := range p {
    fmt.Printf("%x", b)
  }
  fmt.Printf("\n")

  return len(p), nil
}

type genericType struct{
  s string
}

func (g *genericType) Set(value string) error {
  g.s = value
  return nil
}

func (g *genericType) String() string {
  return g.s
}

func main() {
  app := cli.NewApp()
  app.Name = "kənˈtrīv"
  app.Version = "19.99.0"
  app.Compiled = time.Now()
  app.Authors = []cli.Author{
    cli.Author{
      Name:  "Example Human",
      Email: "human@example.com",
    },
  }
  app.Copyright = "(c) 1999 Serious Enterprise"
  app.HelpName = "contrive"
  app.Usage = "demonstrate available API"
  app.UsageText = "contrive - demonstrating the available API"
  app.ArgsUsage = "[args and such]"
  app.Commands = []cli.Command{
    cli.Command{
      Name:        "doo",
      Aliases:     []string{"do"},
      Category:    "motion",
      Usage:       "do the doo",
      UsageText:   "doo - does the dooing",
      Description: "no really, there is a lot of dooing to be done",
      ArgsUsage:   "[arrgh]",
      Flags: []cli.Flag{
        cli.BoolFlag{Name: "forever, forevvarr"},
      },
      Subcommands: cli.Commands{
        cli.Command{
          Name:   "wop",
          Action: wopAction,
        },
      },
      SkipFlagParsing: false,
      HideHelp:        false,
      Hidden:          false,
      HelpName:        "doo!",
      BashComplete: func(c *cli.Context) {
        fmt.Fprintf(c.App.Writer, "--better\n")
      },
      Before: func(c *cli.Context) error {
        fmt.Fprintf(c.App.Writer, "brace for impact\n")
        return nil
      },
      After: func(c *cli.Context) error {
        fmt.Fprintf(c.App.Writer, "did we lose anyone?\n")
        return nil
      },
      Action: func(c *cli.Context) error {
        c.Command.FullName()
        c.Command.HasName("wop")
        c.Command.Names()
        c.Command.VisibleFlags()
        fmt.Fprintf(c.App.Writer, "dodododododoodododddooooododododooo\n")
        if c.Bool("forever") {
          c.Command.Run(c)
        }
        return nil
      },
      OnUsageError: func(c *cli.Context, err error, isSubcommand bool) error {
        fmt.Fprintf(c.App.Writer, "for shame\n")
        return err
      },
    },
  }
  app.Flags = []cli.Flag{
    cli.BoolFlag{Name: "fancy"},
    cli.BoolTFlag{Name: "fancier"},
    cli.DurationFlag{Name: "howlong, H", Value: time.Second * 3},
    cli.Float64Flag{Name: "howmuch"},
    cli.GenericFlag{Name: "wat", Value: &genericType{}},
    cli.Int64Flag{Name: "longdistance"},
    cli.Int64SliceFlag{Name: "intervals"},
    cli.IntFlag{Name: "distance"},
    cli.IntSliceFlag{Name: "times"},
    cli.StringFlag{Name: "dance-move, d"},
    cli.StringSliceFlag{Name: "names, N"},
    cli.UintFlag{Name: "age"},
    cli.Uint64Flag{Name: "bigage"},
  }
  app.EnableBashCompletion = true
  app.HideHelp = false
  app.HideVersion = false
  app.BashComplete = func(c *cli.Context) {
    fmt.Fprintf(c.App.Writer, "lipstick\nkiss\nme\nlipstick\nringo\n")
  }
  app.Before = func(c *cli.Context) error {
    fmt.Fprintf(c.App.Writer, "HEEEERE GOES\n")
    return nil
  }
  app.After = func(c *cli.Context) error {
    fmt.Fprintf(c.App.Writer, "Phew!\n")
    return nil
  }
  app.CommandNotFound = func(c *cli.Context, command string) {
    fmt.Fprintf(c.App.Writer, "Thar be no %q here.\n", command)
  }
  app.OnUsageError = func(c *cli.Context, err error, isSubcommand bool) error {
    if isSubcommand {
      return err
    }

    fmt.Fprintf(c.App.Writer, "WRONG: %#v\n", err)
    return nil
  }
  app.Action = func(c *cli.Context) error {
    cli.DefaultAppComplete(c)
    cli.HandleExitCoder(errors.New("not an exit coder, though"))
    cli.ShowAppHelp(c)
    cli.ShowCommandCompletions(c, "nope")
    cli.ShowCommandHelp(c, "also-nope")
    cli.ShowCompletions(c)
    cli.ShowSubcommandHelp(c)
    cli.ShowVersion(c)

    categories := c.App.Categories()
    categories.AddCommand("sounds", cli.Command{
      Name: "bloop",
    })

    for _, category := range c.App.Categories() {
      fmt.Fprintf(c.App.Writer, "%s\n", category.Name)
      fmt.Fprintf(c.App.Writer, "%#v\n", category.Commands)
      fmt.Fprintf(c.App.Writer, "%#v\n", category.VisibleCommands())
    }

    fmt.Printf("%#v\n", c.App.Command("doo"))
    if c.Bool("infinite") {
      c.App.Run([]string{"app", "doo", "wop"})
    }

    if c.Bool("forevar") {
      c.App.RunAsSubcommand(c)
    }
    c.App.Setup()
    fmt.Printf("%#v\n", c.App.VisibleCategories())
    fmt.Printf("%#v\n", c.App.VisibleCommands())
    fmt.Printf("%#v\n", c.App.VisibleFlags())

    fmt.Printf("%#v\n", c.Args().First())
    if len(c.Args()) > 0 {
      fmt.Printf("%#v\n", c.Args()[1])
    }
    fmt.Printf("%#v\n", c.Args().Present())
    fmt.Printf("%#v\n", c.Args().Tail())

    set := flag.NewFlagSet("contrive", 0)
    nc := cli.NewContext(c.App, set, c)

    fmt.Printf("%#v\n", nc.Args())
    fmt.Printf("%#v\n", nc.Bool("nope"))
    fmt.Printf("%#v\n", nc.BoolT("nerp"))
    fmt.Printf("%#v\n", nc.Duration("howlong"))
    fmt.Printf("%#v\n", nc.Float64("hay"))
    fmt.Printf("%#v\n", nc.Generic("bloop"))
    fmt.Printf("%#v\n", nc.Int64("bonk"))
    fmt.Printf("%#v\n", nc.Int64Slice("burnks"))
    fmt.Printf("%#v\n", nc.Int("bips"))
    fmt.Printf("%#v\n", nc.IntSlice("blups"))
    fmt.Printf("%#v\n", nc.String("snurt"))
    fmt.Printf("%#v\n", nc.StringSlice("snurkles"))
    fmt.Printf("%#v\n", nc.Uint("flub"))
    fmt.Printf("%#v\n", nc.Uint64("florb"))
    fmt.Printf("%#v\n", nc.GlobalBool("global-nope"))
    fmt.Printf("%#v\n", nc.GlobalBoolT("global-nerp"))
    fmt.Printf("%#v\n", nc.GlobalDuration("global-howlong"))
    fmt.Printf("%#v\n", nc.GlobalFloat64("global-hay"))
    fmt.Printf("%#v\n", nc.GlobalGeneric("global-bloop"))
    fmt.Printf("%#v\n", nc.GlobalInt("global-bips"))
    fmt.Printf("%#v\n", nc.GlobalIntSlice("global-blups"))
    fmt.Printf("%#v\n", nc.GlobalString("global-snurt"))
    fmt.Printf("%#v\n", nc.GlobalStringSlice("global-snurkles"))

    fmt.Printf("%#v\n", nc.FlagNames())
    fmt.Printf("%#v\n", nc.GlobalFlagNames())
    fmt.Printf("%#v\n", nc.GlobalIsSet("wat"))
    fmt.Printf("%#v\n", nc.GlobalSet("wat", "nope"))
    fmt.Printf("%#v\n", nc.NArg())
    fmt.Printf("%#v\n", nc.NumFlags())
    fmt.Printf("%#v\n", nc.Parent())

    nc.Set("wat", "also-nope")

    ec := cli.NewExitError("ohwell", 86)
    fmt.Fprintf(c.App.Writer, "%d", ec.ExitCode())
    fmt.Printf("made it!\n")
    return ec
  }

  if os.Getenv("HEXY") != "" {
    app.Writer = &hexWriter{}
    app.ErrWriter = &hexWriter{}
  }

  app.Metadata = map[string]interface{}{
    "layers":     "many",
    "explicable": false,
    "whatever-values": 19.99,
  }

  app.Run(os.Args)
}

func wopAction(c *cli.Context) error {
  fmt.Fprintf(c.App.Writer, ":wave: over here, eh\n")
  return nil
}
```

## Contribution Guidelines

Feel free to put up a pull request to fix a bug or maybe add a feature. I will
give it a code review and make sure that it does not break backwards
compatibility. If I or any other collaborators agree that it is in line with
the vision of the project, we will work with you to get the code into
a mergeable state and merge it into the master branch.

If you have contributed something significant to the project, we will most
likely add you as a collaborator. As a collaborator you are given the ability
to merge others pull requests. It is very important that new code does not
break existing code, so be careful about what code you do choose to merge.

If you feel like you have contributed to the project but have not yet been
added as a collaborator, we probably forgot to add you, please open an issue.
# bluemonday [![Build Status](https://travis-ci.org/microcosm-cc/bluemonday.svg?branch=master)](https://travis-ci.org/microcosm-cc/bluemonday) [![GoDoc](https://godoc.org/github.com/microcosm-cc/bluemonday?status.png)](https://godoc.org/github.com/microcosm-cc/bluemonday)

bluemonday is a HTML sanitizer implemented in Go. It is fast and highly configurable.

bluemonday takes untrusted user generated content as an input, and will return HTML that has been sanitised against a whitelist of approved HTML elements and attributes so that you can safely include the content in your web page.

If you accept user generated content, and your server uses Go, you **need** bluemonday.

The default policy for user generated content (`bluemonday.UGCPolicy().Sanitize()`) turns this:
```html
Hello <STYLE>.XSS{background-image:url("javascript:alert('XSS')");}</STYLE><A CLASS=XSS></A>World
```

Into a harmless:
```html
Hello World
```

And it turns this:
```html
<a href="javascript:alert('XSS1')" onmouseover="alert('XSS2')">XSS<a>
```

Into this:
```html
XSS
```

Whilst still allowing this:
```html
<a href="http://www.google.com/">
  <img src="https://ssl.gstatic.com/accounts/ui/logo_2x.png"/>
</a>
```

To pass through mostly unaltered (it gained a rel="nofollow" which is a good thing for user generated content):
```html
<a href="http://www.google.com/" rel="nofollow">
  <img src="https://ssl.gstatic.com/accounts/ui/logo_2x.png"/>
</a>
```

It protects sites from [XSS](http://en.wikipedia.org/wiki/Cross-site_scripting) attacks. There are many [vectors for an XSS attack](https://www.owasp.org/index.php/XSS_Filter_Evasion_Cheat_Sheet) and the best way to mitigate the risk is to sanitize user input against a known safe list of HTML elements and attributes.

You should **always** run bluemonday **after** any other processing.

If you use [blackfriday](https://github.com/russross/blackfriday) or [Pandoc](http://johnmacfarlane.net/pandoc/) then bluemonday should be run after these steps. This ensures that no insecure HTML is introduced later in your process.

bluemonday is heavily inspired by both the [OWASP Java HTML Sanitizer](https://code.google.com/p/owasp-java-html-sanitizer/) and the [HTML Purifier](http://htmlpurifier.org/).

## Technical Summary

Whitelist based, you need to either build a policy describing the HTML elements and attributes to permit (and the `regexp` patterns of attributes), or use one of the supplied policies representing good defaults.

The policy containing the whitelist is applied using a fast non-validating, forward only, token-based parser implemented in the [Go net/html library](https://godoc.org/golang.org/x/net/html) by the core Go team.

We expect to be supplied with well-formatted HTML (closing elements for every applicable open element, nested correctly) and so we do not focus on repairing badly nested or incomplete HTML. We focus on simply ensuring that whatever elements do exist are described in the policy whitelist and that attributes and links are safe for use on your web page. [GIGO](http://en.wikipedia.org/wiki/Garbage_in,_garbage_out) does apply and if you feed it bad HTML bluemonday is not tasked with figuring out how to make it good again.

### Supported Go Versions

bluemonday is regularly tested against Go 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7 and tip.

We do not support Go 1.0 as we depend on `golang.org/x/net/html` which includes a reference to `io.ErrNoProgress` which did not exist in Go 1.0.

## Is it production ready?

*Yes*

We are using bluemonday in production having migrated from the widely used and heavily field tested OWASP Java HTML Sanitizer.

We are passing our extensive test suite (including AntiSamy tests as well as tests for any issues raised). Check for any [unresolved issues](https://github.com/microcosm-cc/bluemonday/issues?page=1&state=open) to see whether anything may be a blocker for you.

We invite pull requests and issues to help us ensure we are offering comprehensive protection against various attacks via user generated content.

## Usage

Install in your `${GOPATH}` using `go get -u github.com/microcosm-cc/bluemonday`

Then call it:
```go
package main

import (
	"fmt"

	"github.com/microcosm-cc/bluemonday"
)

func main() {
	p := bluemonday.UGCPolicy()
	html := p.Sanitize(
		`<a onblur="alert(secret)" href="http://www.google.com">Google</a>`,
	)

	// Output:
	// <a href="http://www.google.com" rel="nofollow">Google</a>
	fmt.Println(html)
}
```

We offer three ways to call Sanitize:
```go
p.Sanitize(string) string
p.SanitizeBytes([]byte) []byte
p.SanitizeReader(io.Reader) bytes.Buffer
```

If you are obsessed about performance, `p.SanitizeReader(r).Bytes()` will return a `[]byte` without performing any unnecessary casting of the inputs or outputs. Though the difference is so negligible you should never need to care.

You can build your own policies:
```go
package main

import (
	"fmt"

	"github.com/microcosm-cc/bluemonday"
)

func main() {
	p := bluemonday.NewPolicy()

	// Require URLs to be parseable by net/url.Parse and either:
	//   mailto: http:// or https://
	p.AllowStandardURLs()

	// We only allow <p> and <a href="">
	p.AllowAttrs("href").OnElements("a")
	p.AllowElements("p")

	html := p.Sanitize(
		`<a onblur="alert(secret)" href="http://www.google.com">Google</a>`,
	)

	// Output:
	// <a href="http://www.google.com">Google</a>
	fmt.Println(html)
}
```

We ship two default policies:

1. `bluemonday.StrictPolicy()` which can be thought of as equivalent to stripping all HTML elements and their attributes as it has nothing on it's whitelist. An example usage scenario would be blog post titles where HTML tags are not expected at all and if they are then the elements *and* the content of the elements should be stripped. This is a *very* strict policy.
2. `bluemonday.UGCPolicy()` which allows a broad selection of HTML elements and attributes that are safe for user generated content. Note that this policy does *not* whitelist iframes, object, embed, styles, script, etc. An example usage scenario would be blog post bodies where a variety of formatting is expected along with the potential for TABLEs and IMGs.

## Policy Building

The essence of building a policy is to determine which HTML elements and attributes are considered safe for your scenario. OWASP provide an [XSS prevention cheat sheet](https://www.owasp.org/index.php/XSS_(Cross_Site_Scripting)_Prevention_Cheat_Sheet) to help explain the risks, but essentially:

1. Avoid anything other than the standard HTML elements
1. Avoid `script`, `style`, `iframe`, `object`, `embed`, `base` elements that allow code to be executed by the client or third party content to be included that can execute code
1. Avoid anything other than plain HTML attributes with values matched to a regexp

Basically, you should be able to describe what HTML is fine for your scenario. If you do not have confidence that you can describe your policy please consider using one of the shipped policies such as `bluemonday.UGCPolicy()`.

To create a new policy:
```go
p := bluemonday.NewPolicy()
```

To add elements to a policy either add just the elements:
```go
p.AllowElements("b", "strong")
```

Or add elements as a virtue of adding an attribute:
```go
// Not the recommended pattern, see the recommendation on using .Matching() below
p.AllowAttrs("nowrap").OnElements("td", "th")
```

Attributes can either be added to all elements:
```go
p.AllowAttrs("dir").Matching(regexp.MustCompile("(?i)rtl|ltr")).Globally()
```

Or attributes can be added to specific elements:
```go
// Not the recommended pattern, see the recommendation on using .Matching() below
p.AllowAttrs("value").OnElements("li")
```

It is **always** recommended that an attribute be made to match a pattern. XSS in HTML attributes is very easy otherwise:
```go
// \p{L} matches unicode letters, \p{N} matches unicode numbers
p.AllowAttrs("title").Matching(regexp.MustCompile(`[\p{L}\p{N}\s\-_',:\[\]!\./\\\(\)&]*`)).Globally()
```

You can stop at any time and call .Sanitize():
```go
// string htmlIn passed in from a HTTP POST
htmlOut := p.Sanitize(htmlIn)
```

And you can take any existing policy and extend it:
```go
p := bluemonday.UGCPolicy()
p.AllowElements("fieldset", "select", "option")
```

### Links

Links are difficult beasts to sanitise safely and also one of the biggest attack vectors for malicious content.

It is possible to do this:
```go
p.AllowAttrs("href").Matching(regexp.MustCompile(`(?i)mailto|https?`)).OnElements("a")
```

But that will not protect you as the regular expression is insufficient in this case to have prevented a malformed value doing something unexpected.

We provide some additional global options for safely working with links.

`RequireParseableURLs` will ensure that URLs are parseable by Go's `net/url` package:
```go
p.RequireParseableURLs(true)
```

If you have enabled parseable URLs then the following option will `AllowRelativeURLs`. By default this is disabled (bluemonday is a whitelist tool... you need to explicitly tell us to permit things) and when disabled it will prevent all local and scheme relative URLs (i.e. `href="localpage.html"`, `href="../home.html"` and even `href="//www.google.com"` are relative):
```go
p.AllowRelativeURLs(true)
```

If you have enabled parseable URLs then you can whitelist the schemes (commonly called protocol when thinking of `http` and `https`) that are permitted. Bear in mind that allowing relative URLs in the above option will allow for a blank scheme:
```go
p.AllowURLSchemes("mailto", "http", "https")
```

Regardless of whether you have enabled parseable URLs, you can force all URLs to have a rel="nofollow" attribute. This will be added if it does not exist, but only when the `href` is valid:
```go
// This applies to "a" "area" "link" elements that have a "href" attribute
p.RequireNoFollowOnLinks(true)
```

We provide a convenience method that applies all of the above, but you will still need to whitelist the linkable elements for the URL rules to be applied to:
```go
p.AllowStandardURLs()
p.AllowAttrs("cite").OnElements("blockquote", "q")
p.AllowAttrs("href").OnElements("a", "area")
p.AllowAttrs("src").OnElements("img")
```

An additional complexity regarding links is the data URI as defined in [RFC2397](http://tools.ietf.org/html/rfc2397). The data URI allows for images to be served inline using this format:

```html
<img src="data:image/webp;base64,UklGRh4AAABXRUJQVlA4TBEAAAAvAAAAAAfQ//73v/+BiOh/AAA=">
```

We have provided a helper to verify the mimetype followed by base64 content of data URIs links:

```go
p.AllowDataURIImages()
```

That helper will enable GIF, JPEG, PNG and WEBP images.

It should be noted that there is a potential [security](http://palizine.plynt.com/issues/2010Oct/bypass-xss-filters/) [risk](https://capec.mitre.org/data/definitions/244.html) with the use of data URI links. You should only enable data URI links if you already trust the content.

We also have some features to help deal with user generated content:
```go
p.AddTargetBlankToFullyQualifiedLinks(true)
```

This will ensure that anchor `<a href="" />` links that are fully qualified (the href destination includes a host name) will get `target="_blank"` added to them.

Additionally any link that has `target="_blank"` after the policy has been applied will also have the `rel` attribute adjusted to add `noopener`. This means a link may start like `<a href="//host/path"/>` and will end up as `<a href="//host/path" rel="noopener" target="_blank">`. It is important to note that the addition of `noopener` is a security feature and not an issue. There is an unfortunate feature to browsers that a browser window opened as a result of `target="_blank"` can still control the opener (your web page) and this protects against that. The background to this can be found here: [https://dev.to/ben/the-targetblank-vulnerability-by-example](https://dev.to/ben/the-targetblank-vulnerability-by-example)

### Policy Building Helpers

We also bundle some helpers to simplify policy building:
```go

// Permits the "dir", "id", "lang", "title" attributes globally
p.AllowStandardAttributes()

// Permits the "img" element and it's standard attributes
p.AllowImages()

// Permits ordered and unordered lists, and also definition lists
p.AllowLists()

// Permits HTML tables and all applicable elements and non-styling attributes
p.AllowTables()
```

### Invalid Instructions

The following are invalid:
```go
// This does not say where the attributes are allowed, you need to add
// .Globally() or .OnElements(...)
// This will be ignored without error.
p.AllowAttrs("value")

// This does not say where the attributes are allowed, you need to add
// .Globally() or .OnElements(...)
// This will be ignored without error.
p.AllowAttrs(
	"type",
).Matching(
	regexp.MustCompile("(?i)^(circle|disc|square|a|A|i|I|1)$"),
)
```

Both examples exhibit the same issue, they declare attributes but do not then specify whether they are whitelisted globally or only on specific elements (and which elements). Attributes belong to one or more elements, and the policy needs to declare this.

## Limitations

We are not yet including any tools to help whitelist and sanitize CSS. Which means that unless you wish to do the heavy lifting in a single regular expression (inadvisable), **you should not allow the "style" attribute anywhere**.

It is not the job of bluemonday to fix your bad HTML, it is merely the job of bluemonday to prevent malicious HTML getting through. If you have mismatched HTML elements, or non-conforming nesting of elements, those will remain. But if you have well-structured HTML bluemonday will not break it.

## TODO

* Add support for CSS sanitisation to allow some CSS properties based on a whitelist, possibly using the [Gorilla CSS3 scanner](http://www.gorillatoolkit.org/pkg/css/scanner)
* Investigate whether devs want to blacklist elements and attributes. This would allow devs to take an existing policy (such as the `bluemonday.UGCPolicy()` ) that encapsulates 90% of what they're looking for but does more than they need, and to remove the extra things they do not want to make it 100% what they want
* Investigate whether devs want a validating HTML mode, in which the HTML elements are not just transformed into a balanced tree (every start tag has a closing tag at the correct depth) but also that elements and character data appear only in their allowed context (i.e. that a `table` element isn't a descendent of a `caption`, that `colgroup`, `thead`, `tbody`, `tfoot` and `tr` are permitted, and that character data is not permitted)

## Development

If you have cloned this repo you will probably need the dependency:

`go get golang.org/x/net/html`

Gophers can use their familiar tools:

`go build`

`go test`

I personally use a Makefile as it spares typing the same args over and over whilst providing consistency for those of us who jump from language to language and enjoy just typing `make` in a project directory and watch magic happen.

`make` will build, vet, test and install the library.

`make clean` will remove the library from a *single* `${GOPATH}/pkg` directory tree

`make test` will run the tests

`make cover` will run the tests and *open a browser window* with the coverage report

`make lint` will run golint (install via `go get github.com/golang/lint/golint`)

## Long term goals

1. Open the code to adversarial peer review similar to the [Attack Review Ground Rules](https://code.google.com/p/owasp-java-html-sanitizer/wiki/AttackReviewGroundRules)
1. Raise funds and pay for an external security review
Core is a lightweight wrapper of sql.DB.

[![CircleCI](https://circleci.com/gh/go-xorm/core/tree/master.svg?style=svg)](https://circleci.com/gh/go-xorm/core/tree/master)

# Open
```Go
db, _ := core.Open(db, connstr)
```

# SetMapper
```Go
db.SetMapper(SameMapper())
```

## Scan usage

### Scan
```Go
rows, _ := db.Query()
for rows.Next() {
    rows.Scan()
}
```

### ScanMap
```Go
rows, _ := db.Query()
for rows.Next() {
    rows.ScanMap()
```

### ScanSlice

You can use `[]string`, `[][]byte`, `[]interface{}`, `[]*string`, `[]sql.NullString` to ScanSclice. Notice, slice's length should be equal or less than select columns.

```Go
rows, _ := db.Query()
cols, _ := rows.Columns()
for rows.Next() {
    var s = make([]string, len(cols))
    rows.ScanSlice(&s)
}
```

```Go
rows, _ := db.Query()
cols, _ := rows.Columns()
for rows.Next() {
    var s = make([]*string, len(cols))
    rows.ScanSlice(&s)
}
```

### ScanStruct
```Go
rows, _ := db.Query()
for rows.Next() {
    rows.ScanStructByName()
    rows.ScanStructByIndex()
}
```

## Query usage
```Go
rows, err := db.Query("select * from table where name = ?", name)

user = User{
    Name:"lunny",
}
rows, err := db.QueryStruct("select * from table where name = ?Name",
            &user)

var user = map[string]interface{}{
    "name": "lunny",
}
rows, err = db.QueryMap("select * from table where name = ?name",
            &user)
```

## QueryRow usage
```Go
row := db.QueryRow("select * from table where name = ?", name)

user = User{
    Name:"lunny",
}
row := db.QueryRowStruct("select * from table where name = ?Name",
            &user)

var user = map[string]interface{}{
    "name": "lunny",
}
row = db.QueryRowMap("select * from table where name = ?name",
            &user)
```

## Exec usage
```Go
db.Exec("insert into user (`name`, title, age, alias, nick_name,created) values (?,?,?,?,?,?)", name, title, age, alias...)

user = User{
    Name:"lunny",
    Title:"test",
    Age: 18,
}
result, err = db.ExecStruct("insert into user (`name`, title, age, alias, nick_name,created) values (?Name,?Title,?Age,?Alias,?NickName,?Created)",
            &user)

var user = map[string]interface{}{
    "Name": "lunny",
    "Title": "test",
    "Age": 18,
}
result, err = db.ExecMap("insert into user (`name`, title, age, alias, nick_name,created) values (?Name,?Title,?Age,?Alias,?NickName,?Created)",
            &user)
```# SQL builder

[![CircleCI](https://circleci.com/gh/go-xorm/builder/tree/master.svg?style=svg)](https://circleci.com/gh/go-xorm/builder/tree/master)

Package builder is a lightweight and fast SQL builder for Go and XORM.

Make sure you have installed Go 1.1+ and then:

    go get github.com/go-xorm/builder

# Insert

```Go
sql, args, err := Insert(Eq{"c": 1, "d": 2}).Into("table1").ToSQL()
```

# Select

```Go
sql, args, err := Select("c, d").From("table1").Where(Eq{"a": 1}).ToSQL()

sql, args, err = Select("c, d").From("table1").LeftJoin("table2", Eq{"table1.id": 1}.And(Lt{"table2.id": 3})).
		RightJoin("table3", "table2.id = table3.tid").Where(Eq{"a": 1}).ToSQL()
```

# Update

```Go
sql, args, err := Update(Eq{"a": 2}).From("table1").Where(Eq{"a": 1}).ToSQL()
```

# Delete

```Go
sql, args, err := Delete(Eq{"a": 1}).From("table1").ToSQL()
```

# Conditions

* `Eq` is a redefine of a map, you can give one or more conditions to `Eq`

```Go
import . "github.com/go-xorm/builder"

sql, args, _ := ToSQL(Eq{"a":1})
// a=? [1]
sql, args, _ := ToSQL(Eq{"b":"c"}.And(Eq{"c": 0}))
// b=? AND c=? ["c", 0]
sql, args, _ := ToSQL(Eq{"b":"c", "c":0})
// b=? AND c=? ["c", 0]
sql, args, _ := ToSQL(Eq{"b":"c"}.Or(Eq{"b":"d"}))
// b=? OR b=? ["c", "d"]
sql, args, _ := ToSQL(Eq{"b": []string{"c", "d"}})
// b IN (?,?) ["c", "d"]
sql, args, _ := ToSQL(Eq{"b": 1, "c":[]int{2, 3}})
// b=? AND c IN (?,?) [1, 2, 3]
```

* `Neq` is the same to `Eq`

```Go
import . "github.com/go-xorm/builder"

sql, args, _ := ToSQL(Neq{"a":1})
// a<>? [1]
sql, args, _ := ToSQL(Neq{"b":"c"}.And(Neq{"c": 0}))
// b<>? AND c<>? ["c", 0]
sql, args, _ := ToSQL(Neq{"b":"c", "c":0})
// b<>? AND c<>? ["c", 0]
sql, args, _ := ToSQL(Neq{"b":"c"}.Or(Neq{"b":"d"}))
// b<>? OR b<>? ["c", "d"]
sql, args, _ := ToSQL(Neq{"b": []string{"c", "d"}})
// b NOT IN (?,?) ["c", "d"]
sql, args, _ := ToSQL(Neq{"b": 1, "c":[]int{2, 3}})
// b<>? AND c NOT IN (?,?) [1, 2, 3]
```

* `Gt`, `Gte`, `Lt`, `Lte`

```Go
import . "github.com/go-xorm/builder"

sql, args, _ := ToSQL(Gt{"a", 1}.And(Gte{"b", 2}))
// a>? AND b>=? [1, 2]
sql, args, _ := ToSQL(Lt{"a", 1}.Or(Lte{"b", 2}))
// a<? OR b<=? [1, 2]
```

* `Like`

```Go
import . "github.com/go-xorm/builder"

sql, args, _ := ToSQL(Like{"a", "c"})
// a LIKE ? [%c%]
```

* `Expr` you can customerize your sql with `Expr`

```Go
import . "github.com/go-xorm/builder"

sql, args, _ := ToSQL(Expr("a = ? ", 1))
// a = ? [1]
sql, args, _ := ToSQL(Eq{"a": Expr("select id from table where c = ?", 1)})
// a=(select id from table where c = ?) [1]
```

* `In` and `NotIn`

```Go
import . "github.com/go-xorm/builder"

sql, args, _ := ToSQL(In("a", 1, 2, 3))
// a IN (?,?,?) [1,2,3]
sql, args, _ := ToSQL(In("a", []int{1, 2, 3}))
// a IN (?,?,?) [1,2,3]
sql, args, _ := ToSQL(In("a", Expr("select id from b where c = ?", 1))))
// a IN (select id from b where c = ?) [1]
```

* `IsNull` and `NotNull`

```Go
import . "github.com/go-xorm/builder"

sql, args, _ := ToSQL(IsNull{"a"})
// a IS NULL []
sql, args, _ := ToSQL(NotNull{"b"})
	// b IS NOT NULL []
```

* `And(conds ...Cond)`, And can connect one or more condtions via And

```Go
import . "github.com/go-xorm/builder"

sql, args, _ := ToSQL(And(Eq{"a":1}, Like{"b", "c"}, Neq{"d", 2}))
// a=? AND b LIKE ? AND d<>? [1, %c%, 2]
```

* `Or(conds ...Cond)`, Or can connect one or more conditions via Or

```Go
import . "github.com/go-xorm/builder"

sql, args, _ := ToSQL(Or(Eq{"a":1}, Like{"b", "c"}, Neq{"d", 2}))
// a=? OR b LIKE ? OR d<>? [1, %c%, 2]
sql, args, _ := ToSQL(Or(Eq{"a":1}, And(Like{"b", "c"}, Neq{"d", 2})))
// a=? OR (b LIKE ? AND d<>?) [1, %c%, 2]
```

* `Between`

```Go
import . "github.com/go-xorm/builder"

sql, args, _ := ToSQL(Between{"a", 1, 2})
// a BETWEEN 1 AND 2
```

* Define yourself conditions

Since `Cond` is an interface.

```Go
type Cond interface {
	WriteTo(Writer) error
	And(...Cond) Cond
	Or(...Cond) Cond
	IsValid() bool
}
```

You can define yourself conditions and compose with other `Cond`.# xorm

[English](https://github.com/go-xorm/xorm/blob/master/README.md)

xorm是一个简单而强大的Go语言ORM库. 通过它可以使数据库操作非常简便。

[![CircleCI](https://circleci.com/gh/go-xorm/xorm.svg?style=shield)](https://circleci.com/gh/go-xorm/xorm) [![codecov](https://codecov.io/gh/go-xorm/xorm/branch/master/graph/badge.svg)](https://codecov.io/gh/go-xorm/xorm)
[![](https://goreportcard.com/badge/github.com/go-xorm/xorm)](https://goreportcard.com/report/github.com/go-xorm/xorm)
[![Join the chat at https://img.shields.io/discord/323460943201959939.svg](https://img.shields.io/discord/323460943201959939.svg)](https://discord.gg/HuR2CF3)

## 特性

* 支持Struct和数据库表之间的灵活映射，并支持自动同步

* 事务支持

* 同时支持原始SQL语句和ORM操作的混合执行

* 使用连写来简化调用

* 支持使用Id, In, Where, Limit, Join, Having, Table, Sql, Cols等函数和结构体等方式作为条件

* 支持级联加载Struct

* 支持缓存

* 支持根据数据库自动生成xorm的结构体

* 支持记录版本（即乐观锁）

* 内置SQL Builder支持

## 驱动支持

目前支持的Go数据库驱动和对应的数据库如下：

* Mysql: [github.com/go-sql-driver/mysql](https://github.com/go-sql-driver/mysql)

* MyMysql: [github.com/ziutek/mymysql/godrv](https://github.com/ziutek/mymysql/godrv)

* Postgres: [github.com/lib/pq](https://github.com/lib/pq)

* Tidb: [github.com/pingcap/tidb](https://github.com/pingcap/tidb)

* SQLite: [github.com/mattn/go-sqlite3](https://github.com/mattn/go-sqlite3)

* MsSql: [github.com/denisenkom/go-mssqldb](https://github.com/denisenkom/go-mssqldb)

* MsSql: [github.com/lunny/godbc](https://github.com/lunny/godbc)

* Oracle: [github.com/mattn/go-oci8](https://github.com/mattn/go-oci8) (试验性支持)

## 更新日志

* **v0.6.3**
    * 合并单元测试到主工程
    * 新增`Exist`方法
    * 新增`SumInt`方法
    * Mysql新增读取和创建字段注释支持
    * 新增`SetConnMaxLifetime`方法
    * 修正了时间相关的Bug
    * 修复了一些其它Bug

* **v0.6.2**
    * 重构Tag解析方式
    * Get方法新增类似Scan的特性
    * 新增 QueryString 方法

* **v0.6.0**
    * 去除对 ql 的支持
    * 新增条件查询分析器 [github.com/go-xorm/builder](https://github.com/go-xorm/builder), 从因此 `Where, And, Or` 函数
将可以用 `builder.Cond` 作为条件组合
    * 新增 Sum, SumInt, SumInt64 和 NotIn 函数
    * Bug修正

* **v0.5.0**
    * logging接口进行不兼容改变
    * Bug修正

[更多更新日志...](https://github.com/go-xorm/manual-zh-CN/tree/master/chapter-16)

## 安装

	go get github.com/go-xorm/xorm

## 文档

* [操作指南](http://xorm.io/docs)

* [GoWalker代码文档](http://gowalker.org/github.com/go-xorm/xorm)

* [Godoc代码文档](http://godoc.org/github.com/go-xorm/xorm)

# 快速开始

* 第一步创建引擎，driverName, dataSourceName和database/sql接口相同

```Go
engine, err := xorm.NewEngine(driverName, dataSourceName)
```

* 定义一个和表同步的结构体，并且自动同步结构体到数据库

```Go
type User struct {
    Id int64
    Name string
    Salt string
    Age int
    Passwd string `xorm:"varchar(200)"`
    Created time.Time `xorm:"created"`
    Updated time.Time `xorm:"updated"`
}

err := engine.Sync2(new(User))
```

* 创建Engine组

```Go
dataSourceNameSlice := []string{masterDataSourceName, slave1DataSourceName, slave2DataSourceName}
engineGroup, err := xorm.NewEngineGroup(driverName, dataSourceNameSlice)
```

```Go
masterEngine, err := xorm.NewEngine(driverName, masterDataSourceName)
slave1Engine, err := xorm.NewEngine(driverName, slave1DataSourceName)
slave2Engine, err := xorm.NewEngine(driverName, slave2DataSourceName)
engineGroup, err := xorm.NewEngineGroup(masterEngine, []*Engine{slave1Engine, slave2Engine})
```

所有使用 `engine` 都可以简单的用 `engineGroup` 来替换。

* `Query` 最原始的也支持SQL语句查询，返回的结果类型为 []map[string][]byte。`QueryString` 返回 []map[string]string, `QueryInterface` 返回 `[]map[string]interface{}`.

```Go
results, err := engine.Query("select * from user")
results, err := engine.Where("a = 1").Query()

results, err := engine.QueryString("select * from user")
results, err := engine.Where("a = 1").QueryString()

results, err := engine.QueryInterface("select * from user")
results, err := engine.Where("a = 1").QueryInterface()
```

* `Exec` 执行一个SQL语句

```Go
affected, err := engine.Exec("update user set age = ? where name = ?", age, name)
```

* `Insert` 插入一条或者多条记录

```Go
affected, err := engine.Insert(&user)
// INSERT INTO struct () values ()

affected, err := engine.Insert(&user1, &user2)
// INSERT INTO struct1 () values ()
// INSERT INTO struct2 () values ()

affected, err := engine.Insert(&users)
// INSERT INTO struct () values (),(),()

affected, err := engine.Insert(&user1, &users)
// INSERT INTO struct1 () values ()
// INSERT INTO struct2 () values (),(),()
```

* `Get` 查询单条记录

```Go
has, err := engine.Get(&user)
// SELECT * FROM user LIMIT 1

has, err := engine.Where("name = ?", name).Desc("id").Get(&user)
// SELECT * FROM user WHERE name = ? ORDER BY id DESC LIMIT 1

var name string
has, err := engine.Where("id = ?", id).Cols("name").Get(&name)
// SELECT name FROM user WHERE id = ?

var id int64
has, err := engine.Where("name = ?", name).Cols("id").Get(&id)
has, err := engine.SQL("select id from user").Get(&id)
// SELECT id FROM user WHERE name = ?

var valuesMap = make(map[string]string)
has, err := engine.Where("id = ?", id).Get(&valuesMap)
// SELECT * FROM user WHERE id = ?

var valuesSlice = make([]interface{}, len(cols))
has, err := engine.Where("id = ?", id).Cols(cols...).Get(&valuesSlice)
// SELECT col1, col2, col3 FROM user WHERE id = ?
```

* `Exist` 检测记录是否存在

```Go
has, err := testEngine.Exist(new(RecordExist))
// SELECT * FROM record_exist LIMIT 1

has, err = testEngine.Exist(&RecordExist{
		Name: "test1",
	})
// SELECT * FROM record_exist WHERE name = ? LIMIT 1

has, err = testEngine.Where("name = ?", "test1").Exist(&RecordExist{})
// SELECT * FROM record_exist WHERE name = ? LIMIT 1

has, err = testEngine.SQL("select * from record_exist where name = ?", "test1").Exist()
// select * from record_exist where name = ?

has, err = testEngine.Table("record_exist").Exist()
// SELECT * FROM record_exist LIMIT 1

has, err = testEngine.Table("record_exist").Where("name = ?", "test1").Exist()
// SELECT * FROM record_exist WHERE name = ? LIMIT 1
```

* `Find` 查询多条记录，当然可以使用Join和extends来组合使用

```Go
var users []User
err := engine.Where("name = ?", name).And("age > 10").Limit(10, 0).Find(&users)
// SELECT * FROM user WHERE name = ? AND age > 10 limit 10 offset 0

type Detail struct {
    Id int64
    UserId int64 `xorm:"index"`
}

type UserDetail struct {
    User `xorm:"extends"`
    Detail `xorm:"extends"`
}

var users []UserDetail
err := engine.Table("user").Select("user.*, detail.*")
    Join("INNER", "detail", "detail.user_id = user.id").
    Where("user.name = ?", name).Limit(10, 0).
    Find(&users)
// SELECT user.*, detail.* FROM user INNER JOIN detail WHERE user.name = ? limit 10 offset 0
```

* `Iterate` 和 `Rows` 根据条件遍历数据库，可以有两种方式: Iterate and Rows

```Go
err := engine.Iterate(&User{Name:name}, func(idx int, bean interface{}) error {
    user := bean.(*User)
    return nil
})
// SELECT * FROM user

err := engine.BufferSize(100).Iterate(&User{Name:name}, func(idx int, bean interface{}) error {
    user := bean.(*User)
    return nil
})
// SELECT * FROM user Limit 0, 100
// SELECT * FROM user Limit 101, 100

rows, err := engine.Rows(&User{Name:name})
// SELECT * FROM user
defer rows.Close()
bean := new(Struct)
for rows.Next() {
    err = rows.Scan(bean)
}
```

* `Update` 更新数据，除非使用Cols,AllCols函数指明，默认只更新非空和非0的字段

```Go
affected, err := engine.ID(1).Update(&user)
// UPDATE user SET ... Where id = ?

affected, err := engine.Update(&user, &User{Name:name})
// UPDATE user SET ... Where name = ?

var ids = []int64{1, 2, 3}
affected, err := engine.In(ids).Update(&user)
// UPDATE user SET ... Where id IN (?, ?, ?)

// force update indicated columns by Cols
affected, err := engine.ID(1).Cols("age").Update(&User{Name:name, Age: 12})
// UPDATE user SET age = ?, updated=? Where id = ?

// force NOT update indicated columns by Omit
affected, err := engine.ID(1).Omit("name").Update(&User{Name:name, Age: 12})
// UPDATE user SET age = ?, updated=? Where id = ?

affected, err := engine.ID(1).AllCols().Update(&user)
// UPDATE user SET name=?,age=?,salt=?,passwd=?,updated=? Where id = ?
```

* `Delete` 删除记录，需要注意，删除必须至少有一个条件，否则会报错。要清空数据库可以用EmptyTable

```Go
affected, err := engine.Where(...).Delete(&user)
// DELETE FROM user Where ...

affected, err := engine.ID(2).Delete(&user)
// DELETE FROM user Where id = ?
```

* `Count` 获取记录条数

```Go
counts, err := engine.Count(&user)
// SELECT count(*) AS total FROM user
```

* `Sum` 求和函数

```Go
agesFloat64, err := engine.Sum(&user, "age")
// SELECT sum(age) AS total FROM user

agesInt64, err := engine.SumInt(&user, "age")
// SELECT sum(age) AS total FROM user

sumFloat64Slice, err := engine.Sums(&user, "age", "score")
// SELECT sum(age), sum(score) FROM user

sumInt64Slice, err := engine.SumsInt(&user, "age", "score")
// SELECT sum(age), sum(score) FROM user
```

* 条件编辑器

```Go
err := engine.Where(builder.NotIn("a", 1, 2).And(builder.In("b", "c", "d", "e"))).Find(&users)
// SELECT id, name ... FROM user WHERE a NOT IN (?, ?) AND b IN (?, ?, ?)
```

* 在一个Go程中多次操作数据库，但没有事务

```Go
session := engine.NewSession()
defer session.Close()

user1 := Userinfo{Username: "xiaoxiao", Departname: "dev", Alias: "lunny", Created: time.Now()}
if _, err := session.Insert(&user1); err != nil {
    return err
}

user2 := Userinfo{Username: "yyy"}
if _, err := session.Where("id = ?", 2).Update(&user2); err != nil {
    return err
}

if _, err := session.Exec("delete from userinfo where username = ?", user2.Username); err != nil {
    return err
}

return nil
```

* 在一个Go程中有事务

```Go
session := engine.NewSession()
defer session.Close()

// add Begin() before any action
if err := session.Begin(); err != nil {
    // if returned then will rollback automatically
    return err
}

user1 := Userinfo{Username: "xiaoxiao", Departname: "dev", Alias: "lunny", Created: time.Now()}
if _, err := session.Insert(&user1); err != nil {
    return err
}

user2 := Userinfo{Username: "yyy"}
if _, err := session.Where("id = ?", 2).Update(&user2); err != nil {
    return err
}

if _, err := session.Exec("delete from userinfo where username = ?", user2.Username); err != nil {
    return err
}

// add Commit() after all actions
return session.Commit()
```

# 案例

* [Go语言中文网](http://studygolang.com/) - [github.com/studygolang/studygolang](https://github.com/studygolang/studygolang)

* [Gitea](http://gitea.io) - [github.com/go-gitea/gitea](http://github.com/go-gitea/gitea)

* [Gogs](http://try.gogits.org) - [github.com/gogits/gogs](http://github.com/gogits/gogs)

* [grafana](https://grafana.com/) - [github.com/grafana/grafana](http://github.com/grafana/grafana)

* [github.com/m3ng9i/qreader](https://github.com/m3ng9i/qreader)

* [Wego](http://github.com/go-tango/wego)

* [Docker.cn](https://docker.cn/)

* [Xorm Adapter](https://github.com/casbin/xorm-adapter) for [Casbin](https://github.com/casbin/casbin) - [github.com/casbin/xorm-adapter](https://github.com/casbin/xorm-adapter)

* [Gowalker](http://gowalker.org) - [github.com/Unknwon/gowalker](http://github.com/Unknwon/gowalker)

* [Gobuild.io](http://gobuild.io) - [github.com/shxsun/gobuild](http://github.com/shxsun/gobuild)

* [Sudo China](http://sudochina.com) - [github.com/insionng/toropress](http://github.com/insionng/toropress)

* [Godaily](http://godaily.org) - [github.com/govc/godaily](http://github.com/govc/godaily)

* [YouGam](http://www.yougam.com/)

* [GoCMS - github.com/zzboy/GoCMS](https://github.com/zzdboy/GoCMS)

* [GoBBS - gobbs.domolo.com](http://gobbs.domolo.com/)

* [go-blog](http://wangcheng.me) - [github.com/easykoo/go-blog](https://github.com/easykoo/go-blog)

## 讨论

请加入QQ群：280360085 进行讨论。

## 贡献

如果您也想为Xorm贡献您的力量，请查看 [CONTRIBUTING](https://github.com/go-xorm/xorm/blob/master/CONTRIBUTING.md)

## LICENSE

BSD License
[http://creativecommons.org/licenses/BSD/](http://creativecommons.org/licenses/BSD/)
[中文](https://github.com/go-xorm/xorm/blob/master/README_CN.md)

Xorm is a simple and powerful ORM for Go.

[![CircleCI](https://circleci.com/gh/go-xorm/xorm.svg?style=shield)](https://circleci.com/gh/go-xorm/xorm) [![codecov](https://codecov.io/gh/go-xorm/xorm/branch/master/graph/badge.svg)](https://codecov.io/gh/go-xorm/xorm)
[![](https://goreportcard.com/badge/github.com/go-xorm/xorm)](https://goreportcard.com/report/github.com/go-xorm/xorm) 
[![Join the chat at https://img.shields.io/discord/323460943201959939.svg](https://img.shields.io/discord/323460943201959939.svg)](https://discord.gg/HuR2CF3)

# Features

* Struct <-> Table Mapping Support

* Chainable APIs

* Transaction Support

* Both ORM and raw SQL operation Support

* Sync database schema Support

* Query Cache speed up

* Database Reverse support, See [Xorm Tool README](https://github.com/go-xorm/cmd/blob/master/README.md)

* Simple cascade loading support

* Optimistic Locking support

* SQL Builder support via [github.com/go-xorm/builder](https://github.com/go-xorm/builder)

* Automatical Read/Write seperatelly

# Drivers Support

Drivers for Go's sql package which currently support database/sql includes:

* Mysql: [github.com/go-sql-driver/mysql](https://github.com/go-sql-driver/mysql)

* MyMysql: [github.com/ziutek/mymysql/godrv](https://github.com/ziutek/mymysql/tree/master/godrv)

* Postgres: [github.com/lib/pq](https://github.com/lib/pq)

* Tidb: [github.com/pingcap/tidb](https://github.com/pingcap/tidb)

* SQLite: [github.com/mattn/go-sqlite3](https://github.com/mattn/go-sqlite3)

* MsSql: [github.com/denisenkom/go-mssqldb](https://github.com/denisenkom/go-mssqldb)

* Oracle: [github.com/mattn/go-oci8](https://github.com/mattn/go-oci8) (experiment)

# Changelog

* **v0.6.4**
    * Automatical Read/Write seperatelly
    * Query/QueryString/QueryInterface and action with Where/And
    * Get support non-struct variables
    * BufferSize on Iterate
    * fix some other bugs.

* **v0.6.3**
    * merge tests to main project
    * add `Exist` function
    * add `SumInt` function
    * Mysql now support read and create column comment.
    * fix time related bugs.
    * fix some other bugs.

* **v0.6.2**
    * refactor tag parse methods
    * add Scan features to Get
    * add QueryString method

[More changes ...](https://github.com/go-xorm/manual-en-US/tree/master/chapter-16)

# Installation

	go get github.com/go-xorm/xorm

# Documents

* [Manual](http://xorm.io/docs)

* [GoDoc](http://godoc.org/github.com/go-xorm/xorm)

* [GoWalker](http://gowalker.org/github.com/go-xorm/xorm)

# Quick Start

* Create Engine

```Go
engine, err := xorm.NewEngine(driverName, dataSourceName)
```

* Define a struct and Sync2 table struct to database

```Go
type User struct {
    Id int64
    Name string
    Salt string
    Age int
    Passwd string `xorm:"varchar(200)"`
    Created time.Time `xorm:"created"`
    Updated time.Time `xorm:"updated"`
}

err := engine.Sync2(new(User))
```

* Create Engine Group

```Go
dataSourceNameSlice := []string{masterDataSourceName, slave1DataSourceName, slave2DataSourceName}
engineGroup, err := xorm.NewEngineGroup(driverName, dataSourceNameSlice)
```

```Go
masterEngine, err := xorm.NewEngine(driverName, masterDataSourceName)
slave1Engine, err := xorm.NewEngine(driverName, slave1DataSourceName)
slave2Engine, err := xorm.NewEngine(driverName, slave2DataSourceName)
engineGroup, err := xorm.NewEngineGroup(masterEngine, []*Engine{slave1Engine, slave2Engine})
```

Then all place where `engine` you can just use `engineGroup`.

* `Query` runs a SQL string, the returned results is `[]map[string][]byte`, `QueryString` returns `[]map[string]string`, `QueryInterface` returns `[]map[string]interface{}`.

```Go
results, err := engine.Query("select * from user")
results, err := engine.Where("a = 1").Query()

results, err := engine.QueryString("select * from user")
results, err := engine.Where("a = 1").QueryString()

results, err := engine.QueryInterface("select * from user")
results, err := engine.Where("a = 1").QueryInterface()
```

* `Exec` runs a SQL string, it returns `affected` and `error`

```Go
affected, err := engine.Exec("update user set age = ? where name = ?", age, name)
```

* `Insert` one or multiple records to database

```Go
affected, err := engine.Insert(&user)
// INSERT INTO struct () values ()

affected, err := engine.Insert(&user1, &user2)
// INSERT INTO struct1 () values ()
// INSERT INTO struct2 () values ()

affected, err := engine.Insert(&users)
// INSERT INTO struct () values (),(),()

affected, err := engine.Insert(&user1, &users)
// INSERT INTO struct1 () values ()
// INSERT INTO struct2 () values (),(),()
```

* `Get` query one record from database

```Go
has, err := engine.Get(&user)
// SELECT * FROM user LIMIT 1

has, err := engine.Where("name = ?", name).Desc("id").Get(&user)
// SELECT * FROM user WHERE name = ? ORDER BY id DESC LIMIT 1

var name string
has, err := engine.Where("id = ?", id).Cols("name").Get(&name)
// SELECT name FROM user WHERE id = ?

var id int64
has, err := engine.Where("name = ?", name).Cols("id").Get(&id)
has, err := engine.SQL("select id from user").Get(&id)
// SELECT id FROM user WHERE name = ?

var valuesMap = make(map[string]string)
has, err := engine.Where("id = ?", id).Get(&valuesMap)
// SELECT * FROM user WHERE id = ?

var valuesSlice = make([]interface{}, len(cols))
has, err := engine.Where("id = ?", id).Cols(cols...).Get(&valuesSlice)
// SELECT col1, col2, col3 FROM user WHERE id = ?
```

* `Exist` check if one record exist on table

```Go
has, err := testEngine.Exist(new(RecordExist))
// SELECT * FROM record_exist LIMIT 1

has, err = testEngine.Exist(&RecordExist{
		Name: "test1",
	})
// SELECT * FROM record_exist WHERE name = ? LIMIT 1

has, err = testEngine.Where("name = ?", "test1").Exist(&RecordExist{})
// SELECT * FROM record_exist WHERE name = ? LIMIT 1

has, err = testEngine.SQL("select * from record_exist where name = ?", "test1").Exist()
// select * from record_exist where name = ?

has, err = testEngine.Table("record_exist").Exist()
// SELECT * FROM record_exist LIMIT 1

has, err = testEngine.Table("record_exist").Where("name = ?", "test1").Exist()
// SELECT * FROM record_exist WHERE name = ? LIMIT 1
```

* `Find` query multiple records from database, also you can use join and extends

```Go
var users []User
err := engine.Where("name = ?", name).And("age > 10").Limit(10, 0).Find(&users)
// SELECT * FROM user WHERE name = ? AND age > 10 limit 10 offset 0

type Detail struct {
    Id int64
    UserId int64 `xorm:"index"`
}

type UserDetail struct {
    User `xorm:"extends"`
    Detail `xorm:"extends"`
}

var users []UserDetail
err := engine.Table("user").Select("user.*, detail.*").
    Join("INNER", "detail", "detail.user_id = user.id").
    Where("user.name = ?", name).Limit(10, 0).
    Find(&users)
// SELECT user.*, detail.* FROM user INNER JOIN detail WHERE user.name = ? limit 10 offset 0
```

* `Iterate` and `Rows` query multiple records and record by record handle, there are two methods Iterate and Rows

```Go
err := engine.Iterate(&User{Name:name}, func(idx int, bean interface{}) error {
    user := bean.(*User)
    return nil
})
// SELECT * FROM user

err := engine.BufferSize(100).Iterate(&User{Name:name}, func(idx int, bean interface{}) error {
    user := bean.(*User)
    return nil
})
// SELECT * FROM user Limit 0, 100
// SELECT * FROM user Limit 101, 100

rows, err := engine.Rows(&User{Name:name})
// SELECT * FROM user
defer rows.Close()
bean := new(Struct)
for rows.Next() {
    err = rows.Scan(bean)
}
```

* `Update` update one or more records, default will update non-empty and non-zero fields except when you use Cols, AllCols and so on.

```Go
affected, err := engine.ID(1).Update(&user)
// UPDATE user SET ... Where id = ?

affected, err := engine.Update(&user, &User{Name:name})
// UPDATE user SET ... Where name = ?

var ids = []int64{1, 2, 3}
affected, err := engine.In("id", ids).Update(&user)
// UPDATE user SET ... Where id IN (?, ?, ?)

// force update indicated columns by Cols
affected, err := engine.ID(1).Cols("age").Update(&User{Name:name, Age: 12})
// UPDATE user SET age = ?, updated=? Where id = ?

// force NOT update indicated columns by Omit
affected, err := engine.ID(1).Omit("name").Update(&User{Name:name, Age: 12})
// UPDATE user SET age = ?, updated=? Where id = ?

affected, err := engine.ID(1).AllCols().Update(&user)
// UPDATE user SET name=?,age=?,salt=?,passwd=?,updated=? Where id = ?
```

* `Delete` delete one or more records, Delete MUST have condition

```Go
affected, err := engine.Where(...).Delete(&user)
// DELETE FROM user Where ...

affected, err := engine.ID(2).Delete(&user)
// DELETE FROM user Where id = ?
```

* `Count` count records

```Go
counts, err := engine.Count(&user)
// SELECT count(*) AS total FROM user
```

* `Sum` sum functions

```Go
agesFloat64, err := engine.Sum(&user, "age")
// SELECT sum(age) AS total FROM user

agesInt64, err := engine.SumInt(&user, "age")
// SELECT sum(age) AS total FROM user

sumFloat64Slice, err := engine.Sums(&user, "age", "score")
// SELECT sum(age), sum(score) FROM user

sumInt64Slice, err := engine.SumsInt(&user, "age", "score")
// SELECT sum(age), sum(score) FROM user
```

* Query conditions builder

```Go
err := engine.Where(builder.NotIn("a", 1, 2).And(builder.In("b", "c", "d", "e"))).Find(&users)
// SELECT id, name ... FROM user WHERE a NOT IN (?, ?) AND b IN (?, ?, ?)
```

* Multiple operations in one go routine, no transation here but resue session memory

```Go
session := engine.NewSession()
defer session.Close()

user1 := Userinfo{Username: "xiaoxiao", Departname: "dev", Alias: "lunny", Created: time.Now()}
if _, err := session.Insert(&user1); err != nil {
    return err
}

user2 := Userinfo{Username: "yyy"}
if _, err := session.Where("id = ?", 2).Update(&user2); err != nil {
    return err
}

if _, err := session.Exec("delete from userinfo where username = ?", user2.Username); err != nil {
    return err
}

return nil
```

* Transation should on one go routine. There is transaction and resue session memory

```Go
session := engine.NewSession()
defer session.Close()

// add Begin() before any action
if err := session.Begin(); err != nil {
    // if returned then will rollback automatically
    return err
}

user1 := Userinfo{Username: "xiaoxiao", Departname: "dev", Alias: "lunny", Created: time.Now()}
if _, err := session.Insert(&user1); err != nil {
    return err
}

user2 := Userinfo{Username: "yyy"}
if _, err := session.Where("id = ?", 2).Update(&user2); err != nil {
    return err
}

if _, err := session.Exec("delete from userinfo where username = ?", user2.Username); err != nil {
    return err
}

// add Commit() after all actions
return session.Commit()
```

# Cases

* [studygolang](http://studygolang.com/) - [github.com/studygolang/studygolang](https://github.com/studygolang/studygolang)

* [Gitea](http://gitea.io) - [github.com/go-gitea/gitea](http://github.com/go-gitea/gitea)

* [Gogs](http://try.gogits.org) - [github.com/gogits/gogs](http://github.com/gogits/gogs)

* [grafana](https://grafana.com/) - [github.com/grafana/grafana](http://github.com/grafana/grafana)

* [github.com/m3ng9i/qreader](https://github.com/m3ng9i/qreader)

* [Wego](http://github.com/go-tango/wego)

* [Docker.cn](https://docker.cn/)

* [Xorm Adapter](https://github.com/casbin/xorm-adapter) for [Casbin](https://github.com/casbin/casbin) - [github.com/casbin/xorm-adapter](https://github.com/casbin/xorm-adapter)

* [Gorevel](http://gorevel.cn/) - [github.com/goofcc/gorevel](http://github.com/goofcc/gorevel)

* [Gowalker](http://gowalker.org) - [github.com/Unknwon/gowalker](http://github.com/Unknwon/gowalker)

* [Gobuild.io](http://gobuild.io) - [github.com/shxsun/gobuild](http://github.com/shxsun/gobuild)

* [Sudo China](http://sudochina.com) - [github.com/insionng/toropress](http://github.com/insionng/toropress)

* [Godaily](http://godaily.org) - [github.com/govc/godaily](http://github.com/govc/godaily)

* [YouGam](http://www.yougam.com/)

* [GoCMS - github.com/zzboy/GoCMS](https://github.com/zzdboy/GoCMS)

* [GoBBS - gobbs.domolo.com](http://gobbs.domolo.com/)

* [go-blog](http://wangcheng.me) - [github.com/easykoo/go-blog](https://github.com/easykoo/go-blog)

# Discuss

Please visit [Xorm on Google Groups](https://groups.google.com/forum/#!forum/xorm)

# Contributing

If you want to pull request, please see [CONTRIBUTING](https://github.com/go-xorm/xorm/blob/master/CONTRIBUTING.md)

# LICENSE

 BSD License
 [http://creativecommons.org/licenses/BSD/](http://creativecommons.org/licenses/BSD/)
# UUID package for Go language

[![Build Status](https://travis-ci.org/satori/go.uuid.png?branch=master)](https://travis-ci.org/satori/go.uuid)
[![Coverage Status](https://coveralls.io/repos/github/satori/go.uuid/badge.svg?branch=master)](https://coveralls.io/github/satori/go.uuid)
[![GoDoc](http://godoc.org/github.com/satori/go.uuid?status.png)](http://godoc.org/github.com/satori/go.uuid)

This package provides pure Go implementation of Universally Unique Identifier (UUID). Supported both creation and parsing of UUIDs.

With 100% test coverage and benchmarks out of box.

Supported versions:
* Version 1, based on timestamp and MAC address (RFC 4122)
* Version 2, based on timestamp, MAC address and POSIX UID/GID (DCE 1.1)
* Version 3, based on MD5 hashing (RFC 4122)
* Version 4, based on random numbers (RFC 4122)
* Version 5, based on SHA-1 hashing (RFC 4122)

## Installation

Use the `go` command:

	$ go get github.com/satori/go.uuid

## Requirements

UUID package requires Go >= 1.2.

## Example

```go
package main

import (
	"fmt"
	"github.com/satori/go.uuid"
)

func main() {
	// Creating UUID Version 4
	u1 := uuid.NewV4()
	fmt.Printf("UUIDv4: %s\n", u1)

	// Parsing UUID from string input
	u2, err := uuid.FromString("6ba7b810-9dad-11d1-80b4-00c04fd430c8")
	if err != nil {
		fmt.Printf("Something gone wrong: %s", err)
	}
	fmt.Printf("Successfully parsed: %s", u2)
}
```

## Documentation

[Documentation](http://godoc.org/github.com/satori/go.uuid) is hosted at GoDoc project.

## Links
* [RFC 4122](http://tools.ietf.org/html/rfc4122)
* [DCE 1.1: Authentication and Security Services](http://pubs.opengroup.org/onlinepubs/9696989899/chap5.htm#tagcjh_08_02_01_01)

## Copyright

Copyright (C) 2013-2016 by Maxim Bublis <b@codemonkey.ru>.

UUID package released under MIT License.
See [LICENSE](https://github.com/satori/go.uuid/blob/master/LICENSE) for details.
# crc32
CRC32 hash with x64 optimizations

This package is a drop-in replacement for the standard library `hash/crc32` package, that features SSE 4.2 optimizations on x64 platforms, for a 10x speedup.

[![Build Status](https://travis-ci.org/klauspost/crc32.svg?branch=master)](https://travis-ci.org/klauspost/crc32)

# usage

Install using `go get github.com/klauspost/crc32`. This library is based on Go 1.5 code and requires Go 1.3 or newer.

Replace `import "hash/crc32"` with `import "github.com/klauspost/crc32"` and you are good to go.

# changes
* Oct 20, 2016: Changes have been merged to upstream Go. Package updated to match.
* Dec 4, 2015: Uses the "slice-by-8" trick more extensively, which gives a 1.5 to 2.5x speedup if assembler is unavailable.


# performance

For *Go 1.7* performance is equivalent to the standard library. So if you use this package for Go 1.7 you can switch back.


For IEEE tables (the most common), there is approximately a factor 10 speedup with "CLMUL" (Carryless multiplication) instruction:
```
benchmark            old ns/op     new ns/op     delta
BenchmarkCrc32KB     99955         10258         -89.74%

benchmark            old MB/s     new MB/s     speedup
BenchmarkCrc32KB     327.83       3194.20      9.74x
```

For other tables and "CLMUL"  capable machines the performance is the same as the standard library.

Here are some detailed benchmarks, comparing to go 1.5 standard library with and without assembler enabled.

```
Std:   Standard Go 1.5 library
Crc:   Indicates IEEE type CRC.
40B:   Size of each slice encoded.
NoAsm: Assembler was disabled (ie. not an AMD64 or SSE 4.2+ capable machine).
Castagnoli: Castagnoli CRC type.

BenchmarkStdCrc40B-4            10000000               158 ns/op         252.88 MB/s
BenchmarkCrc40BNoAsm-4          20000000               105 ns/op         377.38 MB/s (slice8)
BenchmarkCrc40B-4               20000000               105 ns/op         378.77 MB/s (slice8)

BenchmarkStdCrc1KB-4              500000              3604 ns/op         284.10 MB/s
BenchmarkCrc1KBNoAsm-4           1000000              1463 ns/op         699.79 MB/s (slice8)
BenchmarkCrc1KB-4                3000000               396 ns/op        2583.69 MB/s (asm)

BenchmarkStdCrc8KB-4              200000             11417 ns/op         717.48 MB/s (slice8)
BenchmarkCrc8KBNoAsm-4            200000             11317 ns/op         723.85 MB/s (slice8)
BenchmarkCrc8KB-4                 500000              2919 ns/op        2805.73 MB/s (asm)

BenchmarkStdCrc32KB-4              30000             45749 ns/op         716.24 MB/s (slice8)
BenchmarkCrc32KBNoAsm-4            30000             45109 ns/op         726.42 MB/s (slice8)
BenchmarkCrc32KB-4                100000             11497 ns/op        2850.09 MB/s (asm)

BenchmarkStdNoAsmCastagnol40B-4 10000000               161 ns/op         246.94 MB/s
BenchmarkStdCastagnoli40B-4     50000000              28.4 ns/op        1410.69 MB/s (asm)
BenchmarkCastagnoli40BNoAsm-4   20000000               100 ns/op         398.01 MB/s (slice8)
BenchmarkCastagnoli40B-4        50000000              28.2 ns/op        1419.54 MB/s (asm)

BenchmarkStdNoAsmCastagnoli1KB-4  500000              3622 ns/op        282.67 MB/s
BenchmarkStdCastagnoli1KB-4     10000000               144 ns/op        7099.78 MB/s (asm)
BenchmarkCastagnoli1KBNoAsm-4    1000000              1475 ns/op         694.14 MB/s (slice8)
BenchmarkCastagnoli1KB-4        10000000               146 ns/op        6993.35 MB/s (asm)

BenchmarkStdNoAsmCastagnoli8KB-4  50000              28781 ns/op         284.63 MB/s
BenchmarkStdCastagnoli8KB-4      1000000              1029 ns/op        7957.89 MB/s (asm)
BenchmarkCastagnoli8KBNoAsm-4     200000             11410 ns/op         717.94 MB/s (slice8)
BenchmarkCastagnoli8KB-4         1000000              1000 ns/op        8188.71 MB/s (asm)

BenchmarkStdNoAsmCastagnoli32KB-4  10000            115426 ns/op         283.89 MB/s
BenchmarkStdCastagnoli32KB-4      300000              4065 ns/op        8059.13 MB/s (asm)
BenchmarkCastagnoli32KBNoAsm-4     30000             45171 ns/op         725.41 MB/s (slice8)
BenchmarkCastagnoli32KB-4         500000              4077 ns/op        8035.89 MB/s (asm)
```

The IEEE assembler optimizations has been submitted and will be part of the Go 1.6 standard library.

However, the improved use of slice-by-8 has not, but will probably be submitted for Go 1.7.

# license

Standard Go license. Changes are Copyright (c) 2015 Klaus Post under same conditions.
# cpuid
Package cpuid provides information about the CPU running the current program.

CPU features are detected on startup, and kept for fast access through the life of the application.
Currently x86 / x64 (AMD64) is supported, and no external C (cgo) code is used, which should make the library very easy to use.

You can access the CPU information by accessing the shared CPU variable of the cpuid library.

Package home: https://github.com/klauspost/cpuid

[![GoDoc][1]][2] [![Build Status][3]][4]

[1]: https://godoc.org/github.com/klauspost/cpuid?status.svg
[2]: https://godoc.org/github.com/klauspost/cpuid
[3]: https://travis-ci.org/klauspost/cpuid.svg
[4]: https://travis-ci.org/klauspost/cpuid

# features
## CPU Instructions
*  **CMOV** (i686 CMOV)
*  **NX** (NX (No-Execute) bit)
*  **AMD3DNOW** (AMD 3DNOW)
*  **AMD3DNOWEXT** (AMD 3DNowExt)
*  **MMX** (standard MMX)
*  **MMXEXT** (SSE integer functions or AMD MMX ext)
*  **SSE** (SSE functions)
*  **SSE2** (P4 SSE functions)
*  **SSE3** (Prescott SSE3 functions)
*  **SSSE3** (Conroe SSSE3 functions)
*  **SSE4** (Penryn SSE4.1 functions)
*  **SSE4A** (AMD Barcelona microarchitecture SSE4a instructions)
*  **SSE42** (Nehalem SSE4.2 functions)
*  **AVX** (AVX functions)
*  **AVX2** (AVX2 functions)
*  **FMA3** (Intel FMA 3)
*  **FMA4** (Bulldozer FMA4 functions)
*  **XOP** (Bulldozer XOP functions)
*  **F16C** (Half-precision floating-point conversion)
*  **BMI1** (Bit Manipulation Instruction Set 1)
*  **BMI2** (Bit Manipulation Instruction Set 2)
*  **TBM** (AMD Trailing Bit Manipulation)
*  **LZCNT** (LZCNT instruction)
*  **POPCNT** (POPCNT instruction)
*  **AESNI** (Advanced Encryption Standard New Instructions)
*  **CLMUL** (Carry-less Multiplication)
*  **HTT** (Hyperthreading (enabled))
*  **HLE** (Hardware Lock Elision)
*  **RTM** (Restricted Transactional Memory)
*  **RDRAND** (RDRAND instruction is available)
*  **RDSEED** (RDSEED instruction is available)
*  **ADX** (Intel ADX (Multi-Precision Add-Carry Instruction Extensions))
*  **SHA** (Intel SHA Extensions)
*  **AVX512F** (AVX-512 Foundation)
*  **AVX512DQ** (AVX-512 Doubleword and Quadword Instructions)
*  **AVX512IFMA** (AVX-512 Integer Fused Multiply-Add Instructions)
*  **AVX512PF** (AVX-512 Prefetch Instructions)
*  **AVX512ER** (AVX-512 Exponential and Reciprocal Instructions)
*  **AVX512CD** (AVX-512 Conflict Detection Instructions)
*  **AVX512BW** (AVX-512 Byte and Word Instructions)
*  **AVX512VL** (AVX-512 Vector Length Extensions)
*  **AVX512VBMI** (AVX-512 Vector Bit Manipulation Instructions)
*  **MPX** (Intel MPX (Memory Protection Extensions))
*  **ERMS** (Enhanced REP MOVSB/STOSB)
*  **RDTSCP** (RDTSCP Instruction)
*  **CX16** (CMPXCHG16B Instruction)
*  **SGX** (Software Guard Extensions, with activation details)

## Performance
*  **RDTSCP()** Returns current cycle count. Can be used for benchmarking.
*  **SSE2SLOW** (SSE2 is supported, but usually not faster)
*  **SSE3SLOW** (SSE3 is supported, but usually not faster)
*  **ATOM** (Atom processor, some SSSE3 instructions are slower)
*  **Cache line** (Probable size of a cache line).
*  **L1, L2, L3 Cache size** on newer Intel/AMD CPUs.

## Cpu Vendor/VM
* **Intel**
* **AMD**
* **VIA**
* **Transmeta**
* **NSC**
* **KVM**  (Kernel-based Virtual Machine)
* **MSVM** (Microsoft Hyper-V or Windows Virtual PC)
* **VMware**
* **XenHVM**

# installing

```go get github.com/klauspost/cpuid```

# example

```Go
package main

import (
	"fmt"
	"github.com/klauspost/cpuid"
)

func main() {
	// Print basic CPU information:
	fmt.Println("Name:", cpuid.CPU.BrandName)
	fmt.Println("PhysicalCores:", cpuid.CPU.PhysicalCores)
	fmt.Println("ThreadsPerCore:", cpuid.CPU.ThreadsPerCore)
	fmt.Println("LogicalCores:", cpuid.CPU.LogicalCores)
	fmt.Println("Family", cpuid.CPU.Family, "Model:", cpuid.CPU.Model)
	fmt.Println("Features:", cpuid.CPU.Features)
	fmt.Println("Cacheline bytes:", cpuid.CPU.CacheLine)
	fmt.Println("L1 Data Cache:", cpuid.CPU.Cache.L1D, "bytes")
	fmt.Println("L1 Instruction Cache:", cpuid.CPU.Cache.L1D, "bytes")
	fmt.Println("L2 Cache:", cpuid.CPU.Cache.L2, "bytes")
	fmt.Println("L3 Cache:", cpuid.CPU.Cache.L3, "bytes")

	// Test if we have a specific feature:
	if cpuid.CPU.SSE() {
		fmt.Println("We have Streaming SIMD Extensions")
	}
}
```

Sample output:
```
>go run main.go
Name: Intel(R) Core(TM) i5-2540M CPU @ 2.60GHz
PhysicalCores: 2
ThreadsPerCore: 2
LogicalCores: 4
Family 6 Model: 42
Features: CMOV,MMX,MMXEXT,SSE,SSE2,SSE3,SSSE3,SSE4.1,SSE4.2,AVX,AESNI,CLMUL
Cacheline bytes: 64
We have Streaming SIMD Extensions
```

# private package

In the "private" folder you can find an autogenerated version of the library you can include in your own packages.

For this purpose all exports are removed, and functions and constants are lowercased.

This is not a recommended way of using the library, but provided for convenience, if it is difficult for you to use external packages.

# license

This code is published under an MIT license. See LICENSE file for more information.
# Color [![GoDoc](http://img.shields.io/badge/go-documentation-blue.svg?style=flat-square)](http://godoc.org/github.com/fatih/color) [![Build Status](http://img.shields.io/travis/fatih/color.svg?style=flat-square)](https://travis-ci.org/fatih/color)



Color lets you use colorized outputs in terms of [ANSI Escape
Codes](http://en.wikipedia.org/wiki/ANSI_escape_code#Colors) in Go (Golang). It
has support for Windows too! The API can be used in several ways, pick one that
suits you.



![Color](http://i.imgur.com/c1JI0lA.png)


## Install

```bash
go get github.com/fatih/color
```

## Examples

### Standard colors

```go
// Print with default helper functions
color.Cyan("Prints text in cyan.")

// A newline will be appended automatically
color.Blue("Prints %s in blue.", "text")

// These are using the default foreground colors
color.Red("We have red")
color.Magenta("And many others ..")

```

### Mix and reuse colors

```go
// Create a new color object
c := color.New(color.FgCyan).Add(color.Underline)
c.Println("Prints cyan text with an underline.")

// Or just add them to New()
d := color.New(color.FgCyan, color.Bold)
d.Printf("This prints bold cyan %s\n", "too!.")

// Mix up foreground and background colors, create new mixes!
red := color.New(color.FgRed)

boldRed := red.Add(color.Bold)
boldRed.Println("This will print text in bold red.")

whiteBackground := red.Add(color.BgWhite)
whiteBackground.Println("Red text with white background.")
```

### Use your own output (io.Writer)

```go
// Use your own io.Writer output
color.New(color.FgBlue).Fprintln(myWriter, "blue color!")

blue := color.New(color.FgBlue)
blue.Fprint(writer, "This will print text in blue.")
```

### Custom print functions (PrintFunc)

```go
// Create a custom print function for convenience
red := color.New(color.FgRed).PrintfFunc()
red("Warning")
red("Error: %s", err)

// Mix up multiple attributes
notice := color.New(color.Bold, color.FgGreen).PrintlnFunc()
notice("Don't forget this...")
```

### Custom fprint functions (FprintFunc)

```go
blue := color.New(FgBlue).FprintfFunc()
blue(myWriter, "important notice: %s", stars)

// Mix up with multiple attributes
success := color.New(color.Bold, color.FgGreen).FprintlnFunc()
success(myWriter, "Don't forget this...")
```

### Insert into noncolor strings (SprintFunc)

```go
// Create SprintXxx functions to mix strings with other non-colorized strings:
yellow := color.New(color.FgYellow).SprintFunc()
red := color.New(color.FgRed).SprintFunc()
fmt.Printf("This is a %s and this is %s.\n", yellow("warning"), red("error"))

info := color.New(color.FgWhite, color.BgGreen).SprintFunc()
fmt.Printf("This %s rocks!\n", info("package"))

// Use helper functions
fmt.Println("This", color.RedString("warning"), "should be not neglected.")
fmt.Printf("%v %v\n", color.GreenString("Info:"), "an important message.")

// Windows supported too! Just don't forget to change the output to color.Output
fmt.Fprintf(color.Output, "Windows support: %s", color.GreenString("PASS"))
```

### Plug into existing code

```go
// Use handy standard colors
color.Set(color.FgYellow)

fmt.Println("Existing text will now be in yellow")
fmt.Printf("This one %s\n", "too")

color.Unset() // Don't forget to unset

// You can mix up parameters
color.Set(color.FgMagenta, color.Bold)
defer color.Unset() // Use it in your function

fmt.Println("All text will now be bold magenta.")
```

### Disable color

There might be a case where you want to disable color output (for example to
pipe the standard output of your app to somewhere else). `Color` has support to
disable colors both globally and for single color definition. For example
suppose you have a CLI app and a `--no-color` bool flag. You can easily disable
the color output with:

```go

var flagNoColor = flag.Bool("no-color", false, "Disable color output")

if *flagNoColor {
	color.NoColor = true // disables colorized output
}
```

It also has support for single color definitions (local). You can
disable/enable color output on the fly:

```go
c := color.New(color.FgCyan)
c.Println("Prints cyan text")

c.DisableColor()
c.Println("This is printed without any color")

c.EnableColor()
c.Println("This prints again cyan...")
```

## Todo

* Save/Return previous values
* Evaluate fmt.Formatter interface


## Credits

 * [Fatih Arslan](https://github.com/fatih)
 * Windows support via @mattn: [colorable](https://github.com/mattn/go-colorable)

## License

The MIT License (MIT) - see [`LICENSE.md`](https://github.com/fatih/color/blob/master/LICENSE.md) for more details

Resize
======

Image resizing for the [Go programming language](http://golang.org) with common interpolation methods.

[![Build Status](https://travis-ci.org/nfnt/resize.svg)](https://travis-ci.org/nfnt/resize)

Installation
------------

```bash
$ go get github.com/nfnt/resize
```

It's that easy!

Usage
-----

This package needs at least Go 1.1. Import package with

```go
import "github.com/nfnt/resize"
```

The resize package provides 2 functions:

* `resize.Resize` creates a scaled image with new dimensions (`width`, `height`) using the interpolation function `interp`.
  If either `width` or `height` is set to 0, it will be set to an aspect ratio preserving value.
* `resize.Thumbnail` downscales an image preserving its aspect ratio to the maximum dimensions (`maxWidth`, `maxHeight`).
  It will return the original image if original sizes are smaller than the provided dimensions.

```go
resize.Resize(width, height uint, img image.Image, interp resize.InterpolationFunction) image.Image
resize.Thumbnail(maxWidth, maxHeight uint, img image.Image, interp resize.InterpolationFunction) image.Image
```

The provided interpolation functions are (from fast to slow execution time)

- `NearestNeighbor`: [Nearest-neighbor interpolation](http://en.wikipedia.org/wiki/Nearest-neighbor_interpolation)
- `Bilinear`: [Bilinear interpolation](http://en.wikipedia.org/wiki/Bilinear_interpolation)
- `Bicubic`: [Bicubic interpolation](http://en.wikipedia.org/wiki/Bicubic_interpolation)
- `MitchellNetravali`: [Mitchell-Netravali interpolation](http://dl.acm.org/citation.cfm?id=378514)
- `Lanczos2`: [Lanczos resampling](http://en.wikipedia.org/wiki/Lanczos_resampling) with a=2
- `Lanczos3`: [Lanczos resampling](http://en.wikipedia.org/wiki/Lanczos_resampling) with a=3

Which of these methods gives the best results depends on your use case.

Sample usage:

```go
package main

import (
	"github.com/nfnt/resize"
	"image/jpeg"
	"log"
	"os"
)

func main() {
	// open "test.jpg"
	file, err := os.Open("test.jpg")
	if err != nil {
		log.Fatal(err)
	}

	// decode jpeg into image.Image
	img, err := jpeg.Decode(file)
	if err != nil {
		log.Fatal(err)
	}
	file.Close()

	// resize to width 1000 using Lanczos resampling
	// and preserve aspect ratio
	m := resize.Resize(1000, 0, img, resize.Lanczos3)

	out, err := os.Create("test_resized.jpg")
	if err != nil {
		log.Fatal(err)
	}
	defer out.Close()

	// write new image to file
	jpeg.Encode(out, m, nil)
}
```

Caveats
-------

* Optimized access routines are used for `image.RGBA`, `image.NRGBA`, `image.RGBA64`, `image.NRGBA64`, `image.YCbCr`, `image.Gray`, and `image.Gray16` types. All other image types are accessed in a generic way that will result in slow processing speed.
* JPEG images are stored in `image.YCbCr`. This image format stores data in a way that will decrease processing speed. A resize may be up to 2 times slower than with `image.RGBA`. 


Downsizing Samples
-------

Downsizing is not as simple as it might look like. Images have to be filtered before they are scaled down, otherwise aliasing might occur.
Filtering is highly subjective: Applying too much will blur the whole image, too little will make aliasing become apparent.
Resize tries to provide sane defaults that should suffice in most cases.

### Artificial sample

Original image
![Rings](http://nfnt.github.com/img/rings_lg_orig.png)

<table>
<tr>
<th><img src="http://nfnt.github.com/img/rings_300_NearestNeighbor.png" /><br>Nearest-Neighbor</th>
<th><img src="http://nfnt.github.com/img/rings_300_Bilinear.png" /><br>Bilinear</th>
</tr>
<tr>
<th><img src="http://nfnt.github.com/img/rings_300_Bicubic.png" /><br>Bicubic</th>
<th><img src="http://nfnt.github.com/img/rings_300_MitchellNetravali.png" /><br>Mitchell-Netravali</th>
</tr>
<tr>
<th><img src="http://nfnt.github.com/img/rings_300_Lanczos2.png" /><br>Lanczos2</th>
<th><img src="http://nfnt.github.com/img/rings_300_Lanczos3.png" /><br>Lanczos3</th>
</tr>
</table>

### Real-Life sample

Original image  
![Original](http://nfnt.github.com/img/IMG_3694_720.jpg)

<table>
<tr>
<th><img src="http://nfnt.github.com/img/IMG_3694_300_NearestNeighbor.png" /><br>Nearest-Neighbor</th>
<th><img src="http://nfnt.github.com/img/IMG_3694_300_Bilinear.png" /><br>Bilinear</th>
</tr>
<tr>
<th><img src="http://nfnt.github.com/img/IMG_3694_300_Bicubic.png" /><br>Bicubic</th>
<th><img src="http://nfnt.github.com/img/IMG_3694_300_MitchellNetravali.png" /><br>Mitchell-Netravali</th>
</tr>
<tr>
<th><img src="http://nfnt.github.com/img/IMG_3694_300_Lanczos2.png" /><br>Lanczos2</th>
<th><img src="http://nfnt.github.com/img/IMG_3694_300_Lanczos3.png" /><br>Lanczos3</th>
</tr>
</table>


License
-------

Copyright (c) 2012 Jan Schlicht <janschlicht@gmail.com>
Resize is released under a MIT style license.
All files in subdirectories are templates, do modifications based on your environment first.Gogs LDAP Authentication Module
===============================

## About

This authentication module attempts to authorize and authenticate a user
against an LDAP server. It provides two methods of authentication: LDAP via
BindDN, and LDAP simple authentication.

LDAP via BindDN functions like most LDAP authentication systems. First, it
queries the LDAP server using a Bind DN and searches for the user that is
attempting to sign in. If the user is found, the module attempts to bind to the
server using the user's supplied credentials. If this succeeds, the user has
been authenticated, and his account information is retrieved and passed to the
Gogs login infrastructure.

LDAP simple authentication does not utilize a Bind DN. Instead, it binds
directly with the LDAP server using the user's supplied credentials. If the bind
succeeds and no filter rules out the user, the user is authenticated.

LDAP via BindDN is recommended for most users. By using a Bind DN, the server
can perform authorization by restricting which entries the Bind DN account can
read. Further, using a Bind DN with reduced permissions can reduce security risk
in the face of application bugs.

## Usage

To use this module, add an LDAP authentication source via the Authentications
section in the admin panel. Both the LDAP via BindDN and the simple auth LDAP
share the following fields:

* Authorization Name **(required)**
    * A name to assign to the new method of authorization.

* Host **(required)**
    * The address where the LDAP server can be reached.
    * Example: mydomain.com

* Port **(required)**
    * The port to use when connecting to the server.
    * Example: 636

* Enable TLS Encryption (optional)
    * Whether to use TLS when connecting to the LDAP server.

* Admin Filter (optional)
    * An LDAP filter specifying if a user should be given administrator
      privileges. If a user accounts passes the filter, the user will be
      privileged as an administrator.
    * Example: (objectClass=adminAccount)

* First name attribute (optional)
    * The attribute of the user's LDAP record containing the user's first name.
      This will be used to populate their account information.
    * Example: givenName

* Surname attribute (optional)
    * The attribute of the user's LDAP record containing the user's surname This
      will be used to populate their account information.
    * Example: sn

* E-mail attribute **(required)**
    * The attribute of the user's LDAP record containing the user's email
      address. This will be used to populate their account information.
    * Example: mail

**LDAP via BindDN** adds the following fields:

* Bind DN (optional)
    * The DN to bind to the LDAP server with when searching for the user. This
      may be left blank to perform an anonymous search.
    * Example: cn=Search,dc=mydomain,dc=com

* Bind Password (optional)
    * The password for the Bind DN specified above, if any. _Note: The password
      is stored in plaintext at the server. As such, ensure that your Bind DN
      has as few privileges as possible._

* User Search Base **(required)**
    * The LDAP base at which user accounts will be searched for.
    * Example: ou=Users,dc=mydomain,dc=com

* User Filter **(required)**
    * An LDAP filter declaring how to find the user record that is attempting to
      authenticate. The '%s' matching parameter will be substituted with the
      user's username.
    * Example: (&(objectClass=posixAccount)(uid=%s))

**LDAP using simple auth** adds the following fields:

* User DN **(required)**
    * A template to use as the user's DN. The `%s` matching parameter will be
      substituted with the user's username.
    * Example: cn=%s,ou=Users,dc=mydomain,dc=com
    * Example: uid=%s,ou=Users,dc=mydomain,dc=com

* User Filter **(required)**
    * An LDAP filter declaring when a user should be allowed to log in. The `%s`
      matching parameter will be substituted with the user's username.
    * Example: (&(objectClass=posixAccount)(cn=%s))
    * Example: (&(objectClass=posixAccount)(uid=%s))

**Verify group membership in LDAP** uses the following fields:

* Group Search Base (optional)
    * The LDAP DN used for groups.
    * Example: ou=group,dc=mydomain,dc=com

* Group Name Filter (optional)
    * An LDAP filter declaring how to find valid groups in the above DN.
    * Example: (|(cn=gogs_users)(cn=admins))

* User Attribute in Group (optional)
    * Which user LDAP attribute is listed in the group.
    * Example: uid

* Group Attribute for User (optional)
    * Which group LDAP attribute contains an array above user attribute names.
    * Example: memberUid
Execute following command in ROOT directory when anything is changed:

$ make bindata# Docker for Gogs

Visit [Docker Hub](https://hub.docker.com/r/gogs/) / [Docker Store](https://store.docker.com/community/images/gogs/gogs) see all available images and tags.

## Usage

To keep your data out of Docker container, we do a volume (`/var/gogs` -> `/data`) here, and you can change it based on your situation.

```sh
# Pull image from Docker Hub.
$ docker pull gogs/gogs

# Create local directory for volume.
$ mkdir -p /var/gogs

# Use `docker run` for the first time.
$ docker run --name=gogs -p 10022:22 -p 10080:3000 -v /var/gogs:/data gogs/gogs

# Use `docker start` if you have stopped it.
$ docker start gogs
```

Note: It is important to map the Gogs ssh service from the container to the host and set the appropriate SSH Port and URI settings when setting up Gogs for the first time. To access and clone Gogs Git repositories with the above configuration you would use: `git clone ssh://git@hostname:10022/username/myrepo.git` for example.

Files will be store in local path `/var/gogs` in my case.

Directory `/var/gogs` keeps Git repositories and Gogs data:

    /var/gogs
    |-- git
    |   |-- gogs-repositories
    |-- ssh
    |   |-- # ssh public/private keys for Gogs
    |-- gogs
        |-- conf
        |-- data
        |-- log

#### Custom Directory

The "custom" directory may not be obvious in Docker environment. The `/var/gogs/gogs` (in the host) and `/data/gogs` (in the container) is already the "custom" directory and you do not need to create another layer but directly edit corresponding files under this directory.

### Volume With Data Container

If you're more comfortable with mounting data to a data container, the commands you execute at the first time will look like as follows:

```sh
# Create data container
docker run --name=gogs-data --entrypoint /bin/true gogs/gogs

# Use `docker run` for the first time.
docker run --name=gogs --volumes-from gogs-data -p 10022:22 -p 10080:3000 gogs/gogs
```

#### Using Docker 1.9 Volume Command

```sh
# Create docker volume.
$ docker volume create --name gogs-data

# Use `docker run` for the first time.
$ docker run --name=gogs -p 10022:22 -p 10080:3000 -v gogs-data:/data gogs/gogs
```

## Settings

### Application

Most of settings are obvious and easy to understand, but there are some settings can be confusing by running Gogs inside Docker:

- **Repository Root Path**: keep it as default value `/home/git/gogs-repositories` because `start.sh` already made a symbolic link for you.
- **Run User**: keep it as default value `git` because `build.sh` already setup a user with name `git`.
- **Domain**: fill in with Docker container IP (e.g. `192.168.99.100`). But if you want to access your Gogs instance from a different physical machine, please fill in with the hostname or IP address of the Docker host machine.
- **SSH Port**: Use the exposed port from Docker container. For example, your SSH server listens on `22` inside Docker, **but** you expose it by `10022:22`, then use `10022` for this value. **Builtin SSH server is not recommended inside Docker Container**
- **HTTP Port**: Use port you want Gogs to listen on inside Docker container. For example, your Gogs listens on `3000` inside Docker, **and** you expose it by `10080:3000`, but you still use `3000` for this value.
- **Application URL**: Use combination of **Domain** and **exposed HTTP Port** values (e.g. `http://192.168.99.100:10080/`).

Full documentation of application settings can be found [here](https://gogs.io/docs/advanced/configuration_cheat_sheet.html).

### Container Options

This container have some options available via environment variables, these options are opt-in features that can help the administration of this container:

- **SOCAT_LINK**:
  - <u>Possible value:</u>
      `true`, `false`, `1`, `0`
  - <u>Default:</u>
      `true`
  - <u>Action:</u>
      Bind linked docker container to localhost socket using socat.
      Any exported port from a linked container will be binded to the matching port on localhost.
  - <u>Disclaimer:</u>
      As this option rely on the environment variable created by docker when a container is linked, this option should be deactivated in managed environment such as Rancher or Kubernetes (set to `0` or `false`)
- **RUN_CROND**:
  - <u>Possible value:</u>
      `true`, `false`, `1`, `0`
  - <u>Default:</u>
      `false`
  - <u>Action:</u>
      Request crond to be run inside the container. Its default configuration will periodically run all scripts from `/etc/periodic/${period}` but custom crontabs can be added to `/var/spool/cron/crontabs/`.

## Upgrade

:exclamation::exclamation::exclamation:<span style="color: red">**Make sure you have volumed data to somewhere outside Docker container**</span>:exclamation::exclamation::exclamation:

Steps to upgrade Gogs with Docker:

- `docker pull gogs/gogs`
- `docker stop gogs`
- `docker rm gogs`
- Finally, create container as the first time and don't forget to do same volume and port mapping.

## Known Issues

- The docker container can not currently be build on Raspberry 1 (armv6l) as our base image `alpine` does not have a `go` package available for this platform.

## Useful Links

- [Share port 22 between Gogs inside Docker & the local system](http://www.ateijelo.com/blog/2016/07/09/share-port-22-between-docker-gogs-ssh-and-local-system)
