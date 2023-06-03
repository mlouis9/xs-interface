# -*- coding: utf-8 -*-
"""dyn3d

Supporting classes and methods to work with the nodal diffusion code, DYN3D.
The following methods include:
    (1) Single execution of DYN3D (including reading results from _lst file)
    (2) Iterative (non-linear) methods to converge flux

The main ``Iterate`` method focuses on:
Iterative method to calculate correction factors
required to match the predicted flux solution (DYN3D) with the reference one. 

Created on Sat May 27 16:20:00 2023 @author: Dan Kotlyar
Last updated on Tue May 30 11:15:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
__init__ capability - 05/27/2023 - DK
Execute method - 05/27/2023 - DK
exeDyn3D - 05/30/2023 - DK
lstreader - 05/30/2023 - DK


"""

import os
import subprocess

import re

import numpy as np

from xsInterface.functions.newton_krylov_arnoldi import NewtonKrylov,\
    _reshapeTo1D, _numNodes
from xsInterface.errors.checkerrors import _islist, _isequallength, _isarray,\
    _inlist, _isstr

match_number = re.compile('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')


class DYN3D():
    """A container to store unique universes having MultipleSets objects

    Parameters
    ----------
    xs : Main object
        an object of type ``Main`` with all cross sections and methods defined.


    Attributes
    ----------
    xs : Main object
        an object of type ``Main`` with all cross sections and methods defined.
    corrattrs : list of str
        name of the iterative attributes which will be iterated for correction.
    refFlx : 3-dim list
        reference flux solution for all the channels, layers, energy groups. 
        Default is None. In which case the results will be obtained from
        the results on the xs object. The order/structure has to follow
        ``refFlx[channel][layer][group]``


    Methods
    -------
    TBC : ....

    """

    def __init__(self, xs, casedir, casefile, exefile):
        
        # xs object must already contain all the attribute values
        if not hasattr(xs.core, 'corevalues'):
            raise ValueError(
                "The object xs has not been populated with values.\n"
                "Please use the PopulateCoreData method on the xs object\n"
                "before using the CorrectionFactors class.")
                   
        _isstr(casedir, 'casedir')
        _isstr(casefile, 'casefile')
        _isstr(exefile, 'exefile')
        
        # save all parameters
        self.xs = xs
        self.casedir = casedir
        self.casefile = casefile
        self.exefile = exefile
        self.flux = None
        self.keff = None
        # store all results
        self.iterInputs = {}
        self.norm_err = None


    def Execute(self):
        """Read universes cross-section data and associated templates
        
        The ``Read`` method also populates the template files with data. 

        Parameters
        ----------
        casedir : str
            full (relative or absolute) directory where the _kin file is 
            located
        casefile : str
            name of the case file
        exefile : str 
            name of the file with the actual execution command
    
        Returns
        -------
        dyn3dResult : dict
            keff and flux values from DYN3D        
        normFlux : array
            1-dim normalized flux values (normalized to unity)

        """
        
        # create cross section files
        self.xs.Write()
        
        # execute dyn3d
        keff, prdFlx = exeDyn3D(self.casedir, self.casefile, self.exefile)
        
        # save results
        self.keff = keff 
        self.flux = prdFlx
        

    def Iterate(self, corrattrs, refFlx, newtonIters: int, krylovSpan: int, 
                dampingF=1.0):
        """Calculate correction factors via non-linear iterations
        
        Iterative method to calculate correction factors
        required to match the predicted flux solution with the reference one. 

        Parameters
        ----------
        corrattrs : list of str
            name of the iterative attributes which will be iterated for correction.
        refFlx : 3-dim list
            reference flux solution for all the channels, layers, energy groups. 
            Default is None. In which case the results will be obtained from
            the results on the xs object. The order/structure has to follow
            ``refFlx[channel][layer][group]``
        
        Returns
        -------
        corrattrs : list of str
            name of the iterative attributes which will be iterated for
            correction.
        refFlx : 3-dim list
            reference flux solution for all the channels, layers, energy groups. 
            Default is None. In which case the results will be obtained from
            the results on the xs object. The order/structure has to follow
            ``refFlx[channel][layer][group]``
            
        """
        
        # existing and expected attributes
        expattrs = list(self.xs.core.corevalues.keys())
        _islist(corrattrs, "correction attributes")
        
        for attr in corrattrs:
            _inlist(attr, "correction attribute", expattrs)

        chIds = list(self.xs.core.chIds)  # channel Ids

        # check that refFlx is properly provided
        for attr, corevals in self.xs.core.corevalues.items():
            ng = len(corevals[0][0])  # expected number of energy groups
            nchs = len(corevals)
            _isarray(refFlx, "refFlx")
            _isequallength(refFlx, nchs, "#channels refFlx")
            # loop over all the channels
            for ich, chvals in enumerate(corevals):
                nlayers = len(chvals)  # expected #layers in a specific channel
                _isarray(refFlx[ich], "refFlx channel={}".format(chIds[ich]))
                _isequallength(refFlx[ich], nlayers, "#layers refFlx")
                for ilayer, layervals in enumerate(chvals):
                    _isarray(layervals, "refFlx ch={}, layer={}"
                             .format(chIds[ich], ilayer))
                    _isequallength(refFlx[ich][ilayer], ng, 
                                   "#groups refFlx for ch={} "
                                   "layer={}".format(chIds[ich], ilayer))
            break  # only should be done for one attribute        

        self.corrattrs = corrattrs
        self.refFlx = refFlx

        nodesN = _numNodes(refFlx)  # total number of nodes

        for attr in corrattrs:
            x0 =\
            _reshapeTo1D(self.xs.core.corevalues[attr], nodesN, normFlag=False)
            fluxes, xinputs, norm_err, refFlxNorm =\
                NewtonKrylov(self, attr, x0, refFlx, newtonIters, krylovSpan, 
                             dampingF)
         
                
        self.fluxes = fluxes
        self.refFlxNorm = refFlxNorm
        self.xinputs = xinputs
        self.norm_err = norm_err
        


# -----------------------------------------------------------------------------
#         Supplementary functions
# -----------------------------------------------------------------------------


def exeDyn3D(casedir, casefile, exefile):
    """Execute DYN3D and collect results
        
    Provide all the files required to execute DYN3D and execute them
            
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
    
    # normFlux = np.array(fluxes).flatten()
    # normFlux /= normFlux.sum()
    
    return keff, fluxes, # normFlux


###############################################################################

def lstRead(lstfile):
    """Reads keff and fluxes results from lst file
    
    Read the nodal fluxes and k-eff from the _lst file created by DYN3D.
    
    """
    
    
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