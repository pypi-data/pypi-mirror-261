#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# cellmaps_generate_hierarchy documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import os
import sys
import re

sys.path.insert(0, os.path.abspath('..'))

import cellmaps_generate_hierarchy

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinx.ext.intersphinx',
              'sphinx.ext.autosectionlabel',
              'sphinx.ext.viewcode',
              'sphinx_copybutton']

# intersphinx mapping
intersphinx_mapping = {"python": ("https://docs.python.org/3", None),
                       "requests": ("https://requests.readthedocs.io/en/latest/", None),
                       "networkx": ("http://networkx.org/documentation/stable/", None),
                       "pandas": ("https://pandas.pydata.org/docs/", None),
                       "numpy": ("https://numpy.org/doc/stable/", None)
                      }

# prefix document on section labels for references
autosectionlabel_prefix_document = True

# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
# source_suffix = ['.rst', '.md']
source_suffix = '.rst'

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = u'cellmaps_generate_hierarchy'
copyright = u"2023, The Regents of the University of California"
author = u"Christopher Churas"

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = None
# The full version, including alpha/beta/rc tags.
release = None

init_file = os.path.join('..', 'cellmaps_generate_hierarchy', '__init__.py')
with open(init_file) as ver_file:
    for line in ver_file:
        if line.startswith('__version__'):
            release = re.sub("'", "", line[line.index("'"):])
            version = '.'.join(release.split('.')[0:2])

if release is None or version is None:
    raise Exception('Unable to extract version from ' + init_file)

# automatically document constructor
autoclass_content = 'both'


# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
#
# This is also used if you do content translation via gettext catalogs.
# Usually you set "language" from the command line for these cases.
language = 'en'

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = False


# -- Options for HTML output -------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
html_theme = 'sphinx_rtd_theme'

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
# html_static_path = ['_static']


# -- Options for HTMLHelp output ---------------------------------------

# Output file base name for HTML help builder.
htmlhelp_basename = 'cellmaps_generate_hierarchydoc'


# -- Options for LaTeX output ------------------------------------------

latex_elements = {
    # The paper size ('letterpaper' or 'a4paper').
    #
    # 'papersize': 'letterpaper',

    # The font size ('10pt', '11pt' or '12pt').
    #
    # 'pointsize': '10pt',

    # Additional stuff for the LaTeX preamble.
    #
    # 'preamble': '',

    # Latex figure (float) alignment
    #
    # 'figure_align': 'htbp',
}

# Grouping the document tree into LaTeX files. List of tuples
# (source start file, target name, title, author, documentclass
# [howto, manual, or own class]).
latex_documents = [
    (master_doc, 'cellmaps_generate_hierarchy.tex',
     u'CM4AI Generate Hierarchy Documentation',
     u'Christopher Churas', 'manual'),
]


# -- Options for manual page output ------------------------------------

# One entry per manual page. List of tuples
# (source start file, name, description, authors, manual section).
man_pages = [
    (master_doc, 'cellmaps_generate_hierarchy',
     u'CM4AI Generate Hierarchy Documentation',
     [author], 1)
]


# -- Options for Texinfo output ----------------------------------------

# Grouping the document tree into Texinfo files. List of tuples
# (source start file, target name, title, author,
#  dir menu entry, description, category)
texinfo_documents = [
    (master_doc, 'cellmaps_generate_hierarchy',
     u'CM4AI Generate Hierarchy Documentation',
     author,
     'cellmaps_generate_hierarchy',
     'One line description of project.',
     'Miscellaneous'),
]



