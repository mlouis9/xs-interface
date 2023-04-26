# -*- coding: utf-8 -*-
"""debug_main_inp7.py

Debug:
--------
Main functionality of this package is debugged in respect to the input set
located in:
    xsInterface\inputsets\inp3

Created on Tue July 26 15:00:00 2022 @author: Dan Kotlyar
Last updated on Tue July 26 15:00:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.main import Main

inputFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\inputsets\\inp7\\controlDict"

# Read the control dict
xs = Main(inputFile)

# Read xs data and templates and populate data
xs.Read()

# Write data to txt files
xs.Write()





# obtain results:
xs.Table("univ0", ['infkappa'], time=0.0, history='nom', fuel=900, boron=750,
         dens=700)

# obtain results:
# xs.Values("fuel0", 'infkappa', time=0.0, history='nom',
#           dens=700)
# xs.Values("fuel0", 'infkappa', time=0.0, history='nom', boron=500, dens=700)
# xs.Values("fuel0", 'infkappa', fuel=900, boron=0, dens=700,time=0.0, history='nom')
# xs.Values("ref0", "infsp0", fuel=900)