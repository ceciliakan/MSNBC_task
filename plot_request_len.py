#!/usr/bin/env python

import matplotlib.pyplot as plt

def plotLen(sessLength):
    plot1 = plt.figure()
    plt.plot(sessLength)
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