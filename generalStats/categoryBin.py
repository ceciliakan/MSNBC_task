#!/usr/bin/env python

from itertools import groupby
import numpy as np
import matplotlib.pyplot as plt
from flatNestedList import flatten

def total_cat_bin(pg99Pct):
    category_bin = np.bincount(flatten(pg99Pct))
    category_bin = np.delete(category_bin, 0)
    return category_bin

def rm_consecut_bin(pg99Pct):
    rm_consecut_pg = [ [x[0] for x in groupby(line)] for line in pg99Pct ]
    rm_consec_bin = np.bincount(flatten(rm_consecut_pg))
    rm_consec_bin = np.delete(rm_consec_bin, 0)
    return rm_consec_bin, rm_consecut_pg

def rm_repeat_bin(pg99Pct):
    rm_re_pg = [set(line) for line in pg99Pct]
    rm_re_bin = np.bincount(flatten(rm_re_pg))
    rm_re_bin = np.delete(rm_re_bin,0)
    return rm_re_bin

def plotCatBin(category_bin, rm_consec_bin, rm_re_bin, pg_category):
    middleStack = np.true_divide( rm_consec_bin - rm_re_bin, sum(category_bin) )*100
    topStack = np.true_divide( category_bin - rm_consec_bin, sum(category_bin) )*100
    bottomStack = np.true_divide( rm_re_bin, sum(category_bin) )*100
    idx = range(17)
    
    plott = plt.figure()
    plot1 = plt.bar(idx, bottomStack, width = 0.4, color = (0.254902, 0.411765, 0.882353) )
    plot2 = plt.bar(idx, middleStack, bottom = bottomStack, width = 0.4, color = (0.443137, 0.776471, 0.443137) )
    plot3 = plt.bar(idx, topStack, bottom = middleStack+bottomStack, width = 0.4, color = (1, 0.843137, 0) )
    
    plt.title('Page Request by Category')
    plt.ylabel('Percentage of total page counts')
    plt.xticks(idx, pg_category, rotation = 55)
    plt.legend( [plot3,plot2,plot1], ['Consecutive','Repeated','Per user'] )
    
    plott.show()
    return 0


