# -*- coding: utf-8 -*-
"""debug_readserpent.py

Debug:
--------
Read the data using the ``serpentTools`` package.

Created on Sat July 30 05:00:00 2022 @author: Dan Kotlyar
Last updated on Wed Aug 04 16:00:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""
import numpy as np

from xsInterface.functions.readserpent import ReadSerpent

coeFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\debug\\debugfiles\\u0.coe"

# read the .coe file
# -----------------------------------------------------------------------------
# data = ReadCoefFile(coeFile)


fnames = {'fuel_': {'nom': coeFile, 'pert': coeFile},
          'ref': {'nom': coeFile}, }

origLables = {'fuel': ['f600', 'f1200', 'nom', 'f1500'],
              'boron': ['nom', 'b2250', 'b0'],
              'dens': ['dens630', 'nom', 'dens780']}
modLables = {'fuel': np.array([600, 1200.0, 900.0, 1500.0]),
              'boron': [500.0, 2250.0, 0.0],
              'dens': [630.0, 700.0, 780.0]}


dataOut, timepoints =\
    ReadSerpent(fnames, origLables, modLables,
                attrs=['infKappa', 'infSp0', 'cmmTranspxs', 'lambda'],
                times=None,
                burnups=[0.0])
    
sp0 = dataOut['fuel_0']['nom'][0.0][(1500.0, 2250.0, 780.0)]['infSp0']

