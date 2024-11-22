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
# import os
# import sys
# sys.path.insert(0, os.path.abspath('../uiautomator2'))
import os
import yaml
import uiautomator2

# -- Project information -----------------------------------------------------

master_doc = "index"

project = "uiautomator2"
copyright = "2020-2024, codeskyblue"
author = "codeskyblue"


# -- General configuration ---------------------------------------------------
locale_dirs = ['locale/']   # path is an example but recommended.
gettext_compact = False     # optional.

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom
# ones.
extensions = [  # For internationalization
    "sphinx.ext.autodoc",
    "sphinx.ext.autosummary",
    "sphinx.ext.coverage",
    "sphinx.ext.viewcode",
]

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------
html_context = {
  'current_version' : "1.0",
  'versions' : [["1.0", "link to 1.0"], ["2.0", "link to 2.0"]],
  'current_language': 'en',
  'languages': [["en", "link to en"], ["zh", "link to zh"]]
}

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]

build_all_docs = os.environ.get("build_all_docs")
pages_root = os.environ.get("pages_root", "")

if build_all_docs is not None:
  current_language = os.environ.get("current_language")
  current_version = os.environ.get("current_version")

  html_context = {
    'current_language' : current_language,
    'languages' : [],
    'current_version' : current_version,
    'versions' : [],
  }

  if current_version == 'latest':
    html_context['languages'].append(['en', pages_root])
    html_context['languages'].append(['zh_cn', pages_root+'/zh_cn'])

  if current_language == 'en':
    html_context['versions'].append(['latest', pages_root])
  if current_language == 'zh_cn':
    html_context['versions'].append(['latest', pages_root+'/zh_cn'])

  with open("versions.yaml", "r") as yaml_file:
    docs = yaml.safe_load(yaml_file)

  if current_version != 'latest':
    for language in docs[current_version].get('languages', []):
      html_context['languages'].append([language, pages_root+'/'+current_version+'/'+language])

  for version, details in docs.items():
    html_context['versions'].append([version, pages_root+'/'+version+'/'+current_language])