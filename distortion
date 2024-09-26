#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:29:58 2024

@author: jinglian
"""

from pymatgen.core.surface import SlabGenerator, generate_all_slabs
from pymatgen.io.vasp import Poscar
from pymatgen.io.cif import CifWriter
from pymatgen.transformations.standard_transformations import PrimitiveCellTransformation
import os
import sys
import ase
import numpy as np
import pymatgen
import doped
from importlib_metadata import version

import shakenbreak.distortions
import shakenbreak.input
from pymatgen.core.structure import Structure

poscar = Poscar.from_file("/home/jinglian/Documents/crystal-structure/NiFeOOH/vcrelax/Uniform/distort.cube.vasp")
pmg_struct = poscar.structure

distort_cells = shakenbreak.distortions.rattle(pmg_struct)

print(distort_cells)