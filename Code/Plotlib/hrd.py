# hrd.py
#
# Functions for making a Hertzsprung Russel diagram
#
# Freek Temming and Simon van Eeden

from .plotfunctions import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

SIGMA = 5.67051 * pow(10,-5)
R_SUN = 6.957 * pow(10,10)
L_SUN = 3.828 * pow(10,33)

def plot(model, save=False):
    """
    Creates Hertzsprung Russel diagram with annotations of different phases

    Input:
    model : mesaplot model
    """

    TITLE = f"Hertzsprung-Russel diagram {model.hist.data['star_mass'][0]}" + "M$_{\odot}$"
    X_LABEL = 'log (T$_{\mathregular{eff}}$) [K]'
    Y_LABEL = 'log (L / L$_{\odot}$)'   
    CMAP = plt.get_cmap('plasma').reversed() 

    # Make figure
    fig, ax = set_fig(TITLE, X_LABEL, Y_LABEL)
    
    # Whole track
    x = model.hist.data['log_Teff']
    y = model.hist.data['log_L']

    # Gradient from main sequence
    row_start, row_end = get_main_sequence(model)
    age = model.hist.data['star_age'] / 1000000 # Convert to mega year
    line = set_grad_line(ax, x[row_start:-1], y[row_start:-1], age[row_start:-1], CMAP)

    # Pre main sequence
    ax.plot(
        x[0:row_start+1], 
        y[0:row_start+1], 
        lw=1, 
        color='k', 
        alpha=0.2,
        label="Pre main sequence")

    # Annotations
    set_annotations(ax, model)

    # Colorbar
    cbar = fig.colorbar(
        line,
        cmap=CMAP,
        ax=ax)
    cbar.set_label('Age [Myr]') 

    # Legend
    ax.legend(shadow=False, edgecolor='white', fancybox=False, fontsize="small", facecolor='none')

    # Axis limits
    MARGIN = 0.08
    size_x = max(x) - min(x)
    size_y = max(y) - min(y)
    ax.set_xlim(max(x) + MARGIN*size_x, min(x) - MARGIN*size_x)
    ax.set_ylim(min(y) - MARGIN*size_y, max(y) + MARGIN*size_y)

    fig.tight_layout()

    # Save
    if save:
        plt.savefig(f"../Output/hrd_{model.hist.data['star_mass'][0]}M.png", dpi=200)

    # Show plot
    plt.show()


def set_grad_line(ax, x, y, cmap_vals, cmap):
    """
    Plot gradient line
    """

    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(
            segments, 
            cmap=cmap,
            norm=plt.Normalize(min(cmap_vals), max(cmap_vals)))

    # Assign each line segment to a color
    lc.set_array(cmap_vals)

    # Set line widht
    lc.set_linewidth(1)

    # Add linesegments to axis
    line = ax.add_collection(lc)

    return line


def set_annotations(ax, model):

    x = model.hist.data['log_Teff']
    y = model.hist.data['log_L']

    # Start of main sequence
    row_start, row_end = get_main_sequence(model)
    ax.plot(x[row_start], y[row_start], 'ko', ms=3)
    ax.annotate(
        'a', 
        (x[row_start+1], y[row_start+1]),
        horizontalalignment='right', 
        verticalalignment='top')

    # End of main sequence
    ax.plot(4.186, 3.242, 'ko', ms=3)
    ax.annotate(
        'b', 
        (4.186 - 0.01, 3.242),
        horizontalalignment='left', 
        verticalalignment='top')

    # H_shell burning
    ax.plot(4.2264, 3.307, 'ko', ms=3)
    ax.annotate(
        'c', 
        (4.2264, 3.307),
        horizontalalignment='right', 
        verticalalignment='bottom')    

    # The location where the star starts to ascend the giant branch
    ax.plot(3.686, 2.861, 'ko', ms=3)
    ax.annotate(
        'd', 
        (3.686, 2.861 - 0.02),
        horizontalalignment='center', 
        verticalalignment='top')   

    # Central ignition of helium burning
    ax.plot(3.622, 3.360, 'ko', ms=3)
    ax.annotate(
        'e', 
        (3.622, 3.360),
        horizontalalignment='right', 
        verticalalignment='bottom')

    #  The location where the star spends most of the time helium burning
    ax.plot(3.658, 3.102, 'ko', ms=3)
    ax.annotate(
        'f', 
        (3.658, 3.102 - 0.03),
        horizontalalignment='right', 
        verticalalignment='top')    

    # Central exhaustion of helium
    ax.plot(x[-1], y[-1], 'ko', ms=3)
    ax.annotate(
        'g', 
        (x[-1], y[-1]+0.05),
        horizontalalignment='center', 
        verticalalignment='bottom')   
