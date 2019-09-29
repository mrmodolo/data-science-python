#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pandas import read_csv, DataFrame
import pandas as pd
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from matplotlib import rcParams

matplotlib.use('GTK3Agg')
rcParams['figure.figsize'] = 11,8
sns.set_style('darkgrid')

with open('./sample.csv','r') as csv:
    dtf = pd.read_csv(csv)
    dtf.columns = ['red','green','blue']

    plt.plot(dtf['red'],'r-')
    plt.plot(dtf['green'],'g-')
    plt.plot(dtf['blue'],'b-')
    plt.plot(dtf['red'],'ro')
    plt.plot(dtf['green'],'go')
    plt.plot(dtf['blue'],'bo')

    plt.show()
    
