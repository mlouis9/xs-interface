# -*- coding: utf-8 -*-
"""ex_datasettings.py

Example:
The user needs to define the required data to be stored on the containers.
This container stores all the attributes and settings for the required data.


Created on Sat Apr 02 15:30:00 2022 @author: Dan Kotlyar
Last updated on Sat Apr 02 15:30:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu
"""


from xsInterface.containers.datasettings import DataSettings

# Reset the container with expected values
# -----------------------------------------------------------------------------
rc = DataSettings(NG=2, DN=7, macro=True, micro=True, kinetics=True,
                  meta=True, isotopes=[531350, 541350])

# Feed in the required data
# -----------------------------------------------------------------------------
rc.AddData("macro", ["inf_rabs", "inf_nsf", "kappa", "inf_sp0"],
           [1, 1, 1, 2])
rc.AddData("kinetics", ["beta", "decay"],
           [1, 1])
rc.AddData("micro", ["sig_c", "sig_f", "sig_n2n"],
           [1, 1, 1])
rc.AddData("meta", ["burnup", "keff"],
           [1, 0])

# Proof check the data
# -----------------------------------------------------------------------------
rc._proofTest()
