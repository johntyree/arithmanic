#!/usr/bin/env python
# coding: utf8

from setuptools import setup

with open('README.md')as f:
    long_desc = f.read()

setup(name='arithmanic',
      version='0.0.1',
      author='John Tyree',
      author_email='johntyree@gmail.com',
      license='GPL2',
      url='http://github.com/johntyree/arithmanic',
      description="A tool for working on mental arithmetic",
      keywords="mental math arithmetic",
      long_description=long_desc,
      entry_points={
          'console_scripts': ['arithmanic = arithmanic:main'],
      },
      classifiers=[
          "Development Status :: 3 - Alpha",
          "License :: OSI Approved :: "
          "GNU General Public License v2",
      ])
