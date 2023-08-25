# -*- coding: utf-8 -*-
"""exe_xs_shift.py

 SHIFT outputs


Created on Wed Sep 14 06:00:00 2022 @author: Dan Kotlyar
Last updated on Wed Sep 14 06:00:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""
from xsInterface.functions.main import Main
from omnWrite import omnGen

inputFile = str(pathlib.Path("./controlDict"))

# Read the control dict
xs = Main(inputFile)

# Read xs data and templates and populate data
xs.Read(readTemplate=True)

# Write data to txt files
xs.Write()


#      NG  X        Y        Z  Part/cy  cy   ina np  pO nx  ny  nz
# omnGen(2,  18.8976, 18.8976, 1, 100000,  150, 25, 24, 5, 3,  3,  1)
