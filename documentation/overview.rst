.. _project-overview:

================
Project Overview
================

This package is designed to act as a general cross section interface.
It is meant to work with any general lattice and core simulator codes.
For example, the following applications are envisioned:

Lattice-based tools that can be used:

- `Serpent <https://www.sciencedirect.com/science/article/pii/S0306454914004095>`_ ;
- `Shift <https://www.sciencedirect.com/science/article/pii/S0306454919300167>`_ ;
- list to be expanded, but the target codes include OpenMC and MOOSE based tools.

After reading and processing the homogenized data, the following multi-group solvers can use the package:

- `Shift <https://www.sciencedirect.com/science/article/pii/S0306454919300167>`_ ;
- `DYN3D <https://www.sciencedirect.com/science/article/abs/pii/S014919701630035X>`_ ;
- `PARCS <https://www.nrc.gov/docs/ML1016/ML101610098.pdf>`_ ;
- `GeN-Foam <https://www.sciencedirect.com/science/article/abs/pii/S0029549315003829>`_  or any OpenFoam based tool.


Description
============

The package is designed as a general tool. The idea is to avoid the need to dive into the internals of the package.
The ``xsInterface`` includes the following capabilities:

1. User-defined definitions for input parameters.
2. User-defined perturbations.
3. Energy condensation techniques.
4. Spatial homogenization techniques.
5. General templates to write the output files.  

The setup of the problem can be performed via:

1. Memory-based Interface (recommended for coupled codes)
2. Input file-based Interface. 

The package allows to perform the following important operations:

- Energy condensation.
- Spatial homogenization.
- Multivariate interpolation.
- Generation of spatial transfer functions.

