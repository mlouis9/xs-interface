# -*- coding: utf-8 -*-
"""branchesdata

Container to collect, store, and process multi-group cross-sections set.


Created on Tue Feb 01 13:30:00 2022 @author: Dan Kotlyar
Last updated on Tue Feb 01 13:30:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu
"""

import pandas as pd
import xsInterface.initialization as pre

class MultiSet():
    """A container to store sets for different operational conditions

    Methods
    -------
    add : add new SingleSet object
    get : retrieve data from the MultiSet object
    getvalues : obtain values of a specific attribute

    """

    def __init__(self, tallyRules, propRules, tallyEdges, indexes):
        # Init to empty dictionary
        self._objData = pre.getObjData
        self.tallies = {}
        self.indexes = indexes
        self.tallyEdges = tallyEdges
        
        # create the isFilled matrix
        indexVec = list(np.zeros(indexes.numDeps+value.dim))
        self.isFilled = np.full(indexVec, False)
        
        # Preallocate tallies 
        for key,value in tallyRules.items():
            # Create an index for each dependency + dimension of tally
            indexVec = list(np.zeros(indexes.numDeps+value.dim))
            self.tallies[key] = np.empty(indexVec)
        
        # Preallocate props
        for key,value in propRules.items():
            # Create an index for each dependency + dimension of prop (1)
            indexVec = list(np.zeros(indexes.numDeps+1))
            self.tallies[key] = np.empty(indexVec)

    def add(self, *singleSets):
        """Add a new set

        COMPLETE

        Parameters
        ----------

        """
        
        for singleSet in SingleSets:
            
            for key,value in singleSet.indexes.items():
                
                # Preallocate spaces and edit indexes object for new index
                # values
                multiValues = self.indexes[key]
                if value not in multiValues:
                    # Add new index value to the indexes object
                    ndx = multiValues.searchsorted(value)
                    np.insert(multiValues,ndx,value)
                    tallies = self.tallies                
                    
                    # preallocate space for tallies
                    for tally in tallies:
                        _preallocate(self,obj)
                    
                    # preallocate space for objects
                    for prop in props: 
                        _preallocate(self,obj)
                    
                    # preallocate space in isFilled matrix
                    _preallocate(self,self.isFilled)
                
                # Add the SingleSet values to the MultiSet
                for tally in tallies:
                    _addVal(self,obj)
                
                for prop in props:
                    _addVal(self,obj)
                
                self.isFilled(fillindex)

    def insert(**kwargs):
        """Inserts an undefined point in a MultiSet via interpolation"""
        for key,value in kwargs.items():
            self.interpolate()
    
    def node2ndx(**kwargs):
        """finds the index corresponding to the node values"""
        
        out = []
        for key,value in kwargs.items()
            loc = self.nodeloc[key]
            ndx = np.where(self.nodes[key]==value)
            out.append((loc,ndx))

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

###############################################################################
#### Helper Functions #########################################################
###############################################################################

def _preallocate(self,obj):
    # indexVec 1 describes the size and shape of the
    # preallocation matrix. indexVec 2 describes the position
    # the reallocation matrix should 
    indexPoint = indexes.points[key]
    indexVec0 = indexes.vec
    indexVec1 = copy.deepcopy(indexVec0)
    indexVec2 = copy.deepcopy(indexVec0)
    
    # append dimensions describing group structure
    for i in range(tally.dim)+indexes.numPoints:
        indexVec1.append(self.ng)
        indexVec2.append(self.ng)
    
    # adjust values at target point
    indexVec1[indexPoint] = 1
    indexVec2[indexPoint] = ndx
    
    # create the preallocation matrix for the tally
    preMat = np.empty(indexVec1)
    preMat[:] = NaN
    
    # insert preallocation matrix
    np.insert(tally,indexVec2,preMat,axis=indexPoints)