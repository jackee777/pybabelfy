# pybabelfy
A python interface for Babelfy http://babelfy.org/

Babelfy is a multilingual, graph-based approach to Entity Linking and Word Sense Disambiguation.

# Installation
This is for python3, however, is the almost same as original https://github.com/aghie/pybabelfy.

Please download the project, use ```cd``` to move to the pybabelfy folder and run:
```
sudo python setup.py install
```

# Causion
Of course, you can use original code by changing setup.py in to following codes.
It works in ubuntu. Unfortunately, I don't know you can use in windows.
```
from distutils.core import setup

try:
    from distutils.command.build_py import build_py_2to3 as build_py
except ImportError:
    from distutils.command.build_py import build_py

setup(
  name = 'pybabelfy',
  ppackages = ['pybabelfy', 'build/lib/pybabelfy'], # this must be the same as the name above
  version = '0.1',
  description = 'A Python interface for Babelfy',
  author = 'David Vilares',
  author_email = 'david.vilares89@gmail.com',
  url = 'https://github.com/aghie/pybabelfy', # use the URL to the github repo
  download_url = 'https://github.com/aghie/pybabelfy/tarball/0.1', # I'll explain this in a second
  keywords = ['babelfy', 'wrapper', 'api'], # arbitrary keywords
  cmdclass = {'build_py':build_py},
  classifiers = [],
)

```

# Getting started
To use pybabelfy you must register at http://babelfy.org/ and obtain your RESTful key
This code also exists in the pybabelfy/examples directory.

```
from pybabelfy.babelfy import *

text= "BabelNet is both a multilingual encyclopedic dictionary and a semantic network"
lang = "EN"
key = "KEY" #This only works for the demo example. Change it for your RESTful key (you must register at babelfy.org for it)

babelapi = Babelfy()

semantic_annotations = babelapi.disambiguate(text,lang,key)

for semantic_annotation in semantic_annotations:
    print(semantic_annotation.frag(text))
    semantic_annotation.pprint()

```
