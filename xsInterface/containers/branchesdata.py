# -*- coding: utf-8 -*-
"""branchesdata

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
    
    def condense(self, listAttributes, eneCutoffs):
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


class BranchoffSets:
    """A container to store sets for different operational conditions

    Methods
    -------
    addset : add new BasicDataSet
    getset : obtain the BasicDataSet object
    getvalues : obtain values of a specific attribute

    """

    def __init__(self, ndep, states, depInterp):
        # Init to empty dictionary
        self._datasets = {}
        self._ndep = ndep  # integer to the number of total dependencies
        # tuple of numerical values with which the main branch was created
        self.states = states  # all the possible states ; each state will also
        # have an index
        # depInterp - a list of pre-scribed interpolation technique for each
        # dependnecy (linear, root square)

    def addset(self, *states, **BasicDataSet):
        """Add a new set

        COMPLETE

        Parameters
        ----------
        states : contains all the states (T, density, boron, enrichment, ...)
        BasicDataSet : corresponding object for each


        """
        # self._datasets[state] = BasicDataSet
        pass


    def getset(self, state):
        """Obtains the NodeResults object for a specific node

        Parameters
        ----------
        channel : string
            identifier of the channel
        layer : int
            index of the axial layer

        Returns
        -------
        NodeResults object

        Raises
        ------
        TypeError
            If the ``channel`` or ``layer``are not of the correct variable type
        KeyError
            If the node (channel, layer) does not exist.

        """
        # return self._datasets[state]
        # enable indexing as well
        pass

    def __getitem__(self, pos):
        return self._datasets[pos]

    def getvalues(self, attributes, interpFlag):
        """Obtain values of a specific attribute over different states"""

        # return vals
        pass
        # interpolation flag to indicate whether interpolation should be
        # performed
