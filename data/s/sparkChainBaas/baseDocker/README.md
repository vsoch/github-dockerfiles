火花Docker镜像
==============
[![Build Status](https://travis-ci.org/QianmiOpen/interface-test.svg?branch=master)](#)

火花Docker镜像fork了[dockerfile用户](https://github.com/dockerfile)的项目，在其基础编写了基于区块链的接入平台的docker镜像。<br/>
不同的业务不同的开发者对性能、并发、高可用性、易用等要求不尽相同，故其接入链端的部署也完全不同。对于初学区块链的开发者，需要一个简单易用的接入链的环境，方便业务开发，对于大型的业务系统，上链就需要考虑到并发，高可用性等，可能需要采用微服务、服务网格来部署。<br/>
安得世间双全法，不负如来不负卿。有没有一套工具在开发时或简单应用时能实现快速且易用地接入公链，在业务量大增时，能快速地改造成微服务、服务网格这种分布式部署呢？<br/>
火花Docker镜像就是用来实现这个目标的一组Docker镜像，通过这些镜像，你可以自由地组合，形成复杂强大的接入链的部署，也可以简单使用一行命令就可以部署整个接入链的程序（支持的各大公链）


## 使用简介

docker镜像下载
```sh
docker run -d   --name spc-chain-base --env TESTNET="--testnet"  \
-p 8545:8545 -p 8200:8200  -p 8080:8080 -p 3306:3306  \
-p 6379:6379 sparkchain/spc-chain-base:1.0

```
 自己代码调用docker中的接口，其文档见[火花链接入文档]()，示例见 [火花链留言板]()示例。

## docker镜像列表

| 分类 | 说明 |
| :------- | :----- |
| <a href="01ubuntu/README.md" target="_blank">Ubuntu操作系统镜像</a>| 干净的Ubuntu16.04操作系统，其它镜像的基础     |
| <a href="01python/README.md" target="_blank">Python的镜像</a>    | 在Ubuntu的基础上，安装Python环境   |
| <a href="03jdk8/README.md" target="_blank">Oracle JDK8镜像</a>    | 在Ubuntu的基础上，安装oracle的JDK 8|
| <a href="04jdk8_py/README.md" target="_blank">建立在Python基础上Oracle JDK8镜像</a>             | 在Ubuntu的和Python的基础上，安装oracle的JDK 8        |
| <a href="05nodejs/README.md" target="_blank">Nodejs镜像</a>   |    建立在Python基础上的Nodejs镜像         |
| <a href="06nodejs_jdk8/README.md" target="_blank">建立在JDK8基础上的Nodejs镜像</a>  | 既可以运行Nodejs和JDK8的镜像环境   |
| <a href="07mysql57/README.md" target="_blank">干净的mysql镜像</a>   | 建立在ubuntu上的mysql的镜像|
| <a href="08mysql57_jdk8/README.md" target="_blank">建立在JDK8基础上的Mysql镜像</a>                | 可以安装java应用并直接使用本地的mysql的数据库 |
| <a href="09mysql57_node10/README.md" target="_blank">建立在nodejs10基础上的Mysql镜像</a>                | 既可以运行nodejs应用同时还可以使用mysql数据库                  |
| <a href="09mysql57_node10_jdk8/README.md" target="_blank">建立在nodejs10和JKD8基础上的Mysql镜像</a>                | 既可以运行nodejs应用、Java应用，同时还可以使用mysql数据库          |
| <a href="10redis4/README.md" target="_blank">Redis4的单机镜像</a>          | 简化redis的单机版的安装   |
| <a href="11redis4_jdk8/README.md" target="_blank">建立在jdk8基础上的redis4</a> |可以安装使用Redis的java应用  |
| <a href="12redis4_mysql57_jdk8/README.md" target="_blank">redis4、mysql57、jdk8镜像</a> | 可以快速安装需要mysql和redis的java应用  |
| <a href="13redis4_mysql57_node10/README.md" target="_blank">redis4、mysql57、nodejs10的镜像</a> | 可以快速安装需要mysql和redis的nodejs应用  |
| <a href="14redis4_mysql57_node10_jdk8/README.md" target="_blank">redis4、mysql57、nodejs10、jdk8的镜像</a>                        | 一个镜像中既可以安装java应用、也可以安装nodejs应用 ｜
| <a href="15moac/README.md" target="_blank">moac的镜像</a>                 | moac目前不支持docker镜像，这里单独做了一个 |
| <a href="16moac_node10/README.md" target="_blank">moac和nodejs的镜像</a>                 | 可以方便地部署基于nodejs的moac链端应用          |
| <a href="17moac_redis4_mysql57_node10_jdk8/README.md" target="_blank">moac、jdk、nodejs、mysql、redis的镜像</a>                 | 把开发的java接入平台应用和链端应用部署一个docker中，方便开发调试         |


## 技术支持
 
  欢迎大家去<a href="http://sparkda.com" target="_blank">斯巴达论坛</a> 进行区块链的技术交流和沟通<br/>


火花链基本Docker镜像
==============
[![Build Status](https://travis-ci.org/QianmiOpen/interface-test.svg?branch=master)](https://travis-ci.org/QianmiOpen/interface-test)

目标：降低接口测试难度、帮助开发人员快速测试接口。<br/>
目前已支持dubbo接口测试（需要借助[Edge](https://github.com/qianmiopen/edge)将dubbo接口以http形式发布），后期可以经过简单修改就能支持rest接口测试。
测试人员通过json、js语言编写用例文件，通过maven插件执行用例，并生成报告；
![image](report-demo.png)

> 与Edge比较<br/>
> Edge擅长的是以可视化的方式、实时的对接口进行测试，测试结果返回后需要人为的check。比较适合在开发、联调阶段使用。<br/>
> interface-test将用例以脚本的方式保存下来，通过脚本自定义check规则，程序自动判断接口测试结果，用例可以回放执行。比较适合用在服务重构后接口的兼容检查、版本上线前的接口检测。<br/>
> 测试dubbo接口时，interface-test工具依赖Edge工具的测试接口。<br/>

## 使用介绍

添加依赖
```xml
<dependencies>
    <dependency>
        <groupId>com.qianmi</groupId>
        <artifactId>interface-test</artifactId>
        <version>1.0.5-RELEASE</version>
        <scope>runtime</scope>
    </dependency>
</dependencies>
```
指定build plugin
```xml
<plugin>
    <groupId>org.codehaus.mojo</groupId>
    <artifactId>exec-maven-plugin</artifactId>
    <version>1.5.0</version>
    <executions>
        <execution>
            <id>run-testcase</id>
            <goals>
                <goal>java</goal>
            </goals>
        </execution>
    </executions>
    <configuration>
        <classpathScope>runtime</classpathScope>
        <mainClass>org.springframework.boot.loader.JarLauncher</mainClass>
        <arguments>
            <argument>-Dspring.config.location=${basedir}/application.properties</argument> <!--指定运行配置文件-->
        </arguments>
    </configuration>
</plugin>
```

application.properties
```properties
logging.level.root=info
logging.level.com.qianmi=debug
logging.level.com.qianmi.tda.report=info

## 测试用例根目录
test-suit-home=${user.dir}/testcase/com/qianmi/pc/stock/api
## 测试用例文件扩展名
test-case-file-extensions=.ts.json, .ts.js
## 测试报告根目录
test-reports-home=${user.dir}/reports
## 默认dubbo测试服务器地址(Edge服务地址)
default-test-server-url=http://172.19.65.96:8080/executeTest.do

http.client.connection-manager-default-max-per-route=1000
http.client.request-connect-timeout=2000
http.client.connection-manager-max-total=1000
http.client.request-read-timeout=100000

```

使用demo: [interface-test-demo](https://github.com/qianmiopen/inderface-demo)

### 创建测试套（TestSuit）
#### TestCase模板：
```json
   {
      "name": "case1",
      "params": [],
      "expects": [
        {
          "operator": "=",
          "path": "$",
          "value": {}
        }
      ]
    }
```
| Field              |Type      | Description                                                        |
| :------------------|:-------- | :----------------------------------------------------------------- |
| name               |String    | 用例名称，建议根据测试场景命名，不可为空                                  |
| params             |Object[]  | 参数列表，待测接口的JSON格式                                            |
| expects            |Expect[]  | 断言数组。|

>
 operator: 期待值与真实值的比较操作符，支持“=、!=、<、<=、>、>=、contains、!contains、match、!match”;<br/>
 path: 从接口返回结果取值的路径，参见 [JsonPath表达式](#jsonpath表达式); <br/>
 value: 期待值<br/>


#### TestSuit模板：
```json
{
  "dubboServiceURL": "dubbo://172.19.65.199:20880",
  "execOrder": 1,
  "intfName": "com.qianmi.pc.api.app.AppProductProvider:1.0.0@addFromOwner",
  "testCases": [{}],
  "testServerURL": null
}
```

| Field              |Type      | Description                                                        |
| :------------------|:-------- | :----------------------------------------------------------------- |
| dubboServiceURL    |String    | dubbo服务地址，可为空，未指定时从dubbo注册中心上自动查找                 |
| execOrder          |Number    | 测试套执行顺序，默认为1，值越小优先级越高                                |
| intfName           |String    | 待测接口名，不填写时将根据文件名猜测                                    |
| testCases          |TestCase[]| 测试用例数组，参见[TestCase模板](#testcase模板)                               |
| testServerURL      |String    | 测试目标服务器地址，测试dubbo接口时，此处配置[Edge](https://github.com/qianmiopen/edge)服务器代理地址           |

> intfName为空时，系统会根绝文件路径与文件名进行猜测。例如：在%TEST_SUIT_HOME%目录下放置"com/qianmi/pc/api/app/AppProductProvider#1.0.0@addFromOwner.ts.json"文件，intfName将会自动猜测为："com.qianmi.pc.api.app.AppProductProvider:1.0.0@addFromOwner"


完整TestSuit示例：
```json
{
  "dubboServiceURL": "dubbo://172.19.65.199:20880",
  "execOrder": 1,
  "intfName": "com.qianmi.pc.api.app.AppProductProvider:1.0.0@addFromOwner",
  "testCases": [
    {
      "name": "成功从供应商添加商品",
      "params": [
        {
          "chainMasterId": "A1295139",
          "commissionType": 1,
          "cost": 0,
          "optUserCode": null,
          "optUserName": null,
          "price": 0,
          "productId": "1300607",
          "shopStatus": 0,
          "stock": 0,
          "supplierId": "A1437887"
        }
      ],
      "expects": [
        {
          "operator": "=",
          "path": "$.sourceChainMasterId",
          "value": "A1295139"
        },{
          "operator": "=",
          "path": "$.productId",
          "value": "1300607"
        },{
          "operator": ">=",
          "path": "$.goodsIds.length()",
          "value": 1
        }
      ]
    }
  ],
  "testServerURL": "http://172.19.65.96:8080/executeTest.do"
}
```
> TestSuit文件存放路径以及命名规则:<br/>
> 默认TEST_SUIT_HOME目录在System.getProperty("user.dir")下的testcase目录。<br/>
> src/test/java/com/qianmi/tda/TestCaseGenerator.java提供了根据ES接口日志自动生成TestSuit的方法。

### 执行测试
>打开com.qianmi.tda.InterfaceTestApplication，执行main方法即可。测试报告存放在TEST_SUIT_HOME下。


### [JsonPath](https://github.com/jayway/JsonPath)表达式
JsonPath expressions can use the dot–notation

`$.store.book[0].title`

or the bracket–notation

`$['store']['book'][0]['title']`

#### Operators

| Operator                  | Description                                                        |
| :------------------------ | :----------------------------------------------------------------- |
| `$`                       | The root element to query. This starts all path expressions.       |
| `@`                       | The current node being processed by a filter predicate.            |
| `*`                       | Wildcard. Available anywhere a name or numeric are required.       |
| `..`                      | Deep scan. Available anywhere a name is required.                  |
| `.<name>`                 | Dot-notated child                                                  |
| `['<name>' (, '<name>')]` | Bracket-notated child or children                                  |
| `[<number> (, <number>)]` | Array index or indexes                                             |
| `[start:end]`             | Array slice operator                                               |
| `[?(<expression>)]`       | Filter expression. Expression must evaluate to a boolean value.    |


#### Functions

Functions can be invoked at the tail end of a path - the input to a function is the output of the path expression.
The function output is dictated by the function itself.

| Function                  | Description                                                        | Output    |
| :------------------------ | :----------------------------------------------------------------- |-----------|
| min()                    | Provides the min value of an array of numbers                       | Double    |
| max()                    | Provides the max value of an array of numbers                       | Double    |
| avg()                    | Provides the average value of an array of numbers                   | Double    |
| stddev()                 | Provides the standard deviation value of an array of numbers        | Double    |
| length()                 | Provides the length of an array                                     | Integer   |


#### Filter Operators

Filters are logical expressions used to filter arrays. A typical filter would be `[?(@.age > 18)]` where `@` represents the current item being processed. More complex filters can be created with logical operators `&&` and `||`. String literals must be enclosed by single or double quotes (`[?(@.color == 'blue')]` or `[?(@.color == "blue")]`).   

| Operator                 | Description                                                       |
| :----------------------- | :---------------------------------------------------------------- |
| ==                       | left is equal to right (note that 1 is not equal to '1')          |
| !=                       | left is not equal to right                                        |
| <                        | left is less than right                                           |
| <=                       | left is less or equal to right                                    |
| >                        | left is greater than right                                        |
| >=                       | left is greater than or equal to right                            |
| =~                       | left matches regular expression  [?(@.name =~ /foo.*?/i)]         |
| in                       | left exists in right [?(@.size in ['S', 'M'])]                    |
| nin                      | left does not exists in right                                     |
| size                     | size of left (array or string) should match right                 |
| empty                    | left (array or string) should be empty                            |


Path Examples
-------------

Given the json

```json
{
    "store": {
        "book": [
            {
                "category": "reference",
                "author": "Nigel Rees",
                "title": "Sayings of the Century",
                "price": 8.95
            },
            {
                "category": "fiction",
                "author": "Evelyn Waugh",
                "title": "Sword of Honour",
                "price": 12.99
            },
            {
                "category": "fiction",
                "author": "Herman Melville",
                "title": "Moby Dick",
                "isbn": "0-553-21311-3",
                "price": 8.99
            },
            {
                "category": "fiction",
                "author": "J. R. R. Tolkien",
                "title": "The Lord of the Rings",
                "isbn": "0-395-19395-8",
                "price": 22.99
            }
        ],
        "bicycle": {
            "color": "red",
            "price": 19.95
        }
    },
    "expensive": 10
}
```

| JsonPath (click link to try)| Result |
| :------- | :----- |
| <a href="http://jsonpath.herokuapp.com/?path=$.store.book[*].author" target="_blank">$.store.book[*].author</a>| The authors of all books     |
| <a href="http://jsonpath.herokuapp.com/?path=$..author" target="_blank">$..author</a>                   | All authors                         |
| <a href="http://jsonpath.herokuapp.com/?path=$.store.*" target="_blank">$.store.*</a>                  | All things, both books and bicycles  |
| <a href="http://jsonpath.herokuapp.com/?path=$.store..price" target="_blank">$.store..price</a>             | The price of everything         |
| <a href="http://jsonpath.herokuapp.com/?path=$..book[2]" target="_blank">$..book[2]</a>                 | The third book                      |
| <a href="http://jsonpath.herokuapp.com/?path=$..book[0,1]" target="_blank">$..book[0,1]</a>               | The first two books               |
| <a href="http://jsonpath.herokuapp.com/?path=$..book[:2]" target="_blank">$..book[:2]</a>                | All books from index 0 (inclusive) until index 2 (exclusive) |
| <a href="http://jsonpath.herokuapp.com/?path=$..book[1:2]" target="_blank">$..book[1:2]</a>                | All books from index 1 (inclusive) until index 2 (exclusive) |
| <a href="http://jsonpath.herokuapp.com/?path=$..book[-2:]" target="_blank">$..book[-2:]</a>                | Last two books                   |
| <a href="http://jsonpath.herokuapp.com/?path=$..book[2:]" target="_blank">$..book[2:]</a>                | Book number two from tail          |
| <a href="http://jsonpath.herokuapp.com/?path=$..book[?(@.isbn)]" target="_blank">$..book[?(@.isbn)]</a>          | All books with an ISBN number         |
| <a href="http://jsonpath.herokuapp.com/?path=$.store.book[?(@.price < 10)]" target="_blank">$.store.book[?(@.price < 10)]</a> | All books in store cheaper than 10  |
| <a href="http://jsonpath.herokuapp.com/?path=$..book[?(@.price <= $['expensive'])]" target="_blank">$..book[?(@.price <= $['expensive'])]</a> | All books in store that are not "expensive"  |
| <a href="http://jsonpath.herokuapp.com/?path=$..book[?(@.author =~ /.*REES/i)]" target="_blank">$..book[?(@.author =~ /.*REES/i)]</a> | All books matching regex (ignore case)  |
| <a href="http://jsonpath.herokuapp.com/?path=$..*" target="_blank">$..*</a>                        | Give me every thing   
| <a href="http://jsonpath.herokuapp.com/?path=$..book.length()" target="_blank">$..book.length()</a>                 | The number of books                      |

