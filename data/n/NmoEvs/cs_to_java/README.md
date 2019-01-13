
# From C\# or C++ to Java

By Benoît Oury based on training by Christophe Philemotte:


## Clone Me!

The [project](http://bitbucket.evs.tv/projects/FRM/repos/from_cs_to_java) can be cloned:

```Bash
$ git clone ssh://git@bitbucket.evs.tv:7999/frm/from_cs_to_java.git
```

## Prepare your Environment


### Intellij

>_You can find a complete IntelliJ presentation [here](IntelliJ/README.md)_

1. In the "Welcome to IntelliJ IDEA" window, click the "Create new project" option.
2. Select "Empty project"
3. Give a name (such as `Java training`)
4. Set the JDK 8 in the project default properties
5. If not yet done, clone the repository
    * "VCS" -> "checkout from version control" -> git
    * ssh://git@bitbucket.evs.tv:7999/frm/from_cs_to_java.git
    * select target parent directory
    * do NOT create project based on sources
6. Create modules
    * "File" -> "new" -> "module from existing sources"
    * select `settings.gradle` file
    * In the "Import Project" Gradle dialog, check the three checkboxes and select "Use gradle wrapper task configuration".

 ![](IntelliJ/img/new_graddle_module.PNG)

7. Click "OK". IntelliJ will automatically create its project artifacts based
   on the Gradle project file. After the project has loaded and you've
   dismissed the "Tip of the Day" dialog, you may see a notice (in the
   top-right-hand corner), saying, "Unindex remote maven repositories found."
   you can safely dismiss this notice.
8. Open the `README.md` file and carefully read it.
9. Start by running the test suite: In the "Project" view, right-click on the
   test file (`<exercise>\src\test\java\<Exercise>Test`), select "Run", then
   pick the "<Exercise>Test" that has a JUnit icon to the left of it (red and
   green arrows), NOT the Gradle icon (circular green):

>    When you first start an exercise, you should expect compilation errors
>     because the test is setting expectations on a class that you need to write.
>     By trying to run the tests, you get a nice list of what needs to be fixed
>     in the "Messages Make" view.

## Language: Similarities and Differences

In the following, we're going to  introduce by practice the programming language
Java from the perspective of a C# or C++ developer. The comparison focus on the
important components and is not exhaustive.

Lot of tutorials are present on the [Oracle Java Tutorials](https://docs.oracle.com/javase/tutorial/) site. 

* [Main differences with C++](fromcplusplus/README.md)


* [Primitive](primitive/README.md)
* [Classes and Objects](object/README.md)
* [Nested Classes](nested_classes/README.md)
* [Package](package/README.md)
* [Access Modifiers](access_modifiers/README.md)
* [Construction and Destruction](ctor_and_dtor/README.md)
* [Property](property/README.md)
* [Method](method/README.md)
* [Interface](interface/README.md)
* [Enumeration](enum/README.md)
* [Static field](static_field/README.md)
* [Exception](exception/README.md)
* [Annotations](annotations/README.md)
* [Generics](generics/README.md)
* [Event](event/README.md)
* [String](string/README.md)
* [Math](math/README.md)
* [Switch Statement](switch/README.md)
* [List](list/README.md)
* [Set](set/README.md)
* [Map](map/README.md)
* [For-each Loop](foreach/README.md)
* [MultiDimensional Array](multidimensional_array/README.md)
* [Lambda](lambda/README.md)
* [LINQ](linq/README.md)
* [Stream](stream/README.md)
* [Class loader](classloader/README.md)
* [Optional](optional/README.md)
* [CompletableFuture](completablefuture/README.md)
* [Reflexion](reflexion/README.md)
* [I/O](io/README.md)
* [Collection](collection/README.md)
* [Concurrency](concurrency/README.md)
* [Time and Date](time_and_date/README.md)
* [Internationalization](i18n/README.md)
* [Regular Expression](regexp/README.md)

### Further Reading for C# developers

* An up to date blog post about
  [Java for C# Programmers](http://kynosarges.org/JavaCSharp.html)
* A recent blog post addressing
  [Java vs C#](http://weblogs.asp.net/ricardoperes/java-vs-c-%E2%80%93-part-1)
  in [two parts](https://weblogs.asp.net/ricardoperes/java-vs-c-%E2%80%93-part-2)
* An interesting, detailed, but a little bit old,
  [comparison of C# to Java](http://www.25hoursaday.com/CsharpVsJava.html)
* A controversial but very interesting wiki page
  [comparing C# and Java](https://en.wikipedia.org/wiki/Comparison_of_C_Sharp_and_Java)
* An old, but interesting article by Microsoft
  [comparing C# and Java](https://msdn.microsoft.com/en-us/library/ms836794.aspx)

### Further Reading for C++ developers

* A Wikipedia page with great differences between C++ and Java
  [Comparison of Java and C++](https://en.wikipedia.org/wiki/Comparison_of_Java_and_C%2B%2B)


### Further Reading for everyone

* Some information about the [jvm](jvm/README.md)  
* Devoxx is a belgian Java conference which puts online a lot of interesting videos on 
  [Devoxx Youtube channel](https://www.youtube.com/channel/UCCBVCTuk6uJrN3iFV_3vurg)
* The force of Java resides on it's large panel of frameworks. If you need something, someone has already done it,
  take a look at
  * [The apache software foundation](https://www.apache.org/)
  * [Spring](https://spring.io/)
  * [GitHub](https://github.com/)
* If you know the name of a library, you'll find the dependency information on [MVNRepository](https://mvnrepository.com/)  

## Libraries

The Java Development Kit (JDK) offers libraries equivalent to those of the C#
.NET framework or C++ Standard Library, except implementations being quite different. For this reason,
we're going to give first an overview of the JDK, and then to introduce several
important packages

### Overview

* Base Libraries
  [`java.util`](https://docs.oracle.com/javase/8/docs/api/java/util/package-summary.html) and
  [`java.lang`](https://docs.oracle.com/javase/8/docs/api/java/lang/package-summary.html)
  provide basic functionality that is used by almost all applications:

  * [Collection Framework](https://docs.oracle.com/javase/8/docs/technotes/guides/collections/reference.html)
  * [Core Math](https://docs.oracle.com/javase/8/docs/technotes/guides/math/index.html)
  * [Regular Expression](https://docs.oracle.com/javase/8/docs/api/java/util/regex/package-summary.html)
  * [Logging](https://docs.oracle.com/javase/8/docs/api/java/util/logging/package-summary.html)
    * Note the EVS will use [SLF4J](https://www.slf4j.org/) instead to get an abstraction of log system
  * [Concurrency Utilities](https://docs.oracle.com/javase/8/docs/technotes/guides/concurrency/index.html)

* Other Base Libraries

  * [I/O](https://docs.oracle.com/javase/8/docs/technotes/guides/io/index.html)
  * [Date and Time](https://docs.oracle.com/javase/8/docs/technotes/guides/datetime/index.html)
  * [Internationalization](https://docs.oracle.com/javase/8/docs/technotes/guides/intl/index.html)
  * [Networking](https://docs.oracle.com/javase/8/docs/technotes/guides/net/index.html)
  * [Object Serialization](https://docs.oracle.com/javase/8/docs/technotes/guides/serialization/index.html)
  * [XML](https://docs.oracle.com/javase/8/docs/technotes/guides/xml/index.html)

* Integration Libraries: [JDBC](https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/index.html)
* User Interface Toolkit: [JavaFX](http://docs.oracle.com/javase/8/javase-clienttechnologies.htm)

#### Further Reading

* [Base Libraries, JDK 8](http://docs.oracle.com/javase/8/docs/technotes/guides/#base)
* [Java SE 8](https://docs.oracle.com/javase/8/docs/)

## Largely used frameworks

Frameworks are larger then libraries. Those three one are largely used in the industry.

* [Spring](spring/README.md)
* [Spring Boot](springboot/README.md)
* [JPA - Hibernate](jpa/README.md)



## Conventions and miscellaneous

### Code Style

A list on [internal conventions](https://wiki.evs.tv/pages/viewpage.action?pageId=22744423) exists on the wiki. They are
based on the following references.

Among the code style guides, the following ones are good ones to follow:

* [Google Java Style](https://google.github.io/styleguide/javaguide.html)
* [Twitter Java Style Guide](https://github.com/twitter/commons/blob/master/src/java/com/twitter/common/styleguide.md)
* [Oracle Code Conventions for the Java Programming Language](http://www.oracle.com/technetwork/java/codeconvtoc-136057.html)
* [Android Code Style for Contributors](https://source.android.com/source/code-style.html)

In addition, there are several recommendations and considerations made by Java
itself:

* [Naming Variable](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/variables.html#naming)
* [Naming Class](https://docs.oracle.com/javase/tutorial/java/javaOO/classdecl.html)
* [Naming Method](https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html)
* [Naming Package](http://docs.oracle.com/javase/tutorial/java/package/namingpkgs.html)
* [Naming Type Parameter](https://docs.oracle.com/javase/tutorial/java/generics/types.html)

IntelliJ allows you to
[automate the formatting of your code](https://www.jetbrains.com/help/idea/2016.1/code-style-java.html)
and by doing so help you to enforce your conventions.

### Idioms

Idioms are common and good practices to resolve a very common problem. Of course,
Java has its owns. It's important to know several of them, as they are proved
solutions that you can apply directly. However, idioms are not the truth and
it's important to stay critical. For instance, a new version of the language can
bring new features that makes irrelevant some idioms.

You can find them at the following resources:

* [Java Idioms](http://c2.com/cgi/wiki?JavaIdioms)
* [Good Java Idioms](https://www.nayuki.io/page/good-java-idioms)
* [Effective Java](https://amzn.com/0321356683)

### Documentation

[Javadoc](http://docs.oracle.com/javase/8/docs/technotes/guides/javadoc/index.html)
is a companion tool parsing your source code to extract documentation from comments
and generate proper HTML pages. Thanks to the Doclet API, you can also generate
other kind of text output.

[Documentation comments](http://www.oracle.com/technetwork/java/javase/documentation/index-137868.html)
is a valid Java comment following a specific format based on tags and HTML.

## Ecosystem

The Java Ecosystem is very wide and mature. In the following, different keywords
are listed per topic that will help you to explore the ecosystem.

* IDE: Eclipse, IntelliJ, NetBeans
* Java Big Players: Oracle, Google, IBM, Pivotal, Apache, Typesafe, Redhat, Spring.io
* JVM languages: Groovy, Scala, JRuby, Clojure, Jython
* Enterprise Framework: Java EE, Spring
* Build Tool: Ant, Maven, Gradle
* Java Persistence Tool: JPA (Hibernate, OpenJPA, EclipseLink), JDBC, Spring JdbcTemplate
* Web Framework: Spring MVC, Java Server Faces, Struts, DropWizard, SpringBoot
* Test Framework: JUnit, TestNG, Spock, Mockitto, Arquillian, JTest
* Application Server: Tomcat, Wildfly/JBoss, Jetty, Weblogic, Glashfish/Payara
* Continuous Integration: Jenkins, TeamCity
* Continuous Inspection: SonarQube, CAST AIP, Kiuwan
* Artifact Repository: Nexus, Archiva, Artifactory
* Issue Tracker: Jira, Assembla, Pivotal Tracker, YourTrack
* Famous Open Source Projects: Hadoop, Apache Spark, ElasticSearch, Neo4J


## Resources and References

### References

* [The Java Tutorials](http://docs.oracle.com/javase/tutorial/index.html)
* [The Java SE 8 API](https://docs.oracle.com/javase/8/docs/api/)
* [The Java SE 8 Documentations](https://docs.oracle.com/javase/8/docs/)
* [The Java Language and Virtual Machine Specifications](http://docs.oracle.com/javase/specs/index.html)

### Newsletters

* [Oracle Java Magazine](http://www.oracle.com/technetwork/java/javamagazine/index.html)
* [Java Code Geeks](https://www.javacodegeeks.com/)
* [Java Performance Tuning](http://www.javaperformancetuning.com/)
* [Java World](http://www.javaworld.com/)
* [Voxxed](https://www.voxxed.com/blog/category/java/)

### Books

* [Core Java Volume I](https://amzn.com/0134177304) and [Volume II](https://amzn.com/0134177290)
* [Effective Java](https://amzn.com/0321356683)
* [Java Concurrency in Practice](http://jcip.net/)

### Samples and tutorials

* [mkyong.com](https://www.mkyong.com/)
* [java-examples.com](http://www.java-examples.com/)
* [www.jmdoudoux.fr](https://www.jmdoudoux.fr/accueil_java.htm)
* [www.baeldung.com](http://www.baeldung.com/)
* [Oracle java articles](http://www.oracle.com/technetwork/articles/java/index.html)

### Blogs

* [Adam Bien](http://www.adam-bien.com/roller/abien/)
* [Antonio Goncalves](https://antoniogoncalves.org/)
* [Baeldung](http://www.baeldung.com/)
* [Bozhidar Bozhanov](http://techblog.bozho.net/)
* [Markus Eisele](http://blog.eisele.net/)
* [Nicolas Frankel](https://blog.frankel.ch/)
* [Pascal Alma](https://pragmaticintegrator.wordpress.com/)
* [Petri Kainulainen](http://www.petrikainulainen.net/blog/)
* [Reza Rahman](http://blog.rahmannet.net/)
* [Stephen Colebourne](http://blog.joda.org/)
* [Trisha Gee](http://trishagee.github.io/)
* [Vlad Mihalcea](https://vladmihalcea.com/)


## License

The content of this project itself is licensed under the
[Creative Commons Attribution 4.0 license](https://creativecommons.org/licenses/by-nc-sa/4.0/)
, and the underlying source code of the exercises is licensed under the
[MIT license](https://opensource.org/licenses/mit-license.php).
