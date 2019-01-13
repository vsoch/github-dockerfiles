# ATT&CK Python Client

A Python module to access up to date ATT&CK content available in STIX via public TAXII server. This project leverages the python classes and functions of the [cti-python-stix2](https://github.com/oasis-open/cti-python-stix2) and [cti-taxii-client](https://github.com/oasis-open/cti-taxii-client) libraries developed by MITRE.

# Goals

* Provide an easy way to access and interact with up to date ATT&CK content available in STIX via public TAXII server
* Allow security analysts to quickly explore ATT&CK content and apply it in their daily operations
* Allow the integration of ATT&Ck content with other platforms to host up to date information from the framework
* Help security analysts during the transition from the ATT&CK MediaWiki API to the STIX/TAXII 2.0 API
* Learn STIX2 and TAXII Client Python libraries

# Current Status: Beta

The project is currently in a beta stage, which means that the code and the functionality is changing, but the current main functions are stabilising. I would love to get your feedback to make it a better project.

# Resources

* [MITRE CTI](https://github.com/mitre/cti)
* [OASIS CTI TAXII Client](https://github.com/oasis-open/cti-taxii-client)
* [OASIS CTI Python STIX2](https://github.com/oasis-open/cti-python-stix2)
* [MITRE ATT&CK Framework](https://attack.mitre.org/wiki/Main_Page)
* [ATT&CK MediaWiki API](https://attack.mitre.org/wiki/Using_the_API)
* [Invoke-ATTACKAPI](https://github.com/Cyb3rWard0g/Invoke-ATTACKAPI)
* [Mitre-Attack-API](https://github.com/annamcabee/Mitre-Attack-API)

# Getting Started

## Requirements

Python 3+

## Installation

You can install it via PIP:

```
pip install attackcti
```

Or you can also do the following:

```
git clone https://github.com/Cyb3rWard0g/ATTACK-Python-Client
cd ATTACK-Python-Client
pip install .
```

## Jupyter Notebooks - Code Integration

I created a few jupyter notebooks that I hope can help you get familiar with the library and allow you to implement it in your future projects.

* [Basic Functionality](https://github.com/Cyb3rWard0g/ATTACK-Python-Client/blob/master/notebooks/Usage_Basics.ipynb)
* [Custom Filters](https://github.com/Cyb3rWard0g/ATTACK-Python-Client/blob/master/notebooks/Usage_Filters.ipynb)

Install **Jupyter Lab** and **Pandas** in order to use the Jupyter Notebooks on your own. You can do it by using the **requirements.txt** file in this repo

```
pip install -r requirements.txt
```

Start Jupyter Lab by running the following commands in the root directory of the repo

```
cd notebooks
jupyter lab
```

# Author

* Roberto Rodriguez [@Cyb3rWard0g](https://twitter.com/Cyb3rWard0g)

# Contributors

* Jose Luis Rodriguez [@Cyb3rPandaH](https://twitter.com/Cyb3rPandaH)

# Contributing


# To-Do

* [ ] Revokation logic to update Groups Objects
* [ ] Integration with HELK
