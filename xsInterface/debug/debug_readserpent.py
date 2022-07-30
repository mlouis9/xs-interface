# -*- coding: utf-8 -*-
"""debug_readserpent.py

Debug:
--------
Read the data using the ``serpentTools`` package.

Created on Sat July 30 05:00:00 2022 @author: Dan Kotlyar
Last updated on Sat July 30 05:00:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.readserpent import ReadCoefFile, ReadHistoryFiles

coeFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\debug\\debugfiles\\u0.coe"

# read the .coe file
# -----------------------------------------------------------------------------
# data = ReadCoefFile(coeFile)


fnames = {'fuel_': {'nom': coeFile, 'pert': coeFile},
          'ref': {'nom': coeFile},
              }

data = ReadHistoryFiles(fnames)


a = 1