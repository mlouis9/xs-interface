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
    _ispositive, _isstr, _isuniquelist, _isarray,\
    _is1darray, _isequallength, _isBoundArray
from xsInterface.containers.container_header import DATA_TYPES


class DataSettings():
    """
    Stores the names and data that are expected to be stored on containers

    Parameters
    -----------
    NG : int
        number of energy groups for multi-group parameters
    DN : int
        Delayed neutron groups for kinetic parameters
    macro : boolean
        indicate whether macro data is expected to be provided
    micro : boolean
        indicate whether micro data is expected to be provided
    kinetics : boolean
        indicate whether kinetic data is expected to be provided
    meta : boolean
        indicate whether meta data is expected to be provided
    isotopes : array
        ZZAAA0/1 for all the isotopes to be provided
    nuclides : str
        name of the variable that will store nuclides densities in #/b/cm

    Attributes
    -----------
    NG : int
        number of energy groups for multi-group parameters
    DN : int
        delayed neutron groups for kinetic parameters
    dataFlags : dict
        boolean flags to indicate the data types that are provided
    macro : dict
        contains all the macro attributes (e.g., ``abs``)
    micro : boolean
        contains all the micro attributes for all the isotopes (e.g., ``fiss``)
    kinetics : boolean
        contains all the kinetic attributes (e.g., ``beta``)
    meta : boolean
        contains all the metadata attributes (e.g., ``time``)


    Methods
    --------
    AddData(dataType, attributes, attrDims=None):
        Add relevant macroscopic/microscopic/meta data

    Raises
    -------
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
    ---------
    >>> rc = DataSettings(NG=2, DN=7, macro=True, micro=False, kinetics=True,
    >>>                   meta=False, isotopes=None, nuclides=None)
    """

    def __init__(self, NG, DN, macro=True, micro=False, kinetics=False,
                 meta=False, isotopes=None, nuclides=None):
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
                _isstr(nuclides, "Nuclides variable name")
            else:
                raise ValueError("<isotopes> list/array must be provided")
                
        # Reset variables
        self.ng = NG  # number of energy groups
        self.dn = DN  # number of delayed neutron groups
        self.isotopes = isotopes
        self.dataFlags = {"macro": macro, "micro": micro,
                          "kinetics": kinetics, "meta": meta}
        self.macro = []
        self.micro = []
        self.kinetics = []
        self.meta = []
        self.nuclides = nuclides

    def AddData(self, dataType, attributes):
        """Add relevant macroscopic/microscopic/meta data

        Parameters
        ----------
        dataType : ["macro", "micro", "kinetics", "meta"]
            type of data
        attributes : list of strings
            user-defined names for the provided data type (e.g., ``abs``)

        Examples
        --------
        >>> rc.AddData("macro", ["abs", "nsf", "sct"], "array")
        >>> rc.AddData("kinetics", ["beta", "decay"], "array")

        """
        # Error checking
        _isstr(dataType, "data types")
        _inlist(dataType, "data types", DATA_TYPES)
        if not self.dataFlags[dataType]:
            raise ValueError("Data type <{}> was disabled when DataSettings "
                             "object was created".format(dataType))
        _islist(attributes, "names of "+dataType+" attributes")
        _isuniquelist(attributes, "attribute names in ")

        # check if data is already populated
        data0 = getattr(self, dataType)
        if data0 == []:  # data is new
            # define the specific dictionary for the selected data type
            attrList = attributes
        else:  # data already exists
            attr0 = data0
            # create a new/appended list of attributes
            attr1 = attr0 + attributes
            _isuniquelist(attr1, "attribute names in ")
            attrList = attr1

        # set a muted attribute with the settings for the selected data type
        setattr(self, dataType, attrList)

    def _proofTest(self):
        """Check that data was inputted"""
        if self.dataFlags["macro"] and self.macro == []:
            raise ValueError("macro data is expected to be provided.")
        if self.dataFlags["micro"] and self.micro == []:
            raise ValueError("micro data is expected to be provided.")
        if self.dataFlags["kinetics"] and self.kinetics == []:
            raise ValueError("kinetics data is expected to be provided.")
        if self.dataFlags["meta"] and self.meta == []:
            raise ValueError("meta data is expected to be provided.")
