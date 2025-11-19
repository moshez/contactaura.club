# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

import os
import glob

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'ContactAura RPG Materials'
copyright = '2025, ContactAura'
author = 'ContactAura'
release = '1.0'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']

# Source directory for documentation
source_suffix = '.rst'
master_doc = 'index'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'furo'
html_title = 'ContactAura RPG Materials'

# Furo theme options for professional, nuanced styling
html_theme_options = {
    "light_css_variables": {
        "color-brand-primary": "#2962ff",
        "color-brand-content": "#2962ff",
        "color-background-primary": "#ffffff",
        "color-background-secondary": "#f8f9fa",
        "color-foreground-primary": "#212529",
        "color-foreground-secondary": "#6c757d",
    },
    "dark_css_variables": {
        "color-brand-primary": "#5e92f3",
        "color-brand-content": "#5e92f3",
        "color-background-primary": "#1e1e1e",
        "color-background-secondary": "#2d2d2d",
        "color-foreground-primary": "#e4e4e4",
        "color-foreground-secondary": "#b0b0b0",
    },
    "sidebar_hide_name": False,
}

html_static_path = ['_static']

# -- Auto-discovery of RST files ---------------------------------------------

def find_rst_files():
    """Find all .rst files in the docs/ directory (excluding index.rst)"""
    docs_dir = os.path.join(os.path.dirname(__file__), 'docs')
    if not os.path.exists(docs_dir):
        return []

    rst_files = []
    for rst_file in glob.glob(os.path.join(docs_dir, '*.rst')):
        basename = os.path.basename(rst_file)
        # Skip index.rst as it's the main document
        if basename != 'index.rst':
            # Remove .rst extension for Sphinx
            rst_files.append(f"docs/{basename[:-4]}")

    return sorted(rst_files)

# Store auto-discovered files for use in index.rst
autodiscovered_docs = find_rst_files()
