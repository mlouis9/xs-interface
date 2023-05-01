# -*- coding: utf-8 -*-
"""debug_mapping.py

Debug:
--------
mapping capability to input the distributions of channels and layers.

Created on Mon May 01 13:00:00 2023 @author: Dan Kotlyar
Last updated on Mon May 01 16:00:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.containers.mapping import Map
from xsInterface.functions.main import Main

inputFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\inputsets\\inp3\\controlDict"
        

# -----------------------------------------------------------------------------
#                 DEFINE AN ARBITRARY MAP
# -----------------------------------------------------------------------------

# Define the channels Id in the map and the indices
chsMap = [['1'], ['3', '4'], ['1']]  # channels' names
bounds = [[-1, -1], [-1, 0], [-1, -1]]  # channels idx

# Reset the container
core = Map(chsMap, bounds)

# Add channels specifications
core.Channel('1', ['ref0', 'fuel0', 'fuel0', 'ref0'], volumes=[1, 1, 1, 1])

# the user can also copy existing channels and just rename the identifier
core.Copy('1', '3')
core.Copy('1', '4')

# excess the data
#core['3']['layers']


# -----------------------------------------------------------------------------
#                 READ CROSS SECTIONS
# -----------------------------------------------------------------------------

# Read the control dict
xs = Main(inputFile)

# Read xs data and templates and populate data
xs.Read()

# Write data to txt files
xs.Write()



# -----------------------------------------------------------------------------
#                 LINK THE CROSS SECTIONS AND THE MAP
# -----------------------------------------------------------------------------

core.Validate(xs)

core.ValueChannel('1', 'infkappa', 
                  history=['nom', 'nom', 'nom', 'nom'],
                  time=[0.0, 0.0, 0.0, 0.0],
                  fuel=[900, 900, 900, 900],
                  boron=[0, 0, 0, 0],
                  dens=[700, 700, 700, 700])


# obtain results:
# xs.Table("fuel0", ['infkappa'], time=0.0, history='nom', fuel=900, boron=500,
#          dens=700)

# # obtain results:
# xs.Values("fuel0", 'infkappa', time=0.0, history='nom',
#           dens=700)
# xs.Values("fuel0", 'infkappa', time=0.0, history='nom', boron=500, dens=700)
# xs.Values("fuel0", 'infkappa', fuel=900, boron=0, dens=700,time=0.0, history='nom')
# xs.Values("ref0", "infsp0", fuel=900)



