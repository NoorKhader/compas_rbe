from __future__ import print_function
from __future__ import absolute_import
from __future__ import division


import rhinoscriptsyntax as rs
import scriptcontext as sc

import Rhino

import os
import sys

import compas_rhino
import compas_rbe

from compas_rbe.datastructures import Assembly
from compas_rbe.rhino import AssemblyArtist


__commandname__ = "RBE_draw_forces"


def RunCommand(is_interactive):
    if not 'RBE' in sc.sticky:
        raise Exception('Initialise RBE first!')
    RBE = sc.sticky['RBE']

    try:

        assembly = RBE['assembly']

        scale = rs.GetReal("Scale", 0.25, 0.01, 10.0)

        artist = AssemblyArtist(assembly, layer=RBE['settings']['layer'])

        artist.clear_forces();
        artist.draw_forces(scale=scale)
        artist.redraw()

    except Exception as error:

        print(error)