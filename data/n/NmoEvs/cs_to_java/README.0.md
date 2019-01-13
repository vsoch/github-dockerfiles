# From C++

## Here is a non exhaustive list of differences or similarities between Java and C++

* Java is a compiled AND interpreted language. Java files (.java) are compiled into bytecode (.class) with a development
 kit (JDK) which is interpreted into a virtual machine (JVM) provided by a runtime environment (JRE).
* Java is written once and run everywhere.
* As C++, Java allows procedural, functional and generic programming. Object oriented programming is strongly encouraged
* Java allows reflexion allowing metaprogramming and dynamic code generation at runtime
* Bound check is provided by Java
* Primitive types limits are cross platform
* All types are passed by value. It does not mean that all objects are immutable, it means that primitive types are 
copied and variables referencing objects are copied, not the object itself ! 
See [argument java documentation](http://docs.oracle.com/javase/tutorial/java/javaOO/arguments.html).
* Java does not provide destroy methods but implements an automatic garbage collector. Every non referenced object
is marked as eligible for garbage collection. This collection occurs when system is in a low charge of when needed.
* Resources are not automatically closed if you don't use a "try with resource"
* Java operators are not overridable
* Java does not provide explicit multiple inheritance but Java 8 provides default methods in interfaces which allows
 a kind of multiple inheritance. Nevertheless, multiple inheritance by this way is not a good practice in Java.
* Javadoc provides a native online html documentation
* No goto in Java
* Java does not provide method default attribute values, prefer using method overloading
* Autoboxing converts automatically primitives to linked objects types.
* As in C++ the first element of a list/table is at index 0
    

## References

 [Wikipedia comparison of Java and C++](https://en.wikipedia.org/wiki/Comparison_of_Java_and_C%2B%2B)

# The Game of Life

## Life-cycle

In the current section, we're going to illustrate the different parts of the
life-cycle of the Java development: edition, compilation, execution, debugging,
verification, management of dependencies, packaging and distribution, and the
interface with the host platform.

### Structure

This is part is focused on practice. Each aspects will be first shown then be
applied. The practice structure is the following:

* problem: the [game of life](https://en.wikipedia.org/wiki/Conway%27s_Game_of_Life)
* ping-pong programming
* organized in session of about 1 hour:

  * introduction
  * practice
  * retrospective
  * break

## Tools

Before coding, let's discover some tools to allow us to efficiently code the game of life.

### IntelliJ IDEA

A java code is a simple set of text files. A text editor to edit java files and a command line
to compile them are in theory sufficient to make a java project. Of course, an IDE is very helpful
when coding.

Three major IDE are used to develop in Java: NetBeans, Eclipse and IntelliJ. IntelliJ is the most
advanced one, here is a [presentation of IntelliJ](../IntelliJ/README.md).  

### Gradle

Gradle is a build tools largely used to enforce project structure and allow build automation.
Quite all java projects are based today on build tools like Gradle or Maven. 
Here is a [presentation of Gradle](../gradle_build_tool/README.md)

## The project

### Session 1: Basics

#### Create a new Gradle project in IntelliJ

1. In the "Welcome to IntelliJ IDEA" window, click the "Create New Project"
   option.
2. In the "New Project" dialog, select "Gradle", the project SDK, and check
   Java as "Additional Libraries and Frameworks". Click "Next".
   
   ![](img/gol_1.PNG)
3. Fill at least the "ArtificatId" field, that is the name of the project.

   ![](img/gol_2.PNG)
4. In the "New Project" Gradle dialog, check the "auto-import", "create directories"
 and "Create separate module" checkboxes and select "Use gradle wrapper task configuration".
 
   ![](img/gol_3.PNG)
5. Click "Next". Correct the "Project Name" and "Project location" if they don't
   suit you.
   
   ![](img/gol_4.PNG)
6. Click "Finish". IntelliJ will automatically create its project artifacts
   based on the information provided.
   
   ![](img/gol_5.PNG)

#### A minimal Gradle build script

You'll find in the `template` a minimum scaffold of a Java project with a Gradle
build script `build.gradle`:

```Gradle
group 'com.evs.training'
version '1.0-SNAPSHOT'

task wrapper(type: Wrapper) {
  gradleVersion = '3.3'
  distributionUrl = "https://services.gradle.org/distributions/gradle-$gradleVersion-all.zip"
}

apply plugin: 'java'

sourceCompatibility = 1.8

repositories {
    mavenCentral()
}

dependencies {
    testCompile group: 'junit', name: 'junit', version: '4.12'
}
```

#### Write code in IntelliJ

##### The standard Maven directory layout

The [standard Maven directory layout](http://maven.apache.org/guides/introduction/introduction-to-the-standard-directory-layout.html)
is the following:

* `src/main/java`: Code sources
* `src/test/java`: Test sources
* `src/main/resources`: resources
* `src/test/resources`: Test resources

By default, the plugin creates the structure for you. You can now create the package structure 
in the project panel:

1. Right click on the target folder
2. Submenu "New"
3. Item "Directory" if you are in a "resources" folder or item "package" if you are
in a "java" folder.

> Be careful when creating packages, you have 
to create them one per one, if you specify "com.evs" as package name, only one folder named
"com.evs" will be created instead of a hierarchy of two folders.

##### Add a new source file

You can create a new source file as following:

1. Right click on the target folder
2. Submenu "New"
3. Item "Java Class"
4. Select the type of class to create (class, interface, Enum,...)

##### Edit and your file

Double click on the source file you want to edit. By default, IntelliJ saves files at each
context change (lose focus, build, run, ...) 

#### Compile the project

##### With `javac`

When you just have a command line, you can use `javac` from your JDK to compile your code:

```Bash
javac -d <output_dir> <filename.java>
```

##### With Gradle

In the console, you run the program as following in the folder containing your build.gradle file:

```Bash
gradlew build
```

##### With IntelliJ

You can either do:

* Menu "Build"
* Click Item "Make Project" or use the shortcut `Ctrl + F9`

or

* open the Gradle panel
* Select "Tasks", "build"
* Double-click "Build"

#### Execute the program

##### With `java`

To run a program, you can do:

```Bash
java -cp <classpath> <class_name_containing_main_function>
```
The `classpath` is a list of directories containing `.class` files and `.jar`
files separated by `:` on *nix system and `;` on Windows system.

##### With Gradle

In the console, you run the program as following:

```Bash
gradlew run
```

##### With IntelliJ

To run the program you can do either

* Go in the `main` method
* Type `Ctrl + Shift + F10` or click on the green triangle beside the main method

or

* Menu "Run"
* Item "Edit configurations"
* In the "Run/Debug Configurations" dialog

  * Click on the "+"
  * Select "Application"
  * Fill the "Name field"
  * Select the main class
  * Click "Apply"

* Menu "Run"
* Item "Run ..."
* Select the application with the name you gave it

or

* open the Gradle panel
* Select "Tasks", "application"
* Double-click "Run"


### Session 2: Testing

#### Junit

Junit is an external library, by default, the plugin has added it in your build.gradle file

```Gradle
dependencies {
    testCompile group: 'junit', name: 'junit', version: '4.12'
}
```

You can also tell what you want to log during your tests:

```Gradle
test {
  testLogging {
    events "passed", "skipped", "failed", "standardOut", "standardError"
  }
}
```

Then you can create your first test into `src/test/java`. By convention, unit tests foe a class
 are created in a class names as the class suffixed by "Test" in the same package, for instance
`MyClassTest.java`:

```java
import org.junit.Test;

public class MyClassTest {
  @Test
  public void itIsTrue() {
  }
}
```

You need to at least import `org.junit.Test` and then annotate a method with
`@Test`. Now, the method is considered as a test case that can be run and
discovered.

Junit provide a set of
[assertions](https://github.com/junit-team/junit4/wiki/Assertions)
and other features that you can find on
[their wiki](https://github.com/junit-team/junit4/wiki).

#### Run the tests

##### With Gradle

In the console, you run the program as following:

```Bash
gradlew check
```

##### With IntteliJ

* Click on the green triangle of the test

or

* Right click on the "src/test.java" folder and click "Run 'all tests'"

or 

* Menu "Run"
* Item "Edit configurations"
* In the "Run/Debug Configurations" dialog

  * Click on the "+"
  * Select "Junit"
  * Fill the "Name field"
  * Select "All in package" as "Test kind"
  * Check "In whole project" for "Search for tests"
  * Click "Apply"

* Menu "Run"
* Item "Run ..."
* Select the Junit with the name you gave it

or

* open the Gradle panel
* Select "Tasks", "verification"
* Double-click "check"

#### Track test Coverage

* with [Gradle and Jacoco](https://docs.gradle.org/current/userguide/jacoco_plugin.html)
Intellij)
* with [IntelliJ](https://www.jetbrains.com/help/idea/2016.1/code-coverage.html)


### Session 3: Debugging, Profiling, Monitoring

#### Debug with IntelliJ

* Menu "Run"
* Item "Debug ..."
* Select the application with the name you gave it

To note that you can add a Debug configurations "Remote" that allow you to
attach to any JVM even a remote one if the JVM has been run with given
parameters.

You can:

* set breakpoints,
* browse the Debbuger panel,
* evaluate expression,
* watch expression,
* check current variables, and
* inspect available frames and threads.

#### Oracle Tools

Oracle ship with the JDK several
[tools](http://docs.oracle.com/javase/8/docs/technotes/tools/) that are very
useful to monitor, profile, and manage the JVM.

##### JConsole

[JConsole](http://docs.oracle.com/javase/8/docs/technotes/tools/windows/jconsole.html)
is a JMX-compliant graphical tool for monitoring a Java virtual machine. It can
monitor both local and remote JVMs. It can also monitor and manage an application.

* Run `jconsole`
* Select your JVM

##### Java Mission Control

The [Java Mission Control (JMC)](http://docs.oracle.com/javase/8/docs/technotes/tools/windows/jmc.html)
client includes tools to monitor and manage your Java application without
introducing the performance overhead normally associated with these types of
tools.

* Run `jmc`
* In the JVM Browser select the JVM
* Right Click and select "Run JMX Console"

##### VisualVM

A [graphical tool](http://docs.oracle.com/javase/8/docs/technotes/tools/windows/jvisualvm.html)
that provides detailed information about the Java technology-based applications
(Java applications) while they are running in a Java Virtual Machine. Java
VisualVM provides memory and CPU profiling, heap dump analysis, memory leak
detection, access to MBeans, and garbage collection. See Java VisualVM for more
information.

* Run `jvisualvm`
* Open the "Applications" panel
* Double-click on your application

##### JVM Process Status Tool

[JVM Process Status Tool](http://docs.oracle.com/javase/8/docs/technotes/tools/windows/jps.html)
lists instrumented HotSpot Java virtual machines on a target system.

* Run `jps`
* Check the PID of your application

##### JVM Statistics Monitoring Tool

[JVM Statistics Monitoring Tool](http://docs.oracle.com/javase/8/docs/technotes/tools/windows/jstat.html)
attaches to an instrumented HotSpot Java virtual machine and collects and logs
performance statistics as specified by the command line options.

* Run `jstat -class <pid>`
* Run `jstat -options` to consult the other possible statistics

##### Configuration Info for Java

[Configuration Info for Java](http://docs.oracle.com/javase/8/docs/technotes/tools/windows/jinfo.html)
prints configuration information for a given process or core file or a remote
debug server.

* Run `jinfo <pid>`
* On Linux, you might need to run `echo 0 | sudo tee /proc/sys/kernel/yama/ptrace_scope`

##### Stack Trace for Java

[Stack Trace for Java](http://docs.oracle.com/javase/8/docs/technotes/tools/windows/jstack.html)
prints a stack trace of threads for a given process or core file or remote debug
server.

* Run `jstack <pid>`

### Session 4: Packaging and Resources

#### Create a JAR

The JAR is a package file format packaging the program. It contains your
compiled Java application, your resources, and a manifest. JAR is built on
ZIP.

##### With IntelliJ

* Menu "File"
* Submenu "Project Structure..."
* In the "Project Structure" dialog, select in the left panel "Artifacts"
* Click on "+"

  * Give a name to your artifact
  * Select the type "JAR"
  * Check "Build on make"
  * Select in the "Available Elements"

    * any "compile output" you want to add to your JAR file
    * the manifest if there is one

  * If there isn't a manifest, fill "Manifest File" and "Main Class"
  * Click "OK"

* Build your project, your Artifact will be put into `build/classes/artifacts/`

##### With Gradle

Update your build script:

```Gradle
jar {
  manifest {
    attributes(
      "Main-Class": "<your class with your main method>",
    )
  }
}
```

Then you can run

```Bash
gradlew jar
```

Your JAR file will be available at `build/libs/`

#### Execute a jar

The JRE is shipped with the tool `jar` that allows you to work with that kind of
archive.

If you don't need to reference other libraries or classpath, you can run your
JAR file as following:

```Bash
java -jar <yourjarfile>
```

If your application needs external libraries, the classpath can be set in the META-INF file
as the main class. If it's not done, you have to specify it in the command line:
```Bash
java -cp <classpath> -jar <yourjarfile>
```

The `classpath` is a list of directories containing `.class` files and `.jar`
files separated by `:` on *nix system and `;` on Windows system.

#### Inspect a jar

As JAR files are ZIP files, you can use any tools that allow you to look into
a ZIP files.

If the jar is not signed, you can edit files inside, except classes because they are stored
 as binaries. All resources files are stored in clear and can be changed.
The signature of a jar file sets a checksum in the META-INF file and guarantees a non modified jar. 

#### Resources

##### Add Resources

You can add resources to your application by simply adding them to the directory
`src/main/resources`. They will be taken in account by Gradle and IntelliJ.

To add the resources to an artifact in IntelliJ, you need to add them explicitly
via the "Project Structure" dialog.

Remember that the class loader inspects the main jar to get resources and then inspects 
all resources in the classapth. To avoid a random resource loading if the resource name is present
more then once in the classpath, always place them in a package unique in the classapth (use groupId 
and artifactId as base package name) 

##### Work with resources

You can retrieve the path of a resource as following:

```Java
Path file = Paths.get(this.getClass().getClassLoader().getResource("your filename").getPath());
```

There is a special kind of resource called properties. Their extension is
`.properties`. They are a list of keys and their corresponding values. Those
ones can be directly loaded as following:

```Java
ResourceBundle props = ResourceBundle.getBundle("filename without extenstion.");
String value = props.getString("key");
```

Try to add a text file as resource and read it with the `Files.readAllLines` method.

### Session 5: Interface with the host platform

#### Command Line Arguments

The arguments are available in the array of String passed to the `main` method:

```java
public class Main {
  public static void main(String[] args) {
    for(String arg: args) {
      System.out.println(arg);
    }
  }
}
```

In order to parse the arguments, you can use third party libraries as
 [JCommander](http://www.jcommander.org/). Below a simple example:

```Java
import com.beust.jcommander.JCommander;
import com.beust.jcommander.Parameter;

public class Main {
  @Parameter(names={"--option", "-o"})
  public String str = "none";

  public static void main(String[] args){
    Main main = new Main();
    new JCommander(main, args);
    System.out.println(main.str);
  }
```

#### Environment Variables

Environment variables can be retrieved thanks to the method
`System.getenv(String name)`. Beware that you won't find the same environment
variables depending on the host Operating System. In addition, Windows ignores case 
in environment variable names, while UNIX does not.

#### System properties

The JVM provides you a collection of properties that are specific to the host
system. The can be retrieved thanks to the method `System.getProperty(name)`.
It is very helpful to retrieve for instance the line, file, or path separators.
The API lists the [available system properties](https://docs.oracle.com/javase/8/docs/api/java/lang/System.html#getProperties--).


### Session 6: Improve the game of life

#### Import the Gradle project in IntelliJ

1. In your project, click the "File > new > Module from existing source" menu option.
2. Navigate to the game of life folder, for instance
   `C:\Users\johndoe\from_cs_to_java\Game_Of_life` . Make sure you've selected the
   build.gradle file. Click "OK".
3. In the "Import Project" Gradle dialog, check the "auto-import", "create directories"
 and "create separate module" checkboxes and select "Use gradle wrapper task configuration".

    ![](img/gol_6.PNG)

4. Click "OK". IntelliJ will automatically creates a new module in your project based
   on the Gradle project file.

#### Externalize representation of alive and dead cells in a properties file

* Create a health.properties file to store string representation of cell health.
* Load the file 
* Map toString return values to file values

#### Dynamically generate initial state 

* Change the `generateInitalState()` with a `generateRandomInput(long size)` using
streams to generate random initial state

#### Accepts application arguments to sets the size of the world

* Change `width` and `height` initialization to sets them from program argument.

#### Create a Game class to avoid creating an instance of Main class

* Create a Game class
* Extract code from main that is not explicitly linked to program technical launch

#### Optimize //TO_OPTIMIZE code

* Configure the `TODO` tool window to search for `TO_OPTIMIZE` tag using this 
[tutorial](https://www.jetbrains.com/help/idea/2017.1/defining-todo-patterns-and-filters.html)
* Change non optimized code with optimized one using loops, foreach, streams, lambdas,...
# Static Field

* A `static` field is shared with all instances of all threads.
* A class constant is a `static` field declared as `final`.
* Static field can be assigned in a static initializer.
* Static fields typically lead to non thread safe classes.
* Static methods can only access static fields.
* Make field static only and only when needed to avoid side effects because of 
 instance sharing

## References

* [Class members](http://docs.oracle.com/javase/tutorial/java/javaOO/classvars.html)
* [`static` Fields](http://docs.oracle.com/javase/specs/jls/se8/html/jls-8.html#jls-8.3.1.1)
* [`final` Fields](http://docs.oracle.com/javase/specs/jls/se8/html/jls-8.html#jls-8.3.1.2)
# String

* The operator `==` tests object references and not string values.
* The `str1.equals(str2)` compares the value of the 2 strings.
* Strings are immutable.
* The operator `+` concatenate two strings.
* The method `String.substring()` uses inclusive lower bound and exclusive upper
  bound.
* The `toString()` method on an object returns the object instance address as a String. It must
  be overridden to provide a readable representation of an object.
* Java is case sensitive. A `equalsIgnoreCase()` function allows to compare two strings without taking
care of the case.
* When comparing a string to a constant, always use equals function on constant instead of String to avoid
 null pointer exception if the String is null : `"HELLO".equals(myString)` instead of `myString.equals("HELLO")`

## References

* [method `String.equals`](http://docs.oracle.com/javase/8/docs/api/java/lang/String.html#equals-java.lang.Object-)
* [method `String.equalsIgnoreCase`](http://docs.oracle.com/javase/8/docs/api/java/lang/String.html#equalsIgnoreCase-java.lang.String-)
* [method `String.substring`](http://docs.oracle.com/javase/8/docs/api/java/lang/String.html#substring-int-int-)
* [Reference equality operator](http://docs.oracle.com/javase/specs/jls/se8/html/jls-15.html#jls-15.21.3)
* [String Concatenation Operator +](http://docs.oracle.com/javase/specs/jls/se8/html/jls-15.html#jls-15.18.1)
* [Strings in Java](https://docs.oracle.com/javase/tutorial/java/data/strings.html)
# Primitive

* Primitives are not object and so 
  * cannot be instantiated
  * cannot be null
  * begin with a lower case
* You can use `==` to compare two primitives values
* You can't put them in a collection.
* New primitives cannot be defined (value type does not exist in Java).
* For each primitive, there is a boxed version, i.e. a corresponding class.
* Autoboxing and unboxing allows implicit conversion.
* There is not unsigned numerical primitives.
  * Note that non primitive corresponding classes offer method to deal with unsigned
    * https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html      
    *  https://stackoverflow.com/questions/9854166/declaring-an-unsigned-int-in-java


## References

* [Primitive Types and Values](http://docs.oracle.com/javase/specs/jls/se8/html/jls-4.html#jls-4.2)
* [Autoboxing](http://docs.oracle.com/javase/8/docs/technotes/guides/language/autoboxing.html)
# Internationalization

* [Internationalization](https://docs.oracle.com/javase/8/docs/technotes/guides/intl/index.html)
* [Tutorial](http://docs.oracle.com/javase/tutorial/i18n/index.html)
# Spring

## A brief history

A lot of java advanced functionality are provided through the JavaEE API. It means that you need a JavaEE server
  to have this API benefits or you have to provide your own implementations. One of the main missing implementation
  was the bean container used by EJB.
  
EJB has a poor reputation due to awful firsts versions, the first usable version is the 3.1. Nevertheless,
the idea of a container of beans with their own lifecycle was good and a framework named Spring was created
 to provide a lightweight bean container usable in a JavaSE environment.
  
With years, a lot of other projects were created based on this framework and the core project is now 
called `Spring Framework` instead of simply Spring to distinguish it from other projects of the Spring.io team.
 
## The inversion of control
 
Spring Framework provides an inversion of control (IOC). This pattern applies the Hollywood principle:
 "_Don't call me, I'll call you_" ! You just declare your needed objects and the system injects them instead
 of letting you create them.
 By this way, your code is more concise and you can extract technical boiler plate of object creation to
 focus on the business.
  
### Transitive benefits

Using IOC gives you a way to work with interfaces delegating the implementation selection to the dependency
management tool. Your business service needs a DAO interface to get data and Spring will inject an implementation
found in the classpath at runtime, this implementation is determined by your gradle file loading a particular
implementation as a stub on in development and a JPA one in production.

## The container

Spring Framework create a container called `context` at startup. This container allows management of beans.

> What's a Bean ?
>
> In OO world, a bean is a class with only a default constructor, attributes and accessors. Nowadays in java,
  this kind of class is called `JavaBean` and a `bean` represents an `EJB` or a `Spring Bean`

The container manage the beans lifecycle. Each bean is view as an autonomous entity which can be injected
in an other bean. Beans can be services, dao's, data storage,... they are created by Spring and available
in the container.

### Context definition

The context can be defined either by an XML file, by an annotated class or by API. Firsts applications were 
using an XML file but most applications use now the annotation configuration.
  
By default, the class containing the context initialization annotation defines the root of the application,
every class in this package and subpackages is scanned at startup to detect annotations and create beans
if necessary. You can add some other packages to be scanned to create beans found in libraries or sub projects.

Each bean has a name, by default the name of the bean is the name of the class with a lower case first letter.

### Beans definitions

The easiest way to create a bean is to annotate the class with a Spring bean annotation. Three annotations 
are provided to determine the usage of the bean:

* `@Configuration` : Spring configuration class
* `@Service` : Used for services classes providing a business logic.
* `@Repository` : Used for DAO's, those specialized beans allows to get a transaction injected per user even
if the bean itself is a singleton.
* `@Component` : Used for data storage such as configurations.
* `@Controller` : Spring MVC controller

```Java
...
@Repository
public class JPAMediaAssetDAO implements MediaAssetDAO {
...
```

An other way to create bean is to create a factory method with a `@Bean` annotation. This way allows an less
intrusive way to create beans but needs more boiler plate code.

```Java
@Bean
public ContentService.Client getContentServerClient() {
    return clientProvider.createClient(this, ContentService.Client::new);
}
```



### Beans injection

Beans are selected using the object type. When the code ask a MediaAssetDAO injected bean, Spring will inject a bean
of this class. It means that you can have only one bean definition per Class. It could be a problem if you have multiple
implementations of an interfaces annotated with beans annotations. That's why it's a good practice to split different 
implementations into separate projects to allow implementation selection through the dependency management.

You can infer this logic using [@Qualifier](https://docs.spring.io/spring-framework/docs/current/javadoc-api/org/springframework/beans/factory/annotation/Qualifier.html)
annotation. See [example here](https://spring.io/blog/2014/11/04/a-quality-qualifier).

#### By annotation

You can use the @Autowired annotation on an attribute, Spring will inject an instance at runtime.

```Java
 @Autowired
 private MediaAssetDAO mediaAssetDAO; 
```

#### By constructor

If you create a constructor for a bean class using attributes, Spring will inject existing beans instances of attributes types.

```Java
 @Servcie
 public class MediaAssetService{
  
  private MediaAssetDAO mediaAssetDAO; 
  
  public MediaAssetService ( MediaAssetDAO mediaAssetDAO ){
    this.mediaAssetDAO = mediaAssetDAO;
  }
  
 } 
```

#### GOLD RULE

> You can only inject a bean into a bean, otherwise you will have a null object. If you have a NullPointerException you
> probably inject a non bean class in a bean or a bean in a non bean class.

### Useful annotations

Two useful annotations allows you to trigger code during the bean lifecycle:

* @PostConstruct
  * Called after the constructor (attributes are injected) when the bean is created.
* @PreDestroy
  * Called before the destruction of the bean.


### Beans scope

By default, a bean is a singleton. If you need to specify that a bean must not be a singleton, use the `@Scope` annotation
to make it a `prototype`. Each time a prototype bean is injected, a new instance of it is created.

```Java
 @Component
 @Scope("prototype")
 public class MyNonSingletonClass{
  
 }
```

In a web environment, specific scopes are available: `Request`, `Application`, `Session`,... 

## Transactions

Spring provides a transactional API. By annotating a method with `@Transactional` you implicitly create a transaction
by entering the method. The transaction will be committed in case of return and rollbacked in case of exception (by default
only on Runtime exceptions).

This is "just" an API, it means you have to determine an implementation such as a Database implementation.
 
This annotation provides some customization attributes to determine the propagation method, the read only,...
 
[Transaction management reference](http://docs.spring.io/spring-framework/docs/4.2.x/spring-framework-reference/html/transaction.html)


## Other projects

Spring provides lot of other project helping java developers in their day to day life

* `Spring Boot`
  * Takes an opinionated view of building production-ready Spring applications. Spring Boot favors convention over configuration 
  and is designed to get you up and running as quickly as possible.
* `Spring Cloud`
  * Spring Cloud provides tools for developers to quickly build some of the common patterns in distributed systems 
  (e.g. configuration management, service discovery, circuit breakers, intelligent routing, micro-proxy, control bus, 
  one-time tokens, global locks, leadership election, distributed sessions, cluster state). Coordination of distributed 
  systems leads to boiler plate patterns, and using Spring Cloud developers can quickly stand up services and applications 
  that implement those patterns. They will work well in any distributed environment, including the developer's own laptop, 
  bare metal data centres, and managed platforms such as Cloud Foundry.
* `Spring Data`
  * Spring Data’s mission is to provide a familiar and consistent, Spring-based programming model for data access while still
   retaining the special traits of the underlying data store. It makes it easy to use data access technologies, relational 
   and non-relational databases, map-reduce frameworks, and cloud-based data services. This is an umbrella project which 
   contains many subprojects that are specific to a given database. The projects are developed by working together with 
   many of the companies and developers that are behind these exciting technologies.
* `Spring Security`
  * Spring Security is a powerful and highly customizable authentication and access-control framework. It is the de-facto 
  standard for securing Spring-based applications.


[Complete list of Spring projects](https://spring.io/projects)

## Reference

* [Spring framework reference documentation](http://docs.spring.io/spring-framework/docs/current/spring-framework-reference/html/)
* [Spring framework API](http://docs.spring.io/spring-framework/docs/current/javadoc-api/)
* [Spring guides](https://spring.io/guides)
# Method

* Java supports covariant return types which means that you can return a Dog in a method returning an Animal.
* All methods are virtual except ones explicitly declared `final`.
* When `final`, the method cannot be overridden in children classes.
* Operators cannot be overloaded.
* Methods can be overloaded.
* The behavior of a method can be undefined and declared `abstract`.
* A class including `abstract` methods has to be declared `abstract`.
* A method can be a class method when declared `static`.
* Class methods can be hidden by eponym subclass methods.
* Methods can be overridden by eponym subclass methods.

## References

* [Returning a Value from a Method](http://docs.oracle.com/javase/tutorial/java/javaOO/returnvalue.html)
* [Overriding and Hiding Methods](http://docs.oracle.com/javase/tutorial/java/IandI/override.html)
* [Abstract Methods and Classes](http://docs.oracle.com/javase/tutorial/java/IandI/abstract.html)
* [`final` Methods](http://docs.oracle.com/javase/specs/jls/se8/html/jls-8.html#jls-8.4.3.3)
* [`abstract` Methods](http://docs.oracle.com/javase/specs/jls/se8/html/jls-8.html#jls-8.4.3.1)
* [`static` Methods](http://docs.oracle.com/javase/specs/jls/se8/html/jls-8.html#jls-8.4.3.2)
# Package

* Packages are the dot notation representation of directories storing class files.
* A package name must be unique for the whole classpath (list of all classes known by
the application) to avoid random class loading.
* A good practice is to create package naming in this order
  * inverse company domain name
  * project family
  * project name
  * domain
  * technical
  
  example `com.evs.phoenix.ingest.recorder.persistence.jpa`
* Packages are always defined in lower case
* Use the plural for packages with homogeneous contents and the singular for 
packages with heterogeneous contents 
* The `package` statement applies to the whole file.
* The `import` statement allows to import one class of a given package or all of
  them when using the wildecard `.*`.
* The `import static` statement allows to import static class members without
  qualifications.
* The default visibility of classes, methods, and fields is `protected`, which
  means in Java accessible from every member of the package.

## References

* [Packages](http://docs.oracle.com/javase/tutorial/java/package/packages.html)
* [Managing Source and Class Files](http://docs.oracle.com/javase/tutorial/java/package/managingfiles.html)
* [Static Import](http://docs.oracle.com/javase/8/docs/technotes/guides/language/static-import.html)
* [Determining Accessibility](http://docs.oracle.com/javase/specs/jls/se8/html/jls-6.html#jls-6.6.1)
# Annotations

* Java annotations are like C# attributes but has no equivalence in C++.
* They are metadata not affecting the operation of the annotated code.
* They can be used for several purposes such as detection of errors, generation
  of code.
* `@Override` checks that the method declaration overrides a superclass one.
* `@FunctionalInterface` checks that the interface contains only one abstract
  method.
* Annotations are largely used by frameworks to dynamically inject code at compile time or runtime
* Annotations can be set to classes, methods, fields, arguments,...

## References

* [Annotations](http://docs.oracle.com/javase/tutorial/java/annotations/index.html)
* [`@Override` annotation](http://docs.oracle.com/javase/8/docs/api/java/lang/Override.html)
* [`@FunctionalInterface` annotation](https://docs.oracle.com/javase/8/docs/api/java/lang/FunctionalInterface.html)
* [Type Annotations](http://docs.oracle.com/javase/tutorial/java/annotations/type_annotations.html)
# Regular Expression

* [Tutorial](http://docs.oracle.com/javase/tutorial/essential/regex/index.html)
* [Regular Expression](https://docs.oracle.com/javase/8/docs/api/java/util/regex/package-summary.html)
# Input/Output

* [I/O](https://docs.oracle.com/javase/8/docs/technotes/guides/io/index.html)
* [Tutorial](http://docs.oracle.com/javase/tutorial/essential/io/index.html)
# Optional

* Allow to manage nullables objects without null usage
* Use only as function return value
  * Not as bean attribute
  * Not as argument function
* Use only to return a single result (return empty List otherwise)
* Never use `get()` without testing the presence of the optional
* If you need to make an `Optional<Optional<T>>`, something’s wrong
* Prefer `ifPresent(Consumer<? super T> consumer)` then `isPresent()` if statement
* Use `orElseThrow(Supplier<? extends X> exceptionSupplier)` instead of `!isPresent()` if statement throwing exception
* `orElse(T other)`   vs   `orElseGet(Supplier<? extends T> other)`
  * When using `orElse(T other)`   T is always executed even if optional is not present
  * When using `orElseGet(Supplier other)`   the supplier is invoked only if optional is not present
* Use `flatMap()` to chain Optionals
* Use `map()` to chain non Optional and non nullable value
  


## Reference

* [Optional presentation](http://www.oracle.com/technetwork/articles/java/java8-optional-2175753.html)
* [API documentation](https://docs.oracle.com/javase/8/docs/api/java/util/Optional.html)# Concurrency

* [Concurrency Utilities](https://docs.oracle.com/javase/8/docs/technotes/guides/concurrency/index.html)
* [Tutorial](http://docs.oracle.com/javase/tutorial/essential/concurrency/index.html)
# Access Modifiers

* Access modifier determines the visibility of an object, a method or a variable
* There are 3 access modifiers: `public`, `protected`, and `private`.
* Modifier is not mandatory, default modifier is `protected` also named "package".
* The modifier `protected` gives access to every other classes of the same package and
to all classes extending this class.
* A good practice is to hide variables by setting them `private` and expose them with public accessors
* A technical internal method must be declared `private` or `protected` if this method must be overridden 
by the children of the class. Only functional methods must be public to avoid to expose internal mechanisms

## References

* [Controlling Access to Members of a Class](http://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html)
* [Determining Accessibility](http://docs.oracle.com/javase/specs/jls/se8/html/jls-6.html#jls-6.6.1)
# Construction and Destruction

* A constructor is a method which is called to create an instance of a class with e the `new` keyword
* A constructor must be named as the class beginning with an upper letter and without a return type
* A constructor without argument is called a default constructor
* If no constructor is defined, the JDK will add a default one at compile time
* Use constructors with arguments to allow developers to create objects with instance variables initialization
* A class without any public constructor can't be instantiated (to create a static class for example) 
* Constructor chaining can use `this` or `super` for base classes. They have to
  be called on the first line.
* If there is no explicit call to parent constructor, the default one is called
  implicitly.
* There is no static constructor but you can use initializer bloc.
* There isn't any destructor, but `Object` provides the `finalize()` method that
  may be called before the instance being garbage-collected. Be careful, there is no guarantee that this
  method will be called before the application shut down. Try to never us it...
* In a bean container environment (as Spring or EJB) the container provides annotations to call methods
during the object lifecycle like @PostConstruct and @PreDestroy to achieve this goal

## References

* [Providing Constructors for Your Classes](http://docs.oracle.com/javase/tutorial/java/javaOO/constructors.html)
* [The `finalize()` method](https://docs.oracle.com/javase/tutorial/java/IandI/objectclass.html)
* [Using the keyword `super`](https://docs.oracle.com/javase/tutorial/java/IandI/super.html)
# Spring Boot

Spring Boot makes it easy to create stand-alone, production-grade Spring based Applications
that you can "just run". It takes an opinionated view of the Spring platform and third-party 
libraries so you can get started with minimum fuss. Most Spring Boot applications need very 
little Spring configuration.

## Features

* Create stand-alone Spring applications
* Embed Tomcat, Jetty or Undertow directly (no need to deploy WAR files)
* Automatically configure Spring whenever possible
* Provide production-ready features such as metrics, health checks and externalized configuration
* Absolutely no code generation and no requirement for XML configuration

The [reference guide](https://docs.spring.io/spring-boot/docs/current-SNAPSHOT/reference/htmlsingle)
 includes detailed descriptions of all the features, plus an extensive howto for common use cases.

## Minimal sample

Here is a sample code to generate a web application

### Gradle dependency

```Groovy
dependencies {
    compile("org.springframework.boot:spring-boot-starter-web:1.5.2.RELEASE")
}
```

### Simple controller

```Java

package hello;

import org.springframework.boot.*;
import org.springframework.boot.autoconfigure.*;
import org.springframework.stereotype.*;
import org.springframework.web.bind.annotation.*;

@Controller
@EnableAutoConfiguration
public class SampleController {

    @RequestMapping("/")
    @ResponseBody
    String home() {
        return "Hello World!";
    }

    public static void main(String[] args) throws Exception {
        SpringApplication.run(SampleController.class, args);
    }
}

```

## Reference

* [Spring Boot reference guide](https://docs.spring.io/spring-boot/docs/current-SNAPSHOT/reference/htmlsingle)
# Exception

* Java error management is done with exceptions
* Java has two types of exceptions, checked exceptions and unchecked exceptions.
* Checked exceptions inherits from `Exception`. 
* Unchecked exceptions inherits either from `Error` or `RuntimeException`.
* When a method ca throw a checked exception, it must be declared in the function declaration.
* When a method use a method throwing a checked exception, it must catch it or rethrow it 
(and declare it in its own declaration). 
* Checked exceptions must be used for business errors needing a treatment.
* `RuntimeException` must be use for exceptions occurring in runtime and not necessary manageable.
* Declare your own exceptions inheriting `Exception` or `RuntimeException` instead of throwing those 
base exceptions.
* You can catch multiple exceptions in a single `catch`.
* The `finally` statement is always called. 
* Any jump from the `finally` clause will discard jumps made from the `try`
  clause, either it's a `return` or a thrown exceptions.
* When working with `Closable` classes, prefer a try with resource instead of closing resources 
in hte finally clause.

## References

* [Checked Excpetions](https://en.wikipedia.org/wiki/Exception_handling#Checked_exceptions)
* [The Catch or Specify Requirement](http://docs.oracle.com/javase/tutorial/essential/exceptions/catchOrDeclare.html)
* [Exception](http://docs.oracle.com/javase/8/docs/api/java/lang/Exception.html)
* [RuntimeException](http://docs.oracle.com/javase/8/docs/api/java/lang/RuntimeException.html)
* [Error](http://docs.oracle.com/javase/8/docs/api/java/lang/Error.html)
* [Unchecked Exceptions - The Controversy](http://docs.oracle.com/javase/tutorial/essential/exceptions/runtime.html)
* [Return, Exception, and Finally](http://docs.oracle.com/javase/specs/jls/se8/html/jls-14.html#jls-14.17)
# Time and Date

* [Time and Date](https://docs.oracle.com/javase/8/docs/technotes/guides/datetime/index.html)
* [Tutorial](http://docs.oracle.com/javase/tutorial/datetime/index.html)
# Property

* No property in Java.
* You have to define yourself the accessors. In IntelliJ, `alt+insert` allows to to generate them
* Some frameworks like "lombok" could provide properties like functionality by injecting code at compile time 

## References

* [JavaBeans Pattern](http://docs.oracle.com/javase/tutorial/javabeans/writing/properties.html)
# Switch Statement

* It can compare String objects.
* It can compare a boxed version with their corresponding primitive.
* It allows fall-through.
* Use `break` instruction to exit the evaluation process
* Use `default` bloc to catch unmatched objects

## Reference

* [Oracle Doc](http://docs.oracle.com/javase/tutorial/java/nutsandbolts/switch.html)
# Multidimensional Array

* There is no multidimensionnal array in Java.
* You can use jagged array, i.e. array of array.

## References

* [Array in Java](https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html)
* [Getting and Setting Arrays and Their Components](https://docs.oracle.com/javase/tutorial/reflect/special/arraySetGet.html)
# Internals and JVM

In the following, we give an overview of how the JVM HotSpot works, its
capabilities, its different garbage collectors, the other possible JVM
languages, and what you can do with the JVM at Runtime.

## The General Workflow

* Java Source Files
* Compilation
* Binary Class Files (bytecode)
* Class Loading and Preparation (loading, verification, linking, initializing)
* Internal Data Structure

  * bytecode
  * Metadata: methods, constants, classes, objects

* JIT compiler and bytecode interpreter

## HotSpot

HotSpot is a stack-based VM. There are two implementations of the
[HotSpot JVM](http://docs.oracle.com/javase/8/docs/technotes/guides/vm/index.html):

* The Client VM tuned for small start-up time and memory footprint.
* The Server VM tuned for maximum execution speed.

They are both composed of the 4 main components:

* The class loader
* The execution engine
  * Just-In-Time compiler
  * Bytecode interpreter
  * [4 Available Garbage Collectors](http://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/collectors.html):

    * Serial Collector
    * Parallel Collector
    * [Mostly Concurrent Collectors](http://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/concurrent.html):

      * Concurrent Mark Sweep (CMS) Collector
      * Garbage-First Garbage Collector

* The runtime data areas

  * Java and System Threads
  * Stacks, Heap, Non-Heap
  * Method, Constants, Exception, Symbol, Variables, Strings
  * etc.

* Set of supporting runtime libraries

### Example of Capabilities

* The adaptive compiler can

  * detect performance bottlenecks (hot spots) and compile them.
  * dynamically inline virtual methods when no override is detected at runtime.
  * run analysis during runtime to determine which optimizations are the best.

* Several types of garbage collectors provide different strategies to deal with
  memory garbage and addressing different use cases.
* The thread-handling capability is designed to scale readily for use in large,
  shared-memory multiprocessor servers.

### Going Further

* [JVM internals](http://blog.jamesdbloom.com/JVMInternals.html)
* [HotSpot Internals](https://wiki.openjdk.java.net/display/HotSpot/Main)
* [Introduction to HotSpot Internals](https://www.youtube.com/watch?v=XjfhsJarQy0)

## The Garbage Collectors

As stated above, there are 4 different collectors that you can select:

  * Serial Collector: Single-Threaded GC, very performant on a single processor
    machine or with a very small data sets (< 100MB).
  * Parallel Collector: minor collections in parallel, suited to multi-processor
    or multi-threaded processors with medium and large sized data sets.
  * Mostly Concurrent Collectors: major concurrent collections, suited to
    the cases of parallel collector but that needs better response time.

    * Concurrent Mark Sweep (CMS) Collector: suited to applications that prefer
      shorter garbage collection pauses and can afford to share processor
      resources with the garbage collection.
    * Garbage-First Garbage Collector: suited to multiprocessor machines with
      large memories. It meets garbage collection pause time goals with high
      probability while achieving high throughput.

The CMS is the current default one. The G1 will be the next default.

The [reference library](https://docs.oracle.com/javase/8/docs/api/java/lang/ref/package-summary.html)
provide reference-object classes that can help the garbage collector and by
doing so improving the application performance.

_**TIP**_: Do not change the default collector if you have no performance troubles.

**_TIP_**: If you have memory leaks, first have a look at events listeners, a referenced object is never collected.

### References

* [Garbage Collectors](http://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/collectors.html)
* [Mostly Concurrent Collectors](http://docs.oracle.com/javase/8/docs/technotes/guides/vm/gctuning/concurrent.html)
* [Java 9 The G1 GC Awakens](http://www.slideshare.net/MonicaBeckwith/java-9-the-g1-gc-awakens)

## JVM languages

The JVM HotSpot allows
[scripting languages](https://docs.oracle.com/javase/8/docs/technotes/guides/scripting/index.html).
For instance, it is shipped with the
[Nashorn Engine](https://docs.oracle.com/javase/8/docs/technotes/guides/scripting/nashorn/index.html)
wich support ECMAScript 5. But there are other options.

Indeed, some programming languages can be compiled to be run on the JVM such as:

* Groovy, a scripting and programming language (interpreted and compiled),
* Scala, an object oriented and functional programming language (compiled),
* Clojure, a functional Lisp dialect (compiled),
* JRuby, an implementation of Ruby (interpreted and compiled),
* Jython, and implementation of Python (interpreted and compiled).

Those options allow to use other programming languages, to leverage the JVM
powers, and to integrate with the whole Java ecosystem.

## Playing with the Runtime

There are several tools and libraries allowing to monitor and manage the JVM
thanks to the
[JMX technologies](https://docs.oracle.com/javase/tutorial/jmx/overview/index.html)
with but not only:

* [Jconsole](http://docs.oracle.com/javase/8/docs/technotes/guides/management/jconsole.html):
  the profiler shipped with the JDK
* [Apache JMeter](http://jmeter.apache.org/): load test and performance
  monitoring
* [JVMTop](https://github.com/patric-r/jvmtop): monitoring of running java
  processes
* [Oracle Tools](https://docs.oracle.com/javase/8/docs/technotes/tools/):
  several tools to monitor, profile, or troubleshoot the JVM
* [VisualVM](https://visualvm.java.net/): memory profiler (also shipped with
  Oracle tools)
* [StageMonitor](http://www.stagemonitor.org/): monitoring of your application
  performance
# Gradle build tool

## Why a build tool ?

When developing java applications the same problems occurs each time
* Dependencies management
* Compilation automation
* Test automation
* Bundle deploy
* ...

### The solutions

Home made solutions was not convenient, shared folder with jars, batch files,... that's why
 a first generation of solution was created by Apache with `Ant`. Ant is a scripting tool
 allowing developers to automate steps manipulating code and generating different output as
 documentation, binaries, bundles,...
  
A second generation of solutions give us `Ivy` and `Maven`, a more powerful tool based on Ant and mainly
 based on the `convention over configuration` principle. Maven is used in 70% of java projects
 and provides a new concept for dependencies management. Each jar is defined by a `groupId`, an `artifactId`
 and a `version`. All those jars (called `dependencies` or `artifacts`) are stored on public `repositories`
 to be downloaded when needed. More important, each artifact knows its own dependencies and Maven can
 download the dependencies of your dependencies also called `transitive dependencies`. As is, you just define
 your own dependencies without taking care about the transitive dependencies.
  
In parallel, somme tolls were created to manage the repositories. Some public repositories are storing
a lot of common artifacts and products as `Nexus` or `Artifactory` allows companies to store an internal
repository to share internal artifacts inside the company and used as proxies for public artifacts.

The last generation is represented by `Gradle` which use the largely deployed Maven and Ivy repositories,
use the same conventions but provide a scripting configuration mechanism based on `Groovy` instead
of a static XML definition file. In fact Gradle is based on Maven conventions but provide a scripting
way to use them.


## Gradle description

Gradle provides:

* A very flexible general purpose build tool like Ant.
* Switchable, build-by-convention frameworks a la Maven. But we never lock you in!
* Very powerful support for multi-project builds.
* Very powerful dependency management (based on Apache Ivy).
* Full support for your existing Maven or Ivy repository infrastructure.
* Support for transitive dependency management without the need for remote repositories or pom.xml and ivy.xml files.
* Ant tasks and builds as first class citizens.
* Groovy build scripts.
* A rich domain model for describing your build.

![](images/Gradle1.PNG)

## Project conventions

### Build file

The entry point of a Gradle project is the `build.gradle` file. It's placed on the root of the project.

### Gradle default project layout

A Gradle java project assumes to be structured as this 

![](images/Gradle_default_structure.PNG)


## DSL the Domain Specific Language

[Gradle DSL reference](https://docs.gradle.org/current/dsl/)

* Gradle is composed of two concepts
  * `Projects` : may represent the creation of a jar or a full deploy of an application on a server.
  A project is composed of several tasks
  * `Tasks` : some atomic job

Example of a gradle task

``` Groovy
task hello {
    doLast {
        println 'Hello world!'
    }
}

task count {
    doLast {
        4.times { print "$it " }
    }
}
```

Gradle allows to setup default tasks (executed if no other task specified)
 and dependencies between tasks

``` Groovy
defaultTasks 'clean', 'compile'

task clean {
    doLast {
        println 'clean something'
    }
 }
 
task compile {
    doLast {
        println 'compile code'
    }
 }
 
task other(dependsOn: 'compile') {
    doLast {
        println 'not a default task'
    }
  }
```

Gradle provides plugins to simplify tasks usage

``` Groovy
// Import the plugin to make build of a java project
apply plugin: 'java' 
```

A simple java project would be configured as this

``` Groovy
// Import the plugin to make build of a java project

group 'com.evs.training'
version = '1.0-SNAPSHOT'

apply plugin: 'java'

repositories {
    mavenCentral()
    maven {
        url "http://searchservicepoc.evs.tv:8081/repository/maven-snapshots/"
    }
}

dependencies {

   compile('com.fasterxml.jackson.datatype:jackson-datatype-jsr310:2.8.5')
   testCompile('com.google.guava:guava:21.0')
}

```

Each IDE has plugins to manage gradle projects. They configure the environment based on the
 gradle files content. You don't have to manage yourself the path, source level,... the plugin
 change the IDE configuration when you change the gradle files.
 
> Gradle projects are IDE agnostics. No need to share IDE configuration files, everything
is in the gradle files. **Never commit IDE configuration files in your VCS !**

### Manage multiple projects

Multi projects allows to separate purposes into a single build model
 
 ![](images/Gradle2.PNG)

File `settings.gradle` defines the project structure.
By default, Gradle uses the name of the directory as name of subproject and finds the settings.gradle 
location to determine the name of the root project.

``` Groovy
include 'common'
include 'api'
include 'impl'
``` 

The build.gradle file can apply general configuration for all or sub projects

``` Groovy
allprojects {
  group 'com.evs.training'
  version = '1.0-SNAPSHOT'
}

subprojects {
  apply plugin: 'java'  
}
``` 

Dependencies can be defined between projects

``` Groovy
dependencies {
  compile project(':common')
  compile project(':api')
}
``` 

### Source sets

Gradle allows you to group sources as a `source set` example of source sets are

* Unit tests
* Integration tests
* tools (a test client for your server project)

You can apply dependencies, tasks and so on on different source sets, by this way you can create multiple
jars or exclude tools from your build result,...

### Dependency management

Gradle supports both Maven and Ivy dependencies mechanisms. Here is a list of good practices recommended
 by gradle team about dependency management
 
* Put the Version in the Filename (Version the jar)
  * Its more clear to prevent dependency conflict and be warned if different jars of a same project
   as Hibernate are not in the same version
* Manage transitive dependencies
  * Only refer to first level dependency to avoid a spaghetti dependencies schema
* Resolve version conflicts
  * If two transitive dependencies has different versions, force one of them by checking api's differences
      guarantying a wanted comportment to your application.
* Use Dynamic Versions and Changing Modules
  * Use -SNAPSHOT versions of in-development dependencies and RELEASE versions of others
  
Dependencies can be declared by multiple ways

|Type	|Description|
|----|----|
|External module dependency	|A dependency on an external module in some repository.|
|Project dependency	|A dependency on another project in the same build.|
|File dependency	|A dependency on a set of files on the local filesystem.|
|Client module dependency	|A dependency on an external module, where the artifacts are located in some repository but the module meta-data is specified by the local build. You use this kind of dependency when you want to override the meta-data for the module.|
|Gradle API dependency	|A dependency on the API of the current Gradle version. You use this kind of dependency when you are developing custom Gradle plugins and task types.|
|Local Groovy dependency	|A dependency on the Groovy version used by the current Gradle version. You use this kind of dependency when you are developing custom Gradle plugins and task types.|

#### External module dependencies

External module dependencies are the most common dependencies. They refer to a module in an external repository.

``` Groovy
dependencies {
    runtime group: 'org.springframework', name: 'spring-core', version: '2.5'
    runtime 'org.springframework:spring-core:2.5',
            'org.springframework:spring-aop:2.5'
    runtime(
        [group: 'org.springframework', name: 'spring-core', version: '2.5'],
        [group: 'org.springframework', name: 'spring-aop', version: '2.5']
    )
    runtime('org.hibernate:hibernate:3.0.5') {
        transitive = true
    }
    runtime group: 'org.hibernate', name: 'hibernate', version: '3.0.5', transitive: true
    runtime(group: 'org.hibernate', name: 'hibernate', version: '3.0.5') {
        transitive = true
    }
}
``` 

#### Client module dependencies

Client module dependencies allow you to declare transitive dependencies directly in the build
 script. They are a replacement for a module descriptor in an external repository.

``` Groovy
dependencies {
    runtime module("org.codehaus.groovy:groovy:2.4.10") {
        dependency("commons-cli:commons-cli:1.0") {
            transitive = false
        }
        module(group: 'org.apache.ant', name: 'ant', version: '1.9.6') {
            dependencies "org.apache.ant:ant-launcher:1.9.6@jar",
                         "org.apache.ant:ant-junit:1.9.6"
        }
    }
}
``` 

#### Project dependencies

Gradle distinguishes between external dependencies and dependencies on projects which are part 
of the same multi-project build. For the latter you can declare Project Dependencies.

``` Groovy
dependencies {
    compile project(':shared')
}
```

#### File dependencies
File dependencies allow you to directly add a set of files to a configuration, without first adding
 them to a repository. This can be useful if you cannot, or do not want to, place certain files in a
  repository. Or if you do not want to use any repositories at all for storing your dependencies.
     
To add some files as a dependency for a configuration, you simply pass a file collection as a 
dependency:
     
``` Groovy
dependencies {
    runtime files('libs/a.jar', 'libs/b.jar')
    runtime fileTree(dir: 'libs', include: '*.jar')
}
``` 

#### Gradle API Dependency
You can declare a dependency on the API of the current version of Gradle by using the 
DependencyHandler.gradleApi() method. This is useful when you are developing custom Gradle 
tasks or plugins.
     
``` Groovy
 dependencies {
     compile gradleApi()
 }
``` 

#### Local Groovy Dependency
You can declare a dependency on the Groovy that is distributed with Gradle by using the 
DependencyHandler.localGroovy() method. This is useful when you are developing custom Gradle 
tasks or plugins in Groovy.
     
``` Groovy
dependencies {
    compile localGroovy()
}
``` 

#### Excluding transitive dependencies

You can exclude a transitive dependency either by configuration or by dependency:

``` Groovy
configurations {
    compile.exclude module: 'commons'
    all*.exclude group: 'org.gradle.test.excludes', module: 'reports'
}

dependencies {
    compile("org.gradle.test.excludes:api:1.0") {
        exclude module: 'shared'
    }
}
``` 

### Publishing artifacts

If the result of your build must be published on a maven repository (such as for library projects),
use the `uploadArchive` plugin.

``` Groovy
apply plugin: 'maven'

uploadArchives {
    repositories {
        mavenDeployer {
            repository(url: "file://localhost/tmp/myRepo/")
        }
    }
}
``` 

### Project properties

You can define properties available in your projet. By default, gradle sets some properties

|Name	            |Type	        |Default Value                              |
|:-----------------:|:-------------:|-------------------------------------------|
|project	        |Project	    |The Project instance                       |
|name	            |String	        |The name of the project directory.         |
|path	            |String	        |The absolute path of the project.          |
|description	    |String         |A description for the project.             |
|projectDir     	|File	        |The directory containing the build script. |
|buildDir	        |File	        |projectDir/build                           |
|group	            |Object	        |unspecified                                |
|version	        |Object	        |unspecified                                |
|ant	            |AntBuilder	    |An AntBuilder instance                     |

You can define local variables

``` Groovy
def dest = "dest"

task copy(type: Copy) {
    from "source"
    into dest
}
```

### Gradle wrapper

To avoid local installation, it's possible to include a gradle wrapper into the project.
 The wraper is named `gradlew`, the version of gradle used by the wraper is defined in
 the build.gradle file.

## References

* [Official Gradle site](https://gradle.org/)
* [Gradle DSL reference](https://docs.gradle.org/current/dsl/)
* [Gradle Slideshare presentation](https://fr.slideshare.net/jadsonjs/gradle-53757208)

## Books

* [Gradle in Action](https://www.manning.com/books/gradle-in-action)
* [Mastering Gradle](https://books.google.be/books/about/Mastering_Gradle.html?id=9qFNCgAAQBAJ&source=kp_cover&redir_esc=y&hl=fr)
* [Gradle Beyond the Basics](http://shop.oreilly.com/product/0636920019923.do?sortby=publicationDate)

# Math

* Overflows aren't not checked and don't throw exception.
* Division by zero produce NaN for floating point number and throw
  `ArithmeticException` for integer.
* The `Math` class provides several `...Exact()` methods checking overflow
  and throwing exceptions when occurring.
* The modifier `strictfp` can be applied to class, interface, and methods and
  guarantees that all floating point expressions must be those predicted by
  IEEE 754 arithmetic.
* The `StrictMath` class provides a portable, standard, and more strict
  arithmetic.

## References

* [`Math` class](http://docs.oracle.com/javase/8/docs/api/java/lang/Math.html)
* [FP-strict expressions](http://docs.oracle.com/javase/specs/jls/se8/html/jls-15.html#jls-15.4)
* [`StrictMath` class](http://docs.oracle.com/javase/8/docs/api/java/lang/StrictMath.html)
# A REST web app

## The solution

Here is a solution using Spring Boot.

#### References

* [JDK 8 API reference](https://docs.oracle.com/javase/8/docs/api/)
* [Gradle User Guide](https://docs.gradle.org/current/userguide/userguide.html)
# Map

* Map offers a typed key-value storage
* You can linked maps with map of maps
* The methods `keySet()` gives the list of keys
* Think to use` putIfAbsent()` instead of `put()` to avoid exception  

## Reference

[API documentation](http://docs.oracle.com/javase/8/docs/api/java/util/Map.html)# CompletableFuture

* Allow to return an object which will be completed later
* Manage cancellation
* Provides a `get()` blocking method executed when `CompletableFuture` is completed 
* May be run in parallel and synchronized 

## Reference

* [API documentation](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html)
* [CompletableFuture for Asynchronous Programming](https://community.oracle.com/docs/DOC-995305)# Interface

* An interface is a contract that must be followed by classes implementing it.
* An interface can't be instantiated.
* Java supports multiple interface implementations.
* An interface is declared with the keyword `interface`.
* A class implementing an interface with the keyword `implements`.
* An interface can extends another interface.
* There is no convention on the naming of an interface except it must be in camel case.
* It can contain abstract, default, and static methods.
* It can contain contants.
* Since Java8, an interface can contain default method implementation to propose new features
without breaking retro compatibility. Those methods must be leaded with the `default` keyword 
* Every member is public by default. The `public` modifier can be omitted.
* A class must override all methods defines in all interfaces defined in the `implements` declaration
  except default method (allowed but not mandatory for default methods).
* When creating an object implementing an interface, a good practice is to declare the variable
as the interface type and creating the object of the implementing class as `List myList = new ArrayList()`
where `List` is an interface and `ArrayList` a class implementing `List` interface

## References

* [Interface](http://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html)
* [Default and static methods](http://docs.oracle.com/javase/tutorial/java/IandI/defaultmethods.html)
# Stream

* Streams gives a way to operate treatment on iterations through a lambda expression
* Streams creates instances at the final operation only
* Streams can be paralleled user `parallelStream()` instead of `stream()` 
* Streams offers filtering, mapping, collecting, mathematical operations,...  

[Processing Data with Java SE 8 Streams](http://www.oracle.com/technetwork/articles/java/ma14-java-se-8-streams-2177646.html)
[Aggregate Operations](http://docs.oracle.com/javase/tutorial/collections/streams/index.html)
# List

* You get an element thanks to the method `List.get`. There is no `[]` operator.
* You can't create a list of primitive.
* `List` is an interface, there is multiple implementations providing thread-safe, thread-non safe, sorted, 
linked,... lists. The most used one is `ArrayList<T>`, check the
 [API documentation](http://docs.oracle.com/javase/8/docs/api/java/util/List.html) to choose your implementation
 when you have a specific usage.
* A `List` can contains null objects.
* A `List` can contains the same object multiple times
* When you need a distinct operation on a `List`, move it to a `Set` which can't contains null objects
and only one instance of the same object

## Reference

* [The method `List.get`](http://docs.oracle.com/javase/8/docs/api/java/util/List.html#get-int-)
* [The `Collection` interface](http://docs.oracle.com/javase/tutorial/collections/interfaces/collection.html)
* [The method `Arrays.asList`](http://docs.oracle.com/javase/8/docs/api/java/util/Arrays.html#asList-T...-)
# LINQ

* LINQ doesn't exist in Java.
* Stream will give you the same than LINQ to Objects.
* There are libraries that will give you LINQ-like queries such as Jinq or JOOQ.

## References

* [Stream API](http://docs.oracle.com/javase/8/docs/api/java/util/stream/package-summary.html)
* [AggregateOperations](http://docs.oracle.com/javase/tutorial/collections/streams/index.html)
* [Jinq](http://www.jinq.org/)
* [JOOQ](http://www.jooq.org/)
# Reflexion

* Allow to examine and modify objects at runtime
* Used by ide's and debug tools
* Can lead to performance issues 
* Can lead to side effects bugs by using private methods without following the normal path 

## Reference

* [API documentation](https://docs.oracle.com/javase/8/docs/api/java/lang/reflect/package-summary.html)
* [Reflexion tutorial](https://docs.oracle.com/javase/tutorial/reflect/)# Set

* You get elements with an iterator. There is no `get` method.
* You can't create a set of primitive.
* `Set` is an interface, there is multiple implementations providing thread-safe, thread-non safe,... sets.
 The most used one is `HashSet<T>`, check the
 [API documentation](http://docs.oracle.com/javase/8/docs/api/java/util/Set.html) to choose your implementation
 when you have a specific usage.
* A `Set` can't contains null objects or twice the same instance.
* If you add an instance to a Set that yet contains this instance, nothing happens 

## Reference

[API documentation](http://docs.oracle.com/javase/8/docs/api/java/util/Set.html)# Enumeration

* Enum is type safe.
* Enum is full-fleged reference type which means they are typesafe and can be
 extended by adding methods, fields or even implementing interfaces.
* Enum can be null.
* Enum interface can be completely defined.

## References

* [Enums](http://docs.oracle.com/javase/8/docs/technotes/guides/language/enums.html)
* [Enum Types](http://docs.oracle.com/javase/tutorial/java/javaOO/enum.html)
* [Enum class](http://docs.oracle.com/javase/8/docs/api/java/lang/Enum.html)
# Classes and Objects

* A class is the definition of an object.
* An object is an instance of a class.
* The phrase "instantiating a class" means the same thing as "creating an object." 
When you create an object, you are creating an "instance" of a class, therefore "instantiating" a class.
* All Java classes instances are children of `java.lang.Object`.
* The class of an object is an `Object` too.
* You can inherit from another class by using `extends` keyword.
* There is no multi-inheritance.
* A class declared `final` cannot be subclassed.
* A class is fully defined in one file, there is no partial class in Java. The name of the file
must match the name of the public class written in the file and the extension is `.java`.
* By default, a class is visible inside it's package and subpackages.
* A class marked as public is visible by all other classes.
  

## Reference

* [Classes and objects](http://docs.oracle.com/javase/tutorial/java/javaOO/index.html)
* [Object](https://docs.oracle.com/javase/8/docs/api/java/lang/Object.html)
* [Class](https://docs.oracle.com/javase/8/docs/api/java/lang/Class.html)
* [instanceof](http://docs.oracle.com/javase/specs/jls/se8/html/jls-15.html#jls-15.20.2)
* [Inheritance](http://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html)
# IntelliJ

For internal use, the wiki provides a 
[Quick start guide to set-up dev environnement](https://wiki.evs.tv/display/PRENG/Quick+start+guide+to+set-up+dev+environnement) 

## Editions

The Community edition is free and allows to develop java applications supporting all JavaSE libraries

The Ultimate edition is commercial and provides lot of tools useful for enterprise application development
 as database tools, JavaEE support, Spring integration ans many more.
 
Both editions comes with 32 and 64 bits launchers. A 32 bits JRE can manage a maximum of 2Gb od memory. 
 Use the 64 bits version to be able to allocate more memory to your IDE and give it better performances.

## Project organization

IntelliJ works with two main principles
* Project
  * A project is a workspace grouping all modules concerning a global project.
  * One instance of IntelliJ works with only one project at a time but you can open multiple 
  instances of IntelliJ working on different projects.
* Module
  * A module correspond to an application or an autonomous part of an application.
  * A module has it's own classpath.
  * A module is unique inside a project but can be shared by multiple projects.
  
When you create a project or a module, technical files (*.iml) or directories (.idea) are created.
  A good practice recommends to separate those files from you source files to void adding them to
  your source control.
```
└-IdeaProjects
|└-Project1
|└-Project2
└-Sources
 └-MyLib1
 └-MyLib2
 └-MyRepo1 
```

### Project creation

  There is many ways to create a project, here is an efficient one when working with maven or gradle projects.
  
  IntelliJ will analyse the maven or gradle configuration file to configure the module, that's why
  it's better to import modules from sources then letting it create the project just after the check-out 
  operation.
  
1. Clone your project into the `Sources` directory from git, either in command line, with an external tool
or withe IntelliJ menu "VCS > Checkout from version control > git". **In this latest case, reply "no" when 
Intellij ask you to create a project with the checked out sources.**
2. Create an empty project
   1. "File > New > Project"
   2. Choose "Empty project"
   3. Set a name and locate files in your `IdeaProjects` folder
3. Set the JDK of your project if not yet set.
4. Close the dialog
5. Create a module for your project sources
   1. "File > New > Module from existing sources"
   2. Select the `build.gradle` file of your project
   3. In the "Import Project" Gradle dialog, check the three checkboxes and select "Use gradle wrapper task configuration".
   
   ![](img/new_graddle_module.PNG)
   
Repeat 5 if you have multiple modules to import.  

## Configuration

 IntelliJ is full customizable, take time to show config and menus or explore documentation to take advantage of it.
 
 Here is some helpful tips.
 
### Shortcuts

The list os most used shortcuts is available on the menu "Help > Keymap reference"

To find any action inside the IDE use Find Action (`Ctrl+Shift+A`)

Some useful shortcuts :

|Action	                                        |Shortcut                     |
|-----------------------------------------------|---------------------------------|
|Basic code completion                          | `Ctrl+Space`|
|Smart Completion (context aware)               | `Ctrl+Shift+Space`|
|Statement Completion                           | `Ctrl+Shift+Enter`|
|Search everywhere	                            | `Double Shift` |
|Quick fix                                      |`Alt+Enter`|
|Documentation (Javadoc)                        | `Ctrl+Q`|
|Show usages                                    | `Ctrl+Alt+F7`|
|Move the current line of code	                | `Ctrl+Shift+Up` `Ctrl+Shift+Down`   |
|Duplicate a line of code	                    | `Ctrl+D`                          |
|Remove a line of code	                        | `Ctrl+Y`                          |
|Comment or uncomment a line of code	        | `Ctrl+Slash`                      |
|Comment a block of code	                    | `Ctrl+Shift+Slash`                |
|Find in the currently opened file	            | `Ctrl+F`                          |
|Find and replace in the current file	        | `Ctrl+R`                          |
|Next occurrence	                            | `F3`                              |
|Previous occurrence	                        | `Shift+F3`                        |
|Navigate between opened tabs	                | `Alt+Right Alt+Left`              |
|Navigate back/forward	                        | `Ctrl+Alt+Left` `Ctrl+Alt+Right`    |
|Expand or collapse a code block in the editor  | `Ctrl+NumPad plus` `Ctrl+NumPad -`  |
|Create new...	                                | `Alt+Insert`                      |
|Surround with	                                | `Ctrl+Alt+T`                      |
|Highlight usages of a symbol	                | `Ctrl+F7`                         |
|Rename	                                        |`Shift+F6`|
|Extract variable	                            |`Ctrl+Alt+V`|
|Extract field	                                |`Ctrl+Alt+F`|
|Refactor this	                                |`Ctrl+Shift+Alt+T`|
|Reformat code	                                |`Ctrl+Alt+L`|
|Auto-indent lines	                            |`Ctrl+Alt+I`|
|Optimize imports	                            |`Ctrl+Alt+O`|
|VCS Commit changes	                            |`Ctrl+K`|
|VCS Update project	                            |`Ctrl+T`|
|VCS Push commits	                            |`Ctrl+Shift+K`|
|Run	                                        |`Shift+F10`|
|Debug	                                        |`Shift+F9`|
|Debug Toggle breakpoint	                    |`Ctrl+F8`|
|Debug Step into	                            |`F7`|
|Debug Smart step into	                        |`Shift+F7`|
|Debug Step over	                            |`F8`|
|Debug Step out	                                |`Shift+F8`|
|Debug Resume	                                |`F9`|
|Debug Evaluate expression	                    |`Alt+F8`|
|Insert a live template.	|`Ctrl+J`|
|Surround with a live template.	|`Ctrl+Alt+J`|

Some often used expressions can be created by writing some letters and selecting code snippet. Here is a non exhaustive list.

|code     |   generated code                                      |
|---------|-------------------------------------------------------|
|`sout`   |`System.out.println();`                                |
|`fori`   |`for (int i = 0; i < ; i++) {  }`                      |
|`iten`   |`while (enumeration.hasMoreElements()) {`              |
|         |`Object nextElement =  enumeration.nextElement(); `    |
|         |         ` }`                                          |
|`iter`   |`for (Object o : ) { }`                                |
|`itar`   |`for (int i = 0; i < array.length; i++) {`             |
|         |              ` = array[i];`                           |
|         |      ` }`                                             |
|`psvm`   |`public static void main(String[] args) {}`            |
|`prsf`   |`private static final`                                 |

### Memory allocation
 
After installing IntelliJ you can allocate more memory to the IDE by acceding the 
"Help > Edit Custom VM Options..." menu. It will create a configuration file used to configure your JRE at startup.
  Change values of `Xms` and `Xmx` to allocate more memory. `Xms` set the memory allocation at startup,
   `Xmx` sets the maximum memory allocation.
  
  ```
  ...
  -Xms1024m
  -Xmx2048m
  ...
```

### Toolbars and menus

By default, IntelliJ hides menu, toolbars and tools boxes. You can show/hide them using `view` menu. 

### Code style

Settings can be customized for the IDE or for current project only with "File > Settings" for current project
or "File > other settings > Default settings" for entire IDE.

To change default code style (indentation, colors, braces placement,...) open settings and enter "Editor > Codestyle > Java"
section. The settings can be different for each file type.

>A wiki page explains [EVS conventions](https://wiki.evs.tv/pages/viewpage.action?pageId=22744423)

### Database tools

A database tools allows you to configure database connections and provides an SQL editor.

1. Click on Database tool window
2. Clock on green plus icon to create a new datasource and select the database type
3. Enter database connection info and click on the "Download drivers" on bottom of window if's the first time you
crete a connection for this type of database.
4. Click on test connection button.

You can navigate on schema. By double clicking a table, you open a grid view editable tab.

The black window icon on top of database tool window opens a SQL console.
 
### Version control
 
 If your sources are linked to a VCS as git, a `Version Control` tool windows shows the local modifications, the log,
  the console og git commands,...
  
 The local history can manage multiple change lists to organize your modified files into separate tasks. You can commit
  a change list in one operation by right clicking on the change list name. The commit message is the change list name by default
  
 A wiki page explains [how to link IntelliJ and Jira](https://wiki.evs.tv/pages/viewpage.action?pageId=28250345)
  to create change lists based on Jira issue information 

### Plugins

 A lot of plugins are available. You can install them through the settings windows.

 By default, the internal plugins list is display, those plugins manage classical frameworks or general purposes.
 
 You can click on `Browse repositories` button to search for third parties plugins. Interesting plugins are:
 * .ignore
 * Git Flow
 * Gradle
 * Groovy
 * SonarLint
 * Grep Console
 * String Manipulation
 
Warning, the wiki talks about `Save Action` plugin, by experience, this plugin is awful due to lags and side effects.
 
 When you open a file with an extension linked to an non installed existing plugin, IntelliJ propose to install it.
 
 Remember that your IDE could start less faster if you install too much plugins... 

### Code completion case sensitivity

By default IntelliJ IDEA code completion case sensitivity only affects the first letter you type. 
This strategy can be changed in the Settings/Preferences dialog, Editor | General | Code Completion, 
so you can make to either make the IDE sensitive to all letters or make it insensitive to the case at all, 
based on what better fits your preferences.

![](img/code_completion.png)

### Type migration
When you refactor, you usually rename symbols, or extract and move statements in the code.
 However, there’s more to refactoring than just that. For example, Type Migration 
 (available via `Ctrl+Shift+F6`) lets you change the type for a variable, field, parameter or a method’s 
 return value `(int → String`, `int → Long`, etc), update the dependant code, and resolve possible conflicts.

## References

* [Discover IntelliJ](https://www.jetbrains.com/help/idea/2017.1/discover-intellij-idea.html#EditorBasics)
* [IntelliJ documentation](https://www.jetbrains.com/idea/documentation/)
* [Youtube IntelliJ channel](https://www.youtube.com/user/intellijideavideo)# Collection Framework

* [Tutorial](http://docs.oracle.com/javase/tutorial/collections/index.html)
* [Collection Framework](https://docs.oracle.com/javase/8/docs/technotes/guides/collections/reference.html)
# Generics

* Java implements generics with type erasure. This allows backward
  compatibility.
* The prototype of a method can be declared with a wildcard type, i.e. an
  unknown parameter type.
* In Java, the derivation constraint is the only constraint that could be
  applied on a generic type.
* Generics don't support primitive as parameter type in Java.
* Generics are not transitive for inheritance between parameter types.
* Static fields cannot be of any generic type as they are shared with all
  instances.
* All the instances of a generic type have the same run-time class whatever
  their respective parameter types are.
* Java supports generic method.
* Array of a generic type can't be created.

## References

* [Generics](http://docs.oracle.com/javase/tutorial/extra/generics/intro.html)
* [Generics (updated)](https://docs.oracle.com/javase/tutorial/java/generics/index.html)
* [Type Erasure](http://docs.oracle.com/javase/tutorial/java/generics/erasure.html)
* [Specification of Type Erasure](http://docs.oracle.com/javase/specs/jls/se8/html/jls-4.html#jls-4.6)
* [Generic Method](http://docs.oracle.com/javase/tutorial/extra/generics/methods.html)
# Nested Classes

* A static nested class is declared inside another class. It has access only to
  the static members of the outer class.
* An inner class is non-static and its instance lives in the instance of an
  outer class. It has an implicit reference to the outer class `OuterClass.this`.
  It can't have any static members.
* A local class is an inner class declared in a block. It can capture local
  variables that are effectively final.
* An anonymous class is an expression creating an instance of anonymous subclass
  of a given class or interface and defining at the same time the interface
  of that anonymous subclass. It can capture any local variable
* Nested classes could lead to performance issues, do not abuse of them.
* Lambdas can replace nested class in some cases (handlers, threads,...)  

## References

* [Nested Class](http://docs.oracle.com/javase/tutorial/java/javaOO/nested.html)
# Class loader

* There is one class loader per `main()` method
* Class loader load classes first from current application class and then from classpath
  without order guarantee if two classes have same name in same package
* `ClassLoader` class is used to get resources from classpath  

## Reference

[API documentation](https://docs.oracle.com/javase/8/docs/api/java/lang/ClassLoader.html)# Event

* There is no event in Java.
* You have to simulate them with the Observer pattern or external frameworks as Akka or Guava.

## References

* [Observer Pattern](https://en.wikipedia.org/wiki/Observer_pattern)
* [Akka event bus](http://doc.akka.io/docs/akka/current/java/event-bus.html)
* [Guava event bus](https://google.github.io/guava/releases/19.0/api/docs/com/google/common/eventbus/EventBus.html)
* [Reactor event bus](https://spring.io/guides/gs/messaging-reactor/)
# The Game of Life

## Solution proposal

The current project offers a solution proposal for the game of life.

# Lambda

* Lambda expressions in Java are similar to C# or C++ ones, except `->`.
* An interface type with only one abstract method is a funtional interface.
* A lambda type is a defined thanks to a functional interface.
* The package `java.util.function` provides standard functional interfaces.
* There is reference to method that you can pass as lambda function.
* There is no delegate in Java, but a lambda function or a reference to a method
  achieves the same.

## References

* [Lambda Expressions](http://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html)
* [Syntax of Lambda Expressions](http://docs.oracle.com/javase/tutorial/java/javaOO/lambdaexpressions.html#syntax)
* [Method References](http://docs.oracle.com/javase/tutorial/java/javaOO/methodreferences.html)
* [Package `java.util.function`](http://docs.oracle.com/javase/8/docs/api/java/util/function/package-summary.html)
# JPA

Java Persistence Api is the JavaEE api used to persist data.

## Main principles

JPA defines how to declare and persist entities. An entity is a functional data model, entities
can be linked together with relations. This is a persistence abstraction, it means that the developer
does not matters how it's persisted, it can be in a database, in a file, in memory,...

In the code, an entity merged in the persistence context is consider as persisted, if the physical
linked storage is a database, that means that the data is inserted.

JPA is linked with the transactional API used in your application.

As JPA is most often implemented over a database, this article will make reference to database principles.

There is two ways to work with JPA : _code first_ or _database first_. In a code first view, JPA implementation
is able to create or upgrade the database based on Entities definition. In a database first view, JPA
implementation assumes that the database matches with entities definition.

## Entities

### Definition

An entity is a class annotated with JPA annotations. The class will be translated in a table in the 
database. A class is marked to be a table with the annotation `@Entity`

Attributes of the class are consider as table columns if they are annotated. An attribute is marked
to be a column with the annotation `@Column`

`@Entity` can be qualified with an attribute to set the corresponding table name.

`@Column` can be qualified by attributes to set additional corresponding column information as
* name
* insertable
* updatable
* length
* precision
* nullable
* unique

The primary key of the entity is annotated with `@Id`.

```Java
@Entity
public class Project {
    @Id 
    Long id;
     
    @Column
    String name;
    
    ...
}
```

### Primary keys

If you want to create an composite key, you
can either annotate different components of the key with the `@Id` annotation or create a separate class
annotated with `@Embeddable` ans use `@EmbeddedId` instead of `@Id` into the entity itself.

```Java
@Entity
public class Project {
    @Id 
    Integer departmentId;
    @Id
    Long projectId;
     
    @Column
    String name;
} 
```

or

```Java
@Entity
public class Project {
    @EmbeddedId 
    ProjectId id;
     
    @Column
    String name;
}
 ```
 ```Java
@Embeddable
public Class ProjectId {
    Integer departmentId;
    Long projectId;
}
```

If you want to get generated id's you can add `@GeneratedValue` on the `@Id` annotated attribute.
Four generation strategies are available:
* `@GeneratedValue(strategy=GenerationType.AUTO)` 
  * A unique generator will be used for all entities marked as well. The generator depends on the
   database vendor but is most often based on a sequence
* @GeneratedValue(strategy=GenerationType.IDENTITY)
  * it's quite the same as "AUTO" but a separate system will be used for each entity.
* `@GeneratedValue(strategy=GenerationType.SEQUENCE, generator="seq")` 
  * Use a specific sequence (named "seq" in the example) which must be declared with an other annotation
  `@SequenceGenerator(name="seq", initialValue=1, allocationSize=100)`
* `@GeneratedValue(strategy = GenerationType.TABLE, generator = "PK_Table")`
  * Use a table with last value by key, this table is used in an autonomous transaction and must be 
    declared with an annotation `@TableGenerator(name = "PK_Table", pkColumnValue = "MyEntity", pkColumnName = "ENTTY_NAME", allocationSize = 1, table = "PrimaryKeys", valueColumnName = "VAL")`

### Non persisted information

If you need to store information in the class which must not be persisted (as calculated field), 
you can annotate it with the `@Transient` annotation.

```Java
@Entity
public class Project {
    @Id 
    Integer departmentId;
    @Id
    Long projectId;
     
    @Column
    String name;
    
    @Transient
    String fullName = departmentId + "/" + projectId + "/" + name;
} 
```

### Data type conversion

JPA can work with most of java types but you can create your own converter if there is no default one.

```Java
@Converter
public class BooleanToIntegerConverter 
    implements AttributeConverter<Boolean, Integer> 
{  ... }
```

```Java
@Entity
@Table(name = "EMPLOYEE")
public class Employee
{

    @Id
    private Long id;

    @Column
    @Convert(converter = BooleanToIntegerConverter.class)
    private boolean fullTime;

}
```

If you're using the `java.util.Date` type, you can define if you want to store date only or datetime
by using additional annotation on the attribute
* `@Temporal(TemporalType.TIMESTAMP)`
  * Store a full date and time
* `@Temporal(TemporalType.DATE)`
  * Store date only
* `@Temporal(TemporalType.TIME)`
  * Store time only

Note that NIO2 `LocalDateTime` and `LocalDate` are managed in latest versions of JPA implementations even
if it not in the JPA 2.1 specification.

### Embedded entities

Embedded entities are used to create a class for specific information which will not be stored in a separated
table but inside the containing entity related table. You can override the name of the attribute to set
specific column name in your table

Following example will inject `AspectRation` columns into the `VideoEssence` table renaming default columns name:

```Java
@Embeddable
public class AspectRatio {

  @Column
  private Integer widthFactor;

  @Column
  private Integer heightFactor;
}
```
```Java
@Entity
public class VideoEssence {

...

@Embedded
    @AttributeOverrides( {
        @AttributeOverride(name="widthFactor", column = @Column(name="aspectRatioWidthFactor") ),
        @AttributeOverride(name="heightFactor", column = @Column(name="aspectRatioHeightFactor") )
    } )
    private AspectRatio aspectRatio;

...

}
```

### Multiple entities in a table with a discriminator field

If you need to store different entities in a single table, you can use a discriminator.

Following example will store `AudioEssence` and `VideoEssence` in the same `Essence` table:

Define an abstract class as base entity determining the name of the table and including all shared attributes.
`@DiscriminatorColumn` is used to define the name of the column containing the discriminator value.
```Java
@Entity
@DiscriminatorColumn(name = "ESSENCE_TYPE")
public abstract class Essence {

  @Id
  @GeneratedValue(strategy = GenerationType.AUTO)
  protected UUID id;

}
```

Extends the base entity and specify the discriminator value with `@DiscriminatorValue`
```Java
@Entity
@DiscriminatorValue("AUDIO")
public class AudioEssence extends Essence {

  @Column
    private Integer bitDepth;

}
```

```Java
@Entity
@DiscriminatorValue("VIDEO")
public class VideoEssence extends Essence {

    @Column
        private Integer height;
}
```

### Storing enumerations

Enums can be stored as strings (using `toString()` method) or as numerical values representing the index 
of the value in the Enum. This second method must be used with caution due to index modification during
the life of the application...

Use the `@Enumerated` annotation specifying the type of storage as attribute.

```Java
@Column
  @Enumerated(EnumType.STRING)
  private BitrateMode bitRateMode;
```
or
```Java
@Column
  @Enumerated(EnumType.ORDINAL)
  private BitrateMode bitRateMode;
```

### Annotations location

Attributes annotations can be placed on the attribute definition or on the attribute accessor (getter).
The difference consists on how JPA will access data of your class.

* Annotation on attribute use introspection to set/get data
* Annotation on accessor use accessor methods to set/get data

You can use only one method in a same entity. We recommend to use annotations on attributes definition 
to have a more comprehensive code and avoid side effects when changing accessors code.

### Concurrent modification
 
JPA provides a system to avoid concurrent modification conflicts. The `@Version` annotation.
This annotation can be set on a numeric or temporal field. JPA will increase the numeric field or set
the temporal field to "now" on each modification and will check that this information has not changed
between the retrieve and the update. If the version has changed, an `OptimisticLockException` is thrown. 

```Java
@Entity
public class MyEntity {    

    @Id
    @GeneratedValue
    private Long id;

    private String name;

    @Version
    private Long version;

    //...
}
```

### Partial entities

If you want to partially load an entity to avoid to get systematically a column filled with a big amount
of data you can use the `@Basic` annotation to lazily load it's value.

In the following example, when a `Message` is loaded, the `body` attribute is not loaded first. It will
be loaded when accessing the `body` attribute. 

```Java
@Entity
public class Message {    

    @Id
    @GeneratedValue
    private Long id;

    @Column
    private String subject;

    @Column
    @Basic(fetch=FetchType.LAZY)
    private String body;
    
}
```

## Relationship

Relationship between entities is the most difficult part of JPA and must be understood to avoid performance
issues.

Three main relations exists and their names are clear: `@OneToOne`, `@OneToMany` and `@ManyToOne`.

Relations are object based, it's a major difference with database relations where relation is only
represented with the primary key of the related table. It means that you have a parent object in each
child and a collection of children in the parent object. If you think on term of objects, it's normal
but it's not the first vision when you're used with database representation.

A basic relation would be:

```Java
@Entity
public class Parent {

  @Id
  private UUID id;
  
  @OneToMany
  private Set<Child> children = new HashSet<>();
}
```

```Java
@Entity
public class Child {

  @Id
  private UUID id;
  
  @ManyToOne
  private Parent parent;
}
```

Represented in database as
 
|PARENT|
|------|
|UUID  id|

|CHILD|
|------|
|UUID  id|
|UUID  parent_id|


> Use `Set` instead of `List` to store collections to avoid empty records !

When setting a `@ManyToMany` relationship, both entities have a collection of other entity.
It's impossible to represent it as is in the database. By default, JPA will create a association
table named with the name of the entities separated with an underscore and containing id's of 
linked entities. You can infer the association table creation with a `@JoinTable`

```Java
@Entity
public class Employee {
  @Id
  @Column(name="ID")
  private long id;
  ...
  @ManyToMany
  @JoinTable(
      name="EMP_PROJ",
      joinColumns=@JoinColumn(name="EMP_ID", referencedColumnName="ID"),
      inverseJoinColumns=@JoinColumn(name="PROJ_ID", referencedColumnName="ID"))
  private Set<Project> projects;
  .....
}
```
```Java
@Entity
public class Project {
  @Id
  @Column(name="ID")
  private long id;
  ...
  @ManyToMany(mappedBy="projects")
  private Set<Employee> employees;
  ...
}
```

To complete the definition of a relation, you have to determine the join column and determine if you
want a bi-directional relation. A bi-directional relation will set a `Parent` object in the `Child` entity,
an uni-directional relation (without the `mappedBy` attribute) will use a `UUID` instead of a `Parent` in the 
`Child`.

Bi-directional
```Java
@Entity
public class Parent {

  @Id
  private UUID id;
  
  @OneToMany(mappedBy="parent")
  private Set<Child> children = new HashSet<>();
}
```

```Java
@Entity
public class Child {

  @Id
  private UUID id;
  
  @ManyToOne
  @JoinColumn(name="parent_id")
  private Parent parent;
}
```

Uni-directional
```Java
@Entity
public class Parent {

  @Id
  private UUID id;
  
  @OneToMany
  private Set<Child> children = new HashSet<>();
}
```

```Java
@Entity
public class Child {

  @Id
  private UUID id;
  
  @Column(name="parent_id")
  private UUID parentId;
}
```

### Cascading actions

By default, operations on an entity are not cascaded to their relations. It means that if you delete
a parent, children are not deleted.

You can infer the cascading using attribute on relation annotation.

```Java
@Entity
public class Parent {

  @Id
  private UUID id;
  
  @OneToMany(cascade = CascadeType.ALL)
  private Set<Child> children = new HashSet<>();
}
```

Cascade types can be `ALL`, `DETACH`, `MERGE`, `PERSIST`, `REFRESH` or `REMOVE` and you can set a collection of 
values. See Entity Manager section for further details on those operations.

[CascadeType API](http://docs.oracle.com/javaee/7/api/javax/persistence/CascadeType.html)

>The cascading can be set on both side of the relation, be careful, if you set a cascade ALL on both side,
a delete on a child will invoke a delete on the parent and then on other children, it's not necessary
what is attendee.

### Lazy loading

By default, a relation is lazy loaded. It means that a request on a parent will fill a Parent object
with a collection of fake Children, you can count the children but when you want to get data from a 
child, a new request is done on the database to get information about this element.

The good thing is that your first query is quick and light but it means you need to stay in your
session to access children information. If your entity gets out of the transaction, a call to a child
attribute will cause an Exception.

If you want to load the whole information in the first query you can use the `fetch` attribute on the 
relation ans set it to `EAGER` instead of the default `LAZY`
 
```Java
@Entity
public class Parent {

  @Id
  private UUID id;
  
  @OneToMany(fetch = FetchType.EAGER)
  private Set<Child> children = new HashSet<>();
}
```

> Be careful, if your relations are set in EAGER mode, you could load all database in one query... 

Choosing between EAGER and LAZY is important in term of performance, memory impact and side effects.

### inner or outer join 
 
On a @OneToOne or a @ManyToOne relation, you can set an attribute `optional` which is default set to 
`true` and determines if the linked object is always set or not. If this attributes is set to `true`
the request will use an `outer join` but if the attributes is set to `false`, an `inner join` will be used.

In term of performance, an inner join is better but can be used only if all references exists. Think to
set this attribute correctly to improve performance without having false empty result sets.


## The Entity Manager

The `EntityManager` is the entry point to the persistence context. It's configured to receive a datasource
and is injected as a bean in your dto's.

```Java
@Repository
public class JPARecorderDAO implements RecorderDAO{

    @PersistenceContext
    private EntityManager em;
}
```

[EntityManager API](http://docs.oracle.com/javaee/7/api/javax/persistence/EntityManager.html)

You can use the EntityManager to make a lot of operations with entities as basic ones

* `persist` : Make an entity persistent (insert)
* `merge` : Merge the state of a persisted entity into the persistence context (update) 
* `find` : Gets a persisted entity by it's ID (select)
* `refresh` : reload the current state of a loaded entity
* `remove` : Remove an entity from the persistence context (delete, no instance returned)
* `detach` : Remove an entity from the persistence context but keep it detached (delete and remove ID from returned instance)

`EntityManager` is also the entry point to make more complex data manipulation as queries, criteria,...

## Data manipulation

### Queries

Queries are an easy way to make data manipulation. It's very close to a SQL query execution.

#### JPQL

As JPA is implementation agnostic, it does not use `SQL` but `JPQL`. Both syntax are very closed but
JPQL is talking about entities, you are querying entities and filtering on attributes, relations are known, you don't have to 
set joins if the relations are defined in the entities.

The folowing code will return the Parent with ID `parentId` with all its children:
```Java
Parent parent = em.createQuery("SELECT p FROM Parent p WHERE p.id=:parent_id", Parent.class)
                              .setParameter("parent_id", parentId)
                              .getSingleResult();
```

The following code will return a list of Child with a parent named "John":
```Java
List<Child> children = em.createQuery("SELECT c FROM Child c WHERE c.parent.name=:parent_name", Child.class)
                              .setParameter("parent_name", "John")
                              .getResultList();
```

#### Named queries

To get queries and entities together, you can store often used queries directly in the entity and 
give them names. It's called `named queries`.

```Java
@Entity
@NamedQueries({
  @NamedQuery(
    name="findAllParentsWithName",
    query="SELECT p FROM Parent p WHERE p.name LIKE :parentName"),
  @NamedQuery(
    name="findAllParentsOlderThen",
    query="SELECT p FROM Parent p WHERE p.birthday < :searchDate")
})
public class Parent {

  @Id
  private UUID id;
  
  @Column
  private String name;
  
  @Column
  private LocalDate birthday;
}
```

You can use thous named queries through the entity manager

```Java
List<Parent> parents = em.createNamedQuery("Parent.findAllParentsWithName", Parent.class)
                              .setParameter("parentName", "John")
                              .getResultList();
```

#### Native queries

If you need to use a specific platform SQL syntax which has no equivalent in JPQL, you can use native
SQL syntax. This must be used only when mandatory because you're linking your application to a specific
database implementation.

```Java
Query q = em.createNativeQuery("SELECT p.name, to_date(p.birthday,'dd/MM/YY') FROM parent_table p WHERE p.id = :id");
q.setParameter("id", UUID.fromString("f83f5cf7-a662-4d62-99d5-ea1042a322e7"));
Object[] parent = (Object[]) q.getSingleResult();
```

> In a native query, use the database tables and columns name, not entities one

### Criteria

When a request must be dynamically generated, you can use the `criteria` API. A criteria is an object
aggregating filters, predicates,... to create complex where clause, grouping,...

How to generate this sql in criteria ?

```SQL
SELECT c FROM Country c WHERE c.population > :p
```

```Java
CriteriaBuilder cb = em.getCriteriaBuilder();
 
  CriteriaQuery<Country> q = cb.createQuery(Country.class);
  Root<Country> c = q.from(Country.class);
  ParameterExpression<Integer> p = cb.parameter(Integer.class);
  q.select(c).where(cb.gt(c.get("population"), p));
```

Criteria can quickly be complex but allows a lot of dynamic features.

```Java
CriteriaQuery<Pet> cq = cb.createQuery(Pet.class);
Root<Pet> pet = cq.from(Pet.class);
cq.groupBy(pet.get(Pet_.color));
cq.having(cb.in(pet.get(Pet_.color)).value("brown").value("blonde"));
```

```Java
Map<SingularAttribute<Transaction, ?>, Object> params = ...;
CriteriaBuilder cb = em.getCriteriaBuilder();           
CriteriaQuery<Tuple> cq = cb.createTupleQuery();     
Root<Transaction> r = cq.from(Transaction.class);

Predicate p= cb.conjunction();
for (Map.Entry<SingularAttribute<Transaction, ?>, Object> param: params.entrySet())
    p = cb.and(p, cb.equal(r.get(param.getKey()), param.getValue()));

cq.multiselect(r.get(Transaction_.id), r.get(Transaction_.status), 
          r.get(Transaction_.created_at))
    .where(p)
    .orderBy(cb.asc(r.get(Transaction_.id)));

List<Tuple> result = em.createQuery(cq).getResultList();
```
### Entity graph

Lazy loading was often an issue with JPA 2.0. You have to define at the entity if you want to use 
FetchType.LAZY (default) or FetchType.EAGER to load the relation and this mode is always used. 
FetchType.EAGER is only used if we want to always load the relation. FetchType.LAZY is used in 
almost all of the cases to get a well performing and scalable application.

But this is not without drawbacks. If you have to use an element of the relation, you need to make 
sure, that the relation gets initialized within the transaction that load the entity from the 
database. This can be done by using a specific query that reads the entity and the required 
relations from the database. But this will result in use case specific queries. Another option 
is to access the relation within your business code which will result in an additional query for 
each relation. Both approaches are far from perfect.

JPA 2.1 entity graphs are a better solution for it. The definition of an entity graph is independent 
of the query and defines which attributes to fetch from the database. An entity graph can be used 
as a fetch or a load graph. If a fetch graph is used, only the attributes specified by the entity 
graph will be treated as FetchType.EAGER. All other attributes will be lazy. If a load graph is 
used, all attributes that are not specified by the entity graph will keep their default fetch type.

#### Example

For this example we will use an order with a list of items and each item has a product. All 
relations are lazy.

**The Order entity**
```Java
@Entity
@Table(name = "purchaseOrder")
@NamedEntityGraph(name = "graph.Order.items", 
               attributeNodes = @NamedAttributeNode(value = "items", subgraph = "items"), 
               subgraphs = @NamedSubgraph(name = "items", attributeNodes = @NamedAttributeNode("product")))
public class Order implements Serializable {

   @Id
   @GeneratedValue(strategy = GenerationType.AUTO)
   @Column(name = "id", updatable = false, nullable = false)
   private Long id = null;
   @Version
   @Column(name = "version")
   private int version = 0;

   @Column
   private String orderNumber;

   @OneToMany(mappedBy = "order", fetch = FetchType.LAZY)
   private Set<OrderItem> items = new HashSet<OrderItem>();

   ...
   
```

**The OrderItem entity**
```Java
@Entity
public class OrderItem implements Serializable
{

   @Id
   @GeneratedValue(strategy = GenerationType.AUTO)
   @Column(name = "id", updatable = false, nullable = false)
   private Long id = null;
   @Version
   @Column(name = "version")
   private int version = 0;

   @Column
   private int quantity;

   @ManyToOne
   private Order order;

   @ManyToOne(fetch = FetchType.LAZY)
   private Product product;
   
```

**The Product entity**
```Java
@Entity
public class Product implements Serializable
{

   @Id
   @GeneratedValue(strategy = GenerationType.AUTO)
   @Column(name = "id", updatable = false, nullable = false)
   private Long id = null;
   @Version
   @Column(name = "version")
   private int version = 0;

   @Column
   private String name;
```

**Named entity graph**

The definition of a named entity graph is done by the `@NamedEntityGraph` annotation at the entity.
It defines a unique name and a list of attributes (the attributeNodes) that have be loaded.
The following example shows the definition of the entity graph `graph.Order.items` which will load 
the list of `OrderItem` of an `Order`.

```Java
@Entity
@Table(name = "purchase_order")
@NamedEntityGraph(name = "graph.Order.items", 
      attributeNodes = @NamedAttributeNode("items"))
public class Order implements Serializable {

   ...
```

Now that we have defined the entity graph, we can use it in a query. Therefore we need to create a 
Map with query hints and set it as an additional parameter on a find or query method call.
The following code snippet shows how to use a named entity graph as a fetch graph in a find statement.

```Java
EntityGraph graph = this.em.getEntityGraph("graph.Order.items");

Map hints = new HashMap();
hints.put("javax.persistence.fetchgraph", graph);

return this.em.find(Order.class, orderId, hints);
```

**Named sub graph**

We used the entity graph to define the fetch operation of the Order entity. If we want to do the 
same for the OrderItem entity, we can do this with an entity sub graph. The definition of a named 
sub graph is similar to the definition of an named entity graph and can be referenced as an 
attributeNode.

The following code snippets shows the definition of a sub graph to load the Product of each 
OrderItem. The defined entity graph will fetch an Order with all OrderItems and their Products.

```Java
@Entity
@Table(name = "purchase_order")
@NamedEntityGraph(name = "graph.Order.items", 
               attributeNodes = @NamedAttributeNode(value = "items", subgraph = "items"), 
               subgraphs = @NamedSubgraph(name = "items", attributeNodes = @NamedAttributeNode("product")))
public class Order implements Serializable {
```
  
What’s happening inside?

OK, from a development point of view entity graphs are great. They are easy to use and we do not 
need to write additional code to avoid lazy loading issues. But what is happening inside? How many 
queries are send to the database? Lets have a look at the hibernate debug log.

```LOG
2014-03-22 21:56:08,285 DEBUG [org.hibernate.loader.plan.build.spi.LoadPlanTreePrinter] (pool-2-thread-1) LoadPlan(entity=blog.thoughts.on.java.jpa21.entity.graph.model.Order) - Returns - EntityReturnImpl(entity=blog.thoughts.on.java.jpa21.entity.graph.model.Order, querySpaceUid=<gen:0>, path=blog.thoughts.on.java.jpa21.entity.graph.model.Order) - CollectionAttributeFetchImpl(collection=blog.thoughts.on.java.jpa21.entity.graph.model.Order.items, querySpaceUid=<gen:1>, path=blog.thoughts.on.java.jpa21.entity.graph.model.Order.items) - (collection element) CollectionFetchableElementEntityGraph(entity=blog.thoughts.on.java.jpa21.entity.graph.model.OrderItem, querySpaceUid=<gen:2>, path=blog.thoughts.on.java.jpa21.entity.graph.model.Order.items.<elements>) - EntityAttributeFetchImpl(entity=blog.thoughts.on.java.jpa21.entity.graph.model.Product, querySpaceUid=<gen:3>, path=blog.thoughts.on.java.jpa21.entity.graph.model.Order.items.<elements>.product) - QuerySpaces - EntityQuerySpaceImpl(uid=<gen:0>, entity=blog.thoughts.on.java.jpa21.entity.graph.model.Order) - SQL table alias mapping - order0_ - alias suffix - 0_ - suffixed key columns - {id1_2_0_} - JOIN (JoinDefinedByMetadata(items)) : <gen:0> -> <gen:1> - CollectionQuerySpaceImpl(uid=<gen:1>, collection=blog.thoughts.on.java.jpa21.entity.graph.model.Order.items) - SQL table alias mapping - items1_ - alias suffix - 1_ - suffixed key columns - {order_id4_2_1_} - entity-element alias suffix - 2_ - 2_entity-element suffixed key columns - id1_0_2_ - JOIN (JoinDefinedByMetadata(elements)) : <gen:1> -> <gen:2> - EntityQuerySpaceImpl(uid=<gen:2>, entity=blog.thoughts.on.java.jpa21.entity.graph.model.OrderItem) - SQL table alias mapping - items1_ - alias suffix - 2_ - suffixed key columns - {id1_0_2_} - JOIN (JoinDefinedByMetadata(product)) : <gen:2> -> <gen:3> - EntityQuerySpaceImpl(uid=<gen:3>, entity=blog.thoughts.on.java.jpa21.entity.graph.model.Product) - SQL table alias mapping - product2_ - alias suffix - 3_ - suffixed key columns - {id1_1_3_} 

2014-03-22 21:56:08,285 DEBUG [org.hibernate.loader.entity.plan.EntityLoader] (pool-2-thread-1) Static select for entity blog.thoughts.on.java.jpa21.entity.graph.model.Order [NONE:-1]: select order0_.id as id1_2_0_, order0_.orderNumber as orderNum2_2_0_, order0_.version as version3_2_0_, items1_.order_id as order_id4_2_1_, items1_.id as id1_0_1_, items1_.id as id1_0_2_, items1_.order_id as order_id4_0_2_, items1_.product_id as product_5_0_2_, items1_.quantity as quantity2_0_2_, items1_.version as version3_0_2_, product2_.id as id1_1_3_, product2_.name as name2_1_3_, product2_.version as version3_1_3_ from purchase_order order0_ left outer join OrderItem items1_ on order0_.id=items1_.order_id left outer join Product product2_ on items1_.product_id=product2_.id where order0_.id=? 
```

The log shows that only one query is created. Hibernate uses the entity graph to create a load plan 
with all 3 entities (Order, OrderItem and Product) and load them with one query.

#### Dynamic graph

You can also create a graph dynamically without defining it in the entity. Remember that in a graph 
mode, all attributes are lazily loaded except if you specify a `@Basic` annotation to force eager mode.

```Java
@Entity
public class EmailMessage implements Serializable {
    @Id    
    String messageId;
    @Column
    @Basic(fetch=EAGER)
    String subject;
    @Column
    String body;
    @Column
    String sender;
    @OneToMany(mappedBy="message", fetch=LAZY)
    Set<EmailAttachment> attachments;
    ...
}
```

With a `fetch graph`, you force a graph without taking care of existing annotations. This example will
load only the `body` attribute ignoring existing predicates :

```Java
EntityGraph<EmailMessage> eg = em.createEntityGraph(EmailMessage.class);
eg.addAttributeNodes("body");
...
Properties props = new Properties();
props.put("javax.persistence.fetchgraph", eg);
EmailMessage message = em.find(EmailMessage.class, id, props);
```

If you want to customize existing graph definitions or `@Basic` predicates, use a `load graph`.
This example will load the entire entity without attachments but including the body :

```Java
EntityGraph<EmailMessage> eg = em.createEntityGraph(EmailMessage.class);
eg.addAttributeNodes("body");
...
Properties props = new Properties();
props.put("javax.persistence.loadgraph", eg);
EmailMessage message = em.find(EmailMessage.class, id, props);
```

[Entity Graphs tutorial](https://docs.oracle.com/javaee/7/tutorial/persistence-entitygraphs.htm)

## Spring data integration

Spring provides a way to expose data with a JPA implementation through [Spring Data JPA project](http://projects.spring.io/spring-data-jpa/).

The idea is to provide default DAO methods on an entity. Just create a DAO interface extending `JpaRepository`
and use it...

```Java
public interface CustomerRepository extends JpaRepository<Customer, Long> {
    
}
```

The `JpaRepository` must be typed with your entity and the type of the ID. It provides lots of methods
described in the [JpaRepository API](http://docs.spring.io/spring-data/jpa/docs/current/api/org/springframework/data/jpa/repository/JpaRepository.html)

* count()
* delete(ID)
* delete(Entity)
* deleteAll()
* FindOne(ID)
* ...

Data can be paginated or sorted using `PagingAndSortingRepository` methods or versioned using a 
`RevisionRepository`.

Spring data also provides an automatic query tool based on the method name called Query Derivation Mechanism.
By adding a method with a name beginning with `findBy` followed by the name of an attribute of the 
entity, a query will be generated at runtime to get all occurrences of the entity with the 
corresponding attribute value

```Java
public interface CustomerRepository extends JpaRepository<Customer, Long> {
    List<Customer> findByLastName(String lastName);
}
```
This method declaration will generate automatically this code at runtime without implementing yourself:
```Java
return em.createQuery("SELECT c from Customer c where c.lastName = :lastName",Customer.class)
  .setParameter("lastName",lastName)
  .getResultList();
```

## Reference

* [The Java EE Tutorial : Persistence](http://docs.oracle.com/javaee/7/tutorial/partpersist.htm#BNBPY)
* [JPA API reference](https://docs.oracle.com/javaee/7/api/javax/persistence/package-summary.html)
* [Java persistence wiki book](https://en.wikibooks.org/wiki/Java_Persistence)# A REST web app

## The problem

We're going to develop an application listing live events such as concerts,
conferences, or sport games. Meta data can be added to a given
event. The web app should either respond with JSON payload.

We will create a REST service using Spring Boot persisting data with JPA and
 use the Chrome app [Postman](https://chrome.google.com/webstore/detail/postman/fhbjgbiflinjbdggehcddcbncdddomop)
 as client. 

## Technologies

### Spring

Let's first have a look to Spring. This framework is largely used in enterprise 
java applications, a good knowledge of Spring is necessary in many cases.
 
[Spring introduction](../spring/README.md)
 
### Spring Boot
 
Spring Boot is a project from Spring.io which allows to quickly create applications.

[Spring Boot introduction](../springboot/README.md)

 
### JPA

JPA is an API of JaveEE providing a persistence context. It's major implementation
is Hibernate. JPA will be used in this project to persist information in a database.

[JPA introduction](../jpa/README.md)


## Our server

### A basic Rest server with Spring Boot

With the help of [this tutorial](https://spring.io/guides/gs/rest-service/), create a basic Spring Boot application. 

### Add a health check

Add actuator dependency to give a "/health" mapping to your application.

### A route to add events

Add a POST route to add a JSON event.
Persist events in a Map

### A route to get events

Add GET route to get an event based on it's id

### Events persistence

Replace Map persistence by an H2 database storage

# For-each Loop

* As C# and C++, Java has an iteration construct.
* It allows to iterate through collection implementing the interface
  `java.lang.Iterable`.
* Instead of iterating in a loop or in a `for` statement, you can use the `foreach()` function 
  with a lambda expression
  
  
```java
List<String> myList = new ArrayList<>();
myList.add("One");
myList.add("Two");
myList.add("Three");

// Simple for loop
for (int i = 0; i < myList.size(); i++) {
    System.out.println(myList.get(i));
}

// For each loop
for (String s : myList) {
    System.out.println(s);
}

// Iteration
Iterator<String> e = myList.iterator();
while (e.hasNext()) {
    System.out.println(e.next());
}

// foreach() function
myList.forEach(s -> System.out.println(s));
myList.forEach(System.out::println);

// foreach() on a Stream
myList.stream().forEach(s -> System.out.println(s));
myList.stream().forEach(System.out::println);

// foreach() using parallel threads on Streams
myList.parallelStream().forEach(s -> System.out.println(s));
myList.parallelStream().forEach(System.out::println);

```

> **Warning** Never add or remove an element of the collection while looping on it! 

Never this:
```java
for (car : cars) {
 	if (car.something()) {
 		cars.remove(car)
 	}
 }
```

Prefer use iterator:
```java
Iterator<Car> iterator = cars.iterator();
while (iterator.hasNext()) {
    Car car = iterator.next();
    if (car.something()) {
        iterator.remove();
    }
}
```

Or use streams:
```java
List<Car> toRemove = cars.stream.filter(Car::something()).collect(Collectors.toList());
cars.removeAll(toRemove);
```

Or better since Java 8:
```java
cars.removeIf(Car::something());
```

## References

* [For statement](http://docs.oracle.com/javase/tutorial/java/nutsandbolts/for.html)
* [Interface `Iterable`](https://docs.oracle.com/javase/8/docs/api/java/lang/Iterable.html)
