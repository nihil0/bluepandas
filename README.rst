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

Reading a data frame
~~~~~~~~~~~~~~~~~~~~~~
::
    
    import bluepandas

    df = bluepandas.read_csv("wasbs://<container-name>@<storage-account-name>.blob.core.windows.net/path/to/your.csv")

This returns a BluePandas data frame, which subclasses the pandas data frame, but allows you to write to Blob Storage using the ``write_csv()`` method. 

Writing a data frame
~~~~~~~~~~~~~~~~~~~~~~
::
    
    import bluepandas
    
    # Import the iris dataset
    from sklearn import datasets
    
    values = datasets.load_iris()['data']
    columns = datasets.load_iris()['feature_names']
    
    df = bluepandas.DataFrame(values, columns=columns)
    
    df.to_csv("wasbs://<container-name>@<storage-account-name>.blob.core.windows.net/path/to/iris.csv", index=False)
    
Converting a pandas data frame to a BluePandas data frame
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
::
    
    import pandas as pd
    import bluepandas
    
    df = pd.DataFrame([(1,2,3),(4,5,6)], columns=['A','B','C'])
    
    # BluePandas data frame
    bpd_df = bluepandas.DataFrame(df.values, columns=df.columns)
    

.. |build| image:: https://dev.azure.com/nihil0/bluepandas/_apis/build/status/nihil0.bluepandas
.. _build: https://dev.azure.com/nihil0/bluepandas/_build/latest?definitionId=1

.. |release| image:: https://vsrm.dev.azure.com/nihil0/_apis/public/Release/badge/6b10a683-55d0-4844-a53d-e972b2f200b6/1/1
.. _release: https://dev.azure.com/nihil0/bluepandas/_releases2?definitionId=1&view=mine&_a=releases


