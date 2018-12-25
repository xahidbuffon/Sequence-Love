#!/usr/bin/env python
"""
@author: Jahid 
@email: islam034@umn.edu

Utility functions for geometric computations
"""
from __future__ import division
import numpy as np

def get_line_pts2d(p0, p1, n):
    """ get n interpolated points between o0, p1
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
        
