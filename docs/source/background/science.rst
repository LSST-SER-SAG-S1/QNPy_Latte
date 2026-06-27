Scientific background
======================

Motivation
----------

Much of what we can learn about quasars is encoded in their variability. LSST will deliver a
very large number of quasar light curves over its ten-year run, but with seasonal gaps. To use
these data for variability analysis the gaps must be modelled, and at LSST scale the model must
be data-driven, computationally inexpensive, non-parametric, and able to interpolate - while
also exposing physically interpretable internal representations.

Attentive Latent Neural Processes (AttnLNP)
-------------------------------------------

QNPy-Latte upgrades the Conditional Neural Process used in `QNPy
<https://github.com/kittytheastronaut/QNPy-0.0.2>`_ with a latent path and attention, which
addresses CNP underfitting and poor sampling.

* **Deterministic path** - observation times and magnitudes are encoded by an MLP into a
  per-point representation; self-attention up-weights the more informative points; a
  cross-attention step produces a target-time-specific representation.
* **Latent path** - per-point representations are averaged into a global representation, mapped
  by an MLP to a multivariate Gaussian latent space that can be sampled.
* **Decoder** - latent samples are combined with the deterministic representation and decoded by
  an MLP to a predicted magnitude at each target time.

Optionally, input and target times can be encoded with an LSTM/RNN layer for improved
reconstruction (Qin et al. 2019). The architecture follows Kim et al. 2019.

Self-Organizing Maps (SOM)
--------------------------

Light curves are clustered with SOMs (built on `MiniSom
<https://github.com/JustGlowing/minisom>`_) before modelling. Clustering partitions the dataset
for faster modelling and yields topologically balanced groups; SOMs are unsupervised, support
many clusters, and can incorporate new data without full retraining. Best-matching units can be
used directly as clusters or merged by density/gradient analysis into fewer, larger clusters.

Parameter and transfer-function recovery
----------------------------------------

Following Park et al. 2021, the hidden representation of the light curve is used to infer
physical parameters. An MLP head - trained jointly or attached to a pre-trained model - is
trained against theoretical transfer functions, enabling recovery of the **transfer function**
and related properties of the central-engine region, purely data-driven.

See :doc:`../references` for citations.
