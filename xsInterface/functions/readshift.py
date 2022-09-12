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

import copy

from pathlib import Path
import h5py
import numpy as np


from xsInterface.errors.checkerrors import _isstr, _isarray, _isequallength,\
    _isndarray, _is1darray


def ReadShiftFiles(files, attrs=None, mgxsName = 'mg_xs/tallies',
                   tallies = ['scattering_matrix0', 'scattering_matrix1'],
                   sct_neutrons=4, transfer='transfer_{:d}n', flux='flux',
                   scattering='scattering_matrix'):
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
    mgxsName : string
        full path to the mg_xs data in the hdf5 file
    tallies : list of strings
        names of the tallies to be added or overwritten from the tallies onto
        the mg_xs
    sct_neutrons : int
        max number of neutrons produced in nxn reaction
    transfer : str
        string pattern for the scattering cross section name
    scattering : str
        name of the output scattering matrix to be defined in the dictionary
        
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
    for state, file in files.items():
        
        # Read shift single file for a specific state
        dataOut = _ReadShiftFile(file, mgxsName, tallies, sct_neutrons, flux,
                                 scattering)
        # structure of structure is history, time, branches         
        history = state[0]  # history
        time = state[1]  # time
        branch = list(state[2:])  # branch
        
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
                   tallies = ['scattering_matrix0', 'scattering_matrix1'],
                   sct_neutrons=4,
                   transfer='transfer_{:d}n', flux='flux',
                   scattering='scattering_matrix'):
    """Read a specific hdf5 shift file with cell nodal tallies and mg_xs
    
    Parameters
    ----------
    shiftFile : string
        shift hdf5 file directory path + file name
    mgxsName : string
        full path to the mg_xs data in the hdf5 file
    tallies : list of strings
        names of the tallies to be added or overwritten from the tallies onto
        the mg_xs
    sct_neutrons : int
        max number of neutrons produced in nxn reaction
    transfer : str
        string pattern for the scattering cross section name
    scattering : str
        name of the output scattering matrix to be defined in the dictionary
        

    Returns
    -------
    data : dict
        data dict that stores all the tallies and mg_xs attributes and
        their coresponding values.
        The data structure is  = {univId1: {attr1: values1, attr2: values2,...},
                                 univId2: {attr1: values1, attr2: values2,...},
                                 ...}


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
    mgxsdata = {}
    tallydata = {}

    # Read mg_xs data
    mgxsdata = _GetMgXsShift(h5file, mgxsName)
    if mgxsdata == {}:
        raise OSError('Cannot identify ng_xs in the hdf5 file {}'
                      .format(shiftFile))
    
    if tallies is None or tallies == []:
        return mgxsdata
    # Read tally data
    tallydata =\
        _GetTalliesShift(h5file, sct_neutrons, transfer, flux, scattering)

    data = copy.deepcopy(mgxsdata)    
    # Overwrite mg_xs data with tally data
    for idxId in tallydata:
        for tally in tallies:
            if tally not in tallydata[idxId]:
                raise KeyError('Tally {} does not exist for Id={}.\nThe '
                               'following tallies exist: {}'
                               .format(tally, idxId, tallydata[idxId].keys()))
            data[idxId][tally] = tallydata[idxId][tally]
    
    return data


def _GetMgXsShift(h5file, mgxsName):
    """Obtain the mg_xs data in the hdf5 file"""
    # Loop over all the attributes in mg_xs
    mgxs = h5file.get(mgxsName)
    mgxsdata = {}
    for attr in mgxs.keys():
        values = mgxs.get(attr+'/'+attr)
        if values is None:
            continue
        nvals = values.shape
        if len(nvals) == 3:  # (Ids, energy-groups, data)
            nIds = nvals[0]
            # nEgs = nvals[1]
            for idxId in range(nIds):
                if idxId in mgxsdata:
                    mgxsdata[idxId].update({attr: values[idxId].flatten()})
                else:
                    mgxsdata[idxId] = {attr: values[idxId].flatten()}
            
        elif len(nvals) == 5:  # (Ids, energy-groups, energy-groups, Pn order, data)
            nIds = nvals[0]
            # EgsFrom = nvals[1]
            # EgsTo = nvals[2]
            orderPn = nvals[3]
            for idxId in range(nIds):
                for Pn in range(orderPn):
                    if idxId in mgxsdata: 
                        mgxsdata[idxId].update({attr+str(Pn): 
                                            values[idxId, :, :, Pn, 0]
                                            .flatten()})
                    else:
                        mgxsdata[idxId] = {attr+str(Pn): values[idxId, :, :, Pn, 0]
                                       .flatten()}
        else:
            raise ValueError("Unrecognized data structure for {} with shape {}"
                             ".\n".format(attr, nvals))
    return mgxsdata


def _GetTalliesShift(h5data, order_nxn, transfer, flux, scattering):
    """Obtain the tallies data in the hdf5 file"""
    
    binned_data = ['tally/tallies.coarse', 'tally/tallies.spm']
    
    data = {}  # store all the data in this dict
       
    # -------------------------------------------------------------------------
    # Binned data: SPM, cross sections, fluxes
    # -------------------------------------------------------------------------

    multiplier_names = 'multiplier_names'
    try:
        for bindata in binned_data:
            attrnames = h5data.get(bindata+'/'+multiplier_names)
            # attr structure: 1-energy; 2-Ids; 3-multiplier_idx; 4-mean/std
            attr = h5data.get(bindata+'/binned')
            nIds = attr.shape[1]
            
            for idxId in range(nIds):
                for attridx, attrname in enumerate(attrnames): 
                    if idxId in data:
                        data[idxId].update({attrname.decode():
                                            attr[:, idxId, attridx, 0]})
                    else:
                        data[idxId] = {attrname.decode():
                                       attr[:, idxId, attridx, 0]}
    except:
        raise KeyError("Data for {} cannot be accessed".format(bindata))
        
    # -------------------------------------------------------------------------
    # Fission spectrum
    # -------------------------------------------------------------------------
    attrname = 'birth_spectrum'
    attrpath = 'tally/tallies/birth_spectrum'
    attr = h5data.get(attrpath+'/'+attrname)
    nIds = attr.shape[0]
    try:
        for idxId in range(nIds):
            if idxId in data:
                data[idxId].update({attrname: attr[idxId, :, 0]})
            else:
                data[idxId] = {attrname: attr[idxId, :, 0]}
    except:
        raise KeyError("Data for {} cannot be accessed"
                       .format(attrpath+'/'+attrname))

    # -------------------------------------------------------------------------
    # Average scattering angle
    # -------------------------------------------------------------------------
    attrname = 'mean_transfer_angle'
    attrpath = 'tally/tallies/mean_transfer_angle/binned'
    attr = h5data.get(attrpath)
    nIds = attr.shape[1]
    try:
        for idxId in range(nIds):
            if idxId in data:
                data[idxId].update({attrname: attr[:, idxId, 0]})
            else:
                data[idxId] = {attrname: attr[:, idxId, 0]}
    except:
        raise KeyError("Data for {} cannot be accessed"
                       .format(attrpath+'/'))

    # -------------------------------------------------------------------------
    # Probability Scattering Matrices
    # -------------------------------------------------------------------------
    attrname = 'scattering_prob_matrix'
    attrpath = 'tally/tallies/scatter_prob_matrix'
    # attr structure: 0-Id; 1- from energy; 2-to energy; 3-Pn order; 4-mean/std
    attr = h5data.get(attrpath+'/'+attrname)
    nIds = attr.shape[0]
    ordersPn  = attr.shape[3]
    try:
        for idxId in range(nIds):
            for Pn in range(ordersPn):
                if idxId in data:
                    data[idxId].update({attrname+str(Pn):
                                        attr[idxId, :, :, Pn, 0]})
                else:
                    data[idxId] = {attrname+str(Pn):
                                   attr[idxId, :, :, Pn, 0]}
    except:
        raise KeyError("Data for {} cannot be accessed"
                       .format(attrpath+'/'+attrname))

    # -------------------------------------------------------------------------
    # Create Neutron Production Matrices
    # -------------------------------------------------------------------------
    nIds = len(data)
    for idxId in range(nIds):
        for Pn in range(ordersPn):
            mtxPn = data[idxId][attrname+str(Pn)]
            mtxSPn = np.zeros(mtxPn.shape)
            for nxn in range(1, order_nxn):
                sig_nxn = transfer.format(nxn)
                if sig_nxn not in data[idxId]:
                    raise KeyError('{} does not exist'.format(sig_nxn))
                if flux not in data[idxId]:
                    raise KeyError('{} does not exist'.format(flux))
                for gFrom in range(mtxPn.shape[0]):
                    for gTo in range(mtxPn.shape[1]):
                        mtxSPn[gFrom, gTo] +=\
                            data[idxId][sig_nxn][gFrom] *\
                                nxn *\
                                mtxPn[gFrom, gTo] /\
                                    data[idxId][flux][gFrom]
            data[idxId].update({scattering+str(Pn): mtxSPn})
                                
    
    return data  


