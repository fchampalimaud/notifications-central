#!/usr/bin/python
# -*- coding: utf-8 -*-

# TODO change package name to `pyforms-web-notifications`

__author__ = "Ricardo Ribeiro"
__credits__ = "Ricardo Ribeiro"
__maintainer__ = ["Ricardo Ribeiro"]
__email__ = ["ricardojvr@gmail.com"]
__status__ = "Development"

import re
from setuptools import setup

version, license = None, None
with open('notifications/__init__.py', 'r') as fd:
    content = fd.read()
    version = re.search(r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)
    license = re.search(r'^__license__\s*=\s*[\'"]([^\'"]*)[\'"]', content, re.MULTILINE).group(1)
if version is None: raise RuntimeError('Cannot find version information')
if license is None: raise RuntimeError('Cannot find license information')

setup(
    name='notifications-central',
    url='https://github.com/fchampalimaud/notifications-central.git',
    version=version,
    description="""""",
    author='Ricardo Ribeiro',
    author_email='ricardo.ribeiro@research.fchampalimaud.org',
    license=license,
    packages=['notifications'],
    include_package_data=True,
)
