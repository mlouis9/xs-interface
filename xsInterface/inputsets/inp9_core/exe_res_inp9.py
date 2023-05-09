# -*- coding: utf-8 -*-
"""debug_main_inp7.py

Debug:
--------
Read a file that contains cross sections for the full core.

Created on Thu May 04 16:05:00 2023 @author: Dan Kotlyar
Last updated on Thu May 04 16:05:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.main import Main

controlFile = ".\\res\\controldict"

# Read the control dict
xs = Main(controlFile)

# Read xs data and templates and populate data
xs.Read(what='universes')  # read only the universe data
xs.Read(what='templates')  # read the template data
# Write data to txt files
# xs.Write()  # write data





# obtain results:
# xs.Table("univ0", ['infkappa'], time=0.0, history='nom', fuel=900, boron=750,
#           dens=700)

# # obtain results:
# xs.Values("univ0", 'infflx', time=0.0, history='nom',
#           dens=700)
# xs.Values("fuel0", 'infkappa', time=0.0, history='nom', boron=500, dens=700)
# xs.Values("fuel0", 'infkappa', fuel=900, boron=0, dens=700,time=0.0, history='nom')
# xs.Values("ref0", "infsp0", fuel=900)