# -*- coding: utf-8 -*-
"""test_templatereader.py

py Test:
Read the template file used to define how to print data.
This file contains certain regular-like expressions which are repeated
and replaced.


Created on Tue July 26 12:00:00 2022 @author: Dan Kotlyar
Last updated on Tue July 26 12:30:00 2022 @author: Dan Kotlyar


email: dan.kotlyar@me.gatech.edu

"""

import pytest

import os

from xsInterface.functions.readtemplate import ReadTemplate
from xsInterface.errors.customerrors import TemplateFileError
from xsInterface.functions.readinput import ReadInput


# -----------------------------------------------------------------------------
# universe data
# -----------------------------------------------------------------------------

univFile0 = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\inputsets\\u0"
UNIVERSES = ReadInput({}, u0=univFile0)

# -----------------------------------------------------------------------------
# default formats for outputting data
# -----------------------------------------------------------------------------
STATE_FRMT = "{:5.3f}"
VAR_FRMT = "{:d}"
ATTR_FRMT = "{:5.5e}"
ROW_VALS_N = 5  # maximum number of values printed in a line
FORMATS = {"state": "{:5.3f}", "var": "{:d}", "attr": "{:5.5e}", "nrow": 5}

# -----------------------------------------------------------------------------
# Invalid rules within a template file
# -----------------------------------------------------------------------------
BAD_REP1 = [
    'dummy sentence \n',
    '\"rep\"{2\n',
    '\"rep\"{{4\n',
    'sample\n',
    '\"rep\"} \n',
    '\"rep\"}} \n',] 

BAD_REP2 = [
    'dummy sentence \n',
    '\"rep\"{2\n',
    '\"rep\"{4\n',
    'sample\n',
    '\"rep\"} \n',
    '\"rep\"}} \n',] 

BAD_VARI = [
    'dummy sentence \n',
    '\"rep\"{2\n',
    '\"rep\"{{4\n',
    '\"vari\"{idxE+=1}\n',
    '\"rep\"}} \n',
    '\"rep\"} \n',] 


BAD_VARO = [
    'dummy sentence \n',
    '\"vari\"{idxE=1}',
    '\"rep\"{2\n',
    '\"rep\"{{4\n',
    '\"varo\"{idxE<d>}\n',
    '\"rep\"}} \n',
    '\"rep\"} \n',] 


# -----------------------------------------------------------------------------
# Path to all the input files
# -----------------------------------------------------------------------------
path2File = os.path.abspath(os.getcwd()) + "\\inputfiles\\"


def test_universes(tmp_path):
    """Errors with the repetition rule"""

    d = tmp_path / "temp"
    d.mkdir()
    p = d / "inp.txt"
    filepath = str(p)
    
    #filepath = 'to_delete'
    with open(filepath, 'w') as f:
        f.writelines(BAD_REP1)
        
    # the input writing is perforned using conftest
    with pytest.raises(TemplateFileError, match="!!!*"):
        ReadTemplate(filepath, UNIVERSES, FORMATS)

    with open(filepath, 'w') as f:
        f.writelines(BAD_REP2)
        
    # the input writing is perforned using conftest
    with pytest.raises(TemplateFileError, match="!!!*"):
        ReadTemplate(filepath, UNIVERSES, FORMATS)


def test_vari(tmp_path):
    """Errors when va input card"""

    d = tmp_path / "temp"
    d.mkdir()
    p = d / "inp.txt"
    filepath = str(p)
    
    #filepath = 'to_delete'
    with open(filepath, 'w') as f:
        f.writelines(BAD_VARI)
        
    # the input writing is perforned using conftest
    with pytest.raises(TemplateFileError, match="!!!*"):
        ReadTemplate(filepath, UNIVERSES, FORMATS)


def test_varo(tmp_path):
    """Errors when va input card"""

    d = tmp_path / "temp"
    d.mkdir()
    p = d / "inp.txt"
    filepath = str(p)
    
    #filepath = 'to_delete'
    with open(filepath, 'w') as f:
        f.writelines(BAD_VARO)
        
    # the input writing is perforned using conftest
    with pytest.raises(TemplateFileError, match="!!!"):
        ReadTemplate(filepath, UNIVERSES, FORMATS)