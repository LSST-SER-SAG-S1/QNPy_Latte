# Configuration file for the Sphinx documentation builder.
import os
import sys

# Make the QNPy_Latte package importable (repo root is two levels up).
sys.path.insert(0, os.path.abspath("../.."))

# -- Project information -----------------------------------------------------
project = "QNPy-Latte"
copyright = "2024-2026, SER-SAG-S1 team"
author = "Aman N. Raju, Andjelka Kovacevic, Marina Pavlovic, Dragana Ilic, Iva Cvorovic-Hajdinjak"
release = "0.0.1"
version = "0.0.1"

# -- General configuration ---------------------------------------------------
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.napoleon",        # Google/NumPy-style docstrings
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax",
    "sphinx_copybutton",
    "myst_nb",                    # render Jupyter notebooks (.ipynb) as pages
]

autosummary_generate = True
napoleon_google_docstring = True
napoleon_numpy_docstring = True
autodoc_default_options = {
    "members": True,
    "undoc-members": True,
    "show-inheritance": True,
}
autodoc_typehints = "description"

# Heavy / C-backed dependencies are mocked so the docs build on Read the Docs
# without installing them or importing them at build time.
autodoc_mock_imports = [
    "torch", "numpy", "pandas", "matplotlib", "astropy", "tslearn",
    "minisom", "MiniSom", "plotly", "seaborn", "sklearn", "scipy",
    "dill", "tqdm", "cycler",
]

# Render notebooks from their saved outputs; do NOT re-execute them
# (so the build needs no data, GPU, or the heavy runtime stack).
nb_execution_mode = "off"

templates_path = ["_templates"]
exclude_patterns = []
source_suffix = {".rst": "restructuredtext", ".ipynb": "myst-nb"}

intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "torch": ("https://pytorch.org/docs/stable/", None),
}

# -- HTML output -------------------------------------------------------------
html_theme = "sphinx_rtd_theme"
html_static_path = ["_static"]
html_title = "QNPy-Latte documentation"
html_logo = "_static/QNPy_Latte_logo.jpg"
