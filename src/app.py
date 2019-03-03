import configparser as cp
import numpy as np
from dummy_classify import outer_classify

config = cp.ConfigParser()
config.read('config.ini')

sampling_rate = int(config['DEFAULT']['sampling_rate'])
classifier_length = int(config['DEFAULT']['classifier_length'])
buffer_length = int(config['DEFAULT']['buffer_length'])
channels = int(config['DEFAULT']['channels'])

sig = np.zeros((classifier_length * sampling_rate, channels))


def app(samples, prev_data):
    '''
    samples - a buffer stream from the gathered channels.
    This function will be executed on each recieved buffer of data.
    The analysis of the signal should, be handled through here.
    '''

    sig[buffer_length:] = sig[:-buffer_length]
    sig[-buffer_length:] = samples[:]



    prev_data, class_out = outer_classify(sig, prev_data)
    print(class_out)
    return prev_data

