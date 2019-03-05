import configparser as cp
import numpy as np
import requests
import json
from dummy_classify import outer_classify
from classifier import predict
import matplotlib.pyplot as plt


config = cp.ConfigParser()
config.read('config.ini')

sampling_rate = int(config['DEFAULT']['sampling_rate'])
classifier_length = int(config['DEFAULT']['classifier_length'])
buffer_length = int(config['DEFAULT']['buffer_length'])
channels = int(config['DEFAULT']['channels'])
client_ip = str(config['DEFAULT']['client_ip'])

sig = np.zeros((classifier_length * sampling_rate, channels))


def app(samples, prev_data):
    '''
    samples - a buffer stream from the gathered channels.
    This function will be executed on each recieved buffer of data.
    The analysis of the signal should, be handled through here.
    '''

    global sig

    samples = samples[:, [0,1,3,4,6,7,9,10]]

    sig[:-buffer_length] = sig[buffer_length:]
    sig[-buffer_length:] = samples[:]

    even = np.array([0,2,4,6])
    odd = np.array([1,3,5,7])
    _sig = sig[:,odd] - sig[:,even]


    ###
    sig_noMean = _sig[:]

    for i in range(4):
        mean_chan = _sig[:,i].mean()
        sig_noMean[:,i] = sig_noMean[:,i] - mean_chan


    ###
    prev_data, class_out = outer_classify(_sig, prev_data, sig_noMean)
    print(class_out)
    if class_out != 0:
        requests.post("http://" + client_ip + ":5000/", data=json.dumps({'gesture_id': class_out}))

    return prev_data
