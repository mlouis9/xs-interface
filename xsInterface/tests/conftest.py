# -*- coding: utf-8 -*-
"""conftest

Created on Sun July 26 11:30:00 2020 @author: Dan Kotlyar
Last updated on Wed Aug 05 22:30:00 2020 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

"""


import pytest

@pytest.fixture()
def inputSettings(tmp_path):
    """create all the channels"""
    tlines = [                   
        'set settings NG 2 GR 7    ',  
        'macro =  abs, fiss, nsf   ',  
        'dim_macro = 1, 1, 1       ',  
        'micro =  abs, fiss, nsf   ',  
        'kinetics =  abs, fiss, nsf',  
        'meta =  abs, fiss, nsf    ',  
        'isotopes = 531350, 5141350', ]
    
    d = tmp_path / "temp"
    d.mkdir()
    p = d / "inp.txt"
    # p.write_text(inputSettings)

    with open(p, 'w') as f:
        for item in tlines:
            f.write("%s\n" % item)
    
    return str(p)