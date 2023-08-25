# -*- coding: utf-8 -*-
"""debug_main_inp7.py

Debug:
--------
Check that .coe AND .res files can be read by the package.

Created on Wed Apr 26 09:00:00 2023 @author: Dan Kotlyar
Last updated on Wed Apr 26 09:00:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.main import Main


inputFile = str(pathlib.Path("./coe/controlDict"))

# Read the control dict
xs = Main(inputFile)

# Read xs data and templates and populate data
xs.Read(readTemplate=True)

# Write data to txt files
xs.Write()





# obtain results:
xs.Table("univ0", ['infkappa'], time=0.0, history='nom', fuel=900, boron=750,
          dens=700)

# obtain results:
xs.Values("univ0", 'infflx', time=0.0, history='nom',
          dens=700)
# xs.Values("fuel0", 'infkappa', time=0.0, history='nom', boron=500, dens=700)
# xs.Values("fuel0", 'infkappa', fuel=900, boron=0, dens=700,time=0.0, history='nom')
# xs.Values("ref0", "infsp0", fuel=900)