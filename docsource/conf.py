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
sys.path.insert(0, os.path.abspath('../modules'))


# -- Project information -----------------------------------------------------

project = 'Cockatoo'
copyright = '2020, Max Eschenbach'
author = 'Max Eschenbach'

# The full version, including alpha/beta/rc tags
release = '0.1.1.0-alpha'

# -- General configuration ---------------------------------------------------

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [
    "sphinx.ext.napoleon",
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.todo",
    "sphinx.ext.githubpages",
    "sphinx.ext.viewcode",
    "sphinx.ext.intersphinx"
]

# napoleon extension settings
napoleon_google_docstring = False
napoleon_use_rtype = False

# mock rhino imports to avoid errors
autodoc_mock_imports = ["Rhino"]

# intersphinx mappings
intersphinx_mapping = {
    'python' : ('https://docs.python.org/2/', None),
    'networkx' : ('https://networkx.github.io/documentation/networkx-1.5/', None)
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path .
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'vs'

# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#

# Theme options are theme-specific and customize the look and feel of a theme
# further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Custom sidebar templates, must be a dictionary that maps document names
# to template names.
#
# The default sidebars (for documents that don't match any pattern) are
# defined by theme itself.  Builtin themes are using these templates by
# default: ``['localtoc.html', 'relations.html', 'sourcelink.html',
# 'searchbox.html']``.
#
# html_sidebars = {}
import sphinx_glpi_theme

html_theme = 'glpi'
html_logo = '_static/glpi.png'
html_theme_path = sphinx_glpi_theme.get_html_themes_path()

# -- Options for LaTeX output --------------------------------------------------

# setting for generating a 'print-version' of the manual
# latex_show_urls = 'footnote'

latex_logo = '_static/latex.jpg'
latex_theme = 'manual'
