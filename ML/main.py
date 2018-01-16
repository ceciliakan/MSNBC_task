#!/usr/bin/env python
# coding=UTF-8

import numpy as np
from itertools import izip



from readfile import readData
from wrang import catFragmnts, splitData
import MLalgo

pg_raw, pg_category = readData('msnbc990928.seq')

sessLength = np.array ( [ len(i) for i in pg_raw ] )

sessLenPct = [np.percentile(sessLength, 90), np.percentile(sessLength, 95), np.percentile(sessLength, 99), np.percentile(sessLength, 99.5)]
## Extract first 10 page requests for 90% longest sequences
pg90_95 = [ i[0:10] for i in pg_raw if (len(i) > sessLenPct[0] and len(i) <= sessLenPct[1] ) ]
pg95_99 = [ i[0:10] for i in pg_raw if (len(i) > sessLenPct[1]  and len(i) <= sessLenPct[2]) ]
pg99_995 = [ i[0:10] for i in pg_raw if (len(i) > sessLenPct[2]  and len(i) <= sessLenPct[3]) ]
pg995_m = [ i[0:10] for i in pg_raw if (len(i) > sessLenPct[3] ) ]
'''
len_class = [ pg90_95, pg95_99, pg99_995, pg995_m]
lb = [9095, 9599, 99995, 99500]
'''
len_class = [ pg95_99, pg99_995, pg995_m]
lb = [ 9599, 99995, 99500]
#lenh = [len(pg90_95),len(pg95_99), len(pg99_995) ,len(pg995_m)]

continFrags = len_class

## Lengths of consecutive repeated page requests as feature
'''
for i in len_class:
    continFrags.append(catFragmnts(i))
'''

for i, j in izip(continFrags, lb):
    for v in i: v.append(j)

trainData, trainLb, testData, testLb = splitData(continFrags, 0.25, 0.25)

logLoss, mean_accur = MLalgo.supvKNN(50, trainData, trainLb, testData, testLb)

#logLossSVM, mean_accurSVM = MLalgo.supVectMach(trainData, trainLb, testData, testLb) 