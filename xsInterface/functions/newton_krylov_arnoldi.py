# -*- coding: utf-8 -*-
"""
newton_krylov_arnoldi.py


arnoldi (inner iterations on Krylov subspaces)
----------------------------------------------
Iterative Arnoldi procedure to determine the required variation of dx
for :
    Fx*dx = b

Newton-Krylov (outer iterations on the variation in x)
------------------------------------------------------
xk = x0 + s*dx
dx is obtained by using the Krylov-Arnoldi routine

Created on Wed May 24 15:10:00 2023 @author: Dan Kotlyar
Last updated on Wed May 24 15:10:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
ArnoldiIteration - 05/24/2023 - DK

"""

import copy
import numpy as np
from xsInterface.functions.thirdpartycodes import exeDyn3D


def ArnoldiIteration(xs, Fx0, x0, b, nodesN: int, n: int,
                     iterScheme, refFlx, casedir, casefile, exefile, 
                     pert=1e-03):
    """Computes othonormal basis of the (n + 1)-Krylov subspace for Fx*dx:
        
    This function allow to estimate the required variation in x (i.e., dx)
    by using the space spanned by {b, Ab, ..., A^n b}.
    A is not a matrix in this case, but rather the nonlinear operator that
    estimates the function's value for a given x. The purpose of the function
    is to minimize the residual between the approximated and exact/known 
    solution.
    
    Parameters
    ----------
    xs : xsInterface object
        An object of type xsInterface
    x0 : 1-dim array
        Initial guess/solution for the input vector needed to run a reduced
        order solution. x0 can be diffusion coefficient, discontinuity factors,
        SPH factors.
    Fx0 : 1-dim array
        Approximated solution for x0. This is not the residual but the function
        evaluated for x0. As an example, Fx0 can be the flux obtained by 
        executing DYN3D.
    b : 1-dim array
        this is the vector on the right hand side of Ax=b
    nodesN : int
        Number of total nodes (i.e., #channels x #layers x #energy-groups)
    n : int
        dimension of Krylov subspace, must be >= 1                        
    casedir : str
        full (relative or absolute) directory where the _kin file is located
    casefile : str
        name of the case file
    exefile : str 
        name of the file with the actual execution command
    pert : float
        a fraction that represents the perturbation that is required to be
        applied for x for each vector of the Krylov space.              

    
    Returns
    ----------
    
      Q: m x (n + 1) array, the columns are an orthonormal basis of the
        Krylov subspace.
      h: (n + 1) x n array, A on basis Q. h is the upper Hessenberg.  
    """
    
    
    
    pert = 1e-03  # perturbation to evaluate the function
    eps = 1e-12  # criterion to stop arnoldi iteration

    h = np.zeros((n+1,n))  # upper Hessenberg
    Q = np.zeros((nodesN,n+1))

     # Normalize the input vector
    Q[:,0] =b/np.linalg.norm(b, 2)   # Create the first Krylov vector
    for k in range(1,n+1):
        
        xI = x0 + pert*Q[:,k-1]  # perturbed transport cross section

        # perturbed DYN3D solution
        keff, fluxes, normFlux = exeDyn3D(casedir, casefile, exefile)
        FxI = normFlux.flatten()   
        
        v = (FxI - Fx0) / pert  # this is the matrix-vector product
                                # v = A^n b

        for j in range(k):  # Subtract the projections on previous vectors
            h[j,k-1] = np.dot(Q[:,j].T, v)
            v = v - h[j,k-1] * Q[:,j]
        h[k,k-1] = np.linalg.norm(v,2)
        if h[k,k-1] > eps:  # Add the produced vector to the list, unless
            Q[:,k] = v/h[k,k-1]
        else:  # If that happens, stop iterating.
            return Q, h
    return Q, h


