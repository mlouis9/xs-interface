# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 00:05:30 2022

@author: 17066
"""

def AttrData():
    """Object that details error checking information about an attrobute in an
    object type in the xs-interface package
    
    Attributes
    ----------
    attrNames : str
        name of the attribute
    attrTypes : list of types
        tells which types are acceptable for attrtbute
    attrSize : tuple
        tells what size is acceptable for attribute 
    """
    
    def __init__(self):
        """Initialize attrData"""
        attrs = ["attrNames","attrTypes","attrSize"]
        for attr in attrs:
            self.add(attr=None)
    
    def add(self,**kwargs):
        """set attribute in AttrData"""
        for key,value in kwargs.itmes():
            setattr(self,key,value)
    
def ObjData(dict):
    """Object that details error checking information about all attributes for
    an object type in the xs-interface package  
    """
    
    def __init__(self):
        """Initialize ObjData"""
    
    def add(self,*args):
        for attrData in args:
            self[attrData.attrName] = attrData