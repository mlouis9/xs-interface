# -*- coding: utf-8 -*-
"""singleset

Container to collect, store, and process multi-group cross-sections set.


Created on Tue Feb 01 13:30:00 2022 @author: Dan Kotlyar
Last updated on Tue Feb 01 13:30:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu
"""


class SingleSet:
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

        self._dataLabel = dataLabel  # could also be defined in XsSets
        self._xsLabel = xsLabel
        self._ngroups = ngroups
        # dataLabel = {"keff": "description to throw errors", ...}
        # xsLabel = {"abs": "Abso cross section"}
        
    def dataIn(self, dataType, **kwargs):
        """Feed in cross sections"""
        # dataType will allow us to control whether this a matrix, float,
        # vector
        # **kwargs:
        # name of the cross sections and their correponsing values
        # 
        # we can write this method in one go or multiple times depending on
        # the material being fed to the container.
        pass
    
    def condense(self, listAttributes, eneCutoffs, variable, flux="flux"):
        """Energy condensation"""
        # Condensation will be performed only for the attributes of interest
        # energy cutoffs or indices must be provided
        # The method will return a NEW object, which could be stored indep.
        # The condensed results can also be stored on a muted dictionary
        # in the container
        pass
    
    def getvalues(self, *attributes):
        """obtain the data of specific attributes"""
        # can be return as a separate results container.
        pass

    def printtemplt(self, whatxs, howprint, setrules):
        """print according to a user provided template"""
        pass
