from setuptools import setup, find_packages
VERSION = '0.0.3'
DESCRIPTION = 'NLP Library to find Retail terms'
LONG_DESCRIPTION = 'This library helps to find Retail Terms that are there in unstructured text. Developers can build on top of it.'

# Setting up
setup(
    name="retailterms",
    version=VERSION,
    author="Marcel Tino",
    author_email="<marceltino92@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=['os','csv','re','pandas','string','warning','spacy'],
    keywords=['retail','retailterms'],

)
