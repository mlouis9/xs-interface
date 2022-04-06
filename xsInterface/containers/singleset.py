# -*- coding: utf-8 -*-
"""singleset

Container to collect, store, and process data including:
    - multi-group macroscopic cross sections
    - multi-group microscopic cross sections
    - kinetic parameters
    - metadata


Created on Tue Apr 05 22:30:00 2022 @author: Dan Kotlyar
Last updated on Wed Apr 06 12:30:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu
"""

import numpy as np


class SingleSet():
    """Container that stores the most basic data set

    Parameters
    ----------
    xxxx : dict
        complete

    Attributes
    ----------
    COMPLETE

    """

    def __init__(self, settings, perturbations,
                 spectrum=None, energyStruct=None):
        """Assign parameters that describe the flow"""
        # Set SingleSet properties using the input rules object
        pass
        # make sure that settings are properly defined using the proofTest
        
    def add(self, **kwargs):
        """add data and populate attributes"""
        pass
    
    def get(self, **kwargs):
        """get data"""
        pass
    
    def condense(self, condEnergy, parameters):
        """energy condensation"""
        pass
    
    
    
    