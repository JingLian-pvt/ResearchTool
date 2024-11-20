#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:11:42 2023

@author: jinglian
/home/jinglian/Documents/crystal-structure/NiFeOOH/Overpotential-lit/step6
"""

from ase.io import read, write

write('/home/jinglian/Documents/crystal-structure/graphene/2x2/2x2-relaxed.vasp', read('/home/jinglian/Documents/crystal-structure/graphene/2x2/2x2.relax.out', format='espresso-out'), format='vasp')