# -*- coding: utf-8 -*-
"""debug_main_inp6.py

Debug:
--------
Main functionality of this package is debugged in respect to the input set
located in:
    xsInterface\inputsets\inp6

This debug includes a relabeling of the .coe file first

Created on Mon Feb 27 05:00:00 2023 @author: Dan Kotlyar
Last updated on Mon Feb 27 05:00:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.main import Main
from xsInterface.functions.relabelcoe import coeRelabel



inputFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\inputsets\\inp6\\controlDict"


coeRelabelFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\inputsets\\inp6\\branchLabels"

coeOrigFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\inputsets\\inp6\\combTest2.i.coe"

coeModFile = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\inputsets\\inp6\\u0.coe"

# create a modified .coe file with branches relabeled to a readable
# xsInterface format
coeRelabel(origCoeFile=coeOrigFile,
           modCoeFile=coeModFile,
           inpLabels=coeRelabelFile)


# Read the control dict
xs = Main(inputFile)

# Read xs data and templates and populate data
xs.Read()

# Write data to txt files
xs.Write()



# obtain results:
xs.Table("fuel0", ['infkappa'], time=0.0, history='nom', fuel=900, boron=500,
         dens=700)

# obtain results:
xs.Values("fuel0", 'infkappa', time=0.0, history='nom',
          dens=700)
xs.Values("fuel0", 'infkappa', time=0.0, history='nom', boron=500, dens=700)
xs.Values("fuel0", 'infkappa', fuel=900, boron=0, dens=700,time=0.0, history='nom')
xs.Values("ref0", "infsp0", fuel=900)