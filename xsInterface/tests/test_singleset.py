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
Last updated on Mon Apr 11 05:40:00 2022 @author: Dan Kotlyar

changed what?: reset and state testing


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
                  meta=True, isotopes=[531350, 541350, 922350])
rc.AddData("macro",
           ["inf_rabs", "inf_nsf", "kappa", "inf_sp0", "inf_flx"],
           [1, 1, 1, 2, 1])
rc.AddData("kinetics", ["beta", "decay"], [1, 1])
rc.AddData("micro", ["sig_c", "sig_f", "sig_n2n", "sig_sct"], [1, 1, 1, 2])
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


def test_badReset():
    """Errors when reseting the settings"""

    with pytest.raises(TypeError, match="data settings*"):
        SingleSet(1, states, fluxName="inf_flx",
                  energyStruct=[10.0E+6, 0.6025, 0.0])

    with pytest.raises(TypeError, match="perturbation data*"):
        SingleSet(rc, "BAD_OBJ", fluxName="inf_flx",
                  energyStruct=[10.0E+6, 0.6025, 0.0])

    with pytest.raises(TypeError, match="Flux variable*"):
        SingleSet(rc, states, fluxName=444,
                  energyStruct=[10.0E+6, 0.6025, 0.0])

    with pytest.raises(ValueError, match="Flux name*"):
        SingleSet(rc, states, fluxName="NO_FLUX_VAR",
                  energyStruct=[10.0E+6, 0.6025, 0.0])

    with pytest.raises(TypeError, match="Energy structure*"):
        SingleSet(rc, states, fluxName="inf_flx", energyStruct="NOT_ARRAY")

    with pytest.raises(TypeError, match="Energy structure*"):
        SingleSet(rc, states, fluxName="inf_flx", energyStruct=[[1]])

    with pytest.raises(ValueError, match="Energy structure*"):
        SingleSet(rc, states, fluxName="inf_flx", energyStruct=[-1])

    with pytest.raises(ValueError, match="Energy structure*"):
        SingleSet(rc, states, fluxName="inf_flx", energyStruct=[1, 2, 3])

    with pytest.raises(ValueError, match="Energy structure*"):
        SingleSet(rc, states, fluxName="inf_flx", energyStruct=[1, 2, 3, 4])

    with pytest.raises(TypeError, match="Relative precision*"):
        SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1],
                  relPrecision="NOT_FLOAT")


