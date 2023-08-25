# -*- coding: utf-8 -*-
"""test_inputreader.py

py Test:
Serves as an user-friendly input interface.
Read the user-based input file.
All the input data are provided via the use of input cards.


Created on Tue May 10 05:00:00 2022 @author: Dan Kotlyar
Last updated on Tue May 24 17:00:00 2022 @author: Dan Kotlyar

changed what?:
    - reset and state testing 
    - branch/history/times (05/24 +DK)
    - data (05/24 +DK)

email: dan.kotlyar@me.gatech.edu

"""

import pytest

import os

from xsInterface.functions.readinput import ReadInput
from xsInterface.errors.customerrors import InputCardError, NonInputError,\
    InputGeneralError


# -----------------------------------------------------------------------------
# Settings card
# -----------------------------------------------------------------------------

BAD_SETTINGS = {       
"noset": [
    ' REDUNDANT LINE           ',
    'set settings NG 2 GR 7    ',  
    'macro =  abs, fiss, nsf   ',  
    'micro =  abs, fiss, nsf   ',  
    'kinetics =  abs, fiss, nsf',  
    'meta =  abs, fiss, nsf    ',  
    'isotopes = 531350, 5141350',
    'nuclides=nd'],
"DN": [
    'set settings NG 2 GR 7    ',  
    'macro =  abs, fiss, nsf   ',  
    'micro =  abs, fiss, nsf   ',  
    'kinetics =  abs, fiss, nsf',  
    'meta =  abs, fiss, nsf    ',  
    'isotopes = 531350, 5141350',
    'nuclides=nd'],
"NG": [
    'set settings NG 2 DN 7 BAD_CARD',  
    'macro =  abs, fiss, nsf   ',  
    'micro =  abs, fiss, nsf   ',  
    'kinetics =  abs, fiss, nsf',  
    'meta =  abs, fiss, nsf    ',  
    'isotopes = 531350, 5141350',
    'nuclides=nd'],
"dim": [
    'set settings NG 2 DN 7 BAD_CARD',  
    'macro =  abs, fiss, nsf   ',  
    'micro =  abs, fiss, nsf   ',  
    'kinetics =  abs, fiss, nsf',  
    'meta =  abs, fiss, nsf    ',  
    'isotopes = 531350, 5141350',
    'nuclides=nd'],
"card": [
    'set settings NG 2 DN 7 BAD_CARD',  
    'macro =  abs, fiss, nsf   ',  
    'micro =  abs, fiss, nsf   ',  
    'bad_card =  abs, fiss, nsf',  
    'meta =  abs, fiss, nsf    ',  
    'isotopes = 531350, 5141350',
    'nuclides=nd'],
"isotopes": [
    'set settings NG 2 DN 7 BAD_CARD',  
    'macro =  abs, fiss, nsf   ',  
    'micro =  abs, fiss, nsf   ',  
    'kinetics =  abs, fiss, nsf',  
    'meta =  abs, fiss, nsf    '], 
}


BAD_BRACNHES = {       
"negbranches": [
    'set branches -2',
    'fuel 600 900 1200 1500',
    'mod 500 600 700',  
    'cool 500 600', ],
"N": [
    'set branches 2',
    'fuel 600 900 1200 1500',
    'mod 500 600 700',  
    'cool 500 600', ], 
"nobranches": [
    'set branches 3',
    'fuel ',
    'mod 500 600 700',  
    'cool 500 600', ], }


BAD_HISTORY = {       
"negN": [
    'set histories -2',
    'nom 600 500 500',
    'pert 900 700 625'],
"N": [
    'set histories 6',
    'nom 600 500 500',
    'pert 900 700 625'],
"nohist": [
    'set histories 2',
    'nom',
    'pert 900 700 625'],
"neghist": [
    'set histories 2',
    'nom 600 500 -500',
    'pert 900 700 625'],
"badhist": [
    'set histories 2',
    'nom 600 500 7777',
    'pert 900 700 625'],}


BAD_TIMES = {       
"setLine": [
    'set times 2 2',
    '0 1 2 3 4 5 6 7 8'],
"noVals": [
    'set times MWd/kg',
    '0 1 2 3 4 5 6 7 8'], }

GOOD_TEMPLATE = [     
    'set settings 2 7          ',  
    'macro =  inf_abs, inf_flx ',
    'micro = sig_f             ',
    'isotopes = 541350 531350  ',
    'nuclides = nd',
    'set branches  3',
    'fuel 600 900 1200 1500',
    'mod 500 600 700',  
    'cool 500 600',
    'set histories 2',
    'nom 600 500 500',
    'pert 900 700 625',
    'set times nounits',
    '0 1 2 3']


