# -*- coding: utf-8 -*-
"""generate_xs.py

Generate cross sections for a case:
    - without burnup points,
    - without history branches (i.e., single nominal history branch)
    - with 3 boron levels and 3 coolant density levels
Homogeneous 2-group parameters are outputted using the WQS 22 format in DYN3D

Created on Thu Aug 11 12:30:00 2022 @author: Dan Kotlyar
Last updated on Thu Aug 11 12:30:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.main import Main

controlFile = ".\\inputs\\controldict"

# Read the control dict
xs = Main(controlFile)

# Read xs data and templates and populate data
xs.Read(readUniverses=True)

# Write data to txt files
xs.Write()





# Post-process results:
xs.Table("u0", ['inftranspxs'])

# # obtain results:
# xs.Values("fuel0", 'infkappa', time=0.0, history='nom',
#           dens=700)
# xs.Values("fuel0", 'infkappa', time=0.0, history='nom', boron=500, dens=700)
# xs.Values("fuel0", 'infkappa', fuel=900, boron=0, dens=700,time=0.0, history='nom')
# xs.Values("ref0", "infsp0", fuel=900)