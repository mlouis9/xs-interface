# -*- coding: utf-8 -*-
"""debug_readlst.py

Debug:
--------
Read DYN3D _lst file
Read the nodal fluxes and k-eff from the _lst file created by DYN3D.


Created on Wed May 24 10:30:00 2023 @author: Dan Kotlyar
Last updated on Wed May 24 12:00:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.thirdpartycodes import exeDyn3D

             
casedir = ".\\debugfiles\\\dyn3d_test\\rho1_1gr"   # dyn3d dir
casefile = "bwr"  # name of dyn3d file
exefile = "RUN_DYN3D" # dyn3d executuin file




# execute DYN3D and get fluxes and k-eff
# -----------------------------------------------------------------------------
keff, fluxes, normFlx = exeDyn3D(casedir, casefile, exefile)

