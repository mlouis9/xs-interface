"""readserpent.py

Read the data in multiple .coe branch files using the ``serpentTools`` package.
This method allows to read multiple history files with multiple universes.
It also allows to filter the data/attributes of interest.

Created on Sat July 30 05:00:00 2022 @author: Dan Kotlyar
Last updated on Thu Feb 23 15:00:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

List changes / additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
ReadCoefFiles  - 07/30/2022 - DK
_ReLabelStates  - 08/03/2022 - DK
_FilterAttrs - 08/04/2022 - DK
ReadSerpent - 08/04/2022 - DK
_FilterAttrs - 02/23/2023 - DK (changed burnup / time treatment)

"""

from pathlib import Path
import copy
import itertools
import numpy as np

import serpentTools

from xsInterface.errors.checkerrors import _isstr, _isarray, _isequallength,\
    _isndarray, _is1darray
from xsInterface.errors.customerrors import SerpentFileError
from serpentTools.parsers.results import ResultsReader


def ReadSerpent(fnames, strLabels, numLabels, attrs=None, times=None,
                burnups=None):
    """Read .coe files and extract data in a dictionary format.
    
    The format of the final dictionary is:
        universes-->histories-->times-->branches-->attributes

    Parameters
    ----------
    fnames : dict
        .coe file directory path + file name
        for universes with various history branches
        structure of the dictionary: {universe:{history:filename}}
    strLabels : dict
        keys represent the names of the states, e.g., fuel, boron, ..
        values represent the corresponding names in a string format, e.g.,
        strLabels = {'fuel': ['f600', 'f900', 'nom', 'f1200']}
    numLabels : dict
        keys represent the names of the states, e.g., fuel, boron, ..
        values represent the corresponding names in a numeric format, e.g.,
        strLabels = {'fuel': [600.0, 900.0, 1200.0, 1500.0]}        
    attrs : list
        selected attributes. If None is defined then all the attributes that
        exist on the dataIn container are accounted for.
    times : list/array
        numeric time values.
    burnups : list/array
        numeric burnups values. If both ``times`` and ``burnups`` are None then
        all the time points read by Serpent will be stored.
        
    Returns
    -------
    data : dict
        data dict that acts as a container with the following structure
        univId: {history: {timeIdx: {branch: univData}}}
        where univId is a string, history is a string, timeIdx is an int,
        branch is a tuple Id containing numeric values,
        and univData is a dictionary with keys representing the attributes and
        values the corresponding values.
    timepoints : list
        vector of all the stored time-points on the ``data`` dictionary


    """

    # Error checking
    _errorscheck(fnames, strLabels, numLabels, attrs, times, burnups)
    # convert to lower case
    if attrs is not None:
        attrs = [attr.lower() for attr in attrs]

    # Read all the .coe file
    dataStrBranches = _ReadHistoryFiles(fnames, strLabels)
    
    # Replace the string branch values with numeric values
    dataNumBranches = _ReLabelStates(dataStrBranches, strLabels, numLabels)
    
    # Filter specific time points and attributes
    dataOut, timepoints = _FilterAttrs(dataNumBranches, attrs, times, burnups)

    return dataOut, timepoints


def _ReadHistoryFiles(fnames, strLabels):
    """Read multiple serpent output .coe files

    Parameters
    ----------
    fnames : dict
        .coe file directory path + file name
        for universes with various history branches
        structure of the dictionary: {universe:{history:filename}}
    strLabels : dict
        keys represent the names of the states, e.g., fuel, boron, ..
        values represent the corresponding names in a string format, e.g.,
        strLabels = {'fuel': ['f600', 'f900', 'nom', 'f1200']}        

    Raises
    ------
    TypeError
        If ``filename`` is not str.
    OSError
        If the path ``filename`` does not exist.
        
    Returns
    -------
    data : dict
        data dict that acts as a container with the following structure
        univId: {history: {timeIdx: {branch: univData}}}
        where univId is a string, history is a string, timeIdx is an int,
        branch is a tuple Id, and univData is a data container.

    """

    # dictionary to store universes-->histories-->times-->branches
    data = {}
    
    for univUsrId in fnames:
    
        
        for historyId, coeFile in fnames[univUsrId].items():

            print("... Reading coe/_res.m file for hisotry <{}> ..."
                  .format(historyId))
            
            coedata = _ReadCoefFile(coeFile)
            if isinstance(coedata, ResultsReader): 
                coedata = _ReadResFile(coedata, strLabels)
        
            for univ in coedata:
                univId = univUsrId + univ
                if univId in data:
                    data[univId].update({historyId: coedata[univ]})
                else:
                    data.update({univId:{historyId: coedata[univ]}})
            
    return data
    


