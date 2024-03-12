#!/bin/bash

from setuptools import setup, find_packages

setup(
    name='baseops',
    version='0.0.1',
    packages=['baseops'],
    install_requires=['pandas','tqdm'],
    entry_points={'console_scripts':[
        'count-nulls = baseops.qtnulls:count_nulls']
    }
)