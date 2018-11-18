## blueprint-cli-multicommands-python

[![Build Status](https://travis-ci.org/FabienArcellier/blueprint-cli-multicommands-python.svg?branch=master)](https://travis-ci.org/FabienArcellier/blueprint-cli-multicommands-python)

blueprint to implement a multi commands in python. This command can be install
on remote system or CI with pip

* execute operation in CI
* execute command for user
* install a new command on OS
* ...
* implementation compatible with python2.7 and python3.6

## Getting started

1. clone this repository

2. remove .git directory

3. use your library identifier as module name

    * replace `mycommand`, `mycommand_tests` by your own identifier
    * you have to change as well inside `Makefile`, `.coveragerc`, `tox.ini` and `setup.py`

## The latest version

You can find the latest version to ...

```bash
git clone https://github.com/FabienArcellier/blueprint-cli-multicommands-python.git
```

## Usage

You can run the application with the following command

```bash
python -m mycommand.cli command1 --name fabien

# inside a virtualenv or after installation with pip
mycommand command1 --name fabien
```

## Developper guideline

### Install development environment

Use make to instanciate a python virtual environment in ./venv and install the
python dependencies.

```bash
make install_requirements_dev
```

### Update release dependencies

Use make to instanciate a python virtual environment in ./venv and freeze
dependencies version on requirement.txt.

```bash
make update_requirements
```

### Activate the python environment

When you setup the requirements, a `venv` directory on python 3 is created.
To activate the venv, you have to execute :

```bash
make venv
source venv/bin/activate
```

### Run the linter and the unit tests

Before commit or send a pull request, you have to execute `pylint` to check the syntax
of your code and run the unit tests to validate the behavior.

```bash
make lint
make tests
```

## Contributors

* Fabien Arcellier

## License

A short snippet describing the license (MIT, Apache, etc.)