def NewtonKrylov(dyn3dInputs, iterScheme, refFlx, nodes: int, newtonIters: int,
                 krylovSpan: int, indexMap, channelMap, radialChannels, numFAs,
                 dz, dampingF=1.0):
    """Jacobian-free Newton Krylov iterative sequence to update the
    input-vector x0 until the reference solution is obtained.
        

    Parameters
    ----------
    dyn3dInputs : dict
        includes all the cross sections and inputs required to execute DYN3D
    iterScheme : str
        Determine the iterative parameter, e.g., transport, adf, sph, axial_adf
    refFlx : 1-dim array
        reference flux
    nodes : int
        number of nodes (i.e., channels x layers)
    newtonIters : int
        number of Newton iterates
    krylovSpan : int
        number of Krylov iterates/vectors, must be >= 1    
    indexMap : 2-dim array
        map with channels indices
    channelMap : 2-dim array of str
        radial distribution of channels universes names    
    radialChannels : 1-dim array of str
        universe naming corresponding to the order in which cross sections
        are provided
    numFAs : 2-dim array
         radial distribution with how many times each assembly appears in core                  
    dz : 1-dim array
        the length of each layer
    dampingF : float
        a damping factor between 0 and 1

    Returns
    -------
    fluxes : 2-dim array
        a vector for all channel in layers in 1-dim manner for each Newton step
    xinputs : 2-dim array
        a vector for all channel in layers in 1-dim manner for each Newton step
    norm_err : 1-dim array
        norm2 between serpent and predicted flux values
    refFlx : 1-dim array
        reference flux for all channels and layers
          
    
    """
    
    
    # convert to 1-dim array
    nFAs = len(refFlx)
    nLayers = len(refFlx[0])    
    nodes = int(nFAs * nLayers)
    # define and reset return parameters
    fluxes = np.zeros((newtonIters+1, nodes))
    xinputs = np.zeros((newtonIters+1, nodes))
    norm_err = np.zeros(newtonIters+1)


    refFlxOrig = copy.deepcopy(refFlx)

    # choose what is the iterative parameter
    if iterScheme == 'transpxs':
        x0 = np.array(dyn3dInputs['transpxs']).flatten()
    elif iterScheme == 'adf':
        x0 = np.array(dyn3dInputs['adf']).flatten() 
    elif iterScheme == 'axial_adf':
        x0 = np.array(dyn3dInputs['topDf']).flatten() 
    elif iterScheme == 'sph':
        x0 = np.array(dyn3dInputs['sph']).flatten() 

    for newtonI in range(newtonIters):
        
        x0Reshape = x0.reshape((nFAs, nLayers))
        x0List = [xvals for xvals in x0Reshape]
        if iterScheme == 'transpxs':
            dyn3dInputs['transpxs'] = x0List
        elif iterScheme == 'adf':
            dyn3dInputs['adf'] = x0List
        elif iterScheme == 'axial_adf':
            dyn3dInputs['topDf'] = x0List
        elif iterScheme == 'sph':
            dyn3dInputs['sph'] = x0List
            
        # execute DYN3D
        dyn3dResult, normFlux = ExeDyn3d(**dyn3dInputs)
        
        # calculate the normalized fluxes for both Serpent and DYN3D
        fluxDYN3D, fluxSERP, chFAs =\
            CreateFluxes(dyn3dResult["flux"], refFlxOrig, indexMap, channelMap,
                         radialChannels, numFAs, dz)
        
        fluxes[newtonI, :] = fluxDYN3D.flatten()  # save the current iterate
        refFlx = fluxSERP.flatten()
        
        # difference bewteen the approximate and reference solution
        Fx0 = fluxes[newtonI, :]-refFlx    
        r0 = -Fx0  # define residual
        norm_err[newtonI] = np.linalg.norm(r0)  # store norm2
        
        # execute the krylov-arnoldi procedure to obtain othonormal basis of 
        # Krylov subspace and the upper Hessenberg matrix
        Q, h =\
            ArnoldiIteration(Fx0=fluxes[newtonI, :], x0=x0, b=r0, nodesN=nodes,
                             n=krylovSpan, dyn3dInputs=dyn3dInputs,
                             iterScheme=iterScheme, 
                             indexMap=indexMap, channelMap=channelMap,
                             radialChannels=radialChannels, numFAs=numFAs, 
                             dz=dz,refFlx=refFlxOrig,
                             pert=1e-03)
        
        # calculate the coefficients used as weights for the othonormal basis    
        e1 = np.zeros(krylovSpan+1)
        e1[0] = 1
        normr0 = np.linalg.norm(r0)*e1
        # evaluation of the coefficients from || Hy-||r||e1 ||
        coefy = np.linalg.lstsq(h, normr0, rcond=None)
        
        # input for the current Newton step
        xinputs[newtonI, :] = x0
        
        # promote the Newton step
        dxk = np.dot(Q[:, 0:-1],coefy[0])
        x0 = x0 + dampingF*dxk  # no damping coefficient at the moment
        

    x0Reshape = x0.reshape((nFAs, nLayers))
    x0List = [xvals for xvals in x0Reshape]
    if iterScheme == 'transpxs':
        dyn3dInputs['transpxs'] = x0List
    elif iterScheme == 'adf':
        dyn3dInputs['adf'] = x0List
    elif iterScheme == 'axial_adf':
        dyn3dInputs['topDf'] = x0List
    elif iterScheme == 'sph':
        dyn3dInputs['sph'] = x0List

    xinputs[newtonI+1, :] = x0
    dyn3dResult, normFlux = ExeDyn3d(**dyn3dInputs)
    # calculate the normalized fluxes for both Serpent and DYN3D
    fluxDYN3D, fluxSERP, chFAs =\
        CreateFluxes(dyn3dResult["flux"], refFlxOrig, indexMap, channelMap,
                     radialChannels, numFAs, dz)
    
    fluxes[newtonI+1, :] = fluxDYN3D.flatten()  # save the current iterate

    # define residual    
    norm_err[newtonI+1] = np.linalg.norm(fluxes[newtonI+1, :]-refFlx)

    return fluxes, xinputs, norm_err, refFlx
    
    