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
# reslt.Execute()
reslt.Iterate(
    corrattrs=['topadf'], refFlx=refFlx, newtonIters=4, krylovSpan=8, 
    dampingF=1.0)


# -----------------------------------------------------------------------------
#                 PLOT RESULTS
# -----------------------------------------------------------------------------

layers = np.linspace(0, 365.76, 37)  #active core
layers = np.hstack((-20.0, layers, 385.76))  # with reflectors
zmid = 0.5*(layers[0:-1] + layers[1:])


plt.figure()
reslt.PlotFluxes(zmid, iters=None,  markers=['--', '*', 'o'],
               chId="S1", layers=None, egroup=0)

plt.figure()
reslt.PlotFluxes(zmid, iters=None,  markers=['--', '*', 'o'],
               chId="S1", layers=None, egroup=1)


xs.ChannelsPlot('infflx', zmid, ylabel='Flux', xlabel='Height, cm', markers='ro',
                layers=np.linspace(1,30,30, dtype=int), markerfill=True)

# plt.figure()
# reslt.PlotFluxes(zmid, iters=np.array([0, 1, 2]),  markers=['--', '<', '*', 'o'], markerfill=True,
#                chId="S1", layers=layers, egroup=1)