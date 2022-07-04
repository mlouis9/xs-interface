"""readtemplate.py

Read the template file used to define how to print data.
This file contains certain regular-like expressions which are repeated
and replaced.

Created on Fri July 01 06:00:00 2022 @author: Dan Kotlyar
Last updated on Fri July 01 06:00:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

List changes / additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
Repetition  - 07/01/2022 - DK


"""

from pathlib import Path
from re import compile, IGNORECASE
import copy

import numpy as np

from xsInterface.errors.checkerrors import _isstr
from xsInterface.errors.customerrors import TemplateFileError

# General regular expressions needed for processing data
SPECIAL_CHAR = compile(r'[\?\$\&\@\~\<\>\`]')  # special character
REP_START_REGEX = compile(r'"rep"{+', IGNORECASE)
REP_END_REGEX = compile(r'"rep"}+', IGNORECASE)
VARI_REGEX = compile(r'"vari"\{(.*?)\}')  # variable in
VARO_REGEX = compile(r'"varo"\{(.*?)\}')  # variable out

# print formats
VAR_FORMAT = "{:d}"

def ReadTemplate(templateFile, varFormat=VAR_FORMAT):
    """Read the template input file defined by the user

    This function reads the template file and manipulates it to create
    a more explicit template file.

    Parameters
    ----------
    templateFile : str
        name of the input file

    Raises
    ------
    TypeError
        If ``inputFile`` is not str.
    OSError
        If the path ``inputFile`` does not exist.

    """


    # check that `templateFile` variable is a string
    _isstr(templateFile, "Input file")

    # read the file and return its content
    filePath = Path(templateFile)
    if not filePath.is_file():
        raise OSError("The file {} does not exist.".format(templateFile))

    with open(templateFile, 'r') as fObject:
        dataRaw = fObject.readlines()
    
    # Identify locations within the file with text to be repeated
    pos = _RepetitiveBlocks(dataRaw)
    
    # Repeat blocks that should be repetitive
    dataDup = _DuplicateBlocks(dataRaw, pos)
    
    # Clean and replace variable text with values
    dataClean = _CleanDataCopy(dataDup, varFormat)
        
    return dataClean


def _CleanDataCopy(dataIn, fmt):
    """Create a new data copy with user's variables assessed and replaced"""
    
    msgExe = 'Execution cannot be performed in line:\n'
    
    # check that the format variable is defined properly
    _isstr(fmt, "Variable format")
    try:
        fmtCheck = fmt.format(444)
    except:
        msg0 = 'Variable format <> is not properly defined.\nValid example: '\
        '{:d}'.format(fmt)
        raise TemplateFileError(msg0)            
    
    dataClean = []
    for tline in dataIn:    

        # No need to copy the repetition strings
        condRep0 = REP_START_REGEX.search(tline)
        condRep1 = REP_END_REGEX.search(tline)
        if (condRep0 or condRep1) is not None:
            continue
        
        # Identify and execute a variable (no need to copy)
        condVarI = VARI_REGEX.search(tline)
        if condVarI is not None:
            try:
                exec(condVarI.group(1))
            except:
                msg0 = msgExe + '{}\n'.format(tline) +\
                    'exe commad: {}\n'.format(condVarI.group(1)) 
                raise TemplateFileError(msg0)
            continue
        
        # Identify, execute, and replace a variable with value
        condVarO = VARO_REGEX.search(tline)
        if condVarO is not None:
            # collect all the execution strings within the same text line
            strsExe = [condVarO.group(1)]  # execution only string
            strsComplete = [condVarO.group(0)]  # full strings
            iexecInLine = 0
            tline1 = tline
            while iexecInLine < 999:
                tline1 = tline1[condVarO.span()[1]:]
                condVarO = VARO_REGEX.search(tline1)
                if condVarO is not None:
                    strsExe.append(condVarO.group(1))
                    strsComplete.append(condVarO.group(0))
                else:
                    break
                # no more than 1000 variables in a line (just in case)
                iexecInLine += 1
            
            # execute all the exe strings within the line
            for istrExe, strExe in enumerate(strsExe):
                try:
                    # replace execution occurrences
                    tline = tline.replace('{}'.format(strsComplete[istrExe]),
                                          fmt.format(eval(strExe)))
                except:
                    msg0 = msgExe + '{}\n'.format(tline) +\
                        'exe commad: {}\n'.format(strExe) 
                    raise TemplateFileError(msg0)

                
                # Copy (and if needed replace line) to a clean data list
        dataClean.append(tline)
    
    # a new clean data list is returned
    return dataClean
        
        
            

