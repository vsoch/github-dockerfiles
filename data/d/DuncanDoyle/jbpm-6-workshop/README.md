# JBoss BPMSuite 6 Workshop

This is a workshop for JBoss BPMSuite 6. It provides an introduction into the core concepts, APIs, etc. The workshop comes with a series of labs that mainly focus on process creation, human tasks
asynchronous execution, custom workitemhandlers, process event listeners and custom marshallers. They take a novice user of the platform from a set of simple rules to more complex constructs through a series of lab exercises that gradually introduce new concepts and gradually increase complexity.

## Workshop Documentation
The documentation of the workshop, including the description of the labs and exercises can be found [here](docs/jbpm-6-workshop.adoc)

## Interesting links:
* [The jBPM project](http://www.jbpm.org)
* [The JBoss BPMSuite platform](http://www.redhat.com/en/technologies/jboss-middleware/bpm)

*
*
*
To build this images:
1) Add the following files to the "dockerfile_copy" directory:
- jboss-eap-6.4.0.zip
- jboss-eap-6.4.5-patch.zip
2) Run "build_image.sh".

To build this images:
1) Add the following files to the "dockerfile_copy" directory:
- jboss-bpmsuite-6.2.0.GA-deployable-eap6.x.zip
- jboss-bpmsuite-6.2.0.GA-maven-repository.zip
- jboss-bpmsuite-6.2.0.GA-supplementary-tools.zip
2) Run the "prebuild-prepare.sh" script, which will create a PostgreSQL EAP module ZIP.
3) Run "build_image.sh".

