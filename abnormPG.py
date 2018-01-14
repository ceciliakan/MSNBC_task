#!/usr/bin/env python
# coding=UTF-8

import numpy as np
from scipy import stats

from readfile import readData
from plot_request_len import boxplotLen, plot_requestLen
import categoryBin 
from transitMatrix import gen_transitMat, transHeatMap 

pg_raw, pg_category = readData('msnbc990928.seq')

sessLength = np.array ( [ len(i) for i in pg_raw ] )
sessLength_stats = {'mean': np.mean(sessLength), 'median': np.median(sessLength), \
'mode': stats.mode(sessLength), '75Pct': np.percentile(sessLength, 75), \
'90Pct': np.percentile(sessLength, 90), '95Pct': np.percentile(sessLength, 95), \
'99Pct': np.percentile(sessLength, 99), '99_5Pct': np.percentile(sessLength, 99.5)   }

pg_abnorm = [ i for i in pg_raw if (len(i) >= sessLength_stats["95Pct"] and len(i) < sessLength_stats["99Pct"])  ]

lenAbnorm = np.array ( [ len(i) for i in pg_abnorm ] )

lenAbnorm_stats = {'mean': np.mean(lenAbnorm), 'max': np.amax(lenAbnorm), 'min': np.amin(lenAbnorm)  }

# boxplotLen(lenAbnorm)

category_bin = categoryBin.total_cat_bin(pg_abnorm)
rm_consec_bin, rm_consecut_pg = categoryBin.rm_consecut_bin(pg_abnorm)
rm_re_bin = categoryBin.rm_repeat_bin(pg_abnorm)
# categoryBin.plotCatBin(category_bin, rm_consec_bin, rm_re_bin, pg_category)

transitMat = gen_transitMat(pg_abnorm, 0)
transHeatMap(transitMat, pg_category)

raw_input()