# -*- coding: utf-8 -*-
"""
Created on Tue Feb  8 12:45:06 2022

@author: 17066
"""

def _propTypes():
    return ['absorption','fission','transport','flux','eneCutoffs']

def _propShapes():
    return {'absorption':'vec',
            'fission'   :'vec',
            'transport' :'vec',
            'flux'      :'vec',
            'eneCutoffs':'cut',
            'scattering':'mat'}