def _ReadCoefFile(coeFile):
    """Read serpent output .coe file

    Collection of data is obtained using the ``serpentTools``

    Parameters
    ----------
    coeFile : str
        full name of the .coe input file

    Raises
    ------
    TypeError
        If ``coeFile`` is not str.
    OSError
        If the path ``coeFile`` does not exist.
        
    Returns
    -------
    data : dict
        data dict that acts as a container with the following structure
        univId: {timeIdx: {branch: univData}}
        where univId is a string, timeIdx is an int, branch is a tuple Id, and
        univData is a data container.
    burnups : list
        burnup values
    timedays: list
        time values in days

    """


    # check that `coeFile` variable is a string
    _isstr(coeFile, "Input file")

    # read the file and return its content
    filePath = Path(coeFile)
    if not filePath.is_file():
        raise OSError("The file {} does not exist.".format(coeFile))

    # read the COE file
    # rc['xs.reshapeScatter'] = True
    coe0 = serpentTools.read(coeFile)  # coe is a data container
    
    if isinstance(coe0, ResultsReader):
        return coe0
    
    # Structure of the data container
    # univId: {timeIdx: {state: univData}}   
    data = {}

    # loop over all the branches
    for brKeys, brData in coe0.items():
        # converet to lower case
        brKeysLower = tuple([i.lower() for i in brKeys])
        # Loop over all the universes and time points
        for univKey in brData:
            
            # Obtain the universe Id and time 
            univId = univKey.universe
            step = univKey.step

            if univId not in data:
                data[univId] = {}
            if step not in data[univId]:
                data[univId][step] = {}


            # obtain the data container
            univData = brData.getUniv(univId, index=step)

            # add the data to the data dictionary
            data[univId][step][brKeysLower] = univData
                     
    return data




def _ReadResFile(res0, strLabels):
    """Process serpent output .res file

    Results data is obtained using the ``serpentTools``

    Parameters
    ----------
    res0 : ResultsReader object
        ResultsReader object with 
    strLabels : dict
        keys represent the names of the states, e.g., fuel, boron, ..
        values represent the corresponding names in a string format, e.g.,
        strLabels = {'fuel': ['f600', 'f900', 'nom', 'f1200']}


    Returns
    -------
    data : dict
        data dict that acts as a container with the following structure
        univId: {timeIdx: {branch: univData}}
        where univId is a string, timeIdx is an int, branch is a tuple Id, and
        univData is a data container.
    burnups : list
        burnup values
    timedays: list
        time values in days

    """



    # construct all the labels of the used branches according to their order
    # of appearance
    strIds  = [key for key in itertools.product(*strLabels.values())]
    nbranches = len(strIds)  # total number of branches
    
    # Structure of the data container
    # univId: {timeIdx: {state: univData}}   
    data = {}
    # Loop over all the universes and time points
    for univKey, univData in res0.universes.items():

        # step idx that indicates a branch
        try:
            step, branchIdx = divmod(univKey.step, nbranches)
            brKeysLower = tuple(strIds[branchIdx])
        except:
            raise ValueError("The _res.m file has more branches than defined "
                             "by the branch card{}".format(strLabels))
        

        univId = univKey.universe

        if univId not in data:
            data[univId] = {}
        if step not in data[univId]:
            data[univId][step] = {}


        # add the data to the data dictionary
        data[univId][step][brKeysLower] = univData
        
                     
    return data

            