def test_flags():
    """Errors for not defining flags but trying to insert data"""

    # Data Setup
    with pytest.raises(ValueError, match="Data type*"):
        rc = DataSettings(NG=2, DN=7, macro=False, micro=True, kinetics=True,
                          meta=True, isotopes=[531350, 541350, 922350])
        rc.AddData("macro", ["attr"])

    with pytest.raises(ValueError, match="Data type*"):
        rc = DataSettings(NG=2, DN=7, macro=True, micro=False, kinetics=True,
                          meta=True, isotopes=[531350, 541350, 922350])
        rc.AddData("micro", ["attr"])

    with pytest.raises(ValueError, match="Data type*"):
        rc = DataSettings(NG=2, DN=7, macro=True, micro=True, kinetics=False,
                          meta=True, isotopes=[531350, 541350, 922350])
        rc.AddData("kinetics", ["attr"])

    with pytest.raises(ValueError, match="Data type*"):
        rc = DataSettings(NG=2, DN=7, macro=True, micro=True, kinetics=True,
                          meta=False, isotopes=[531350, 541350, 922350])
        rc.AddData("meta", ["attr"])

    rc = DataSettings(NG=2, DN=7, macro=True, micro=True, kinetics=True,
                      meta=True, isotopes=[531350, 541350, 922350])

    # Data insertion
    with pytest.raises(ValueError, match="Data type*"):
        rc = DataSettings(NG=2, DN=7, macro=False, micro=True, kinetics=True,
                          meta=True, isotopes=[531350, 541350, 922350])
        # rc.AddData("macro", ["inf_sp0"], [2])
        rc.AddData("micro", ["sig_c", "sig_f", "sig_n2n"])
        rc.AddData("meta", ["burnup", "keff"], [1, 1])
        rc.AddData("kinetics", ["beta", "decay"])
        states = Perturbations(branchN=1, branches=["fuel"])
        states.AddBranches(fuel=[600, 900, 1200, 1500])
        ss = SingleSet(rc, states)
        ss.AddData("macro", gen_attr=[0.1, 0.2])

    with pytest.raises(ValueError, match="Data type*"):
        rc = DataSettings(NG=2, DN=7, macro=True, micro=False, kinetics=True,
                          meta=True, isotopes=[531350, 541350, 922350])
        rc.AddData("macro", ["inf_abs"], [1])
        # rc.AddData("micro", ["sig_c", "sig_f", "sig_n2n"])
        rc.AddData("meta", ["burnup", "keff"], [1, 1])
        rc.AddData("kinetics", ["beta", "decay"])
        states = Perturbations(branchN=1, branches=["fuel"])
        states.AddBranches(fuel=[600, 900, 1200, 1500])
        ss = SingleSet(rc, states)
        ss.AddData("micro", inf_abs=[0.1, 0.2])

    with pytest.raises(ValueError, match="Data type*"):
        rc = DataSettings(NG=2, DN=7, macro=True, micro=True, kinetics=False,
                          meta=True, isotopes=[531350, 541350, 922350])
        rc.AddData("macro", ["inf_abs"], [1])
        rc.AddData("micro", ["sig_c", "sig_f", "sig_n2n"])
        rc.AddData("meta", ["burnup", "keff"], [1, 1])
        # rc.AddData("kinetics", ["beta", "decay"])
        states = Perturbations(branchN=1, branches=["fuel"])
        states.AddBranches(fuel=[600, 900, 1200, 1500])
        ss = SingleSet(rc, states)
        ss.AddData("kinetics", inf_abs=[0.1, 0.2])

    with pytest.raises(ValueError, match="Data type*"):
        rc = DataSettings(NG=2, DN=7, macro=True, micro=True, kinetics=True,
                          meta=False, isotopes=[531350, 541350, 922350])
        rc.AddData("macro", ["inf_abs"], [1])
        rc.AddData("micro", ["sig_c", "sig_f", "sig_n2n"])
        # rc.AddData("meta", ["burnup", "keff"], [1, 1])
        rc.AddData("kinetics", ["beta", "decay"])
        states = Perturbations(branchN=1, branches=["fuel"])
        states.AddBranches(fuel=[600, 900, 1200, 1500])
        ss = SingleSet(rc, states)
        ss.AddData("meta", inf_abs=[0.1, 0.2])


def test_state():
    """Errors for the State method"""

    ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])

    with pytest.raises(ValueError, match="history*"):
        ss.AddState([625., 600, 500], timePoint=2.5)

    with pytest.raises(ValueError, match="time*"):
        ss.AddState([625., 600, 500], "nom")

    with pytest.raises(TypeError, match="Branch values*"):
        ss.AddState("NOT_ARRAY", "nom", timePoint=2.5)

    with pytest.raises(TypeError, match="Branch values*"):
        ss.AddState([[1]], "nom", timePoint=2.5)

    with pytest.raises(ValueError, match="Branch*"):
        ss.AddState([625., 600, 500], "nom", timePoint=2.5)

    with pytest.raises(TypeError, match="History*"):
        ss.AddState([600., 600, 500], 444444, timePoint=2.5)

    with pytest.raises(KeyError, match="History*"):
        ss.AddState([600., 600, 500], "BAD_HIST", timePoint=2.5)

    with pytest.raises(TypeError, match="Time index*"):
        ss.AddState([600., 600, 500], "nom", timeIdx=2.4)

    with pytest.raises(ValueError, match="Time index*"):
        ss.AddState([600., 600, 500], "nom", timeIdx=-2)

    with pytest.raises(ValueError, match="Time index*"):
        ss.AddState([600., 600, 500], "nom", timeIdx=20000)

    with pytest.raises(TypeError, match="Time point*"):
        ss.AddState([600., 600, 500], "nom", timePoint="NOT_NUM")

    with pytest.raises(ValueError, match="Time point*"):
        ss.AddState([600., 600, 500], "nom", timePoint=-25.)

    with pytest.raises(ValueError, match="Time point*"):
        ss.AddState([600., 600, 500], "nom", timePoint=2.75)


