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
Last updated on Tue June 06 06:00:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
__init__ capability - 05/27/2023 - DK
Execute method - 05/27/2023 - DK
exeDyn3D - 05/30/2023 - DK
lstreader - 05/30/2023 - DK
Iterate - 06/03/2023 - DK
PlotFluxes - 06/05/2023 - DK
DYN3D polishing - 06/06/2023 - DK

"""

import os
import subprocess

import re

import numpy as np
import matplotlib.pyplot as plt

from xsInterface.functions.newton_krylov_arnoldi import NewtonKrylov,\
    _reshapeTo1D, _numNodes
from xsInterface.functions.plotters import Plot1d
from xsInterface.errors.checkerrors import _islist, _isequallength, _isarray,\
    _inlist, _isstr, _isnonNegativeArray, _iszeropositive, _inrange

match_number = re.compile('-?\ *[0-9]+\.?[0-9]*(?:[Ee]\ *-?\ *[0-9]+)?')

from matplotlib import rcParams
rcParams['figure.dpi'] = 300
FONT_SIZE = 16
MARKER_SIZE = 6

class DYN3D():
    """An object that allows operations with DYN3D

    Parameters
    ----------
    xs : Main object
        an object of type ``Main`` with all cross sections and methods defined.
    casedir : str
        full (relative or absolute) directory where the _kin file is 
        located
    casefile : str
        name of the case file
    exefile : str 
        name of the file with the actual execution command

    Attributes
    ----------
    xs : Main object
        an object of type ``Main`` with all cross sections and methods defined.
    casedir : str
        full (relative or absolute) directory where the _kin file is 
        located
    casefile : str
        name of the case file
    exefile : str 
        name of the file with the actual execution command
    flux : array (3-dim)
        flux values for all channels, layes, and energy groups
    keff : float
        multiplication factor
    iterInputs : dict
        inputs (e.g., adf) values for all the Newton iterations. keys represent
        the attribute, and values represent the 3-dim values 
        [channel, layer, egroup] for each iteration.
    iterOutputs : dict
        Output flux values for all the Newton iterations. keys represent
        the attribute, and values represent the 3-dim values 
        [channel, layer, egroup] for each iteration.
    norm_err : array 1-dim
        norm2 of the predcted minus the reference fluxes


    Raises
    ------
    ValueError
        If the onject ``xs`` has no core values. This indicated that the
        ``PopulateCoreValues`` must be executed prior.
    TypeError
        If ``casedir``, ``casefile``, ``exefile`` are not strings.


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
        self.iterOutputs = {}
        self.norm_err = None


    def Execute(self):
        """Single DYN3D execution

        Parameters
        ----------
        casedir : str
            full (relative or absolute) directory where the _kin file is 
            located
        casefile : str
            name of the case file
        exefile : str 
            name of the file with the actual execution command
    
        Attributes
        ----------
        flux : array (3-dim)
            flux values for all channels, layes, and energy groups
        keff : float
            multiplication factor

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
            name/s of the iterative attributes to be iterated for correction.
        refFlx : 3-dim list
            reference flux solution for all the channels, layers, energy groups. 
            Default is None. In which case the results will be obtained from
            the results on the xs object. The order/structure has to follow
            ``refFlx[channel][layer][group]``
        newtonIters : int
            number of Newton iterates
        krylovSpan : int
            number of Krylov iterates/vectors, must be >= 1 
        dampingF : float
            a damping factor between 0 and 1
        
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
        flux : array 2-dim
            Fluxes (flat 1-dim) as a function of iteration.
        xinputs = xinputs
            Last Input variable (flat 1-dim) as a function of iteration.
            
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
        

    def PlotFluxes(self, xvalues, iters,  
                   chId, layers=None, egroup=0, refFlag=True,
                   flip=False, xlabel="Height, cm", ylabel='Normalized flux',
                   norm=1.0, fontsize=FONT_SIZE, markers="--*", 
                   markerfill=False, markersize=MARKER_SIZE):
        """plot the fluxes for the different newton iterations
        
        Parameters
        ----------
        iters : array
            iteration indices
        xvalues : array
            x-axis values, e.g., heights in cm.
        chId : str
            identification string of the channels.
        layers : array
            layers to be included in the plot. If None all the layers included.
        egroup : int
            energy group integer. Default is 0 (i.e., Fast group).
        refFlag : bool
            flag to indicate if the reference flux to be included in the plot
        flip : bool
            boolean flag to indicate whether results should flipped
        layers : int, list of int, ndarray of int
            identifier/s of the axial layer. If None then all layers are plotted
        xlabel : str
            x-axis label with a default ``Axial height, meters``
        ylabel : str
            y-axis label with a default for any existing parameter
        fontsize : float
            font size value
        markers : str or list of strings
            markers type
        markerfill : bool
            True if the marking filling to be included and False otherwise
        markersize : int or float
            size of the marker with a default of 8.
    
        Raises
        ------
        TypeError
            If ``channel`` is not str or ``layer`` is not int.
            If ``ylabel`` is not str or ``fontsize`` is not int.
        KeyError
            If the channel or layer do not exist.
        NameError
            If attribute does not exist.
    
    
        """
    
        # Check potential errors
  
        allchIds = list(self.xs.core.chIds)
        _inlist(chId, "Channel Id", allchIds)
        
        
        if layers is not None:
            _isnonNegativeArray(layers, "layers")
        
        # iterative results
        results = self.iterOutputs

        # results for all iterations 
        yvalues = {}     
        diff_yvalues = {}
        if iters is not None:
            _isnonNegativeArray(iters, "Iteration indices")
            niter = len(results)
            maxiter = max(iters)
            _inrange(maxiter, "Max iter in {}".format(iters), [0, niter-1])
                
        # energy group
        _iszeropositive(egroup, "energy group")
        _inrange(egroup, "energy groups", [0, self.xs.core.ng-1])

        idxch = allchIds.index(chId)  # channel index
        nlayers = self.xs.core.layers[idxch]  # number of layers
        if layers is None:
            layers = np.linspace(0, nlayers-1, nlayers, dtype=int)
        else:
            maxlayer = max(layers)
            # check that layers exist
            _inrange(maxlayer, "Max layer in {}".format(layers), 
                     [0, nlayers-1])
            nlayers = len(layers)

        
        sumrefFlx = np.sum(np.array(self.refFlx))

        xvals = np.empty(nlayers) 
        for idx, ilayer in enumerate(layers):
            xvals[idx] = xvalues[ilayer]

        # collect results for all iterations
        if iters is not None:
            for it in iters:
                yvals = np.empty(nlayers)
                for idx, ilayer in enumerate(layers):
                    yvals[idx] = results[it][idxch][ilayer][egroup]
                yvalues["It"+str(it)] = yvals
        else:
            yvals = np.empty(nlayers)
            for idx, ilayer in enumerate(layers):
                yvals[idx] = results[0][idxch][ilayer][egroup]
            yvalues["no correction"] = yvals            
            yvals = np.empty(nlayers)
            for idx, ilayer in enumerate(layers):
                yvals[idx] = results[-1][idxch][ilayer][egroup]
            yvalues["with correction"] = yvals 

        refvals = np.empty(nlayers) 
        for idx, ilayer in enumerate(layers):
            refvals[idx] = self.refFlx[idxch][ilayer][egroup] / sumrefFlx
                        
        for key, vals in yvalues.items():
            diff_yvalues[key] = 100*(1-vals/refvals)
            

        if refFlag:
            yvalues["Reference"] = refvals

               
        # plot results for the chosen channels
        plt.figure()
        Plot1d(xvals, yvalues, flip=flip, xlabel=xlabel, ylabel=ylabel, 
               norm=norm, fontsize=fontsize, markers=markers, 
               markerfill=markerfill, markersize=markersize)  
        
        # plot differences
        plt.figure()
        Plot1d(xvals, diff_yvalues, flip=flip, xlabel=xlabel, 
               ylabel="Percent difference in flux, %", 
               norm=norm, fontsize=fontsize, markers=markers[1:], 
               markerfill=markerfill, markersize=markersize) 

        # plot norm2
        niter = len(self.norm_err)
        plt.figure()
        Plot1d(np.linspace(0, niter-1, niter) , self.norm_err, flip=flip,
               xlabel="Iteration #", ylabel="Flux norm2 [reference - predicted]", 
               norm=norm, fontsize=fontsize, markers='--', 
               markerfill=markerfill, markersize=markersize)          

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
        
    fluxes = np.array(fluxes)
    fluxes = fluxes / fluxes.sum()
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