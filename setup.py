#!/usr/bin/env python
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

setup(
    name='mylib',
    version='1.0.0',
    packages=find_packages(exclude=["*_tests"]),
    license='Creative Commons Attribution-Noncommercial-Share Alike license',
    long_description=open('README.md').read(),
    install_requires = [
        'click'
    ],
    entry_points = {
        'console_scripts': [
            'mycommand = mycommand.cli:cli',
        ],
    }
)
