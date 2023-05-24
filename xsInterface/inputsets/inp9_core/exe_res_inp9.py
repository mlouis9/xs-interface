# -*- coding: utf-8 -*-
"""debug_main_inp7.py

Debug:
--------
Read a file that contains cross sections for the full core.

Created on Thu May 04 16:05:00 2023 @author: Dan Kotlyar
Last updated on Tue May 09 10:45:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.main import Main

controlFile = ".\\res\\controldict"

# Read the control dict
xs = Main(controlFile)

# Read xs data and templates and populate data (for all channels and layers)
xs.Read(readUniverses=True, readMapTemplate=True)  

# Write data to txt files
# xs.Write()  # write data

# Get results
chIds=list(xs.core.chIds)
nchs = len(chIds)
nlayers = 22

results, chIds =\
xs.CoreValues(['infnsf', 'infflx'], 
              chIds=xs.core.chIds, 
              volManip=None, 
              history=[['nom']*nlayers]*nchs,
              time=[[0.0]*nlayers]*nchs, 
              dens=[[700.0]*nlayers]*nchs,)

# Plot results
xs.SlicePlot(results['infflx'], layer=3, markersize=160, spacesize=60.0,
             textsize=5, chnls2Ignore='R', textcolor='w', textweight="bold", 
             precision=".2f", edge=2.0, norm=1E+16, label="flux [1E+16]")

xs.SlicePlot(results['infflx'], layer=15, markersize=300, spacesize=2.0,
             textsize=5, chnls2Ignore='R', textcolor='w', textweight="bold", 
             precision=".2f", edge=0.5, norm=1E+16, label="flux [1E+16]", 
             includeCols=[0, 8], includeRows=[0, 8])

