#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 13:22:15 2023

@author: jinglian
"""

from pymatgen.core.surface import SlabGenerator, generate_all_slabs
from pymatgen.io.vasp import Poscar
from pymatgen.io.cif import CifWriter
from pymatgen.transformations.standard_transformations import PrimitiveCellTransformation

poscar = Poscar.from_file("/home/jinglian/Documents/crystal-structure/y-NiOOH/Bulk/CONTCAR")
pmg_struct = poscar.structure


miller = [0,0,1]
slabsize= 15 #in angstrom , thickness of the slab to generate
vacsize = 18 #in angstrom, thickness of vacuum to generate
slabgen = SlabGenerator(pmg_struct, miller, slabsize, vacsize, primitive=True, center_slab=True) 
    #can add center_slab=True to center the surface between vacuum
    #can add primitive=False to generate slab with conventional unit cell
slabs = slabgen.get_slabs(symmetrize=False, ftol=0.01, max_broken_bonds=0)

i = 0
for slab in slabs:
    i += 1
    #prim = PrimitiveCellTransformation()
    #prim_slab = prim.apply_transformation(slab)  
    #To check if primitive parameters in SlabGenerator function the same as PrimitiveCellTransformation
    w = CifWriter(slab)
    w.write_file('/home/jinglian/Documents/crystal-structure/y-NiOOH/OER/001slab'+str(i)+'.cif')
