Input data format
=================

Light curves are **CSV files with three columns**: ``mjd``, ``mag`` and ``magerr``.

Place all light curves in a single folder, or - for multi-band data - separate them by band
under one parent directory::

    Light_Curves/
        source_0001.csv
        source_0002.csv

    # or, multi-band:
    Light_Curves/
        u_band/source_0001.csv
        g_band/source_0001.csv

Each file looks like:

.. code-block:: text

   mjd,mag,magerr
   59000.12,19.83,0.04
   59005.31,19.79,0.05
   ...

For the parameter-recovery workflow you additionally supply theoretical transfer functions and a
dataframe of the parameters used to generate each light curve (see :doc:`parameters`).
