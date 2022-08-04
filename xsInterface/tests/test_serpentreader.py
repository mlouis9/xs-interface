# -*- coding: utf-8 -*-
"""test_serpentreader.py

py Test:
Read the data in multiple .coe branch files using the ``serpentTools`` package.
This method allows to read multiple history files with multiple universes.
It also allows to filter the data/attributes of interest.

Created on Wed Aug 04 16:00:00 2022 @author: Dan Kotlyar
Last updated on Wed Aug 04 16:30:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

"""

import pytest

from xsInterface.errors.customerrors import SerpentFileError
from xsInterface.functions.readserpent import ReadSerpent

coeFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\tests\\testfiles\\u0.coe"


def test_fnames():
    """Errors when defining the file names"""

    
    origLables = {'fuel': ['f600', 'f1200', 'nom', 'f1500'],
                  'boron': ['nom', 'b2250', 'b0'],
                  'dens': ['dens630', 'nom', 'dens780']}
    modLables = {'fuel': [600, 1200.0, 900.0, 1500.0],
                  'boron': [500.0, 2250.0, 0.0],
                  'dens': [630.0, 700.0, 780.0]}
        
    with pytest.raises(SerpentFileError, match="!!!*"):
        ReadSerpent('BAD_TYPE', origLables, modLables,
                    attrs=['infKappa', 'infSp0', 'cmmTranspxs', 'lambda'],
                    times=None,
                    burnups=[0.0])

    with pytest.raises(SerpentFileError, match="!!!*"):
        ReadSerpent({'univ': 'BAD_TYPE'}, origLables, modLables,
                    attrs=['infKappa', 'infSp0', 'cmmTranspxs', 'lambda'],
                    times=None,
                    burnups=[0.0])

def test_relabel():
    """Errors when using string and numeric labels"""

 
    fnames = {'fuel_': {'nom': coeFile, 'pert': coeFile},
              'ref': {'nom': coeFile}, }   
    origLables = {'fuel': ['f600', 'f1200', 'nom', 'f1500'],
                  'boron': ['nom', 'b2250', 'b0'],
                  'dens': ['dens630', 'nom', 'dens780']}
    modLables = {'fuel': [600, 1200.0, 900.0, 1500.0],
                  'boron': [500.0, 2250.0, 0.0],
                  'dens': [630.0, 700.0, 780.0]}
   
    # not the same states     
    with pytest.raises(SerpentFileError, match="!!!*"):
        origLables = {'fuel': ['f600', 'f1200', 'nom', 'f1500'],
                      'boron': ['nom', 'b2250', 'b0'],
                      'dens': ['dens630', 'nom', 'dens780']}
        modLables = {'fuel': [600, 1200.0, 900.0, 1500.0],
                      'dens': [630.0, 700.0, 780.0]}
        ReadSerpent(fnames, origLables, modLables,
                    attrs=['infKappa', 'infSp0', 'cmmTranspxs', 'lambda'],
                    times=None,
                    burnups=[0.0])

    # missing branch points  
    with pytest.raises(SerpentFileError, match="!!!*"):
        origLables = {'fuel': ['f600', 'f1200', 'nom', 'f1500'],
                      'boron': ['nom', 'b2250', 'b0'],
                      'dens': ['dens630', 'nom', 'dens780']}
        modLables = {'fuel': [600, 1200.0, 900.0, 1500.0],
                      'boron': [500.0, 0.0],
                      'dens': [630.0, 700.0, 780.0]}
        ReadSerpent(fnames, origLables, modLables,
                    attrs=['infKappa', 'infSp0', 'cmmTranspxs', 'lambda'],
                    times=None,
                    burnups=[0.0])


    # not numeric values 
    with pytest.raises(SerpentFileError, match="!!!*"):
        origLables = {'fuel': ['f600', 'f1200', 'nom', 'f1500'],
                      'boron': ['nom', 'b2250', 'b0'],
                      'dens': ['dens630', 'nom', 'dens780']}
        modLables = {'fuel': ['str', 1200.0, 900.0, 1500.0],
                      'boron': [500.0, 2250.0, 0.0],
                      'dens': [630.0, 700.0, 780.0]}
        ReadSerpent(fnames, origLables, modLables,
                    attrs=['infKappa', 'infSp0', 'cmmTranspxs', 'lambda'],
                    times=None,
                    burnups=[0.0])


    # branches not read by Serpent
    with pytest.raises(SerpentFileError, match="!!!*"):
        origLables = {'fuel': ['BAD_BRANCH', 'f1200', 'nom', 'f1500'],
                      'boron': ['nom', 'b2250', 'b0'],
                      'dens': ['dens630', 'nom', 'dens780']}
        modLables = {'fuel': [600, 1200.0, 900.0, 1500.0],
                      'boron': [500.0, 2250.0, 0.0],
                      'dens': [630.0, 700.0, 780.0]}
        ReadSerpent(fnames, origLables, modLables,
                    attrs=['infKappa', 'infSp0', 'cmmTranspxs', 'lambda'],
                    times=None,
                    burnups=[0.0])


def test_attrsfilter():
    """Errors when attempting to filter data"""

 
    fnames = {'fuel_': {'nom': coeFile, 'pert': coeFile},
              'ref': {'nom': coeFile}, }   
    origLables = {'fuel': ['f600', 'f1200', 'nom', 'f1500'],
                  'boron': ['nom', 'b2250', 'b0'],
                  'dens': ['dens630', 'nom', 'dens780']}
    modLables = {'fuel': [600, 1200.0, 900.0, 1500.0],
                  'boron': [500.0, 2250.0, 0.0],
                  'dens': [630.0, 700.0, 780.0]}
   
    # wrong type for attributes    
    with pytest.raises(SerpentFileError, match="!!!*"):
        ReadSerpent(fnames, origLables, modLables,
                    attrs='BAD_TYPE',
                    times=None,
                    burnups=[0.0])

    # attributes do not exist
    with pytest.raises(SerpentFileError, match="!!!*"):
        ReadSerpent(fnames, origLables, modLables,
                    attrs=['BAD_TYPE'],
                    times=None,
                    burnups=[0.0])

    # Both times and burnups defined
    with pytest.raises(SerpentFileError, match="!!!*"):
        ReadSerpent(fnames, origLables, modLables,
                    attrs=['infSp0'],
                    times=[0.0],
                    burnups=[0.0])
        
    # Bad times type
    with pytest.raises(SerpentFileError, match="!!!*"):
        ReadSerpent(fnames, origLables, modLables,
                    attrs=['infSp0'],
                    times='BAD_TYPE',
                    burnups=None)
        
    # Bad burnups type
    with pytest.raises(SerpentFileError, match="!!!*"):
        ReadSerpent(fnames, origLables, modLables,
                    attrs=['infSp0'],
                    times=None,
                    burnups='BAD_TYPE')

    # Non existing burnup points
    with pytest.raises(SerpentFileError, match="!!!*"):
        ReadSerpent(fnames, origLables, modLables,
                    attrs=['infSp0'],
                    times=None,
                    burnups=[0.05])        

    # Non existing time points
    with pytest.raises(SerpentFileError, match="!!!*"):
        ReadSerpent(fnames, origLables, modLables,
                    attrs=['infSp0'],
                    times=[0.0, 1.0],
                    burnups=None)            
        