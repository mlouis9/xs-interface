# -*- coding: utf-8 -*-
"""ex_universes.py

Example:
--------
Container to collect and store ``MultipleSets``.

Created on Thu June 16 20:0:00 2022 @author: Dan Kotlyar
Last updated on Thu June 16 20:0:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

from xsInterface.functions.readinput import ReadInput

inputFile0 = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\inputsets\\u0"

inputFile1 = "C:\\Users\\dkotlyar6\\Dropbox (GaTech)\\"+\
    "Reactor-Simulation-tools\\GitHub Repositories\\Public\\"+\
        "xs-interface\\xsInterface\\inputsets\\u1"

# read the input file/s and collect data for all the universes
# -----------------------------------------------------------------------------
universes = ReadInput({}, u0=inputFile0, u1=inputFile1)

# read the input file/s and collect data for all the universes
# -----------------------------------------------------------------------------
#universes.PrintValues()


# Build Pandas Tables for all the universes
# -----------------------------------------------------------------------------
# universes.PandaTables()

# Get all the data objects for a specific universe
# -----------------------------------------------------------------------------
rc0, states0, msets0 = universes.Get("u0")
rc1, states1, msets1 = universes.Get("u1")

# Get Table  values for specific attributes and a specific universe
# -----------------------------------------------------------------------------
universes.TableValues("u0", attrs=["inf_nsf", 'inf_sp0'], fuel=900)

# Get values
# -----------------------------------------------------------------------------
universes.Values("u0", attr="inf_nsf", fuel=1500)

# compare with using the direct container
msets0.Values(attrs=["inf_nsf", 'inf_sp0'], fuel=1500)

# check that all states are defined
# missingStates, existingStates = msets0._IsCompleteTable()

