import os
import sys
sys.path.insert(0, os.path.abspath('..'))  # Add the project root to sys.path

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.napoleon',  # If using Google or NumPy style docstrings
]

print("CONF.PY LOADED")

# Configuration file for the Sphinx documentation builder.


# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Average_Squares'
copyright = '2025, Ella Turtle'
author = 'Ella Turtle'
release = '0.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'alabaster'
html_static_path = ['_static']
