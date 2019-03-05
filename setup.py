#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages

setup(
    author='gescande',
    author_email='escande.guillaume@gmail.com',
    description="robscreen",
    scripts=['robscreen/robscreen_main.py'],
    license='MIT',
    name='robscreen',
    version='0.0.1',
    include_package_data=True,
    packages=find_packages(exclude=('tests', 'docs')),
    package_data={'robscreen': ['resources/*']},
    test_suite="tests",
    tests_require=[
        'pytest'
    ],
    install_requires=[
        'firob'
    ]
)
