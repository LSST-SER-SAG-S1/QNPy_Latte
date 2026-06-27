Reconstructing light curves
===========================

With a trained model, the :doc:`../api/prediction` module reconstructs light curves and writes
both plots and the numerical reconstructions.

.. code-block:: python

   import torch
   from QNPy_Latte import PREDICTION as pred
   from QNPy_Latte import LOSS_METRICS as lm

   device = "cuda" if torch.cuda.is_available() else "cpu"

   # Load the trained AttnLNP
   # model = pred.load_trained_model("model.pth", device, encoding_size=128, latent_dim=64,
   #            latent_mlp_size=128, attention=True, self_attention=True)

   criterion = pred.get_criteria(no_latent_space_sample=1)
   mseMetric = lm.MSELoss()

   # Load test data and plot reconstructions
   # testLoader = pred.load_test_data(DATA_PATH_TEST, num_target_smooth=400)
   # pred.plot_test_data(model, testLoader, criterion, mseMetric, pred.plot_function2, ...)
   # pred.save_test_metrics(OUTPUT_PATH, testMetrics)

Predictions are produced in the model's internal scale; use
:func:`QNPy_Latte.PREDICTION.back_x` and :func:`QNPy_Latte.PREDICTION.back_y` (with the saved
transform coefficients) to return to physical units.
