# -*- coding: utf-8 -*-
"""debug_inputreader.py

Debug:
--------
Read input file

Created on Fri Apr 15 05:30:00 2022 @author: Dan Kotlyar
Last updated on Thu May 05 09:15:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.readcontroldict import Read

inputFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\inputsets\\controlDict"

# read the input file/s and collect all the universes
universes, outputs, templates, links, formats, serpent = Read(inputFile)
