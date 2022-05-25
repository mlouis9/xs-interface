# -*- coding: utf-8 -*-
"""debug_inputreader.py

Debug:
--------
Read input file

Created on Fri Apr 15 05:30:00 2022 @author: Dan Kotlyar
Last updated on Thu May 05 09:15:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.readinput import ReadInput

inputFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\debug\\inp_example1"

# read the input file
rc, states, msets = ReadInput(inputFile)

# Create a pandas table foe selected properties
pdTable = msets.DataTable(
    ['inf_rabs', 'inf_nsf', 'inf_sp0', 'inf_flx', 'beta', 'sig_f'])

# Get specific values
msets.Values(attrs=["inf_nsf", 'inf_sp0'], fuel=900)