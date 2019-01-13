# build command : docker build -t kapacitor_atomiq_p3:1.5.0 --build-arg HTTPS_PROXY=http://genproxy.amdocs.com:8080 --build-arg HTTP_PROXY=http://genproxy.amdocs.com:8080 /home/dockerFile/py3/

FROM kapacitor:1.5.0

COPY Miniconda3-latest-Linux-x86_64.sh /home/dockerFile/Miniconda3-latest-Linux-x86_64.sh
COPY udf-py3.zip /home/dockerFile/udf-py3.zip
COPY influxdb-5.0.0-py2.py3-none-any.whl /home/dockerFile/influxdb-5.0.0-py2.py3-none-any.whl

RUN http_proxy='http://genproxy.amdocs.com:8080/' apt-get install bzip2 && \
	http_proxy='http://genproxy.amdocs.com:8080/' apt-get install unzip
	
RUN bash /home/dockerFile/Miniconda3-latest-Linux-x86_64.sh -b

RUN export HTTP_PROXY='http://genproxy.amdocs.com:8080/' && \
	export HTTPS_PROXY='http://genproxy.amdocs.com:8080/' && \
	cd /root/miniconda3/bin && \
	/root/miniconda3/bin/conda config --set always_yes True && \
	/root/miniconda3/bin/conda config --set proxy_servers http:http://genproxy.amdocs.com:8080 && \
	/root/miniconda3/bin/conda config --set proxy_servers https:http://genproxy.amdocs.com:8080 && \
	/root/miniconda3/bin/conda install --channel "anaconda" pandas && \
	/root/miniconda3/bin/conda install --channel "anaconda" scikit-learn && \
 	/root/miniconda3/bin/conda install --channel "anaconda" scipy && \
	/root/miniconda3/bin/conda install --channel "anaconda" statsmodels && \
	/root/miniconda3/bin/conda install --channel "anaconda" h5py && \
	/root/miniconda3/bin/conda install --channel "conda-forge" fbprophet && \
	/root/miniconda3/bin/conda install --channel "conda-forge" pystan && \
	/root/miniconda3/bin/conda install --channel "conda-forge" toml

RUN cd /root/miniconda3/bin && \
	/root/miniconda3/bin/pip install --proxy http://genproxy.amdocs.com:8080 protobuf==3.0.0b2
	
RUN cd /root/miniconda3/bin && \
	/root/miniconda3/bin/pip install /home/dockerFile/influxdb-5.0.0-py2.py3-none-any.whl

RUN cd /home/dockerFile && \
    unzip /home/dockerFile/udf-py3.zip -d /home/dockerFile/ && \
	cd /home/dockerFile/udf-py3/udf-py3/agent/py/ && \
	/root/miniconda3/bin/python3 /home/dockerFile/udf-py3/udf-py3/agent/py/setup.py build && \
	/root/miniconda3/bin/python3 /home/dockerFile/udf-py3/udf-py3/agent/py/setup.py install
	
RUN sed 's/from matplotlib import pyplot as plt/#from matplotlib import pyplot as plt/g' /root/miniconda3/lib/python3.6/site-packages/fbprophet/forecaster.py > /home/dockerFile/for1.py && \
	sed 's/from matplotlib.dates import MonthLocator, num2date/#from matplotlib.dates import MonthLocator, num2date/g' /home/dockerFile/for1.py > /home/dockerFile/for2.py && \
	sed 's/from matplotlib.ticker import FuncFormatter/#from matplotlib.ticker import FuncFormatter/g' /home/dockerFile/for2.py > /home/dockerFile/for3.py && \
	cp -f /home/dockerFile/for3.py /root/miniconda3/lib/python3.6/site-packages/fbprophet/forecaster.py
	
RUN rm -rf /home/temp && \
	rm -rf /home/dockerFile
