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

REL_PRECISION = 0.00001  # 0.001% - used to find indices in arrays


class SingleSet():
    """Container that stores the most basic data set

    Parameters
    ----------
    dataSetup : DataSettings object
        an object that defines the data (and type) to be collected
    statesSetup : Perturbations object
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

    def __init__(self, dataSetup, statesSetup,
                 fluxName=None, energyStruct=None):
        """Assign parameters that describe the flow"""

        # errors checking
        # ---------------------------------------------------------------------
        self._initErrors(dataSetup, statesSetup, fluxName, energyStruct)

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

    def _initErrors(self, dSetup, sSetup, fluxName, energyStruct):
        """check that the object is properly initialized"""

        # check that objects are at all defined
        _isobject(dSetup, DataSettings, "data settings")
        _isobject(sSetup, Perturbations, "perturbation data")
        # check that these objects contain the required fields
        dSetup._proofTest()
        sSetup._proofTest()
        # check that flux name and energy structure are properly defined
        if fluxName is not None:
            _isstr(fluxName, "Flux variable name")
            # make sure this variable is defined on the object
            if fluxName not in (dSetup._macro['attributes'] or
                                dSetup._micro['attributes'] or
                                dSetup._kinetics['attributes'] or
                                dSetup._meta['attributes']):
                raise ValueError("Flux name <{}> is not on the "
                                 "datasets object".format(fluxName))

        if energyStruct is not None:
            _isarray(energyStruct, "Energy structure")
            energyStruct = np.array(energyStruct)
            _is1darray(energyStruct, "Energy structure")
            _ispositiveArray(energyStruct, "Energy structure")
            _isequallength(energyStruct, dSetup.ng, "Energy structure")
            _issortedarray(energyStruct, "Energy structure")

    def _stateErrors(self, stSetup, branch, history, timeIdx, timePoint):
        """check that a state is described properly"""

        # Array with indices correponding to the branch values
        branchIndices = np.zeros(stSetup._branchN, dtype=int)

        # check that a branch is properly defined
        _isarray(branch, "Branch values")
        branch = np.array(branch, dtype=float)  # convert to ndarray
        _is1darray(branch, "Branch values")
        _isequallength(branch, stSetup._branchN, "Branch values")
        
        # check that the value for each branch is defines
        for brIdx, brName in enumerate(stSetup._branchList):
            # create lower (val0) and upper (val1) bounds of the branches
            val0 = stSetup.branch[brName]-REL_PRECISION*stSetup.branch[brName]
            val1 = stSetup.branch[brName]+REL_PRECISION*stSetup.branch[brName]
            idx, = np.where((branch[brIdx] > val0) and (branch[brIdx] < val1))
            if not idx.size:
                raise ValueError(
                        "Branch <{}> with value {} does not exist!!!\n in the "
                        "pre-defined branch points {}"
                        .format(brName, branch[brIdx],stSetup.branch[brName]))     
            else:
                branchIndices[brIdx] = idx[0]

        if history is not None:
            _isstr(history, "History name")
            _inlist(history, "History name", stSetup._historyList)
        # check that timeIdx or timePoint are properly defined
        if timeIdx is not None:
            _isint(timeIdx, "Time index")
            _isnonnegative(timeIdx, "Time index")
            _inrange(timeIdx, "Time index", [0, stSetup.time["npoints"]])
        elif timePoint is not None:
            _isnumber(timePoint, "Time point")
            _isnonnegative(timePoint, "Time point")
            lowBound =\
                stSetup.time["values"]-REL_PRECISION*stSetup.time["values"]
            upperBound =\
                stSetup.time["values"]+REL_PRECISION*stSetup.time["values"]
            timeIdx, = np.where((timePoint > lowBound) and
                                (timePoint < upperBound))
            if not timeIdx.size:
                raise ValueError("Time point {} does not exist!!!\n in the "
                                 "pre-defined points on the branches "
                                 "container {}"
                                 .format(timePoint, stSetup.time["values"]))
            else:
                timeIdx = timeIdx[0]
        return timeIdx
