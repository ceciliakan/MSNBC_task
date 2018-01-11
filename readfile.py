#!/usr/bin/env python

import numpy as np

def readData(fileName):
	f = open(fileName)
	lines = f.readlines()
	splitLines = [ line.split() for line in lines ]
	pg_raw = [ np.array( [ int(n) for n in line ] ) for line in splitLines ]
	pg_category = [ "frontpage", "news", "tech", "local", "opinion", "on-air", "misc", "weather", "health", "living", "business", "sports", "summary", "bulletin board", "travel", "msn-news", "msn-sports" ]
	
	return pg_raw, pg_category