"""readtemplate.py

Read the template file used to define how to print data.
This file contains certain regular-like expressions which are repeated
and replaced.

Created on Fri July 01 06:00:00 2022 @author: Dan Kotlyar
Last updated on Sat Aug 13 07:00:00 2022 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

List changes / additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
Repetition  - 07/01/2022 - DK
ReadTemplate  - 07/05/2022 - DK
_CleanDataCopy - 07/05/2022 - DK
_PopulateValues - 07/21/2022 - DK
_PopulateValues - 08/13/2022 - DK
"""

from pathlib import Path
from re import compile, IGNORECASE
import copy

import numpy as np

from xsInterface.errors.checkerrors import _isstr
from xsInterface.errors.customerrors import TemplateFileError

# General regular expressions needed for processing data
REP_START_REGEX = compile(r'"rep"{+', IGNORECASE)
REP_END_REGEX = compile(r'"rep"}+', IGNORECASE)
VARI_REGEX = compile(r'"vari"\{(.*?)\}')  # variable in
VARO_REGEX = compile(r'"varo"\{(.*?)\}')  # variable out
STATE_REGEX = compile(r'"state"\{(.*?)\}')  # state
VALS_REGEX = compile(r'"values"\{(.*?)\}')  # attribute
IDX_REGEX = compile(r'\[(.*?)\]')  # index inside parentheses
FRMT_REGEX = compile(r'\<(.*?)\>')  # format inside <> parentheses
FRMT_N_REGEX = compile(r'\<(.*?)\>\s*\d+')  # format inside <> parentheses and N
VALUES_REGEX = compile(r'"values"\{')  # used to identify "values"


# print formats
#VAR_FMT = "{:d}"  # users' defined variables
#ATTR_FMT = "{:5.5e}"  # attributes values
#STATE_FMT = "{:5.3f}"  # state values
#MAX_N_ROW = 5  # maximum number of values printed in a row


def ReadTemplate(tmplFile, universes, formats, univId=None):
    """Read the template input file defined by the user

    This function reads the template file and manipulates it to create
    a more explicit template file.

    Parameters
    ----------
    tmplFile : str
        name of the template input file
    universes : Universes object
        a container that stores unique universes having MultipleSets objects
    formats : dict
        defines the formatting of different output parameters types    
        {"state": "{:5.3f}", "var": "{:d}", "attr": "{:5.5e}", "nrow": 5}

    Raises
    ------
    TypeError
        If ``tmplFile`` is not str.
    OSError
        If the path ``tmplFile`` does not exist.

    """


    # check that `templateFile` variable is a string
    _isstr(tmplFile, "Input file")

    # read the file and return its content
    filePath = Path(tmplFile)
    if not filePath.is_file():
        raise OSError("The file {} does not exist.".format(tmplFile))

    with open(tmplFile, 'r') as fObject:
        dataRaw = fObject.readlines()

    # If user provides the univ Id - need to feed the name into the file
    if univId is not None:
        _isstr(univId, "Universe Id")
        dataRaw = _InsertUnivId(dataRaw, univId)
    
    # Identify locations within the file with text to be repeated
    pos = _RepetitiveBlocks(dataRaw)
    
    # Repeat blocks that should be repetitive
    dataDup = _DuplicateBlocks(dataRaw, pos)
    
    # Clean and replace variable text with values
    dataClean = _CleanDataCopy(dataDup, formats["var"])

    # Populate data
    dataPopulated = _PopulateValues(dataClean, universes, formats)

    return dataPopulated


def _InsertUnivId(dataIn, univId):
    """Insert the name of the universe into the datafile"""

    dataOut = []    
    for tline in dataIn:
        condvals = VALUES_REGEX.search(tline)
        if condvals is not None:
            tline = tline.replace(
                condvals.group(0), condvals.group(0)+univId+', ')
        dataOut.append(tline)
    return dataOut

