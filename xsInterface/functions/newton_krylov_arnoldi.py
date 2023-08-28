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
Last updated on Mon Aug 28 16:30:00 2023 @author: Dan Kotlyar

email: dan.kotlyar@me.gatech.edu

List changes or additions:
--------------------------
"Concise description" - MM/DD/YYY - Name initials
ArnoldiIteration - 05/24/2023 - DK
ArnoldiIteration - 06/03/2023 - DK
ArnoldiIteration (objective function) - 08/01/2023 - DK
NewtonKrylov (regression factors & bounds) - 08/01/2023 - DK
_reshapeTo1D (normalize according to each group) - 08/26/2023 - DK
NewtonKrylov (removed some of the user-defined inputs) - 08/28/2023 - DK
"""

from sklearn.linear_model import Ridge
import numpy as np


def ArnoldiIteration(dyn3d, Fx0, x0, b, nodesN: int, n: int, iterScheme, 
                     refFlx, weights=None, k0=0, Qpriv=None, hPriv=None,
                     pert=1e-03, eps=1e-12, sphMultp=None, sphDiv=None, 
                     objmultp=None, printstatus=False):
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
    attrObj : str
        objective attribute used to multiply the flux to create a reaction
        rate objective function
    Qpriv: array
        previous m x (n + 1) array, the columns are an orthonormal basis of the
        Krylov subspace.
    hPriv: array
        previous (n + 1) x n array, A on basis Q. h is the upper Hessenberg.  
    
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
    
    # Restart option to pick up from the previous run
    if (Qpriv is not None) and (hPriv is not None):
        Q[:, 0:k0+1] = Qpriv
        h[0:k0+1, 0:k0] = hPriv
        
    
    for k in range(k0+1,n+1):
        
        if printstatus:
            if k0==0:
                print("Arnoldi #" ,end="")
            print(" {}".format(k),end="")
        
        xI = x0 + pert*Q[:,k-1]  # perturbed transport cross section

        # reshape xI to fit the flux structure [channels x layers x groups]
        xIcore = _reshapeTo3D(dyn3d.flux, xI)

        # update the cross sections
        dyn3d.xs.core.corevalues[iterScheme] = xIcore

        # manipulate/modify all the cross sections if the scheme is SPH
        if iterScheme == 'sph':
            corevaluesmod = _sphManipulation(
                dyn3d.xs.core.corevalues, dyn3d, sphMultp, sphDiv)
            # Read xs data and templates and populate data for channels & layers
            dyn3d.xs.Read(readUniverses=False, readMapTemplate=True,
                          userdata = corevaluesmod)             
        else:
            # Read xs data and templates and populate data for channels&layers
            dyn3d.xs.Read(readUniverses=False, readMapTemplate=True,
                          userdata = dyn3d.xs.core.corevalues) 

        # Execute DYN3D and obtain solution
        dyn3d.Execute(printstatus=False)
                
        dyn3dFlux =\
            _reshapeTo1D(dyn3d.flux, nodesN, normFlag=True, weights=weights)
        if objmultp is None:
            FxI = dyn3dFlux
        else:
            FxI = dyn3dFlux * objmultp
        
        
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
                 krylovSpan: int, krylovErr=5E-03, newtonErr=1E-05,
                 dampingF=1.0, pert=1e-03, lbound=0.2, ubound=3.0, 
                 attrObj=None, weights=None, sphMultp=None, sphDiv=None):
    """Jacobian-free Newton Krylov iterative sequence to update the
    input-vector x0 until the reference solution is obtained.
        

    Parameters
    ----------
    dyn3d : DYN3D object
        an object with the ability to execute DYN3D and collect result
    iterScheme : str
        Determine the iterative parameter, e.g., transport, adf, sph, axial_adf
    x0 : 1-dim array
        initial unperturbed (or guessed) input vector that needs to be found
    refFlx : 1-dim array
        reference flux
    newtonIters : int
        number of Newton iterates. The number is set as a limit.
    krylovSpan : int
        number of Krylov iterates/vectors, must be >= 1. This is the limit but
        the actual number used will be chosen on-the-fly.
    newtonErr : float
        tolerance for stopping the Newton iterations.
    krylovErr : float
        tolerance for stopping the iterations on Krylov.
    dampingF : float
        a damping factor between 0 and 1
    pert : float
        a fraction that represents the perturbation that is required to be
        applied for x for each vector of the Krylov space.  
    lbound : float
        lower bound to limit the variation of correction factors during 
        Newton iterates.
    ubound : float
        upper bound to limit the variation of correction factors during 
        Newton iterates.
    attrObj : str
        objective attribute used to multiply the flux to create a reaction
        rate objective function
    weights : list
        energy group-wise weighting factors for the objective function.
        Envisioned to be used for normalization techniques.
    sphMultp : list
        attributes that will be multiplied by the iterated SPH factors.
        These attributes must exist otherwise an error will be thrown.
    sphDiv : list
        attributes that will be divided by the iterated SPH factors.        
        These attributes must exist otherwise an error will be thrown.
            
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
    
    # -------------------------------------------------------------------------
    #                   Built-in control parameters
    # -------------------------------------------------------------------------
    alpha=0.0    # a hyper parameter for Ridge regression and it is a penalty 
                 # coefficient to minimize the coeff_y in the regression 
                 # procedure. Default value 0.0 --> linear regression.
    printstatus=True  # do not print status of DYN3D execution
    eps=1e-14          # criterion to stop arnoldi iteration.
                       # in the new implementation `eps` is redundant.
    marginKrylovRatio = 1.05  # when comparing previous Krylov span a margin
                              # is applied
    
    nodes = _numNodes(refFlx)  # total number of nodes channels x layers groups
    
    # define and reset return parameters
    fluxes = np.zeros((newtonIters+1, nodes))
    xinputs = np.zeros((newtonIters+1, nodes))
    norm_err = np.zeros(newtonIters+1)
    keff = np.zeros(newtonIters+1)
    
    dyn3d.iterInputs[iterScheme] = [None]*(newtonIters+1)
    dyn3d.iterOutputs = [None]*(newtonIters+1)
    dyn3d.iterDifferences = [None]*(newtonIters+1)

    refFlxNorm = _reshapeTo1D(refFlx, nodes, normFlag=True, weights=weights)

    # If certain reaction rates are to be the objective function
    if attrObj is not None:  # objective function multiplier
        objmultp = _reshapeTo1D(dyn3d.xs.core.corevalues[attrObj], nodes)
    else:
        objmultp = np.ones(nodes)
    
    refFlxNorm = refFlxNorm * objmultp
    dyn3d.refFlx = _reshapeTo3D(dyn3d.refFlx, refFlxNorm)    

    for newtonI in range(newtonIters):

        if printstatus:
            print("Newton #{}/{}".format(newtonI,newtonIters))

        if dampingF == "RM":  # Robbins-Monro
            weightIter = 1/(newtonI+1)
        else:
            weightIter = dampingF
        
        # execute DYN3D and collect results
        dyn3d.Execute(printstatus=False)
        keff[newtonI] = dyn3d.keff
        
        # calculate the normalized fluxes for both the reference and dyn3d
        # the 3-dim lists are converted to 1-dim arrays
        dynFlxNorm =\
            _reshapeTo1D(dyn3d.flux, nodes, normFlag=True, weights=weights)
        dynFlxNorm = dynFlxNorm * objmultp
        # dyn3d.iterOutputs[newtonI] = dyn3d.flux
        dyn3d.iterOutputs[newtonI] = _reshapeTo3D(dyn3d.flux, dynFlxNorm)
        
        # store the differences in fluxes
        difference = 100*(1-dynFlxNorm/refFlxNorm)
        dyn3d.iterDifferences[newtonI] = _reshapeTo3D(dyn3d.flux, difference)
        
        # save the current iterate
        fluxes[newtonI, :] = dynFlxNorm  
        
        # difference bewteen the approximate and reference solution
        Fx0 = fluxes[newtonI, :]-refFlxNorm    
        r0 = -Fx0  # define residual
        norm_err[newtonI] = np.linalg.norm(r0)  # store norm2
        
        # save the very first result for the guessed input corrections
        if newtonI == 0:
            xinputs[0, :] = x0
            # reshape xI to fit the flux structure [channels x layers x groups]
            x0core = _reshapeTo3D(dyn3d.flux, x0)    
            # save the variation in inputs as a function of iteration
            dyn3d.iterInputs[iterScheme][0] = x0core
        
        
        # execute the krylov-arnoldi procedure to obtain othonormal basis of 
        # Krylov subspace and the upper Hessenberg matrix
        Qpriv, hPriv = None, None
        expNormErr = np.zeros(krylovSpan)
        prdNormErr = np.zeros(krylovSpan)
        x0Newton = x0
        dxKrylov = np.zeros((nodes, krylovSpan))
        for krylovN in range(1, krylovSpan+1):
            Q, h =\
                ArnoldiIteration(
                    dyn3d=dyn3d, Fx0=fluxes[newtonI, :], x0=x0Newton, b=r0, 
                    nodesN=nodes, n=krylovN, k0=krylovN-1, refFlx=refFlxNorm,
                    weights=weights, Qpriv=Qpriv, hPriv=hPriv, 
                    iterScheme=iterScheme, pert=pert, eps=eps,
                    sphMultp=sphMultp, sphDiv=sphDiv, objmultp=objmultp, 
                    printstatus=printstatus)
        
            # calculate the coefficients used as weights for the othonormal basis    
            e1 = np.zeros(krylovN+1)
            e1[0] = 1
            normr0 = np.linalg.norm(r0)*e1
            # evaluation of the coefficients from || Hy-||r||e1 ||
            # coefy = np.linalg.lstsq(h, normr0, rcond=None)
            # ridge regression           
            model = Ridge(alpha=alpha,fit_intercept=False)
            model.fit(h, normr0)
            coefy = model.coef_
        
            # Evaluate the expected error
            expNormErr[krylovN-1] = np.linalg.norm(np.dot(h,coefy) - normr0)
                
            # promote the Newton step
            dxk = np.dot(Q[:, 0:-1],coefy)
            dxKrylov[:, krylovN-1] = dxk
            
            # promote x0
            x0 = x0Newton + weightIter*dxk  # no damping for this step
            
            # Bound the changes in the correction factors 
            lmask = np.where(x0 < lbound + pert)
            umask = np.where(x0 > ubound - pert)
            x0[lmask] = lbound + pert
            x0[umask] = ubound - pert
    
            # reshape xI to fit the flux structure [channels x layers x groups]
            x0core = _reshapeTo3D(dyn3d.flux, x0)
    
            # update the cross sections
            dyn3d.xs.core.corevalues[iterScheme] = x0core

            # Store the matrices Q and h for restart purposes
            Qpriv = Q
            hPriv = h

            # -----------------------------------------------------------------
            # Estimate whether more Krylov vectors should be included
            # this is done by executing DYN3D and comparing the norm2 errors
            # -----------------------------------------------------------------
            # manipulate/modify all the cross sections if the scheme is SPH
            if iterScheme == 'sph':
                corevaluesmod = _sphManipulation(
                    dyn3d.xs.core.corevalues, dyn3d, sphMultp, sphDiv)
                # Read xs data & templates; populate data for channels & layers
                dyn3d.xs.Read(readUniverses=False, readMapTemplate=True,
                              userdata = corevaluesmod)             
            else:
                dyn3d.xs.Read(readUniverses=False, readMapTemplate=True,
                              userdata = dyn3d.xs.core.corevalues) 

            dyn3d.Execute(printstatus=False)
    
            # calculate the normalized fluxes for both the reference and dyn3d
            # the 3-dim lists are converted to 1-dim arrays
            dynFlxNorm =\
                _reshapeTo1D(dyn3d.flux, nodes, normFlag=True, weights=weights)
            dynFlxNorm = dynFlxNorm * objmultp           

            # Evaluate the predicted error
            prdNormErr[krylovN-1] = np.linalg.norm(dynFlxNorm-refFlxNorm)

            cond1 = expNormErr[krylovN-1]/prdNormErr[krylovN-1] < krylovErr
            cond2 = False
            
            if krylovN > 2:
                cond2 = prdNormErr[krylovN-1] > marginKrylovRatio*\
                    np.average(prdNormErr[krylovN-3:krylovN-1])
            
            if cond1 or cond2:
                # best solution
                optmKrylovN = np.argmin(prdNormErr[0:krylovN])
                dxk = dxKrylov[:, optmKrylovN]
                break  # stop Arnoldi iterations

        # ---------------------------------------------------------------------
        # Continue with Newton iterations
        # ---------------------------------------------------------------------
        print("")
        if (not cond1) and (not cond2):
            optmKrylovN = np.argmin(prdNormErr[0:krylovN])
            dxk = dxKrylov[:, optmKrylovN]            
        
        x0 = x0Newton + weightIter*dxk  # no damping coefficient at the moment

        # Bound the changes in the correction factors 
        lmask = np.where(x0 < lbound + pert)
        umask = np.where(x0 > ubound - pert)
        x0[lmask] = lbound + pert
        x0[umask] = ubound - pert

        # reshape xI to fit the flux structure [channels x layers x groups]
        x0core = _reshapeTo3D(dyn3d.flux, x0)
        
        # input for the updated Newton step
        xinputs[newtonI+1, :] = x0
    
        # save the variation in inputs as a function of iteration
        dyn3d.iterInputs[iterScheme][newtonI+1] = x0core
            
        # update the cross sections
        dyn3d.xs.core.corevalues[iterScheme] = x0core            
    
        if iterScheme == 'sph':
            corevaluesmod = _sphManipulation(
                dyn3d.xs.core.corevalues, dyn3d, sphMultp, sphDiv)
            # Read xs data and templates and populate data for channels & layers
            dyn3d.xs.Read(readUniverses=False, readMapTemplate=True,
                          userdata = corevaluesmod)             
        else:
            # Read xs data and templates and populate data for channels&layers
            dyn3d.xs.Read(readUniverses=False, readMapTemplate=True,
                          userdata = dyn3d.xs.core.corevalues)         
        
        cond3 = max(abs(1-x0/x0Newton)) < newtonErr
        if cond3:
            break  # stop Newton iterations
        

    # LAST EXECUTION FOR THE OPTIMUM CASE
    # -------------------------------------------------------------------------
    # execute DYN3D and collect results
    dyn3d.Execute(printstatus=False)
    keff[newtonI+1] = dyn3d.keff
    # calculate the normalized fluxes for both the reference and dyn3d
    # the 3-dim lists are converted to 1-dim arrays
    dynFlxNorm =\
        _reshapeTo1D(dyn3d.flux, nodes, normFlag=True, weights=weights)
    dynFlxNorm = dynFlxNorm * objmultp
    
    # dyn3d.iterOutputs[newtonI] = dyn3d.flux
    dyn3d.iterOutputs[newtonI+1] = _reshapeTo3D(dyn3d.flux, dynFlxNorm)

    # store the differences in fluxes
    difference = 100*(1-dynFlxNorm/refFlxNorm)
    dyn3d.iterDifferences[newtonI+1] = _reshapeTo3D(dyn3d.flux, difference)

    
    # save the current iterate
    fluxes[newtonI+1, :] = dynFlxNorm  * objmultp
    # difference bewteen the approximate and reference solution
    Fx0 = fluxes[newtonI+1, :]-refFlxNorm    
    r0 = -Fx0  # define residual
    norm_err[newtonI+1] = np.linalg.norm(r0)  # store norm2    
    

    # -------------------------------------------------------------------------
    # store and return final results
    # -------------------------------------------------------------------------
    fluxes = fluxes[0:newtonI+2, :]
    xinputs = xinputs[0:newtonI+2, :]
    norm_err = norm_err[0:newtonI+2] 
    keff = keff[0:newtonI+2]
    dyn3d.iterkeff = keff
    dyn3d.iterOutputs = dyn3d.iterOutputs[0:newtonI+2]
    dyn3d.iterDifferences = dyn3d.iterDifferences[0:newtonI+2]
    dyn3d.iterInputs[iterScheme] = dyn3d.iterInputs[iterScheme][0:newtonI+2]
    
    return fluxes, xinputs, norm_err, refFlxNorm
    

