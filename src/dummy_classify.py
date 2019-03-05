#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  2 21:17:04 2019

@author: joshbierbrier
"""

import numpy as np
import configparser as cp
from classifier import predict

config = cp.ConfigParser()
config.read('config.ini')

sampling_rate = int(config['DEFAULT']['sampling_rate'])
classifier_length = int(config['DEFAULT']['classifier_length'])
buffer_length = int(config['DEFAULT']['buffer_length'])
channels = int(config['DEFAULT']['channels'])
no_response_time = int(config['DEFAULT']['no_response_time'])


# Create dummy matrix (512x8)
rand_array = np.random.rand(sampling_rate, channels)
fitted_model = np.load('../fitted_model/fitted_model.npy')

fitted_model[0] = np.array(fitted_model[0])

def outer_classify(in_data, prev_data, sig_noMean):

# Check if previous in_data was classified
    if (prev_data != 0):
        # decrement prev_data
        prev_data -= 1
        class_out = 0

    else:
        print('can classify')
        # Take in data 
        in_data

    # Fix data for biploar montage 
    # ... 
    # ... 
    # ...

        fitted_model[1] = 0.9

    # Classify
        class_out = int(predict.predict(fitted_model, sig_noMean)) + 1

        # classification output...
        # Make random output  !!! !!! !!! 
        # class_out = np.random.randint(0,6)

    # if ouput is a class
        if(class_out > 0 and class_out != 3):
            # call frontend for output...

            # set prev_data to 20, so next 20 in_data are not checked
                # in each new in_data, updated by 16/128=0.125s
            prev_data = int(sampling_rate * no_response_time / buffer_length)
        else:
        # if output is no class
            # do nothing, check next in_data
            # set prev_data to 0, so next in_data is checked
            prev_data = 0
    
    
    return prev_data,class_out
