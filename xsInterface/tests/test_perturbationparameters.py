# -*- coding: utf-8 -*-
"""test_perturbationparameters.py

py Test:
A container to hold all possible perturbation parameters.
These perturbation parameters are used when homogenized cross sections
are defined.


Created on Tue Apr 05 15:45:00 2022 @author: Dan Kotlyar
Last updated on Tue Apr 05 15:45:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu
"""

import pytest

from xsInterface.containers.perturbationparameters import Perturbations

# Reset the container with expected values
# -----------------------------------------------------------------------------
states = Perturbations(branchN=3, branches=["fuel", "dens", "cool"],
                       histN=2, histories=["nom", "pert"],
                       timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')

# Add branches
# -----------------------------------------------------------------------------
states.AddBranches(fuel=[600, 900, 1200, 1500],
                   dens=[600, 700, 800],
                   cool=[500, 600])

# Add histories
# -----------------------------------------------------------------------------
states.AddHistories(nom=[900, 700, 550],
                    pert=[950, 750, 600])

# Proof check the data
# -----------------------------------------------------------------------------
states._proofTest()


def test_badReset():
    """Errors when reseting the settings"""

    with pytest.raises(TypeError, match="number of branches*"):
        Perturbations(branchN=3.5, branches=["fuel", "dens", "cool"],
                      histN=2, histories=["nom", "pert"],
                      timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')

    with pytest.raises(TypeError, match="number of branches*"):
        Perturbations(branchN=3.5, branches=["fuel", "dens", "cool"],
                      histN=2, histories=["nom", "pert"],
                      timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')

    with pytest.raises(TypeError, match="branch names*"):
        Perturbations(branchN=3, branches="NOT_LIST",
                      histN=2, histories=["nom", "pert"],
                      timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')

    with pytest.raises(ValueError, match="branch names*"):
        Perturbations(branchN=3, branches=["fuel", "fuel"],
                      histN=2, histories=["nom", "pert"],
                      timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')

    with pytest.raises(ValueError, match="number of branches*"):
        Perturbations(branchN=-2, branches=["fuel", "dens", "cool"],
                      histN=2, histories=["nom", "pert"],
                      timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')

    with pytest.raises(ValueError, match="branch names*"):
        Perturbations(branchN=4, branches=["fuel", "dens", "cool"],
                      histN=2, histories=["nom", "pert"],
                      timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')

    with pytest.raises(TypeError, match="number of histories*"):
        Perturbations(branchN=3, branches=["fuel", "dens", "cool"],
                      histN=2.5, histories=["nom", "pert"],
                      timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')

    with pytest.raises(TypeError, match="histories names*"):
        Perturbations(branchN=3, branches=["fuel", "mod", "cool"],
                      histN=2, histories="NOT_LIST",
                      timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')

    with pytest.raises(ValueError, match="histories names*"):
        Perturbations(branchN=3, branches=["fuel", "dens", "cool"],
                      histN=2, histories=["nom", "nom"],
                      timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')

    with pytest.raises(ValueError, match="number of histories*"):
        Perturbations(branchN=3, branches=["fuel", "dens", "cool"],
                      histN=-2, histories=["nom", "pert"],
                      timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')

    with pytest.raises(ValueError, match="histories names*"):
        Perturbations(branchN=3, branches=["fuel", "dens", "cool"],
                      histN=3, histories=["nom", "pert"],
                      timeValues=[0, 2, 2.5, 3, 4], timeUnits='MWd/kg')

    with pytest.raises(TypeError, match="Time/Burnup values*"):
        Perturbations(branchN=3, branches=["fuel", "mod", "cool"],
                      histN=2, histories=["nom", "pert"],
                      timeValues="NOT_ARRAY", timeUnits='MWd/kg')

    with pytest.raises(TypeError, match="Time/Burnup values*"):
        Perturbations(branchN=3, branches=["fuel", "mod", "cool"],
                      histN=2, histories=["nom", "pert"],
                      timeValues=[[1, 2, 3], [1, 2, 3]], timeUnits='MWd/kg')

    with pytest.raises(ValueError, match="Time/Burnup values*"):
        Perturbations(branchN=3, branches=["fuel", "mod", "cool"],
                      histN=2, histories=["nom", "pert"],
                      timeValues=[-1, 2, 3], timeUnits='MWd/kg')

    with pytest.raises(ValueError, match="Time/Burnup values*"):
        Perturbations(branchN=3, branches=["fuel", "mod", "cool"],
                      histN=2, histories=["nom", "pert"],
                      timeValues=[2, 1, 3], timeUnits='MWd/kg')

    with pytest.raises(ValueError, match="Time/Burnup values*"):
        Perturbations(branchN=3, branches=["fuel", "mod", "cool"],
                      histN=2, histories=["nom", "pert"],
                      timeValues=[2, 2, 3], timeUnits='MWd/kg')


def test_addbranch():
    """Errors for the AddBranches method"""

    with pytest.raises(KeyError, match="keyword state*"):
        states = Perturbations(branchN=3, branches=["fuel", "dens", "cool"])
        states.AddBranches(fuel1=[600, 900, 1200, 1500],
                           dens=[600, 700, 800],
                           cool=[500, 600])

    with pytest.raises(ValueError, match="Branch*"):
        states = Perturbations(branchN=3, branches=["fuel", "dens", "cool"])
        states.AddBranches(fuel=[600, 900, 1200, 1500],
                           dens=[600, 700, 800],
                           cool=[500, 600])
        states.AddBranches(fuel=[600, 900, 1200, 1500],
                           dens=[600, 700, 800],
                           cool=[500, 600])

    with pytest.raises(TypeError, match="Branch*"):
        states = Perturbations(branchN=3, branches=["fuel", "dens", "cool"])
        states.AddBranches(fuel="not_array",
                           dens=[600, 700, 800],
                           cool=[500, 600])

    with pytest.raises(TypeError, match="Branch*"):
        states = Perturbations(branchN=3, branches=["fuel", "dens", "cool"])
        states.AddBranches(fuel=[[600, 700, 800]],
                           dens=[600, 700, 800],
                           cool=[500, 600])

def test_addhistory():
    """Errors for the AddBranches method"""

    with pytest.raises(KeyError, match="History*"):
        states = Perturbations(branchN=3, branches=["fuel", "dens", "cool"],
                               histN=2, histories=["nom", "pert"],)
        states.AddHistories(nom1=[900, 700, 550],
                            pert=[950, 750, 600])

    with pytest.raises(ValueError, match="History*"):
        states = Perturbations(branchN=3, branches=["fuel", "dens", "cool"],
                               histN=2, histories=["nom", "pert"],)
        states.AddHistories(nom=[900, 700, 550],
                            pert=[950, 750, 600])
        states.AddHistories(nom=[900, 700, 550],
                            pert=[950, 750, 600])

    with pytest.raises(TypeError, match="History*"):
        states = Perturbations(branchN=3, branches=["fuel", "dens", "cool"],
                               histN=2, histories=["nom", "pert"],)
        states.AddHistories(nom="not_array",
                            pert=[950, 750, 600])

    with pytest.raises(TypeError, match="History*"):
        states = Perturbations(branchN=3, branches=["fuel", "dens", "cool"],
                               histN=2, histories=["nom", "pert"],)
        states.AddHistories(nom=[[900, 700, 550]],
                            pert=[950, 750, 600])


