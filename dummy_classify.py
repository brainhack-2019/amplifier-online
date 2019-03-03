#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:17:04 2019

@author: joshbierbrier
"""

import numpy as np



# Create dummy matrix (512x8)
rand_array = np.random.rand(512,8)




def outer_classify(in_data,prev_data):

# Check if previous in_data was classified
    if (prev_data != 0):
        # decrement prev_data
        prev_data -= 1
    
    else:
        # Take in data 
        in_data

    # Fix data for biploar montage 
    # ... 
    # ... 
    # ...


    # Classify
    # ... 
    # ... 
    # ... 
        # classification output... 
        # Make random output  !!! !!! !!! 
        class_out = np.random.randint(0,6)
    
    # if ouput is a class
    if(class_out > 0):
        # call frontend for output... 
        
        # set prev_data to 20, so next 20 in_data are not checked
            # in each new in_data, updated by 16/128=0.125s
        prev_data = 20
    else: 
    # if output is no class
        # do nothing, check next in_data 
        # set prev_data to 0, so next in_data is checked
        prev_data = 0
    
    
    return prev_data,class_out








prev = outer_classify(rand_array,0)




















