#!/usr/bin/env python

from itertools import groupby
import numpy as np
import matplotlib.pyplot as plt

def flatten(seq,container=None):
    if container is None:
        container = []
    for s in seq:
        if hasattr(s,'__iter__'):
            flatten(s,container)
        else:
            container.append(s)
    return container

def total_cat_bin(pg99Pct):
    category_bin = np.bincount(flatten(pg99Pct))
    category_bin = np.delete(category_bin, 0)
    return category_bin

def rm_consecut_bin(pg99Pct):
    rm_consecut_pg = [ [x[0] for x in groupby(line)] for line in pg99Pct ]
    rm_consec_bin = np.bincount(flatten(rm_consecut_pg))
    rm_consec_bin = np.delete(rm_consec_bin, 0)
    return rm_consec_bin

def rm_repeat_bin(pg99Pct):
    rm_re_pg = [set(line) for line in pg99Pct]
    rm_re_bin = np.bincount(flatten(rm_re_pg))
    rm_re_bin = np.delete(rm_re_bin,0)
    return rm_re_bin

def plotCatBin(category_bin, rm_consec_bin, rm_re_bin, pg_category):
    middleDiff = rm_consec_bin - rm_re_bin
    topDiff = category_bin - rm_consec_bin
    idx = np.arange(17)
    
    plt.figure()
    plot1 = plt.bar(idx, rm_re_bin, width = 0.4, color = (0.254902, 0.411765, 0.882353) )
    plot2 = plt.bar(idx, middleDiff, bottom = rm_re_bin, width = 0.4, color = (0.443137, 0.776471, 0.443137) )
    plot3 = plt.bar(idx, topDiff, bottom = middleDiff+rm_re_bin, width = 0.4, color = (1, 0.843137, 0) )
    
    plt.title('Page Request Counts by Category')
    plt.ylabel('Occurence / page')
    plt.xticks(idx, pg_category)
    plt.legend( [plot3,plot2,plot1], ['Consecutive','Repeated','Per user'] )
    
    plt.show()
    return 0


