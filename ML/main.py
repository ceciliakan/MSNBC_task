#!/usr/bin/env python
# coding=UTF-8

import numpy as np
from itertools import izip

from readfile import readData
from wrangle import catFragmnts, splitData, classSelect, classCategory
from MLalgo import supvKNN, randForest 

np.set_printoptions(suppress=True)

pg_raw, pg_category = readData('msnbc990928.seq') # read raw data

## Partition data by sequence length
classBound = [95, 99, 99.5, 100]
sliceLen = 16 # slice first n pages requested

sessLength = np.array ( [ len(i) for i in pg_raw ] ) 

classInterval = [0] * len(classBound)
for i,n in enumerate(classBound):
    classInterval[i] = np.percentile(sessLength, n)

len_class, classLen, lb = classSelect(pg_raw, classInterval, sliceLen)

len_class[0] = len_class[0][::5] # reduce imbalance
#len_class[1] = len_class[0][::5]

print classLen
##  Select feature
dataContainer = len_class # training input container

for i in len_class:
    featureSize = 10
    #dataContainer.append(catFragmnts(i, featureSize)) # Lengths of consecutive repeated page
    # dataContainer.append(classCategory(i, featureSize)) # Category

## Data training
trainData, trainLb, testData, testLb = splitData(dataContainer, lb, 0.25, 0.25)
 
logLoss, mean_accur, confusMat = supvKNN(30, trainData, trainLb, testData, testLb)
ada_logLoss, ada_mean_accur, ada_confusMat, confidence  = randForest(trainData, trainLb, testData, testLb)
#logLossSVM, mean_accurSVM = supVectMach(trainData, trainLb, testData, testLb) 

# np.savetxt('confuse.csv', confusMat, delimiter=" ")
