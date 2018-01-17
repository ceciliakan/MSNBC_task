#!/usr/bin/env python
# coding=UTF-8

import numpy as np
from itertools import groupby, izip
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import normalize
from sklearn.utils import shuffle
from sklearn.utils.class_weight import compute_class_weight

# get lengths of consective repeated page requests
def catFragmnts(len_class_lines, fragLen):
    fragment_bin = []

    for data in len_class_lines:
        fragmnt = [ sum( 1 for _ in group ) for key, group in groupby( data ) if key ]
        if len(fragmnt) > fragLen:
            fragmnt = fragmnt[0:fragLen]
        else:
            fragmnt = fragmnt + [0] * ( fragLen-len(fragmnt) )
        fragment_bin.append(fragmnt)
    
    fragment_bin = normalize(fragment_bin)
    fragment_bin = fragment_bin.tolist()
    return fragment_bin

# get class weight as scale of class size proportion
def genClassWeight(tData, lb):
    weightDict = {}
    class_weight_vect = compute_class_weight(class_weight='balanced', classes = lb, y = tData)
    for i,j in izip(lb, class_weight_vect):
        weightDict[str(i)] = j
    return weightDict

# Split data in training, test, validation sets
def splitData(continFrags, testSize, valSize):
    val_size = np.true_divide(valSize , 1 - testSize )
    
    trainData = []
    testData = []
    #valData = []

    for value in continFrags:
        trainD, testD = train_test_split(value, test_size=testSize, random_state = 42)
        #trainD, valD = train_test_split(trainD, test_size=val_size, random_state = 42)

        trainData = trainData + trainD
        testData = testData + testD
        #valData = valData + valD

    trainData, trainLb = data_label_split(trainData)
    testData, testLb = data_label_split(testData)
    #valData, valLb = data_label_split(valData)
    
    return trainData, trainLb, testData, testLb #, valData, valLb

# Shuffle data set, take out labels
def data_label_split(tData):
    data = shuffle(tData)

    labels = [ i[-1] for i in data ]
    for i in data: i.pop()

    return data, labels