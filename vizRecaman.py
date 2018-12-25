#!/usr/bin/env python
"""
@author: Jahid 
@email: islam034@umn.edu

visialier for Recaman sequence
"""

from __future__ import division
from matplotlib import pyplot as plt
from matplotlib import patches as pat

# for colored arcs
colors=['blue', 'red', 'green', 'orange', 'pink', 'cyan', 'magenta', 'yellow']

def generateRecaman(N=50):
    """ generates first N numbers in Recaman sequence
    """
    seqRecaman = [0]
    for i in range(1, N):
        if (seqRecaman[-1] - i in seqRecaman) or (seqRecaman[-1] - i < 0):
            seqRecaman.append(seqRecaman[-1] + i)
        else:
            seqRecaman.append(seqRecaman[-1] - i)
    return seqRecaman


def getColor(i, colored=False):
    """ for colored arcs
    """
    global colors
    if not colored: return 'black'
    else:  return colors[i%8]
    


def vizualizeRecaman(N=50, colored=False):
    """ generates arcs for first N numbers in Recaman sequence
    """
    # get the sequence 
    seqRecaman = generateRecaman(N)
    print ("Recaman sequence [{0}]: \n{1}".format(N, seqRecaman))
    # plot arcs for each number
    fig = plt.figure()
    ax = fig.add_subplot(111)
    for i in range(len(seqRecaman) - 1):
        new_patch = pat.Arc((0.5*(seqRecaman[i] + seqRecaman[i+1]), 0), 
                             abs(seqRecaman[i+1] - seqRecaman[i]), 
                             abs(seqRecaman[i+1] - seqRecaman[i]), 
                             (((-1)**(i+1)+1)*0.5)*180, 
                             180, 
                             color=getColor(i, colored),
                             linewidth=1.1)
        ax.add_patch(new_patch)
    canvas_scale = 1.1
    ax.set_xlim(-(canvas_scale-1)*max(seqRecaman), canvas_scale*max(seqRecaman))
    ax.set_ylim(-0.6*canvas_scale*N, 0.6*canvas_scale*N)
    ax.set_aspect('equal')
    plt.savefig('data/Recaman_viz.png')
    plt.show()



N=400
vizualizeRecaman(N, colored=True)





