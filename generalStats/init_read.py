#!/usr/bin/env python
# coding=UTF-8

import numpy as np
from scipy import stats

from readfile import readData
from plot_request_len import plotLen, boxplotLen, plot_requestLen # plot user request lengths
from singleRequest import single_request, pie_singReqst_cat, singReqst_cat # single-page requests
from transitMatrix import gen_transitMat, transHeatMap # transition matrix of categories
import categoryBin # page request count by category
from categryData import webEntry

pg_raw, pg_category = readData('msnbc990928.seq')

## Session length data
sessLength = np.array ( [ len(i) for i in pg_raw ] )

sessLength_stats = {'mean': np.mean(sessLength), 'median': np.median(sessLength), \
'mode': stats.mode(sessLength), '75Pct': np.percentile(sessLength, 75), \
'90Pct': np.percentile(sessLength, 90), '95Pct': np.percentile(sessLength, 95), \
'99Pct': np.percentile(sessLength, 99), '99_5Pct': np.percentile(sessLength, 99.5)   }

#plotLen(sessLength)
plot_requestLen(sessLength)
'''
pg99Pct = [ i for i in pg_raw if len(i) < sessLength_stats["95Pct"] ]

#pg99Pct = [ i for i in pg_raw if (len(i) >= sessLength_stats["95Pct"] and len(i) < sessLength_stats["99Pct"])  ]

sessLength99 = np.array ( [ len(i) for i in pg99Pct ] )

sessLength99_stats = {'mean': np.mean(sessLength99), 'median': np.median(sessLength99), \
'mode': stats.mode(sessLength99), '75Pct': np.percentile(sessLength99, 75), \
'90Pct': np.percentile(sessLength99, 90), '95Pct': np.percentile(sessLength99, 95), \
'99Pct': np.percentile(sessLength99, 99), '99_5Pct': np.percentile(sessLength99, 99.5)   }

#boxplotLen(sessLength99)
plot_requestLen(sessLength99)

## Page request by category
category_bin = categoryBin.total_cat_bin(pg99Pct)
rm_consec_bin, rm_consecut_pg = categoryBin.rm_consecut_bin(pg99Pct)
rm_re_bin = categoryBin.rm_repeat_bin(pg99Pct)
#categoryBin.plotCatBin(category_bin, rm_consec_bin, rm_re_bin, pg_category)

## Single page requests
one_category, one_cat_bins = single_request(pg99Pct)
singReqst_cat(one_cat_bins, sessLength99.size, pg_category)
#pie_singReqst_cat(one_cat_bins, pg_category)

## Category transition
transitMat = gen_transitMat(pg99Pct, 0)
transHeatMap(transitMat, pg_category)

transitMatRp = gen_transitMat(rm_consecut_pg, 0)
transHeatMap(transitMatRp, pg_category)

webEntry(pg99Pct, sessLength99.size, pg_category)
'''
raw_input()