def _PopulateValues(dataIn, universes, formats):
    """Replace states and attrs with corresponding states and atrrs values"""

    # correct format message    
    msg_exe = "<universe name>, <attr name>, <state name1>=<state val1>,..."\
              "[indices] <format>N"

    dataOut = []    
    for tline in dataIn:

        frmtPrnt = None
        nrowPrnt = None

        # Identify and execute an "values" line having an attribute
        attrline0 = VALS_REGEX.search(tline)
        if attrline0 is not None:
            attrline = attrline0.group(1)
            attrline = attrline.replace("\n", '')  # remove new line
            attrline = attrline.replace("\t", ' ')  # remove tabs
            attrline = attrline.replace(',', ' ')  # remove commas
            attrline = attrline.replace('=', ' ')  # remove = signs
            
            # -----------------------------------------------------------------
            # Obtain formatting requirements
            # -----------------------------------------------------------------
            indices = []
            if FRMT_N_REGEX.search(attrline) is not None:
                # the format included within <...>&nrow
                condFrmt = FRMT_N_REGEX.search(attrline)
                frmtPrnt = "{:" + condFrmt.group(1) + "}"
                nrowPrnt = condFrmt.group(0).split('>')[-1]
                attrline = attrline.replace(condFrmt.group(0), '')
            elif FRMT_REGEX.search(attrline) is not None:
                # the format included within <...> only
                condFrmt = FRMT_N_REGEX.search(attrline)
                frmtPrnt = "{:" + condFrmt.group(1) + "}"
                attrline = attrline.replace(condFrmt.group(0), '')
            if frmtPrnt is not None:
                try:
                    fmtCheck = frmtPrnt.format(444)
                except ValueError as detail:
                    if frmtPrnt != '{:s}':
                        msg0 = 'Provided format <{}> is not valid.\n{}'\
                        .format(frmtPrnt, tline)
                        raise TemplateFileError(msg0+'\n'+detail)
            if nrowPrnt is not None:
                try:
                    nrowPrnt = int(nrowPrnt)
                except ValueError as detail:
                    msg0 = 'Provided format <{}> is not valid.\n{}'\
                    .format(nrowPrnt, tline)
                    raise TemplateFileError(msg0+'\n'+detail)           

            # -----------------------------------------------------------------
            # Obtain indices
            # -----------------------------------------------------------------
            idxcond = IDX_REGEX.search(attrline)
            indices = []
            if idxcond is not None:
                # the content included within [...]
                idxmatch = idxcond.group(1)
                try:
                    # indices will be used to access the data
                    indices = [int(idx) for idx in idxmatch.split()]
                    indices = tuple(indices)
                except:
                    msg0 = 'The "values" command is not properly defined.\n{}'\
                        'Indices format <{}> is not allowed. Use integers.'\
                            'Follow the format:\n.'.format(tline, idxmatch)
                    raise TemplateFileError(msg0+msg_exe)
                # remove the indices from the line
                attrline = attrline[0:idxcond.span()[0]].split()
            else:
                attrline = attrline.split()

            # check that enough parameters are provided (at least univ & attr)
            if len(attrline) % 2 != 0 or len(attrline) < 2:
                msg0 = 'The "values" command is not properly defined.\n{}'\
                    'Follow the format:\n.'.format(tline)
                raise TemplateFileError(msg0+msg_exe)

            # Assign values
            univId = attrline[0]
            attr = attrline[1]
            states = {}
            for j in range(2, len(attrline), 2):
                if attrline[j] == 'history':
                    # history is the only non-numeric value
                    states[attrline[j]] = attrline[j+1]
                    continue
                try:
                    # 1st is key and 2nd is val
                    states[attrline[j]] = float(attrline[j+1])
                except:
                    msg0 = 'The "values" command is not properly defined.\n{}'\
                        '<{}> cannot be coverted to a number.'\
                        'Follow the format:\n.'.format(tline, attrline[j+1])
                    raise TemplateFileError(msg0+msg_exe)                    
            
            # Get values
            try:
                vals =\
                    universes.Values(univId, attr, **states)[attr]              
            except ValueError as detail:
                msg0 = 'The "values" command is not properly defined.\n{}\n{}'\
                        'Follow the format:\n.'.format(tline, detail)
                raise TemplateFileError(msg0+msg_exe)            

            if vals == []:
                msg0 = 'The "values" command is not properly defined.\n{}'\
                        '\nThe evaluated states do not exist: {}\n'\
                        .format(tline, states)
                raise TemplateFileError(msg0)    

            try:
                valsPrint = np.array([])  # array for printed values
                for val in vals:
                    if indices != []:
                        try:
                            valsPrint = np.append(valsPrint, val[indices])   
                        except:
                             
                             valsPrint = np.append(valsPrint,
                                                   val[list(indices)])
                    else:
                        valsPrint = np.append(valsPrint, val)
            except:
                msg0 = 'The "values" command is not properly defined.\n{}'\
                    '<{}> cannot be appended into an array.'\
                    '\nFollow the format:\n.'.format(tline, vals)
                raise TemplateFileError(msg0+msg_exe)

            if frmtPrnt is None:
                # Need to determine if the attr is a state or anything else
                states = universes.universes[univId][1]
                statesList = ['history', 'time'] + states._branchList
                if attr in statesList:
                    frmtPrnt = formats["state"]
                else:
                    frmtPrnt = formats["attr"]
            if nrowPrnt is None:
                nrowPrnt = formats["nrow"]  # default val of max number in row 
          
            # format the values to be printed
            tlines = _Array2tlines(tline, attrline0.group(0), valsPrint,
                                   nrowPrnt, frmtPrnt)
            
            for tline in tlines:
                dataOut.append(tline)
            
        else:            
            # Copy (and if needed replace line) to a clean data list
            dataOut.append(tline)
    return dataOut


