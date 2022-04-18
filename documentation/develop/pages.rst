.. _docs-pages:

Host Documentation on GitHub
============================

GitHub Pages is available in public repositories with GitHub Free and GitHub Free for organizations,
and in public and private repositories with GitHub Pro.

From GitHub Pages <https://docs.github.com/en/pages>`_


Before you enable ``pages`` on your GitHub repository several steps need to be undertaken on your personal working station.
We'll assume sphinx documentation is already generated in a ``html`` format. 

Handling the Sphinx documentation:
----------------------------------


1. Create a separate branch for your documentation, e.g., ideally ``gh-pages`` but any name should work.
2. Make sure that the root directory (where the setup.py) contains the ``docs`` directory where you will build your html directory and index.html file.
	- This may require you to create a different directory (e.g., ``documentation``) where the ``make`` and ``Makefile`` will be hosted.
3. Change the default build folder as ``docs`` in your makefile. If you have a make.bat file change there as well.

``Makefile``
    .. code:: 

    	BUILDDIR = ../docs


``make.bat``
    .. code:: 

      set BUILDDIR=../docs

4. Build documentation:

    .. code:: 

       make html
        
5. The ``docs`` folder in the root directory should have the following content:


    .. code:: 

			--docs 
			  |--doctrees 
			  |--html 
			     |--index.html 

6. The ``index.html`` is not inside the top level of ``docs`` folder.
Copy the ``index.html`` inside ``docs/index.html`` in the ``docs`` directory. Open the copied file and insert the following line:

    .. code:: 
				
				<meta http-equiv="refresh" content="0; url=./html/index.html" />
				
7. It may be needed to add an empty ``.nojekyll`` file in the docs directory (or root dir) as GitHub publishes the pages through jekyll.


Enabling Pages on GitHub:
-------------------------

GitHub is disabled by default. To enable follow the next steps:

1. Go to your GitHub repository
2. Open the ``Settings`` tab and select ``Pages`` from the sidebar
3. From the source section, select the branch (e.g., ``gh-pages``) wherever you have pushed the documentation code.
4. Commit the code and select the branch in the source section.
5. If you create a branch called gh-pages, GitHub will automatically recognize the documentation and show it.
6. Make sure the ``index.html`` file is available at the top level of the directory (e.g., ``docs``) you are hosting. Else, you may see the 404 error.
7. Your page should be available at the mentioned location after you save the configuration.

