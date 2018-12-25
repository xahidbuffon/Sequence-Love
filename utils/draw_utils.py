#!/usr/bin/env python
"""
@author: Jahid 
@email: islam034@umn.edu

Utility functions for drawing objects
"""
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.artist import Artist
from matplotlib.patches import Polygon

class DrawPolygon(object):
    """ For drawing a polygon with vertices
    """
    def __init__(self, ax, poly):
        assert (poly.figure is not None), "polygon not found"
        self.ax = ax
        canvas = poly.figure.canvas
        self.poly = poly
        x, y = zip(*self.poly.xy)
        self.line = Line2D(x, y, marker='o',markerfacecolor='r', linewidth=2)
        self.ax.add_line(self.line)
        canvas.mpl_connect('draw_event', self.draw_callback)
        self.canvas = canvas

    def draw_callback(self, event):
        #self.background = self.canvas.copy_from_bbox(self.ax.bbox)
        self.ax.draw_artist(self.poly)
        self.ax.draw_artist(self.line)



