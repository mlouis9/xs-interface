.. _meth-energycond:


Energy Condensation
------------------- 

In order to obtain the few-group cross-sections we need to collapse the :math:`\sigma(E)` with the flux :math:`\phi(E)`. 
To find the few-group cross sections we use the energy continues diffusion equation :eq:`eq-diffusion`.

.. math::
	&\frac{1}{v}\frac{\partial \phi}{\partial t}= \nabla \cdot D\nabla\phi-\Sigma_{a}\phi-\Sigma_{s}\phi \\
	& + \int_{0}^{\infty}\Sigma_{s}(E' \rightarrow E)\phi (E')dE' \\
	&+\chi(E)\int_{0}^{\infty}\nu(E')\Sigma_{f}(E')\phi(E')
   :label: eq-diffusion

Please note that :math:`\phi=\phi(\mathbf{r},E,t)`. The group flux is defined as:

.. math::
	\phi_g(\mathbf{r},t)\equiv \int_{E_g}^{E_{g-1}}\phi(\mathbf{r},E,t)dE 
   :label: eq-groupflux	

We will now eliminate the energy variable in the energy-dependent diffusion by integrating Eq. :eq:`eq-diffusion` over the :math:`g^{th}` energy group.
These will generate rigorous definition of group-averaged cross sections. 

The absorption :eq:`eq-absxs` and production :eq:`eq-nufissxs` cross sections are straightforward to calculate.
The scattering removal term has the same form, however, the scattering (source) term requires more work as described in Eq. :eq:`eq-sctxs`.

.. math::
	\Sigma_{ag} = \frac{1}{\phi_g}\int_{E_g}^{E_{g-1}}\Sigma_a(E) \phi(E)dE
   :label: eq-absxs

.. math::
	& \nu_{g'}\Sigma_{fg'} \equiv \frac{1}{\phi_g}\int_{E_g}^{E_{g-1}}\nu(E') \Sigma_f(E') \phi(E') dE' \\
	& \chi_g \equiv \int_{E_g}^{E_{g-1}} \chi(E)dE
   :label: eq-nufissxs

.. math::
	\Sigma_{sg'g}\equiv \frac{1}{\phi_g'}\int_{E_g}^{E_{g-1}}dE\int_{E_{g'}}^{E_{g'-1}} \Sigma_s(E'\rightarrow E) \phi(E') dE'
   :label: eq-sctxs 
   
The group-wise diffusion coefficient is evaluated using the :math:`\nabla \phi` rather than the flux values:
 
.. math::
	D_g=\frac{\int_{E_g}^{E_{g-1}}D(E) \nabla \phi(E)dE}{\int_{E_g}^{E_{g-1}}\nabla \phi(E)dE}
   :label: eq-diffxs  
   
and the neutron speed characterizing group g is:

.. math::
	\frac{1}{v_g}\equiv\frac{1}{\phi_g}\int_{E_g}^{E_{g-1}}\frac{1}{v(E)}\phi(E)dE
   :label: eq-invv 