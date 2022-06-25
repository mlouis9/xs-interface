# -*- coding: utf-8 -*-
"""multiplesets

Container to collect and store ``SingleSet``s.
The container incorporates methods to allow adding and retreiving data easily:
    - Add method (store single or multiple ``SingleSet``s)
    - Get method (obtain a ``SingleSet``)
    - DataTable (obtain states and data values in an easy-to-read table format)
    - Values (obtain values for specific set of states)
    - Condense (to be completed based on ``SingleSet``)
It also includes processing of data, such as:
    - Future: Intersecting a specific values over multiple single sets.
    - Interpolation



Created on Thu Apr 14 05:45:00 2022 @author: Dan Kotlyar
Last updated on Thu May 05 12:30:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
__init__ capability - 04/14/2022 - DK
Add method - 04/14/2022 - DK
Get method - 04/16/2022 - DK
DataTable - 05/05/2022 - DK
Values - 05/05/2022 - DK

"""
import copy

from collections import namedtuple

import numpy as np
import pandas as pd
import itertools

from xsInterface.containers.singleset import SingleSet
from xsInterface.containers.perturbationparameters import Perturbations
from xsInterface.errors.checkerrors import _isobject, _isbool, _isint,\
    _isarray, _is1darray, _inlist, _isnumber, _inrange, _arriscloseInList,\
    _islist


StateDescrp = namedtuple("State", ["history", "time", "branch"])


