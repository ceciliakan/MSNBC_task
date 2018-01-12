#!/usr/bin/env python

import numpy as np
from itertools import tee, izip
import matplotlib.pyplot as plt

def pairwise(iterable):
    a, b = tee(iterable)
    next(b, None)
    return izip(a, b)

def gen_transitMat(pg99Pct):
    transitMat = np.zeros( (18,18) )
    
    T0x = [ x[0] for x in [ i for i in pg99Pct ] ]
    transitMat[0:,0] = np.bincount(T0x)

    Tx0 = [ x[-1] for x in [ i for i in pg99Pct ] ]
    transitMat[0,0:] = np.bincount(Tx0)

    for line in pg99Pct:
        for i, j in pairwise(line):
            transitMat[j][i] = transitMat[j][i] + 1 
        
    transitMat = np.true_divide(transitMat, transitMat.sum(axis=1, keepdims=True))*100
    
    return transitMat

def transHeatMap(transitMat, pg_category):
    nw_pg_cat = list(pg_category)
    nw_pg_cat.insert(0, "Exit*")

    fig, ax = plt.subplots()
    heatmap = ax.pcolor(transitMat, cmap = plt.cm.jet)

    cbar = plt.colorbar(heatmap)
    cbar.ax.set_yticklabels(['0','25','50'])
    cbar.set_label('% transition', rotation = 270)

    # put the major ticks at the middle of each cell
    ax.set_xticks(np.arange(transitMat.shape[1]) + 0.5, minor=False)
    ax.set_yticks(np.arange(transitMat.shape[0]) + 0.5, minor=False)

    # want a more natural, table-like display
    ax.invert_yaxis()
    ax.xaxis.tick_top()

    ax.set_xticklabels(nw_pg_cat, minor=False)
    ax.set_yticklabels(nw_pg_cat, minor=False)
    plt.show()