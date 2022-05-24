# -*- coding: utf-8 -*-
"""singleset

Container to collect, store, and process data including:
    - state of the perturbation
    - multi-group macroscopic cross sections
    - multi-group microscopic cross sections
    - kinetic parameters
    - metadata


Created on Tue Apr 05 22:30:00 2022 @author: Dan Kotlyar
Last updated on Mon Apr 11 05:00:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
Energy condensation method - 04/13/2022 - DK

"""

import copy

import numpy as np

from xsInterface.containers.datasettings import DataSettings
from xsInterface.containers.perturbationparameters import Perturbations
from xsInterface.containers.container_header import DATA_TYPES, REL_PRECISION
from xsInterface.functions.energycondensation import EnergyCondensation
from xsInterface.errors.checkerrors import _isobject, _isstr, _isarray,\
    _is1darray, _isequallength, _issortedarray, _inlist,\
    _isnumber, _isnonnegative, _isint, _inrange, _exp2dshape, _compare2lists,\
    _islist, _isnonNegativeArray

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
        descending sorted energy structure array. Includes the energy structure
        including the lowest and highest energy values.
        For a two group structure: [E1, E2, E3],
        where E1 is the upper energy bound, E2 is energy cutoff, and E3 is the
        lowest energy bound.
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

    def __init__(self, dataSetup, statesSetup, fluxName=None,
                 energyStruct=None, relPrecision=REL_PRECISION):
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
        self.energygrid = energyStruct
        self.fluxname = fluxName
        # add isotopes to the micro dictionary
        if dataSetup.dataFlags["micro"]:
            self.micro["isotopes"] = dataSetup.isotopes

    def AddState(self, branch, history=None, timeIdx=None, time=None):
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
        time : float
            an existing time point.
            If ``timeIdx`` is defined then this is redundant

        Raises
        ------
        TypeError
            If ``branch`` is not an array.
            If ``history`` is not string.
            If ``timeIdx`` is not an integer.
            If ``time`` is not a number.
        ValueError
            If ``branch`` values do not exist.
            If ``history`` value does not exist.
            If ``timeIdx`` is out of range.
            If ``time`` does not exist.

        Examples
        --------
        >>>
        >>> ss = SingleSet(rc, states, fluxName="inf_flx",
        >>>                energyStruct=[0.1, 4E+5])
        >>> ss.AddState([600.001, 600, 500], "nom", time=2.5)

        """
        branchIndices, branchValues, timeIdx, time, historyValue =\
            self._stateErrors(branch, history, timeIdx, time)
        stateDict = {"stateVals": branchValues, "stateIdx": branchIndices,
                     "timeIdx": timeIdx, "time": time,
                     "historyName": history,
                     "historyVals": historyValue}
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

    def GetValues(self, attributes):
        """get data for a specific attribute"""

        # Single attribute
        if isinstance(attributes, str):
            if attributes in self.state:
                return self.state[attributes]
            elif attributes in self.macro:
                return self.macro[attributes]
            elif attributes in self.micro:
                return self.micro[attributes]
            elif attributes in self.kinetics:
                return self.kinetics[attributes]
            elif attributes in self.meta:
                return self.meta[attributes]
            else:
                raise KeyError("Attribute <{}> does not exist on this object"
                               .format(attributes))
        # Multiple attributes - return a dictionary
        _islist(attributes, "Attributes")
        dictValues = {}

        for attr in attributes:
            if attr in self.state:
                dictValues[attr] = self.state[attr]
            elif attr in self.macro:
                dictValues[attr] = self.macro[attr]
            elif attr in self.micro:
                dictValues[attr] = self.micro[attr]
            elif attr in self.kinetics:
                dictValues[attr] = self.kinetics[attr]
            elif attr in self.meta:
                dictValues[attr] = self.meta[attr]
            else:
                raise KeyError("Attribute <{}> does not exist on this object"
                               .format(attr))
        return dictValues

    def Condense(self, cutoffE):
        """Energy condensation method

        Condensation is performed for a new energy structure and for all the
        parameters in the macro and micro dictionaries.

        Parameters
        ----------
        cutoffE : 1-dim array
            energy cutoffs

        Raises
        ------
        TypeError
            If ``cutoffE`` is not array.
        ValueError
            If ``cutoffE`` is negative.

        Examples
        --------
        >>> ss.Condense([0.0625, 1E+03])

        """
        condObj = copy.deepcopy(self)  # deep copy of for the condensed object

        # ---------------------------------------------------------------------
        #           Condense Macro parameters (all energy dependent)
        # ---------------------------------------------------------------------
        for attr, value in self.macro.items():
            ndim = value.ndim  # 1-dim or  2-dim values are allowed
            ng = int(value.size / ndim)  # number of energy groups
            boundsE = self.energygrid
            flux = self.GetValues(self.fluxname)
            condvals, condE =\
                EnergyCondensation(ndim, ng, boundsE, value, flux, cutoffE)
            condObj.macro[attr] = condvals

        # ---------------------------------------------------------------------
        #               Condense Micro parameters
        # ---------------------------------------------------------------------
        ng = len(self.energygrid) - 1
        for attr, values in self.micro.items():
            if attr == "isotopes":
                continue
            nisotopes = len(self.micro["isotopes"])
            condvalues = np.array(values)
            for idx in range(nisotopes):
                ndim = 1  # by default
                if values[idx].size > ng:  # if matrix
                    values0 = np.reshape(values[idx], (ng, ng))
                    ndim = 2
                else:
                    values0 = values[idx]  # if a vector
                boundsE = self.energygrid
                flux = self.GetValues(self.fluxname)
                values1, condE = EnergyCondensation(ndim, ng, boundsE, values0,
                                                    flux, cutoffE)
                if ndim == 2:
                    values1 = np.reshape(values1, ng*ng)
                condvalues[idx] = values1  # values for each isotope

            # matrix for each attribute
            condObj.macro[attr] = condvalues

        # update the energy structure
        condObj.energygrid = condE
        # condensed object to be retubred
        return condObj

    def ProofTest(self, macro=True, micro=True, kinetics=True, meta=True):
        """Check that all data was inputted

        Parameters
        ----------
        macro : bool
            flag to incdicate if all data in macro must be defined
        micro : bool
            flag to incdicate if all data in micro must be defined
        kinetics : bool
            flag to incdicate if all data in kinetics must be defined
        meta : bool
            flag to incdicate if all data in meta must be defined

        """

        dSetup = copy.deepcopy(self._dSetup)  # description of data

        if macro:
            expMacro = dSetup.macro
            prdMacro = list(self.macro.keys())
            _compare2lists(expMacro, prdMacro, "Macro attr. in data setup",
                           "Macro attrs. actually defined")
        if micro:
            expMicro = dSetup.micro
            prdMicro = list(self.micro.keys())
            prdMicro.remove("isotopes")
            _compare2lists(expMicro, prdMicro, "Micro attr. in data setup",
                           "Micro attrs. actually defined")

        if kinetics:
            expKinetics = dSetup.kinetics
            prdKinetics = list(self.kinetics.keys())
            _compare2lists(expKinetics, prdKinetics,
                           "Kinetics attr. in data setup",
                           "Kinetics attrs. actually defined")
        if meta:
            expMeta = dSetup.meta
            prdMeta = list(self.meta.keys())
            _compare2lists(expMeta, prdMeta, "Meta attr. in data setup",
                           "Meta attrs. actually defined")

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
            if fluxName not in (dSetup.macro or dSetup.micro or
                                dSetup.kinetics or dSetup.meta):
                raise ValueError("Flux name <{}> is not on the "
                                 "datasets object".format(fluxName))

        if energyStruct is not None:
            _isarray(energyStruct, "Energy structure")
            energyStruct = np.array(energyStruct)
            _is1darray(energyStruct, "Energy structure")
            _isnonNegativeArray(energyStruct, "Energy structure")
            _isequallength(energyStruct, dSetup.ng+1, "Energy structure")
            _issortedarray(energyStruct[::-1], "Energy structure")
        _isnumber(relPrec, "Relative precision")

    def _stateErrors(self, branch, history, timeIdx, time):
        """check that a state is described properly"""
        stSetup = copy.deepcopy(self._sSetup)

        # sufficient data must be provided when calling this method
        if stSetup.time != {}:
            if timeIdx is None and time is None:
                raise ValueError(
                    "timeIdx or time must be defined in ""AddState")

        if stSetup.histories != {}:
            if history is None:
                raise ValueError(
                    "history must be defined in ""AddState")

        if stSetup.branches != {}:
            if branch is None:
                raise ValueError(
                    "branch must be defined in ""AddState")

        # Array with indices correponding to the branch values
        branchIndices = np.zeros(stSetup._branchN, dtype=int)
        branchValues = np.zeros(stSetup._branchN, dtype=float)

        # check that a branch is properly defined
        _isarray(branch, "Branch values")
        branch = np.array(branch, dtype=float)  # convert to ndarray
        _is1darray(branch, "Branch values")
        _isequallength(branch, stSetup._branchN, "Branch values")

        # check that the value for each branch is defines
        for brIdx, brName in enumerate(stSetup._branchList):
            # Find the closest value numerically
            cond = np.isclose(stSetup.branches[brName],
                              branch[brIdx], rtol=self._relPrc)
            if not cond.any():
                raise ValueError(
                    "Branch <{}> with value {} does not exist!!!\n in the "
                    "pre-defined branch points {}"
                    .format(brName, branch[brIdx], stSetup.branches[brName]))
            else:
                idx = np.where(cond)[0][0]
                branchIndices[brIdx] = idx
                branchValues[brIdx] = stSetup.branches[brName][idx]

        if history is not None:
            _isstr(history, "History name")
            _inlist(history, "History name", stSetup._historyList)
            historyValue = stSetup.histories[history]
        else:
            historyValue = None
        # check that timeIdx or time are properly defined
        if timeIdx is not None:
            if isinstance(timeIdx, (np.ndarray, list)) and len(timeIdx) == 1:
                timeIdx = float(timeIdx)
            _isint(timeIdx, "Time index")
            _isnonnegative(timeIdx, "Time index")
            _inrange(timeIdx, "Time index", [0, stSetup.time["npoints"]])
            time = stSetup.time["values"][timeIdx]
        elif time is not None:
            if isinstance(time, (np.ndarray, list)) and len(time) == 1:
                time = float(time)
            _isnumber(time, "Time point")
            _isnonnegative(time, "Time point")
            # Find the closest (numerically) time value 
            cond = np.isclose(stSetup.time["values"],
                              time, rtol=self._relPrc)
            if not cond.any():
                raise ValueError("Time point {} does not exist!!!\n in the "
                                 "pre-defined points on the branches "
                                 "container {}"
                                 .format(time, stSetup.time["values"]))
            else:
                timeIdx = np.where(cond)[0][0]
                time = stSetup.time["values"][timeIdx]

        return branchIndices, branchValues, timeIdx, time, historyValue

    def _addMacroData(self, attr, value):
        """add data/attributes values
        Parameters
        ----------
        attr : str
            name of the macro property to be added
        value : array
            value of the macro property to be added
        """

        dsetup = copy.deepcopy(self._dSetup)  # data setup/rules
        attributes = dsetup.macro
        _inlist(attr, "Attribute", attributes)
        if attr in self.macro:  # check if already exists
            raise ValueError("Attribute <{}> in macro is already "
                             "populated with data".format(attr))

        _isarray(value, "Attribute <{}>".format(attr))
        value = np.array(value, dtype=float)
        ndim = value.ndim
        if ndim == 2:
            # Expected data includes: scattering matrices cross sections
            _exp2dshape(value, (dsetup.ng, dsetup.ng),
                        "Attribute <{}>".format(attr))
        elif ndim == 1:        
            # Expected data includes: absorption, fission, ... cross sections
            if len(value) == dsetup.ng*dsetup.ng:  # convert to 2-dim
                value = np.reshape(value, (dsetup.ng, dsetup.ng))
            else:
                _isequallength(value, dsetup.ng, "Energy groups for "
                               "attribute <{}>".format(attr))
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

        dsetup = copy.deepcopy(self._dSetup)  # data setup/rules
        nisotopes = len(dsetup.isotopes)  # number of isotopes
        attributes = dsetup.micro
        _inlist(attr, "Attribute", attributes)
        if attr in self.micro:  # check if already exists
            raise ValueError("Attribute <{}> in micro is already "
                             "populated with data".format(attr))

        _isarray(value, "Attribute <{}>".format(attr))
        value = np.array(value, dtype=float)

        try:
            # Expected data includes: microscopic fission, capture, ...
            _exp2dshape(value, (nisotopes, dsetup.ng),
                        "Attribute <{}> [row=isotopes, col=energy groups]"
                        .format(attr))
        except ValueError:
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

        dsetup = copy.deepcopy(self._dSetup)  # data setup/rules
        attributes = dsetup.kinetics
        _inlist(attr, "Attribute", attributes)
        if attr in self.kinetics:  # check if already exists
            raise ValueError("Attribute <{}> in kinetics is already "
                             "populated with data".format(attr))

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
        attributes = dsetup.meta
        _inlist(attr, "Attribute", attributes)
        if attr in self.meta:  # check if already exists
            raise ValueError("Attribute <{}> in meta is already "
                             "populated with data".format(attr))
        try:
            value = np.array(value, dtype='float')
        except ValueError:
            pass
        self.meta[attr] = value
