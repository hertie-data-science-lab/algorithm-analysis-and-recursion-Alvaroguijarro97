# -*- coding: utf-8 -*-
"""
Created on Mon Feb 20 08:24:20 2023

@author: Hannah
"""

n=3
def TowerOfHanoi(n, from_rod, to_rod, aux_rod):
    if n == 0:
        return
    #Move all the plates except for the biggest one to the aux_rod
    TowerOfHanoi(n - 1, from_rod, aux_rod, to_rod)
    #Move the biggest rod to the to_rod
    print("Move disk", n, "from rod", from_rod, "to rod", to_rod)
    TowerOfHanoi(n - 1, aux_rod, to_rod, from_rod)

TowerOfHanoi(n, 'A', 'C', 'B')
