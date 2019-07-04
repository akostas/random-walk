# -*- coding: utf-8 -*-
"""
Created on Thu Jul  4 23:09:19 2019

@author: aggel
"""

import random

steps, runs = 1000, 10000
mysum = 0
for run in range(runs):
    x, y = 0, 0
    for step in range(steps):
        tmp = random.random()
        if tmp<0.25:
            x -= 1
        elif tmp<0.5:
            x += 1
        elif tmp<0.75:
            y -= 1
        else:
            y += 1
    r2 = x*x + y*y
    mysum += r2
print('R^2 = {}'.format(mysum/runs))