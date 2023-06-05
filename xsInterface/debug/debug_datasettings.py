# -*- coding: utf-8 -*-
"""debug_datasettings.py

Debug:
The user needs to define the required data to be stored on the containers.
This container stores all the attributes and settings for the required data.


Created on Fri Apr 01 11:30:00 2022 @author: Dan Kotlyar
Last updated on Fri Apr 01 11:30:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

Last Checked:
---------------
06/05/2023 - DK

"""

from xsInterface.containers.datasettings import DataSettings

# Reset the container with expected values
# -----------------------------------------------------------------------------
rc = DataSettings(NG=2, DN=7, macro=True, micro=False, kinetics=True,
                  meta=False, isotopes=None)

# Feed in Macroscopic parameters
# -----------------------------------------------------------------------------
rc.AddData("macro", ["abs", "nsf", "sct"])

# Feed in kinetics parameters
# -----------------------------------------------------------------------------
rc.AddData("kinetics", ["beta", "decay"])
