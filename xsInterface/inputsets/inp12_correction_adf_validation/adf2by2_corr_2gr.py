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

nchs = 4
nlayers = 1
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


refFlx = xs.core.corevalues['infflx']
# refFlx, chIds = xs.CoreValues('infflx', volManip=['divide'])
# refFlx = refFlx['infflx']


# -----------------------------------------------------------------------------
#                 EXECUTE DYN3D
# -----------------------------------------------------------------------------



casedir = ".\\dyn3d"   # dyn3d dir
casefile = "2x2PWR2g"  # name of dyn3d file
exefile = "RUN_DYN3D" # dyn3d executuin file

# Reset correction factors
reslt = DYN3D(xs, casedir, casefile, exefile)


# -----------------------------------------------------------------------------
#                 PLOT RESULTS
# -----------------------------------------------------------------------------

# serpent_keff = 1.08880E+00
# reslt.keff
# reslt.refFlx
# reslt.flux


# -----------------------------------------------------------------------------
#                 EXECUTE DYN3D - WITH CORRECTION
# -----------------------------------------------------------------------------

reslt.Iterate(
    corrattrs=['adf'], refFlx=refFlx, newtonIters=8,
    dampingF=0.8, lbound=0.9, ubound=1.1, pert=1E-03)


zmid = [0]

# plt.figure()
reslt.PlotFluxes(zmid, iters=None,  markers=['<', '*', 'o'], chId="RR4")

# Plot results
xs.SlicePlot(reslt.iterOutputs[-1], layer=0, markersize=5000, spacesize=2.0,
              textsize=12, textcolor='w', textweight="bold", 
              precision=".2f", edge=1.5, norm=1.0, label="Normalized fast flux", 
              egroup=0)

xs.SlicePlot(reslt.iterOutputs[-1], layer=0, markersize=5000, spacesize=2.0,
              textsize=12, textcolor='w', textweight="bold", 
              precision=".2f", edge=1.5, norm=1.0, label="Normalized thermal flux", 
              egroup=1)


xs.SlicePlot(reslt.iterDifferences[-1], layer=0, markersize=5000, spacesize=2.0,
              textsize=12, textcolor='w', textweight="bold", 
              precision=".2f", edge=1.5, norm=1.0, label="Percent difference in fast flux", 
              egroup=0)

xs.SlicePlot(reslt.iterDifferences[-1], layer=0, markersize=5000, spacesize=2.0,
              textsize=12, textcolor='w', textweight="bold", 
              precision=".2f", edge=1.5, norm=1.0, label="Percent difference in thermal flux", 
              egroup=1)


xs.SlicePlot(reslt.refFlx, layer=0, markersize=5000, spacesize=2.0,
              textsize=12, textcolor='w', textweight="bold", 
              precision=".2f", edge=1.5, norm=1.0, label="Normalized fast flux", 
              egroup=0)

xs.SlicePlot(reslt.refFlx, layer=0, markersize=5000, spacesize=2.0,
              textsize=12, textcolor='w', textweight="bold", 
              precision=".2f", edge=1.5, norm=1.0, label="Normalized thermal flux", 
              egroup=1)


xs.SlicePlot(reslt.iterDifferences[0], layer=0, markersize=5000, spacesize=2.0,
              textsize=12, textcolor='w', textweight="bold", 
              precision=".2f", edge=1.5, norm=1.0, label="Percent difference in fast flux", 
              egroup=0)

xs.SlicePlot(reslt.iterDifferences[0], layer=0, markersize=5000, spacesize=2.0,
              textsize=12, textcolor='w', textweight="bold", 
              precision=".2f", edge=1.5, norm=1.0, label="Percent difference in thermal flux", 
              egroup=1)


xs.SlicePlot(reslt.iterInputs['adf'][-1], layer=0, markersize=5000, spacesize=2.0,
              textsize=12, textcolor='w', textweight="bold", 
              precision=".4f", edge=1.5, norm=1.0, label="ADFs fast group", 
              egroup=0)

xs.SlicePlot(reslt.iterInputs['adf'][-1], layer=0, markersize=5000, spacesize=2.0,
              textsize=12, textcolor='w', textweight="bold", 
              precision=".4f", edge=1.5, norm=1.0, label="ADFs thermal group", 
              egroup=1)


print(reslt.keff)
pcmdiff = 1E+5*(1/1.08880E+00-1/reslt.keff)
print("{:.1f} pcm".format(pcmdiff))


# Plot results
xs.SlicePlot(reslt.iterOutputs[0], layer=0, markersize=5000, spacesize=2.0,
              textsize=12, textcolor='w', textweight="bold", 
              precision=".4f", edge=1.5, norm=1.0, label="Normalized fast flux", 
              egroup=0)

xs.SlicePlot(reslt.iterOutputs[0], layer=0, markersize=5000, spacesize=2.0,
              textsize=12, textcolor='w', textweight="bold", 
              precision=".4f", edge=1.5, norm=1.0, label="Normalized thermal flux", 
              egroup=1)




xs.SlicePlot(reslt.iterInputs['adf'][0], layer=0, markersize=5000, spacesize=2.0,
              textsize=12, textcolor='w', textweight="bold", 
              precision=".4f", edge=1.5, norm=1.0, label="ADFs fast group", 
              egroup=0)

xs.SlicePlot(reslt.iterInputs['adf'][0], layer=0, markersize=5000, spacesize=2.0,
              textsize=12, textcolor='w', textweight="bold", 
              precision=".4f", edge=1.5, norm=1.0, label="ADFs thermal group", 
              egroup=1)
