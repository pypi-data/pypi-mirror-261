from setuptools import setup, find_packages
import codecs
import os
import re
import pandas
import string
import warnings
import spacy
from pkg_resources import resource_filename
filepath = resource_filename('retailterms', 'rt.xlsx')
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()
VERSION = '0.0.21'
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
    package_data={'':[filepath]},
    include_package_data=True,
    install_requires=['pandas','spacy'],
    keywords=['retail','retailterms'])
