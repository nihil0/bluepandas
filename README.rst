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
blob storage account. The variable must be named ``AZ_<STORAGE-ACCOUNT-NAME>``  
and set to your connection string, which is obtained from the Azure Portal by 
navigating to you storage account under settings/access keys as shown below


.. image:: http://i67.tinypic.com/25sljxt.png

Short example on usage::

    import bluepandas

    df = bluepandas.read_csv("wasbs://<container-name>@<storage-account-name>.blob.core.windows.net/path/to/your.csv")





