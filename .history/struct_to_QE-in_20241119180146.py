#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 25 15:11:42 2023

@author: jinglian
/home/jinglian/Documents/crystal-structure/NiFeOOH/Overpotential-lit/step6
"""

from ase.io import read, write

write('/home/jinglian/Documents/crystal-structure/graphene/3x3.vcrelax.in', read('/home/jinglian/Documents/crystal-structure/graphene/3x3-graph.vasp', format='vasp'), format='espresso-in')