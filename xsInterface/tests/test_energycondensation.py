# -*- coding: utf-8 -*-
"""test_energycondensation.py

py Test:
Energy condensation on multi-group maco- and micro- parameters.
The condensation procedure can be applied on vectors, such as absorption xs,
as well as on scattering matrices.


Created on Mon Apr 11 11:00:00 2022 @author: Dan Kotlyar
Last updated on Mon Apr 11 11:30:00 2022 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu
"""

import pytest

import numpy as np

from xsInterface.functions.energycondensation import EnergyCondensation
from xsInterface.examples.xs_data_condensation import MICRO_E, NG, ABS, NSF,\
    flx, SP0

prdAbs =\
    EnergyCondensation(ndim=1, ng=NG, boundsE=MICRO_E, attr=ABS, flux=flx,
                       cutoffE=[0.625e-06])

# Expected values (pre-generated in advance)
refAbs = np.array([1.00889E-02, 1.15010E-01])

# Percent difference
diffAbs = 100*(1-prdAbs/refAbs)


def test_absorption():
    """Errors in input parameters"""

    prdAbs, condE =\
        EnergyCondensation(ndim=1, ng=NG, boundsE=MICRO_E, attr=ABS, flux=flx,
                           cutoffE=[0.625e-06])
    # Expected values (pre-generated in advance)
    refAbs = np.array([1.00889E-02, 1.15010E-01])
    assert prdAbs == pytest.approx(refAbs, rel=0.01)


def test_nufission():
    """Errors in input parameters"""

    prdNsf, condE =\
        EnergyCondensation(ndim=1, ng=NG, boundsE=MICRO_E, attr=NSF, flux=flx,
                           cutoffE=[0.625e-06])
    # Expected values (pre-generated in advance)
    refNsf = np.array([7.22598E-03, 1.41791E-01])
    assert prdNsf == pytest.approx(refNsf, rel=0.01)


def test_scattering():
    """Errors in input parameters"""

    # matrix condensation
    prdSct, condE =\
        EnergyCondensation(ndim=2, ng=NG, boundsE=MICRO_E, attr=SP0, flux=flx,
                           cutoffE=[0.625e-06])

    # Expected values (pre-generated in advance)
    refSct = np.array([[4.80685E-01, 1.61547E-02],  # 1-->1, 1-->2
                       [2.10527E-03, 1.18859E+00]])  # 2-->1, 2-->2

    assert prdSct == pytest.approx(refSct, rel=0.01)


def test_badParameters():
    """Errors in input parameters"""

    with pytest.raises(TypeError, match="Dimensions*"):
        EnergyCondensation(ndim="BAD_DIM", ng=NG, boundsE=MICRO_E,
                           attr=ABS, flux=flx, cutoffE=[0.625e-06])

    with pytest.raises(TypeError, match="Number*"):
        EnergyCondensation(ndim=1, ng="BAD_NG", boundsE=MICRO_E,
                           attr=ABS, flux=flx, cutoffE=[0.625e-06])

    with pytest.raises(TypeError, match="Energy boundaries*"):
        EnergyCondensation(ndim=1, ng=NG, boundsE="NOT_ARRAY",
                           attr=ABS, flux=flx, cutoffE=[0.625e-06])

    with pytest.raises(TypeError, match="Attribute*"):
        EnergyCondensation(ndim=1, ng=NG, boundsE=MICRO_E,
                           attr="NOT_ARRAY", flux=flx, cutoffE=[0.625e-06])

    with pytest.raises(TypeError, match="Flux*"):
        EnergyCondensation(ndim=1, ng=NG, boundsE=MICRO_E,
                           attr=ABS, flux="NOT_ARRAY", cutoffE=[0.625e-06])

    with pytest.raises(TypeError, match="Energy cutoffs*"):
        EnergyCondensation(ndim=1, ng=NG, boundsE=MICRO_E,
                           attr=ABS, flux=flx, cutoffE="NOT_ARRAY")

    with pytest.raises(TypeError, match="Attribute*"):
        EnergyCondensation(ndim=1, ng=NG, boundsE=MICRO_E,
                           attr=[[1]], flux=flx, cutoffE=[0.625e-06])

    with pytest.raises(TypeError, match="Flux*"):
        EnergyCondensation(ndim=1, ng=NG, boundsE=MICRO_E,
                           attr=ABS, flux=[[1]], cutoffE=[0.625e-06])

    with pytest.raises(TypeError, match="Energy cutoffs*"):
        EnergyCondensation(ndim=1, ng=NG, boundsE=MICRO_E,
                           attr=ABS, flux=flx, cutoffE=[[1]])

    with pytest.raises(TypeError, match="Attribute*"):
        EnergyCondensation(ndim=2, ng=NG, boundsE=MICRO_E,
                           attr=[1], flux=flx, cutoffE=[0.625e-06])

    with pytest.raises(ValueError, match="Dimensions*"):
        EnergyCondensation(ndim=3, ng=NG, boundsE=MICRO_E,
                           attr=ABS, flux=flx, cutoffE=[0.625e-06])

    with pytest.raises(ValueError, match="Number of energy groups*"):
        EnergyCondensation(ndim=1, ng=0, boundsE=MICRO_E,
                           attr=ABS, flux=flx, cutoffE=[0.625e-06])

    with pytest.raises(ValueError, match="Energy boundaries*"):
        EnergyCondensation(ndim=1, ng=NG, boundsE=MICRO_E[1::],
                           attr=ABS, flux=flx, cutoffE=[0.625e-06])

    with pytest.raises(ValueError, match="Attribute*"):
        EnergyCondensation(ndim=1, ng=NG, boundsE=MICRO_E,
                           attr=ABS[1::], flux=flx, cutoffE=[0.625e-06])

    with pytest.raises(ValueError, match="Flux*"):
        EnergyCondensation(ndim=1, ng=NG, boundsE=MICRO_E,
                           attr=ABS, flux=flx[1::], cutoffE=[0.625e-06])

    with pytest.raises(ValueError, match="Energy boundaries*"):
        EnergyCondensation(ndim=1, ng=NG, boundsE=-1*MICRO_E,
                           attr=ABS, flux=flx, cutoffE=[0.625e-06])

    with pytest.raises(ValueError, match="Energy cutoffs*"):
        EnergyCondensation(ndim=1, ng=NG, boundsE=MICRO_E,
                           attr=ABS, flux=flx, cutoffE=[-0.625e-06])

    with pytest.raises(ValueError, match="Energy boundaries*"):
        MICRO_E0 = MICRO_E
        MICRO_E0[10] = 10
        EnergyCondensation(ndim=1, ng=NG, boundsE=MICRO_E0,
                           attr=ABS, flux=flx, cutoffE=[0.625e-06])



