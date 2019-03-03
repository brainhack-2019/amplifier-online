import configparser as cp
import numpy as np
import requests
import json
from dummy_classify import outer_classify
from classifier import predict


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

    samples = samples[:, [0,1,3,4,6,7,9,10]]

    sig[buffer_length:] = sig[:-buffer_length]
    sig[-buffer_length:] = samples[:]


    ###
    sig_noMean = sig[:]

    for i in range(channels):
        mean_chan = sig[:,i].mean()
        sig_noMean[:,i] -= mean_chan


    ###

    prev_data, class_out = outer_classify(sig, prev_data, sig_noMean)
    if class_out != 0:
        requests.post("http://" + client_ip + ":5000/", data=json.dumps({'gesture_id': class_out}))

    return prev_data
