* [一、准备工作](#%E4%B8%80%E5%87%86%E5%A4%87%E5%B7%A5%E4%BD%9C)
* [二、安装步骤](#%E4%BA%8C%E5%AE%89%E8%A3%85%E6%AD%A5%E9%AA%A4)
* [三、启动Apollo配置中心](#%E4%B8%89%E5%90%AF%E5%8A%A8apollo%E9%85%8D%E7%BD%AE%E4%B8%AD%E5%BF%83)
* [四、使用Apollo配置中心](#%E5%9B%9B%E4%BD%BF%E7%94%A8apollo%E9%85%8D%E7%BD%AE%E4%B8%AD%E5%BF%83)

为了让大家更快的上手了解Apollo配置中心，我们这里准备了一个Quick Start，能够在几分钟内在本地环境部署、启动Apollo配置中心。

考虑到Docker的便捷性，我们还提供了Quick Start的Docker版本，如果你对Docker比较熟悉的话，可以参考[Apollo Quick Start Docker部署](https://github.com/ctripcorp/apollo/wiki/Apollo-Quick-Start-Docker%E9%83%A8%E7%BD%B2)通过Docker快速部署Apollo。

不过这里需要注意的是，Quick Start只针对本地测试使用，如果要部署到生产环境，还请另行参考[分布式部署指南](https://github.com/ctripcorp/apollo/wiki/%E5%88%86%E5%B8%83%E5%BC%8F%E9%83%A8%E7%BD%B2%E6%8C%87%E5%8D%97)。

> 注：Quick Start需要有bash环境，Windows用户建议安装[Git Bash](https://git-for-windows.github.io/)，或者也可以直接通过IDE环境启动，详见[Apollo开发指南](https://github.com/ctripcorp/apollo/wiki/Apollo%E5%BC%80%E5%8F%91%E6%8C%87%E5%8D%97)。

# 一、准备工作
## 1.1 Java

* Apollo服务端：1.8+
* Apollo客户端：1.7+

由于Quick Start会在本地同时启动服务端和客户端，所以需要在本地安装Java 1.8+。

在配置好后，可以通过如下命令检查：
```sh
java -version
```

样例输出：
```sh
java version "1.8.0_74"
Java(TM) SE Runtime Environment (build 1.8.0_74-b02)
Java HotSpot(TM) 64-Bit Server VM (build 25.74-b02, mixed mode)
```

## 1.2 MySQL

* 版本要求：5.6.5+

Apollo的表结构对`timestamp`使用了多个default声明，所以需要5.6.5以上版本。

连接上MySQL后，可以通过如下命令检查：
```sql
SHOW VARIABLES WHERE Variable_name = 'version';
```

| Variable_name | Value  |
|---------------|--------|
| version       | 5.7.11 |

## 1.3 下载Quick Start安装包
我们准备好了一个Quick Start安装包，大家只需要下载到本地，就可以直接使用，免去了编译、打包过程。

安装包共50M，如果访问github网速不给力的话，可以从百度网盘下载。

1. 从Github下载
    * checkout或下载[apollo-build-scripts项目](https://github.com/nobodyiam/apollo-build-scripts)
    * **由于Quick Start项目比较大，所以放在了另外的repository，请注意项目地址**
        * https://github.com/nobodyiam/apollo-build-scripts
2. 从百度网盘下载
    * 通过[网盘链接](https://pan.baidu.com/s/1CtLAXQFxOfvb2xUV2R0PlQ)下载
    * 下载到本地后，在本地解压apollo-quick-start.zip
3. 为啥安装包要50M这么大？
    * 因为这是一个可以自启动的jar包，里面包含了所有依赖jar包以及一个内置的tomcat容器

# 二、安装步骤
## 2.1 创建数据库
Apollo服务端共需要两个数据库：`ApolloPortalDB`和`ApolloConfigDB`，我们把数据库、表的创建和样例数据都分别准备了sql文件，只需要导入数据库即可。

> 注意：如果你本地已经创建过Apollo数据库，请注意备份数据。我们准备的sql文件会清空Apollo相关的表。

### 2.1.1 创建ApolloPortalDB
通过各种MySQL客户端导入[sql/apolloportaldb.sql](https://github.com/nobodyiam/apollo-build-scripts/blob/master/sql/apolloportaldb.sql)即可。

下面以MySQL原生客户端为例：
```sql
source /your_local_path/sql/apolloportaldb.sql
```

导入成功后，可以通过执行以下sql语句来验证：
```sql
select `Id`, `AppId`, `Name` from ApolloPortalDB.App;
```

| Id | AppId     | Name       |
|----|-----------|------------|
| 1  | SampleApp | Sample App |

### 2.1.2 创建ApolloConfigDB
通过各种MySQL客户端导入[sql/apolloconfigdb.sql](https://github.com/nobodyiam/apollo-build-scripts/blob/master/sql/apolloconfigdb.sql)即可。

下面以MySQL原生客户端为例：
```sql
source /your_local_path/sql/apolloconfigdb.sql
```

导入成功后，可以通过执行以下sql语句来验证：
```sql
select `NamespaceId`, `Key`, `Value`, `Comment` from ApolloConfigDB.Item;
```
| NamespaceId | Key     | Value | Comment            |
|-------------|---------|-------|--------------------|
| 1           | timeout | 100   | sample timeout配置 |

## 2.2 配置数据库连接信息
Apollo服务端需要知道如何连接到你前面创建的数据库，所以需要编辑[demo.sh](https://github.com/nobodyiam/apollo-build-scripts/blob/master/demo.sh)，修改ApolloPortalDB和ApolloConfigDB相关的数据库连接串信息。

> 注意：填入的用户需要具备对ApolloPortalDB和ApolloConfigDB数据的读写权限。

```sh
#apollo config db info
apollo_config_db_url=jdbc:mysql://localhost:3306/ApolloConfigDB?characterEncoding=utf8
apollo_config_db_username=用户名
apollo_config_db_password=密码（如果没有密码，留空即可）

# apollo portal db info
apollo_portal_db_url=jdbc:mysql://localhost:3306/ApolloPortalDB?characterEncoding=utf8
apollo_portal_db_username=用户名
apollo_portal_db_password=密码（如果没有密码，留空即可）
```

> 注意：不要修改demo.sh的其它部分

# 三、启动Apollo配置中心
## 3.1 确保端口未被占用
Quick Start脚本会在本地启动3个服务，分别使用8070, 8080, 8090端口，请确保这3个端口当前没有被使用。

例如，在Linux/Mac下，可以通过如下命令检查：
```sh
lsof -i:8080
```

## 3.2 执行启动脚本
```sh
./demo.sh start
```

当看到如下输出后，就说明启动成功了！
```sh
==== starting service ====
Service logging file is ./service/apollo-service.log
Started [10768]
Waiting for config service startup.......
Config service started. You may visit http://localhost:8080 for service status now!
Waiting for admin service startup....
Admin service started
==== starting portal ====
Portal logging file is ./portal/apollo-portal.log
Started [10846]
Waiting for portal startup......
Portal started. You can visit http://localhost:8070 now!
```

## 3.3 异常排查
如果启动遇到了异常，可以分别查看service和portal目录下的log文件排查问题。

> 注：在启动apollo-configservice的过程中会在日志中输出eureka注册失败的信息，如`com.sun.jersey.api.client.ClientHandlerException: java.net.ConnectException: Connection refused`。需要注意的是，这个是预期的情况，因为apollo-configservice需要向Meta Server（它自己）注册服务，但是因为在启动过程中，自己还没起来，所以会报这个错。后面会进行重试的动作，所以等自己服务起来后就会注册正常了。

## 3.4 注意
Quick Start只是用来帮助大家快速体验Apollo项目，具体实际使用时请参考：[分布式部署指南](https://github.com/ctripcorp/apollo/wiki/%E5%88%86%E5%B8%83%E5%BC%8F%E9%83%A8%E7%BD%B2%E6%8C%87%E5%8D%97)。

另外需要注意的是Quick Start不支持增加环境，只有通过分布式部署才可以新增环境，同样请参考：[分布式部署指南](https://github.com/ctripcorp/apollo/wiki/%E5%88%86%E5%B8%83%E5%BC%8F%E9%83%A8%E7%BD%B2%E6%8C%87%E5%8D%97)

# 四、使用Apollo配置中心
## 4.1 使用样例项目

### 4.1.1 查看样例配置
1. 打开http://localhost:8070

> Quick Start集成了[Spring Security简单认证](https://github.com/ctripcorp/apollo/wiki/Portal-%E5%AE%9E%E7%8E%B0%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%E5%8A%9F%E8%83%BD#%E5%AE%9E%E7%8E%B0%E6%96%B9%E5%BC%8F%E4%B8%80%E4%BD%BF%E7%94%A8apollo%E6%8F%90%E4%BE%9B%E7%9A%84spring-security%E7%AE%80%E5%8D%95%E8%AE%A4%E8%AF%81)，更多信息可以参考[Portal 实现用户登录功能](https://github.com/ctripcorp/apollo/wiki/Portal-%E5%AE%9E%E7%8E%B0%E7%94%A8%E6%88%B7%E7%99%BB%E5%BD%95%E5%8A%9F%E8%83%BD)

<img src="https://github.com/nobodyiam/apollo-build-scripts/raw/master/images/apollo-login.png" alt="登录" width="640px">

2. 输入用户名apollo，密码admin后登录

![首页](https://github.com/nobodyiam/apollo-build-scripts/blob/master/images/apollo-sample-home.png)

3. 点击SampleApp进入配置界面，可以看到当前有一个配置timeout=100
![配置界面](https://github.com/nobodyiam/apollo-build-scripts/blob/master/images/sample-app-config.png)

> 如果提示`系统出错，请重试或联系系统负责人`，请稍后几秒钟重试一下，因为通过Eureka注册的服务有一个刷新的延时。

### 4.1.2 运行客户端程序
我们准备了一个简单的[Demo客户端](https://github.com/ctripcorp/apollo/blob/master/apollo-demo/src/main/java/com/ctrip/framework/apollo/demo/api/SimpleApolloConfigDemo.java)来演示从Apollo配置中心获取配置。

程序很简单，就是用户输入一个key的名字，程序会输出这个key对应的值。

如果没找到这个key，则输出undefined。

同时，客户端还会监听配置变化事件，一旦有变化就会输出变化的配置信息。

运行`./demo.sh client`启动Demo客户端，忽略前面的调试信息，可以看到如下提示：
```sh
Apollo Config Demo. Please input key to get the value. Input quit to exit.
>
```
输入`timeout`，会看到如下信息：
```sh
> timeout
> [SimpleApolloConfigDemo] Loading key : timeout with value: 100
```

> 如果运行客户端遇到问题，可以通过修改`client/log4j2.xml`中的level为DEBUG来查看更详细日志信息
> ```xml
> <logger name="com.ctrip.framework.apollo" additivity="false" level="trace">
>     <AppenderRef ref="Async" level="DEBUG"/>
> </logger>
> ```

### 4.1.3 修改配置并发布

1. 在配置界面点击timeout这一项的编辑按钮
![编辑配置](https://github.com/nobodyiam/apollo-build-scripts/blob/master/images/sample-app-modify-config.png)

2. 在弹出框中把值改成200并提交
![配置修改](https://github.com/nobodyiam/apollo-build-scripts/blob/master/images/sample-app-submit-config.png)

3. 点击发布按钮，并填写发布信息
![发布](https://github.com/nobodyiam/apollo-build-scripts/blob/master/images/sample-app-release-config.png)

![发布信息](https://github.com/nobodyiam/apollo-build-scripts/blob/master/images/sample-app-release-detail.png)

### 4.1.4 客户端查看修改后的值
如果客户端一直在运行的话，在配置发布后就会监听到配置变化，并输出修改的配置信息：
```sh
[SimpleApolloConfigDemo] Changes for namespace application
[SimpleApolloConfigDemo] Change - key: timeout, oldValue: 100, newValue: 200, changeType: MODIFIED
```

再次输入`timeout`查看对应的值，会看到如下信息：
```sh
> timeout
> [SimpleApolloConfigDemo] Loading key : timeout with value: 200
```

## 4.2 使用新的项目
### 4.2.1 应用接入Apollo
这部分可以参考[Java应用接入指南](https://github.com/ctripcorp/apollo/wiki/Java%E5%AE%A2%E6%88%B7%E7%AB%AF%E4%BD%BF%E7%94%A8%E6%8C%87%E5%8D%97)

### 4.2.2 运行客户端程序
由于使用了新的项目，所以客户端需要修改appId信息。

编辑`client/META-INF/app.properties`，修改app.id为你新创建的app id。
```properties
app.id=你的appId
```
# 运行`./demo.sh client`启动Demo客户端即可。