# dens_temp.py
#
# Functions for making a density temperature plot
#
# Freek Temming and Simon van Eeden 

from .plotfunctions import *
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.collections import LineCollection

RHO_SUN = 1.41
T_SUN = 5778

def plot(model, save=False):
    """
    Creates density temperature plot

    Input:
    model : mesaplot model
    """

    TITLE = f"Central density vs central temperature {model.hist.data['star_mass'][0]}" + "M$_{\odot}$"
    X_LABEL = 'log (rho / rho$_{\odot}$)'
    Y_LABEL = 'log (T / T$_{\odot}$)'  
    CMAP = plt.get_cmap('cool')  

    # Make figure
    fig, ax = set_fig(TITLE, X_LABEL, Y_LABEL)

    # Gradient line
    row_start, row_end = get_main_sequence(model)
    x = model.hist.data['log_cntr_Rho'][row_start:row_end]
    y = model.hist.data['log_cntr_T'][row_start:row_end]
    age = model.hist.data['star_age'][row_start:row_end]
    line = set_grad_line(ax, x, y, age, CMAP)

    # Gas fase regions
    set_eos_regimes(ax)

    # Colorbar
    cbar = fig.colorbar(
        line,
        cmap=CMAP,
        ax=ax)
    cbar.set_label('Age [Myr]')

    # Set margins around figure
    ax.margins(0.2, 0.2)

    # Show plot
    fig.tight_layout()
    plt.show()

    # Save
    if save:
        plt.savefig(f"Output/dens_temp_{model.hist.data['star_mass'][0]}M", dpi=200)


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


def set_eos_regimes(ax):
    """
    Plot equation of state regimes
    """

    pass
