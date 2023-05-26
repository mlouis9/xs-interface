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

inputFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\debug\\inp10_correction\\controlDict"
        


# -----------------------------------------------------------------------------
#                 READ CROSS SECTIONS
# -----------------------------------------------------------------------------

# Read the control dict
xs = Main(inputFile)

# Read xs data and templates and populate data
xs.Read(readUniverses=True)

# Read xs data and templates and populate data
# xs.Read(readUniverses=False, readMapTemplate=True)

# Write data to txt files
# xs.Write()  # I am not writing anything here

# Condense cross section to a single group
xscond = xs.Condense([10.0E+06, 0.0])

# -----------------------------------------------------------------------------
#                 ESTIMATE CROSS SECTIONS FOR THE CORE
# -----------------------------------------------------------------------------

nchs = 4
states = {
'history':[['nom', 'nom', 'nom', 'nom']]*nchs,
'time': [[0.0, 0.0, 0.0, 0.0]]*nchs,
'fuel': [[900, 900, 900, 900]]*nchs,
'boron': [[0, 0, 0, 0]]*nchs,
'dens': [[700, 700, 700, 700]]*nchs,
}

adfvals = [[[0.91, 1.11], [0.92, 1.12], [0.93, 1.13], [0.94, 1.14]]]*nchs


xs.PopulateCoreData(attributes=['infkappa', 'infsp0', 'infflx'],
                    states=states, 
                    volManip=[None, None, 'divide'],
                    sph=None, adf=adfvals)


# Write data to txt files
xs.Write()  # I am not writing anything here