# -*- coding: utf-8 -*-
"""debug_inputreader.py

Debug:
--------
Read input file

Created on Fri Apr 15 05:30:00 2022 @author: Dan Kotlyar
Last updated on Thu May 05 09:15:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.readtemplate import ReadTemplate
from xsInterface.functions.readinput import ReadInput


inputFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\debug\\debugfiles\\bad_template"

univFile0 = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\inputsets\\u0"

univFile1 = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\inputsets\\u1"


# read the universe file/s and collect data for all the universes
# -----------------------------------------------------------------------------
universes = ReadInput({}, u0=univFile0, u1=univFile1)

# read the template files
# -----------------------------------------------------------------------------
# default formats for outputting data
STATE_FRMT = "{:5.3f}"
VAR_FRMT = "{:d}"
ATTR_FRMT = "{:5.5e}"
ROW_VALS_N = 5  # maximum number of values printed in a line
formats = {"state": "{:5.3f}", "var": "{:d}", "attr": "{:5.5e}", "nrow": 5}
dataFile = ReadTemplate(inputFile, universes, formats)

a = 1