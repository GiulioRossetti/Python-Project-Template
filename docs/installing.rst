**********************
Installing PackageName
***********************

Before installing ``PackageName``, you need to have setuptools installed.

=============
Quick install
=============

Get ``PackageName`` from the Python Package Index at pypl_.

or install it with

.. code-block:: python

    pip install package_name

and an attempt will be made to find and install an appropriate version that matches your operating system and Python version.
Please note that ``PackageName`` requires Python>=3.8

You can install the development version with

.. code-block:: python

    pip install git+https://github.com/USERNAME/project.git


Alternatively, you can install using conda:

.. code-block::

    conda config --add channels package_owner_repository
    conda config --add channels conda-forge
    conda install package_name



=====================
Optional Dependencies
=====================

``PackageName`` relies on a few packages calling C code that can be cumbersome to install on Windows machines: to address such issue, the default installation does not try to install set up such requirements.

Such a choice has been made to allow (even) Windows user to install the library and get access to its core functionalities.

To made available (most of) the optional packages you can either:

- (Windows) manually install the optional packages (versions details are specified in ``requirements_optional.txt``) following the original projects guidelines, or
- (Linux/OSX) run the command:

.. code-block:: python

    pip install package_name[flag]



Such caveat will install everything that can be easily automated under Linux/OSX.

======================
Installing from source
======================

You can install from source by downloading a source archive file (tar.gz or zip) or by checking out the source files from the GitHub source code repository.

``PackageName`` is a pure Python package; you don’t need a compiler to build or install it.

-------------------
Source archive file
-------------------
Download the source (tar.gz or zip file) from pypl_  or get the latest development version from GitHub_

Unpack and change directory to the source directory (it should have the files README.txt and setup.py).

Run python setup.py install to build and install

------
GitHub
------
Clone the ``PackageName`` repostitory (see GitHub_ for options)

.. code-block:: python

    git clone https://github.com/USERNAME/project.git

Change directory to project

Run python setup.py install to build and install

If you don’t have permission to install software on your system, you can install into another directory using the --user, --prefix, or --home flags to setup.py.

For example

.. code-block:: python

    python setup.py install --prefix=/home/username/python

or

.. code-block:: python

    python setup.py install --home=~

or

.. code-block:: python

    python setup.py install --user

If you didn’t install in the standard Python site-packages directory you will need to set your PYTHONPATH variable to the alternate location. See http://docs.python.org/2/install/index.html#search-path for further details.

============
Requirements
============
------
Python
------

To use ``PackageName`` you need Python 3.8 or later.

The easiest way to get Python and most optional packages is to install the Enthought Python distribution “Canopy” or using Anaconda.

There are several other distributions that contain the key packages you need for scientific computing. 


.. _pypl: https://pypi.python.org/pypi/package_name/
.. _GitHub: https://github.com/USERNAME/project/
