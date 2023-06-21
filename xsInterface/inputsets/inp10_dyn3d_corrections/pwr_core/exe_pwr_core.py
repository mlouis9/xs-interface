# -*- coding: utf-8 -*-
"""exe_pwr_core.py

This is a full PWR core execution with DYN3D.
The file includes correction via the JFNK method.

Created on Fri June 16 05:35:00 2023 @author: Dan Kotlyar
Last updated on Fri June 16 05:35:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.main import Main
from xsInterface.functions.dyn3d import DYN3D

controlFile = ".\\inputs\\controldict"


# -----------------------------------------------------------------------------
#                 READ CROSS SECTIONS
# -----------------------------------------------------------------------------

# Read the control dict
xs = Main(controlFile)

# Read xs data and templates and populate data
xs.Read(readUniverses=True)


# -----------------------------------------------------------------------------
#                 ESTIMATE CROSS SECTIONS FOR THE CORE
# -----------------------------------------------------------------------------

nchs = 73  # number of assemblies in the core including reflectors
nlayers = 22  # number of layers
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
casefile = "core3D"  # name of dyn3d file
exefile = "RUN_DYN3D" # dyn3d executuin file

# Reset correction factors
reslt = DYN3D(xs, casedir, casefile, exefile)
# reslt.Execute()
reslt.Iterate(
    corrattrs=['adf'], refFlx=refFlx, newtonIters=5, krylovSpan=10, 
    dampingF=1.0, writestatus=False)



# -----------------------------------------------------------------------------
#                 POST-PROCESS RESULTS
# -----------------------------------------------------------------------------


# results, chIds =\
# xs.CoreValues(['infnsf', 'infflx'], 
#               chIds=xs.core.chIds, 
#               volManip=None, 
#               history=[['nom']*nlayers]*nchs,
#               time=[[0.0]*nlayers]*nchs, 
#               dens=[[700.0]*nlayers]*nchs,)

# Plot results
# xs.SlicePlot(results['infflx'], layer=3, markersize=160, spacesize=60.0,
#              textsize=5, chnls2Ignore='R', textcolor='w', textweight="bold", 
#              precision=".2f", edge=2.0, norm=1E+16, label="flux [1E+16]")

# xs.SlicePlot(results['infflx'], layer=15, markersize=300, spacesize=2.0,
#              textsize=5, chnls2Ignore='R', textcolor='w', textweight="bold", 
#              precision=".2f", edge=0.5, norm=1E+16, label="flux [1E+16]", 
#              includeCols=[0, 8], includeRows=[0, 8])

