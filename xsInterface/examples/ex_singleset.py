# -*- coding: utf-8 -*-
"""ex_singleset.py

Example:
Container to collect, store, and process data including:
    - multi-group macroscopic cross sections
    - multi-group microscopic cross sections
    - kinetic parameters
    - metadata


Created on Tue Apr 05 22:30:00 2022 @author: Dan Kotlyar
Last updated on Fri Apr 07 12:30:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu
"""


from xsInterface.containers.datasettings import DataSettings
from xsInterface.containers.perturbationparameters import Perturbations
from xsInterface.containers.singleset import SingleSet

# -----------------------------------------------------------------------------
#                       Data Settings
# -----------------------------------------------------------------------------
rc = DataSettings(NG=2, DN=7, macro=True, micro=True, kinetics=True,
                  meta=True, isotopes=[531350, 541350])
rc.AddData("macro",
           ["inf_rabs", "inf_nsf", "kappa", "inf_sp0", "inf_flx"], "array")
rc.AddData("kinetics", ["beta", "decay"], "array")
rc.AddData("micro", ["sig_c", "sig_f", "sig_n2n"], "dict")
rc.AddData("meta", ["burnup", "keff"], "array")


# -----------------------------------------------------------------------------
#                       Perturbations / Branches States
# -----------------------------------------------------------------------------
states = Perturbations(branchN=3, branches=["fuel", "dens", "cool"],
                       histN=2, histories=["nom", "pert"],
                       timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')
states.AddBranches(fuel=[600, 900, 1200, 1500],
                   dens=[600, 700, 800],
                   cool=[500, 600])
states.AddHistories(nom=[900, 700, 550],
                    pert=[950, 750, 600])


# -----------------------------------------------------------------------------
#                       Data for a Single State
# -----------------------------------------------------------------------------

ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[0.1, 4E+5])
ss.State([600.001,600,500], "nom", timePoint=2.51)
a = 1

