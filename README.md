# xs-interface
Homogenized multi-group (MG) cross section (XS) interface to link between codes that generate and those that use these MG XS.

Description
============
The primary objective of the interface is to store multi-group cross-sections sets.
The following capabilities are embedded within the code. 
1. Energy condensation.
2. Spatial homoganization.
2. Intrpolation base-off specific operational data.
3. Storing arbitrary cross sections defined by the user.
4. Defining cross sections for arbirary dependnecies.

The ``xsInterface`` is primary designed to link between:
1. Continuous in energy Monte Carlo to MG Monte Carlo
2. Continuous in energy or MG Monte Carlo to Reduced-Order Transport codes.


Installation
============
After downloading all the package navigate to the root directory.
The ``setup.py`` defines how to install the code.
Execute the following line:

NO NEED:: python setup.py sdist bdist_wheel

python setup.py install --user

The command should create a ``dist`` directory where you should find the `<tar.gz>`
and `<.whl>` files. The `<tar.gz>` file is a source archive and `<.whl>` is a built distribution.

Before installing you may need to make sure that you have the latest pip, setuptools,and wheel on your system.
Follow the next execution line:

`<python -m pip install -upgrade pip setuptools wheel>`

You can also install the package with a develop mode, which is useful if you want to make constant changes and debug:
<python setup.py develop --user>


Execution
=========
The `xsInterface` package can now be imported as as standard PyPI using:

import `import xsInterface`

Currently a memory-based input data is required.
The user must import the following modules:

`from xsInterface.functions.<functionFile> FunctionName


References
==========
[1] Ref-1-

[2] Ref-1-

