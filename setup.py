from os.path import join
from glob import glob

import setuptools


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="xsInterface",
    version="0.2.1",
    author="Dan Kotlyar",
    author_email="dan.kotlyar@me.gatech.edu",
    description="Cross Section Interface for multi-group XS manipulation ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/CORE-GATECH-GROUP/xs-interfaces",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    packages=['xsInterface',
              'xsInterface.containers', 'xsInterface.debug',
              'xsInterface.errors', 'xsInterface.examples',
              'xsInterface.functions', 'xsInterface.inputsets',
              'xsInterface.inputsets', 'xsInterface.otemplates',
              'xsInterface.tests', 'xsInterface.workshops' ],
)
