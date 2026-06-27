Clustering with SOMs
====================

The :doc:`../api/clustering_with_som` module loads, pads, scales and clusters light curves.

.. code-block:: python

   from QNPy_Latte import Clustering_with_SOM as som

   # Load light curves from a folder (single band shown here)
   light_curves, ids = som.Load_Light_Curves("Light_Curves", one_filter=True, filters="a")

   # Pad to a common minimum length, then scale to a common range
   padded = som.Pad_Light_Curves(light_curves, minimum_length=100)
   scaled = som.scale_curves(padded, what_scaler="default", scale_times=True)

   # Train a 1-D SOM
   som_model = som.SOM_1D(scaled, learning_rate=0.1, sigma=1.0,
                          topology="rectangular", pca_init=True)

   # Assign clusters and inspect them
   cluster_map = som.Assign_Cluster_Labels(som_model, scaled, ids)
   som.SOM_Clusters_Histogram(cluster_map)
   som.SOM_Distance_Map(som_model)

   # Save the members of a chosen cluster to disk for downstream modelling
   som.save_chosen_cluster(chosen_cluster=0, cluster_map=cluster_map,
                           source_path="./Light_Curves", save_path="./cluster_0")

Multi-band clustering is available through ``som.multi_band_clustering(...)`` and
``som.Gradient_Cluster_Map(...)`` provides gradient-based clustering for large SOMs. Cluster
properties (variability, luminosities/masses, structure functions) are computed via
``som.Cluster_Properties(...)`` and related helpers.

.. seealso:: The ``Clustering_Tutorial_Notebooks`` folder (Basic, Advanced Visualization,
   Advanced Clustering, Multiband) for runnable examples.
