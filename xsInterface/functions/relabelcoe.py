# -*- coding: utf-8 -*-
"""relabelcoe

The function allows to rename the branching labels set as individual
branches, e.g. ``f600b0dens630``, to a more structured manner,
which then allows the xsInterface package to work with the modified .coe files
as it recognizes the new labeling,
e.g. f600 dens630 b0

Created on Tue May 12 09:46:21 2022 @author: Dan Kotlyar
Last modified on Mon Feb 27 04:45:00 2023 @author: Dan Kotlyar
@author: Dan Kotlyar
"""

from os import path


def coeRelabel(origCoeFile, modCoeFile, inpLabels):
    """creates a new .coe file with modified lables for all the branches

    Reads the original .coe file used to generate the cross sections and
    creates a new/modified .coe file with labels that are suitable for
    the ``xsInterface package``.

    Parameters
    ----------
    origCoeFile : str
        name of the original .coe file
    modCoeFile : str
        name of the modified .coe file
    inpLabels : str
        The name of the input file that contains the description of the labels

    Raises
    ------
    IOError
        If the ``origCoeFile`` or ``inpLabels`` file do not exist.

    Examples
    --------
    >>> coeRelabel(origCoeFile, modCoeFile, inpLabels)

    """

    # reads in the original and modified name tags / labels
    nvars, brLabels = _readBranchLables(inpLabels)

    # the new labels are used to update the original .coe file
    _modifiedCoeFile(origCoeFile, modCoeFile, brLabels, nvars-1)


def _modifiedCoeFile(origCoeFile, modCoeFile, brLabels, nvars):
    """creates a new .coe file with modified lables for all the branches

    Reads the original .coe file used to generate cross sections and
    creates a new/modified .coe file with labels that are suitable for
    the ``xsInterface package``.

    Parameters
    ----------
    origCoeFile : str
        name of the original .coe file
    modCoeFile : str
        name of the modified .coe file
    brLabels : dict
        The keys represent the original labels and the values represent the
        names/labels of the separate perturbations.
    nvars : int
        number of dependencies, i.e. fuel, coolant temperature

    Raises
    ------
    TypeError
        If either ``origCoeFile`` or ``modCoeFile``  is not a string.
        If ``nvars`` is not an integer.

    IOError
        If the ``origCoeFile`` file does not exist. If the name of the input
        and output files is identical.

    Examples
    --------
    >>> _modifiedCoeFile(origCoeFile, modCoeFile, brLabels, nvars)

    """

    if not isinstance(origCoeFile, str):
        raise TypeError("!!!origCoeFile must be a string and not {} "
                        .format(type(origCoeFile)))
    if not isinstance(modCoeFile, str):
        raise TypeError("!!!origCoeFile must be a string and not {} "
                        .format(type(modCoeFile)))
    if not isinstance(nvars, int):
        raise TypeError("!!!nvars must be an integer and not {} "
                        .format(type(nvars)))

    if origCoeFile == modCoeFile:
        raise IOError("!!!Names of the modified {} and original {} flies "
                      "must ne different".format(modCoeFile, origCoeFile))

    if not path.exists(origCoeFile):
        raise IOError("!!!The file {} does not exist".format(origCoeFile))

    # Read in the original .coe file
    with open(origCoeFile, 'r') as fileOrig:
        filedata = fileOrig.read()

    # Replace the target string
    for key in brLabels.keys():
        filedata = filedata.replace('1 ' + key, str(nvars) + ' ' + brLabels[key])

    # Write the file out again
    with open(modCoeFile, 'w') as fileMod:
        fileMod.write(filedata)


