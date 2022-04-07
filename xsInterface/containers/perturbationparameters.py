# -*- coding: utf-8 -*-
"""perturbationparameters.py

A container to hold all possible perturbation parameters.
These perturbation parameters are used when homogenized cross sections
are defined.

Created on Mon Apr 04 12:30:00 2022 @author: Dan Kotlyar
Last updated on Tue Apr 05 07:00:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu
"""

import numpy as np

from xsInterface.errors.checkerrors import _isint, _islist, _inlist,\
    _ispositive, _isequallength, _is1darray, _isstr, _isuniquelist,\
    _isnonNegativeArray, _issortedarray, _isarray

TIME_UNITS = ['MWd/kg', 'days', 'hours', 'minutes', 'seconds']


class Perturbations():
    """Stores the names and values of the perturbation parameters.

    The container uses the following structure:

                     Time-1      Time-i      Time-i
                    ________________________________
                    branch-1  |    ...   |  branch-1
    History1 -->    branch-2  |    ...   |  branch-2
                      ...     |          |    ...
                    branch-N  |    ...   |  branch-N


                           ........


                     Time-1      Time-i      Time-i
                    ________________________________
                    branch-1  |    ...   |  branch-1
    HistoryM -->    branch-2  |    ...   |  branch-2
                      ...     |          |    ...
                    branch-N  |    ...   |  branch-N

    Parameters
    ----------
    branchN : int
        number of perturbation states
    branches : list of strings
        user-defined names of all the states (e.g., fuelT, modDens)
    historyM : int
        number of histories / main branches
    histories : list of strings
        user-defined names of all the histories (e.g., nom, hist1, hist2)
    timeValues : array
        time/burnup values
    timeUnits : str
        indicate time or burnup by indicating the units

    Attributes
    ----------

    branches : dict
        contains bracnhes names and values (set to None)
    histories : dict
        contains histories names and values (set to None)
    time : dict
        contains values and units
    timeUnits : str
        indicate time or burnup by indicating the units
    branchN : int
        number of perturbation states
    historyM : int
        number of histories / main branches
    _branchList : list of strings
        user-defined names of all the states (e.g., fuelT, modDens)
    _historyList : list of strings
        user-defined names of all the histories (e.g., nom, hist1, hist2)

    Raises
    ------
    TypeError
        If ``branchN`` or ``histN`` is not an integer.
        If ``branches`` or ``histories`` is not a list of strings.
        If ``timeValues`` is not a 1-dim array.
    ValueError
        If ``branchN`` or ``histN`` is not positive.
        If the length of ``branches`` not equal to ``branchN`` or ``histories``
        not equal to ``histN``.
        If ``branches``,``histories`` or ``timeValues`` contain duplicates.
        If ``timeValues`` contains negative values or not sorted.
    KeyError
        If ``timeUnits`` is an undefined string.

    Examples
    --------
    >>> states = Perturbations(N=4, ["fuelT", "modDens", "coolDens", "time"])

    """

    def __init__(self, branchN, branches, histN=None, histories=None,
                 timeValues=None, timeUnits='MWd/kg'):
        """Assign parameters to describe the required/provided states"""

        # Define empty dictionaries to store branches, histories, and times
        self.branches = {}
        self.histories = {}
        self.time = {}
        self._branchList = []
        self._historyList = []

        # Check variables types
        _isint(branchN, "number of branches")
        _islist(branches, "branch names")
        _isuniquelist(branches, "branch names")

        # Check values for different variables
        _ispositive(branchN, "number of branches")
        _isequallength(branches, branchN, "branch names")

        # Assign attributes defined in the branches
        self._branchN = branchN
        self._branchList = branches
        for branch in branches:
            self.branches[branch] = None

        if histN is not None:
            # Check variables types
            _isint(histN, "number of histories")
            _islist(histories, "histories names")
            _isuniquelist(histories, "histories names")
            # Check values of variables
            _ispositive(histN, "number of histories")
            _isequallength(histories, histN, "histories names")
            # Assign histories
            self._histN = histN
            self._historyList = histories
            for history in histories:
                self.histories[history] = None

        if timeValues is not None:
            _isarray(timeValues, "Time/Burnup values")
            timeValues = np.array(timeValues, dtype=float)
            # check that time array is non-negative 1-dim array
            _is1darray(timeValues, "Time/Burnup values")
            _isnonNegativeArray(timeValues, "Time/Burnup values")
            _issortedarray(timeValues, "Time/Burnup values")
            _isuniquelist(timeValues, "Time/Burnup values")
            # Check variables types
            _inlist(timeUnits, "Time/Burnup units", TIME_UNITS)
            # Assign histories
            self.time["values"] = timeValues
            self.time["units"] = timeUnits
            self.time["npoints"] = len(timeValues)

    def AddBranches(self, **kwargs):
        """Add the branch perturbation values for a specific state

        Parameters
        ----------
        kwargs : named arguments
            keys represent the state name and value represent the state values.

        Raises
        ------
        TypeError
            If ``name`` is not a string.
        KeyError
            If ``name`` is not an allowed branch name

        Examples
        --------
        >>> states.AddBranches(fuel=[600, 900, 1200, 1500],
        >>>                    dens=[600, 700, 800],
        >>>                    cool=[500, 600])

        """

        for name, value in kwargs.items():
            # Check variable type
            _isstr(name, "keyword state name")

            # check that this attribute exists in the list of states
            _inlist(name, "keyword state name", self._branchList)

            # check that attributes are not already defined
            if self.branches[name] is not None:
                raise ValueError("Branch name <{}> is already populated"
                                 .format(name))
            else:
                _isarray(value, "Branch <{}> values".format(name))
                vals = np.array(value, dtype=float)
                _is1darray(vals, "Branch <{}> values".format(name))
                self.branches[name] = vals

    def AddHistories(self, **kwargs):
        """Add the different main histories that will hold all the branches

        Parameters
        ----------
        kwargs : named arguments
            keys represent the history name and value is a set that follows the
            order provided within the ``states`` when reseting the container.

        Raises
        ------
        TypeError
            If ``name`` is not a string.
        ValueError
            If kwargs values are not alligned with the length of the number of
            branches.
        KeyError
            If ``name`` is not an allowed branch name

        Examples
        --------
        >>> states.AddBranches(fuel=[600, 900, 1200, 1500],
        >>>                    dens=[600, 700, 800],
        >>>                    cool=[500, 600])

        """

        for name, value in kwargs.items():
            # Check variable type
            _isstr(name, "keyword state name")

            # check that this attribute exists in the list of states
            _inlist(name, "History keyword", self._historyList)

            # check that attributes are not already defined
            if self.histories[name] is not None:
                raise ValueError("History <{}> is already populated"
                                 .format(name))
            else:
                _isarray(value, "History <{}> values".format(name))
                vals = np.array(value, dtype=float)
                _is1darray(vals, "History values for <{}>".format(name))
                _isequallength(vals, self._branchN, "History values for "
                               "<{}>".format(name))

                self.histories[name] = vals

    def _proofTest(self):
        """Check that all the data was inputted"""
        if self.branches != {}:
            for key, value in self.branches.items():
                if value is None:
                    raise ValueError("No data is provided for branch <{}>."
                                     .format(key))

        if self.histories != {}:
            for key, value in self.histories.items():
                if value is None:
                    raise ValueError("No data is provided for history <{}>."
                                     .format(key))

        if self.time != {}:
            if "values" not in self.time or "units" not in self.time:
                raise ValueError("Time values and units must be provided")
