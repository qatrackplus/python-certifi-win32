import sys
import os

from setuptools import setup
from distutils.sysconfig import get_python_lib

setup_kwargs = dict(
    name = 'python-certifi-win32',
    version = '1.0',
    description = 'Add windows certificate store to certifi cacerts.',
    author = 'Andrew Leech',
    author_email = 'andrew.leech@planetinnovation.com.au',
    license = 'BSD',
    url = 'https://gitlab.com/alelec/python-certifi-win32',
    packages = ['python-certifi-win32'],
    package_dir = {'python-certifi-win32': 'src'},
    data_files = [(get_python_lib(prefix=''), ['python-certifi-win32-init.pth'])],
    install_requires = ['wrapt>=1.10.4', 'wincertstore', 'certifi'],
)

setup(**setup_kwargs)
