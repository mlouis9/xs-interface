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

import xsInterface
from xsInterface.functions.main import Main
from xsInterface.functions.dyn3d import DYN3D
import pathlib

inputFile = str(pathlib.Path("./inputs/controlDict"))
        


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
nlayers = 34
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



casedir = str(pathlib.Path("./dyn3d"))   # dyn3d dir
casefile = "supercell"  # name of dyn3d file
exefile = "RUN_DYN3D.sh" # dyn3d executuin file

# Reset correction factors
reslt = DYN3D(xs, casedir, casefile, exefile)
# reslt.Execute()
reslt.Iterate(
    corrattrs=['topadf'], refFlx=refFlx, newtonIters=2, krylovSpan=34, 
    dampingF=1.0, writestatus=False, alpha=0.7, pert=1E-3, attrObj=None)

# reslt.Iterate(
#     corrattrs=['topadf'], refFlx=refFlx, newtonIters=13, krylovSpan=13, 
#     dampingF=1.0, writestatus=False, attrObj='infrabsxs')

# -----------------------------------------------------------------------------
#                 PLOT RESULTS
# -----------------------------------------------------------------------------

layers = np.array([0, 2, 6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54,
                      58, 62, 66, 70, 74, 78, 82, 86, 90, 94, 98, 102, 106,
                      110, 114, 118, 122, 127, 132, 137])  #active core
layers = abs(layers[::-1] - 137)
zmid = 0.5*(layers[0:-1] + layers[1:])


plt.figure()
reslt.PlotFluxes(zmid, iters=None,  markers=['--', '*', 'o'],
               chId="S1", layers=None, egroup=0, refFlag=True)

plt.figure()
reslt.PlotFluxes(zmid, iters=None,  markers=['--', '*', 'o'],
               chId="S1", layers=None, egroup=1)


plt.figure()
xs.ChannelsPlot('topadf', zmid, egroup=1)

plt.figure()
xs.ChannelsPlot('topadf', zmid, egroup=0)

serpent_keff = 1.33554E+00

diff_rho = 1E+05*(1/reslt.keff - 1/serpent_keff)
print("{} pcm".format(diff_rho))
