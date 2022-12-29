## blueprint-cli-multicommands-python

[![ci](https://github.com/FabienArcellier/blueprint-cli-multicommands-python/actions/workflows/main.yml/badge.svg)](https://github.com/FabienArcellier/blueprint-cli-multicommands-python/actions/workflows/main.yml)

blueprint to implement a multi commands in python. This command can be install
on remote system or CI with pip

* execute operation in CI
* execute command for user
* install a new command on OS
* ...

## Getting started

1. clone this repository

2. remove .git directory

3. use your library identifier as module name

    * rename `src/mycommand` into your own package name
    * you have to change as well inside `pyproject.toml` and `.coveragerc`

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

```bash
poetry install
```

### Update release dependencies

```bash
poetry update
```

### Activate python virtual environment

```bash
poetry shell
```

### Run the continuous integration process

Before commit or send a pull request, you have to execute `pylint` to check the syntax
of your code and run the unit tests to validate the behavior.

```bash
make ci
```

## Contributors

* Fabien Arcellier

## License

MIT License

Copyright (c) 2018-2022 Fabien Arcellier

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
