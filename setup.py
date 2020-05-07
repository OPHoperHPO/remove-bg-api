"""Setup script"""
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.md') as f:
    readme = f.read()

with open('LICENSE') as f:
    lic = f.read()

setup(
    name='removebg.py',
    version='0.2.0',
    description='Remove.bg Python API Wrapper',
    long_description=readme,
    author='Anodev (OPHoperHPO)',
    author_email='netbook21@mail.ru',
    url='https://github.com/OPHoperHPO/removebg.py',
    license=lic,
    packages=find_packages(exclude=('docs', 'examples'))
)
