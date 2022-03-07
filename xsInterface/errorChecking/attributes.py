# -*- coding: utf-8 -*-
"""
Created on Sat Mar  5 00:19:04 2022

@author: 17066
"""

import xsInterface
import xsInterface.errorChecking as err
import numpy as np

def _packageAttr(obj,**kwargs):
    switch = {xsInterface.Tally()     : _case1(**kwargs),
              xsInterface.Prop()      : _case2(**kwargs),
              xsInterface.UserLabel() : _case3(**kwargs),
              xsInterface.SingleSet() : _case4(**kwargs)}
    return switch[type(obj)]

def _case1(**kwargs):
    # Initialize objData
    objData = err.ObjData()
    
    # extract kwargs data
    for key,value in kwargs.items():
        if key == "tallyEdges":
            tallyEdges = value
            ng = len(tallyEdges)
    
    attrNames = ["name", "dim", "type", "tallyEdges", "value"]
    attrTypes = [ [str,type(None)], 
                  [int,type(None)], 
                  [str,type(None)], 
                  [np.array(),type(None)],
                  [np.array(),type(None)] ]
    attrSizes = [(1),(1),(1),(ng),(1)]
    
    for ndx,attrName in attrNames:
        tmpData = err.AttrData()
        tmpData.add(attrName=attrName)
        tmpData.add(attrType=attrTypes[ndx])
        tmpData.add(attrSize=attrSizes[ndx])
        objData.add(tmpData)

def _case2():
    # Case2 needs to be defined
    pass

def _case3():
    # Case3 needs to be defined
    pass

def _case4():
    # Case4 needs to be defined
    pass