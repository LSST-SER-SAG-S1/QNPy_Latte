# QNPy-Latte documentation - setup notes

These files add a full **Sphinx + Read the Docs** documentation site to your fork.

## What was added
```
.readthedocs.yaml          # Read the Docs build config (repo root)
docs/
  requirements.txt         # Sphinx + theme (used by RTD and local builds)
  Makefile  make.bat       # local build entry points
  source/
    conf.py                # Sphinx config (mocks heavy deps so RTD builds cleanly)
    index.rst              # landing page + toctree
    installation.rst  quickstart.rst
    user_guide/            # data format, clustering, preprocessing, training, modelling, parameters
    background/science.rst # AttnLNP / SOM / parameter recovery
    api/                   # one auto-generated page per module
    references.rst  contributing.rst  changelog.rst
```

## 1. Fork & drop in
Fork https://github.com/rajuaman1/QNPy_Latte, then copy `.readthedocs.yaml` and the `docs/`
folder into the **root** of your fork (next to `pyproject.toml`). Commit and push.

## 2. Build locally (optional but recommended)
```bash
pip install -r docs/requirements.txt
cd docs && make html
# open docs/build/html/index.html
```

## 3. Publish on Read the Docs
1. Sign in at https://readthedocs.org with your GitHub account.
2. "Import a Project" -> pick your QNPy_Latte fork.
3. RTD auto-detects `.readthedocs.yaml` and builds. Your site goes live at
   `https://<your-project-slug>.readthedocs.io`.

## Notes
- The API pages use `automodule`, so they update automatically as docstrings are added to the
  code - the more NumPy/Google-style docstrings you add, the richer the API reference.
- Heavy dependencies (torch, astropy, tslearn, ...) are mocked in `conf.py`, so RTD does **not**
  need to install them to build the docs.
- If you later add the tutorial notebooks to the repo, you can surface them by adding
  `nbsphinx` (or `myst-nb`) to `docs/requirements.txt` and a `tutorials/` toctree.
- For the closeout "Documentation" field, use your published RTD URL.

## Adding your Jupyter notebooks
The site renders `.ipynb` files via **myst-nb** (already configured — no pandoc needed).

1. Open each notebook, **Run All**, then **Save** (the site shows the *saved* outputs; it does
   not re-run notebooks, so they need no data or GPU at build time).
2. Copy the `.ipynb` files into the matching folder:
   - `docs/source/tutorials/clustering/`
   - `docs/source/tutorials/modelling/`
   - `docs/source/tutorials/modelling_with_params/`
3. Rebuild: from `docs/`, run `make clean && make html`. The notebooks appear automatically
   under the **Tutorials** section — you don't edit any `.rst` file.

(The empty-folder build warnings disappear once each folder has at least one notebook.)
