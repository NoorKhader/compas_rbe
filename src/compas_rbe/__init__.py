"""
********************************************************************************
compas_rbe
********************************************************************************

.. currentmodule:: compas_rbe


.. toctree::
    :maxdepth: 1

    compas_rbe.datastructures
    compas_rbe.equilibrium
    compas_rbe.interfaces
    compas_rbe.rhino
    compas_rbe.viewer

"""

from __future__ import print_function

import os
import sys

__author__ = 'Tom Van Mele'
__copyright__ = 'Copyright 2017 - Block Research Group, ETH Zurich'
__license__ = 'MIT License'
__email__ = 'vanmelet@ethz.ch'
__version__ = '0.1.0'

HERE = os.path.dirname(__file__)

HOME = os.path.abspath(os.path.join(HERE, '../../'))
DATA = os.path.abspath(os.path.join(HOME, 'data'))
DOCS = os.path.abspath(os.path.join(HOME, 'docs'))
SRC = os.path.abspath(os.path.join(HOME, 'src'))
TEMP = os.path.abspath(os.path.join(HOME, 'temp'))

# # specify the python location (can be in the conda environment as well)
# PYTHON = '/Users/kaot/anaconda3/envs/rbe/bin/python'


def _find_resource(filename):
    filename = filename.strip('/')
    return os.path.abspath(os.path.join(DATA, filename))


def get(filename):
    return _find_resource(filename)


def requirements():
    with open(os.path.join(HERE, '../requirements.txt')) as f:
        for line in f:
            print(line.strip())


def reload():
    pass


__all__ = ['HOME', 'DATA', 'DOCS', 'SRC', 'TEMP', 'get']
