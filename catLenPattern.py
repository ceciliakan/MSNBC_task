#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt
from itertools import izip

## number of pages in each category in each class
def lenClass_bins(flat_pg):
    flag_pg_bins = [ ]

    for i in flat_pg:
        bins = np.bincount(i)
        bins = np.delete(bins,0)
        flag_pg_bins.append(bins)

    return flag_pg_bins

# pie chart of number of page request of each class
def pie_lenClass(flag_pg_bins, classList):
    pgCount = np.sum(flag_pg_bins, axis=1) 
    fig, ax = plt.subplots()
    ax.pie( pgCount, labels = classList, autopct='%1.1f%%',  shadow=False, startangle=90 )
    ax.axis('equal')
    plt.title('Page Request Distribution')
    plt.show()

def cat_bar(flag_pg_bins, pg_category, classList):
    data = []
    for n in flag_pg_bins: data.append( np.true_divide(n, np.sum(n)) ) 
    
    #for i, j in izip(flag_pg_bins, groupSize):
     #   data.append( np.true_divide(i, j) )

    width = 0.15
    
    idx = range(5)

    for i in idx: idx[i] = np.add( np.arange(17), width*i + 0.1  )

    fig = plt.figure()
    ax = fig.add_subplot(111)
    plot1 = ax.bar(idx[0], data[0], width, color = (1, 0, 0.3) )
    plot2 = ax.bar(idx[1], data[1], width, color = (0.7, 1, 0.1) )
    plot3 = ax.bar(idx[2], data[2], width, color = (0.4, 0.4, 1) )
    plot4 = ax.bar(idx[3], data[3], width, color = (1, 0.5, 0) )
    plot5 = ax.bar(idx[4], data[4], width, color = (0.7, 0.3, 0.8) )

    ax.set_title('Page Requests by Category')
    ax.set_ylabel('Percentage of page request in class / %')
    ax.set_xlabel('Category')
    ax.set_xticks(idx[2])
    ax.set_xticklabels(pg_category, rotation = 55)
    ax.legend( [plot1,plot2,plot3, plot4, plot5], classList)
    plt.show()


'''
def cat_len(flat_pg):
    uniqueCat = np.unique(data)
    for n in uniqueCat:
        np.diff(np.where(np.concatenate(([data[0]], data[:-1] != data[1:],
            [n])))[0])[::2]
'''