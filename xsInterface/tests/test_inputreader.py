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
# Settings card
# -----------------------------------------------------------------------------

BAD_SETTINGS = {
#"template": [
#    'set settings NG 2 DN 7 BAD_CARD',  
#    'macro =  abs, fiss, nsf   ',  
#    'dim_macro = 1, 1, 1       ',  
#    'micro =  abs, fiss, nsf   ',  
#    'kinetics =  abs, fiss, nsf',  
#    'meta =  abs, fiss, nsf    ',  
#    'isotopes = 531350, 5141350'],          
"noset": [
    ' REDUNDANT LINE           ',
    'set settings NG 2 GR 7    ',  
    'macro =  abs, fiss, nsf   ',  
    'dim_macro = 1, 1, 1       ',  
    'micro =  abs, fiss, nsf   ',  
    'kinetics =  abs, fiss, nsf',  
    'meta =  abs, fiss, nsf    ',  
    'isotopes = 531350, 5141350'],
"DN": [
    'set settings NG 2 GR 7    ',  
    'macro =  abs, fiss, nsf   ',  
    'dim_macro = 1, 1, 1       ',  
    'micro =  abs, fiss, nsf   ',  
    'kinetics =  abs, fiss, nsf',  
    'meta =  abs, fiss, nsf    ',  
    'isotopes = 531350, 5141350'],
"NG": [
    'set settings NG 2 DN 7 BAD_CARD',  
    'macro =  abs, fiss, nsf   ',  
    'dim_macro = 1, 1, 1       ',  
    'micro =  abs, fiss, nsf   ',  
    'kinetics =  abs, fiss, nsf',  
    'meta =  abs, fiss, nsf    ',  
    'isotopes = 531350, 5141350'],
"dim": [
    'set settings NG 2 DN 7 BAD_CARD',  
    'macro =  abs, fiss, nsf   ',  
    'dim_macro = 1, 1, 1, 1    ',  
    'micro =  abs, fiss, nsf   ',  
    'kinetics =  abs, fiss, nsf',  
    'meta =  abs, fiss, nsf    ',  
    'isotopes = 531350, 5141350'],
"card": [
    'set settings NG 2 DN 7 BAD_CARD',  
    'macro =  abs, fiss, nsf   ',  
    'dim_macro = 1, 1, 1, 1    ',  
    'micro =  abs, fiss, nsf   ',  
    'bad_card =  abs, fiss, nsf',  
    'meta =  abs, fiss, nsf    ',  
    'isotopes = 531350, 5141350'],
"isotopes": [
    'set settings NG 2 DN 7 BAD_CARD',  
    'macro =  abs, fiss, nsf   ',  
    'dim_macro = 1, 1, 1,      ',  
    'micro =  abs, fiss, nsf   ',  
    'kinetics =  abs, fiss, nsf',  
    'meta =  abs, fiss, nsf    '], 
}

# -----------------------------------------------------------------------------
# Path to all the input files
# -----------------------------------------------------------------------------
path2File = os.path.abspath(os.getcwd()) + "\\inputfiles\\"

def test_bad_settings(tmp_path):
    """Errors when reseting the settings"""
    
    
    d = tmp_path / "temp"
    d.mkdir()
    p = d / "inp.txt"
    filepath = str(p)
    
    
    # multiple bad settings
    for keyTest in BAD_SETTINGS: 
    
        with open(filepath, 'w') as f:
            for item in BAD_SETTINGS["DN"]:
                f.write("%s\n" % item)
        
        # the input writing is perforned using conftest
        with pytest.raises(InputCardError, match="!!!*"):
            ReadInput(filepath)


    

