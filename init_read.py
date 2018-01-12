#!/usr/bin/env python
# coding=UTF-8

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
from itertools import groupby

import readfile
import plot_request_len # plot user request lengths
import singleRequest # single-page requests

pg_raw, pg_category = readfile.readData('msnbc990928.seq')

## session length data
sessLength = np.array ( [ len(i) for i in pg_raw ] )

sessLength_stats = {'mean': np.mean(sessLength), 'median': np.median(sessLength), 'mode': stats.mode(sessLength), '75Pct': np.percentile(sessLength, 75), '90Pct': np.percentile(sessLength, 90), '95Pct': np.percentile(sessLength, 95), '99Pct': np.percentile(sessLength, 99), '99_5Pct': np.percentile(sessLength, 99.5)   }

sessLength_stats = {'mean': np.mean(sessLength), 'median': np.median(sessLength), \
'mode': stats.mode(sessLength), '75Pct': np.percentile(sessLength, 75), \
'90Pct': np.percentile(sessLength, 90), '95Pct': np.percentile(sessLength, 95), \
'99Pct': np.percentile(sessLength, 99), '99_5Pct': np.percentile(sessLength, 99.5)   }

plot_request_len.plotLen(sessLength)
plot_request_len.boxplotLen(sessLength)

pg99Pct = [ line for line in pg_raw if len(line) < sessLength_stats["99Pct"] ]

## single page requests
one_category, one_cat_bins = singleRequest.single_request(pg99Pct)
singleRequest.plot_single_request_cat(one_cat_bins, pg_category)



raw_input()