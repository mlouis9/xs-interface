# -*- coding: utf-8 -*-
"""singleset

Container to collect, store, and process data including:
    - state of the perturbation
    - multi-group macroscopic cross sections
    - multi-group microscopic cross sections
    - kinetic parameters
    - metadata


Created on Tue Apr 05 22:30:00 2022 @author: Dan Kotlyar
Last updated on Sun Apr 10 16:55:00 2022 @author: Dan Kotlyar

Last changed what?: AddData method

email: dan.kotlyar@me.gatech.edu
"""

import numpy as np

from xsInterface.containers.datasettings import DataSettings
from xsInterface.containers.perturbationparameters import Perturbations

from xsInterface.errors.checkerrors import _isobject, _isstr, _isarray,\
    _is1darray, _ispositiveArray, _isequallength, _issortedarray, _inlist,\
    _isnumber, _isnonnegative, _isint, _inrange, _exp2dshape
from xsInterface.containers.container_header import DATA_TYPES, REL_PRECISION

# REL_PRECISION = 0.00001  # 0.001% - used to find indices in arrays


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
    relPrecision : float
        relative precision that is used to find if a close perturbation exists

    Attributes
    ----------
    state : dict
        describes the state (branch, time, history)
    macro : dict
        names and values of macro data
    micro : dict
        names and values of micro data
    kinetics : dict
        names and values of kinetics data
    meta : dict
        names and values of meta data

    Raises
    ------
    TypeError
        If ``dataSetup`` or ``statesSetup`` are not objects.
        If ``fluxName`` is not string.
        If ``energyStruct`` is not an array.
        If ``relPrecision`` is not a number.
    ValueError
        If ``fluxName`` does not exist in the pre-defined values.
        If ``energyStruct`` is not sorted, includes negative values, or not of
        the right length.

    Examples
    --------
    >>>
    >>> ss = SingleSet(rc, states, fluxName="inf_flx",
    >>>                energyStruct=[0.1, 4E+5])

    """

    def __init__(self, dataSetup, statesSetup,
                 fluxName=None, energyStruct=None, relPrecision=REL_PRECISION):
        """Assign parameters that describe the flow"""

        # errors checking
        # ---------------------------------------------------------------------
        self._initErrors(dataSetup, statesSetup, fluxName, energyStruct,
                         relPrecision)
        self._dSetup = dataSetup  # description of data rules
        self._sSetup = statesSetup  # description of states
        self._relPrc = relPrecision
        self.state = {}  # dict to store state description
        # data dictionaries
        self.macro = {}
        self.micro = {}
        self.kinetics = {}
        self.meta = {}
        # add isotopes to the micro dictionary
        if dataSetup.dataFlags["micro"]:
            self.micro["isotopes"] = dataSetup.isotopes

    def AddState(self, branch, history=None, timeIdx=None, timePoint=None):
        """add the values that describe this state

        Parameters
        ----------
        branch : array
            set of values to describe a specific branch-off
            e.g. [Tf, Tm]=[900, 600]
        history : string
            the name of the history
        timeIdx : int
            time index
        timePoint : float
            an existing time point.
            If ``timeIdx`` is defined then this is redundant

        Raises
        ------
        TypeError
            If ``branch`` is not an array.
            If ``history`` is not string.
            If ``timeIdx`` is not an integer.
            If ``timePoint`` is not a number.
        ValueError
            If ``branch`` values do not exist.
            If ``history`` value does not exist.
            If ``timeIdx`` is out of range.
            If ``timePoint`` does not exist.

        Examples
        --------
        >>>
        >>> ss = SingleSet(rc, states, fluxName="inf_flx",
        >>>                energyStruct=[0.1, 4E+5])
        >>> ss.AddState([600.001, 600, 500], "nom", timePoint=2.5)

        """
        branchIndices, timeIdx, timePoint =\
            self._stateErrors(branch, history, timeIdx, timePoint)
        stateDict = {"stateVals": branch, "stateIdx": branchIndices,
                     "timeIdx": timeIdx, "timePoint": timePoint,
                     "historyName": history,
                     "historyVals": self._sSetup.histories[history]}
        self.state = stateDict

    def AddData(self, dtype, **kwargs):
        """add data/attributes values

        Parameters
        ----------
        dtype : str
            a string from: ["macro", "micro", "kinetics", "meta"]
        kwargs : named arguments
            keys represent the data name and value represent the values.

        Raises
        ------
        TypeError
            If ``dtype`` is not a string.
            If the arrays dimensions are not correct.
        ValueError
            If any of the named arguments is already populated with data.
            If the number of components in the named arguments is not correct.
        KeyError
            If ``dtype`` is not in ["macro", "micro", "kinetics", "meta"].
            If any of the named argument is not defined in the ``DataSettings``

        Examples
        --------
        >>> ss.AddData("macro", inf_rabs=[0.1, 0.2], inf_nsf=[0.3, 0.4])
        >>>

        """

        _isstr(dtype, "Data type")
        _inlist(dtype, "Data type", DATA_TYPES)
        if not self._dSetup.dataFlags[dtype]:
            raise ValueError("Data type <{}> was disabled in the data setup "
                             "stage".format(dtype))
        for attr, value in kwargs.items():
            if dtype == DATA_TYPES[0]:  # macro
                self._addMacroData(attr, value)
            elif dtype == DATA_TYPES[1]:  # micro
                self._addMicroData(attr, value)
            elif dtype == DATA_TYPES[2]:  # kinetics
                self._addKineticsData(attr, value)
            else:
                self._addMetaData(attr, value)

    def GetValues(self, **kwargs):
        """get data"""
        pass

    def Condense(self, condEnergy, parameters):
        """energy condensation"""
        pass

    def _initErrors(self, dSetup, sSetup, fluxName, energyStruct, relPrec):
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
            if fluxName not in (dSetup.macro['attributes'] or
                                dSetup.micro['attributes'] or
                                dSetup.kinetics['attributes'] or
                                dSetup.meta['attributes']):
                raise ValueError("Flux name <{}> is not on the "
                                 "datasets object".format(fluxName))

        if energyStruct is not None:
            _isarray(energyStruct, "Energy structure")
            energyStruct = np.array(energyStruct)
            _is1darray(energyStruct, "Energy structure")
            _ispositiveArray(energyStruct, "Energy structure")
            _isequallength(energyStruct, dSetup.ng, "Energy structure")
            _issortedarray(energyStruct, "Energy structure")
        _isnumber(relPrec, "Relative precision")

    def _stateErrors(self, branch, history, timeIdx, timePoint):
        """check that a state is described properly"""
        stSetup = self._sSetup
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
            val0 =\
                stSetup.branches[brName]-self._relPrc*stSetup.branches[brName]
            val1 =\
                stSetup.branches[brName]+self._relPrc*stSetup.branches[brName]
            idx, = np.where((branch[brIdx] > val0) & (branch[brIdx] < val1))
            if not idx.size:
                raise ValueError(
                    "Branch <{}> with value {} does not exist!!!\n in the "
                    "pre-defined branch points {}"
                    .format(brName, branch[brIdx], stSetup.branches[brName]))
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
            timePoint = stSetup.time["values"][timeIdx]
        elif timePoint is not None:
            _isnumber(timePoint, "Time point")
            _isnonnegative(timePoint, "Time point")
            lowBound =\
                stSetup.time["values"]-self._relPrc*stSetup.time["values"]
            upperBound =\
                stSetup.time["values"]+self._relPrc*stSetup.time["values"]
            timeIdx, = np.where((timePoint > lowBound) &
                                (timePoint < upperBound))
            if not timeIdx.size:
                raise ValueError("Time point {} does not exist!!!\n in the "
                                 "pre-defined points on the branches "
                                 "container {}"
                                 .format(timePoint, stSetup.time["values"]))
            else:
                timeIdx = timeIdx[0]
                timePoint = stSetup.time["values"][timeIdx]
        return branchIndices, timeIdx, timePoint

    def _addMacroData(self, attr, value):
        """add data/attributes values
        Parameters
        ----------
        attr : str
            name of the macro property to be added
        value : array
            value of the macro property to be added
        """

        dsetup = self._dSetup  # data setup/rules
        attributes = dsetup.macro["attributes"]
        dimensions = dsetup.macro["dimensions"]
        _inlist(attr, "Attribute", attributes)
        if attr in self.macro:  # check if already exists
            raise ValueError("Attribute <{}> in macro is already "
                             "populated with data".format(attr))
        # find position of the attribute in the list of attributes
        idx = attributes.index(attr)
        ndim = dimensions[idx]
        if ndim == 1:
            _isarray(value, "Attribute <{}>".format(attr))
            value = np.array(value)
            # Expected data includes: absorption, fission, ... cross sections
            _is1darray(value, "Attribute <{}>".format(attr))
            _isequallength(value, dsetup.ng, "Energy groups for "
                           "attribute <{}>".format(attr))
        elif ndim == 2:
            _isarray(value, "Attribute <{}>".format(attr))
            value = np.array(value)
            # Expected data includes: scattering matrices cross sections
            _exp2dshape(value, (dsetup.ng, dsetup.ng),
                        "Attribute <{}>".format(attr))
        self.macro[attr] = value

    def _addMicroData(self, attr, value):
        """add data/attributes values
        Parameters
        ----------
        attr : str
            name of the macro property to be added
        value : array
            value of the macro property to be added

        Note
        ----
        All the values must be provided as matrices. Rows represent isotopes
        and columns energy groups.

        """

        dsetup = self._dSetup  # data setup/rules
        nisotopes = len(dsetup.isotopes)  # number of isotopes
        attributes = dsetup.micro["attributes"]
        dimensions = dsetup.micro["dimensions"]
        _inlist(attr, "Attribute", attributes)
        if attr in self.micro:  # check if already exists
            raise ValueError("Attribute <{}> in micro is already "
                             "populated with data".format(attr))
        # find position of the attribute in the list of attributes
        idx = attributes.index(attr)
        ndim = dimensions[idx]
        if ndim == 1:
            _isarray(value, "Attribute <{}>".format(attr))
            value = np.array(value)
            # Expected data includes: microscopic fission, capture, ...
            _exp2dshape(value, (nisotopes, dsetup.ng),
                        "Attribute <{}> [row=isotopes, col=energy groups]"
                        .format(attr))
        elif ndim == 2:
            _isarray(value, "Attribute <{}>".format(attr))
            value = np.array(value)
            # Expected data includes: scattering cross sections
            _exp2dshape(value, (nisotopes, dsetup.ng*dsetup.ng),
                        "Attribute <{}> [row=isotopes, col=energy groups]"
                        .format(attr))
        self.micro[attr] = value

    def _addKineticsData(self, attr, value):
        """add data/attributes values to kinetics properties
        Parameters
        ----------
        attr : str
            name of the kinetics property to be added
        value : array
            value of the kinetics property to be added
        """

        dsetup = self._dSetup  # data setup/rules
        attributes = dsetup.kinetics["attributes"]
        dimensions = dsetup.kinetics["dimensions"]
        _inlist(attr, "Attribute", attributes)
        if attr in self.kinetics:  # check if already exists
            raise ValueError("Attribute <{}> in kinetics is already "
                             "populated with data".format(attr))
        # find position of the attribute in the list of attributes
        idx = attributes.index(attr)
        ndim = dimensions[idx]
        if ndim == 1:
            _isarray(value, "Attribute <{}>".format(attr))
            value = np.array(value)
            # Expected data includes: decay constants and beta values
            _is1darray(value, "Attribute <{}>".format(attr))
            _isequallength(value, dsetup.dn, "Delayed neutron groups for "
                           "attribute <{}>".format(attr))
        self.kinetics[attr] = value

    def _addMetaData(self, attr, value):
        """add data/attributes values to meta properties
        Parameters
        ----------
        attr : str
            name of the meta property to be added
        value : array
            value of the meta property to be added
        """

        dsetup = self._dSetup  # data setup/rules
        attributes = dsetup.meta["attributes"]
        dimensions = dsetup.meta["dimensions"]
        _inlist(attr, "Attribute", attributes)
        if attr in self.meta:  # check if already exists
            raise ValueError("Attribute <{}> in meta is already "
                             "populated with data".format(attr))
        # find position of the attribute in the list of attributes
        idx = attributes.index(attr)
        ndim = dimensions[idx]
        if ndim == 1:
            _isarray(value, "Attribute <{}>".format(attr))
            value = np.array(value)
            _is1darray(value, "Attribute <{}>".format(attr))
        elif ndim == 2:
            _isarray(value, "Attribute <{}>".format(attr))
            value = np.array(value)
        self.meta[attr] = value
