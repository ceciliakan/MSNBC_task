#!/usr/bin/env python
# coding=UTF-8

import numpy as np
import matplotlib.pyplot as plt
from scipy import stats
import readfile

pg_raw,pg_category = readfile.readData('msnbc990928.seq')

## session length data
sessLength = np.array ( [ len(i) for i in pg_raw ] )

sessLength_stats = {'mean': np.mean(sessLength), 'median': np.median(sessLength), \
'mode': stats.mode(sessLength), '75Pct': np.percentile(sessLength, 75), \
'90Pct': np.percentile(sessLength, 90), '95Pct': np.percentile(sessLength, 95), \
'99Pct': np.percentile(sessLength, 99), '99_5Pct': np.percentile(sessLength, 99.5)   }

mode_cnt = 365435

## single page requests
one_category = np.array([ x[0] for x in [ i for i in pg_raw if i.size == 1 ] ])

one_cat_bins = np.bincount(one_category)
one_cat_bins = np.delete(one_cat_bins, 0)
one_cat_bins.tolist


# plot3 = plt.figure(3)
plt.bar(range(len(one_cat_bins)), one_cat_bins, width = 0.4, align = 'center')
plt.xticks(range(len(pg_category)), pg_category)

plt.xlabel("Page Category")
plt.ylabel("Number of Users")
plt.title("Single-Page-Request Counts by Page Categories")
plt.show()


'''
## plot graphs

# session length
plot1 = plt.figure(1)    
plt.plot(sessLength)
plt.ylabel('Session Lengths')
plt.xlabel('Session')
plot1.show()

plot2 = plt.figure(2)
plt.boxplot(sessLength, vert=False)
plt.title('Session Length Distribution')
plot2.show()


raw_input()
'''