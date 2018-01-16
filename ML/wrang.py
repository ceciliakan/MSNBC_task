#!/usr/bin/env python

import numpy as np
from itertools import groupby, izip
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle

# get lengths of consective repeated page requests
def catFragmnts(len_class_lines):
    fragment_bin = []

    for data in len_class_lines:
        fragmnt = [ sum( 1 for _ in group ) for key, group in groupby( data ) if key ]
        fragmnt = fragmnt + [0] * ( 10-len(fragmnt) ) 
        fragment_bin.append(fragmnt)
    
    return fragment_bin


# Split data in training, test, validation sets
def splitData(continFrags, testSize, valSize):
    val_size = np.true_divide(valSize , 1 - testSize )
    
    trainData = []
    testData = []
    valData = []

    for value in continFrags:
        trainD, testD = train_test_split(value, test_size=testSize, random_state = 42)
        trainD, valD = train_test_split(trainD, test_size=val_size, random_state = 42)

        trainData.append(trainD[0])
        testData.append(testD[0])
        valData.append(valD[0])
        print trainData

    trainData, trainLb = data_label_split(trainData)
    testData, testLb = data_label_split(testData)
    valData, valLb = data_label_split(valData)
    
    return trainData, testData, valData, trainLb, testLb, valLb

# Shuffle training sets, take out labels
def data_label_split(tData):
    data = shuffle(tData)

    labels = [ i[-1] for i in data ]
    for i in data: i.pop()

    return data, labels