Parameter and transfer-function recovery
========================================

The parameter workflow mirrors the modelling workflow but additionally supplies **theoretical
transfer functions** and a **dataframe of generating parameters** for each light curve. The
model then reconstructs the transfer function and the parameters alongside the light curve.

.. code-block:: python

   from QNPy_Latte import PREDICTION as pred

   # Provide transfer-function directory and parameter dataframe to the loaders, e.g.:
   # testLoader = pred.load_test_data(DATA_PATH_TEST, num_target_smooth=400,
   #                                  tf_dir="transfer_functions/",
   #                                  param_df=params, param_columns=["tau", "mass"])

   # Plot mean and per-object transfer functions and parameter comparisons
   # pred.Plotting_TF_Mean(predicted_tf, actual_tf, ttau, "tf_plots/")
   # pred.Plotting_TF_Individual(dataLoader, predicted_tf, actual_tf, ttau, "tf_plots/")
   # pred.Plotting_Param_Individual(dataLoader, predicted_params, actual_params,
   #                                columns=["tau", "mass"], PARAM_SAVE_PATH="param_plots/")

.. seealso:: ``Modelling_Tutorial_Notebooks_w_Params`` for the full parameter-recovery pipeline.
