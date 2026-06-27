QNPy-Latte
==========

**Latent ATTEntive Neural Processes for Quasar Light Curves with parametric recovery.**

QNPy-Latte is an open-source Python package developed by the **SER-SAG-S1** team as part of
the Serbian in-kind software contribution to the Vera C. Rubin Observatory / LSST. It models
quasar light curves with **Attentive Latent Neural Processes (AttnLNPs)**, clusters them with
**Self-Organizing Maps (SOMs)**, and recovers physical parameters of the source - in particular
the **transfer function** - from the model's latent representation.

It is the successor to `QNPy <https://github.com/kittytheastronaut/QNPy-0.0.2>`_ (Conditional
Neural Processes), adding a latent path, attention, optional RNN time-encoding, and
parameter/transfer-function recovery.

.. note::

   This documentation site is maintained for the SER-SAG-S1 in-kind closeout. The package
   source lives at https://github.com/rajuaman1/QNPy_Latte and is installable from PyPI
   (``pip install QNPy_Latte``).

.. toctree::
   :maxdepth: 2
   :caption: Getting started

   installation
   quickstart

.. toctree::
   :maxdepth: 2
   :caption: User guide

   user_guide/overview
   user_guide/data_format
   user_guide/clustering
   user_guide/preprocessing
   user_guide/training
   user_guide/modelling
   user_guide/parameters

.. toctree::
   :maxdepth: 2
   :caption: Tutorials

   tutorials/index

.. toctree::
   :maxdepth: 2
   :caption: Background

   background/science

.. toctree::
   :maxdepth: 2
   :caption: API reference

   api/index

.. toctree::
   :maxdepth: 1
   :caption: Project

   references
   contributing
   changelog

Indices
-------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