def test_getValues():
    """Errors for the getvalues method"""

    ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
    ss.AddData("macro", inf_rabs=[0.1, 0.2], inf_nsf=[0.3, 0.4])
    ss.AddData("macro", inf_sp0=[[0.1, 0.2], [-0.05, 0.3]])

    with pytest.raises(KeyError, match="Attribute*"):
        ss.GetValues("bad_attr")

    with pytest.raises(TypeError, match="Attribute*"):
        ss.GetValues(44444)


def test_condense():
    """Errors for the energy condensation method"""

    rc = DataSettings(NG=2, DN=7, macro=True, micro=True, kinetics=True,
                      meta=True, isotopes=[531350, 541350, 922350])
    rc.AddData("macro",
               ["inf_rabs", "inf_nsf", "kappa", "inf_sp0", "inf_flx"],
               [1, 1, 1, 2, 1])
    rc.AddData("kinetics", ["beta", "decay"], [1, 1])
    rc.AddData("micro", ["sig_c", "sig_f", "sig_n2n", "sig_sct"], [1, 1, 1, 2])
    rc.AddData("meta", ["burnup", "keff"], [1, 1])
    rc.AddData("meta", ["date"])

    ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
    ss.AddData("macro", inf_rabs=[0.1, 0.2], inf_nsf=[0.3, 0.4])
    ss.AddData("macro", inf_sp0=[[0.1, 0.2], [-0.05, 0.3]])

    with pytest.raises(KeyError, match="Attribute <inf_flx>*"):
        ss.Condense([2])

    ss.AddData("macro", inf_flx=[1, 1])

    with pytest.raises(TypeError, match="Energy*"):
        ss.Condense("BAD_ENERGY")

    with pytest.raises(ValueError, match="Energy*"):
        ss.Condense([-10])

    ss1 = ss.Condense([2])
    assert ss1.macro["inf_nsf"] == pytest.approx(ss.macro["inf_nsf"], 0.0001)


