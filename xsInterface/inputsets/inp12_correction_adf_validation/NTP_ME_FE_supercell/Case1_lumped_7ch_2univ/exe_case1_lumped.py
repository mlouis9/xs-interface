# -*- coding: utf-8 -*-
"""debug_mapping.py

COMPLETE LATER

Created on Mon May 01 13:00:00 2023 @author: Dan Kotlyar
Last updated on Mon May 02 15:00:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""



from xsInterface.functions.main import Main
from xsInterface.functions.dyn3d import DYN3D
import matplotlib as plt

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

nchs = 7
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



casedir = "./dyn3d"   # dyn3d dir
casefile = "case1"  # name of dyn3d file
exefile = "RUN_DYN3D" # dyn3d executuin file

# Reset correction factors
reslt = DYN3D(xs, casedir, casefile, exefile)



# -----------------------------------------------------------------------------
#                 EXECUTE DYN3D - WITH CORRECTION
# -----------------------------------------------------------------------------

reslt.Iterate(
    corrattrs=['adf'], refFlx=refFlx, newtonIters=7, krylovSpan=10,
    krylovErr=5E-05, newtonErr=1E-07,
    dampingF=0.8, lbound=0.5, ubound=1.5, pert=5E-03)

# -----------------------------------------------------------------------------
#                 PLOT RESULTS
# -----------------------------------------------------------------------------

serpent_keff = 1.26227


zmid = [0]

# plt.figure()
reslt.PlotFluxes(zmid, iters=None,  markers=['<', '*', 'o'], chId="S2")

# Plot results
xs.SlicePlot(reslt.iterOutputs[0], layer=0, markersize=3000, spacesize=2.0,
              textsize=8, textcolor='w', textweight="bold", 
              precision=".5f", edge=1.5, norm=10.0, label="Normalized fast flux", 
              egroup=0, geomarker='h', shift=[-0.5, 0, -0.5])

xs.SlicePlot(reslt.iterOutputs[-1], layer=0, markersize=3000, spacesize=2.0,
              textsize=8, textcolor='w', textweight="bold", 
              precision=".5f", edge=1.5, norm=10.0, label="Normalized fast flux", 
              egroup=0, geomarker='h', shift=[-0.5, 0, -0.5])

xs.SlicePlot(reslt.refFlx, layer=0, markersize=3000, spacesize=2.0,
              textsize=8, textcolor='w', textweight="bold", 
              precision=".5f", edge=1.5, norm=10.0, label="Normalized fast flux", 
              egroup=0, geomarker='h', shift=[-0.5, 0, -0.5])

xs.SlicePlot(reslt.iterDifferences[0], layer=0, markersize=3000, spacesize=2.0,
              textsize=8, textcolor='w', textweight="bold", 
              precision=".2f", edge=1.5, norm=1.0, label="% Diff gr-1 (no Corrections)", 
              egroup=0, geomarker='h', shift=[-0.5, 0, -0.5])

xs.SlicePlot(reslt.iterDifferences[-1], layer=0, markersize=3000, spacesize=2.0,
              textsize=8, textcolor='w', textweight="bold", 
              precision=".2f", edge=1.5, norm=1.0, label="% Diff gr-1 (with Corrections)", 
              egroup=0, geomarker='h', shift=[-0.5, 0, -0.5])

xs.SlicePlot(reslt.iterDifferences[0], layer=0, markersize=3000, spacesize=2.0,
              textsize=8, textcolor='w', textweight="bold", 
              precision=".2f", edge=1.5, norm=1.0, label="% Diff gr-2 (no Corrections)", 
              egroup=1, geomarker='h', shift=[-0.5, 0, -0.5])

xs.SlicePlot(reslt.iterDifferences[-1], layer=0, markersize=3000, spacesize=2.0,
              textsize=8, textcolor='w', textweight="bold", 
              precision=".2f", edge=1.5, norm=1.0, label="% Diff gr-2 (with Corrections)", 
              egroup=1, geomarker='h', shift=[-0.5, 0, -0.5])


xs.SlicePlot(reslt.iterInputs['adf'][-1], layer=0, markersize=3000, spacesize=2.0,
              textsize=8, textcolor='w', textweight="bold", 
              precision=".4f", edge=1.5, norm=1.0, label="ADFs gr-1", 
              egroup=0, geomarker='h', shift=[-0.5, 0, -0.5])

xs.SlicePlot(reslt.iterInputs['adf'][-1], layer=0, markersize=3000, spacesize=2.0,
              textsize=8, textcolor='w', textweight="bold", 
              precision=".4f", edge=1.5, norm=1.0, label="ADFs gr-2", 
              egroup=1, geomarker='h', shift=[-0.5, 0, -0.5])



print(reslt.keff)
pcmdiff0 = 1E+5*(1/serpent_keff-1/reslt.iterkeff[0])
pcmdiff1 = 1E+5*(1/serpent_keff-1/reslt.iterkeff[1])
print("initial {:.1f} pcm".format(pcmdiff0))
print("converged {:.1f} pcm".format(pcmdiff1))
