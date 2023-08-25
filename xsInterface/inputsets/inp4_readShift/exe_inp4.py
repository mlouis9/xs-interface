# -*- coding: utf-8 -*-
"""debug_main_inp4.py

Debug:
--------
Main functionality of this package is debugged in respect to the input set
located in:
    xsInterface\inputsets\inp4

Test - SHIFT outputs


Created on Wed Sep 14 06:00:00 2022 @author: Dan Kotlyar
Last updated on Wed Sep 14 06:00:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.main import Main

inputFile = str(pathlib.Path("./controlDict"))

# Read the control dict
xs = Main(inputFile)

# Read xs data and templates and populate data
xs.Read(readTemplate=True)

# Write data to txt files
xs.Write()

# obtain results:
xs.Table("fuel0", ['kappa_fission'])

# obtain results:
xs.Values("fuel0", 'kappa_fission')
