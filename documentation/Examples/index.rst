.. _ex-toctree:
  

Examples
========

.. toctree::
   :maxdepth: 2
   :hidden:
   :caption: Contents:

   singleset.rst
   multiplesets.rst
   write_xs.rst
   generate_xs.rst
   exe_dyn3d.rst
   exe_dyn3d_2d_xs.rst
   jfnk_dyn3d.rst
 
Utilization of containers
^^^^^^^^^^^^^^^^^^^^^^^^^

This section includes useful utilization of specific classes and methods:

- :ref:`singleset_example`: Collect, store, and process data for a single state point.
- :ref:`multiplesets_example`: Collect, store, and process data for multiple state points.


Full Examples
^^^^^^^^^^^^^

- **BWR** case with a single channel and multiple layers (38 total)

	- Read cross secctions [:ref:`readxs_example`],
	- Read & write cross sections to template files [:ref:`writexs_example`],
	- Execute DYN3D using the read cross sections [:ref:`exe_dyn3d_example`]
	- Read and execute DYN3D using 2-dim cross sections [:ref:`exe_dyn3d_2d_example`],
	- Iterate on DYN3D using the JFNK built-in method [:ref:`iterate_dyn3d_example`]. 



