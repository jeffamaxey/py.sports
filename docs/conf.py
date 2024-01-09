"""Sphinx configuration."""
project = "Py.Sports"
author = "Jeff Maxey"
copyright = "2024, Jeff Maxey"
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.napoleon",
    "sphinx_click",
    "myst_parser",
]
autodoc_typehints = "description"
html_theme = "furo"
