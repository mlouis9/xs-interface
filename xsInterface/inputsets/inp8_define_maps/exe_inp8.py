# -*- coding: utf-8 -*-
"""debug_mapping.py

Debug:
--------
mapping capability to input the distributions of channels and layers.

Created on Mon May 01 13:00:00 2023 @author: Dan Kotlyar
Last updated on Mon May 02 15:00:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.main import Main

inputFile = ".\\controlDict"
        


# -----------------------------------------------------------------------------
#                 READ CROSS SECTIONS
# -----------------------------------------------------------------------------

# Read the control dict
xs = Main(inputFile)

# Read xs data and templates and populate data
xs.Read(readUniverses=True)

# Read xs data and templates and populate data
xs.Read(readUniverses=False, readMapTemplate=True)

# Write data to txt files
xs.Write()  # I am not writing anything here


xscond = xs.Condense([10.0E+06, 0.0])

# -----------------------------------------------------------------------------
#                 ESTIMATE CROSS SECTIONS FOR THE CORE
# -----------------------------------------------------------------------------

nchs = 4
history=[['nom', 'nom', 'nom', 'nom']]*nchs
time = [[0.0, 0.0, 0.0, 0.0]]*nchs
fuel = [[900, 900, 900, 900]]*nchs
boron = [[0, 0, 0, 0]]*nchs
dens = [[700, 700, 700, 700]]*nchs

xs.CoreValues(['infkappa', 'infsp0'], 
              chIds=['S1', 'S2', 'S3', 'S4'], 
              volManip=None, 
              history=[['nom', 'nom', 'nom', 'nom']]*nchs,
              time=[[0.0, 0.0, 0.0, 0.0]]*nchs, 
              fuel=[[900, 900, 900, 900]]*nchs, 
              boron=[[0, 0, 0, 0]]*nchs,
              dens=[[700, 700, 700, 700]]*nchs)

flx2g, chIds0 =\
xs.CoreValues('infflx', 
              chIds=['S1', 'S2', 'S3', 'S4'], 
              volManip='divide',  # divide the flux by volume
              history=[['nom', 'nom', 'nom', 'nom']]*nchs,
              time=[[0.0, 0.0, 0.0, 0.0]]*nchs, 
              fuel=[[900, 900, 900, 900]]*nchs, 
              boron=[[0, 0, 0, 0]]*nchs,
              dens=[[700, 700, 700, 700]]*nchs)


flx, chIds =\
    xscond.CoreValues('infflx', 
                      chIds=['S1', 'S2', 'S3', 'S4'], 
                      volManip='divide',  # divide the flux by volume
                      history=[['nom', 'nom', 'nom', 'nom']]*nchs,
                      time=[[0.0, 0.0, 0.0, 0.0]]*nchs, 
                      fuel=[[900, 900, 900, 900]]*nchs, 
                      boron=[[0, 0, 0, 0]]*nchs,
                      dens=[[700, 700, 700, 700]]*nchs)


xscond.SlicePlot(flx['infflx'], shift=[0, 0.5, 0], layer=1, norm=1E+17,
                 markersize=250, spacesize=5, geomarker='s')




