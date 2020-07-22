# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     notebook_metadata_filter: all
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
#   language_info:
#     codemirror_mode:
#       name: ipython
#       version: 3
#     file_extension: .py
#     mimetype: text/x-python
#     name: python
#     nbconvert_exporter: python
#     pygments_lexer: ipython3
#     version: 3.7.7
#   latex_envs:
#     LaTeX_envs_menu_present: true
#     autoclose: false
#     autocomplete: true
#     bibliofile: biblio.bib
#     cite_by: apalike
#     current_citInitial: 1
#     eqLabelWithNumbers: true
#     eqNumInitial: 1
#     hotkeys:
#       equation: Ctrl-E
#       itemize: Ctrl-I
#     labels_anchors: false
#     latex_user_defs: false
#     report_style_numbering: false
#     user_envs_cfg: false
# ---

# %% [markdown]
#  # Jeppe Druedahl & Thomas Høgholm Jørgensen (2017)
#
#  # "[A general endogenous grid method for multi-dimensional models with non-convexities and constraints](https://www.sciencedirect.com/science/article/pii/S0165188916301920?via%3Dihub)"

# %%
import time
from HARK.G2EGM.mcnab import MCNAB

# %%
# Calibration & Setup

params = {
    # Model parameters #
    
    'T': 20, # Number of periods in life
    'Ra': 1.02, # Returns on asset A
    'Rb': 1.04, # Returns on asset B
    'DiscFac': 0.98, # Time discount factor
    'CRRA': 2.0, # Coefficient of relative risk aversion
    'alpha': 0.25, # Labor disutility
    'y': 0.5, # Retirement income
    'eta': 1.0, # Pre-retirement income
    'chi': 0.1, # Transfer cost parameter
    'sigma': 0.0, # Taste shock variance/smoothing parameter
    'verbose': True, # Print solution progress
    
    # Grid and interpolation parameters #
    
    # Common regular grids
    'mlims': (1e-6, 10.0), 'Nm': 100, # m grid
    'nlims': (1e-6, 12.0), 'Nn': 100, # n grid
    'n_phi': 1.25,
    # Post decision grids
    'alims': (1e-6, 8.0), # a grid
    'blims': (1e-6, 14.0), # b grid
    'posdec_factor': 2,
    # retirement grids
    'mlims_ret': (1e-6, 50.0), 'Nm_ret': 500, # m grid when retired (last period)
    'alims_ret': (1e-6, 25.0), 'Na_ret': 500, # a grid when retired
    # interpolation
    'interp_factor': 2}

# %%
# Agent creation and solution

model = MCNAB(**params)
t = time.time()
model.solve()
elapsed = time.time() - t
print("Solution took %f seconds" % elapsed)
