# -*- coding: utf-8 -*-
"""singleset

Container to collect, store, and process multi-group cross-sections set.


Created on Tue Feb 01 13:30:00 2022 @author: Dan Kotlyar
Last updated on Tue Feb 01 13:30:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu
"""

import numpy as np
import copy
import xsInterface
import xsInterface.errorChecking as err

class SingleSet():
    """Container that stores the most basic data set

    Parameters
    ----------
    userLabel : dict
        Assigns a label to data and tells singleSet how to error check that 
        data
    
    Attributes
    ----------
    COMPLETE

    """
    
    def __init__(self,tallyEdges):
        """Assign parameters that describe the flow"""
        # Set SingleSet properties using the user defined label
        self.tallyEdges = tallyEdges
        self.ng         = len(tallyEdges) + 1
        
        # Initialize muted dictionaries
        self._tallies = {}
        self._props = {}
    
    def add(self, *args):
        """Add data to SingleSet obect"""
        # *args:
        # must either be a Tally or Prop object
        
        for obj in args:
            if type(obj) == xsInterface.Tally():
                err.checkObj(obj)
                self._tallies[obj.name] = obj
            
            elif type(obj) == xsInterface.Prop():
                err.checkObj(obj)
                self._props[obj.name] = obj
            
            else:
                # Raise error
                pass
    
    def get(self, *attributes):
        """obtain the data of specific attributes"""
        # can be return as a separate results container.
        pass
    
    def condense(self, tallyEdges=None, selfCondense=False):
        """Energy condensation"""
        # Decide whether condense data or make a copy
        if selfCondense==False:
            out = copy.deepcopy(self)
        else:
            out = self
        
        # Identify initial and final tally edges
        tallyEdges0 = out.tallyEdges
        tallyEdges1 = tallyEdges
        
        # Condense flux first to create condenseMap for xs condensation
        for tallyName,tally in self._tallies.items():
            if tally.type == 'flux':
                flux0 = copy.deepcopy(tally)
                flux1 = tally
                flux1.condense(tallyEdges0,tallyEdges1)
                out.ng = flux1.ng
        
        # Condense each value in attributes over the specified cutoff range
        for tallyName,tally in self._tallies.items():
            tally.condense(tallyEdges0,tallyEdges1,flux0,flux1)
            err.checkObj(tally)
            out.add(tally)
        
        if selfCondense==False:
            return out
    
    def printData(self, whatxs, howprint, setrules):
        """print according to a user provided template"""
        pass