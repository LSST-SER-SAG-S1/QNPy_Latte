Overview
========

QNPy-Latte is organized as eight modules grouped into two workflows that can be used
independently or together:

**Clustering workflow**

* :doc:`Clustering_with_SOM <../api/clustering_with_som>` - load, pad, scale and cluster light
  curves with Self-Organizing Maps; visualize clusters; compute cluster properties.

**Modelling workflow**

* :doc:`PREPROCESS <../api/preprocess>` - outlier cleaning, padding and magnitude transforms.
* :doc:`DATASETCLASS <../api/datasetclass>` - the PyTorch ``Dataset`` and collate function.
* :doc:`MODEL_ARCHITECTURE <../api/model_architecture>` - encoders, decoder and the full AttnLNP.
* :doc:`ATTENTION <../api/attention>` - attention building blocks (dot, multihead, transformer).
* :doc:`LOSS_METRICS <../api/loss_metrics>` - log-probability loss plus MSE/MAE metrics.
* :doc:`SPLITTING_AND_TRAINING <../api/splitting_and_training>` - data splitting, loaders, model
  construction, the training loop and loss/metric plots.
* :doc:`PREDICTION <../api/prediction>` - load a trained model, reconstruct light curves and
  plot transfer functions and recovered parameters.

Recommended order: :doc:`data_format` -> :doc:`clustering` -> :doc:`preprocessing` ->
:doc:`training` -> :doc:`modelling` -> :doc:`parameters`.
