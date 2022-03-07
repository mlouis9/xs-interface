# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 13:01:01 2022

@author: 17066
"""

def _checkAttr(obj,key,value):
    """Checks whether an attribute will be consistent with the object it is
    being defined in"""
    # extract object data
    objData = obj._objData
    
    # Check whether attribute name is valid, then extract relevant data to 
    # object
    _checkName(key,objData)
    attrData = objData[key]
    
    # Perform check on the aattribute's value
    _checkType(value,attrData)
    _checkSize(value,attrData)

def _checkObj(obj):
    """Performs all error checking on an object based on the data stored in
    objData"""
    # extract object data
    objData = obj._objData
    
    # Perform an error check for all attributes in the object
    for key,value in objData.items():
        # Check whether attribute name is valid, then extract relevant data to 
        # object
        _checkName(key,objData)
        attrData = objData[key]
        
        # Perform check on the aattribute's value
        _checkType(value,attrData)
        _checkSize(value,attrData)

def _checkName(key,attrData):
    """Tests whether specified attribute is valid in the object"""
    pass

def _checkSize():
    """Tests whether specifed attribute's vlaue is correct size in the object"""
    pass

def _checkType():
    """Tests whether specifed attribute's type is valid"""
    pass