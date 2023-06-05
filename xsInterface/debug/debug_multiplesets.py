# -*- coding: utf-8 -*-
"""ex_multiplesets.py

Example:
--------
Container to collect and store ``SingleSet``s.
It also includes processing of data, such as:
    - Intersecting aspecific values over multiple single sets.
    - Spatial homogenization.
    - COMPLETE


Created on Fri Apr 15 05:30:00 2022 @author: Dan Kotlyar
Last updated on Thu May 05 09:15:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""


from xsInterface.containers.datasettings import DataSettings
from xsInterface.containers.perturbationparameters import Perturbations
from xsInterface.containers.singleset import SingleSet
from xsInterface.containers.multiplesets import MultipleSets

# -----------------------------------------------------------------------------
#                       Data Settings
# -----------------------------------------------------------------------------
rc = DataSettings(NG=2, DN=7, macro=True, micro=True, kinetics=True,
                  meta=True, isotopes=[531350, 541350, 922350], nuclides="nd")
rc.AddData("macro",
           ["inf_rabs", "inf_nsf", "kappa", "inf_flx"])
rc.AddData("macro", ["inf_sp0"])
rc.AddData("kinetics", ["beta", "decay"])
rc.AddData("micro", ["sig_c", "sig_f", "sig_n2n"])
rc.AddData("micro", ["sig_sct"])
rc.AddData("meta", ["burnup", "keff"])
rc.AddData("meta", ["date"])


# -----------------------------------------------------------------------------
#                       Perturbations / Branches States
# -----------------------------------------------------------------------------
states = Perturbations(branchN=3, branches=["fuel", "dens", "cool"],
                       timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')
states.AddBranches(fuel=[600, 900, 1200, 1500],
                   dens=[600, 700, 800],
                   cool=[500, 600])


# -----------------------------------------------------------------------------
#                       Data for a Single State-0-
# -----------------------------------------------------------------------------
ss0 = SingleSet(rc, states, fluxName="inf_flx",
                energyStruct=[10.0E+6, 0.6025, 0.0])
#ss0.AddState([600.001, 600, 500], "nom", time=2.5)
ss0.AddState([600.0, 600, 500], time=2.5)
# Add data
# --------------
ss0.AddData("macro", inf_rabs=[0.1, 0.2], inf_nsf=[0.3, 0.4],
            kappa=[0.3, 0.4], inf_flx=[0.3, 0.4])
ss0.AddData("macro", inf_sp0=[[0.1, 0.2], [-0.05, 0.3]])
ss0.AddData("kinetics", beta=[1, 1, 1, 1, 1, 1, 1],
            decay=[1, 1, 1, 1, 1, 1, 1])

ss0.AddData("meta", burnup=[1, 1, 1, 1],
            keff=[1, 1, 1, 1], date="April 09, 2022")
ss0.AddData("micro", sig_c=[[1, 1], [2, 2], [3, 3]])
ss0.AddData("micro", sig_sct=[[11, 12, 21, 22], [11, 12, 21, 22],
            [11, 12, 21, 22]])

# -----------------------------------------------------------------------------
#                       Data for a Single State-1-
# -----------------------------------------------------------------------------
ss1 = SingleSet(rc, states, fluxName="inf_flx",
                energyStruct=[10.0E+6, 0.6025, 0.0])
ss1.AddState([900, 600, 500], time=2.5)
# Add data
# --------------
ss1.AddData("macro", inf_rabs=[0.1, 0.2], inf_nsf=[0.3, 0.4],
            kappa=[0.3, 0.4], inf_flx=[0.3, 0.4])
ss1.AddData("macro", inf_sp0=[[0.1, 0.2], [-0.05, 0.3]])
ss1.AddData("kinetics", beta=[2, 2, 2, 2, 2, 2, 2],
            decay=[1, 1, 1, 1, 1, 1, 1])
# -----------------------------------------------------------------------------
#                    Add/Get data to a MultipleSets Container
# -----------------------------------------------------------------------------
ms = MultipleSets(states, macro=True, micro=False, kinetics=False, meta=False)
ms.Add(ss0, ss1)
ms.Get(branch=[600, 600, 500], time=2.5)

# -----------------------------------------------------------------------------
#                    Get Values from MultipleSets Container
# -----------------------------------------------------------------------------
#ms.DataTable('inf_nsf')
pdTable = ms.DataTable(['inf_nsf', 'inf_rabs', 'inf_flx'])

pdTable1 = ms.DataTable(macroFlag=True, microFlag=False, kineticsFlag=True)

ms.Values(attrs=["inf_flx", "inf_nsf"], fuel=900)

#a = 1
