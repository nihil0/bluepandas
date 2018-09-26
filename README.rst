===========
BluePandas
===========

A Python library to read files in Azure Blob Storage as Pandas DataFrames

Installation
-------------

The latest version is available on PyPI::

    pip install bluepandas

Example
--------

The library reads an environment variable containing the connection string to your
blob storage account. The variable must be named ``AZ_<STORAGE-ACCOUNT-NAME>``.


.. image:: http://i68.tinypic.com/2jfbnfp.png

Short example::

    import bluepandas

    df = bluepandas.read_csv("wasbs://<container-name>@<storage-account-name>.blob.core.windows.net/path/to/your.csv")





