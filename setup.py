try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

config = {
    'description': 'Module to access azure blob CSV files with Pandas',
    'author': 'Neelabh Kashyap',
    'url': '',
    'download_url': '',
    'author_email': 'neelabh.kashyap@cgi.com',
    'version': '0.1',
    'install_requires': ['pytest'],
    'packages': find_packages(exclude=['contrib', 'docs', 'tests']),
    'scripts': [],
    'name': 'bluepandas'
}

setup(**config)