# -*- coding: utf-8 -*-
"""plotters.py

Diffrenet plotting capabilities:

(1)
    


(2)
    A method to plot various results/inputs/cross sections as a slice 
    (i.e., radial map) of the core.

Created on Tue May 23 05:30:00 2023 @author: Dan Kotlyar
Last updated on Tue May 23 05:30:00 2023 @author: Dan Kotlyar
email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
coreSlicePlot - 05/23/2023 - DK

"""

import numpy as np
import pandas as pd
from matplotlib import pyplot
import matplotlib.pyplot as plt
from matplotlib import rcParams

from xsInterface.errors.checkerrors import _isnumber, _isbool, _isstr

rcParams['figure.dpi'] = 300
GEOM_MARKERS = {"hexagonal": "h", "square": "s", "circular": "o"}
FONT_SIZE = 16
MARKER_SIZE = 6



def Plot1d(xvalues, yvalues, flip=False, xlabel=None, ylabel=None, norm=1,
           fontsize=FONT_SIZE, markers="--*", markerfill=False,
           markersize=MARKER_SIZE):
    """plot the 1-dim data of a property over multiple channels/layers

    The use of this method is similar to the ``getvalues`` method.
    It is important to note that not all the values have axial layers.

    Parameters
    ----------
    xvalues : array
        x-axis values, e.g., heights in cm.
    yvalues : dict or 1-dim array
        y-axis values where keys represent channels and values are data arrays 
    channels : str or list of str
        identifier/s of the channel
    flip : bool
        boolean flag to indicate whether results should flipped
    layers : int, list of int, ndarray of int
        identifier/s of the axial layer
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


    # check variable types
    _isnumber(fontsize, "Font size")
    _isnumber(markersize, "Marker size")
    _isbool(flip, "flip results axis")
    _isbool(markerfill, "Marker fill option")
    _isnumber(norm, "Normalization factor")
    
    if not isinstance(markers, list):
        _isstr(markers, "Markers")
        markers = [markers] * len(yvalues)
    elif isinstance(markers, list):
        markers = markers * len(yvalues)

    if ylabel is not None:
        _isstr(ylabel, "ylabel")
    else:
        ylabel = ""

    if xlabel is not None:
        _isstr(xlabel, "xlabel")
    else:
        xlabel = ""

    if markerfill:
        mfc = "white"  # marker fill color
    else:
        mfc = None

    plt.ylabel(ylabel)
    plt.xlabel(xlabel)
    # plot the results for multiple channels
    if isinstance(yvalues, dict):
        ich = 0
        for ch, vals in yvalues.items():
            vals = vals if not flip else vals[::-1]
            vals = np.array(vals)/norm
            plt.plot(xvalues, vals, markers[ich],
                     mfc=mfc, ms=markersize)
            ich += 1
        plt.legend(yvalues.keys())
    else:
        plt.plot(xvalues, yvalues, markers[0], mfc=mfc, ms=markersize)
    plt.grid()
    plt.rc('font', size=fontsize)      # text sizes
    plt.rc('axes', labelsize=fontsize)  # labels
    plt.rc('xtick', labelsize=fontsize)  # tick labels
    plt.rc('ytick', labelsize=fontsize)  # tick labels


def coreSlicePlot(radmap, values, label=None, shift=None, geomarker='s',
                  norm=1.0,
                  spacesize=1.0, markersize=500, cmap='viridis',
                  text=True, textsize=7, textcolor="w", textweight="bold",
                  precision=".2f", edge=2.5, chnls2Ignore=None,
                  includeRows=None, includeCols=None):
    """Plot radial selected property distribution

    Parameters
    ----------
    label : str
        description of the output variable. A default exist for every
        parameter.
    shift : list of int
        shift rows by increments of 0.5 or 1 (negative or positive)
    geomarker : str
        marker type {"hexagonal": "h", "square": "s", "circular": "o"}
    norm : float
        data normalization factor
    spacesize : float
        determines the space between elements. The larger the number the
        the larger is the spacing.
    markersize : float
        hexagon/square/circles marker/shape size
    cmap : str
        color map
    text : bool
        flag to indicate if the text should be printed or not
    textsize : float
        size of the text
    textcolor : str
        color of the text
    textweight : str
        font weight of the text
    precision : str
        defines the precision of printing inside the markers.
        e.g., ".2f", ".5e" - must follow the format allowed in python.

    Examples
    --------
    >>> coreSlicePlot('TbIn', 3, shift=[0, -0.5, 0])

    """



    if shift is not None and len(shift) != len(radmap):
        raise ValueError("The length of shift must be {}, and not {}"
                         .format(len(radmap), len(shift)))
    if shift is None:
        shift = np.zeros(len(radmap))

    if label is None:
        label = " "

        
    # Store the position of the fuel assemblies
    x = []
    y = []
    vals = []
    for idxrow, row in enumerate(radmap):
        for idxcol, col in enumerate(row):
            condIgnore = False
            if col is not None and chnls2Ignore is not None and chnls2Ignore in col:
                condIgnore = True
            if col is not None and not condIgnore:
                if includeRows is None and includeCols is None:
                    x.append(idxrow)  # store row/column positions
                    y.append(idxcol + shift[idxrow])
                    # add the value of a specific attribute
                    vals.append(values[idxrow][idxcol]/norm)
                else:
                    if idxrow >= includeRows[0] and idxrow <= includeRows[1] \
                        and idxcol >= includeCols[0] and\
                            idxcol <= includeCols[1]:
                                x.append(idxrow)  # store row/column positions
                                y.append(idxcol + shift[idxrow])
                                # add the value of a specific attribute
                                vals.append(values[idxrow][idxcol]/norm)
                
    # Define the boundaries of the figure
    xmin = min(x)
    xmax = max(x)
    ymin = min(y)
    ymax = max(y)
    
    zmin = min(xmin, ymin)
    zmax = max(xmax, ymax)
    dz = (zmax - zmin)/spacesize
    
    xlim = (xmin-edge*dz, xmax+edge*dz)
    ylim = (ymin-edge*dz, ymax+edge*dz)


    # define the data dictionary
    valsDict = {"x": x, "y": y, label: vals}
    data = pd.DataFrame(valsDict)

    ax = data.plot(x='y', y='x', kind='scatter', xlim=xlim, ylim=ylim,
                    c=label, cmap=cmap,
                    marker=geomarker, s=markersize)
    if text:
        for pos in data.index:
            ax.text(data['y'][pos], data['x'][pos],
                    "{1:{0}}".format(precision, data[label][pos]),
                    fontsize=textsize, verticalalignment='center',
                    horizontalalignment='center', color=textcolor,
                    fontweight=textweight)
    pyplot.axis('off')