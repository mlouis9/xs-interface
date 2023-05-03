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
        "xs-interface\\xsInterface\\inputsets\\inp8_maps\\controlDict"
        


# -----------------------------------------------------------------------------
#                 READ CROSS SECTIONS
# -----------------------------------------------------------------------------

# Read the control dict
xs = Main(inputFile)

# Read xs data and templates and populate data
xs.Read()

# Write data to txt files
# xs.Write()  # I am not writing anything here


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

xs.CoreValues('infflx', 
              chIds=['S1', 'S2', 'S3', 'S4'], 
              volManip='divide',  # divide the flux by volume
              history=[['nom', 'nom', 'nom', 'nom']]*nchs,
              time=[[0.0, 0.0, 0.0, 0.0]]*nchs, 
              fuel=[[900, 900, 900, 900]]*nchs, 
              boron=[[0, 0, 0, 0]]*nchs,
              dens=[[700, 700, 700, 700]]*nchs)


# -----------------------------------------------------------------------------
#                 DEFINE THE MAP MANUALLY - NOT USED ANYMORE
# -----------------------------------------------------------------------------

# # Define the channels Id in the map and the indices
# chsMap = [['1'], ['3', '4'], ['1']]  # channels' names
# bounds = [[-1, -1], [-1, 0], [-1, -1]]  # channels idx

# # Reset the container
# core = Map(chsMap, bounds)

# # Add channels specifications
# core.Channel('1', ['ref0', 'fuel0', 'fuel0', 'ref0'], volumes=[1, 1, 1, 1])

# # the user can also copy existing channels and just rename the identifier
# core.Copy('1', '3')
# core.Copy('1', '4')

# # excess the data
# #core['3']['layers']



