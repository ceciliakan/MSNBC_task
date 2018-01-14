#!/usr/bin/env python

import numpy as np
import matplotlib.pyplot as plt

def plotLen(sessLength):
    plot1 = plt.figure()
    plt.plot(sessLength, color = (0.254902, 0.411765, 0.882353) )
    plt.ylabel('User Request Length')
    plt.xlabel('User')
    plt.title('User Request Lengths')
    plot1.show()

def boxplotLen(sessLength):
    plot2 = plt.figure()
    plt.boxplot(sessLength, vert=False)
    plt.title('User Request Lengths Distribution')
    plt.ylabel('')
    plt.xlabel('User Request Length')
    plot2.show()

def plot_requestLen(sessLength):
    sessLengthsize = np.bincount(sessLength)
    sessLengthsize = np.delete(sessLengthsize, [range(0,10)] )
  
    plot3 = plt.figure()
    plt.bar(range(10,sessLengthsize.size+10), sessLengthsize, width = 0.4, align = 'center', color = (0.254902, 0.411765, 0.882353) )
    plt.title("User Request Length Count")
    plt.xlabel('User Request Length')
    plt.ylabel('Length Occurrence')
    plt.xticks( range(10,sessLengthsize.size+10) )
    plot3.show()
    
    
