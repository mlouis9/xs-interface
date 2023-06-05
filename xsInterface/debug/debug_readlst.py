# -*- coding: utf-8 -*-
"""debug_readlst.py

Debug:
--------
Read DYN3D _lst file
Read the nodal fluxes and k-eff from the _lst file created by DYN3D.


Created on Wed May 24 10:30:00 2023 @author: Dan Kotlyar
Last updated on Wed May 24 12:00:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

Last Checked:
---------------
06/05/2023 - DK

"""

from xsInterface.functions.dyn3d import lstRead


lstFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\debug\\debugfiles\\core_lst.dat"




# read fluxes and k-eff
# -----------------------------------------------------------------------------
keff, fluxes = lstRead(lstFile)

