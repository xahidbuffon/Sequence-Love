#!/usr/bin/env python
"""
@author: Jahid 
@email: islam034@umn.edu

visualizer for Polygon sequence
"""
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
# local library
from utils.draw_utils import DrawPolygon
from utils.geo_utils import get_line_pts2d


def generatePentagon(N=5):
    """ generates first N numbers in Polygon sequence
    """
    assert (N>0), "N must be a positive integer"
    seq = []
    for i in range(1, N+1):
        Pi = 0.5* (3 * (i**2) - i) #p[i]=(3i**2-i)/2
        seq.append(int(Pi))
    return seq



def getPentagons(N):
    """ generates N polygons corresponding to the Polygon sequence
    """
    c45, s45 = np.cos(45), np.sin(45)
    polys = []  
    for i in xrange(1, N):
        # counter clock-wise pts po-p1-p2-p3-p4
        loop_corners = [[0, 0], [i, 0], 
                        [i+i*c45, i*s45], [i*c45, i+i*s45], 
                        [0, i], [0, 0]] 
        poly = []
        for j in xrange(5):
            pts_ = get_line_pts2d(loop_corners[j], loop_corners[j+1], i+1)
            for p in pts_:
                if p not in poly:   
                    poly.append(p)
        poly_ar = np.array(poly).reshape(-1, 2)
        polys.append(Polygon(poly_ar, True, alpha=0.01))
    return polys


def vizualizePentagon(N=5):
    """ generates arcs for first N numbers in Polygon sequence
    """
    # get the sequence 
    seqPolygon = generatePentagon(N)
    print ("Polygon sequence [{0}]: \n{1}".format(N, seqPolygon))
    # get the polygons
    all_polys = getPentagons(N)
    # draw the polygons
    fig, ax = plt.subplots()
    for poly in all_polys:
        ax.add_patch(poly)
        DrawPolygon(ax, poly)

    ax.set_xlim((-1, N*2))
    ax.set_ylim((-1, N*2))
    plt.savefig('data/Pentagon_viz.png')
    plt.show()


N=8
vizualizePentagon(N)





