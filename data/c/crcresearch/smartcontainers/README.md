# SmartContainers (sc) for docker enabled software and data preservation [![codecov.io](https://codecov.io/github/crcresearch/smartcontainers/coverage.svg?branch=master)](https://codecov.io/github/crcresearch/smartcontainers?branch=master)

SmartContainers is python wrapper for docker that facilitates the recording
and tracking of provenance information using the W3C recommendation [prov-o](http://www.w3.org/TR/prov-o/).
SmartConainers is being developed as part of the Data and Software Preservation  for Open Science [(DASPOS)](http://daspos.org) project.

Current build status  build status: [![Build Status](https://travis-ci.org/crcresearch/smartcontainers.svg?branch=master)](https://travis-ci.org/crcresearch/smartcontainers)

SmartContainers provides a command line tool, sc, that provides a surrogate for the docker command line tool.

```bash
sc --docker <docker command line>
```

Will create a docker label with provenance metadata using the W3C Prov-o vocabulary with respect to the
computational environment created or provided by a particular docker container.

A python setup file is provided for installation of the command line utility. It is recommended to install the tool in a Python virtual environment since the tool is under heavy development.

```bash
pip install .
```

Will install the tool and it's dependencies in a virtual environment.

### User Identity setup
On first use after installation, the sc command will guide the user through connecting the tool with the
users [ORCID](http://orcid.org). It is recommended to setup a ORCID account to connect to the tool. If the user chooses
not to create an ORCID account, the tool with prompt for a First and Last name, email and organization for provenance information. A global configuration file will be created in the user that contains this information so it only needs to be input once. The configuration file will be written to a `.sc` directory created in your home directory.  In the future, the configuration file location will be a user option.

### Purpose
For data to be useful to scientists, data must be accompanied by the context of how it is captured, processed, analyzed, and other provenance information that identify the people and tools involved in this process. In the Computational Sciences, some of this context is provided by the identity of software, workflows and the computational environment where these computational activities take place. Smart Containers is a tool that wraps the standard docker commandline tool with the intent to capture some of this context that is naturally associated with a Docker based infrastructure. We capture this metadata using linked open data principles and web standard vocabularies such as the W3C Prov-O [recommendation](https://www.w3.org/TR/prov-o/) to facilitate interoperability and reuse. This provenance information is attached directly to a docker container label using [JSON-LD](http://json-ld.org) thus "*infecting*" containers and images derived from the original container resource with contextual information necessary to understand the identity of the contained computational environment and activities that environment affords.

Use of linked data principles allow us to link to other vocabularies and incorporate other efforts such as [Mozilla Science's Code as a Research Object](https://github.com/codemeta/codemeta), [Schema.org](https://schema.org/Code), [dbpedia](http://dbpedia.org/ontology/Software) software vocabularies and [ORCID](http://orcid.org/) to provide broader context for how a Docker container may be provisioned utilizing ["Five Stars of Linked Data Vocabulary Use"](http://www.semantic-web-journal.net/content/five-stars-linked-data-vocabulary-use) recommendation. We have extended the Prov-O notion of Activity by creating the [formal ontology pattern](http://linkedscience.org/wp-content/uploads/2015/04/paper2.pdf)  of [Computational Activity](https://github.com/Vocamp/ComputationalActivity) and a taxonomy to capture Computational Environment . Lastly, we provide the ability for scientific data to be published and preserved, along with it's provenance using a docker container as a "research bundle". We utilize ideas from the [W3C Linked Data Platform](https://www.w3.org/TR/ldp/) recommendation and W3C work on ["Linked Data Fragments"](http://linkeddatafragments.org/) using the [Hydra Core Vocabulary](https://www.hydra-cg.com/spec/latest/linked-data-fragments/), that is still in the development stage, to provide metadata for data entry points inside the docker container as well as the ability to attach rdf metadata to non-rdf dataset resources, which is a common use case in the sciences.
