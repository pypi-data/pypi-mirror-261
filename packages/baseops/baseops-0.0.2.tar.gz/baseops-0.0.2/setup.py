#!/bin/bash

from setuptools import setup, find_packages

setup(
    name='baseops',
    version='0.0.2',
    packages=['baseops'],
    install_requires=['pandas','tqdm']
)