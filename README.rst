DeFiPy Documentation
============================

Sphinx source for `DeFiPy <https://github.com/defipy-devs/defipy>`_'s documentation site, published at `defipy.org <https://defipy.org>`_ and `defipy.readthedocs.io <https://defipy.readthedocs.io>`_.

DeFiPy is a unified Python SDK for agentic DeFi, covering analytics, simulation, and LLM-native tool schemas for autonomous agents. For product information, see the `main repository <https://github.com/defipy-devs/defipy>`_ or the `rendered docs <https://defipy.org>`_.

Repo contents
--------------------------

* ``docs/`` — Sphinx source (``.rst`` pages, ``.ipynb`` notebooks, ``conf.py``)
* ``docs/agentic_primitives/notebooks/`` — executable category notebooks (9 files covering all 21 primitives)
* ``docs/math/`` — DeFi math reference notebooks
* ``docs/img/`` — images, banners, diagrams
* ``.readthedocs.yaml`` — RTD build configuration

Building locally
--------------------------

Requires Python 3.10+:

.. code-block:: console

    pip install -r docs/requirements.txt
    cd docs
    sphinx-build -b html . _build/html

Open ``_build/html/index.html`` in a browser to view the rendered site.

Notebook authoring
--------------------------

Category notebooks use ``nbsphinx`` with ``nbsphinx_execute = "never"`` — outputs are baked into the committed ``.ipynb`` files. To edit a notebook:

.. code-block:: console

    jupyter notebook docs/agentic_primitives/notebooks/<category>.ipynb
    # edit, Kernel → Restart & Run All, save

For source-controlled editing via ``jupytext``, percent-format ``.py`` sources can be maintained alongside ``.ipynb`` files. See ``.readthedocs.yaml`` for the RTD build pipeline.

Contributing
--------------------------

Documentation fixes, typo corrections, and notebook improvements are welcome. Larger structural changes (IA, toctree, theming) should be discussed via issue first.

For library-level changes, see the `main repository <https://github.com/defipy-devs/defipy>`_.

License
--------------------------

Apache License, Version 2.0. See ``LICENSE``.
