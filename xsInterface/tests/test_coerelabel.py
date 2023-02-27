# -*- coding: utf-8 -*-
"""test_relabelcoe.py

py Test:
The function allows to rename the branching labels set as individual
branches, e.g. ``f600b0dens630``, to a more structured manner,
which then allows the xsInterface package to work with the modified .coe files
as it recognizes the new labeling,
e.g. f600 dens630 b0


Created on Mon Feb 27 05:00:00 2023 @author: Dan Kotlyar
Last updated on Mon Feb 27 05:00:00 2023 @author: Dan Kotlyar

changed what?:
    - 
    - 
    - 

email: dan.kotlyar@me.gatech.edu

"""

import pytest

import os

from xsInterface.functions.relabelcoe import coeRelabel

# -----------------------------------------------------------------------------
# Settings card
# -----------------------------------------------------------------------------

GOOD_TEMPLATE = [     
    'f600b0dens630        f600 b0 dens630     ',      
    'f600b0densNom        f600 b0 nom         ',  
    'f600b0dens780        f600 b0 dens780     ',      
    'f600bNomdens630      f600 nom dens630    ',       
    'f600bNomdensNom      f600 nom nom        ',   
    'f600bNomdens780      f600 nom dens780    ',       
    'f600b2250dens630     f600 b2250 dens630  ',         
    'f600b2250densNom     f600 b2250 nom      ',     
    'f600b2250dens780     f600 b2250 dens780  ',        
    'fNomb0dens630        nom b0 dens630      ',     
    'fNomb0densNom        nom b0 nom          ', 
    'fNomb0dens780        nom b0 dens780      ',     
    'fNombNomdens630      nom nom dens630     ',      
    'nom                  nom nom nom         ',    
    'fNombNomdens780      nom nom dens780     ',      
    'fNomb2250dens630     nom b2250 dens630   ',        
    'fNomb2250densNom     nom b2250 nom       ',    
    'fNomb2250dens780     nom b2250 dens780   ',       
    'f1200b0dens630       f1200 b0 dens630    ',       
    'f1200b0densNom       f1200 b0 nom        ',   
    'f1200b0dens780       f1200 b0 dens780    ',       
    'f1200bNomdens630     f1200 nom dens630   ',        
    'f1200bNomdensNom     f1200 nom nom       ',    
    'f1200bNomdens780     f1200 nom dens780   ',        
    'f1200b2250dens630    f1200 b2250 dens630 ',         
    'f1200b2250densNom    f1200 b2250 nom     ',     
    'f1200b2250dens780    f1200 b2250 dens780 ',         
    'f1500b0dens630       f1500 b0 dens630    ',       
    'f1500b0densNom       f1500 b0 nom        ',   
    'f1500b0dens780       f1500 b0 dens780    ',       
    'f1500bNomdens630     f1500 nom dens630   ',        
    'f1500bNomdensNom     f1500 nom nom       ',    
    'f1500bNomdens780     f1500 nom dens780   ',        
    'f1500b2250dens630    f1500 b2250 dens630 ',         
    'f1500b2250densNom    f1500 b2250 nom     ',     
    'f1500b2250dens780    f1500 b2250 dens780 ', ]


BAD_NOT_COMPLETE_LIST = [     
    'f600b0dens630        f600 b0 dens630     ',      
    'f600b0densNom        f600 b0 nom         ',  
    'f600b0dens780        f600 b0 dens780     ',              
    'f1500b2250dens780    f1500 b2250 dens780 ', ]


BAD_BRANCH_NAME = [     
    'f600b0densBAD        f600 b0 dens630     ',      
    'f600b0densNom        f600 b0 nom         ',  
    'f600b0dens780        f600 b0 dens780     ',      
    'f600bNomdens630      f600 nom dens630    ',       
    'f600bNomdensNom      f600 nom nom        ',   
    'f600bNomdens780      f600 nom dens780    ',       
    'f600b2250dens630     f600 b2250 dens630  ',         
    'f600b2250densNom     f600 b2250 nom      ',     
    'f600b2250dens780     f600 b2250 dens780  ',        
    'fNomb0dens630        nom b0 dens630      ',     
    'fNomb0densNom        nom b0 nom          ', 
    'fNomb0dens780        nom b0 dens780      ',     
    'fNombNomdens630      nom nom dens630     ',      
    'nom                  nom nom nom         ',    
    'fNombNomdens780      nom nom dens780     ',      
    'fNomb2250dens630     nom b2250 dens630   ',        
    'fNomb2250densNom     nom b2250 nom       ',    
    'fNomb2250dens780     nom b2250 dens780   ',       
    'f1200b0dens630       f1200 b0 dens630    ',       
    'f1200b0densNom       f1200 b0 nom        ',   
    'f1200b0dens780       f1200 b0 dens780    ',       
    'f1200bNomdens630     f1200 nom dens630   ',        
    'f1200bNomdensNom     f1200 nom nom       ',    
    'f1200bNomdens780     f1200 nom dens780   ',        
    'f1200b2250dens630    f1200 b2250 dens630 ',         
    'f1200b2250densNom    f1200 b2250 nom     ',     
    'f1200b2250dens780    f1200 b2250 dens780 ',         
    'f1500b0dens630       f1500 b0 dens630    ',       
    'f1500b0densNom       f1500 b0 nom        ',   
    'f1500b0dens780       f1500 b0 dens780    ',       
    'f1500bNomdens630     f1500 nom dens630   ',        
    'f1500bNomdensNom     f1500 nom nom       ',    
    'f1500bNomdens780     f1500 nom dens780   ',        
    'f1500b2250dens630    f1500 b2250 dens630 ',         
    'f1500b2250densNom    f1500 b2250 nom     ',     
    'f1500b2250dens780    f1500 b2250 dens780 ', ]


# -----------------------------------------------------------------------------
# Path to all the input files
# -----------------------------------------------------------------------------
path2File = os.path.abspath(os.getcwd()) + "\\inputfiles\\"


def test_notCompleteBranchList(tmp_path):
    """Errors when reseting the settings"""

    list0 = BAD_NOT_COMPLETE_LIST

    d = tmp_path / "temp"
    d.mkdir()
    p = d / "inp.txt"
    filepath = str(p)
    
    
    with open(filepath, 'w') as f:
        for item in list0:
            f.write("%s\n" % item)

    
    # the input writing is perforned using conftest
    with pytest.raises(ValueError, match="!!!*"):
        coeRelabel(origCoeFile="../debug/debugfiles/combTest2.i.coe",
                   modCoeFile='dummy_file',
                   inpLabels=filepath)


def test_badBranchName(tmp_path):
    """Errors when reseting the settings"""

    list0 = BAD_NOT_COMPLETE_LIST

    d = tmp_path / "temp"
    d.mkdir()
    p = d / "inp.txt"
    filepath = str(p)
    
    
    with open(filepath, 'w') as f:
        for item in list0:
            f.write("%s\n" % item)

    
    # the input writing is perforned using conftest
    with pytest.raises(ValueError, match="!!!*"):
        coeRelabel(origCoeFile="../debug/debugfiles/combTest2.i.coe",
                   modCoeFile='dummy_file',
                   inpLabels=filepath)

