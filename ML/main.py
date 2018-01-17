#!/usr/bin/env python
# coding=UTF-8

import numpy as np
from itertools import izip

from readfile import readData
from wrang import catFragmnts, splitData, classSelect
import MLalgo

np.set_printoptions(suppress=True)

pg_raw, pg_category = readData('msnbc990928.seq') # read raw data

sessLength = np.array ( [ len(i) for i in pg_raw ] ) # query sequence lengths

## Partition data by sequence length
classBound = [90, 95, 99, 99.5, 100] 

classInterval = [0] * len(classBound)
for i,n in enumerate(classBound):
    classInterval[i] = np.percentile(sessLength, n)

## Extract first n pages requested for 90% longest sequences
sliceLen = 10
len_class, classLen, lb = classSelect(pg_raw, classInterval, sliceLen)

# Sample data to reduce imbalance
len_class[0] = len_class[0][::3]

continFrags = [] #len_class

## Lengths of consecutive repeated page requests as feature

for i in len_class:
    continFrags.append(catFragmnts(i,10))

for i, j in izip(continFrags, lb):
    for v in i: v.append(j)

trainData, trainLb, testData, testLb = splitData(continFrags, 0.25, 0.25)

logLoss, mean_accur, confusMat = MLalgo.supvKNN(10, trainData, trainLb, testData, testLb)

# logLossSVM, mean_accurSVM = MLalgo.supVectMach(trainData, trainLb, testData, testLb) 

# np.savetxt('confuse.csv', confusMat, delimiter=" ")