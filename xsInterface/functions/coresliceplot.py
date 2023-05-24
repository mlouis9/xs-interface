# -*- coding: utf-8 -*-
"""coresliceplot.py

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


GEOM_MARKERS = {"hexagonal": "h", "square": "s", "circular": "o"}


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