def _CleanDataCopy(dataIn, fmt0):
    """Create a new data copy with user's variables assessed and replaced"""
    # all the local variables defined in this current function/method
    localVarsList = ['dataIn', 'fmt0', 'fmt', 'localVarsList', 'msgExe',
                     'fmtCheck', 'dataClean', 'tline', 'condRep0', 'condRep1',
                     'condVarI', 'condVarO', 'locVariables', 'strsExe',
                     'strsComplete', 'msg0',
                     'iexecInLine', 'tline1', 'istrExe', 'strExe', 
                     'prevLocals', 'currLocals', 'varLocal'] 
    msgExe = 'Execution cannot be performed in line:\n'
    
    # check that the format variable is defined properly
    _isstr(fmt0, "Variable format")
    try:
        fmtCheck = fmt0.format(444)
    except:
        msg0 = 'Variable format <> is not properly defined.\nValid example: '\
        '{:d}'.format(fmt0)
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
                currLocals = locals()  # local variables after execution
                varLocal = _LocalVariables(currLocals, localVarsList)

            except:
                msg0 = msgExe + '{}\n'.format(tline) +\
                    'exe command: {}\n'.format(condVarI.group(1)) 
                raise TemplateFileError(msg0)
            if varLocal == []:
                msg0 = 'The name for varibale {} is not allowed.\nPlease '\
                    'select a different name.'.format(condVarI.group(0))
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
                # check if format is provided
                condFrmt = FRMT_REGEX.search(strExe)
                if condFrmt is not None:
                    fmt = "{:" + condFrmt.group(1) + "}"
                    strExe = strExe[0:condFrmt.span()[0]]
                    try:
                        fmtCheck = fmt.format(444)
                    except ValueError as detail:
                        if fmt != '{:s}':
                            msg0 = 'Provided format <{}> is not valid.\n{}'\
                            .format(fmt, tline)
                            raise TemplateFileError(msg0+'\n'+detail)  
                else:
                    fmt = fmt0  # default variable format
                try:
                    # evaluate expression
                    evalexpr = eval(strExe)
                    if isinstance(evalexpr, (np.ndarray, list)):
                        fmt = (fmt+' ')*len(evalexpr)
                        fmt = fmt.rstrip()
                        # replace execution occurrences
                        tline =\
                            tline.replace('{}'.format(strsComplete[istrExe]),
                                          fmt.format(*evalexpr))
                    else:
                        # replace execution occurrences
                        tline =\
                            tline.replace('{}'.format(strsComplete[istrExe]),
                                          fmt.format(evalexpr))
                except ValueError as detail:
                    msg0 = msgExe + '{}\n'.format(tline) +\
                        'exe command: {}\n{}\n'.format(strExe,detail)
                    raise TemplateFileError(msg0)
                except TypeError as detail:
                    msg0 = msgExe + '{}\n'.format(tline) +\
                        'exe command: {}\n{}\n'.format(strExe,detail) 
                    raise TemplateFileError(msg0)
                except IndexError as detail:
                    msg0 = msgExe + '{}\n'.format(tline) +\
                        'exe command: {}\n{}\n'.format(strExe,detail) 
                    raise TemplateFileError(msg0)
                except NameError as detail:
                    msg0 = msgExe + '{}\n'.format(tline) +\
                        'exe command: {}\n{}\n'.format(strExe,detail)
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
    

# -----------------------------------------------------------------------------
#                            Supplementary Functions
# -----------------------------------------------------------------------------


def _LocalVariables(currLocals, funcList):
    """get the new local variable defined after the user's execution command"""

    currList = []
    for key in currLocals.keys():
        if key not in funcList:
            currList.append(key)

    return currList


def _Array2tlines(tline, origstr, valsarray, nrow, frmt):
    """Convert original string in a line to multiple lines given by an array"""
    # tline: original line
    # origstr: original string to be replaced/removed
    # valsarray: values in an array
    # nrow: maximum number of values in a row
    # frmt: the format of the 

    tlines = []
    valsremain = copy.deepcopy(valsarray)
    replaceFlag = True  # flag that indicates if the original line is replaced
    while 1:
        if len(valsremain) > nrow:
            valsrow = valsremain[0:nrow]  # values to be printed a row
            valsremain = valsremain[nrow:]  # remaining vals for following rows
        else:
            valsrow = valsremain
            valsremain = []

        str0 = ''  # empty string to be appended
        for val in valsrow:
            if isinstance(val, str):
                str0 += '{} '.format(val)
            else:
                str0 += frmt.format(val) + ' '
        
        if replaceFlag:
            tlines.append(tline.replace(origstr, str0))
            replaceFlag = False
        else:
            str0 += '\n'
            tlines.append(str0)

        # all values are printed
        if len(valsremain) == 0:
            break  # the while loop

    return tlines