def _ReLabelStates(dataIn, strLabels, numLabels):
    """ReLabel the names of the states in the .coe files

    Parameters
    ----------
    dataIn : dict
        data dict that acts as a container with the following structure
        univId: {history: {timeIdx: {branch: univData}}}
        where univId is a string, history is a string, timeIdx is an int,
        branch is a tuple Id containing string values,
        and univData is a data container.
    strLabels : dict
        keys represent the names of the states, e.g., fuel, boron, ..
        values represent the corresponding names in a string format, e.g.,
        strLabels = {'fuel': ['f600', 'f900', 'nom', 'f1200']}
    numLabels : dict
        keys represent the names of the states, e.g., fuel, boron, ..
        values represent the corresponding names in a numeric format, e.g.,
        strLabels = {'fuel': [600.0, 900.0, 1200.0, 1500.0]}        
        
    Raises
    ------
    SerpentFileError
        If ``dataIn`` do not contain a branch defined in ``strLabels``.
        
    Returns
    -------
    data : dict
        data dict that acts as a container with the following structure
        univId: {history: {timeIdx: {branch: univData}}}
        where univId is a string, history is a string, timeIdx is an int,
        branch is a tuple Id containing numeric values,
        and univData is a data container.

    """

    # updated dictionary to store universes-->histories-->times-->branches
    dataOut = copy.deepcopy(dataIn)

    strIds  = [key for key in itertools.product(*strLabels.values())]
    numIds  = [key for key in itertools.product(*numLabels.values())]
    
    if len(strIds) == 1:
        strIds = list(strIds[0])

    # link between the original branch Ids and their numeric values
    for univId, univData in dataIn.items():
        for histId, histData in univData.items():
            for timeIdx, timeData in histData.items():
                for branchId, branchData in timeData.items():
                    if branchId in strIds:
                        idxId = strIds.index(branchId)
                        # remove the existing data
                        dataOut[univId][histId][timeIdx].pop(branchId)
                        # replace with the numeric key
                        dataOut[univId][histId][timeIdx][numIds[idxId]] =\
                            branchData
                    else:
                        raise SerpentFileError(
                            "Branch <{}> not provided\nfor univ=<{}>; "
                            "history=<{}>.\nCheck that order of branches card "
                            "correspond to the order provided in the .coe file"
                            .format(branchId, univId, histId))
                    
    return dataOut


def _FilterAttrs(dataIn, attrs, times, burnups):
    """Select only the given attributes and remove all others

    Parameters
    ----------
    dataIn : dict
        data dict that acts as a container with the following structure
        univId: {history: {timeIdx: {branch: univData}}}
        where univId is a string, history is a string, timeIdx is an int,
        branch is a tuple Id containing numeric values,
        and univData is a data container.
    attrs : list
        selected attributes. If None is defined then all the attributes that
        exist on the dataIn container are accounted for.
    times : list/array
        numeric time values.
    burnups : list/array
        numeric burnups values. If both ``times`` and ``burnups`` are None then
        all the time points read by Serpent will be stored.

    Raises
    ------
    SerpentFileError
        If points within ``times`` or ``burnups` do not exist on the ``dataIn``
        If ``attrs`` do not exist on the ``dataIn``
                
    Returns
    -------
    data : dict
        data dict that acts as a container with the following structure
        univId: {history: {timeIdx: {branch: univData}}}
        where univId is a string, history is a string, timeIdx is an int,
        branch is a tuple Id containing numeric values,
        and univData is a dictionary with keys representing the attributes and
        values the corresponding values.
    timepoints : list
        vector of all the stored time-points on the ``data`` dictionary

    """

    # updated dictionary to store universes-->histories-->times-->branches
    dataOut = copy.deepcopy(dataIn)

    timepoints = []  # to store all the timepoints
    # Keep only the attributes of interest
    for univId, univData in dataIn.items():
        for histId, histData in univData.items():
            for timeIdx, timeData in histData.items():
                for branchId, branchData in timeData.items():
                    # ---------------------------------------------------------
                    # filter specific time points
                    # ---------------------------------------------------------
                    if times is not None:
                        if branchData.day is None:
                           raise SerpentFileError(
                               "Times <{}> provided but no time points exist "
                               "in Serpent.\nTry burnups.".format(times)) 
                        # this time-point should be saved
                        elif (np.isclose(times, branchData.day)).any():
                            if (len(timepoints) == 0 or not (np.isclose(
                                    timepoints, branchData.day)).any()):
                                timepoints.append(branchData.day)
                        else:
                            # remove the data for the current time point
                            dataOut[univId][histId].pop(timeIdx)
                            break  # from the branch loop
                    # ---------------------------------------------------------
                    # filter specific burnup points
                    # ---------------------------------------------------------                          
                    elif burnups is not None:
                        if branchData.bu is None:
                           raise SerpentFileError(
                               "Burnups <{}> provided but no bu points exist "
                               "in Serpent.\nTry times.".format(burnups))                                                       
                        # this burnup-point should be saved
                        elif (np.isclose(burnups, branchData.bu)).any():
                            if (len(timepoints) == 0 or not
                                (np.isclose(timepoints, branchData.bu)).any()):
                                timepoints.append(branchData.bu) 
                        else:
                            # remove the data for the current time point
                            dataOut[univId][histId].pop(timeIdx)
                            break  # from the branch loop                        

                    serpentDict = {}  # store all the data from serpent
                    for attr, values in branchData.infExp.items():
                        serpentDict[attr.lower()] = values
                    for attr, values in branchData.b1Exp.items():
                        serpentDict[attr.lower()] = values
                    for attr, values in branchData.gc.items():
                        serpentDict[attr.lower()] = values
                    # ---------------------------------------------------------
                    # filter specific attributes 
                    # ---------------------------------------------------------
                    attrsDict = {}  # store all attributes
                    if attrs is not None:
                        for attr in attrs:
                            if attr in serpentDict:
                                attrsDict[attr] = serpentDict[attr]
                            else:
                                raise SerpentFileError("No attribute <{}>"
                                                           .format(attr))
                    else:
                        attrsDict = serpentDict

                    # remove the existing homogeneous universe data
                    dataOut[univId][histId][timeIdx].pop(branchId)
                    # replace with the numeric key
                    dataOut[univId][histId][timeIdx][branchId] = attrsDict
    
    ntimes = len(timepoints)
    if times is not None and len(times) != ntimes:
        raise SerpentFileError(
            "times <{}>\nprovided do not match times read by Serpent\n<{}>"
            .format(times, timepoints))
    elif burnups is not None and len(burnups) != ntimes:
        raise SerpentFileError(
            "burnups <{}>\nprovided do not match burnups read by Serpent\n<{}>"
            .format(burnups, timepoints))
                                
    return dataOut, timepoints


