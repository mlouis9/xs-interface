# -*- coding: utf-8 -*-
"""historysets

Container to collect, store, and process multi-group cross-sections set.


Created on Tue Feb 01 13:30:00 2022 @author: Dan Kotlyar
Last updated on Tue Feb 01 13:30:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu
"""


class HistorySets:
    """Container that stores multiple branchesdata

    Parameters
    ----------
    The history 


    Attributes
    ----------
    COMPLETE

    """

    def __init__(self, *historiesCond):
        """Assign parameters that describe the flow"""

        self._historysets = {}
        # keys will be histories nominal conditions
        # values will be the branch sets
        # histories will be assigned with indices
        
    def addhistory(self, state, histObject):
        """Feed in cross sections"""
        # self._historysets[state] = histObject
        pass
    
    def gethistory(self):
        """bla bla bla"""
        pass
    
    def weight(self, state, method):
        """Create a weighted branch based on the closest data"""
        pass