# -*- coding: utf-8 -*-
"""debug_mapping.py

Debug:
--------
mapping capability to input the distributions of channels and layers.

Created on Mon May 01 13:00:00 2023 @author: Dan Kotlyar
Last updated on Mon May 02 15:00:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

import numpy as np
import matplotlib.pyplot as plt

from xsInterface.functions.main import Main
from xsInterface.functions.dyn3d import DYN3D
from xsInterface.functions.plotters import Plot1d

inputFile = ".\\inputs\\controlDict"
        


# -----------------------------------------------------------------------------
#                 READ CROSS SECTIONS
# -----------------------------------------------------------------------------

# Read the control dict
xs = Main(inputFile)

# Read xs data and templates and populate data
xs.Read(readUniverses=True)

# Condense cross section to a single group
# xscond = xs.Condense([10.0E+06, 0.0])

# -----------------------------------------------------------------------------
#                 ESTIMATE CROSS SECTIONS FOR THE CORE
# -----------------------------------------------------------------------------

nchs = 1
nlayers = 38
states = {
'history':[['nom']*nlayers]*nchs,
'time': [[0.0]*nlayers]*nchs,
'dens': [[700.]*nlayers]*nchs,
}

#adfvals = [[[1.0, 1.0]]*nlayers]*nchs
#refFlx = [[[1.0, 1.0]]*nlayers]*nchs


volmanip = {'infflx': 'divide'}

xs.PopulateCoreData(
                    states=states, 
                    attributes=None,  # specify only if specific attrs needed
                    volManip=volmanip,
                    adf=None, bottomadf=None, topadf=None, sph=None,)


refFlx, chIds = xs.CoreValues('infflx', volManip=['divide'])
refFlx = refFlx['infflx']

# -----------------------------------------------------------------------------
#                 EXECUTE DYN3D
# -----------------------------------------------------------------------------



casedir = ".\\dyn3d"   # dyn3d dir
casefile = "bwr"  # name of dyn3d file
exefile = "RUN_DYN3D" # dyn3d executuin file

# Reset correction factors
reslt = DYN3D(xs, casedir, casefile, exefile)

reslt.Iterate(
    corrattrs=['topadf'], refFlx=refFlx, newtonIters=5, krylovSpan=7, 
    dampingF=1.0)


# -----------------------------------------------------------------------------
#                 PLOT RESULTS
# -----------------------------------------------------------------------------

layers = np.linspace(0, 365.76, 37)  #active core
layers = np.hstack((-20.0, layers, 385.76))  # with reflectors
zmid = 0.5*(layers[0:-1] + layers[1:])

# Absolute fluxes
flx_g1 = {'Serpent': reslt.refFlxNorm[0::2],
          'DYN3D wo/corr': reslt.fluxes[0, 0::2],
          'DYN3D w/corr': reslt.fluxes[-1, 0::2],}

flx_g2 = {'Serpent': reslt.refFlxNorm[1::2],
          'DYN3D wo/corr': reslt.fluxes[0, 1::2],
          'DYN3D w/corr': reslt.fluxes[-1, 1::2],}


plt.figure()
Plot1d(xvalues=zmid, yvalues=flx_g1,
       markers=['--', '*', 'o'],
       xlabel="Height, cm", ylabel="Normalized flux [fast group]")

plt.figure()
Plot1d(xvalues=zmid, yvalues=flx_g2, 
       markers=['--', '*', 'o'],
       xlabel="Height, cm", ylabel="Normalized flux [Thermal group]")


# difference in flux
diff_flx_nocorr =\
    100*(1-(reslt.refFlxNorm[1::2]+reslt.refFlxNorm[0::2])/\
        (reslt.fluxes[0, 1::2]+reslt.fluxes[0, 0::2]))
diff_flx_wcorr =\
    100*(1-(reslt.refFlxNorm[1::2]+reslt.refFlxNorm[0::2])/\
        (reslt.fluxes[-1, 1::2]+reslt.fluxes[-1, 0::2])) 

diff_flx = {
          'DYN3D wo/corr': diff_flx_nocorr,
          'DYN3D w/corr': diff_flx_wcorr,}


plt.figure()
Plot1d(xvalues=zmid, yvalues=diff_flx, 
       markers=['*', 'o'],
       xlabel="Height, cm", ylabel="Percent difference in flux, %")



