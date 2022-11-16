# Python Project Template
[![SBD++](https://img.shields.io/badge/Available%20on-SoBigData%2B%2B-green)](https://sobigdata.d4science.org/group/sobigdata-gateway/explore?siteId=20371853)
[![Black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

A small template project to exemplify the use of GitHub Actions to automatically build and publish a Python package to PyPI (and Conda).

The project is a simple Python package that contains an object class, an object container ad a few functions to sort them and convert from/to JSON.

The project comes with:
- a few GitHub Actions to automatically build and publish the package to PyPI (and Conda) when a new release is created (or on demand);
- a GitHub Action to check the code quality using CodeQL;
- a GitHub Action to check compliance with Black code style;
- a few tests to exemplify the use of pytest;
- a minimal sphinx documentation to exemplify the use of sphinx and readthedocs;
- a minimal configuration files to exemplify the use of gitignore and coveragerc;
- a minimal setup.py to exemplify the use of setuptools.

## Packaging and Distribution

For a detailed guide refer to: 
- pip installable package: [Python Packaging User Guide](https://packaging.python.org/en/latest/);
- conda installable package: [Conda Packaging Guide](https://docs.conda.io/projects/conda-build/en/latest/user-guide/tutorials/build-pkgs.html).
Here a small summary of the most important steps.


### Pypi test (optional, for testing only)

Create a [PyPi test](https://test.pypi.org/) account and a new project (using [twine](https://packaging.python.org/en/latest/guides/using-testpypi/)). 
Then, create a new token and copy it.
Go to the GitHub project settings and add a new secret named TEST_PYPI_API_TOKEN and paste the token as value. 
Finally, go to the project settings and enable the GitHub Actions.

### PyPi

Create a [PyPi](https://pypi.org/) account and a new project (using [twine](https://packaging.python.org/en/latest/guides/distributing-packages-using-setuptools/)). 
Then, create a new token and copy it. 
Go to the GitHub project settings and add a new secret named PYPI_API_TOKEN and paste the token as value. 
Finally, go to the project settings and enable the GitHub Actions. 


### Conda
 
Create an Anacoda account.
Get an Anaconda token (with read and write API access) at

**anaconda.org/USERNAME/settings/access**

Go to the GitHub project settings and add a new secret named ANACONDA_TOKEN and paste the token as value. 
Finally, go to the project settings and enable the GitHub Actions.

## Documentation (ReadTheDocs)

Create a [ReadTheDocs](https://readthedocs.org/) account and import the GitHub project. 

To generate the documentation locally (after having installed ``sphinx``, ``sphinx_rtd_theme`` and ``mock`` using **pip**) move to the ``docs`` folder and run:

```bash 
make html
```

To clean the generated documentation run:

```bash 
make clean
```

