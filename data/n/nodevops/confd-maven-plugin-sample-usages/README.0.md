= README
NoDevops team <team@nodevops.io>
1.0, July 19, 2016, Springboot Application + confd-maven-plugin example
:toc:
:icons: font
:quick-uri: https://github.com/nodevops/confd-maven-plugin/

== What?

This maven project is a (very) simple Springboot project that uses the link:https://github.com/nodevops/confd-maven-plugin/[confd maven plugin]
to generate its configuration.

== Directory structure

* src/main/confd/templates : the directory where *all* the confd templates are stored
* src/main/confd/dictionaries : the directory where the dictionaries are stored (a single local dictionary in our case)
* src/main/assembly : the directory where is store the assembly descriptor that the project uses to generate the _confd_ files (templates and toml files)
* src/main/java : application source

== Files of interest

* src/main/confd/templates/application.yml.tmpl
* src/main/confd/dictionaries/local.dict
* pom.xml

Please note that there is no application.properties/yml in the src/main/resources dir, this is by design so that we never ship such a file in our jar (obviously, the default config stuff provide by SpringBoot is still there)

== Use Cases

=== Local Development

We want to be able to generate our config file for the local dev environment, and use it, so:

* we rely on the common/shared configuration (i.e. not associated to a specific profile) that calls the _prepare_ goal of the plugin. The _prepare_ goal will generate a *confd* _toml_ configuration file that would target a final generated file in the `target/generated-configuration` directory
* we activate a `run-local` profile that triggers the _generate_ goal that will process the template according to our local dictionary stored in `src/main/confd/dictionary/local.dict`
* because we want the build to be independent of the dev environment, we use the _java-processor_ that doesn't rely on the _confd_ binary
* the `run-local` profile also specifies to springboot where it can find its config file (through the springboot plugin, with the customized argument `--spring.config.location=file:target/generated-configuration/application.yml`

To test your project locally, use `mvn spring-boot:run` or the following combo to use the fatjar generated:

[source, shell]
----
mvn clean package
java -jar target/myfatjar.jar --spring.config.location=file:target/generated-configuration/application.yml
----

=== Get ready for the delivery

We want to generate a configuration artifact that will carry the templates and the ready to use confd toml files

* we rely on the common/shared configuration, that only calls the _prepare_ goal
* we use a dedicated `delivery` profile that overrides the final destination of the target file (that will be stored in the _toml_ config file)
* the same `delivery` profile uses the assembly plugin to generate a zip file that can be unzipped as-is in the `/etc/confd` directory on the destination server(s). This is the default directory structure expected by the confd binary



