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
                  meta=True, isotopes=[531350, 541350, 922350], nuclides="nd")
rc.AddData("macro",
           ["inf_rabs", "inf_nsf", "kappa", "inf_flx"])
rc.AddData("macro", ["inf_sp0"])
rc.AddData("kinetics", ["beta", "decay"])
rc.AddData("micro", ["sig_c", "sig_f", "nd"])
rc.AddData("micro", ["sig_sct"])
rc.AddData("meta", ["burnup", "keff"])
rc.AddData("meta", ["date"])


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

ss = SingleSet(rc, states, fluxName="inf_flx",
               energyStruct=[10.0E+6, 0.6025, 0.0])
ss.AddState([600.001, 600, 500], "nom", time=2.5)
# --------------
# Add macro data
# --------------
ss.AddData("macro", inf_rabs=[0.1, 0.2], inf_nsf=[0.3, 0.4],
           kappa=[0.3, 0.4], inf_flx=[0.3, 0.4])
#ss.AddData("macro", inf_sp0=[[0.1, 0.2], [-0.05, 0.3]])
ss.AddData("macro", inf_sp0=[0.1, 0.2, -0.05, 0.3])

# -----------------
# Add kinetics data
# -----------------
ss.AddData("kinetics", beta=[1, 1, 1, 1, 1, 1, 1],
           decay=[1, 1, 1, 1, 1, 1, 1])

# -----------------
# Add meta data
# -----------------
ss.AddData("meta", burnup=[1, 1, 1, 1],
           keff=[1, 1, 1, 1], date="April 09, 2022")

# -----------------
# Add micro data
# -----------------
ss.AddData("micro", sig_c=[[1, 1], [2, 2], [3, 3]])
ss.AddData("micro", sig_f=[[1, 1], [2, 2], [3, 3]])
ss.AddData("micro", nd=[[1], [1], [1]])
ss.AddData("micro", sig_sct=[[11, 12, 21, 22], [11, 12, 21, 22],
                             [11, 12, 21, 22]])

# --------------------------------------------
# check that all the data was properly defined
# --------------------------------------------
ss.ProofTest(micro=True, kinetics=False, meta=False)

# --------------------------------------------
# Get values
# --------------------------------------------
ss.GetValues(["inf_flx", "beta"])


# --------------------------------------------
# Energy condensation
# --------------------------------------------
ss1 = ss.Condense([0.6025])

# --------------------------------------------
# Data manipulation
# --------------------------------------------
ss2 = ss1.Manipulate("add", "new_nsf", "inf_nsf", "sig_f")
ss2 = ss1.Manipulate("add", "new_sct", "inf_sp0", "sig_sct")
