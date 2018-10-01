===========
BluePandas |build|_ |release|_
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


.. |build| image:: https://dev.azure.com/nihil0/bluepandas/_apis/build/status/nihil0.bluepandas
.. _build: https://dev.azure.com/nihil0/bluepandas/_build/latest?definitionId=1

.. |release| image:: https://vsrm.dev.azure.com/nihil0/_apis/public/Release/badge/6b10a683-55d0-4844-a53d-e972b2f200b6/1/1
.. _release: https://dev.azure.com/nihil0/bluepandas/_releases2?definitionId=1&view=mine&_a=releases


