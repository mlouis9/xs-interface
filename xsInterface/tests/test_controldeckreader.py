# -*- coding: utf-8 -*-
"""test_controldeckreader.py

py Test:
This is a control dictionary interface that describes what files and templates
should be read. It also specifies the format that wil be used to output
the required information.


Created on Tue July 26 09:00:00 2022 @author: Dan Kotlyar
Last updated on Tue July 26 12:00:00 2022 @author: Dan Kotlyar


email: dan.kotlyar@me.gatech.edu

"""

import pytest

import os

from xsInterface.functions.readcontroldict import Read
from xsInterface.errors.customerrors import ControlFileError


# -----------------------------------------------------------------------------
# Properly defined & invalid card within the control deck
# -----------------------------------------------------------------------------

GOOD_UNIVERSES = [
    'set universes\n',
    'u0 ./inp1/u0 \n',
    'u1 ./inp1/u1 \n',] 

GOOD_TEMPLATES = [
    'set templates        \n',
    'tmpl0 tmpl/template0\n',
    'tmpl1 tmpl/template1\n',] 

GOOD_OUTPUTS = [
    'set outputs  \n',
    'tmpl0 output_\n',
    'tmpl1 output_\n',] 


GOOD_LINKS = [
    'set links\n',
    'tmpl0 u0 \n',
    'tmpl1 u1 \n',]

GOOD_SERP = [
    'set universes\n',
    'fuel ./inp1/u0 \n',
    'ref ./inp1/u1 \n',
    'set links\n',
    'tmpl0 fuel0 \n',
    'tmpl1 ref1 \n',
    'set serpent\n',
    'fuel 0 \n',
    'ref 1 \n',
    ]

GOOD_FORMATS = [
    'set formats 8 .dat\n',
    'state 5.5f        \n',
    'attr 6.6e         \n',
    'var 5d            \n',]


BAD_UNIVERSES = [
    'set universes\n',
    'u0\n',
    'u1 ./inp1/u1 \n',] 

BAD_TEMPLATES = [
    'set templates        \n',
    'tmpl0\n',
    'tmpl1 tmpl/template1\n',] 

BAD_OUTPUTS = [
    'set outputs  \n',
    'tmpl3 output_\n'
    'tmpl1 output_\n',] 


BAD_LINKS = [
    'set links\n',
    'tmpl0\n',
    'tmpl1 u1 \n',]


BAD_FORMATS1 = [
    'set formats 8 .dat\n',
    'bad_attr 5.5f        \n',
    'attr 6.6e         \n',
    'var 5d            \n',]

BAD_FORMATS2 = [
    'set formats 8 .dat\n',
    'state 5.5rrr        \n',
    'attr 6.6e         \n',
    'var 5d            \n',]

BAD_SERP = [
    'set universes\n',
    'fuel ./inp1/u0 \n',
    'ref ./inp1/u1 \n',
    'set links\n',
    'tmpl0 fuel0 \n',
    'tmpl1 ref1 \n',
    'set serpent\n',
    'fuel 0 \n',
    'ref 0 \n',
    ]



# -----------------------------------------------------------------------------
# Path to all the input files
# -----------------------------------------------------------------------------
path2File = os.path.abspath(os.getcwd()) + str(pathlib.Path("/inputfiles/"))


def test_universes(tmp_path):
    """Errors when reseting the settings"""

    d = tmp_path / "temp"
    d.mkdir()
    p = d / "inp.txt"
    filepath = str(p)
    

    with open(filepath, 'w') as f:
        #f.writelines(GOOD_UNIVERSES)
        f.writelines(BAD_UNIVERSES)
        
        f.writelines(GOOD_TEMPLATES)
        f.writelines(GOOD_OUTPUTS)
        f.writelines(GOOD_LINKS)
        f.writelines(GOOD_FORMATS)

    # the input writing is perforned using conftest
    with pytest.raises(ControlFileError, match="!!!*"):
        Read(filepath)


def test_templates(tmp_path):
    """Errors when reseting the settings"""

    d = tmp_path / "temp"
    d.mkdir()
    p = d / "inp.txt"
    filepath = str(p)
    

    with open(filepath, 'w') as f:
        f.writelines(GOOD_UNIVERSES)
        # f.writelines(GOOD_TEMPLATES)
        f.writelines(BAD_TEMPLATES)
        
        f.writelines(GOOD_OUTPUTS)
        f.writelines(GOOD_LINKS)
        f.writelines(GOOD_FORMATS)

    # the input writing is perforned using conftest
    with pytest.raises(ControlFileError, match="!!!*"):
        Read(filepath)


def test_outputs(tmp_path):
    """Errors when reseting the settings"""

    d = tmp_path / "temp"
    d.mkdir()
    p = d / "inp.txt"
    filepath = str(p)
    

    with open(filepath, 'w') as f:
        f.writelines(GOOD_UNIVERSES)
        f.writelines(GOOD_TEMPLATES)
        # f.writelines(GOOD_OUTPUTS)
        f.writelines(BAD_OUTPUTS)
        f.writelines(GOOD_LINKS)
        f.writelines(GOOD_FORMATS)

    # the input writing is perforned using conftest
    with pytest.raises(ControlFileError, match="!!!*"):
        Read(filepath)


def test_links(tmp_path):
    """Errors when reseting the settings"""

    d = tmp_path / "temp"
    d.mkdir()
    p = d / "inp.txt"
    filepath = str(p)
    

    with open(filepath, 'w') as f:
        f.writelines(GOOD_UNIVERSES)
        f.writelines(GOOD_TEMPLATES)
        f.writelines(GOOD_OUTPUTS)
        #f.writelines(GOOD_LINKS)
        f.writelines(BAD_LINKS) 
        f.writelines(GOOD_FORMATS)

    # the input writing is perforned using conftest
    with pytest.raises(ControlFileError, match="!!!*"):
        Read(filepath)


def test_serpent(tmp_path):
    """Errors when reseting the settings"""

    d = tmp_path / "temp"
    d.mkdir()
    p = d / "inp.txt"
    filepath = str(p)
    

    with open(filepath, 'w') as f:
        f.writelines(BAD_SERP)
        f.writelines(GOOD_TEMPLATES)
        f.writelines(GOOD_OUTPUTS)


    # the input writing is perforned using conftest
    with pytest.raises(ControlFileError, match="!!!*"):
        Read(filepath)


def test_formats(tmp_path):
    """Errors when reseting the settings"""

    d = tmp_path / "temp"
    d.mkdir()
    p = d / "inp.txt"
    filepath = str(p)
    

    with open(filepath, 'w') as f:
        f.writelines(GOOD_UNIVERSES)
        f.writelines(GOOD_TEMPLATES)
        f.writelines(GOOD_OUTPUTS)
        f.writelines(GOOD_LINKS)
        f.writelines(BAD_FORMATS1)

    # the input writing is perforned using conftest
    with pytest.raises(ControlFileError, match="!!!*"):
        Read(filepath)
        
    with open(filepath, 'w') as f:
        f.writelines(GOOD_UNIVERSES)
        f.writelines(GOOD_TEMPLATES)
        f.writelines(GOOD_OUTPUTS)
        f.writelines(GOOD_LINKS)
        f.writelines(BAD_FORMATS2)

    # the input writing is perforned using conftest
    with pytest.raises(ControlFileError, match="!!!*"):
        Read(filepath)