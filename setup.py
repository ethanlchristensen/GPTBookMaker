from setuptools import setup, find_packages
import codecs
import os
import sys

here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()

VERSION = '0.0.1'
DESCRIPTION = 'GPT Book Creator'
LONG_DESCRIPTION = 'A package that allows for book creation given a target audience and short story description.'

# Setting up
setup(
    name="bruhbook",
    version=VERSION,
    author="Ethan Christensen",
    author_email="ethanlchristensen@outlook.com",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    url='https://github.com/ethanlchristensen/bruhbook',
    packages=find_packages(),
    install_requires=[
        "openai",
        "bruhcolor",
        "docx",
        "python-dotenv",
        "docx2pdf"
    ],
    extras_require={},
    setup_requires=['setuptools_scm'],
    keywords=['python', 'ai', 'gpt', 'generate'],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)