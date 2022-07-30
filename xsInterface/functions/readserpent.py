"""readserpent.py

Read the data using the ``serpentTools`` package.

Created on Sat July 30 05:00:00 2022 @author: Dan Kotlyar
Last updated on Sat July 30 07:00:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

List changes / additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
ReadCoefFiles  - 07/30/2022 - DK


"""

from pathlib import Path

import serpentTools

from xsInterface.errors.checkerrors import _isstr


def ReadHistoryFiles(fnames):
    """Read multiple serpent output .coe fils

    Parameters
    ----------
    fnames : dict
        .coe file directory path + file name
        for universes with various history branches
        structure of the dictionary: {universe:{history:filename}}
        

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

            print("... Reading coe file for univ= <{}>, hisotry <{}> ..."
                  .format(univUsrId, historyId))
            coedata = ReadCoefFile(coeFile)
        
            for univ in coedata:
                univId = univUsrId + univ
                if univId in data:
                    data[univId].update({historyId: coedata[univ]})
                else:
                    data.update({univId:{historyId: coedata[univ]}})
            
    return data
    



def ReadCoefFile(coeFile):
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
    coe0 = serpentTools.read(coeFile)  # coe is a data container
    
    # Structure of the data container
    # univId: {timeIdx: {state: univData}}   
    data = {}

    # loop over all the branches
    for brKeys, brData in coe0.items():
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
            data[univId][step][brKeys] = univData
                     
    return data
                
            


