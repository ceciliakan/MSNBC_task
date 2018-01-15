#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def single_request(pg_raw):
    one_category = [ x[0] for x in [ i for i in pg_raw if len(i) == 1 ] ]
    one_cat_bins = np.bincount(one_category)
    one_cat_bins = np.delete(one_cat_bins, 0)
    return one_category, one_cat_bins

def pie_singReqst_cat(one_cat_bins, pg_category):
    one_cat_bins.tolist
    fig, ax = plt.subplots()
    ax.pie( one_cat_bins, labels = pg_category, autopct='%1.1f%%',  shadow=False, startangle=90 )
    ax.axis('equal')
    plt.title("Single-Page-Request Counts by Page Categories")
    plt.show()

def singReqst_cat(one_cat_bins, sessLen_size, pg_category):
    data = np.true_divide(one_cat_bins, sessLen_size )*100
    plot1 = plt.figure()
    idx = range(17)
    plt.bar(idx, data, width = 0.4, color = (0.254902, 0.411765, 0.882353))
    plt.xlabel('Categories')
    plt.ylabel('Percentage of User / %')
    plt.title("Percentage Single-Page-Request by Page Categories")
    plt.xticks(idx, pg_category, rotation = 55)

    plot1.show()