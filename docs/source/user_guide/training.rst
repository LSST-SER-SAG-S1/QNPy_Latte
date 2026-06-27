Training the model
==================

The :doc:`../api/splitting_and_training` module splits the data, builds loaders, constructs the
AttnLNP and runs the training loop.

.. code-block:: python

   import torch
   from QNPy_Latte import SPLITTING_AND_TRAINING as st
   from QNPy_Latte import LOSS_METRICS as lm

   device = "cuda" if torch.cuda.is_available() else "cpu"

   # 1. Create split folders and split the transformed data
   st.create_split_folders("./dataset/train/", "./dataset/test/", "./dataset/val/")
   # st.split_data(files, DATA_SRC, TRAIN_FOLDER, TEST_FOLDER, VAL_FOLDER)

   # 2. Build data loaders
   # train_loader, val_loader = st.get_data_loaders(data_path_train, data_path_val,
   #                                                batch_size=32, augment=True)

   # 3. Construct the model and optimizer (latent + attention paths)
   # model, optimizer, scheduler = st.create_model_and_optimizer(
   #     device, encoding_size=128, latent_dim=64,
   #     attention=True, self_attention=True, attention_type="scaledot")

   # 4. Train; metrics are written to CSV and can be plotted afterwards
   criterion = lm.LogProbLoss()
   mseMetric, maeMetric = lm.MSELoss(), lm.MAELoss()
   # st.train_model(model, criterion, optimizer, scheduler, num_runs, EPOCHS,
   #                EARLY_STOPPING_LIMIT, mseMetric, maeMetric, device, DATA_PATH_TRAIN, ...)
   # st.save_model(model, "model.pth")

   # 5. Visualize training history
   # st.plot_loss("history_loss_train.csv", "history_loss_val.csv", "epoch_counter.csv")

.. seealso:: ``Modelling_Tutorial_Notebooks/Training_Model`` for a complete configuration.
