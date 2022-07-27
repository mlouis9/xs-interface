# -*- coding: utf-8 -*-
"""debug_main_in.py

Debug:
--------
Main functionality of this package is debugged in respect to the input set
located in:
    xsInterface\inputsets\inp2

Created on Tue July 26 15:00:00 2022 @author: Dan Kotlyar
Last updated on Tue July 26 15:00:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.main import Main

inputFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\inputsets\\inp2\\controlDict"

# Read the control dict
xs = Main(inputFile)

# Read xs data and templates and populate data
xs.Read()

# Write data to txt files
xs.Write()

# obtain results:
xs.Table("u0", ['inf_rabs', 'beta'], fuel=1500)

# obtain results:
xs.Values("u0", "inf_sp0", fuel=1500)