#!/usr/bin/env python
# coding=UTF-8

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from generalStats.readfile import readData
from generalStats.categoryBin import total_cat_bin, rm_consecut_bin, rm_repeat_bin
from generalStats.transitMatrix import gen_transitMat, transHeatMap

from ML.wrangle import classSelect, catFragmnts
from ML.MLalgo import randForest, supvKNN
from functLib import splitData
from itertools import izip

pg_raw, pg_category = readData('msnbc990928.seq')

sessLength = np.array ( [ len(i) for i in pg_raw ] ) 

bound = [90,95,99,99.5,100]

classInter = [0] * len(bound)

for i,n in enumerate(bound):
    classInter[i] = np.percentile(sessLength, n)

len_class, classLen, lb = classSelect(pg_raw, classInter, None)

for i in len_class:
    transitMap = gen_transitMat(i, 1)
    transHeatMap(transitMap, pg_category)

'''
dataContainer = []

for i in len_class:
    featureSize = 11
    dataContainer.append(catFragmnts(i, featureSize)) # Lengths of consecutive repeated page
    # dataContainer.append(classCategory(i, featureSize)) # Category

trainData, trainLb, testData, testLb, trainIdx, testIdx = splitData(dataContainer, lb, 0.25, 0.25)

logLoss, mean_accur, confusMat = supvKNN(30, trainData, trainLb, testData, testLb)
ada_logLoss, ada_mean_accur, ada_confusMat, confidence  = randForest(trainData, trainLb, testData, testLb)

for i,j in izip(confidence, testIdx):
    i.insert(0,j)

for i,j in izip(confidence, testLb):
    i..append(j)

a9095 = [ x for x in confidence if x[-1] == 'a']
b9599 = [ x for x in confidence if x[-1] == 'b']
c99_995 = [ x for x in confidence if x[-1] == 'c']
d995 = [ x for x in confidence if x[-1] == 'd']

a9095c = [ x for x in confidence if max(x[1:5]) == x[1]]


category_bin=[]
rm_consec_bin=[]
rm_re_bin =[]
topStack=[]
middleStack=[]
bottomStack=[]

for i in len_class:
    category_bin.append(total_cat_bin(i))
    rm_consec_bin.append(rm_consecut_bin(i) )
    rm_re_bin.append(rm_repeat_bin(i))
print category_bin[1][1:3]

for i in range(5):
    middleStack.append( np.true_divide( rm_consec_bin[i] - rm_re_bin[i], sum(category_bin[i]) )*100 )
    topStack.append( np.true_divide( category_bin[i] - rm_consec_bin[i], sum(category_bin[i]) )*100 )
    bottomStack.append( np.true_divide( rm_re_bin[i], sum(category_bin[i]) )*100 )

width = 0.15
idx = range(4)
for i in idx: idx[i] = np.add( np.arange(17), (width+0.02)*i + 0.09  )

fig, ax = plt.subplots()
plot3 = ax.bar(idx[0], bottomStack[1], width = 0.4, color = (0.254902, 0.411765, 0.882353) )
plot4 = ax.bar(idx[0], middleStack[1], bottom = bottomStack[1], width = 0.4, color = (0.443137, 0.776471, 0.443137) )
plot5 = ax.bar(idx[0], topStack[1], bottom = middleStack[1]+bottomStack[1], width = 0.4, color = (1, 0.843137, 0) )
    
plot7 = ax.bar(idx[1], bottomStack[2], width = 0.4, color = (0.254902, 0.411765, 0.882353) )
plot8 = ax.bar(idx[1], middleStack[2], bottom = bottomStack[0], width = 0.4, color = (0.443137, 0.776471, 0.443137) )
plot9 = ax.bar(idx[1], topStack[2], bottom = middleStack[2]+bottomStack[2], width = 0.4, color = (1, 0.843137, 0) )

plota = ax.bar(idx[2], bottomStack[3], width = 0.4, color = (0.254902, 0.411765, 0.882353) )
plotb = ax.bar(idx[2], middleStack[3], bottom = bottomStack[3], width = 0.4, color = (0.443137, 0.776471, 0.443137) )
plotc = ax.bar(idx[2], topStack[3], bottom = middleStack[3]+bottomStack[3], width = 0.4, color = (1, 0.843137, 0) )

plt.show()
'''