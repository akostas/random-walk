# -*- coding: utf-8 -*-
"""
@author: Konstantinos Angelou
"""

import random
import sys

class RandomWalker():
    '''This is a random walker simulator'''
    def __init__(self, x=0, y=0, mseed=0):
        self.x = 0
        self.y = 0
        random.seed(mseed)
    
    def move(self):
        tmp = random.random()
        if tmp < 0.25:
            self.x -= 1
        elif tmp < 0.5:
            self.x += 1
        elif tmp < 0.75:
            self.y -= 1
        else:
            self.y += 1
    
    def calculateR2(self):
        r2 = self.x*self.x + self.y*self.y
        return r2

def rwInput():
    return int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3])

def main():
    steps, runs, mseed = rwInput()
    mysum = 0
    for run in range(runs):
        # Create a random walker
        rwalker = RandomWalker(0, 0, (1+mseed)*run)
        for step in range(steps):
            # Move the random walker
            rwalker.move()
        # Calculate R^2 = x^2 + y^2
        r2 = rwalker.calculateR2()
        mysum += r2
            
    print('R^2 = {}'.format(mysum/runs))

if __name__ == "__main__":
    # execute only if run as a script
    main()