def _readBranchLables(inpLabels):
    """read the labels that were defined individually for the .coe file

    The function reads an input file provided by the user.
    This file contains the original lables used to create all the branches
    individually. Each non-empty row in the file starts with the original
    label, and followed by the modified labeling for each perturbation,
    e.g. f600b0dens630 f600 b0 dens630

    Parameters
    ----------
    inpLabels : str
        The name of the input file that contains the description of the labels

    Returns
    -------
    brLabels : dict
        The keys represent the original labels and the values represent the
        names/labels of the separate perturbations.

    Raises
    ------
    TypeError
        If ``inpLabels`` is not a string.
    IOError
        If the file does not exist
    ValueError
        If the number of entries per perturbation is smaller than two.
        If there are no pertirbations defined in the file.

    Examples
    --------
    >>> _readBranchLables(inpLabels)
    {'f600b0dens630': 'f600 b0 dens630',
     'f600b0densNom': 'f600 b0 nom',...

    """

    if not isinstance(inpLabels, str):
        raise TypeError("!!!inpLabels must be a string and not {} "
                        .format(type(inpLabels)))

    if not path.exists(inpLabels):
        raise IOError("!!!The file {} does not exist".format(inpLabels))

    nvals = None  # number of dependencies (e.g. fuel, density)
    with open(inpLabels) as fid:
        allLabels = []
        for tline in fid:
            if not tline.strip():  # if the line is empty continue
                continue
            else:
                vals = tline.split()
                nvals = len(vals)
                if nvals < 2:
                    raise ValueError("!!!At least two entries must exist and "
                                     "not {}".format(vals))

                if allLabels and len(vals) != len(allLabels[-1]):
                    raise ValueError("!!!The number of entries should be {} and "
                                     "not {}".format(len(allLabels[-1]), vals))
                allLabels.append(vals)
    if allLabels:
        nper = len(allLabels)
    else:
        raise ValueError("!!!No perturbations were defined in {}"
                         .format(inpLabels))

    # obtain the list for the original and modified labels
    origLabels, modLabels = _reLabel(allLabels, nvals, nper)

    if len(origLabels) != len(modLabels):
        raise ValueError("!!!The number of original labels {}, and modified {} "
                         "is not the same"
                         .format(len(origLabels), len(modLabels)))

    brLabels = {}  # empty dictionary to store the original and modified names
    for idx, key in enumerate(origLabels):
        brLabels[key] = modLabels[idx]

    return nvals, brLabels


def _reLabel(listLabels, nVar, totPert):
    """identifies potential errors in the list

    Error checking to cover if the original label is repeated more than once.
    In addition, the function checks if the number of each perturbation
    sums to the total number of perturbations defined in the problem.

    Parameters
    ----------
    listLabels : list (2D)
        A list that contains all the labels. The first column represents
        the name of the original label. The following columns represent
        the labeling for the individual perturbations.
    nVar : int
        Number of perturbation dependencies
    totPert : int
        Total number of perturbations

    Returns
    -------
    origLabels : list
        The names/labels used to define the original perturbations
    modLabels : list
        The names/labels used for the modified perturbations

    Raises
    ------
    ValueError
        If the same branching is defined multiple times.
        Total number of unique perturbations is not identical to the
        total number of perturbations defined by the user.

    """

    origLabels = []  # the name of the original branchings
    modLabels = []  # the name of the modified branchings

    pertLabels = {}  # to store the unique lables for EACH perturbation
    for idx in range(1, nVar):
        pertLabels.update({idx: []})

    for ipert in range(len(listLabels)):
        # check that the original labels are not defined multiple times
        if listLabels[ipert][0] not in origLabels:
            origLabels.append(listLabels[ipert][0])
        else:
            raise ValueError("!!!The branching {} is defined multiple time "
                             .format(listLabels[ipert][0]))

        # add the new modified name
        modLabels.append(' '.join(listLabels[ipert][1:]))

        # traverse over the perturbations
        for idx in range(1, nVar):
            # For each perturbation/column append only if uniqe
            if listLabels[ipert][idx] not in pertLabels[idx]:
                pertLabels[idx].append(listLabels[ipert][idx])

    numPert = 1
    for idx in range(1, nVar):
        numPert *= len(pertLabels[idx])

    if numPert != totPert:
        raise ValueError("!!!{} unique perturbations were predicted, but {} were "
                         "given in the file".format(numPert, totPert))

    return origLabels, modLabels
