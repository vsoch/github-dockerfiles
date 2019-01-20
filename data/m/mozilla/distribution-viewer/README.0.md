Testing on ATMO
===============

By default any Python files that are executed are run with a Jupyter driver, so
the following environment variables need to be set (or unset) to run standalone:

  export PYSPARK_DRIVER_PYTHON=/mnt/anaconda2/bin/python
  unset PYSPARK_DRIVER_PYTHON_OPTS

Secure copy ('scp') the Python file to the host machine.

Next you can submit the Python file to Spark, with the specified arguments to
more closely match how Airflow will execute jobs:

  spark-submit --executor-cores 8 --master yarn --deploy-mode client "./aggregate-and-import.py"

