# -*- coding: utf-8 -*-
"""debug_main_in.py

Debug:
--------
Main functionality of this package is debugged in respect to the input set
located in:
    xsInterface\inputsets\inp2

Created on Tue July 26 15:00:00 2022 @author: Dan Kotlyar
Last updated on Tue July 26 15:00:00 2022 @author: Dan Kotlyar

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
xs.Table("u0", ['inf_nsf'], time=0.0, history='nom', fuel=900, mod=650,
         cool=600)

# obtain results:
xs.Values("u0", 'inf_nsf', time=0.0, history='nom',
          cool=600)
xs.Values("u0", 'inf_nsf', time=0.0, history='nom', mod=650, cool=550)
xs.Values("u0", 'inf_nsf', fuel=900, mod=650, cool=600,time=0.0, history='nom')
xs.Values("u0", "sig_f", fuel=900)