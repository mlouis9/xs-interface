# -*- coding: utf-8 -*-
"""
Spyder 

This is a temporary script file.
"""


#import os
import numpy as np

#arr = os.listdir()


nchs = 73
nlayers = 22
nfiles = nchs * nlayers
filenames = [None]*nfiles
    
channels = np.linspace(1, 56, 56, dtype=int)
layers = np.linspace(0, 21, 22, dtype=int)

refChannels = np.linspace(0, 16, 17, dtype=int)


# CORE
c = 0
for ch in channels:
    for layer in layers:
        filenames[c] = 'xs_' + str(ch) + '_' + str(layer) + '_u' + str(ch) + '_' + str(layer)  + '.dat'
        c += 1

for ch in refChannels:
    for layer in layers:
        filenames[c] = 'xs_R' + str(ch) + '_' + str(layer) + '_uR' + str(ch) + '_' + str(layer) + '.dat' 
        c += 1
