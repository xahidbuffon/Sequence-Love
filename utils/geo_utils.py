#!/usr/bin/env python
"""
@author: Jahid 
@email: islam034@umn.edu

Utility functions for geometric computations
"""
from __future__ import division
import numpy as np
import matplotlib.patches as mpatches


def get_line_pts2d(p0, p1, n):
    """ get n interpolated points between p0, p1
    """
    x1, y1 = p0
    x2, y2 = p1 
    if (x1==x2 and y1==y2):    return []
    if x1==x2:    return [[x1, i] for i in np.linspace(y1, y2, n)]
    if y1==y2:    return [[i, y1] for i in np.linspace(x1, x2, n)]
    # bad slopes avoided, now interpolate
    D = (x1-x2)
    slope = (y1-y2)/D
    Xs = np.linspace(x1, x2, n)
    # uses (y-y1)/(y1-x2)=(x-x1)/(x1-x2)
    pts = []
    for i in xrange(n):
        ys = slope*(Xs[i]-x1) + y1
        pts.append([Xs[i], ys])

    return pts
        



def getSpiralGoldenRatio(N=200):
    """ Finds patches of spirals based on golden ratio
    """
    cx = cy = 0.5 # centre of spiral
    spacing = 0.1 # inter-spiral

    golden_ratio = (1 + 5**0.5) / 2.0 # approx = 1.618
    delta = (2 - golden_ratio) * 2 * np.pi + spacing

    scale = 0.1
    leaf_rad= scale * (1 + 5**0.5)/4.0 # radius of each leaf
    theta=0; min_y = max_y = 0;

    # collect list of spirals
    patches = []
    for i in xrange(1, N+1):
        r = scale * i **0.5
        theta += delta
        x = cx + r*np.cos(theta)
        y = cy + r*np.sin(theta)
        if   y > max_y: max_y = y
        elif y < min_y: min_y = y
        leaf = mpatches.Circle((x, y), leaf_rad)
        patches.append(leaf)

    return patches




def getSpiralFibonacci(seqFibo):
    """ Finds patches of spirals based on the given Fibonacci sequence
    """
    c = xy = np.array([0, 0])
    t = np.array([270, 0]) 

    i=1; patches = []
    for j in xrange(1, len(seqFibo)):
        t += 90
        if i==5: 
            i = 1
        if i==1:
            xy = xy + [-seqFibo[j-2], seqFibo[j-1]]
            c  = c  + [-seqFibo[j-2],  0      ]
        if i==2:
            xy = xy + [ -seqFibo[j], -seqFibo[j-2]]     
            c  =  c + [     0 ,     -seqFibo[j-2]]
        elif i==3:
            xy = xy + [   0,        -seqFibo[j]  ]    
            c  = c  + [seqFibo[j-2],     0       ]
        elif i==4:
            xy = xy + [ seqFibo[j-1],      0     ]   
            c  = c  + [   0,       seqFibo[j-2]  ]
        else: pass

        # The spiral and the rectangle
        rect = mpatches.Wedge([c[0], c[1]], seqFibo[j], t[0], t[1])
        patches.append(rect)
        rect = mpatches.Rectangle([xy[0], xy[1]], seqFibo[j], seqFibo[j])
        patches.append(rect)
        i+=1

    return patches





