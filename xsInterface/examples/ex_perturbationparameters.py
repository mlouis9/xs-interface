# -*- coding: utf-8 -*-
"""ex_perturbationparameters.py

Example:
A container to hold all possible perturbation parameters.
These perturbation parameters are used when homogenized cross sections
are defined.


Created on Mon Apr 04 15:45:00 2022 @author: Dan Kotlyar
Last updated on Mon Apr 04 15:45:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu
"""


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
