# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 13:35:46 2022

@author: 17066
"""

import xsInterface.dataTypes as dt

def _isPropType(name):
    """Check whether name is a valid prop type in the xsInterface package"""
    if name not in dt._propTypes():
        raise AttributeError("{} is not a valid property in xs-interface"
                             .format(name))