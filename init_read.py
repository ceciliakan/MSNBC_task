#!/usr/bin/env python
# coding=UTF-8

import numpy as np
from scipy import stats
from more_itertools import flatten

from readfile import readData
from plot_request_len import plotLen, boxplotLen # plot user request lengths
from singleRequest import single_request, plot_single_request_cat # single-page requests
from transitMatrix import gen_transitMat, transHeatMap # transition matrix of categories
import categoryBin

pg_raw, pg_category = readData('msnbc990928.seq')

## Session length data
sessLength = np.array ( [ len(i) for i in pg_raw ] )

sessLength_stats = {'mean': np.mean(sessLength), 'median': np.median(sessLength), 'mode': stats.mode(sessLength), '75Pct': np.percentile(sessLength, 75), '90Pct': np.percentile(sessLength, 90), '95Pct': np.percentile(sessLength, 95), '99Pct': np.percentile(sessLength, 99), '99_5Pct': np.percentile(sessLength, 99.5)   }

sessLength_stats = {'mean': np.mean(sessLength), 'median': np.median(sessLength), \
'mode': stats.mode(sessLength), '75Pct': np.percentile(sessLength, 75), \
'90Pct': np.percentile(sessLength, 90), '95Pct': np.percentile(sessLength, 95), \
'99Pct': np.percentile(sessLength, 99), '99_5Pct': np.percentile(sessLength, 99.5)   }

# plotLen(sessLength)
# boxplotLen(sessLength)

pg99Pct = [ i for i in pg_raw if len(i) < sessLength_stats["99Pct"] ]

## Singlflatten.e page requests
one_category, one_cat_bins = single_request(pg99Pct)
# plot_single_request_cat(one_cat_bins, pg_category)

## Page request by category
category_bin = categoryBin.total_cat_bin(pg99Pct)
rm_consec_bin = categoryBin.rm_consecut_bin(pg99Pct)
rm_re_bin = categoryBin.rm_repeat_bin(pg99Pct)
categoryBin.plotCatBin(category_bin, rm_consec_bin, rm_re_bin, pg_category)

## Category transition
transitMat = gen_transitMat(pg99Pct)
transHeatMap(transitMat, pg_category)

raw_input()