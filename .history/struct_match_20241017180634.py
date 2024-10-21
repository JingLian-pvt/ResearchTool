#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 17 17:08:38 2024

@author: jinglian
"""

import pymatgen as mg
from pymatgen.io.vasp import Poscar
from pymatgen.analysis.structure_matcher import StructureMatcher
from pymatgen.transformations.standard_transformations import PrimitiveCellTransformation
s1 = Poscar.from_file("/home/jinglian/Documents/crystal-structure/NiOOH/NiOOH-U/FM-vcrelax/uniform-CONTCAR.vasp")
uniform = s1.structure
prim = PrimitiveCellTransformation(0.5)
#uniform = prim.apply_transformation(uni)
#reference structure in VASP format
s2 = Poscar.from_file("/home/jinglian/Documents/crystal-structure/NiOOH/shift-stag/FM-vcrelax/FM-D3-relaxed.vasp")
#structure to transform in VASP format
mc = s2.structure
stag = prim.apply_transformation(mc)

m = StructureMatcher(ltol=0.2, angle_tol=5,
scale=False,attempt_supercell=True,primitive_cell=False, ignored_species='H')
# ltol is tolerance in fractional length of the ions in structural mapping
#angle_tol is the tolerance in lattice vectors angles in structural mapping
#scale = False prevents volume scaling while matching structures
#attempt_supercell = True allows for expansion of the cell through periodic repetition
#primitive_cell = False prevents reduction of the supercell to their corresponding primitive
#cells prior to matching
#ignored_species=’H’ indicates that structure mapping is done without regard for the H
#atoms
print(m.fit_anonymous(uniform, stag,skip_structure_reduction=True))
#Returns a mapping which maps s1 and s2 onto each other
result = m.get_s2_like_s1(uniform, stag,include_ignored_species=True)
result.to_file("/home/jinglian/Documents/crystal-structure/NiOOH/shift-stag/FM-vcrelax/sup2.cif","cif")
#transforms vectors of s2 to be similar to s1, within tolerance
print(m.get_transformation(uniform,stag)) #Returns lattice transformation matrix
print(m.get_rms_dist(uniform, stag)) #Returns root mean square distance between s1 and s2