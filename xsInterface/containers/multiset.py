# -*- coding: utf-8 -*-
"""branchesdata

Container to collect, store, and process multi-group cross-sections set.


Created on Tue Feb 01 13:30:00 2022 @author: Dan Kotlyar
Last updated on Tue Feb 01 13:30:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu
"""

import pandas

class MultiSets(pandas.DataFrame):
    """A container to store sets for different operational conditions

    Methods
    -------
    addset : add new BasicDataSet
    getset : obtain the BasicDataSet object
    getvalues : obtain values of a specific attribute

    """

    def __init__(self, ndep, states, legend, depInterp):
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


    def intrpset(self, layer, interpFlag):
        pass

    def getset(self, state, interpFlag):
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
    
    def add(self,**kwargs):
        """adds data to all Single Sets contained within the MutiSet

        Parameters
        ----------

        Returns
        -------

        Raises
        ------

        """
        if isinstance(obj,xsInterface.MultiSet):
            """"perform operation for each child in obj"""
            for child in obj:
                xsInterface.add(obj,**kwargs)
        
        elif isinstance(obj,xsInterface.SingleSet):
            """perform operation on a SingleSet object"""
            obj.add(**kwargs)
        
        else:
            """Raise errors"""
            pass
            
    if isinstance(obj,xsInterface.MultiSet):
        """"perform operation for each child in obj"""
        for child in obj:
            xsInterface.add(obj,**kwargs)
    
    elif isinstance(obj,xsInterface.SingleSet):
        """perform operation on a SingleSet object"""
        obj.add(**kwargs)
    
    else:
        """Raise errors"""
        pass
    
    def __getitem__(self, pos):
        return self._datasets[pos]

    def getvalues(self, attributes, state, interpFlag=True):
        """Obtain values of a specific attribute over different states"""

        # return vals
        pass
        # interpolation flag to indicate whether interpolation should be
        # performed