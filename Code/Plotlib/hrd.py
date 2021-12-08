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
    Creates Hertzsprung Russel diagram

    Input:
    model : mesaplot model
    """

    TITLE = f"Hertzsprung-Russel diagram {model.hist.data['star_mass'][0]}" + "M$_{\odot}$"
    X_LABEL = 'log (T$_{\mathregular{eff}}$) [K]'
    Y_LABEL = 'log (L / L$_{\odot}$)'  
    CMAP = plt.get_cmap('cool')  

    # Make figure
    fig, ax = set_fig(TITLE, X_LABEL, Y_LABEL)
    
    # Whole track
    x = model.hist.data['log_Teff']
    y = model.hist.data['log_L']

    # Main sequence
    row_start, row_end = get_main_sequence(model)
    age = model.hist.data['star_age'] / 1000000 # Convert to mega year
    line = set_grad_line(ax, x[row_start:row_end], y[row_start:row_end], age[row_start:row_end], CMAP)

    # Pre main sequence
    ax.plot(
        x[0:row_start], 
        y[0:row_start], 
        lw=2, 
        color='k', 
        alpha=0.2,
        label="Pre main sequence")

    # Colorbar
    cbar = fig.colorbar(
        line,
        cmap=CMAP,
        ax=ax)
    cbar.set_label('Age [Myr]') 

    # Legend
    ax.legend(shadow=False, edgecolor='white', fancybox=False) 

    # Axis limits
    MARGIN = 0.1
    size_x = max(x) - min(x)
    size_y = max(y) - min(y)
    ax.set_xlim(max(x) + MARGIN*size_x, min(x) - MARGIN*size_x)
    ax.set_ylim(min(y) - MARGIN*size_y, max(y) + MARGIN*size_y)

    # Show plot
    fig.tight_layout()
    plt.show()

    # Save
    if save:
        plt.savefig(f"Output/hrd_{model.hist.data['star_mass'][0]}M", dpi=200)


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
    lc.set_linewidth(3)

    # Add linesegments to axis
    line = ax.add_collection(lc)

    return line
