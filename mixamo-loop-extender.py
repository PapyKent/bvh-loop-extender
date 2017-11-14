# -*- coding: utf-8 -*-
"""
Created on Mon Nov 13 12:13:24 2017

@author: Quentin
"""


import sys
import os
import numpy as np


sys.path.append('./motion')

import math as math
import BVH as BVH
import Animation as Animation
import Quaternions as Quaternions


file_name = "mixamo"
file_path= "./data/animations/"


file_object = open(file_path+file_name+"_footsteps.txt", 'w')

anim, names, frametime = BVH.load(file_path+file_name+".bvh")
frames_number = len(anim)

new_positions = np.zeros((anim.positions.shape[0]*2, anim.positions.shape[1], anim.positions.shape[2]))
new_rotations = anim.rotations.copy()
new_rotations.qs = np.vstack((new_rotations.qs, anim.rotations.qs))


for i in range(0,76-1):
    for j in range (0, 55-1):       
        if i >= 37 :
            new_positions[i][j] = anim.positions[i-37][j]+(0,0,anim.positions[36][j][2])         
            new_rotations.qs[i][j] = anim.rotations.qs[i-37][j]
        else:
            new_positions[i][j] = anim.positions[i][j]
            new_rotations.qs[i][j] = anim.rotations.qs[i][j]
           
  
print(new_rotations.qs)
print("////////////////////////////////")
print(anim.rotations.qs)  
       

new_anim = Animation.Animation(new_rotations, new_positions, anim.orients, anim.offsets, anim.parents)



BVH.save(file_path+"test.bvh", new_anim, names, frametime)


