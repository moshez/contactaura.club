# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

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
    'myst_parser',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store', 'README.md']

# Source directory for documentation
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
master_doc = 'index'

# MyST Parser configuration
myst_enable_extensions = [
    "colon_fence",      # ::: fence syntax
    "deflist",          # Definition lists
    "tasklist",         # Task lists (- [ ] and - [x])
    "fieldlist",        # Field lists
]

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
