# -*- coding: utf-8 -*-
"""thirdpartycodes.py

(1) Collect cross sections from serpent
(2) Provide all the files required to execute DYN3D and execute them
(3) Future 3rd party codes will be added


Created on Wed May 24 10:15:00 2023 @author: Dan Kotlyar
Last updated on Wed May 24 12:45:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
exeDyn3D - 05/24/20223 - DK

"""

import numpy as np
import os
import subprocess

from xsInterface.functions.lstreader import lstRead


def exeDyn3D(casedir, casefile, exefile):
    """Execute DYN3D and collect results
   
        
    Parameters
    ----------
    casedir : str
        full (relative or absolute) directory where the _kin file is located
    casefile : str
        name of the case file
    exefile : str 
        name of the file with the actual execution command

    Returns
    ------
    dyn3dResult : dict
        keff and flux values from DYN3D        
    normFlux : array
        1-dim normalized flux values (normalized to unity)

    """
    
    # initial working directory
    current_path = os.getcwd()
    if not os.path.isabs(casedir):
        casedir = os.path.abspath(casedir)

    # change directory
    os.chdir(casedir)  
        
    print("... DYN3D Execution ... Start")
    exe_process = subprocess.run(exefile, shell=True,
                                   stdout=subprocess.PIPE)   
    if exe_process.stderr is None:
        print("... DYN3D Execution ... Ended Successfully")
    else:
        raise OSError("... DYN3D Execution ... Error!!!\n{}"
                      .format(exe_process.stderr))

    # change directory to the original working directory
    os.chdir(current_path)

    # lst file
    lstFile = os.path.join(casedir, casefile+'_lst.dat')

    # obtain results from dyn3d _lst file
    keff, fluxes = lstRead(lstFile)
    
    normFlux = np.array(fluxes).flatten()
    normFlux /= normFlux.sum()
    
    return keff, fluxes, normFlux