BAD_DATA = {
    # "energy": [
    # 'set data inf_flx 10.0, 0.6025, 0.0',
    # 'block state',
    # 'branch 900.0, 600.0, 600.0',
    # 'history nom',
    # 'time 0.0',
    # 'block macro',
    # 'inf_abs 0.1, 0.2',
    # 'inf_flx 1E+9, 1E+10',
    # 'block micro',
    # 'sig_f',
    # '1 2',
    # '3 4'],
"energy": [
    'set data inf_flx 0.0, 0.6025, 0.0',
    'block state',
    'branch 900.0, 600.0, 600.0',
    'history nom',
    'time 0.0',
    'block macro',
    'inf_abs 0.1, 0.2',
    'inf_flx 1E+9, 1E+10',
    'block micro',
    'sig_f',
    '1 2',
    '3 4'],
"noblock": [
    'set data inf_flx 10.0, 0.6025, 0.0',
    'branch 900.0, 600.0, 600.0',
    'history nom',
    'time 0.0',
    'block macro',
    'inf_abs 0.1, 0.2',
    'inf_flx 1E+9, 1E+10',
    'block micro',
    'sig_f',
    '1 2',
    '3 4'],
"branch": [
    'set data inf_flx 10.0, 0.6025, 0.0',
    'block state',
    'branch 900.0, 600.0, 600.0, 500.0',
    'history nom',
    'time 0.0',
    'block macro',
    'inf_abs 0.1, 0.2',
    'inf_flx 1E+9, 1E+10',
    'block micro',
    'sig_f',
    '1 2',
    '3 4'],
"history": [
    'set data inf_flx 10.0, 0.6025, 0.0',
    'block state',
    'branch 900.0, 600.0, 600.0',
    'history BAD_HIST',
    'time 0.0',
    'block macro',
    'inf_abs 0.1, 0.2',
    'inf_flx 1E+9, 1E+10',
    'block micro',
    'sig_f',
    '1 2',
    '3 4'],
"time": [
    'set data inf_flx 10.0, 0.6025, 0.0',
    'block state',
    'branch 900.0, 600.0, 600.0',
    'history nom',
    'time -10.0',
    'block macro',
    'inf_abs 0.1, 0.2',
    'inf_flx 1E+9, 1E+10',
    'block micro',
    'sig_f',
    '1 2',
    '3 4'],
"macro": [
    'set data inf_flx 10.0, 0.6025, 0.0',
    'block state',
    'branch 900.0, 600.0, 600.0',
    'history nom',
    'time 0.0',
    'block macro',
    'inf_abs 0.1, 0.2',
    'block micro',
    'sig_f',
    '1 2',
    '3 4'],
"macroE": [
    'set data inf_flx 0.0, 0.6025, 0.0',
    'block state',
    'branch 900.0, 600.0, 600.0',
    'history nom',
    'time 0.0',
    'block macro',
    'inf_abs 0.1, 0.2, 0.0, 0.0, 0.0',
    'inf_flx 1E+9, 1E+10',
    'block micro',
    'sig_f',
    '1 2',
    '3 4'],
"micro": [
    'set data inf_flx 0.0, 0.6025, 0.0',
    'block state',
    'branch 900.0, 600.0, 600.0',
    'history nom',
    'time 0.0',
    'block macro',
    'inf_abs 0.1, 0.2',
    'inf_flx 1E+9, 1E+10',
    'block micro',
    'sig_f',
    '1 2',
    '3 4 5'],}

# -----------------------------------------------------------------------------
# Path to all the input files
# -----------------------------------------------------------------------------
path2File = os.path.abspath(os.getcwd()) + str(pathlib.Path("/inputfiles/"))


def test_setData(tmp_path):
    """Errors when reseting the settings"""

    list0 = GOOD_TEMPLATE
    dict0 = BAD_DATA

    d = tmp_path / "temp"
    d.mkdir()
    p = d / "inp.txt"
    filepath = str(p)
    
    # multiple bad settings
    for keyTest in dict0: 
    
        with open(filepath, 'w') as f:
            for item in list0:
                f.write("%s\n" % item)
            for item in dict0[keyTest]:
                f.write("%s\n" % item)
        
        # the input writing is perforned using conftest
        with pytest.raises((InputCardError, NonInputError, InputGeneralError),
                           match="!!!*"):
            ReadInput({}, u0=filepath)


@pytest.mark.parametrize("dict0", [BAD_SETTINGS, BAD_BRACNHES, BAD_HISTORY,
                                   BAD_TIMES])
def test_setcard(tmp_path, dict0):
    """Errors when reseting the settings"""

    # dict0 = BAD_TIMES

    d = tmp_path / "temp"
    d.mkdir()
    p = d / "inp.txt"
    filepath = str(p)
    
    # multiple bad settings
    for keyTest in dict0: 
    
        with open(filepath, 'w') as f:
            for item in dict0[keyTest]:
                f.write("%s\n" % item)
        
        # the input writing is perforned using conftest
        with pytest.raises((InputCardError, NonInputError, InputGeneralError),
                           match="!!!*"):
            ReadInput({}, u0=filepath)

