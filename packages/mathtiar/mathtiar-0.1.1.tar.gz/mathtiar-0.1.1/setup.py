from setuptools import setup, find_packages
import codecs
import os

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.1.1'
DESCRIPTION = 'Simple Math'
LONG_DESCRIPTION = 'A simple Python package for math operations and geometry calculations'

# Setting up
setup(
    name="mathtiar",
    version=VERSION,
    author="Ikhtiar Oktafio Wibowo",
    author_email="tiarokta@gmail.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    keywords=['python', 'math', 'simple'],
    license="MIT",
    url="https://github.com/szzin20/simple-math.git",
    project_urls={
        'Source': 'https://github.com/szzin20/simple-math.git',
    },
)