# -*- coding: utf-8 -*-
"""
Created on Tue Mar 12 11:27:18 2024

@author: FredEvif
"""

import setuptools

with open("README.md","r",encoding="utf-8") as fh:
    long_description=fh.read()
    
setuptools.setup(
    name='example',
    version='1.0',
    description='this is a program for dia',
    author='',
    author_email='',
    packages=setuptools.find_packages(),
   )