This is where the packaging stuff for zenoss-*-service packages goes.

Usage: make deb or make rpm. Both options package $(NAME)-service-$(PKG_VERSION).
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
Note: files in this directory are shared by NameNode, DataNode, and SecondaryNameNode services by means of symlinks. 
This directory contains a python script (bench.py) to generate fake application templates for benchmark testing, and a directory containing a model service with service definitions stubbed to deploy a web server in place of each service. The directory can be used by the script to generate templates for load testing or benchmarking.

Given a directory with a service tree and a path to a subtree within that directory, bench.py will create a copy of the directory which contains the requested number of copies of the subtree. If the -t or -z flag is given, it will also create a template file for use with serviced. The -z argument will map zendev/devimg:europa in for zenoss/zenoss5x, which will generate a template that can be used with a zendev deployment. The -t argument will generate a template for normal use.

For full command usage, run `bench.py -h`.
