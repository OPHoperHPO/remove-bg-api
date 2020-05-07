"""Setup script"""
# -*- coding: utf-8 -*-

from setuptools import find_packages
from distutils.core import setup

with open('README.md') as f:
    readme = f.read()

setup(
    name='remove_bg_api',
    version='0.2.1',
    description='Remove.bg Python API Wrapper',
    license='MIT',
    author='Anodev (OPHoperHPO)',
    keywords = ['remove_bg_api', 'removebg', 'api', "wrapper"],
    author_email='netbook21@mail.ru',
    url='https://github.com/OPHoperHPO/remove_bg_api',
    long_description=readme,
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