def _DuplicateBlocks(dataIn, pos):
    """Duplicate/copy blocks that need to be repeated"""
    pos1 = copy.deepcopy(pos)    
    # sort pos1 according to the level of appearance in text file
    idxsort = np.argsort(pos[:, 0])
    pos1 = pos1[idxsort[::-1], :]

    # text line after processing
    dataOut = copy.deepcopy(dataIn)
    
    # Identify the new text locations where the duplicate text is inserted
    for i in range(pos.shape[0]):
        
        # duplicate the current level
        data0 = dataOut[pos1[i, 1]:pos1[i, 2]+1]*pos1[i, 3]
        
        # replace the original section with the number of repetitions
        dataOut = dataOut[0:pos1[i, 1]] + data0 +  dataOut[pos1[i, 2]+1:]
        
        # change the indecises
        addNrows = (pos1[i, 2] - pos1[i, 1] + 1) * (pos1[i, -1]-1)
        pos1[:, 1] = np.where(pos1[:, 1] < pos1[i, 1],
                              pos1[:, 1], pos1[:, 1] + addNrows)
        pos1[:, 2] = np.where(pos1[:, 2] < pos1[i, 2],
                              pos1[:, 2], pos1[:, 2] + addNrows)
    
    return dataOut

def _RepetitiveBlocks(dataIn):
    """Identify blocks that should be repeated and create multiple of these"""

    # messages definitions
    msgRep = "Repetition block not defined properly\n"  
       
    # positions marks the location of repetitive text within the file
    #    1        2          3          4
    # [level, start-line, end-line, #repetitions]
    pos = np.zeros((1, 4), dtype=int)   
    
    for iline, tline in enumerate(dataIn):

        # index to indicate the last unclosed repetition
        idxLvl = pos.shape[0]-1
        for i in range(pos.shape[0]-1, 0, -1):
            if pos[i, 2] == 0:
                break
            else:
                idxLvl -= 1
                

        # New repetetive block
        str0 = REP_START_REGEX.search(tline)
        if str0 is not None:
            currLvl = str0[0].count('{') - 1  # determine the level
 
            # number of repetitions
            try:
                nrep = int(tline[str0.span()[1]:])
            except ValueError:
                nrep = 1

            # Expected level must be defined first
            if currLvl < pos[idxLvl, 0] or currLvl > pos[idxLvl, 0] + 1:
                msg0 = "The repetition in line #{:d}: {}\ncannot be defined "\
                "before defining: {}\n"\
                .format(iline+1, dataIn[iline], '\rep'+'{'*(pos[idxLvl, 0]+1)) 
                raise TemplateFileError(msgRep+msg0)

                
            # current identifier
            pos0 = np.array([[currLvl, iline, 0, nrep]], dtype=int)
            
            if (pos[0, :] == 0).all():
                pos = pos0
            else:
                pos = np.append(pos, pos0, axis=0)

        # Close exisiting repetitive block
        str0 = REP_END_REGEX.search(tline)
        if str0 is not None:
            currLvl = str0[0].count('}') - 1 # determine the level
 
            # Wrong level is atempted to be closed
            if pos[idxLvl, 0] != currLvl:
                msg0 = "Closing repetition in line #{:d}: {}\ncannot be "\
                "performed before closing repetition on line #{:d}\n"\
                .format(iline+1, dataIn[iline], pos[idxLvl, 1]+1) 
                raise TemplateFileError(msgRep+msg0)
            
            pos[idxLvl, 2] = iline
         
    # if positions table is incomplete with all identifiers
    if not (pos[:, 1:] > 0).all():
        msg1 = ''
        for idx in range(pos.shape[0]):
            if pos[idx, 2] == 0:
                msg1 = msg1 + '\nline #{} has no closure.'\
                    .format(pos[idx, 1]+1)
        
        raise TemplateFileError(msgRep+msg1)
            
    return pos
    
    
    
    
