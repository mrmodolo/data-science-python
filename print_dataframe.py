#!/usr/bin/env python3

from pandas import read_csv, DataFrame
import pandas as pd

with open('sample.csv', 'r') as csv:
    print(pd.read_csv(csv))
