#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 16:29:58 2024

generate an amorphous system based on shake N break

@author: jinglian
"""

from pymatgen.io.vasp import Poscar
import shakenbreak.distortions

poscar = Poscar.from_file("/home/jinglian/Documents/crystal-structure/NiFeOOH/vcrelax/Uniform/distort.cube.vasp")
pmg_struct = poscar.structure

distort_cells = shakenbreak.distortions.rattle(pmg_struct)

print(distort_cells)