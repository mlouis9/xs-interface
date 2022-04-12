# -*- coding: utf-8 -*-
"""ex_energycond.py

Example:
Energy condensation on multi-group maco- and micro- parameters.
The condensation procedure can be applied on vectors, such as absorption xs,
as well as on scattering matrices.


Created on Mon Apr 11 11:00:00 2022 @author: Dan Kotlyar
Last updated on Mon Apr 11 11:30:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu
"""

import numpy as np

from xsInterface.functions.energycondensation import EnergyCondensation
from xsInterface.examples.xs_data_condensation import MICRO_E, NG, ABS, SP0,\
    flx

# vector condensation
prdAbs, condE =\
    EnergyCondensation(ndim=1, ng=NG, boundsE=MICRO_E, attr=ABS, flux=flx,
                       cutoffE=[0.625e-06])

# Expected values (pre-generated in advance)
refAbs = np.array([1.00889E-02, 1.15010E-01])

# Percent difference
diffAbs = 100*(1-prdAbs/refAbs)

# matrix condensation
prdSct, condE =\
    EnergyCondensation(ndim=2, ng=NG, boundsE=MICRO_E, attr=SP0, flux=flx,
                       cutoffE=[0.625e-06])

# Expected values (pre-generated in advance)
refSct = np.array([[4.80685E-01, 1.61547E-02],  # 1-->1, 1-->2
                   [2.10527E-03, 1.18859E+00]])  # 2-->1, 2-->2

# Percent difference
diffAbs = 100*(1-prdSct/refSct)
