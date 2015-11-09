
#!/usr/bin/env python
#
# Setup script for the Natural Language Toolkit
#
# Copyright (C) 2001-2015 NLTK Project
# Author: Steven Bird <stevenbird1@gmail.com>
#         Edward Loper <edloper@gmail.com>
#         Ewan Klein <ewan@inf.ed.ac.uk>
# URL: <http://nltk.org/>
# For license information, see LICENSE.TXT

# Work around mbcs bug in distutils.
# http://bugs.python.org/issue10945

import os

# setuptools
from setuptools import setup, find_packages
from pip.req import parse_requirements

install_reqs = parse_requirements(<requirements_path>)
reqs = [str(ir.req) for ir in install_reqs]

setup(name='PyLinguistics',
      version='1.0',
      description='Python Distribution Utilities',
      author='Vinicius Woloszyn',
      author_email='vinicius@open.inf.br',
      url='http://inf.ufrgs.br/~vwoloszyn/',
      packages=['distutils', 'distutils.command'],
      license="GPLv3",
      install_requires =reqs

     )
