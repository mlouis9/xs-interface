# -*- coding: utf-8 -*-
"""ex_universes.py

PYTEST:
-------
Container to collect and store multiple universes.
Each universes within this objects relies on the ``Multisets`` objects


Created on Tue July 26 05:35:00 2022 @author: Dan Kotlyar
Last updated on Tue July 26 06:00:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

"""

import pytest

import numpy as np

from xsInterface.containers.datasettings import DataSettings
from xsInterface.containers.perturbationparameters import Perturbations
from xsInterface.containers.singleset import SingleSet
from xsInterface.containers.multiplesets import MultipleSets
from xsInterface.containers.universes import Universes

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
ss0.AddState([600.001, 600, 500], "nom", time=2.5)
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
ss1.AddState([900, 600, 500], "nom", time=2.5)
ss1.AddData("macro", inf_rabs=[0.1, 0.2], inf_nsf=[0.3, 0.4],
            kappa=[0.3, 0.4], inf_flx=[0.3, 0.4])
ss1.AddData("macro", inf_sp0=[[0.1, 0.2], [-0.05, 0.3]])

# -----------------------------------------------------------------------------
#                    Add data to a MultipleSets Container
# -----------------------------------------------------------------------------
ms0 = MultipleSets(states, macro=True, micro=False, kinetics=False, meta=False)
ms0.Add(ss0)
ms0.Add(ss1)

ms1 = MultipleSets(states, macro=True, micro=False, kinetics=False, meta=False)
ms1.Add(ss0)
ms1.Add(ss1)


# -----------------------------------------------------------------------------
#                    Add data to the Universes Container
# -----------------------------------------------------------------------------

univs = Universes()
univs.Add("u0", rc, states, ms0)
univs.Add("u1", rc, states, ms1)


def test_addUniv():
    """Errors when reseting and adding universes"""


    with pytest.raises(TypeError, match="Universe*"):
        univs = Universes()
        univs.Add(999, rc, states, ms0)

    with pytest.raises(TypeError, match="Data settings*"):
        univs = Universes()
        univs.Add("u0", "BAD_rc", states, ms0)

    with pytest.raises(TypeError, match="Perturbation*"):
        univs = Universes()
        univs.Add("u0", rc, "BAD_states", ms0)

    with pytest.raises(TypeError, match="Multiple*"):
        univs = Universes()
        univs.Add("u0", rc, states, "Bad multisets")


def test_getUniv():
    """Errors when getting universe from the container"""

    with pytest.raises(KeyError, match="BAD*"):
        univs = Universes()
        univs.Add("u0", rc, states, ms0)
        univs.Add("u1", rc, states, ms1)
        univs.Get("BAD UNIV ID")


def test_DataTable():
    """Errors when obtaining the table with all states and data"""
    
    with pytest.raises(KeyError, match="BAD*"):
        univs = Universes()
        univs.Add("u0", rc, states, ms0)
        univs.Add("u1", rc, states, ms1)
        univs.PandaTables() 
        univs.TableValues("BAD UNIV", attrs=['inf_sp0'], fuel=900)

    with pytest.raises(KeyError, match="\"Attribute*"):
        univs = Universes()
        univs.Add("u0", rc, states, ms0)
        univs.Add("u1", rc, states, ms1)
        univs.PandaTables() 
        univs.TableValues("u0", attrs=["BAD ATTR", 'inf_sp0'], fuel=900)
    
    with pytest.raises(KeyError, match="bad_*"):
        univs = Universes()
        univs.Add("u0", rc, states, ms0)
        univs.Add("u1", rc, states, ms1)
        univs.PandaTables() 
        univs.TableValues("u0", attrs=['inf_sp0'], bad_state=900)


def test_Values():
    """Errors when obtaining the values in a dict form"""

    with pytest.raises(KeyError, match="bad*"):
        univs = Universes()
        univs.Add("u0", rc, states, ms0)
        univs.Add("u1", rc, states, ms1)
        univs.PandaTables() 
        univs.Values("bad univ", attr='inf_sp0', fuel=900)    

    with pytest.raises(KeyError, match="\"Attribute*"):
        univs = Universes()
        univs.Add("u0", rc, states, ms0)
        univs.Add("u1", rc, states, ms1)
        univs.PandaTables() 
        univs.Values("u0", attr='bad_attr', fuel=900) 

    with pytest.raises(KeyError, match="bad_*"):
        univs = Universes()
        univs.Add("u0", rc, states, ms0)
        univs.Add("u1", rc, states, ms1)
        univs.PandaTables() 
        univs.Values("u0", attr='inf_sp0', bad_state=1500)
        
    univs = Universes()
    univs.Add("u0", rc, states, ms0)
    univs.Add("u1", rc, states, ms1)
    univs.PandaTables() 
    prdvals = univs.Values("u0", attr='inf_nsf', fuel=900)['inf_nsf'][0]
    refvals = np.array([0.3, 0.4])
    assert prdvals == pytest.approx(refvals, rel=0.01)
    
    univs = Universes()
    univs.Add("u0", rc, states, ms0)
    univs.Add("u1", rc, states, ms1)
    univs.PandaTables() 
    prdvals = univs.Values("u0", attr='inf_nsf', fuel=1500)['inf_nsf']
    refvals = []
    assert prdvals == pytest.approx(refvals, rel=0.01)