"""readshift.py

Read the data in multiple .coe branch files using the ``serpentTools`` package.
This method allows to read multiple history files with multiple universes.
It also allows to filter the data/attributes of interest.

Created on Sat July 30 05:00:00 2022 @author: Dan Kotlyar
Last updated on Wed Aug 04 16:00:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

List changes / additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
ReadCoefFiles  - 07/30/2022 - DK
_ReLabelStates  - 08/03/2022 - DK
_FilterAttrs - 08/04/2022 - DK
ReadSerpent - 08/04/2022 - DK

"""

from pathlib import Path
import h5py
import copy
import itertools
import numpy as np

import serpentTools

from xsInterface.errors.checkerrors import _isstr, _isarray, _isequallength,\
    _isndarray, _is1darray


def ReadShiftFiles(files, attrs=None, mgxsName = 'mg_xs/tallies',
                   talliesName = 'tallies'):
    """Read all the cell nodal tallies and mg_xs from multiple shift files
    
    The format of the returned data dictionary is:
        universes-->histories-->times-->branches-->attributes

    Parameters
    ----------
    files : dict
        file name (+path included) as keys and states dictionary as values
        files = {'file1': {state1}, 'file2': {state2}, ...}
        state = {'history': value, 'time': value, 'branch': value}    
    attrs : list
        selected attributes. If None is defined then all the attributes that
        exist in the tallies and mg xs are collected.
        
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
    
    data = {}
    for file, states in files.items():
        
        dataOut = _ReadShiftFile(file, mgxsName, talliesName)             
        history = states['history']
        time = states['time']
        branch = states['branch']
        
        # universes-->histories-->times-->branches-->attributes
        for univId, univData in dataOut.items():
            if univId not in data:
                # universe does not exist
                data.update({univId: {history: {time:{ branch:{univData}}}}})
                
            elif history not in data[univId]:
                data[univId].update({history: {time:{ branch:{univData}}}})

            elif time not in data[univId][history]:
                data[univId][history].update({time:{ branch:{univData}}})

            else:
                [univId][history][time].update({ branch:{univData}})            
                
    return data
            

def _ReadShiftFile(shiftFile, mgxsName = 'mg_xs/tallies',
                   talliesName = 'tallies'):
    """Read a specific shift file with cell nodal tallies and mg_xs
    
    Parameters
    ----------
    file : string
        shift file directory path + file name

    Returns
    -------
    data : dict
        data dict that stores all the tallies and mg_xs attributes and
        their coresponding values.


    """

    # check that `shiftFile` variable is a string
    _isstr(shiftFile, "Input file")

    # read the file and return its content
    filePath = Path(shiftFile)
    if not filePath.is_file():
        raise OSError("The file {} does not exist.".format(shiftFile))
        
    if not h5py.is_hdf5(shiftFile):
        raise OSError('{} is not an hdf5 file'.format(shiftFile))

    try:
        h5file = h5py.File(shiftFile, 'r')
    except:
        raise OSError('Cannot read the hdf5 file {}'.format(shiftFile))

    # Structure of the data container
    # univId: {timeIdx: {state: univData}}   
    data = {}

    # Loop over all the attributes in mg_xs
    mgxs = h5file.get(mgxsName)
    for attr in mgxs.keys():
        values = mgxs.get(attr+'/'+attr)
        if values is None:
            continue
        nvals = values.shape
        if len(nvals) == 3:  # (Ids, energy-groups, data)
            nIds = nvals[0]
            # nEgs = nvals[1]
            for idxId in range(nIds):
                if idxId in data:
                    data[idxId].update({attr: values[idxId].flatten()})
                else:
                    data[idxId] = {attr: values[idxId].flatten()}
            
        elif len(nvals) == 5:  # (Ids, energy-groups, energy-groups, Pn order, data)
            nIds = nvals[0]
            # EgsFrom = nvals[1]
            # EgsTo = nvals[2]
            orderPn = nvals[3]
            for idxId in range(nIds):
                for Pn in range(orderPn):
                    if idxId in data: 
                        data[idxId].update({attr+str(Pn): 
                                            values[idxId, :, :, Pn, 0]
                                            .flatten()})
                    else:
                        data[idxId] = {attr+str(Pn): values[idxId, :, :, Pn, 0]
                                       .flatten()}
        else:
            raise ValueError("Unrecognized data structure for {} with shape {}"
                             ".\n".format(attr, nvals))

    return data


  


