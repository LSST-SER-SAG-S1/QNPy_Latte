Installation
============

Requirements
------------

QNPy-Latte targets **Python 3.9** and depends on the scientific-Python and PyTorch stack
(``torch``, ``numpy``, ``pandas``, ``scipy``, ``scikit-learn``, ``astropy``, ``tslearn``,
``MiniSom``, ``matplotlib``, ``seaborn``, ``plotly``, ``dill``, ``tqdm``). All are installed
automatically with the package.

From PyPI
---------

A virtual environment (Anaconda recommended) keeps the PyTorch stack isolated:

.. code-block:: bash

   conda create --name qnpy-latte -c anaconda python=3.9
   conda activate qnpy-latte
   pip install QNPy_Latte

From source
-----------

.. code-block:: bash

   git clone https://github.com/<your-account>/QNPy_Latte.git
   cd QNPy_Latte
   pip install -e .

Verify
------

.. code-block:: python

   import QNPy_Latte
   from QNPy_Latte import Clustering_with_SOM, PREPROCESS, SPLITTING_AND_TRAINING, PREDICTION
   print("QNPy-Latte import OK")
