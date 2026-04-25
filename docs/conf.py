# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os
import sys
sys.path.insert(0, os.path.abspath('..'))


# -- Project information -----------------------------------------------------

project = "DeFiPy"
copyright = "2022-2026, Ian Moore"
author = "Ian Moore"
html_show_sphinx = False
html_baseurl = 'https://defipy.readthedocs.io/en/latest/'
sitemap_url_scheme = "{link}"

html_meta = {
    "description": "DeFiPy is a unified Python SDK for agentic DeFi — analytics, simulation, and MCP tool schemas for autonomous agents. Hand-derived AMM math across Uniswap V2, V3, Balancer, and Stableswap.",
    "keywords": "DeFi, DeFiPy, Python, agentic DeFi, on-chain analytics, AMM math, liquidity pools, simulation, MCP, Uniswap, Balancer, Stableswap, LLM, autonomous agents",
    "author": "Ian Moore",
}

# -- General configuration ---------------------------------------------------
# -- General configuration

extensions = [
    "sphinx.ext.duration",
    "sphinx.ext.doctest",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.intersphinx",
    "nbsphinx",
    "sphinx_design",
    "sphinx_sitemap",
    "sphinxcontrib.googleanalytics",
]

exclude_patterns = [
    "_build",
    "_legacy",
    "_legacy/**",
    "Thumbs.db",
    ".DS_Store",
    ".ipynb_checkpoints",
    ".ipynb_checkpoints/**",
    "**/.ipynb_checkpoints",
    "**/.ipynb_checkpoints/**",
]



intersphinx_mapping = {
    "rtd": ("https://docs.readthedocs.io/en/stable/", None),
    "python": ("https://docs.python.org/3/", None),
    "sphinx": ("https://www.sphinx-doc.org/en/master/", None),
}
intersphinx_disabled_domains = ["std"]

templates_path = ["_templates"]

# -- Options for EPUB output
epub_show_urls = "footnote"

# -- Google Analytics -------------------------------------------------

googleanalytics_id = 'G-RVXH17JXT0'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = "sphinx_rtd_theme"

# https://sphinx-rtd-theme.readthedocs.io/en/stable/configuring.html#theme-options 
html_theme_options = {  
    'logo_only': True,
    'style_nav_header_background': '#673147',
    'navigation_depth': 4, 
    'collapse_navigation': True,
#    'collapse_navigation': False,  # Expand all nested items by default
    'sticky_navigation': True    # Keep sidebar fixed while scrolling
#    'navigation_depth': 4,        # Allow deeper nesting (default is 4)
}

html_logo = "defipy_logo.png"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = []

# Files copied verbatim to the build root (e.g. robots.txt)
html_extra_path = ['robots.txt']

# -- nbsphinx ----------------------------------------------------------------
nbsphinx_execute = "never"
nbsphinx_prompt_width = "0"