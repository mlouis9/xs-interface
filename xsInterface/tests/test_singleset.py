# -*- coding: utf-8 -*-
"""test_singleset.py

py Test:
Container to collect, store, and process data including:
    - state of the perturbation
    - multi-group macroscopic cross sections
    - multi-group microscopic cross sections
    - kinetic parameters
    - metadata


Created on Tue Apr 05 22:30:00 2022 @author: Dan Kotlyar
Last updated on Fri Apr 07 04:10:00 2022 @author: Dan Kotlyar

changed what?: State methog
                 more detail

email: dan.kotlyar@me.gatech.edu

email: dan.kotlyar@me.gatech.edu
"""

import pytest

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


def test_badReset():
    """Errors when reseting the settings"""

    with pytest.raises(TypeError, match="data settings*"):
        SingleSet(1, states, fluxName="inf_flx", energyStruct=[0.1, 4E+5])

    with pytest.raises(TypeError, match="perturbation data*"):
        SingleSet(rc, "BAD_OBJ", fluxName="inf_flx", energyStruct=[0.1, 4E+5])

    with pytest.raises(TypeError, match="Flux variable*"):
        SingleSet(rc, states, fluxName=444, energyStruct=[0.1, 4E+5])

    with pytest.raises(ValueError, match="Flux name*"):
        SingleSet(rc, states, fluxName="NO_FLUX_VAR", energyStruct=[0.1, 4E+5])

    with pytest.raises(TypeError, match="Energy structure*"):
        SingleSet(rc, states, fluxName="inf_flx", energyStruct="NOT_ARRAY")

    with pytest.raises(TypeError, match="Energy structure*"):
        SingleSet(rc, states, fluxName="inf_flx", energyStruct="NOT_ARRAY")

    with pytest.raises(TypeError, match="Energy structure*"):
        SingleSet(rc, states, fluxName="inf_flx", energyStruct=[[1]])

    with pytest.raises(ValueError, match="Energy structure*"):
        SingleSet(rc, states, fluxName="inf_flx", energyStruct=[-1])

    with pytest.raises(ValueError, match="Energy structure*"):
        SingleSet(rc, states, fluxName="inf_flx", energyStruct=[1, 2, 3])

    with pytest.raises(ValueError, match="Energy structure*"):
        SingleSet(rc, states, fluxName="inf_flx", energyStruct=[2, 1])

    with pytest.raises(TypeError, match="Relative precision*"):
        SingleSet(rc, states, fluxName="inf_flx", energyStruct=[1, 2],
                  relPrecision="NOT_FLOAT")


def test_state():
    """Errors for the State method"""

    ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[1, 2])

    with pytest.raises(TypeError, match="Branch values*"):
        ss.State("NOT_ARRAY", "nom", timePoint=2.5)

    with pytest.raises(TypeError, match="Branch values*"):
        ss.State([[1]], "nom", timePoint=2.5)

    with pytest.raises(ValueError, match="Branch*"):
        ss.State([625., 600, 500], "nom", timePoint=2.5)

    with pytest.raises(TypeError, match="History*"):
        ss.State([600., 600, 500], 444444, timePoint=2.5)

    with pytest.raises(KeyError, match="History*"):
        ss.State([600., 600, 500], "BAD_HIST", timePoint=2.5)

    with pytest.raises(TypeError, match="Time index*"):
        ss.State([600., 600, 500], "nom", timeIdx=2.4)

    with pytest.raises(ValueError, match="Time index*"):
        ss.State([600., 600, 500], "nom", timeIdx=-2)

    with pytest.raises(ValueError, match="Time index*"):
        ss.State([600., 600, 500], "nom", timeIdx=20000)

    with pytest.raises(TypeError, match="Time point*"):
        ss.State([600., 600, 500], "nom", timePoint="NOT_NUM")

    with pytest.raises(ValueError, match="Time point*"):
        ss.State([600., 600, 500], "nom", timePoint=-25.)

    with pytest.raises(ValueError, match="Time point*"):
        ss.State([600., 600, 500], "nom", timePoint=2.75)
