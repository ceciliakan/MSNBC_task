#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def webEntry(pg99Pct, sessLen_size, pg_category):
    first_Cat = [ x[0] for x in [ i for i in pg99Pct if len(i) > 1] ]
    firstCat_bin = np.bincount(first_Cat)
    firstCat_bin = np.delete(firstCat_bin, 0)

    data = np.true_divide(firstCat_bin, sessLen_size)*100
    
    idx = np.arange(17)
    plot1 = plt.figure()
    plt.bar(idx, data, width = 0.4, align = 'center', color = (0.254902, 0.411765, 0.882353) )
    plt.title("Percentage Request as Website Entrance by Page Category")
    plt.xlabel('Category')
    plt.ylabel('Percentage of User / %')
    plt.xticks(idx, pg_category, rotation = 55)
    plot1.show()

#def cat_data(pg99Pct):
    first_Cat = [ x[0] for x in [ i for i in pg99Pct if len(i) > 1] ]
