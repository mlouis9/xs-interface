# -*- coding: utf-8 -*-
"""singleset

Container to collect, store, and process multi-group cross-sections set.


Created on Tue Feb 01 13:30:00 2022 @author: Dan Kotlyar
Last updated on Tue Feb 01 13:30:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu
"""

import numpy as np
import copy

class SingleSet():
    """Container that stores the most basic data set

    Parameters
    ----------
    dataLabel : dict
        Labels that describe the type of data inputted to the set.
        Keys describe the name of the stored attributed and values the
        corresponding description used for error tracking.
    xsLabel : dict
        specific label description only for xs.
    ngroups : int
        Number of energy groups. 


    Attributes
    ----------
    COMPLETE

    """

    def __init__(self, dataLabel, xsLabel, ngroups):
        """Assign parameters that describe the flow"""

        self._dataLabel = dataLabel
        self._xsLabel = xsLabel
        self._ngroups = ngroups
        self._attr = {}
        
        # dataLabel = {"keff": "description to throw errors", ...}
        # xsLabel = {"abs": "Abso cross section"}
    
    def addLabel(self, mode="xsLabel", **kwargs):
        """Set or add a new label to data"""
        
        if mode == "xsLabel":
            for key,value in kwargs.items():
                self._xsLabel[key] = value
        elif mode == "dataLabel":
            for key,value in kwargs.items():
                self._dataLabel[key] = value
    
    def add(self, dataType, **kwargs):
        """Feed in cross sections"""
        # dataType will allow us to control whether this a matrix, float,
        # vector
        # **kwargs:
        # name of the cross sections and their correponsing values
        # 
        # we can write this method in one go or multiple times depending on
        # the material being fed to the container.
        
        for key,value in kwargs.items():
            if isinstance(value,dataType):
                self._attr[key] = value
            else:
                # Pass error if invalid dataType?
                pass
    
    def get(self, *attributes):
        """obtain the data of specific attributes"""
        # can be return as a separate results container.
        
        out = {}
        for attribute in attributes:
            out[attribute] = copy.deepcopy(self._attr[attribute])
        
        return out
    
    def condense(self, *attributes, flux="flux", eneCutoffs=None):
        """Energy condensation"""
        # how to incorporate eneCutoffs?
        # Error check that data is an np.array()
        
        # ene = self["ene"]
        # mask = ene == eneCutoffs
        
        # Condense each value in attributes over energy range
        for attribute in attributes:
            attr = self._attr[attribute]
            phi  = self._attr[flux]
            self._attr[attribute] = np.sum(attr*phi)/np.sum(phi)
        
        # condnse flux over energy range
        self._attr[flux] = np.sum(phi)
        
    def printData(self, whatxs, howprint, setrules):
        """print according to a user provided template"""
        pass
