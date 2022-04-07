# -*- coding: utf-8 -*-
"""singleset

Container to collect, store, and process data including:
    - multi-group macroscopic cross sections
    - multi-group microscopic cross sections
    - kinetic parameters
    - metadata


Created on Tue Apr 05 22:30:00 2022 @author: Dan Kotlyar
Last updated on Wed Apr 06 12:30:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu
"""

import numpy as np

from xsInterface.containers.datasettings import DataSettings
from xsInterface.containers.perturbationparameters import Perturbations

from xsInterface.errors.checkerrors import _isobject, _isstr, _isarray,\
    _is1darray, _ispositiveArray, _isequallength, _issortedarray, _inlist,\
    _isnumber, _isnonnegative, _isint, _inrange

REL_PRECISION = 0.0001  # 0.01% - used to find indices in arrays


class SingleSet():
    """Container that stores the most basic data set

    Parameters
    ----------
    datasets : DataSettings object
        an object that defines the data (and type) to be collected
    branches : Perturbations object
        an object to store the perturbation states including branches, history,
        and time parameters.
    fluxName : string
        name of the flux variable on the ``datasets`` object.
    energyStruct : array
        sorted energy structure array. Includes the energy structure excluding
        the lowest energy value. For a two group structure: [E1, E2], where
        E1 is the enrgy cutoff and E2 is the highest energy of the neutrons.

    Attributes
    ----------
    COMPLETE

    """

    def __init__(self, datasets, branches, fluxName=None, energyStruct=None):
        """Assign parameters that describe the flow"""

        # errors checking
        # ---------------------------------------------------------------------
        self._initErrors(datasets, branches, fluxName, energyStruct)

    def state(self, branch, history=None, timeIdx=None, timePoint=None):
        """add the values that describe this state"""
        pass

    def data(self, **kwargs):
        """add data and populate attributes"""
        pass

    def getvalues(self, **kwargs):
        """get data"""
        pass

    def condense(self, condEnergy, parameters):
        """energy condensation"""
        pass

    def _initErrors(self, datasets, branches, fluxName, energyStruct):
        """check that the object is properly initialized"""

        # check that objects are at all defined
        _isobject(datasets, DataSettings, "data settings")
        _isobject(branches, Perturbations, "branches")
        # check that these objects contain the required fields
        datasets._proofTest()
        branches._proofTest()
        # check that flux name and energy structure are properly defined
        if fluxName is not None:
            _isstr(fluxName, "Flux variable name")
            # make sure this variable is defined on the object
            if fluxName not in (datasets._macro['attributes'] or
                                datasets._micro['attributes'] or
                                datasets._kinetics['attributes'] or
                                datasets._meta['attributes']):
                raise ValueError("Flux name <{}> is not on the "
                                 "datasets object".format(fluxName))

        if energyStruct is not None:
            _isarray(energyStruct, "Energy structure")
            energyStruct = np.array(energyStruct)
            _is1darray(energyStruct, "Energy structure")
            _ispositiveArray(energyStruct, "Energy structure")
            _isequallength(energyStruct, datasets.ng, "Energy structure")
            _issortedarray(energyStruct, "Energy structure")

    def _stateErrors(self, branches, branch, history, timeIdx, timePoint):
        """check that a state is described properly"""

        # check that a branch is properly defined
        _isarray(branch, "Branch values")
        branch = np.array(branch)  # convert to ndarray
        _is1darray(branch, "Branch values")
        _isequallength(branch, branches._branchN, "Branch values")
        # NEED to check that the branch exists!!!
        #
        # COMPLETE HERE
        #
        # check that history is defined
        if history is not None:
            _isstr(history, "History name")
            _inlist(history, "History name", branches._historyList)
        # check that timeIdx or timePoint are properly defined
        if timeIdx is not None:
            _isint(timeIdx, "Time index")
            _isnonnegative(timeIdx, "Time index")
            _inrange(timeIdx, "Time index", [0, branches.time["npoints"]])
        elif timePoint is not None:
            _isnumber(timePoint, "Time point")
            _isnonnegative(timePoint, "Time point")
            lowBound =\
                branches.time["values"]-REL_PRECISION*branches.time["values"]
            upperBound =\
                branches.time["values"]+REL_PRECISION*branches.time["values"]
            timeIdx, = np.where((timePoint > lowBound) and
                                (timePoint < upperBound))
            if not timeIdx.size:
                raise ValueError("Time point {} does not exist!!!\n in the "
                                 "pre-defined points on the branches "
                                 "container {}"
                                 .format(timePoint, branches.time["values"]))
        return timeIdx
