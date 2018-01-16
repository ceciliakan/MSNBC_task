#!/usr/bin/env python
# coding=UTF-8

import numpy as np
from scipy import stats
from itertools import izip

from sklearn.neighbors import KNeighborsClassifier

from readfile import readData
from wrang import catFragmnts, splitData

pg_raw, pg_category = readData('msnbc990928.seq')

sessLength = np.array ( [ len(i) for i in pg_raw ] )

## Extract first 10 page requests for 90% longest sequences
pg90_95 = [ i[0:10] for i in pg_raw if (len(i) > np.percentile(sessLength, 90) and len(i) <= np.percentile(sessLength, 95)) ]
pg95_99 = [ i[0:10] for i in pg_raw if (len(i) > np.percentile(sessLength, 95) and len(i) <= np.percentile(sessLength, 99)) ]
pg99_995 = [ i[0:10] for i in pg_raw if (len(i) > np.percentile(sessLength, 99) and len(i) <= np.percentile(sessLength, 99.5)) ]
pg995_m = [ i[0:10] for i in pg_raw if (len(i) > np.percentile(sessLength, 99.5) ) ]

len_class = [pg90_95, pg95_99, pg99_995, pg995_m]
lb = [9095, 9599, 99995, 99500]

## Lengths of consecutive repeated page requests as feature
continFrags = []

for i in len_class:
    continFrags.append(catFragmnts(i))

for i, j in izip(continFrags, lb):
    for v in i: v.append(j)

trainData, testData, valData, trainLb, testLb, valLb = splitData(continFrags, 0.25, 0.25)

# supervised KNN
n_neighbours = 15
neigh = KNeighborsClassifier(n_neighbours)
neigh.fit(trainData, trainLb)
confidnce = neigh.predict_proba(testData)
mean_accur = neigh.score(testData, testLb)





