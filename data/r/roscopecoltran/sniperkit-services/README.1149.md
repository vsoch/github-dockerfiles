
# python3-ml-jupyter
Docker image providing ZeroMQ + JZMQ + Scala + Python 3.5.2 environment + ML Libs + Jupyter Notebook

numpy, scipy, scikit-learn, pandas, tensorflow, h5py, keras

FROM deepcortex/python3-ml-jupyter:latest

To run locally ```make && make run```

To run as a docker image ```docker run --rm -it -p 8888:8888 -v <local-projects-path>:/home/projects deepcortex/python3-ml-jupyter```