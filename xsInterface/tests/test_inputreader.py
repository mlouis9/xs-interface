# -*- coding: utf-8 -*-
"""test_inputreader.py

py Test:
Serves as an user-friendly input interface.
Read the user-based input file.
All the input data are provided via the use of input cards.


Created on Tue May 10 05:00:00 2022 @author: Dan Kotlyar
Last updated on Tue May 10 05:00:00 2022 @author: Dan Kotlyar

changed what?:
    - reset and state testing 

email: dan.kotlyar@me.gatech.edu

"""

import pytest

import os

from xsInterface.functions.readinput import ReadInput
from xsInterface.errors.customerrors import InputCardError

# -----------------------------------------------------------------------------
# Path to all the input files
# -----------------------------------------------------------------------------
path2File = os.path.abspath(os.getcwd()) + "\\inputfiles\\"

def test_bad_settings():
    """Errors when reseting the settings"""

    inp = path2File  + "inp_example1"

    with pytest.raises(InputCardError, match="Expected inputs*"):
        ReadInput(inp)



