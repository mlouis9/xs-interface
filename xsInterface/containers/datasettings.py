# -*- coding: utf-8 -*-
"""datasettings.py

The user needs to define the required data to be stored on the containers.
This container stores all the attributes and settings for the required data.


Created on Sat Mar 19 18:30:00 2022 @author: Dan Kotlyar and Bailey Painter
Last updated on Tue Apr 01 11:30:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu
"""

import numpy as np

from xsInterface.errors.checkerrors import _isint, _islist, _isbool, _inlist,\
    _ispositive, _isstr

FRMT_OPTS = ["array", "dict"]
DATA_TYPES = ["macro", "micro", "kinetics", "meta"]


class DataSettings():
    """Stores the names and data that are expected to be stored on containers

    Parameters
    ----------
    NG : int
        number of energy groups for multi-group parameters
    DN : int
        Delayed neutron groups for kinetic parameters
    macro : boolean
        indicate whether macro data is expepcted to be provided
    micro : boolean
        indicate whether micro data is expepcted to be provided
    kinetics : boolean
        indicate whether kinetic data is expepcted to be provided
    meta : boolean
        indicate whether meta data is expepcted to be provided
    isotopes : array
        ZZAAA0/1 for all the isotopes to be provided

    Attributes
    ----------
    NG : int
        number of energy groups for multi-group parameters
    DN : int
        delayed neutron groups for kinetic parameters
    _dataFlags : dict
        boolean flags to indicate the data types that are provided
    _macro : dict
        contains all the macro attributes (e.g., ``abs``)
    _micro : boolean
        contains all the micro attributes for all the isotopes (e.g., ``fiss``)
    _kinetics : boolean
        contains all the kinetic attributes (e.g., ``beta``)
    _meta : boolean
        contains all the metadata attributes (e.g., ``time``)

    Raises
    ------
    TypeError
        If any of the parameters, e.g., ``NG``, ``DN`` are not integers.
        If any of the ``macro``, ``micro``, ``kinetics``, ``meta``
        are not booleans.
    ValueError
        If ``NG`` is below one.
        If ``DN`` is below one.
        If ``isotopes`` list is not provided but ``micro`` data is expected.
    KeyError
        If ``dataType`` or ``frmt`` do not exist in DATA_TYPES or FRMT_OPTS.

    Examples
    --------
    >>> rc = DataSettings(NG=2, DN=7, macro=True, micro=False, kinetics=True,
    >>>                   meta=False, isotopes=None)
    >>> rc.AddData("macro", ["abs", "nsf", "sct"], "array")
    >>> rc.AddData("kinetics", ["beta", "decay"], "array")

    """

    def __init__(self, NG, DN, macro=True, micro=False, kinetics=False,
                 meta=False, isotopes=None):
        """Assign parameters that describe the required data to be provided"""

        # Check variables types
        _isint(NG, "number of energy groups")
        _isint(DN, "number of delayed neutron groups")
        _isbool(macro, "macro data")
        _isbool(micro, "micro data")
        _isbool(kinetics, "kinetics data")
        _isbool(meta, "meta data")

        # Check values/entries for different variables
        _ispositive(NG, "number of energy groups")
        _ispositive(DN, "number of delayed neutron groups")
        if micro:
            if isotopes is not None:
                isotopes = np.array(isotopes, dtype=int)
            else:
                raise ValueError("<isotopes> list/array must be provided")

        # Reset variables
        self.ng = NG  # number of energy groups
        self.dn = DN  # number of delayed neutron groups
        self.isotopes = isotopes
        self._dataFlags = {"macro": macro, "micro": micro,
                           "kinetics": kinetics, "meta": meta}
        self._macro = {}
        self._micro = {}
        self._kinetics = {}
        self._meta = {}

    def AddData(self, dataType, attributes, frmt):
        """Add relevant macroscopic/microscopic/meta data

        Parameters
        ----------
        dataType : ["macro", "micro", "kinetics", "meta"]
            type of data
        attributes : list of strings
            user-defined names for the provided data type (e.g., ``abs``)
        frmt : string {"array", "dict"}
            method to provide data. ``array`` denotes that each parameters is
            provided individually with a given array of multi-group data.
            ``dict`` indicates that the data is provided within a dictionary,
            where keys indicate name of parameters and values represent
            the multi-group
            values.

        """
        # Error checking
        _isstr(dataType, "data types")
        _islist(attributes, "names of "+dataType+" attributes")
        _inlist(dataType, "data types", DATA_TYPES)
        _inlist(frmt, dataType+" format", FRMT_OPTS)

        # define the specific dictionary for the selected data type
        dataDict = {"attributes": attributes,
                    "format": frmt}

        # set a muted attribute with the settings for the selected data type
        setattr(self, "_"+dataType, dataDict)

    def _proofTest(self):
        """Check that data was inputted"""
        if self._dataFlags["macro"] and self._macro == {}:
            raise ValueError("macro data is expected to be provided.")
        if self._dataFlags["micro"] and self._micro == {}:
            raise ValueError("micro data is expected to be provided.")
        if self._dataFlags["kinetics"] and self._kinetics == {}:
            raise ValueError("kinetics data is expected to be provided.")
        if self._dataFlags["meta"] and self._meta == {}:
            raise ValueError("meta data is expected to be provided.")
