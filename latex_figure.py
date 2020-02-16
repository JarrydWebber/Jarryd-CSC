#!/usr/bin/env python
# coding: utf-8

# In[3]:


import matplotlib.pyplot as plt
import numpy
from matplotlib import rc


# In[4]:


rc("text", usetex=True)
rc("font", family="serif")

# These figure sizes should correspond with the size in the LaTeX document.
# don't change the font size to compensate for scaling the figure down
aspect_ratio = 4 / 5
FULLSIZE = 5, 5 * aspect_ratio
HALFSIZE = 3, 3 * aspect_ratio


# In[6]:


def samplefigure(xs, ys, YNAMES, LINETYPES, figsize, ylabel, xlabel, legend=True):
    """
    Generate the sample figure

    x: x values for data
    ys: iterable of y values
    figsize: size of the figure in inches (width, height)
    ylabel: What the y label should be
    legend: Add a legend?
    """

    fig, ax = plt.subplots(1, 1, figsize=figsize)

    for x, y, linetype, label in zip(xs, ys, LINETYPES, YNAMES):
        ax.plot(x, y, linetype, label=label)

    ax.set_xlabel(xlabel)
    ax.set_ylabel(ylabel)

    if legend:
        ax.legend()

    # This ensures the bounding box is correct. If we don't call tight_layout
    # sometimes elements get cut off on the edges.
    plt.tight_layout()


# In[ ]:


def plotfigure(x, ys, YNAMES, LINETYPES, xlabel, ylabel,figsize, filename, diff=False, legend=True):

    samplefigure(x, ys, YNAMES, LINETYPES, figsize, ylabel, xlabel, legend)
    plt.savefig(filename.format(diff="model"))

#     if diff:
#         diffys = [numpy.gradient(y, x) for y in ys]
#         samplefigure(x, diffys, figsize, r"Velocity / m$\cdot$s$^{-1}$", "Time /s", legend)
#         plt.savefig(filename.format(diff="derivative", noise_factor=noise_factor))

