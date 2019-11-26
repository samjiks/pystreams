#!/usr/bin/env python

from os.path import exists
from setuptools import setup
import streams

packages = ['streams']


setup(name='pystreams',
      version=streams.__version__,
      description='Streams',
      url='http://github.com/samjiks/pystreams/',
      maintainer='Samuel Thampy',
      maintainer_email='samjiks@hotmail.com',
      license='BSD',
      keywords='streams',
      python_requires='>=3.5',
      packages=['streams'],
      setup_requires=['pytest-runner'],
      tests_require=['pytest'],
      long_description=(open('README.md').read() if exists('README.rst')
                        else ''),
      install_requires=list(open('requirements.txt').read().strip().split('\n')),
      zip_safe=False)