#!/usr/bin/env python

import numpy as np
from itertools import groupby, izip, tee
from string import ascii_lowercase

from sklearn.preprocessing import normalize
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.utils.class_weight import compute_class_weight


def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

## Partition data by sequence lengths
def classSelect(pg_raw, classInterval, sliceLen):
    len_class = []

    for i,j in pairwise(classInterval):
        data = [ x[0:sliceLen] for x in pg_raw if (len(x) > i and len(x) <= j ) ]
        len_class.append(data)

    lb = list(ascii_lowercase)[ 0:len(classInterval)-1 ]

    classLen = [ len(i) for i in len_class ]
    return len_class, classLen, lb

# get lengths of consective repeated page requests
def catFragmnts(len_class_lines, featureSize):
    fragment_bin = []

    for data in len_class_lines:
        fragmnt = [ sum( 1 for _ in group ) for key, group in groupby( data ) if key ]
        if len(fragmnt) > featureSize:
            fragmnt = fragmnt[0:featureSize]
        else:
            fragmnt = fragmnt + [0] * ( featureSize-len(fragmnt) )
        fragment_bin.append(fragmnt)
    
    return fragment_bin

def classCategory(len_class_lines, featureSize):
    classCat_bin = []
    for line in len_class_lines:
        data.append( np.bincount(line) )
    data = [ i.tolist()[1:i.size] for i in data ]
    data = [ x + [0 for i in range(featureSize - len(x))] for x in data ]
    classCat_bin = [ x[0:featureSize] for x in data ]

    return classCat_bin

# Split data in training, test, validation sets
def splitData(dataContainer, lb, testSize, valSize):    
    for i, j in izip(dataContainer, lb):
        for v in i: v.append(j)

    # val_size = np.true_divide(valSize , 1 - testSize )

    trainData = []
    testData = []
    #valData = []

    for value in dataContainer:
        trainD, testD = train_test_split(value, test_size=testSize, random_state = 42)
        #trainD, valD = train_test_split(trainD, test_size=val_size, random_state = 42)

        trainData = trainData + trainD
        testData = testData + testD
        #valData = valData + valD

    trainData

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

def sig():
    return 0
