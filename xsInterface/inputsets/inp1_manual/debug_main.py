# -*- coding: utf-8 -*-
"""debug_main.py

Debug:
--------
Main functionality of this package

Created on Fri July 22 13:00:00 2022 @author: Dan Kotlyar
Last updated on Fri July 22 13:30:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

Last Checked:
---------------
06/05/2023 - DK

"""

from xsInterface.functions.main import Main

inputFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\inputsets\\inp1\\controlDict"

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