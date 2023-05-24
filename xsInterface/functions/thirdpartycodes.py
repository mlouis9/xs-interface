# -*- coding: utf-8 -*-
"""thirdpartycodes.py

(1) Collect cross sections from serpent
(2) Provide all the files required to execute DYN3D and execute them
(3) Future 3rd party codes will be added


Created on Wed May 24 10:15:00 2023 @author: Dan Kotlyar
Last updated on Wed May 24 10:15:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
exeDyn3D - 05/24/20223 - DK

"""

import numpy as np
import os
import copy
import subprocess

from xsInterface.functions.lstreader import get_fluxes as getFlxDyn3d
from xsInterface.functions.lstreader import get_keff as getKeffDyn3d




def exeDyn3D(casedir, xsdir, casefile, exefile, prefixFile='xs', postFile='.dat'):
    """write cross sections into a nemtab format and execute DYN3D
   
        
    Parameters
    ----------
    dyn3dFiles : dict
        describes position of files and directories.
        {'xsdir': 'string', 'casedir': 'string', 'casefile': 'string', 
         'exefile': 'string''}
         xsdir - full directory where the cross sections are
         casedir - full (relative or absolute) directory of _kin file
         casefile - name of the case file
         exefile - name of the file with the actual execution command
    prefixFile : str
        a prefix that starts the cross section file name
    postFile : str
        a postfix that ends the cross section file name

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
    dyn3dResult = {}
    dyn3dResult['keff'] = getKeffDyn3d(lstFile)
    dyn3dResult['flux'] = getFlxDyn3d(lstFile)
    
    normFlux = np.array(dyn3dResult['flux']).flatten()
    normFlux /= normFlux.sum()
    

    return dyn3dResult, normFlux

    


            
    














