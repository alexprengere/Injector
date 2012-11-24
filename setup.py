#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
Main installation file for Injector.
'''

from setuptools import setup

setup(
    name = 'Injector',
    version = '0.1',
    author = 'Alex Prengere',
    author_email = 'alex.prengere@gmail.com',
    description = 'Inject delimiter into positional data feed.',
    # Manage standalone scripts
    entry_points = {
        'console_scripts' : [
            'inject = inject:main'
        ]
    },
    py_modules = [
        'inject'
    ]
)

