#!/usr/bin/env python

from distutils.core import setup
from pip.req import parse_requirements

setup(name='PyLinguistics',
      version='1.0',
      description='Python Distribution Utilities',
      author='Vinicius Woloszyn',
      author_email='vinicius@open.inf.br',
      url='http://inf.ufrgs.br/~vwoloszyn/',
      packages=['distutils', 'distutils.command'],
      license="GPLv3",
      install_requires = [str(ir.req)
                        for ir in parse_requirements('requirements.txt')]

     )
