# -*- coding: utf-8 -*-
"""ex_multiplesets.py

PYTEST:
-------
Container to collect and store ``SingleSet``s.
It also includes processing of data, such as:
    - Intersecting aspecific values over multiple single sets.
    - Spatial homogenization.
    - COMPLETE


Created on Fri Apr 15 05:30:00 2022 @author: Dan Kotlyar
Last updated on Fri Apr 15 06:30:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

import pytest

from xsInterface.containers.datasettings import DataSettings
from xsInterface.containers.perturbationparameters import Perturbations
from xsInterface.containers.singleset import SingleSet
from xsInterface.containers.multiplesets import MultipleSets

# -----------------------------------------------------------------------------
#                       Data Settings
# -----------------------------------------------------------------------------
rc = DataSettings(NG=2, DN=7, macro=True, micro=True, kinetics=True,
                  meta=True, isotopes=[531350, 541350, 922350])
rc.AddData("macro",
           ["inf_rabs", "inf_nsf", "kappa", "inf_flx"],
           [1, 1, 1, 1])
rc.AddData("macro", ["inf_sp0"], [2])
rc.AddData("kinetics", ["beta", "decay"])
rc.AddData("micro", ["sig_c", "sig_f", "sig_n2n"])
rc.AddData("micro", ["sig_sct"], [2])
rc.AddData("meta", ["burnup", "keff"], [1, 1])
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
#                       Data for a Single State-0-
# -----------------------------------------------------------------------------
ss0 = SingleSet(rc, states, fluxName="inf_flx",
                energyStruct=[10.0E+6, 0.6025, 0.0])
ss0.AddState([600.001, 600, 500], "nom", timePoint=2.5)
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
ss1.AddState([900, 600, 500], "nom", timePoint=2.5)
ss1.AddData("macro", inf_rabs=[0.1, 0.2], inf_nsf=[0.3, 0.4],
            kappa=[0.3, 0.4], inf_flx=[0.3, 0.4])
ss1.AddData("macro", inf_sp0=[[0.1, 0.2], [-0.05, 0.3]])

# -----------------------------------------------------------------------------
#                    Add data to a MultipleSets Container
# -----------------------------------------------------------------------------
ms = MultipleSets(states, macro=True, micro=False, kinetics=False, meta=False)
ms.Add(ss0)
# ms.Get(branch=[600, 900, 900], time=2.5, history=[900, 700, 550])
# ms.Get(branch=[600, 900, 900], time=2.5, history="nom")


def test_badReset():
    """Errors when reseting the multiplesets container"""

    with pytest.raises(TypeError, match="States*"):
        MultipleSets("BAD_STATES", macro=True)

    with pytest.raises(TypeError, match="Macro*"):
        MultipleSets(states, macro="BAD_MACRO")

    with pytest.raises(TypeError, match="Micro*"):
        MultipleSets(states, micro="BAD_MICRO")


def test_addSet():
    """Errors when adding SingleSets to the container"""

    # not all attributes are defined on the SingleSet
    with pytest.raises(ValueError, match="Micro*"):
        ms = MultipleSets(states, macro=True, micro=True)
        ms.Add(ss0)

    # the set is not a SingleSet type
    with pytest.raises(TypeError, match="Argument / Single Set*"):
        ms = MultipleSets(states, macro=True)
        ms.Add("BAD_SS")

    # the set already exists
    with pytest.raises(KeyError, match="<State*"):
        ms = MultipleSets(states, macro=True)
        ms.Add(ss0)
        ms.Add(ss0)


def test_getSet():
    """Errors when getting SingleSets to the container"""

    with pytest.raises(KeyError, match="Set*"):
        ms = MultipleSets(states, macro=True, micro=False)
        ms.Add(ss0)
        ms.Get()

    with pytest.raises(TypeError, match="Set*"):
        ms = MultipleSets(states, macro=True, micro=False)
        ms.Add(ss0)
        ms.Get(4.5)

    with pytest.raises(TypeError, match="Branch*"):
        ms = MultipleSets(states, macro=True, micro=False)
        ms.Add(ss0)
        ms.Get(branch="NOT_ARRAY")

    with pytest.raises(TypeError, match="Time*"):
        ms = MultipleSets(states, macro=True, micro=False)
        ms.Add(ss0)
        ms.Get(branch=[1, 2, 3], time="NOT_NUM")

    with pytest.raises(TypeError, match="History*"):
        ms = MultipleSets(states, macro=True, micro=False)
        ms.Add(ss0)
        ms.Get(branch=[1, 2, 3], history=44444)

    with pytest.raises(KeyError, match="History*"):
        ms = MultipleSets(states, macro=True, micro=False)
        ms.Add(ss0)
        ms.Get(branch=[1, 2, 3], history="NO_HISTORY")

    with pytest.raises(KeyError, match="State*"):
        ms = MultipleSets(states, macro=True, micro=False)
        ms.Add(ss0)
        ms.Get(branch=[1, 2, 3], history=[3, 4, 5])
