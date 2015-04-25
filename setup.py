#!/usr/bin/env python

import sys
from setuptools import setup, find_packages
from setuptools.command.test import test as TestCommand

setup(
    name='libmtl',
    version='0.0.1',
    description=(
        "Get abbrev for Montreal arrondissement and vice versa fuzzily",
    ),
    author='Antoine Reversat',
    author_email='a.reversat@gmail.com',
    url='https://github.com/crevetor/libmtl',
    packages=find_packages(exclude=("tests*",)),
    install_requires=['python-levenshtein'],
    license='GPLv2',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Software Development :: Testing',
        'Topic :: Internet :: WWW/HTTP',
        'License :: OSI Approved :: GPL',
    ]
)
