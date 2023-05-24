# -*- coding: utf-8 -*-
"""lstreader.py

Read the nodal fluxes and k-eff from the _lst file created by DYN3D.


Created on Wed May 24 10:30:00 2023 @author: Dan Kotlyar
Last updated on Wed May 24 12:00:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
_getnums - 05/24/20223 - DK

"""

import re
import numpy as np
match_number = re.compile('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')



###############################################################################

def lstRead(lstfile):
    """Reads keff and fluxes results from lst file"""
    
    
    with open(lstfile, 'r') as fObject:
        dataFile = fObject.readlines()
      
    # reset values    
    ng = None
    nch = None
    nz = None
    keff = None
    fluxes = None
    
    flagFluxes = False  # flag to indicate if the NODAL FLUXES str is found
    
    nlines = len(dataFile)   # number of lines within the lst file
    
    for idxline, tline in enumerate(dataFile):
        # get settings
        if ng is None and "NUMBER OF NEUTRON ENERGY GROUPS" in tline:
            ng = _getnums(tline)[-1]
        elif nch is None and "NUMBER OF COOLANT CHANNELS" in tline:
            nch = _getnums(tline)[-1]
        elif nz is None and "AXIAL NODES IN CORE" in tline:
            nz = _getnums(tline)[-1]
   
        # Preallocate flux dictionary (only one time)
        if fluxes is None and (ng and nz and nch) is not None: 
            fluxes = np.zeros((nch,nz,ng))


        if  keff is None and "keff =" in tline:  # obtain k-eff
            keff = _getnums(tline,integer=False)[0]    

        if  "DISTRIBUTION OF NODAL FLUXES IN 1/(CM**2*S)" in tline:
            flagFluxes = True
    
        # Axial gate
        if flagFluxes:
            if "CAS-NR" in tline:
                chs = np.array(_getnums(tline))-1
                fluxes, idxline =\
                    _getFluxes(dataFile, fluxes, chs, ng, idxline, nlines)
            
            elif "NORMALIZED POWER DISTRIBUTION" in tline:
                flagFluxes = False
        
        if fluxes is not None and keff is not None:
            break
    # multiplication factor and flux values
    return keff, np.array(fluxes)


###############################################################################

def _getFluxes(dataFile, fluxes, chs, ng, idx0, nlines):
    """Gets the flux in each group and axial layer for all channels"""
    
    for idx in range(idx0, nlines):
        tline = dataFile[idx]
        if "GR" in tline:
            vals = tline.split()
            if vals[0] != "GR":
                # First group
                z    = int(vals[0])
                g    = int(vals[2].strip(":"))
                vals = vals[3:]
            else:
                # Higher group
                g    = int(vals[1].strip(":"))
                vals = vals[2:]
            
            # save values to flux array
            fluxes[chs,z-1,g-1] = np.array([float(x) for x in vals])
            
            # Break once group ng has been reached
            if z == 1 and g == ng:
                return fluxes, idx


###############################################################################

def _getnums(line,integer=True):
    if integer:
        return [int(x) for x in re.findall(match_number, line)]
    else:
        return [float(x) for x in re.findall(match_number, line)]