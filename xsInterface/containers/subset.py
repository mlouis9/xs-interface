# -*- coding: utf-8 -*-
"""
Created on Fri Mar  4 12:57:03 2022

@author: 17066
"""

import numpy as np
import xsInterface.errorChecking as err
        
def Tally():
    """Object that stores data related to a specific tally in a SingleSet
    object
    
    Attributes
    ----------
    _objData : dict
        tells valid attributes and their valid types
    name : str
        gives the name of the tally
    dim : int
        tells whether the tally has one or two dimensions
    type : str
        tells whether the tally is a cross section ('xs'), reaction rate 
        ('rr'), or flux ('flux')
    tallyEdges : ndarray
        tells what binedges were used to calculated the tallies
    value : ndarray
        tells the tally value for the object
        
    """
    
    def __init__(self,dim,tallyEdges):
        """initialize TallyObject"""
        # initialize object data
        self._objData = err._objData(self,tallyEdges=tallyEdges)
        
        # Preallocate attributes
        for attr in self._attrDict:
            self.add(attr=None)
    
    def add(self,**kwargs):
        """specify one or more attributes in the TallyObject"""
        for key,value in kwargs.items():
            err.checkAttr(self,key,value)
            setattr(self,key,value)
    
    def condense(self,flux0,flux1,condenseMap):
        """condense tally results in value based on flux0 and flux1"""
        if self.dim == 1:
            self.value = _condense1d(self,flux0,flux1,condenseMap)
        elif self.dim == 2: 
            self.value = _condense2d(self,flux0,flux1,condenseMap)
    
def Prop():
    """Object that stores data related to a specific prop
    
    Attributes
    ----------
    _objData : dict
        tells valid attributes and their valid types
    name : str
        gives the name of the tally
    value : ndarray
        gives the value of the property
        
    """
    
    def __init__(self):
        """initialize TallyObject"""
        # Retrieve package data
        self._objData = err._packageAttr(self)
        
        # Preallocate attributes
        for attr in self._attrDict:
            self.add(attr=None)
    
    def add(self,**kwargs):
        """specify one or more attributes in the TallyObject"""
        for key,value in kwargs.items():
            err.checkAttr(self,key,value)
            setattr(self,key,value)

###############################################################################
#### Helper Functions #########################################################
###############################################################################

def _condense1d(self,tallyName,flux1,condenseMap):
    """condenses a 1D nonflux tally based on the initial and final flux"""
    fluxName = self._fluxName
    flux0 = self._tallies[fluxName]
    tally = self._tallies[tallyName]
    #### tallyDim = self._tallyDims[tallyName]
    
    # This formula is incomplete and needs to be properly implemented
    return np.sum(tally*flux0)/flux1

def _condense2d(self,tallyName,flux1,condenseMap):
    """condensess a 2d nonflux tally based on the initial and final flux"""
    ### fluxName = self._fluxName
    ### flux0 = self._tallies[fluxName]
    tally = self._tallies[tallyName]
    ### tallyDim = self._tallyDims[tallyName]
    
    # This formula is incomplete and needs to be properly implemented
    return np.sum(np.sum(tally))