def _errorscheck(fnames, strLabels, numLabels, attrs, times, burnups):
    """Check that all the parameters are properly defined
    
    Raises
    ------
    SerpentFileError
        If ``times`` and ``burnups`` are both provided.
        If ``times`` or ``burnups` are not numeric 1-dim arrays.
        If points within ``times`` or ``burnups` do not exist on the ``dataIn``
        If ``attrs`` do not exist on the ``dataIn``    
        If ``strLabels`` and ``numLabels`` do not contain the same keys.
        If ``dataIn`` do not contain a branch defined in ``strLabels``.
        If the values in ``strLabels`` or ``numLabels`` do not contain arrays.
        If the values in ``strLabels`` or ``numLabels`` do not have equal
        number of values.    
    """
    
    # -------------------------------------------------------------------------    
    # fnames must be a dict within dictionaries
    # -------------------------------------------------------------------------
    if not isinstance(fnames, dict):
        raise SerpentFileError('File names must be of a dict type and not {}'
                               .format(fnames))
    for univId, univDict in fnames.items():
        if not isinstance(univDict, dict):
            raise SerpentFileError("The items <{}> for universe <{}> must be "
                                   "of a dict type".format(univDict, univId))


    # -------------------------------------------------------------------------    
    # Relabeling
    # -------------------------------------------------------------------------
    strKeys = list(strLabels.keys())
    numKeys = list(numLabels.keys())
    if strKeys != numKeys:
        errmsg = "Branch str Ids <{}>\n must be provided in identical order "\
        "as the corresponding numeric values <{}>".format(strKeys, numKeys)
        raise SerpentFileError(errmsg)
        
    # check that lists/arrays are of identical size and of proper types
    for key, strvals in strLabels.items():
        try:
            _isarray(strvals, 'String values <{}> for state <{}>'
                     .format(strvals, key))
            numvals = numLabels[key]
            _isarray(numvals, 'Numeric values <{}> for state <{}>'
                     .format(numvals, key))
            nvals = len(strvals)
            _isequallength(numvals, nvals,
                           "Numeric values for state <{}>".format(key))
            numLabels[key] = np.array(numvals, dtype=float)
        except (ValueError, TypeError) as detail:
            raise SerpentFileError("Values <{}> for <{}>\n{}"
                                   .format(numvals, key, detail))


    # -------------------------------------------------------------------------    
    # attrs, times, burnups
    # -------------------------------------------------------------------------
    if times is not None and burnups is not None:
        raise SerpentFileError(
            "times <{}> and burnups <{}> cannot be provided together.\nProvide"
            " only one.".format(times, burnups))
    elif times is not None:
        try:
            _isarray(times, "Times")
            times = np.array(times, dtype=float)
            _isndarray(times, "Times")
            _is1darray(times, "Times")
        except (TypeError, ValueError) as detail:   
            raise SerpentFileError("{}".format(detail))    
            
    elif burnups is not None:
        try:
            _isarray(burnups, "Burnups")
            burnups = np.array(burnups, dtype=float)
            _isndarray(burnups, "Burnups")
            _is1darray(burnups, "Burnups")        
        except (TypeError, ValueError) as detail:   
            raise SerpentFileError("{}".format(detail))
    if attrs is not None:
        try:
            _isarray(attrs, "Attributes")
        except (TypeError, ValueError) as detail:   
            raise SerpentFileError("{}".format(detail))    