def test_addMacroData():
    """Errors for the AddData and specifically the macro data"""

    ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
    ss.AddData("macro", inf_rabs=[0.1, 0.2], inf_nsf=[0.3, 0.4])
    ss.AddData("macro", inf_sp0=[[0.1, 0.2], [-0.05, 0.3]])

    with pytest.raises(KeyError, match="Data type*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("BAD_TYPE", inf_rabs=[0.1, 0.2], inf_nsf=[0.3, 0.4])

    with pytest.raises(KeyError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("macro", bad_attr=[0.1, 0.2], inf_nsf=[0.3, 0.4])

    with pytest.raises(ValueError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("macro", inf_nsf=[0.1, 0.2])
        ss.AddData("macro", inf_nsf=[0.1, 0.2])

    with pytest.raises(TypeError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("macro", inf_nsf="not_array")

    with pytest.raises(TypeError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("macro", inf_nsf=[[1, 2], [1, 2]])

    with pytest.raises(ValueError, match="Energy groups*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("macro", inf_nsf=[1, 2, 3])

    with pytest.raises(TypeError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("macro", inf_sp0=[1, 2])

    with pytest.raises(ValueError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("macro", inf_sp0=[[1, 2, 3], [1, 2, 3]])


def test_addMicroData():
    """Errors for the AddData and specifically the micro data"""

    ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
    ss.AddData("micro", sig_c=[[1, 1], [2, 2], [3, 3]])
    ss.AddData("micro", sig_sct=[[11, 12, 21, 22], [11, 12, 21, 22],
                                 [11, 12, 21, 22]])

    with pytest.raises(KeyError, match="Data type*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("BAD_TYPE", sig_c=[[1, 1], [2, 2], [3, 3]])

    with pytest.raises(KeyError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("micro", bad_attr=[[1, 1], [2, 2], [3, 3]])

    with pytest.raises(ValueError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("micro", sig_c=[[1, 1], [2, 2], [3, 3]])
        ss.AddData("micro", sig_c=[[1, 1], [2, 2], [3, 3]])

    with pytest.raises(TypeError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("micro", sig_c="not_array")

    with pytest.raises(TypeError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("micro", sig_c=[[[1, 1], [2, 2], [3, 3]]])

    with pytest.raises(ValueError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("micro", sig_c=[[1, 1, 1], [2, 2, 2], [3, 3, 3]])

    with pytest.raises(ValueError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("micro", sig_sct=[[1, 1], [2, 2], [3, 3]])


def test_addKineticsData():
    """Errors for the AddData and specifically the kinetics data"""

    ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
    ss.AddData("kinetics", beta=[1, 1, 1, 1, 1, 1, 1],
               decay=[1, 1, 1, 1, 1, 1, 1])

    with pytest.raises(KeyError, match="Data type*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("bad_type", beta=[1, 1, 1, 1, 1, 1, 1],
                   decay=[1, 1, 1, 1, 1, 1, 1])

    with pytest.raises(KeyError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("kinetics", bad_attr=[1, 1, 1, 1, 1, 1, 1],
                   decay=[1, 1, 1, 1, 1, 1, 1])

    with pytest.raises(ValueError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("kinetics", beta=[1, 1, 1, 1, 1, 1, 1],
                   decay=[1, 1, 1, 1, 1, 1, 1])
        ss.AddData("kinetics", beta=[1, 1, 1, 1, 1, 1, 1])

    with pytest.raises(TypeError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("kinetics", beta="not_array",
                   decay=[1, 1, 1, 1, 1, 1, 1])

    with pytest.raises(TypeError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("kinetics", beta=[[1, 1, 1, 1, 1, 1, 1]],
                   decay=[1, 1, 1, 1, 1, 1, 1])

    with pytest.raises(ValueError, match="Delayed neutron groups*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("kinetics", beta=[1, 1],
                   decay=[1, 1, 1, 1, 1, 1, 1])


def test_addMetaData():
    """Errors for the AddData and specifically the meta data"""

    ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
    ss.AddData("meta", burnup=[1, 1, 1, 1],
               keff=[1, 1, 1, 1], date="April 09, 2022")

    with pytest.raises(KeyError, match="Data type*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("bad_type", burnup=[1, 1, 1, 1],
                   keff=[1, 1, 1, 1], date="April 09, 2022")

    with pytest.raises(KeyError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("meta", bad_attr=[1, 1, 1, 1],
                   keff=[1, 1, 1, 1], date="April 09, 2022")

    with pytest.raises(ValueError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("meta", burnup=[1, 1, 1, 1],
                   keff=[1, 1, 1, 1], date="April 09, 2022")
        ss.AddData("meta", burnup=[1, 1, 1, 1],
                   keff=[1, 1, 1, 1], date="April 09, 2022")

    with pytest.raises(TypeError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("meta", burnup="not_array",
                   keff=[1, 1, 1, 1], date="April 09, 2022")

    with pytest.raises(TypeError, match="Attribute*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("meta", burnup=[[1, 1, 1, 1]],
                   keff=[1, 1, 1, 1], date="April 09, 2022")

    with pytest.raises(ValueError, match="Delayed neutron groups*"):
        ss = SingleSet(rc, states, fluxName="inf_flx", energyStruct=[3, 2, 1])
        ss.AddData("kinetics", beta=[1, 1],
                   decay=[1, 1, 1, 1, 1, 1, 1])
