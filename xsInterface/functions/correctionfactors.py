# -*- coding: utf-8 -*-
"""correctionfactors

Iterative method to calculate correction factors
required to match the predicted flux solution with the reference one. 

Created on Fri July 22 10:20:00 2022 @author: Dan Kotlyar
Last updated on Wed May 24 05:00:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
__init__ capability - 05/25/2023 - DK


"""


import numpy as np

from xsInterface.errors.checkerrors import _inlist, _islist, _isequallength,\
    _iszeropositive, _inrange



class CorrectionFactors():
    """A container to store unique universes having MultipleSets objects

    Parameters
    ----------
    xs : Main object
        data Main object with all the read, write, etc. methods
    attributes : list
        all the attributes required for the problem
    states : dict
        dict with keys as the states names, e.g., history, time, and pert names 
        and values as 2-dim list with the values of the state for channels and
        layers. e.g., time = [[0.0, 0.0, 0.0, 0.0]]*5
    volManip : string or list of string
        volume manipulation ['multiply', 'divide']. Default is None.
    corrAttr : str
        name of the iterative attribute which will be iterated for correction
    refAttr : str
        name of the objective attribute set for convergence (e.g., flux)
    refSol : 3-dim list
        reference solution for all the channels, layers, energy groups. 
        Default is None. In which case the results will be obtained from
        the results on the xs object.
    attrValue : 3-dim list
        initial guess for the correction attribute. Defualt is None, in which
        case unity values will be populated for all channels, layers, and
        energy groups.


   

    Attributes
    ----------
    xs : Main object
        data Main object with all the read, write, etc. methods
    attributes : list
        all the attributes required for the problem
    states : dict
        dict with keys as the states names, e.g., history, time, and pert names 
        and values as 2-dim list with the values of the state for channels and
        layers. e.g., time = [[0.0, 0.0, 0.0, 0.0]]*5
    volManip : string or list of string
        volume manipulation ['multiply', 'divide']. Default is None.
    corrAttr : str
        name of the iterative attribute which will be iterated for correction
    refAttr : str
        name of the objective attribute set for convergence (e.g., flux)
    refSol : 3-dim list
        reference solution for all the channels, layers, energy groups. 
        Default is None. In which case the results will be obtained from
        the results on the xs object.
    attrValue : 3-dim list
        initial guess for the correction attribute. Defualt is None, in which
        case unity values will be populated for all channels, layers, and
        energy groups.
    chIds : list
        names for all the channels corresponding (in order) to ``nomvalues``


    Methods
    -------
    TBC : ....

    """

    def __init__(self, xs, attributes, states, volManip,
                 corrAttr, refAttr, refSol=None, attrValue=None):
        
        # obtain all the values for the reference points
        nomvalues, chIds =\
        xs.CoreValues(attributes, 
                      chIds=xs.core.chIds, 
                      volManip=volManip, 
                      **states)

        _inlist(refAttr, "Objective function name", attributes)

        nchs = len(chIds)  # number of channels
        ng = len(nomvalues[attributes[0]][0][0])  # number of energy groups
        if refSol is not None:
            _islist(refSol, "Reference solution")
            _isequallength(refSol, nchs, "1st-dim is the channels number")
            for ich, ch in enumerate(nomvalues[attributes[0]]):
                nlayers = len(ch)  # number of layers
                _isequallength(refSol[ich], nlayers, "2nd-dim - layers number")
                for layer in refSol[ich]:
                     _isequallength(layer, ng, "3rd-dim - ene-groups number")
        else:
            refSol = nomvalues[refAttr]


        if attrValue is None:
            x0 = [1.0]*nchs
            for ich, ch in enumerate(nomvalues[attributes[0]]):
                nlayers = len(ch)  # number of layers
                x0[ich] = [np.ones(ng)]*nlayers
            nomvalues[corrAttr] = x0  # add the new attribute
        else:
            if corrAttr not in attributes:
                raise KeyError("{} does not appear in {}."
                               .format(corrAttr, attributes))


        self.attributes = attributes
        self.chIds = chIds
        self.volManip = volManip
        self.states = states
        self.nomvalues = nomvalues
        self.refAttr = refAttr
        self.corrAttr = corrAttr
        self.refSol = refSol
        self.attrValue = x0
        self._xs = xs




    def PopulateCoreData(self):
        """Read universes cross-section data and associated templates
        
        The ``Read`` method also populates the template files with data. 

        Parameters
        ----------
        readTemplate : bool
            flag that indicates if templates need to be read and populated
            with data
        readUniverses : bool
            flag that indicates if cross sections for different universes
            need to be read



        Returns
        -------
        dataFiles : dict
            keys represent universes or dummy variables; values represent
            correponding files populated with data.

        """
        
        # Read xs data and templates and populate data
        self._xs.Read(readUniverses=False, readMapTemplate=True,
                      userdata = self.nomvalues)            




  