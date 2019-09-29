#!/usr/bin/env python3

from pandas import read_csv, DataFrame
import pandas as pd

with open('sample.csv', 'r') as csv:
    dtf = pd.read_csv(csv)

    # define as colunas
    dtf.columns = ['red', 'green', 'blue']

    print(dtf['red'])

