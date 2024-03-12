from setuptools import setup, find_packages
import codecs
import os
import re
import pandas
import string
import warnings
import spacy
VERSION = '0.0.15'
DESCRIPTION = 'NLP Library to find Retail terms'
LONG_DESCRIPTION = 'This library helps to find Retail Terms that are there in unstructured text. Developers can build on top of it.'

setup(
    name="retailterms",
    version=VERSION,
    author="Marcel Tino",
    author_email="<marceltino92@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    install_requires=[],
    keywords=['retail','retailterms'])
