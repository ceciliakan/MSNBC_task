#!/usr/bin/env python
# coding=UTF-8

import numpy as np
from scipy import stats

from readfile import readData
from flatNestedList import flat0sep
from catLenPattern import lenClass_bins, pie_lenClass, cat_bar
from transitMatrix import gen_transitMat, transHeatMap

pg_raw, pg_category = readData('msnbc990928.seq')

sessLength = np.array ( [ len(i) for i in pg_raw ] )
sessLength_stats = {'mean': np.mean(sessLength), 'median': np.median(sessLength), \
'mode': stats.mode(sessLength), '75Pct': np.percentile(sessLength, 75), \
'90Pct': np.percentile(sessLength, 90), '95Pct': np.percentile(sessLength, 95), \
'99Pct': np.percentile(sessLength, 99), '99_5Pct': np.percentile(sessLength, 99.5)   }

pg1_50 = [ i for i in pg_raw if (len(i) >=1 and len(i) <= sessLength_stats["median"])  ]
pg50_75 = [ i for i in pg_raw if (len(i) > sessLength_stats["median"] and len(i) <= sessLength_stats["75Pct"]) ]
pg75_95 = [ i for i in pg_raw if (len(i) > sessLength_stats["75Pct"] and len(i) <= sessLength_stats["95Pct"]) ]
pg95_99 = [ i for i in pg_raw if (len(i) > sessLength_stats["95Pct"] and len(i) <= sessLength_stats["99Pct"]) ]
pg_99 = [ i for i in pg_raw if len(i) > sessLength_stats["99Pct"] ]

classList = ['<=50th', '50 - 75th', '75 - 95th', '95 - 99th', '>99th' ]
groupSize = [ len(pg1_50), len(pg50_75), len(pg75_95), len(pg95_99), len(pg_99) ]
flat_pg = [ flat0sep(pg1_50), flat0sep(pg50_75), flat0sep(pg75_95), flat0sep(pg95_99), flat0sep(pg_99) ]

## Category of all pages
flag_pg_bins = lenClass_bins(flat_pg)
np.savetxt("flag_pg_bins.csv", flag_pg_bins, delimiter=",")
# pie_lenClass(flag_pg_bins, classList)
cat_bar(flag_pg_bins, pg_category, classList)
## 


'''
transMat0150 = gen_transitMat(pg1_50, 0)
transHeatMap(transMat0150, pg_category)

transMat5075 = gen_transitMat(pg50_75, 0)
transHeatMap(transMat5075, pg_category)

transMat7595 = gen_transitMat(pg75_95, 0)
transHeatMap(transMat7595, pg_category)

transMat9599 = gen_transitMat(pg95_99, 0)
transHeatMap(transMat9599, pg_category)

transMat99 = gen_transitMat(pg_99, 0)
transHeatMap(transMat99, pg_category)

category_bin = categoryBin.total_cat_bin(pg_abnorm)
rm_consec_bin, rm_consecut_pg = categoryBin.rm_consecut_bin(pg_abnorm)
rm_re_bin = categoryBin.rm_repeat_bin(pg_abnorm)
categoryBin.plotCatBin(category_bin, rm_consec_bin, rm_re_bin, pg_category)
'''
raw_input()