# -----------------------------------------------------------------------------
#                          Supplementary function
# -----------------------------------------------------------------------------

def _reshapeTo1D(flxIn, n, normFlag=True, weights=None):
    """Normalize the flux to unity"""

    # Normlization
    # normFlag indicates if fluxes should be normalized to unity
    # weights - list of weights indicating the importance of each group

    ng = len(flxIn[0][0])  # number of energy groups
    flx = np.zeros(n)
    c = 0  # counter
    for channel in flxIn:
        for layer in channel:
            for grVal in layer:
                flx[c] = grVal
                c += 1
    if weights is not None:
        for ig in range(ng):
            flx[ig::ng] = weights[ig]*flx[ig::ng]/flx[ig::ng].sum()
    elif normFlag:
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


def _sphManipulation(corevalues, dyn3d, sphMultp=None, sphDiv=None):
    """Normalize the flux to unity"""

    # sphMultp is a list with attributes to be multiplied by SPH factors
    # sphDiv is a list with attributes to be divided by SPH factors

    if sphMultp is None and sphDiv is None:
        raise ValueError('SPH multiplier and dividers cannot be both None')
    if sphMultp is None:
        sphMultp = [None]
    if sphDiv is None:
        sphDiv = [None]
    sphAttrs = sphMultp + sphDiv  # create one list of attributes


    dictOut = {}
    nchannels = len(dyn3d.xs.core.layers)  # number of channels
    nlayers = dyn3d.xs.core.layers  # vector indicating number of layers for each channel
    
    noAttrs = []
    existingAttrs = list(corevalues.keys())
    for attr in sphAttrs:
        if attr is None:
            continue
        if attr not in existingAttrs:
            noAttrs.append(attr)
    if len(noAttrs) > 0:
        raise ValueError('SPH manipulation attributes:\n{}\ndo not exist in:{}'
                         .format(noAttrs, existingAttrs))
    
    
    # manipulate all the attributes
    for attr, values in corevalues.items():
        if attr == 'sph':
            continue  # no need to manipulate
        valuesOut = [None]*nchannels
        for chIdx in range(nchannels):
            chVals = values[chIdx]
            valuesOut[chIdx] = [None]*nlayers[chIdx]
            for ilayer, layerVals in enumerate(chVals):
                try:
                    if attr in sphMultp: 
                        # can only succeed if these are cross sections
                        valuesOut[chIdx][ilayer] =\
                            layerVals * corevalues['sph'][chIdx][ilayer]
                    elif attr in sphMultp:
                        valuesOut[chIdx][ilayer] =\
                            layerVals / corevalues['sph'][chIdx][ilayer]
                    else:
                        valuesOut[chIdx][ilayer] = layerVals                        
                except:
                    valuesOut[chIdx][ilayer] = layerVals                 
        dictOut[attr] = valuesOut        

    return dictOut


# def dxmag_res(alpha, h, normr0, dxmag):
#     """get the max step size"""
#     alpha = alpha[0]
#     model = Ridge(alpha=alpha)
#     model.fit(h, normr0)
#     coefy = model.coef_
#     return (np.linalg.norm(coefy)-dxmag)**2




                 