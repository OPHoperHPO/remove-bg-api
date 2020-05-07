"""Setup script"""
# -*- coding: utf-8 -*-

from setuptools import find_packages
from distutils.core import setup

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
    keywords = ['removebg.py', 'removebg', 'api', "wrapper"],
    author_email='netbook21@mail.ru',
    url='https://github.com/OPHoperHPO/removebg.py',
    license=lic,
    long_description_content_type='text/markdown',
    packages=find_packages(exclude=('docs', 'examples')),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
        'Intended Audience :: Developers',  # Define that your audience are developers
        'License :: OSI Approved :: MIT License',  # Again, pick a license
        'Programming Language :: Python :: 3',  # Specify which pyhton versions that you want to support
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
)
