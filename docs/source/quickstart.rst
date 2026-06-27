Quickstart
==========

The end-to-end workflow has four stages. Each maps to a module and to one of the tutorial
notebook folders shipped with the package.

.. list-table::
   :header-rows: 1
   :widths: 22 30 30

   * - Stage
     - Module
     - Tutorial notebooks
   * - Cluster light curves
     - :doc:`Clustering_with_SOM <api/clustering_with_som>`
     - ``Clustering_Tutorial_Notebooks``
   * - Preprocess
     - :doc:`PREPROCESS <api/preprocess>`
     - ``Modelling_Tutorial_Notebooks``
   * - Train the model
     - :doc:`SPLITTING_AND_TRAINING <api/splitting_and_training>`
     - ``Modelling_Tutorial_Notebooks``
   * - Reconstruct & recover parameters
     - :doc:`PREDICTION <api/prediction>`
     - ``Modelling_Tutorial_Notebooks_w_Params``

A minimal modelling run
-----------------------

.. code-block:: python

   from QNPy_Latte import PREPROCESS as pre
   from QNPy_Latte import SPLITTING_AND_TRAINING as st
   from QNPy_Latte import PREDICTION as pred
   import torch

   device = "cuda" if torch.cuda.is_available() else "cpu"

   # 1. Preprocess: clean, pad to a common length, transform magnitudes to [-2, 2]
   pre.clean_outliers_median("Light_Curves", "cleaned", threshold=0.25)
   pre.backward_pad_curves("cleaned", "padded", desired_observations=100)

   # 2. Split into train / test / val folders and build data loaders
   st.create_split_folders("./dataset/train/", "./dataset/test/", "./dataset/val/")
   # st.split_data(...) ; train_loader, val_loader = st.get_data_loaders(...)

   # 3. Build the AttnLNP model and train
   # model, optimizer, scheduler = st.create_model_and_optimizer(device, encoding_size,
   #                                   latent_dim, attention=True, self_attention=True)
   # st.train_model(model, criterion, optimizer, scheduler, num_runs, EPOCHS, ...)
   # st.save_model(model, "model.pth")

   # 4. Reconstruct light curves with the trained model
   # model = pred.load_trained_model("model.pth", device, encoding_size, latent_dim, ...)
   # pred.plot_test_data(model, testLoader, criterion, mseMetric, pred.plot_function2, ...)

.. note::

   The snippets above are intentionally illustrative - exact argument lists and return values
   are given in the :doc:`API reference <api/index>`, and the tutorial notebooks demonstrate a
   complete, runnable pipeline.
