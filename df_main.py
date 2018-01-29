
# coding: utf-8

import numpy as np
import pandas as pd
from itertools import groupby
import matplotlib.pyplot as plt

#cf.go_offline()


df = pd.read_csv('msnbc990928.seq', header=None)
df.rename(columns={0:'Session'}, inplace=True)
df['Session'] = df.Session.str.split()
df['Length'] = df['Session'].str.len()


stst = [df.Length.quantile(0.5), df.Length.quantile(0.75), df.Length.quantile(0.90), 
df.Length.quantile(0.95), df.Length.quantile(0.99), df.Length.quantile(0.995)]

N = int( df.Length.quantile(0.90) )


ab10 = df.loc[df['Length'] >= N].copy()
ab10['Transition'] = ab10['Session'].apply(lambda x: [ i[0] for i in groupby(x) ])
ab10['TransitionCount'] = ab10['Transition'].str.len()

ab10['First10'] = ab10['Session'].apply(lambda x: x[0:N])
ab10['Trans_1st_10'] = ab10['First10'].apply(lambda x: [ i[0] for i in groupby(x) ])
ab10['Trans_1st_10_cnt'] = ab10['Trans_1st_10'].str.len()
ab10['DiffTrans'] = ab10['TransitionCount'] - ab10['Trans_1st_10_cnt']
ab10['DiffTransRatio'] = ab10['DiffTrans'] / ( ab10['Length'] - N)
ab10['DiffTransRatio'].fillna(value=-0.02, inplace=True)

compress =[0]*4
b = np.arange(-0.02, 1.02, 0.02)
b2=np.arange(-0.02, 1, 0.02)
x = ab10.loc[ (ab10.Length <= stst[3]), ['DiffTransRatio'] ].as_matrix()
compress[0], n = np.histogram(x, bins = b, density='True')
x = ab10.loc[ (ab10.Length > stst[3]) & (ab10.Length <= stst[4]), ['DiffTransRatio'] ].as_matrix()
compress[1], n = np.histogram(x, bins = b, density='True')
x = ab10.loc[ (ab10.Length > stst[4]) & (ab10.Length <= stst[5]), ['DiffTransRatio'] ].as_matrix()
compress[2], n = np.histogram(x, bins = b, density='True')
x = ab10.loc[ (ab10.Length > stst[5]) , ['DiffTransRatio'] ].as_matrix()
compress[3], n = np.histogram(x, bins = b, density='True')

plot1 = plt.figure()
plt.plot(b2, compress[0], 'r', b2, compress[1], 'b', b2, compress[2], 'g', b2, compress[3], 'm')

plt.title('Distribution of Ratio of Number of Category Transitions to User Session Length')
plt.ylabel('Probability Density')
plt.xlabel('Trasistion to Session Lemgth Ratio')
plt.legend(["P90-P95", 'P95-P99','P99-P99.5', 'P99.5-P100'])

plot1.show()

raw_input()

'''
trace0 = [go.Histogram( x = ab10.loc[ (ab10.Length <= stst[3]), ['DiffTransRatio'] ], histnorm = "percent", xbins=dict( start=0, end=1, size=0.2 ) , orientation = 'v', marker=dict( color='rgb(49,130,189)') )]
trace1 = [go.Histogram( x = ab10.loc[ (ab10.Length > stst[3]) & (ab10.Length <= stst[4]), ['DiffTransRatio'] ], histnorm = "percent", xbins=dict( start=0, end=1, size=0.2 ) , orientation = 'v') ]
trace2 = [go.Histogram( x = ab10.loc[ (ab10.Length > stst[4]) , ['DiffTransRatio'] ], histnorm = "percent", xbins=dict( start=0, end=1, size=0.2 ) , orientation = 'v', marker=dict( color='rgb(204,204,204)') )]

data = [trace0, trace1, trace2]

#layout = go.Layout(barmode = 'group')

#fig = go.Figure(data=data, layout=layout)
py.iplot(data)
'''

#ab10.DiffTransRatio.iplot(kind='histogram', filename='comp_ratio')