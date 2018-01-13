#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def single_request(pg_raw):
    one_category = [ x[0] for x in [ i for i in pg_raw if len(i) == 1 ] ]
    one_cat_bins = np.bincount(one_category)
    one_cat_bins = np.delete(one_cat_bins, 0)
    return one_category, one_cat_bins

def plot_single_request_cat(one_cat_bins, pg_category):
    one_cat_bins.tolist
    plot1 = plt.figure()
    plt.bar(range(len(one_cat_bins)), one_cat_bins, width = 0.4, align = 'center', color = (0.254902, 0.411765, 0.882353) )
    plt.xticks(range(len(pg_category)), pg_category, rotation = 55)
    plt.xlabel("Page Category")
    plt.ylabel("Number of Users")
    plt.title("Single-Page-Request Counts by Page Categories")
    plot1.show()
