Preprocessing
=============

The :doc:`../api/preprocess` module prepares raw light curves for the model: it removes
outliers, pads curves to a common length, and transforms magnitudes/times into the range the
model expects (``[-2, 2]``).

.. code-block:: python

   from QNPy_Latte import PREPROCESS as pre

   # Remove outliers with a median/polynomial filter
   pre.clean_outliers_median("Light_Curves", "cleaned", threshold=0.25, median=True)

   # Pad each curve to a fixed number of observations
   pre.backward_pad_curves("cleaned", "padded", desired_observations=100, verbose=1)

   # Transform and save (optionally with augmentation); `transform` is provided by the module
   # pre.transform_and_save(files, data_src="padded", data_dst="transformed",
   #                        transform=pre.transform, augment=False)

The padding step records the transform coefficients so that predictions can later be mapped back
to physical units (see :func:`QNPy_Latte.PREDICTION.back_x` / :func:`QNPy_Latte.PREDICTION.back_y`).