class MultipleSets():
    """A container to store the data for all the perturbation states

    Parameters
    ----------
    states : Perturbations object
        an object with perturbation states including branches, history,
        and time parameters.
    macro : bool
        flag to incdicate if all data in macro must be defined
    micro : bool
        flag to incdicate if all data in micro must be defined
    kinetics : bool
        flag to incdicate if all data in kinetics must be defined
    meta : bool
        flag to incdicate if all data in meta must be defined

    Attributes
    ----------
    setIds : list of strings
        complete list of strings for all the sets to be provided.
    macro : bool
        flag to incdicate if all data in macro must be defined
    micro : bool
        flag to incdicate if all data in micro must be defined
    kinetics : bool
        flag to incdicate if all data in kinetics must be defined
    meta : bool
        flag to incdicate if all data in meta must be defined
    sets : dict
        keys are indices and values are ``SingleSet`` objects.
    nsets : int
        number of ``SingleSet``s on the ``MultipleSets`` object.
    states : dict
        description of all the perturbation states.
    setsmap : dict
        link between the nametuples that describe the state and
        indices in the ``sets`` dict.

    Raises
    ------
    TypeError
        If ``macro``, ``micro``, ``kinetics``, ``meta`` are not boolean.

    Methods
    -------
    Add : add a single multiple data for different states
    Get : obtain a single ``SingleSet`` object for a specific state
    DataTable : obtain table with states and values for all/selected attributes
    Values : obtain values of a specific property over multiple states
    Interpolate : (TBC) obtain the interpolated/weighted

    Examples
    --------
    >>> ms = MultipleSets(macro=True, micro=False, kinetics=False, meta=False)

    """

    def __init__(self, states, macro=False, micro=False, kinetics=False,
                 meta=False):

        _isobject(states, Perturbations, "States data")
        _isbool(macro, "Macro flag")
        _isbool(micro, "Micro flag")
        _isbool(kinetics, "Kinetics flag")
        _isbool(meta, "Meta flag")

        self.sets = {}  # empty dictionary to store all sets
        self._flags = {"macro": macro, "micro": micro, "kinetics": kinetics,
                       "meta": meta}
        self.states = states
        self.setsmap = {}  # dictionary to link between states and indices
        self.nsets = 0  # tracks the number of sets

    def Add(self, *argv):
        """Add new data for a specific set

        The ``Add`` method allows to add  a ``SingleSet`` object
        with all its attributes to the ``MultipleSets`` object.
        The ``Add`` method adds all the sets that correposnd to the different
        histories, times, and branches (i.e., states).

        Parameters
        ----------
        argv : non-named arguments
            non-keyworded variable length argument list. Each argument
            represents a ``SingleSet`` object that contains all the required
            attributes, e.g. ``macro`` and ``meta``.

        Raises
        ------
        TypeError
            If arguments in ``argv`` are not ``SingleSet`` object.
        KeyError
            If a ``SingleSet`` is already defined.

        Examples
        --------
        >>> ms = MultipleSets(macro=True)
        >>> ms.Add(ss0)

        """

        for arg in argv:
            # check that argument is a SingleSet object
            _isobject(arg, SingleSet, "Argument / Single Set Data")
            # check that object contains all the fields
            arg.ProofTest(self._flags["macro"], self._flags["micro"],
                          self._flags["kinetics"], self._flags["meta"])

            state = getattr(arg, "state")  # get the description of state
            history = state['historyVals']
            time = state['time']
            branch = state['stateVals']
            # State nametuple
            stateId = StateDescrp(history, time, branch)
            # check if already exists
            if str(stateId) in self.setsmap:
                raise KeyError("<{}> already exists in sets.".format(stateId))

            # assign data and index
            self.sets[self.nsets] = arg
            self.setsmap[str(stateId)] = self.nsets
            self.nsets += 1

    def Get(self, setIdx=None, branch=None, time=None, history=None,
            errFlag=False):
        """Obtains a SingleSet object for a specific state

        Parameters
        ----------
        setIdx : int
            index/position of the set in the sets dictionary
        history : array
            values that represent a history
        time : float/number
            value of the time point
        branch : array
            set of values for the specific branch
        errFlag : boolean
            indicates whether error should be raised if state not found

        Returns
        -------
        SingleSet object

        Raises
        ------
        TypeError
            If the ``setIdx`` is not int.
        KeyError
            If ``setIdx`` is not in the ``sets`` dict.
            If ``branch``-``time``-``history`` triplet does not exist.

        Examples
        --------
        >>> ms = MultipleSets(macro=True)
        >>> ms.Add(ss0)
        >>> ms.Get(0)
        >>> ms.Get(branch=[600, 500, 400])

        """
        # check variable type
        if setIdx is not None:
            _isint(setIdx, "Set Index")
            _inrange(setIdx, "Set Index", [0, self.nsets-1])
        elif branch is not None:
            _isarray(branch, "Branch")
            branch = np.array(branch, dtype=float)
            _is1darray(branch, "Branch")
            if time is not None:
                _isnumber(time, "Time")
                time = float(time)
                _inlist(time, "Time", self.states.time['values'])
            if history is not None:
                if isinstance(history, str):  # name of history is provided
                    _inlist(history, "History",
                            list(self.states.histories.keys()))
                    history = self.states.histories[history]

                else:  # numerical value of history provided
                    _isarray(history, "History")
                    _is1darray(history, "History")
                    history = np.array(history, dtype=float)
                    historyList = list(self.states.histories.values())
                    idxHist =\
                        _arriscloseInList(history, "History", historyList)
                    history = historyList[idxHist]
            _isbool(errFlag, "Error flag")
            # Obtain the state description
            stateId = str(StateDescrp(history, time, branch))
            try:
                _inlist(stateId, "State", list(self.setsmap.keys()))
                setIdx = self.setsmap[stateId]
            except KeyError:
                if errFlag:
                    _inlist(stateId, "State", list(self.setsmap.keys()))
                else:
                    return None
        else:
            raise KeyError("Set index or the history-time-branch values must "
                           "be provided.")
        return self.sets[setIdx]


    def Condense(self, cutoffE):
        """Energy condensation method

        Condensation is performed for a new energy structure and for all the
        parameters in the macro and micro dictionaries over all existing states

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
        for iset, ss in self.sets.items():
            condObj.sets[iset] = ss.Condense(cutoffE)
        ng = len(ss.energygrid) - 1
        return condObj, ng


    def Manipulate(self, modes, attrs, attrs1, attrs2):
        """Mathematical operation between two attributes or attribute-constant

        Mathematical operation is performed between two macro/micro attributes
        including:
            - Multiplication, division, addition, and subtraction operations

        Parameters
        ----------
        modes : string or list of strings
            types of the mathematical relation
            ["multiply", "divide", "add", "subtract"]
        attrs : string or list of strings
            name/ss of attribute/s where results will be written to.            
        attrs1 : string or list of strings
            names of attributes type-1 (can be macro or micro)
        attrs2 : string or list of strings
            names of attributes type-2 (can be macro or micro) 


        Raises
        ------
        TypeError
            If any of the ``modes``, ``attrs``, ``attrs1``, ``attrs2`` is
            not string or list of strings.
        ValueError
            If the operations within ``modes`` are not defined.
            If the dimensions of ``modes``, ``attrs1``, ``attrs2``
            dot not correspond to the dimensions of ``attrs``


        Examples
        --------
        >>> ss.BinaryOperation(substract, FISS_NEW,  FISS, sig_f)

        """
        newObj = copy.deepcopy(self)
        for iset, ss in self.sets.items():
            newObj.sets[iset] = ss.Manipulate(modes, attrs, attrs1, attrs2)
        return newObj


    def __getitem__(self, setIdx):
        """direct method to obtain a set only if index is known"""
        return self.sets[setIdx]

    def DataTable(self, attrs=None, macroFlag=None, microFlag=None,
                  kineticsFlag=None, metaFlag=None):
        """Create a table with existing states and values for all attributes

        Loops over the ``MultipleSets`` object to collect all existing states
        and values for a specific attribute.

        Parameters
        ----------
        attrs : string or list of strings
            name of existing fields/attributes within a `SingleSet` object
        macroFlag : boolean, default is True
            flag to indicate if all macro attributes are included in the table
        microFlag : boolean, default is True
            flag to indicate if all micro attributes are included in the table
        kineticsFlag : boolean, default is True
            flag to indicate if all kinetics attributes are included in table
        metaFlag : boolean, default is False
            flag to indicate if all meta attributes are included in the table        

        Attributes
        ----------
        pandasTable : Pandas object
            contains all the state names, branches, and values for the specific

        Returns
        -------
        table : Pandas object
            contains all the state names, branches, and values for the specific

        Raises
        ------
        TypeError
            If ``attrs`` is not string, list, or None.
            If ``macroFlag``, ``microFlag``, ``kineticsFlag``, ``metaFlag`` are
            not booleans.


        Examples
        --------
        >>> pdTable = ms.DataTable('flx')
        >>> pdTable = ms.DataTable(['inf_nsf', 'inf_rabs', 'inf_flx'])
        >>> pdTable = ms.DataTable(macroFlag=True, microFlag=False,
                                   kineticsFlag=False)
        ...   history  time  ...                   beta
        ...   0    None   2.5  ...  [1, 1, 1, 1, 1, 1, 1]
        ...   1    None   2.5  ...  [2, 2, 2, 2, 2, 2, 2]

        """

        # apply default values
        if macroFlag is None:
            macroFlag = self._flags["macro"]
        if microFlag is None:
            microFlag = self._flags["micro"]
        if kineticsFlag is None:
            kineticsFlag = self._flags["kinetics"]
        if metaFlag is None:
            metaFlag = self._flags["meta"]

        if attrs is not None:
            if isinstance(attrs, str):
                attrs = [attrs]
            _islist(attrs, "Attributes")
        else:
            attrs = []
            _isbool(macroFlag, "Macro flag")
            _isbool(microFlag, "Micro flag")
            _isbool(kineticsFlag, "Kinetics flag")
            _isbool(metaFlag, "Meta flag")
            if self.sets != {}:
                dSetup = self.sets[0]._dSetup
                if macroFlag:
                    attrs = attrs + dSetup.macro
                if microFlag:
                    attrs = attrs + dSetup.micro
                if kineticsFlag:
                    attrs = attrs + dSetup.kinetics
                if metaFlag:
                    attrs = attrs + dSetup.meta

        # Pandas table to store information of time, states, and branch values
        df = pd.DataFrame(
            columns=["history", "time"] + self.states._branchList + attrs)

        # histrorical branches
        hstList = [None]
        if not self.states._historyList == []:
            hstList = self.states._historyList

        # time points
        timeVals = [None]
        if not self.states.time == {}:
            timeVals = self.states.time['values']

        idx = 0
        # loop over all histories, times, and branches
        branches = list(self.states.branches.values())
        for history in hstList:
            for time in timeVals:
                for branch in itertools.product(*branches):
                    branchArr = np.array(branch, dtype=float)
                    # Obtain the state description
                    stateId = StateDescrp(history, time, branch)
                    ss = self.Get(branch=branchArr, time=time, history=history)
                    if ss is not None:
                        try:
                            vals = ss.GetValues(attrs)
                        except KeyError as detail:
                            raise KeyError("Error in {}\n {} \n"
                                           .format(stateId, detail))
                        vals = ss.GetValues(attrs)
                        df.loc[idx] = [history, time] + list(branchArr) +\
                            list(vals.values())
                        idx += 1

        self.pandasTable = df
        return df

    def Values(self, attrs=None, **kwargs):
        """Obtain the values of the specific attribute across different states

        The method obtains the values across all the provided states.
        Specific attributes can be selected.


        Parameters
        ----------
        attrs : string, list of strings
            name of the attributes to be included in the returned table.
            If None then all the attributes are returned
        kwargs : named arguments
            keys represent the data name and value represent the values.
            The filtering of data is performed according to kwargs.
            The use can filter according to a specific state, time, or history

        Returns
        -------
        pd : Pandas Object (dataframe)
            states and values across multiple states

        Raises
        ------
        TypeError
            If ``attrs`` is not str, list of str, or None.
        KeyError
            If the node (channel, layer) does not exist.
        AttributeError
            If ``pandasTable`` is not an attribute on the object.

        Examples
        --------
        >>> ms.Values(attrs=None, dens=600)
        ... history  time  ...                   beta                  decay
        ... 0    None   2.5  ...  [1, 1, 1, 1, 1, 1, 1]  [1, 1, 1, 1, 1, 1, 1]
        ... 1    None   2.5  ...  [2, 2, 2, 2, 2, 2, 2]  [1, 1, 1, 1, 1, 1, 1]

        >>> ms.Values(attrs=None, time=2.5, fuel=900, dens=600)
        ... history  time  ...                   beta                  decay
        ... 1    None   2.5  ...  [2, 2, 2, 2, 2, 2, 2]  [1, 1, 1, 1, 1, 1, 1]

        """

        if not hasattr(self, 'pandasTable'):
            raise AttributeError("No pandasTable attribute.\n Create using the"
                                 " DataTable method")
        # pandas table with all states and values
        pd = self.pandasTable

        # Column index for the starting position of values
        valsIdx0 = len(self.states._branchList) + 2  # 2 for (hist., time)
        idx = [i for i in range(valsIdx0)]  # indices to be included

        # Error checking for attributes
        if attrs is not None:
            if isinstance(attrs, str):
                attrs = [attrs]
            _islist(attrs, "Attributes")
            for attr in attrs:
                # attribute must exist in the table
                _inlist(attr, "Attribute", pd.columns.values)
                idx0 = pd.columns.get_loc(attr)
                if idx0 not in idx:  # only if the column has not been added
                    idx += [idx0]

        # loop over all the dependencies
        for col, value in kwargs.items():
            if not pd[col].isnull().any():  # check: column contains no None
                # select the values of interest in col.
                pd = pd[pd[col] == value]

        if attrs is not None:  # all attributes should be included
            pd = pd.iloc[:, idx]

        return pd


    def CheckFilters(self, branches=None, histories=None, times=None,
                     attrs=None):
        """Check that data use to filter the multiset container is valid

        The method allows to filter what data will be used to print results.
        The MultipleSets container may store many state points with multiple
        branches, histories, times, and atributes. This method allows to verify
        that specific points do exist on the MultipleSets container.


        Parameters
        ----------
        branches : dictionary
            keys represent the names of the branches and values correspond to
            the branches values.
        histories : list of strigs
            names of the histories. If not provided then 
        times : list or array of floats
            time points to be included

        Returns
        -------
        missingStates : list
            list of missing states.

        Returns
        -------
        missingStates : list
            list of missing states.
            
        Raises
        ------
        ValueError
            If ``branches`` is not defined pproperly.


        Examples
        --------
        >>> ms.CheckFilters(branches={'fuel': [1200 1500], 'mod': [600]},
                            histories=['nom'], times=[0.0, 5.0],
                            attrs=['inf_nsf', 'inf_abs', 'inf_flx'])
        ... [State(history='nom', time=0.0, branch=(600.0, 500.0, 600.0)),
        ... State(history='nom', time=0.0, branch=(600.0, 500.0, 500.0)),]
        """

        # create pandas table with all the states and the filtered attributes
        self.DataTable(attrs=attrs) 
       # collect existing and missing states on the container
        missingStates, existingStates = self._IsCompleteTable()

        # If no state points are provided then ALL the states defined
        # under the Perturbations container must exist
        if (branches and histories and times and attrs) is None:
            return missingStates
        
        if branches is None and not isinstance(branches, dict):
            raise ValueError(
                "branches variable must be a dict with keys as branch names "
                "and values as branches values, e.g., branches={'mod': [600]")
        if histories is None:
            histories = [None]
        if times is None:
            times = [None]
                
        branches = list(branches.values())
        
        states = []
        # loop over all histories, times, and branches
        for history in histories:
            for time in times:
                for branch in itertools.product(*branches):
                    stateId = StateDescrp(history, time, branch)
                    states.append(stateId)
        missingStates = []
        for state in states:
            if state not in existingStates:
                missingStates.append(state)
      
        return missingStates

    def _IsCompleteTable(self):
        """Check that Pandas table contains all states

        Check whether all states were provided by user. Return a dictionary
        with the missing states. This method can be executed only after the
        pandas tables are generated.

        Returns
        -------
        missingStates : dict
            states names as keys and their correponding values

        Raises
        ------
        AttributeError
            If ``pandasTable`` is not an attribute on the object.

        """

        # store all the missing & existing states
        missingStates = []
        existingStates = []

        if not hasattr(self, 'pandasTable'):
            raise AttributeError("No pandasTable attribute.\n Create using the"
                                 " DataTable method")

        # histrorical branches
        hstList = [None]
        if not self.states._historyList == []:
            hstList = self.states._historyList

        # time points
        timeVals = [None]
        if not self.states.time == {}:
            timeVals = self.states.time['values']

        # loop over all histories, times, and branches
        branches = list(self.states.branches.values())

        # Loop and check is states exist or not
        for history in hstList:
            for time in timeVals:
                for branch in itertools.product(*branches):
                    branchArr = np.array(branch, dtype=float)
                    stateId = StateDescrp(history, time, branch)
                    ss = self.Get(branch=branchArr, time=time, history=history)

                    # check is state exists
                    if ss is None:
                        missingStates.append(stateId)
                    else:
                        existingStates.append(stateId)

        return missingStates, existingStates
