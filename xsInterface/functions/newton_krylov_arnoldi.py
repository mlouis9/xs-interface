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
Last updated on Sat June 03 07:15:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
ArnoldiIteration - 05/24/2023 - DK
ArnoldiIteration - 06/03/2023 - DK

"""

import numpy as np


def ArnoldiIteration(dyn3d, Fx0, x0, b, nodesN: int, n: int, iterScheme, 
                     pert=1e-03, eps=1e-12):
    """Computes othonormal basis of the (n + 1)-Krylov subspace for Fx*dx:
        
    This function allow to estimate the required variation in x (i.e., dx)
    by using the space spanned by {b, Ab, ..., A^n b}.
    A is not a matrix in this case, but rather the nonlinear operator that
    estimates the function's value for a given x. The purpose of the function
    is to minimize the residual between the approximated and exact/known 
    solution.
    
    Parameters
    ----------
    dyn3d : DYN3D object
        An object of type DYN3D with the ability to execute and store results
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
    iterScheme : str
        the name of the attribute or scheme which needs to be iterated and
        converged. e.g, sph.
    pert : float
        a fraction that represents the perturbation that is required to be
        applied for x for each vector of the Krylov space.  
    eps : float
        criterion to stop arnoldi iteration.       

    
    Returns
    ----------
    
      Q: m x (n + 1) array, the columns are an orthonormal basis of the
        Krylov subspace.
      h: (n + 1) x n array, A on basis Q. h is the upper Hessenberg.  
    """
    
    
    h = np.zeros((n+1,n))  # upper Hessenberg
    Q = np.zeros((nodesN,n+1))

     # Normalize the input vector
    Q[:,0] =b/np.linalg.norm(b, 2)   # Create the first Krylov vector
    for k in range(1,n+1):
        
        xI = x0 + pert*Q[:,k-1]  # perturbed transport cross section

        # reshape xI to fit the flux structure [channels x layers x groups]
        xIcore = _reshapeTo3D(dyn3d.flux, xI)

        # update the cross sections
        dyn3d.xs.core.corevalues[iterScheme] = xIcore
        
        # Read xs data and templates and populate data for channels & layers
        dyn3d.xs.Read(readUniverses=False, readMapTemplate=True,
                      userdata = dyn3d.xs.core.corevalues) 

        # Execute DYN3D and obtain solution
        dyn3d.Execute()
        
        FxI = _reshapeTo1D(dyn3d.flux, nodesN, normFlag=True)   
        
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


def NewtonKrylov(dyn3d, iterScheme, x0, refFlx, newtonIters: int,
                 krylovSpan: int, dampingF=1.0):
    """Jacobian-free Newton Krylov iterative sequence to update the
    input-vector x0 until the reference solution is obtained.
        

    Parameters
    ----------
    dyn3d : DYN3D object
        an object with the ability to execute DYN3D and collect result
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
    
    nodes = _numNodes(refFlx)  # total number of nodes channels x layers groups
    
    # define and reset return parameters
    fluxes = np.zeros((newtonIters+1, nodes))
    xinputs = np.zeros((newtonIters+1, nodes))
    norm_err = np.zeros(newtonIters+1)
    
    dyn3d.iterInputs[iterScheme] = [None]*newtonIters


    refFlxNorm = _reshapeTo1D(refFlx, nodes, normFlag=True)

    for newtonI in range(newtonIters):
        
        # if iteration scheme is of SPH manipulation of cross sections needed
        if iterScheme == 'sph':
            pass

            
        # execute DYN3D and collect results
        dyn3d.Execute()
        
        # calculate the normalized fluxes for both the reference and dyn3d
        # the 3-dim lists are converted to 1-dim arrays
        dynFlxNorm = _reshapeTo1D(dyn3d.flux, nodes, normFlag=True)
        

        # save the current iterate
        fluxes[newtonI, :] = dynFlxNorm  
        
        # difference bewteen the approximate and reference solution
        Fx0 = fluxes[newtonI, :]-refFlxNorm    
        r0 = -Fx0  # define residual
        norm_err[newtonI] = np.linalg.norm(r0)  # store norm2
        
        # execute the krylov-arnoldi procedure to obtain othonormal basis of 
        # Krylov subspace and the upper Hessenberg matrix
        Q, h =\
            ArnoldiIteration(dyn3d, Fx0=fluxes[newtonI, :], x0=x0, b=r0,
                             nodesN=nodes, n=krylovSpan,
                             iterScheme=iterScheme, pert=1e-03)
        
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
        
        # reshape xI to fit the flux structure [channels x layers x groups]
        x0core = _reshapeTo3D(dyn3d.flux, x0)

        # update the cross sections
        dyn3d.xs.core.corevalues[iterScheme] = x0core

        # save the variation in inputs as a function of iteration
        dyn3d.iterInputs[iterScheme][newtonI] = x0core
    
        

    # LAST EXECUTION
    # -------------------------------------------------------------------------
    
    # execute DYN3D and collect results
    dyn3d.Execute()
    
    # calculate the normalized fluxes for both the reference and dyn3d
    # the 3-dim lists are converted to 1-dim arrays
    dynFlxNorm = _reshapeTo1D(dyn3d.flux, nodes, normFlag=True)
    # save the current iterate
    fluxes[newtonI+1, :] = dynFlxNorm  
    # difference bewteen the approximate and reference solution
    Fx0 = fluxes[newtonI+1, :]-refFlxNorm    
    r0 = -Fx0  # define residual
    norm_err[newtonI+1] = np.linalg.norm(r0)  # store norm2    
    
    return fluxes, xinputs, norm_err, refFlxNorm
    

# -----------------------------------------------------------------------------
#                          Supplementary function
# -----------------------------------------------------------------------------

def _reshapeTo1D(flxIn, n, normFlag=True):
    """Normalize the flux to unity"""

    flx = np.zeros(n)
    c = 0  # counter
    for channel in flxIn:
        for layer in channel:
            for grVal in layer:
                flx[c] = grVal
                c += 1
    if normFlag:
        flx = flx / flx.sum()
    return flx



def _reshapeTo3D(flx, x0In):
    """Reshape the input parameter to match the flux structure"""

    nch = len(flx)
    x0Out = [None]*nch  # reset the input variable
    ng = len(flx[0][0])  # number of energy groups
    
    c = 0
    for ich in range(nch):
        nz = len(flx[ich])  # of layers
        channel = [None]*nz
        for iz in range(nz):
            groups = np.empty(ng)
            for ig in range(ng):
                groups[ig] = x0In[c]  # group values
                c += 1
            channel[iz] = groups  # group values for each layer
        x0Out[ich] = channel # values for all the channels

    return x0Out


def _numNodes(flxIn):
    """Calculate the total number of nodes required for the solution"""

    c = 0  # counter
    for channel in flxIn:
        c += len(channel)
        
    ng = len(flxIn[0][0])
    c *= ng
    return c  # total number of nodes
                 