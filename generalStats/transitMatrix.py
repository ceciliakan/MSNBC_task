#!/usr/bin/env python

import numpy as np
from itertools import tee, izip
import matplotlib.pyplot as plt
import math

def roundup(x):
    return int(math.ceil(x / 10.0)) * 10

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

def gen_transitMat(pg99Pct, N):
    transitMat = np.zeros( (17,17) )

    for line in pg99Pct:
        for i, j in pairwise(line):
            transitMat[j-1][i-1] = transitMat[j-1][i-1] + 1 
    
    transitMat_sum = transitMat.sum(axis = N, keepdims=True)
    transitMat = np.divide(transitMat, transitMat_sum, out=np.zeros_like(transitMat), where=transitMat_sum!=0)*100
   
    #np.savetxt("transitMat1_rev.csv", transitMat, delimiter=",")

    return transitMat

def transHeatMap(transitMat, pg_category):
    fig, ax = plt.subplots()
    heatmap = ax.pcolor(transitMat, cmap = plt.cm.viridis, vmin=0, vmax=roundup(np.amax(transitMat))) # 100

    idx = np.arange(0,110,10)
    cbar = plt.colorbar(heatmap, ticks=[idx])
    cbar.ax.set_yticklabels( list(map(str,idx)) )
    cbar.set_label('% transition', rotation = 270)

    # put the major ticks at the middle of each cell
    ax.set_xticks(np.arange(transitMat.shape[1]) + 0.5, minor=False)
    ax.set_yticks(np.arange(transitMat.shape[0]) + 0.5, minor=False)

    # want a more natural, table-like display
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    ax.set_xticklabels(pg_category, minor=False, rotation = 55)
    ax.set_yticklabels(pg_category, minor=False)

    plt.show()