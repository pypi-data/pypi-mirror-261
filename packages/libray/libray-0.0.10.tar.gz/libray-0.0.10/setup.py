#!/usr/bin/env python3
# -*- coding: utf8 -*-


from setuptools import setup


with open('README.md') as f:
  long_description = f.read()


setup(
  name="libray",
  version="0.0.10",
  description='A Libre (FLOSS) Python application for unencrypting, extracting, repackaging, and encrypting PS3 ISOs',
  long_description=long_description,
  long_description_content_type='text/markdown',
  author="Nichlas Severinsen",
  author_email="ns@nsz.no",
  url="https://notabug.org/necklace/libray",
  packages=['libray'],
  scripts=['libray/libray'],
  install_requires=[
    'tqdm~=4.66.2',
    'pycryptodome~=3.20.0',
    'requests~=2.31.0',
    'beautifulsoup4~=4.12.3',
    'html5lib~=1.1',
    'setuptools~=69.1.1',
  ],
  include_package_data=True,
  package_data={'': ['data/keys.db']},
)
