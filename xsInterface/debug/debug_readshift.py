# -*- coding: utf-8 -*-
"""debug_readserpent.py

Debug:
--------
Read the data using the ``serpentTools`` package.

Created on Sat July 30 05:00:00 2022 @author: Dan Kotlyar
Last updated on Wed Aug 04 16:00:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""


from xsInterface.functions.readshift import _ReadShiftFile

resFile =\
    "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\Reactor-Simulation-tools\\"+\
        "GitHub Repositories\\Public\\xs-interface\\xsInterface\\debug\\"+\
            "debugfiles\\bwrCellNodal.out.h5"

mgxs = _ReadShiftFile(resFile)

a = 1