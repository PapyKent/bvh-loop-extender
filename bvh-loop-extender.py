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
file = file_path+file_name+".bvh"

def loop_extender(ext_number, file):
    anim, names, frametime = BVH.load(file_path+file_name+".bvh")
    frames_number = anim.positions.shape[0]
    new_frames_number = frames_number * ext_number
    elements_number =  anim.positions.shape[1]
    new_positions = np.zeros((frames_number*ext_number, elements_number, anim.positions.shape[2]))
    new_rotations = anim.rotations.copy()
    for i in range(0,ext_number-1):
        new_rotations.qs = np.vstack((new_rotations.qs, anim.rotations.qs))


    for i in range(0,new_frames_number-1):
        for j in range (0, elements_number-1):       
            if i >= frames_number :
                new_positions[i][j] = anim.positions[i%frames_number][j]+(0,0,new_positions[int(i/frames_number)*frames_number-1][j][2])         
                new_rotations.qs[i][j] = anim.rotations.qs[i%frames_number][j]
            else:
                new_positions[i][j] = anim.positions[i][j]
                new_rotations.qs[i][j] = anim.rotations.qs[i][j]
           

    new_anim = Animation.Animation(new_rotations, new_positions, anim.orients, anim.offsets, anim.parents)

    BVH.save(file_path+"test.bvh", new_anim, names, frametime)
    
    return;

loop_extender(10,file)


