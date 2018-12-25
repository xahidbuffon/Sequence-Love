#!/usr/bin/env python
"""
@author: Jahid 
@email: islam034@umn.edu

visualizer for Prime sequence
"""

from __future__ import division
import numpy as np
import matplotlib.cm as cm
from matplotlib import pyplot as plt


def generatePrime(N=32):
    """ generates first N Prime numbers
    """
    assert (N>0), "N must be a positive integer"
    from math import sqrt
    isPrime = [True]*N
    for i in xrange(2, int(sqrt(N))+1):
        if isPrime[i]:
            for j in xrange(i*i, N, i):
                isPrime[j] = False
    seq = [i for i in xrange(2, N) if isPrime[i]]
    return seq


def getUlamSpiral(isPrime_sq):
    """ generates Ulam spiral
        ref: https://en.wikipedia.org/wiki/Ulam_spiral
    """
    nrows, ncols= isPrime_sq.shape
    idx = np.arange(nrows*ncols).reshape(nrows,ncols)[::-1]
    spiral_idx = []
    while idx.size:
        spiral_idx.append(idx[0])
        idx = idx[1:] # remove the first row 
        idx = idx.T[::-1] # rotate the rest anticlockwise
    spiral_idx = np.hstack(spiral_idx)    # flat array of indices
    spiral_Ulam = np.empty_like(isPrime_sq) # flattened version of target array
    spiral_Ulam.flat[spiral_idx] = isPrime_sq.flat[::-1]
    return spiral_Ulam


def vizPrimePattern(N=32):
    """ visualizes first N*N Prime numbers
    """
    seqPrime = generatePrime(N*N)
    all_primes = np.array(seqPrime)
    # Boolean array: True for prime
    isPrime = np.zeros(N*N)
    isPrime[all_primes-1] = True
    # Spiral (clockwise)
    spiral_Ulam = getUlamSpiral(isPrime.reshape((N, N)))
    # plot
    plt.matshow(spiral_Ulam, cmap=cm.binary) #cmap=cm.summer
    plt.axis('off')
    plt.savefig('data/Prime_viz.png')
    plt.show()



N = 128  # side of the square N*N primes
vizPrimePattern(N)







