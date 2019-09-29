#!/usr/bin/env python3

import random

def rgb():
    return random.randint(0,255)/255

with open ('sample.csv', 'w') as csv:
    csv.write('"red","green","blue"')
    for count in range(10):
        csv.write('\n{:0.2f},{:0.2f},{:0.2f}'.format(rgb(),rgb(),rgb()))
