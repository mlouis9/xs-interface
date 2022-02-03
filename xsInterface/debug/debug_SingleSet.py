# -*- coding: utf-8 -*-
"""
Created on Thu Feb  3 09:14:40 2022

@author: 17066
"""

import os
os.chdir(r"C:\Users\17066\xs-interface\xsInterface\containers")

from singleset import *
import numpy as np

# Debug initialization
xsLabel = {'abs':'reduced order absorption cross section',
           'fiss':'fission cross section',
           'tanspxs':'trasnport cross section'}
dataLabel = {}
set0 = SingleSet(dataLabel,xsLabel,3)

# Debug .add()
rabsxs   = np.array([0.0222,0.011,0.001])
fissxs   = np.array([0.0111,0.021,0.002])
transpxs = np.array([0.0272,0.033,0.002])
flux     = 1e14*np.array([0.9,0.05,0.05])
set0.add(np.ndarray,rabsxs=rabsxs,fissxs=fissxs,transpxs=transpxs,flux=flux)

# Debug.get()
xsDict_uncondensed = set0.get('rabsxs','fissxs','transpxs')

# Debug .condense()
set0.condense('rabsxs','fissxs','transpxs')
xsDict_condensed = set0.get('rabsxs','fissxs','transpxs')