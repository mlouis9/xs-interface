# -*- coding: utf-8 -*-
"""debug_mapping.py

Debug:
--------
mapping capability to input the distributions of channels and layers.

Created on Mon May 01 13:00:00 2023 @author: Dan Kotlyar
Last updated on Mon May 02 15:00:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""


from xsInterface.functions.main import Main

inputFile = ".\\inputs\\controlDict"
        


# -----------------------------------------------------------------------------
#                 READ CROSS SECTIONS
# -----------------------------------------------------------------------------

# Read the control dict
# xs = Main(inputFile)

# Read xs data and templates and populate data
# xs.Read(readTemplate=True)

# xs.Write()

# Store all the cross sections
# xs.Store('xs')  # UNCOMMENT TO STORE TO PICKLE FILE


# Load all the cross sections
# Execute the 1st part so that the object is generated first
xs = Main('xs.pkl')

