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
s1 = Poscar.from_file("/home/jinglian/Documents/crystal-structure/NiOOH/NiOOH-U/VASP-HSE/4x4x4supercel.vasp")
standard_struct = s1.structure
#prim = PrimitiveCellTransformation(0.5)
#prim_struct = prim.apply_transformation(standard_struct)
#prim_struct.to_file("/home/jinglian/Documents/crystal-structure/NiOOH/NiOOH-U/VASP-GGA/prim-uni-gga.vasp",'poscar')
#uniform = prim.apply_transformation(uni)
#reference structure in VASP format
s2 = Poscar.from_file("/home/jinglian/Documents/crystal-structure/NiOOH/shift-stag/VASP-HSE/CONTCAR")
#s2 = Poscar.from_file("/home/jinglian/Documents/crystal-structure/NiOOH/casas.cube.vasp")
#s2 = Poscar.from_file("/home/jinglian/Documents/crystal-structure/NiOOH/Conesa/CONTCAR-stag-rotate.vasp")
#s2 = Poscar.from_file("/home/jinglian/Documents/crystal-structure/NiOOH/EE/CONTCAR.vasp")
#s2 = Poscar.from_file("/home/jinglian/Documents/crystal-structure/NiOOH/Tkalych/CONTCAR.vasp")
#s2 = Poscar.from_file("/home/jinglian/Documents/crystal-structure/NiOOH/Zafran/CONTCAR.vasp")
#structure to transform in VASP format
model = s2.structure
#unit_model = prim.apply_transformation(model)

m = StructureMatcher(ltol=0.2, angle_tol=10,
scale=False,attempt_supercell=True,primitive_cell=False, ignored_species='H')
# ltol is tolerance in fractional length of the ions in structural mapping
#angle_tol is the tolerance in lattice vectors angles in structural mapping
#scale = False prevents volume scaling while matching structures
#attempt_supercell = True allows for expansion of the cell through periodic repetition
#primitive_cell = False prevents reduction of the supercell to their corresponding primitive
#cells prior to matching
#ignored_species=’H’ indicates that structure mapping is done without regard for the H
#atoms
print(m.fit_anonymous(standard_struct, model,skip_structure_reduction=False))
#Returns a mapping which maps s1 and s2 onto each other
result = m.get_s2_like_s1(standard_struct, model,include_ignored_species=True)
#unit_model.to_file("/home/jinglian/Documents/crystal-structure/NiOOH/shift-stag/VASP-mGGA/primitive.cif","cif")
result.to_file("/home/jinglian/Documents/crystal-structure/NiOOH/shift-stag/VASP-HSE/mapped-stag-hse.vasp","poscar")
#transforms vectors of s2 to be similar to s1, within tolerance
print(m.get_transformation(standard_struct,model)) #Returns lattice transformation matrix
print(m.get_rms_dist(standard_struct,model)) #Returns root mean square distance between s1 and s2