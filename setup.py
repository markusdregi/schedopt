#!/usr/bin/env python

from setuptools import setup, find_packages

_requirements = []
with open('requirements.txt', 'r') as f:
    _requirements = [line.strip() for line in f]

setup(
    name='schedopt',
    packages = find_packages(),
    author='Markus Dregi',
    author_email='markusdregi@gmail.com',
    version = '0.0.1',
    description = 'Workshop schedule optimizer.',
    install_requires=_requirements,
)
