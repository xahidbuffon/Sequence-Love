#!/usr/bin/env python
"""
@author: Jahid 
@email: islam034@umn.edu

visialier for Fibonacci sequence
"""
from __future__ import division
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection


def generateFibonacci(N=5):
    """ generates first N numbers in Fibonacci sequence
    """
    assert (N>0), "N must be a positive integer"
    seq = []
    for i in xrange(N):
        if i < 2: Pi = i 
        else: Pi = seq[i-1] + seq[i-2]
        seq.append(Pi)
    return seq



def vizualizeGoldenRatioSpiral(N=100):
    """ generates the golden-ratio spiral
    """
    # Get the spirals
    from utils.geo_utils import getSpiralGoldenRatio
    spirals = getSpiralGoldenRatio(N)

    # Plot the spirals
    fig = plt.figure()
    ax = fig.add_subplot(111)  
    Ncolors = 20; colors=[]
    for j in range(N):
        colors.append((j % Ncolors) * 5) # choose a color
        collection = PatchCollection(spirals, cmap=matplotlib.cm.jet, alpha=0.5)
        collection.set_array(np.array(colors))
        # add the spiral to collection
        ax.add_collection(collection)

    plt.axis('equal')
    plt.savefig('data/Fibo_spiral.png')
    plt.show()




def vizualizeFibonacciSpiral(N=15):
    """ generates Fibonacci sequence and spiral
    """
    seqFibo = generateFibonacci(N)
    print ("Fibonacci sequence [{0}]: \n{1}".format(N, seqFibo))

    # Get the spirals
    from utils.geo_utils import getSpiralFibonacci
    spirals = getSpiralFibonacci(seqFibo)

    # Plot the spirals
    fig = plt.figure()
    ax = fig.add_subplot(111)  
    Ncolors = 10; colors=[]
    for j in range(N):
        colors.append((j % Ncolors) * 5) # choose a color
        collection = PatchCollection(spirals, cmap=matplotlib.cm.jet, alpha=0.05)
        collection.set_array(np.array(colors))
        # add the spiral to collection
        ax.add_collection(collection)

    plt.axis('equal')
    plt.savefig('data/Fibo_spiral_rect.png')
    plt.show()




N=35
vizualizeFibonacciSpiral(N)

#N=100
#vizualizeGoldenRatioSpiral(N)





